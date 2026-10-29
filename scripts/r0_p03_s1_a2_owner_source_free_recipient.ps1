#Requires -Version 5.1
<#
Source-free S1 A2 M1 owner-only recipient.
SelfTest: no mutation. Prepare: owner explicitly generates a fresh encrypted
TEST-ONLY private key and a public certificate using interactive OpenSSL.
Receive: owner authenticates the candidate's source-free CMS, stores the exact
ciphertext, and performs complete report readback without printing private data.
Verify: owner repeats that readback from saved bytes after a separate invocation.

Never execute Prepare, Receive or Verify from the coordinator/Runtime Bridge.
They require the owner's interactive desktop terminal. This does not create
another Windows account, qualify same-user process isolation, admit any reviewer,
or permit real historical-source material.
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

$OwnerPrefix="ADS-S1-A2-SOURCE-FREE-"
$PrivateName="owner-source-free-encrypted-key.pem"
$CertificateName="owner-source-free-public-cert.pem"
$CipherName="a2_candidate_protected_source_free_v1.cms"
$ReceiptName="owner-source-free-receipt.json"
$OpenSsl="C:\Program Files\Git\usr\bin\openssl.exe"
$Repo=Split-Path -Parent $PSScriptRoot
$Python=Join-Path $Repo ".venv\Scripts\python.exe"
$Reader=Join-Path $Repo "experiments\r0_p03_navigation_probe\s1_a2_candidate_protected_output_probe.py"
$Downloads=Join-Path $env:USERPROFILE "Downloads"

function Fail([string]$Reason) {
    [Console]::Error.WriteLine("S1_A2_OWNER_HOLD=$Reason")
    exit 2
}
function Require-OrdinaryFile([string]$Path,[string]$Reason) {
    if (-not [IO.File]::Exists($Path)) { Fail $Reason }
    if (([IO.File]::GetAttributes($Path) -band [IO.FileAttributes]::ReparsePoint) -ne 0) {
        Fail $Reason
    }
}
function Owner-Directory([string]$Id) {
    if ($Id -notmatch '^[0-9a-f]{32}$' -or -not $env:LOCALAPPDATA) {
        Fail "RECIPIENT_ID_INVALID"
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
    $found=@($acl.GetAccessRules($true,$true,[Security.Principal.SecurityIdentifier]))
    $names=@($found | ForEach-Object { $_.IdentityReference.Value })
    if ($me -notin $names -or "S-1-5-18" -notin $names) {
        Fail "OWNER_ACL_PRINCIPALS_INCOMPLETE"
    }
    foreach($ace in $found) {
        if ($ace.IdentityReference.Value -notin @($me,"S-1-5-18") -or
            $ace.AccessControlType -ne [Security.AccessControl.AccessControlType]::Allow) {
            Fail "OWNER_ACL_UNEXPECTED_PRINCIPAL"
        }
    }
}
function Check-EncryptedKey([string]$Key) {
    Require-OrdinaryFile $Key "OWNER_KEY_MISSING"
    $raw=[IO.File]::ReadAllText($Key)
    if (-not $raw.StartsWith("-----BEGIN ENCRYPTED PRIVATE KEY-----")) {
        Fail "OWNER_KEY_NOT_ENCRYPTED_AT_REST"
    }
}
function Readback([string]$Folder,[string]$Sha) {
    Check-OwnerAcl $Folder
    $key=Join-Path $Folder $PrivateName
    $cert=Join-Path $Folder $CertificateName
    $saved=Join-Path $Folder $CipherName
    Check-EncryptedKey $key
    Require-OrdinaryFile $cert "OWNER_CERT_MISSING"
    Require-OrdinaryFile $saved "OWNER_CIPHERTEXT_MISSING"
    $actual=(Get-FileHash -LiteralPath $saved -Algorithm SHA256).Hash.ToLowerInvariant()
    if ($actual -cne $Sha.ToLowerInvariant()) { Fail "OWNER_CIPHERTEXT_HASH_MISMATCH" }
    $args=@($Reader,"owner-verify","--ciphertext",$saved,
        "--recipient-public-cert",$cert,"--recipient-private-key",$key,
        "--expected-ciphertext-sha256",$actual,"--openssl",$OpenSsl)
    # Direct process invocation preserves the owner's interactive terminal.
    # The Python reader prompts locally; no key passphrase is an argv argument.
    $old=$ErrorActionPreference
    try {
        $ErrorActionPreference="Continue"
        & $Python @args
        $resultCode=$LASTEXITCODE
    }
    finally { $ErrorActionPreference=$old }
    if ($resultCode -ne 0) { Fail "OWNER_REPORT_READBACK_FAILED" }
    Write-Output "S1_A2_OWNER_SOURCE_FREE_COMPLETE_READBACK=PASS"
}
foreach($file in @($OpenSsl,$Python,$Reader)) {
    if (-not [IO.File]::Exists($file)) { Fail "OWNER_PREREQUISITE_MISSING" }
}
if (-not [IO.Directory]::Exists($Downloads)) { Fail "OWNER_DOWNLOADS_MISSING" }
if ($Action -eq "SelfTest") {
    if ($RecipientId -or $Ciphertext -or $ExpectedSha256) {
        Fail "SELFTEST_PARAMETERS_INVALID"
    }
    Write-Output "S1_A2_OWNER_SOURCE_FREE_PREFLIGHT=PASS"
    Write-Output "S1_A2_OWNER_KEYS_CREATED=NO"
    return
}
if (-not [Environment]::UserInteractive) { Fail "OWNER_INTERACTIVE_REQUIRED" }

if ($Action -eq "Prepare") {
    if ($RecipientId -or $Ciphertext -or $ExpectedSha256) {
        Fail "PREPARE_PARAMETERS_INVALID"
    }
    $id=[guid]::NewGuid().ToString("N")
    $folder=Owner-Directory $id
    if ([IO.Directory]::Exists($folder) -or [IO.File]::Exists($folder)) {
        Fail "OWNER_DIRECTORY_EXISTS"
    }
    $me=[Security.Principal.WindowsIdentity]::GetCurrent().User
    $dacl=[Security.AccessControl.DirectorySecurity]::new()
    $dacl.SetAccessRuleProtection($true,$false)
    $flags=[Security.AccessControl.InheritanceFlags]::ObjectInherit -bor
        [Security.AccessControl.InheritanceFlags]::ContainerInherit
    foreach($who in @($me,[Security.Principal.SecurityIdentifier]::new("S-1-5-18"))) {
        $rule=[Security.AccessControl.FileSystemAccessRule]::new(
            $who,[Security.AccessControl.FileSystemRights]::FullControl,
            $flags,[Security.AccessControl.PropagationFlags]::None,
            [Security.AccessControl.AccessControlType]::Allow)
        $dacl.AddAccessRule($rule)
    }
    [IO.Directory]::CreateDirectory($folder,$dacl) | Out-Null
    Check-OwnerAcl $folder
    $key=Join-Path $folder $PrivateName
    $cert=Join-Path $folder $CertificateName
    $public=Join-Path $Downloads ("S1_A2_SOURCE_FREE_OWNER_PUBLIC_"+$id+".pem")
    if ([IO.File]::Exists($public)) { Fail "PUBLIC_CERT_ALREADY_EXISTS" }
    Write-Output "Source-free test only. OpenSSL prompts locally for a NEW key passphrase."
    Write-Output "Never share the private key, its path, or the passphrase in ChatGPT."
    $old=$ErrorActionPreference
    try {
        $ErrorActionPreference="Continue"
        & $OpenSsl req -new -x509 -newkey rsa:2048 -keyout $key -out $cert -subj "/CN=ADS-S1-A2-SOURCE-FREE-OWNER" -days 7
        $resultCode=$LASTEXITCODE
    }
    finally { $ErrorActionPreference=$old }
    if ($resultCode -ne 0) { Fail "OWNER_INTERACTIVE_KEY_GENERATION_FAILED" }
    Check-EncryptedKey $key
    Require-OrdinaryFile $cert "OWNER_CERT_NOT_CREATED"
    $bytes=[IO.File]::ReadAllBytes($cert)
    if ($bytes.Length -gt 10000 -or
        -not [Text.Encoding]::ASCII.GetString($bytes).StartsWith("-----BEGIN CERTIFICATE-----")) {
        Fail "PUBLIC_CERT_FORMAT_INVALID"
    }
    $stream=[IO.FileStream]::new($public,[IO.FileMode]::CreateNew,
        [IO.FileAccess]::Write,[IO.FileShare]::None)
    try { $stream.Write($bytes,0,$bytes.Length);$stream.Flush($true) }
    finally { $stream.Dispose() }
    $sha=(Get-FileHash -LiteralPath $public -Algorithm SHA256).Hash.ToLowerInvariant()
    Write-Output "S1_A2_OWNER_SOURCE_FREE_RECIPIENT_PREPARED=PASS"
    Write-Output ("S1_A2_OWNER_PUBLIC_CERT_PATH="+$public)
    Write-Output ("S1_A2_OWNER_PUBLIC_CERT_SHA256="+$sha)
    Write-Output ("S1_A2_OWNER_RECIPIENT_ID="+$id)
    Write-Output "S1_A2_OWNER_PRIVATE_KEY_ENCRYPTED=TRUE"
    Write-Output "S1_A2_REAL_CUSTODY_QUALIFIED=FALSE"
    return
}
if (-not $RecipientId) { Fail "OWNER_RECIPIENT_ID_REQUIRED" }
$folder=Owner-Directory $RecipientId
Check-OwnerAcl $folder
if ($Action -eq "Receive") {
    if (-not $Ciphertext -or -not $ExpectedSha256) {
        Fail "RECEIVE_PARAMETERS_INVALID"
    }
    $source=[IO.Path]::GetFullPath($Ciphertext)
    Require-OrdinaryFile $source "RECEIVED_CIPHERTEXT_MISSING"
    if ([IO.Path]::GetFileName($source) -cne $CipherName) {
        Fail "RECEIVED_CIPHERTEXT_NAME_INVALID"
    }
    $bytes=[IO.File]::ReadAllBytes($source)
    if ($bytes.Length -lt 100 -or $bytes.Length -gt 32000) {
        Fail "RECEIVED_CIPHERTEXT_SIZE_INVALID"
    }
    $digest=(Get-FileHash -LiteralPath $source -Algorithm SHA256).Hash.ToLowerInvariant()
    if ($digest -cne $ExpectedSha256.ToLowerInvariant()) {
        Fail "RECEIVED_CIPHERTEXT_HASH_INVALID"
    }
    $stored=Join-Path $folder $CipherName
    $receipt=Join-Path $folder $ReceiptName
    if ([IO.File]::Exists($stored) -or [IO.File]::Exists($receipt)) {
        Fail "RECEIVED_CIPHERTEXT_VERSION_ALREADY_PRESENT"
    }
    [IO.File]::Copy($source,$stored,$false)
    if ((Get-FileHash -LiteralPath $stored -Algorithm SHA256).Hash.ToLowerInvariant() -cne $digest) {
        Fail "OWNER_STORED_BYTES_MISMATCH"
    }
    $record=@{format="ads-s1-a2-owner-source-free-receipt-v1";
        synthetic_only=$true;ciphertext_file=$CipherName;ciphertext_sha256=$digest}
    [IO.File]::WriteAllText($receipt,($record|ConvertTo-Json -Compress)+[Environment]::NewLine,
        [Text.UTF8Encoding]::new($false))
    Readback $folder $digest
    Write-Output "S1_A2_OWNER_SOURCE_FREE_RECEIVE=PASS"
    return
}
if ($Action -eq "Verify") {
    if ($Ciphertext -or $ExpectedSha256) { Fail "VERIFY_PARAMETERS_INVALID" }
    $receipt=Join-Path $folder $ReceiptName
    Require-OrdinaryFile $receipt "OWNER_RECEIPT_MISSING"
    try { $status=Get-Content -LiteralPath $receipt -Raw -Encoding UTF8|ConvertFrom-Json }
    catch { Fail "OWNER_RECEIPT_NOT_READABLE" }
    if ($status.format -ne "ads-s1-a2-owner-source-free-receipt-v1" -or
        $status.synthetic_only -ne $true -or $status.ciphertext_file -ne $CipherName -or
        $status.ciphertext_sha256 -notmatch '^[0-9a-f]{64}$') {
        Fail "OWNER_RECEIPT_INVALID"
    }
    Readback $folder $status.ciphertext_sha256
    Write-Output "S1_A2_OWNER_SOURCE_FREE_RECHECK=PASS"
    return
}
Fail "OWNER_ACTION_INVALID"
