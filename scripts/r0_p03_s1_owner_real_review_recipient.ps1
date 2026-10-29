#Requires -Version 5.1
<#
Owner-side S1 reviewer-only CMS recipient. NOT a test-only key reuse.
Real-source review output remains restricted to the owner-held encrypted
recipient and must not be pasted into this public coordinator conversation.
Prepare creates a new password-encrypted key and public certificate locally.
Receive stores only exact ciphertext plus a safe private receipt.
Verify independently repeats full GCM/canonical 10-record readback.

Do not execute Prepare/Receive/Verify through a coordinator, Runtime Bridge,
source reviewer, challenger or future blind-author interface. Ordinary user
session ACL is not a different security principal from other same-SID processes.
Actual reviewer/challenger admission and batch disclosure are separately gated.
#>
[CmdletBinding()]
param(
    [ValidateSet("SelfTest","Prepare","Receive","Verify")]
    [string]$Action="SelfTest",
    [ValidatePattern('^[0-9a-f]{32}$')]
    [string]$RecipientId,
    [string]$Ciphertext,
    [ValidatePattern('^[0-9a-fA-F]{64}$')]
    [string]$ExpectedSha256
)
Set-StrictMode -Version Latest
$ErrorActionPreference="Stop"
$OwnerPrefix="ADS-R0-P03-S1-REAL-REVIEW-"
$PrivateName="owner-review-encrypted-key.pem"
$CertName="owner-review-public-cert.pem"
$CipherName="R0_P03_S1_WAVE0_OWNER_REVIEW.cms"
$ReceiptName="owner-review-receipt.json"
$OpenSsl="C:\Program Files\Git\usr\bin\openssl.exe"
$Repo=Split-Path -Parent $PSScriptRoot
$Python=Join-Path $Repo ".venv\Scripts\python.exe"
$Reader=Join-Path $Repo "experiments\r0_p03_navigation_probe\s1_source_status_protected_route.py"
$WaveZip=Join-Path $Repo ".venv\.r0_p03_source_status_wave0\R0_P03_SOURCE_STATUS_FIRST_WAVE_REVIEW_ONLY.zip"
$WaveSha="c90c2d7120ffd32657e6506f876acd10e9779dc968ba9da8fb7f12604aa58387"
$Downloads=Join-Path $env:USERPROFILE "Downloads"

function Fail([string]$Reason) {
    [Console]::Error.WriteLine("S1_REAL_REVIEW_OWNER_HOLD=$Reason")
    exit 2
}
function Require-File([string]$Path,[string]$Reason) {
    if (-not [IO.File]::Exists($Path) -or
        (([IO.File]::GetAttributes($Path) -band [IO.FileAttributes]::ReparsePoint) -ne 0)) {
        Fail $Reason
    }
}
function Owner-Directory([string]$Id) {
    if ($Id -notmatch '^[0-9a-f]{32}$' -or -not $env:LOCALAPPDATA) {
        Fail "OWNER_RECIPIENT_ID_INVALID"
    }
    return (Join-Path $env:LOCALAPPDATA ($OwnerPrefix+$Id))
}
function Check-OwnerAcl([string]$Folder) {
    if (-not [IO.Directory]::Exists($Folder) -or
        (([IO.File]::GetAttributes($Folder) -band [IO.FileAttributes]::ReparsePoint) -ne 0)) {
        Fail "OWNER_FOLDER_INVALID"
    }
    $acl=Get-Acl -LiteralPath $Folder
    if (-not $acl.AreAccessRulesProtected) { Fail "OWNER_ACL_NOT_PROTECTED" }
    $me=[Security.Principal.WindowsIdentity]::GetCurrent().User.Value
    $rules=@($acl.GetAccessRules($true,$true,[Security.Principal.SecurityIdentifier]))
    $ids=@($rules | ForEach-Object { $_.IdentityReference.Value })
    if ($me -notin $ids -or "S-1-5-18" -notin $ids) { Fail "OWNER_ACL_PRINCIPALS_MISSING" }
    foreach($ace in $rules) {
        if ($ace.IdentityReference.Value -notin @($me,"S-1-5-18") -or
            $ace.AccessControlType -ne [Security.AccessControl.AccessControlType]::Allow) {
            Fail "OWNER_ACL_UNEXPECTED_PRINCIPAL"
        }
    }
}
function Check-Key([string]$Path) {
    Require-File $Path "OWNER_KEY_MISSING"
    $f=[IO.File]::ReadAllText($Path)
    if (-not $f.StartsWith("-----BEGIN ENCRYPTED PRIVATE KEY-----")) {
        Fail "OWNER_KEY_NOT_ENCRYPTED_AT_REST"
    }
}
function Verify-Batch {
    Require-File $WaveZip "OWNER_WAVE_ZIP_MISSING"
    $sha=(Get-FileHash -LiteralPath $WaveZip -Algorithm SHA256).Hash.ToLowerInvariant()
    if ($sha -cne $WaveSha) { Fail "OWNER_WAVE_ZIP_INTEGRITY_INVALID" }
}
function Readback([string]$Folder,[string]$Sha) {
    Check-OwnerAcl $Folder
    Verify-Batch
    $key=Join-Path $Folder $PrivateName
    $cert=Join-Path $Folder $CertName
    $cipher=Join-Path $Folder $CipherName
    Check-Key $key
    Require-File $cert "OWNER_CERT_MISSING"
    Require-File $cipher "OWNER_CIPHERTEXT_MISSING"
    $saved=(Get-FileHash -LiteralPath $cipher -Algorithm SHA256).Hash.ToLowerInvariant()
    if ($saved -cne $Sha.ToLowerInvariant()) { Fail "OWNER_CIPHERTEXT_HASH_MISMATCH" }
    $args=@($Reader,"owner-verify","--batch-zip",$WaveZip,
        "--public-cert",$cert,"--private-key",$key,
        "--ciphertext",$cipher,"--expected-ciphertext-sha256",$saved,
        "--openssl",$OpenSsl)
    $old=$ErrorActionPreference
    try {
        $ErrorActionPreference="Continue"
        & $Python @args
        $rc=$LASTEXITCODE
    } finally { $ErrorActionPreference=$old }
    if ($rc -ne 0) { Fail "OWNER_FULL_READBACK_FAILED" }
    Write-Output "S1_REAL_REVIEW_OWNER_FULL_READBACK=PASS"
}
foreach($p in @($OpenSsl,$Python,$Reader)) { Require-File $p "OWNER_PREREQUISITE_MISSING" }
Verify-Batch
if ($Action -eq "SelfTest") {
    if ($RecipientId -or $Ciphertext -or $ExpectedSha256) { Fail "SELFTEST_ARGS_INVALID" }
    Write-Output "S1_REAL_REVIEW_OWNER_PREFLIGHT=PASS"
    Write-Output "S1_REAL_REVIEW_OWNER_KEYS_CREATED=NO"
    return
}
if (-not [Environment]::UserInteractive) { Fail "OWNER_INTERACTIVE_REQUIRED" }
if (-not [IO.Directory]::Exists($Downloads)) { Fail "OWNER_DOWNLOADS_MISSING" }
if ($Action -eq "Prepare") {
    if ($RecipientId -or $Ciphertext -or $ExpectedSha256) { Fail "PREPARE_ARGS_INVALID" }
    $id=[guid]::NewGuid().ToString("N")
    $folder=Owner-Directory $id
    if ([IO.File]::Exists($folder) -or [IO.Directory]::Exists($folder)) { Fail "OWNER_FOLDER_EXISTS" }
    $user=[Security.Principal.WindowsIdentity]::GetCurrent().User
    $acl=[Security.AccessControl.DirectorySecurity]::new()
    $acl.SetAccessRuleProtection($true,$false)
    $flags=[Security.AccessControl.InheritanceFlags]::ObjectInherit -bor
        [Security.AccessControl.InheritanceFlags]::ContainerInherit
    foreach($who in @($user,[Security.Principal.SecurityIdentifier]::new("S-1-5-18"))) {
        $acl.AddAccessRule([Security.AccessControl.FileSystemAccessRule]::new(
            $who,[Security.AccessControl.FileSystemRights]::FullControl,
            $flags,[Security.AccessControl.PropagationFlags]::None,
            [Security.AccessControl.AccessControlType]::Allow))
    }
    [IO.Directory]::CreateDirectory($folder,$acl) | Out-Null
    Check-OwnerAcl $folder
    $key=Join-Path $folder $PrivateName
    $cert=Join-Path $folder $CertName
    $public=Join-Path $Downloads ("S1_REAL_REVIEW_OWNER_PUBLIC_"+$id+".pem")
    if ([IO.File]::Exists($public)) { Fail "PUBLIC_CERT_ALREADY_PRESENT" }
    Write-Output "Owner creates a NEW distinct real-review encrypted private key."
    Write-Output "Enter the key passphrase only into this local OpenSSL prompt."
    $old=$ErrorActionPreference
    try {
        $ErrorActionPreference="Continue"
        & $OpenSsl req -new -x509 -newkey rsa:2048 -keyout $key -out $cert -subj "/CN=ADS-R0-P03-S1-REVIEW-OWNER" -days 30
        $rc=$LASTEXITCODE
    } finally { $ErrorActionPreference=$old }
    if ($rc -ne 0) { Fail "OWNER_KEY_GENERATION_FAILED" }
    Check-Key $key
    Require-File $cert "OWNER_CERT_NOT_CREATED"
    $bytes=[IO.File]::ReadAllBytes($cert)
    if ($bytes.Length -gt 10000 -or
        -not [Text.Encoding]::ASCII.GetString($bytes).StartsWith("-----BEGIN CERTIFICATE-----")) {
        Fail "OWNER_CERT_FORMAT_INVALID"
    }
    $stream=[IO.FileStream]::new($public,[IO.FileMode]::CreateNew,
        [IO.FileAccess]::Write,[IO.FileShare]::None)
    try { $stream.Write($bytes,0,$bytes.Length);$stream.Flush($true) }
    finally { $stream.Dispose() }
    Write-Output "S1_REAL_REVIEW_OWNER_RECIPIENT_PREPARED=PASS"
    Write-Output ("S1_REAL_REVIEW_OWNER_PUBLIC_CERT_PATH="+$public)
    Write-Output ("S1_REAL_REVIEW_OWNER_PUBLIC_CERT_SHA256="+
        (Get-FileHash -LiteralPath $public -Algorithm SHA256).Hash.ToLowerInvariant())
    Write-Output ("S1_REAL_REVIEW_OWNER_RECIPIENT_ID="+$id)
    Write-Output "S1_REAL_REVIEW_OWNER_PRIVATE_KEY_ENCRYPTED=TRUE"
    Write-Output "S1_REAL_REVIEW_CUSTODY_EXCLUSION_PROVEN=FALSE"
    return
}
if (-not $RecipientId) { Fail "OWNER_RECIPIENT_ID_REQUIRED" }
$folder=Owner-Directory $RecipientId
Check-OwnerAcl $folder
if ($Action -eq "Receive") {
    if (-not $Ciphertext -or -not $ExpectedSha256) { Fail "RECEIVE_ARGS_MISSING" }
    $source=[IO.Path]::GetFullPath($Ciphertext)
    Require-File $source "RECEIVED_CIPHERTEXT_MISSING"
    if ([IO.Path]::GetFileName($source) -cne $CipherName) { Fail "CIPHERTEXT_NAME_INVALID" }
    $bytes=[IO.File]::ReadAllBytes($source)
    if ($bytes.Length -lt 100 -or $bytes.Length -gt 400000) { Fail "CIPHERTEXT_SIZE_INVALID" }
    $digest=(Get-FileHash -LiteralPath $source -Algorithm SHA256).Hash.ToLowerInvariant()
    if ($digest -cne $ExpectedSha256.ToLowerInvariant()) { Fail "CIPHERTEXT_DIGEST_INVALID" }
    $stored=Join-Path $folder $CipherName
    $receipt=Join-Path $folder $ReceiptName
    if ([IO.File]::Exists($stored) -or [IO.File]::Exists($receipt)) { Fail "OWNER_VERSION_ALREADY_PRESENT" }
    [IO.File]::Copy($source,$stored,$false)
    if ((Get-FileHash -LiteralPath $stored -Algorithm SHA256).Hash.ToLowerInvariant() -cne $digest) {
        Fail "STORED_CIPHERTEXT_MISMATCH"
    }
    $record=@{format="ads-r0-p03-s1-owner-review-receipt-v1";
        batch_zip_sha256=$WaveSha;ciphertext_file=$CipherName;ciphertext_sha256=$digest}
    [IO.File]::WriteAllText($receipt,($record|ConvertTo-Json -Compress)+[Environment]::NewLine,
        [Text.UTF8Encoding]::new($false))
    Readback $folder $digest
    Write-Output "S1_REAL_REVIEW_OWNER_RECEIVE=PASS"
    return
}
if ($Action -eq "Verify") {
    if ($Ciphertext -or $ExpectedSha256) { Fail "VERIFY_ARGS_INVALID" }
    $receipt=Join-Path $folder $ReceiptName
    Require-File $receipt "OWNER_RECEIPT_MISSING"
    try { $saved=Get-Content -LiteralPath $receipt -Raw -Encoding UTF8 | ConvertFrom-Json }
    catch { Fail "OWNER_RECEIPT_NOT_READABLE" }
    if ($saved.format -ne "ads-r0-p03-s1-owner-review-receipt-v1" -or
        $saved.batch_zip_sha256 -cne $WaveSha -or
        $saved.ciphertext_file -cne $CipherName -or
        $saved.ciphertext_sha256 -notmatch '^[0-9a-f]{64}$') {
        Fail "OWNER_RECEIPT_INVALID"
    }
    Readback $folder $saved.ciphertext_sha256
    Write-Output "S1_REAL_REVIEW_OWNER_RECHECK=PASS"
    return
}
Fail "OWNER_ACTION_INVALID"
