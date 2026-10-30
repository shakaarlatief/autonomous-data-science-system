#Requires -Version 5.1
<#
Owner-only receipt and repeated authenticated readback of Wave0 second,
independent source-status assessment, before the first reviewer's private
findings are disclosed to the challenger candidate.

Reuse the ALREADY PREPARED real Wave0 owner key/certificate and recipient ID.
Never generate a new key here. Never run Receive/Verify through the exposed
Runtime Bridge, project coordinator, reviewer or challenger. This script does
not run the challenger session or certify genuine independent human identity.
#>
[CmdletBinding()]
param(
    [ValidateSet("SelfTest", "Receive", "Verify")]
    [string]$Action = "SelfTest",
    [ValidatePattern('^[0-9a-f]{32}$')]
    [string]$RecipientId,
    [string]$Ciphertext,
    [ValidatePattern('^[0-9a-fA-F]{64}$')]
    [string]$ExpectedSha256
)
Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"
$Repo = Split-Path -Parent $PSScriptRoot
$Python = Join-Path $Repo ".venv\Scripts\python.exe"
$OpenSsl = "C:\Program Files\Git\usr\bin\openssl.exe"
$Reader = Join-Path $Repo "experiments\r0_p03_navigation_probe\s1_wave0_independent_challenger_first_pass.py"
$Wave = Join-Path $Repo ".venv\.r0_p03_source_status_wave0\R0_P03_SOURCE_STATUS_FIRST_WAVE_REVIEW_ONLY.zip"
$WaveHash = "c90c2d7120ffd32657e6506f876acd10e9779dc968ba9da8fb7f12604aa58387"
$ExistingReviewerHash = "9194093b4a4b452b90638bf80eb491d0898c0a7330a77275be74ac9f4aa5a366"
$ReviewerName = "R0_P03_S1_WAVE0_OWNER_REVIEW.cms"
$ChallengerName = "R0_P03_S1_WAVE0_OWNER_CHALLENGER_FIRST_PASS.cms"
$ReceiptName = "owner-challenger-first-pass-receipt.json"

function Fail([string]$Code) {
    [Console]::Error.WriteLine("S1_WAVE0_CHALLENGER_OWNER_HOLD="+$Code)
    exit 2
}
function Require-File([string]$Path,[string]$Code) {
    if (-not [IO.File]::Exists($Path)) { Fail $Code }
    if (([IO.File]::GetAttributes($Path) -band [IO.FileAttributes]::ReparsePoint) -ne 0) {
        Fail $Code
    }
}
function Assert-Hash([string]$Path,[string]$Expected,[string]$Code) {
    Require-File $Path $Code
    $actual=(Get-FileHash -LiteralPath $Path -Algorithm SHA256).Hash.ToLowerInvariant()
    if ($actual -cne $Expected.ToLowerInvariant()) { Fail $Code }
}
foreach($f in @($Python,$Reader,$OpenSsl)) { Require-File $f "PREREQUISITE_MISSING" }
Assert-Hash $Wave $WaveHash "EXACT_WAVE0_SOURCE_ZIP_MISMATCH"

if ($Action -eq "SelfTest") {
    if ($RecipientId -or $Ciphertext -or $ExpectedSha256) {
        Fail "SELFTEST_ARGUMENTS_INVALID"
    }
    Write-Output "S1_WAVE0_CHALLENGER_OWNER_PREFLIGHT=PASS"
    Write-Output "S1_WAVE0_CHALLENGER_NEW_KEYS_CREATED=NO"
    return
}

if (-not [Environment]::UserInteractive) { Fail "OWNER_INTERACTIVE_REQUIRED" }
if (-not $RecipientId) { Fail "EXISTING_OWNER_RECIPIENT_ID_REQUIRED" }
if (-not $env:LOCALAPPDATA) { Fail "LOCAL_OWNER_DIRECTORY_UNAVAILABLE" }
$Folder=Join-Path $env:LOCALAPPDATA ("ADS-R0-P03-S1-REAL-REVIEW-"+$RecipientId)
if (-not [IO.Directory]::Exists($Folder) -or
    (([IO.File]::GetAttributes($Folder) -band [IO.FileAttributes]::ReparsePoint) -ne 0)) {
    Fail "EXISTING_OWNER_RECIPIENT_MISSING"
}
$acl=Get-Acl -LiteralPath $Folder
if (-not $acl.AreAccessRulesProtected) { Fail "OWNER_ACL_NOT_PROTECTED" }
$me=[Security.Principal.WindowsIdentity]::GetCurrent().User.Value
$rules=@($acl.GetAccessRules($true,$true,[Security.Principal.SecurityIdentifier]))
$principalIds=@($rules | ForEach-Object { $_.IdentityReference.Value })
if ($me -notin $principalIds -or "S-1-5-18" -notin $principalIds) {
    Fail "OWNER_ACL_PRINCIPALS_MISSING"
}
foreach($ace in $rules) {
    if ($ace.IdentityReference.Value -notin @($me,"S-1-5-18") -or
        $ace.AccessControlType -ne [Security.AccessControl.AccessControlType]::Allow) {
        Fail "OWNER_ACL_UNEXPECTED_PRINCIPAL"
    }
}
$Key=Join-Path $Folder "owner-review-encrypted-key.pem"
$Cert=Join-Path $Folder "owner-review-public-cert.pem"
$Original=Join-Path $Folder $ReviewerName
$Saved=Join-Path $Folder $ChallengerName
$Receipt=Join-Path $Folder $ReceiptName
Require-File $Key "OWNER_ENCRYPTED_KEY_MISSING"
Require-File $Cert "OWNER_PUBLIC_CERT_MISSING"
if (-not [IO.File]::ReadAllText($Key).StartsWith("-----BEGIN ENCRYPTED PRIVATE KEY-----")) {
    Fail "OWNER_PRIVATE_KEY_NOT_ENCRYPTED"
}
Assert-Hash $Original $ExistingReviewerHash "ORIGINAL_REVIEWER_CIPHERTEXT_MISMATCH"

function Readback([string]$Digest) {
    Assert-Hash $Saved $Digest "CHALLENGER_CIPHERTEXT_HASH_MISMATCH"
    $cmd=@($Reader,"owner-verify","--batch-zip",$Wave,
        "--public-cert",$Cert,"--private-key",$Key,
        "--ciphertext",$Saved,"--expected-ciphertext-sha256",$Digest,
        "--openssl",$OpenSsl)
    $prev=$ErrorActionPreference
    try {
        $ErrorActionPreference="Continue"
        & $Python @cmd
        $code=$LASTEXITCODE
    } finally { $ErrorActionPreference=$prev }
    if ($code -ne 0) { Fail "INDEPENDENT_FIRST_PASS_AUTHENTICATION_FAILED" }
    Write-Output "S1_WAVE0_CHALLENGER_OWNER_FULL_READBACK=PASS"
}

if ($Action -eq "Receive") {
    if (-not $Ciphertext -or -not $ExpectedSha256) {
        Fail "RECEIVE_ARGUMENTS_MISSING"
    }
    $InputFile=[IO.Path]::GetFullPath($Ciphertext)
    Require-File $InputFile "CHALLENGER_CIPHERTEXT_INPUT_MISSING"
    if ([IO.Path]::GetFileName($InputFile) -cne $ChallengerName) {
        Fail "CHALLENGER_CIPHERTEXT_FILENAME_INVALID"
    }
    $size=[IO.FileInfo]::new($InputFile).Length
    if ($size -lt 100 -or $size -gt 400000) { Fail "CHALLENGER_CIPHERTEXT_SIZE_INVALID" }
    Assert-Hash $InputFile $ExpectedSha256 "CHALLENGER_CIPHERTEXT_HASH_INVALID"
    if ([IO.File]::Exists($Saved) -or [IO.File]::Exists($Receipt)) {
        Fail "CHALLENGER_CIPHERTEXT_VERSION_ALREADY_PRESENT"
    }
    [IO.File]::Copy($InputFile,$Saved,$false)
    Assert-Hash $Saved $ExpectedSha256 "CHALLENGER_STORED_BYTES_MISMATCH"
    $record=@{
        format="ads-r0-p03-wave0-owner-challenger-first-pass-receipt-v1"
        source_batch_sha256=$WaveHash
        original_reviewer_ciphertext_sha256=$ExistingReviewerHash
        ciphertext_file=$ChallengerName
        ciphertext_sha256=$ExpectedSha256.ToLowerInvariant()
    }
    [IO.File]::WriteAllText($Receipt,($record|ConvertTo-Json -Compress)+[Environment]::NewLine,
        [Text.UTF8Encoding]::new($false))
    Readback $ExpectedSha256
    Write-Output "S1_WAVE0_CHALLENGER_OWNER_RECEIVE=PASS"
    return
}
if ($Action -eq "Verify") {
    if ($Ciphertext -or $ExpectedSha256) { Fail "VERIFY_ARGUMENTS_INVALID" }
    Require-File $Receipt "CHALLENGER_OWNER_RECEIPT_MISSING"
    try { $r=Get-Content -LiteralPath $Receipt -Raw -Encoding UTF8 | ConvertFrom-Json }
    catch { Fail "CHALLENGER_OWNER_RECEIPT_INVALID" }
    if (
        $r.format -cne "ads-r0-p03-wave0-owner-challenger-first-pass-receipt-v1" -or
        $r.source_batch_sha256 -cne $WaveHash -or
        $r.original_reviewer_ciphertext_sha256 -cne $ExistingReviewerHash -or
        $r.ciphertext_file -cne $ChallengerName -or
        $r.ciphertext_sha256 -cnotmatch '^[0-9a-f]{64}$'
    ) { Fail "CHALLENGER_OWNER_RECEIPT_INVALID" }
    Readback $r.ciphertext_sha256
    Write-Output "S1_WAVE0_CHALLENGER_OWNER_RECHECK=PASS"
    return
}
Fail "OWNER_ACTION_INVALID"
