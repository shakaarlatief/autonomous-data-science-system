#Requires -Version 5.1
<#
Owner-only R0-P03 Wave0 substantively adversarial challenge handoff.

Actions:
  SelfTest      checks exact source archive and Python import availability only
  Export        authenticates both original CMS + comparison; creates precisely
                one restricted PLAINTEXT ZIP under protected owner's ACL folder
  VerifyExport  separately recomputes exact export from authenticated originals
  Receive       receives newly sealed challenge CMS into owner protected store,
                saves digest receipt without overwriting existing evidence
  Verify        independently rechecks saved challenge CMS and fixed receipt

Export deliberately transfers no data. Owner may choose to upload exactly
the resulting ZIP to a separate, authorized non-arm challenger session.
Do not run any protected action through ChatGPT/Runtime Bridge or publish
the restricted packet in the public repository. Never share passphrase/key.
#>
[CmdletBinding()]
param(
    [ValidateSet("SelfTest","Export","VerifyExport","Receive","Verify")]
    [string]$Action="SelfTest",
    [ValidatePattern('^[0-9a-f]{32}$')]
    [string]$RecipientId,
    [string]$Ciphertext,
    [ValidatePattern('^[0-9a-fA-F]{64}$')]
    [string]$ExpectedSha256
)
Set-StrictMode -Version Latest
$ErrorActionPreference="Stop"
$Repo=Split-Path -Parent $PSScriptRoot
$Python=Join-Path $Repo ".venv\Scripts\python.exe"
$OpenSsl="C:\Program Files\Git\usr\bin\openssl.exe"
$PacketModule="experiments.r0_p03_navigation_probe.s1_wave0_adversarial_packet"
$ReportModule="experiments.r0_p03_navigation_probe.s1_wave0_adversarial_challenge_report"
$PacketCode=Join-Path $Repo "experiments\r0_p03_navigation_probe\s1_wave0_adversarial_packet.py"
$ReportCode=Join-Path $Repo "experiments\r0_p03_navigation_probe\s1_wave0_adversarial_challenge_report.py"
$Batch=Join-Path $Repo ".venv\.r0_p03_source_status_wave0\R0_P03_SOURCE_STATUS_FIRST_WAVE_REVIEW_ONLY.zip"
$BatchSha="c90c2d7120ffd32657e6506f876acd10e9779dc968ba9da8fb7f12604aa58387"
$ReviewerSha="9194093b4a4b452b90638bf80eb491d0898c0a7330a77275be74ac9f4aa5a366"
$IndependentSha="50952716754e72a6df915928d1e86c612b510aedc6b3f11c012d9d08b537da64"
$ComparisonSha="f55b6c11e619b8a9b61431564ff19b80073ddfec0b61d8f21d577917cdf66ef3"
$PacketName="R0_P03_S1_WAVE0_RESTRICTED_ADVERSARIAL_INPUT.zip"
$ChallengeName="R0_P03_S1_WAVE0_OWNER_ADVERSARIAL_CHALLENGE.cms"
$ReceiptName="owner-wave0-adversarial-challenge-receipt.json"

function Fail([string]$Code) {
    [Console]::Error.WriteLine("S1_WAVE0_OWNER_ADVERSARIAL_HOLD="+$Code)
    exit 2
}
function FileRequired([string]$File,[string]$Code) {
    if (-not [IO.File]::Exists($File)) { Fail $Code }
    if (([IO.File]::GetAttributes($File) -band [IO.FileAttributes]::ReparsePoint) -ne 0) {
        Fail $Code
    }
}
function HashRequired([string]$File,[string]$Sha,[string]$Code) {
    FileRequired $File $Code
    if ((Get-FileHash -LiteralPath $File -Algorithm SHA256).Hash.ToLowerInvariant() -cne $Sha.ToLowerInvariant()) {
        Fail $Code
    }
}
function Run-Python([string[]]$Arguments) {
    $previous=$ErrorActionPreference
    try {
        $ErrorActionPreference="Continue"
        Push-Location -LiteralPath $Repo
        try {
            & $Python @Arguments
            $processCode=$LASTEXITCODE
        } finally { Pop-Location }
    } finally { $ErrorActionPreference=$previous }
    if ($processCode -ne 0) { Fail "OWNER_PYTHON_OPERATION_FAILED" }
}
foreach($f in @($Python,$OpenSsl,$PacketCode,$ReportCode)) {
    FileRequired $f "OWNER_PREREQUISITES_MISSING"
}
HashRequired $Batch $BatchSha "OWNER_SOURCE_ARCHIVE_MISMATCH"
if ($Action -eq "SelfTest") {
    if ($RecipientId -or $Ciphertext -or $ExpectedSha256) {
        Fail "OWNER_SELFTEST_ARGUMENTS_INVALID"
    }
    Run-Python @("-B","-m",$PacketModule,"--help")
    Run-Python @("-B","-m",$ReportModule,"--help")
    Write-Output "S1_WAVE0_ADVERSARIAL_MODULE_IMPORTS=PASS"
    Write-Output "S1_WAVE0_ADVERSARIAL_OWNER_PREFLIGHT=PASS"
    Write-Output "S1_WAVE0_ADVERSARIAL_PRIVATE_INPUTS_OPENED=NO"
    return
}
if (-not [Environment]::UserInteractive) { Fail "OWNER_INTERACTIVE_TERMINAL_REQUIRED" }
if (-not $RecipientId -or -not $env:LOCALAPPDATA) { Fail "EXISTING_RECIPIENT_ID_REQUIRED" }
if ($Action -notin @("Receive") -and ($Ciphertext -or $ExpectedSha256)) {
    Fail "EXTRANEOUS_CIPHERTEXT_ARGUMENTS"
}
$Folder=Join-Path $env:LOCALAPPDATA ("ADS-R0-P03-S1-REAL-REVIEW-"+$RecipientId)
if (-not [IO.Directory]::Exists($Folder) -or
    (([IO.File]::GetAttributes($Folder) -band [IO.FileAttributes]::ReparsePoint) -ne 0)) {
    Fail "OWNER_PRIVATE_DIRECTORY_MISSING"
}
$acl=Get-Acl -LiteralPath $Folder
if (-not $acl.AreAccessRulesProtected) { Fail "OWNER_DIRECTORY_ACL_UNPROTECTED" }
$mySid=[Security.Principal.WindowsIdentity]::GetCurrent().User.Value
$rules=@($acl.GetAccessRules($true,$true,[Security.Principal.SecurityIdentifier]))
$sids=@($rules | ForEach-Object {$_.IdentityReference.Value})
if ($mySid -notin $sids -or "S-1-5-18" -notin $sids) {
    Fail "OWNER_DIRECTORY_ACL_MISSING_PRINCIPALS"
}
foreach($ace in $rules) {
    if ($ace.IdentityReference.Value -notin @($mySid,"S-1-5-18") -or
        $ace.AccessControlType -ne [Security.AccessControl.AccessControlType]::Allow) {
        Fail "OWNER_DIRECTORY_ACL_UNEXPECTED_PRINCIPAL"
    }
}
$Key=Join-Path $Folder "owner-review-encrypted-key.pem"
$Cert=Join-Path $Folder "owner-review-public-cert.pem"
$Reviewer=Join-Path $Folder "R0_P03_S1_WAVE0_OWNER_REVIEW.cms"
$Independent=Join-Path $Folder "R0_P03_S1_WAVE0_OWNER_CHALLENGER_FIRST_PASS.cms"
$Comparison=Join-Path $Folder "R0_P03_S1_WAVE0_OWNER_PRIVATE_COMPARISON.cms"
$Packet=Join-Path $Folder $PacketName
$Challenge=Join-Path $Folder $ChallengeName
$Receipt=Join-Path $Folder $ReceiptName
FileRequired $Key "OWNER_ENCRYPTED_KEY_MISSING"
FileRequired $Cert "OWNER_PUBLIC_CERT_MISSING"
if (-not [IO.File]::ReadAllText($Key).StartsWith("-----BEGIN ENCRYPTED PRIVATE KEY-----")) {
    Fail "OWNER_KEY_IS_NOT_ENCRYPTED"
}
HashRequired $Reviewer $ReviewerSha "OWNER_REVIEWER_CMS_IDENTITY_MISMATCH"
HashRequired $Independent $IndependentSha "OWNER_INDEPENDENT_CMS_IDENTITY_MISMATCH"
HashRequired $Comparison $ComparisonSha "OWNER_COMPARISON_CMS_IDENTITY_MISMATCH"

function Verified-Packet([string]$Mode) {
    $cliArgs=@("-B","-m",$PacketModule,"--action",$Mode,
        "--batch-zip",$Batch,"--reviewer-cms",$Reviewer,
        "--challenger-cms",$Independent,"--comparison-cms",$Comparison,
        "--public-cert",$Cert,"--private-key",$Key,
        "--sender-module",$ReportCode,"--output",$Packet,
        "--openssl",$OpenSsl)
    Run-Python $cliArgs
}
if ($Action -eq "Export") {
    if ([IO.File]::Exists($Packet)) { Fail "OWNER_PACKET_ALREADY_EXISTS" }
    Write-Output "RESTRICTED: The ZIP will contain original sources and BOTH private reviewer rationales."
    Write-Output "It is plaintext, stored only inside the existing owner-private folder."
    Write-Output "It may be sent only to the owner-authorized NON-ARM adversarial challenger."
    $decision=(Read-Host 'Type AUTHORIZE WAVE0 RESTRICTED CHALLENGE EXPORT').Trim()
    if ($decision -cne "AUTHORIZE WAVE0 RESTRICTED CHALLENGE EXPORT") {
        Fail "OWNER_EXPORT_CONFIRMATION_REQUIRED"
    }
    Verified-Packet "Export"
    Write-Output "S1_WAVE0_OWNER_RESTRICTED_ADVERSARIAL_EXPORT=PASS"
    return
}
if ($Action -eq "VerifyExport") {
    Verified-Packet "VerifyExport"
    Write-Output "S1_WAVE0_OWNER_RESTRICTED_ADVERSARIAL_EXPORT_RECHECK=PASS"
    return
}
FileRequired $Packet "OWNER_RESTRICTED_PACKET_MISSING"
if ($Action -eq "Receive") {
    if (-not $Ciphertext -or -not $ExpectedSha256) {
        Fail "CHALLENGE_RECEIVE_ARGUMENTS_MISSING"
    }
    $InputFile=[IO.Path]::GetFullPath($Ciphertext)
    FileRequired $InputFile "CHALLENGE_INPUT_CIPHERTEXT_MISSING"
    if ([IO.Path]::GetFileName($InputFile) -cne $ChallengeName) {
        Fail "CHALLENGE_CIPHERTEXT_NAME_INVALID"
    }
    $length=[IO.FileInfo]::new($InputFile).Length
    if ($length -lt 100 -or $length -gt 550000) {
        Fail "CHALLENGE_CIPHERTEXT_SIZE_INVALID"
    }
    HashRequired $InputFile $ExpectedSha256 "CHALLENGE_INPUT_CIPHERTEXT_HASH_MISMATCH"
    if ([IO.File]::Exists($Challenge) -or [IO.File]::Exists($Receipt)) {
        Fail "CHALLENGE_OWNER_VERSION_ALREADY_STORED"
    }
    [IO.File]::Copy($InputFile,$Challenge,$false)
    HashRequired $Challenge $ExpectedSha256 "CHALLENGE_CIPHERTEXT_COPY_MISMATCH"
    $rec=@{
        format="ads-r0-p03-s1-wave0-adversarial-owner-receipt-v1"
        packet_sha256=(Get-FileHash -LiteralPath $Packet -Algorithm SHA256).Hash.ToLowerInvariant()
        ciphertext_file=$ChallengeName
        ciphertext_sha256=$ExpectedSha256.ToLowerInvariant()
        original_reviewer_ciphertext_sha256=$ReviewerSha
        independent_first_pass_ciphertext_sha256=$IndependentSha
        owner_comparison_ciphertext_sha256=$ComparisonSha
    }
    [IO.File]::WriteAllText($Receipt,($rec|ConvertTo-Json -Compress)+[Environment]::NewLine,
        [Text.UTF8Encoding]::new($false))
}
if ($Action -eq "Verify") {
    FileRequired $Receipt "CHALLENGE_OWNER_RECEIPT_MISSING"
}
try { $receipt=Get-Content -LiteralPath $Receipt -Raw -Encoding UTF8 | ConvertFrom-Json }
catch { Fail "CHALLENGE_OWNER_RECEIPT_UNREADABLE" }
if (
    $receipt.format -cne "ads-r0-p03-s1-wave0-adversarial-owner-receipt-v1" -or
    $receipt.ciphertext_file -cne $ChallengeName -or
    $receipt.original_reviewer_ciphertext_sha256 -cne $ReviewerSha -or
    $receipt.independent_first_pass_ciphertext_sha256 -cne $IndependentSha -or
    $receipt.owner_comparison_ciphertext_sha256 -cne $ComparisonSha -or
    $receipt.packet_sha256 -cnotmatch '^[0-9a-f]{64}$' -or
    $receipt.ciphertext_sha256 -cnotmatch '^[0-9a-f]{64}$'
) { Fail "CHALLENGE_OWNER_RECEIPT_INVALID" }
HashRequired $Packet $receipt.packet_sha256 "CHALLENGE_PACKET_HASH_DRIFT"
HashRequired $Challenge $receipt.ciphertext_sha256 "CHALLENGE_CIPHERTEXT_HASH_DRIFT"
$verifyArgs=@("-B","-m",$ReportModule,"owner-verify",
    "--packet",$Packet,"--public-cert",$Cert,"--private-key",$Key,
    "--ciphertext",$Challenge,"--expected-sha256",$receipt.ciphertext_sha256,
    "--openssl",$OpenSsl)
Run-Python $verifyArgs
if ($Action -eq "Receive") {
    Write-Output "S1_WAVE0_OWNER_ADVERSARIAL_CHALLENGE_RECEIVE=PASS"
} elseif ($Action -eq "Verify") {
    Write-Output "S1_WAVE0_OWNER_ADVERSARIAL_CHALLENGE_RECHECK=PASS"
} else { Fail "CHALLENGE_ACTION_INVALID" }
