#Requires -Version 5.1
<#
Purpose-specific Wave0 owner-only semantic adjudication transport.

SelfTest      public source archive and harmless Python CLI module imports
Export        existing owner key authenticates all prior sealed reports and
              writes one restricted PLAINTEXT packet in owner ACL directory
VerifyExport  independently recomputes and byte-verifies the saved packet
Receive       stores the new encrypted decision register with no overwrite,
              adds a receipt and authenticates its ten-record schema
Verify        separately reauthenticates the saved decision register/receipt

Only the OWNER executes protected actions in ordinary interactive PowerShell.
NEVER invoke actual private operations through Codexless Runtime Bridge.
Do not share restricted packet, private key, passphrase or findings here.
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
$Exporter="experiments.r0_p03_navigation_probe.s1_wave0_semantic_adjudication_packet"
$Decision="experiments.r0_p03_navigation_probe.s1_wave0_semantic_decision_report"
$ExporterCode=Join-Path $Repo "experiments\r0_p03_navigation_probe\s1_wave0_semantic_adjudication_packet.py"
$DecisionCode=Join-Path $Repo "experiments\r0_p03_navigation_probe\s1_wave0_semantic_decision_report.py"
$PreviousSender=Join-Path $Repo "experiments\r0_p03_navigation_probe\s1_wave0_adversarial_challenge_report.py"
$Original=Join-Path $Repo ".venv\.r0_p03_source_status_wave0\R0_P03_SOURCE_STATUS_FIRST_WAVE_REVIEW_ONLY.zip"
$OriginalHash="c90c2d7120ffd32657e6506f876acd10e9779dc968ba9da8fb7f12604aa58387"
$FirstHash="9194093b4a4b452b90638bf80eb491d0898c0a7330a77275be74ac9f4aa5a366"
$SecondHash="50952716754e72a6df915928d1e86c612b510aedc6b3f11c012d9d08b537da64"
$ComparisonHash="f55b6c11e619b8a9b61431564ff19b80073ddfec0b61d8f21d577917cdf66ef3"
$ChallengeHash="e2d2c31d0486b9314b1d5902776da866397cb092963ac75c95e7b5c6f313ac03"
$AdjudicationName="R0_P03_S1_WAVE0_OWNER_SEMANTIC_ADJUDICATION.cms"
$PacketName="R0_P03_S1_WAVE0_OWNER_SEMANTIC_ADJUDICATION_INPUT.zip"
$ReceiptName="owner-wave0-semantic-adjudication-receipt.json"

function Hold([string]$Reason) {
    [Console]::Error.WriteLine("S1_WAVE0_OWNER_SEMANTIC_ADJUDICATION_HOLD="+$Reason)
    exit 2
}
function Require-File([string]$Path,[string]$Code) {
    if (-not [IO.File]::Exists($Path)) { Hold $Code }
    if (([IO.File]::GetAttributes($Path) -band [IO.FileAttributes]::ReparsePoint) -ne 0) {
        Hold $Code
    }
}
function Require-Hash([string]$Path,[string]$Expected,[string]$Code) {
    Require-File $Path $Code
    if ((Get-FileHash -LiteralPath $Path -Algorithm SHA256).Hash.ToLowerInvariant() -cne $Expected.ToLowerInvariant()) {
        Hold $Code
    }
}
function Run-Module([string[]]$Arguments) {
    $old=$ErrorActionPreference
    try {
        $ErrorActionPreference="Continue"
        Push-Location -LiteralPath $Repo
        try {
            & $Python @Arguments
            $code=$LASTEXITCODE
        } finally { Pop-Location }
    } finally { $ErrorActionPreference=$old }
    if ($code -ne 0) { Hold "SEMANTIC_PYTHON_OPERATION_FAILED" }
}
foreach($f in @($Python,$OpenSsl,$ExporterCode,$DecisionCode,$PreviousSender)) {
    Require-File $f "SEMANTIC_PREREQUISITE_MISSING"
}
Require-Hash $Original $OriginalHash "SEMANTIC_SOURCE_ZIP_DRIFT"

if ($Action -eq "SelfTest") {
    if ($RecipientId -or $Ciphertext -or $ExpectedSha256) {
        Hold "SEMANTIC_SELFTEST_EXTRA_ARGUMENT"
    }
    # Validate real module imports without entering the protected owner area.
    Run-Module @("-B","-m",$Exporter,"--help")
    Run-Module @("-B","-m",$Decision,"--help")
    Write-Output "S1_WAVE0_SEMANTIC_OWNER_MODULE_IMPORTS=PASS"
    Write-Output "S1_WAVE0_SEMANTIC_OWNER_PREFLIGHT=PASS"
    Write-Output "S1_WAVE0_SEMANTIC_OWNER_PRIVATE_EVIDENCE_OPENED=NO"
    return
}
if (-not [Environment]::UserInteractive) { Hold "SEMANTIC_OWNER_INTERACTIVE_REQUIRED" }
if (-not $RecipientId -or -not $env:LOCALAPPDATA) {
    Hold "SEMANTIC_EXISTING_OWNER_RECIPIENT_REQUIRED"
}
if ($Action -ne "Receive" -and ($Ciphertext -or $ExpectedSha256)) {
    Hold "SEMANTIC_EXTRA_CIPHERTEXT_ARGUMENT"
}
$Folder=Join-Path $env:LOCALAPPDATA ("ADS-R0-P03-S1-REAL-REVIEW-"+$RecipientId)
if (-not [IO.Directory]::Exists($Folder) -or
    (([IO.File]::GetAttributes($Folder) -band [IO.FileAttributes]::ReparsePoint) -ne 0)) {
    Hold "SEMANTIC_OWNER_FOLDER_MISSING"
}
$acl=Get-Acl -LiteralPath $Folder
if (-not $acl.AreAccessRulesProtected) { Hold "SEMANTIC_OWNER_ACL_NOT_PROTECTED" }
$me=[Security.Principal.WindowsIdentity]::GetCurrent().User.Value
$rules=@($acl.GetAccessRules($true,$true,[Security.Principal.SecurityIdentifier]))
$principals=@($rules | ForEach-Object {$_.IdentityReference.Value})
if ($me -notin $principals -or "S-1-5-18" -notin $principals) {
    Hold "SEMANTIC_OWNER_ACL_PRINCIPALS_MISSING"
}
foreach($ace in $rules) {
    if ($ace.IdentityReference.Value -notin @($me,"S-1-5-18") -or
        $ace.AccessControlType -ne [Security.AccessControl.AccessControlType]::Allow) {
        Hold "SEMANTIC_OWNER_ACL_UNEXPECTED_PRINCIPAL"
    }
}
$Key=Join-Path $Folder "owner-review-encrypted-key.pem"
$Cert=Join-Path $Folder "owner-review-public-cert.pem"
$First=Join-Path $Folder "R0_P03_S1_WAVE0_OWNER_REVIEW.cms"
$Second=Join-Path $Folder "R0_P03_S1_WAVE0_OWNER_CHALLENGER_FIRST_PASS.cms"
$Comparison=Join-Path $Folder "R0_P03_S1_WAVE0_OWNER_PRIVATE_COMPARISON.cms"
$ChallengePacket=Join-Path $Folder "R0_P03_S1_WAVE0_RESTRICTED_ADVERSARIAL_INPUT.zip"
$Challenge=Join-Path $Folder "R0_P03_S1_WAVE0_OWNER_ADVERSARIAL_CHALLENGE.cms"
$Packet=Join-Path $Folder $PacketName
$Adjudication=Join-Path $Folder $AdjudicationName
$Receipt=Join-Path $Folder $ReceiptName
Require-File $Key "SEMANTIC_OWNER_ENCRYPTED_KEY_MISSING"
Require-File $Cert "SEMANTIC_OWNER_PUBLIC_CERT_MISSING"
if (-not [IO.File]::ReadAllText($Key).StartsWith("-----BEGIN ENCRYPTED PRIVATE KEY-----")) {
    Hold "SEMANTIC_OWNER_KEY_NOT_ENCRYPTED"
}
Require-Hash $First $FirstHash "SEMANTIC_FIRST_CMS_HASH_MISMATCH"
Require-Hash $Second $SecondHash "SEMANTIC_SECOND_CMS_HASH_MISMATCH"
Require-Hash $Comparison $ComparisonHash "SEMANTIC_COMPARISON_CMS_HASH_MISMATCH"
Require-Hash $Challenge $ChallengeHash "SEMANTIC_CHALLENGE_CMS_HASH_MISMATCH"
Require-File $ChallengePacket "SEMANTIC_ORIGINAL_CHALLENGE_PACKET_MISSING"

function Run-Export([string]$Mode) {
    $cmd=@("-B","-m",$Exporter,"--action",$Mode,
        "--source-zip",$Original,"--first-cms",$First,
        "--independent-cms",$Second,"--comparison-cms",$Comparison,
        "--challenge-packet",$ChallengePacket,"--challenge-cms",$Challenge,
        "--public-cert",$Cert,"--private-key",$Key,
        "--previous-sender",$PreviousSender,"--sender",$DecisionCode,
        "--output",$Packet,"--openssl",$OpenSsl)
    Run-Module $cmd
}
if ($Action -eq "Export") {
    if ([IO.File]::Exists($Packet)) { Hold "SEMANTIC_PACKET_ALREADY_EXISTS" }
    Write-Output "RESTRICTED: This creates PLAINTEXT historical sources + all three private assessment layers."
    Write-Output "It remains in the existing owner protected folder until you personally attach it."
    Write-Output "Only the separately owner-authorized NON-ARM semantic adjudicator may receive it."
    $confirm=(Read-Host 'Type AUTHORIZE WAVE0 SEMANTIC ADJUDICATION EXPORT').Trim()
    if ($confirm -cne "AUTHORIZE WAVE0 SEMANTIC ADJUDICATION EXPORT") {
        Hold "SEMANTIC_OWNER_EXPORT_CONFIRMATION_MISSING"
    }
    Run-Export "Export"
    Write-Output "S1_WAVE0_OWNER_SEMANTIC_EXPORT=PASS"
    return
}
if ($Action -eq "VerifyExport") {
    Run-Export "VerifyExport"
    Write-Output "S1_WAVE0_OWNER_SEMANTIC_EXPORT_RECHECK=PASS"
    return
}
Require-File $Packet "SEMANTIC_OWNER_PACKET_MISSING"

if ($Action -eq "Receive") {
    if (-not $Ciphertext -or -not $ExpectedSha256) {
        Hold "SEMANTIC_RECEIVE_ARGUMENTS_MISSING"
    }
    $InputFile=[IO.Path]::GetFullPath($Ciphertext)
    Require-File $InputFile "SEMANTIC_INPUT_CMS_MISSING"
    if ([IO.Path]::GetFileName($InputFile) -cne $AdjudicationName) {
        Hold "SEMANTIC_INPUT_CMS_NAME_MISMATCH"
    }
    $bytes=[IO.FileInfo]::new($InputFile).Length
    if ($bytes -lt 100 -or $bytes -gt 620000) {
        Hold "SEMANTIC_INPUT_CMS_SIZE_INVALID"
    }
    Require-Hash $InputFile $ExpectedSha256 "SEMANTIC_INPUT_CMS_HASH_MISMATCH"
    if ([IO.File]::Exists($Adjudication) -or [IO.File]::Exists($Receipt)) {
        Hold "SEMANTIC_OWNER_VERSION_ALREADY_EXISTS"
    }
    [IO.File]::Copy($InputFile,$Adjudication,$false)
    Require-Hash $Adjudication $ExpectedSha256 "SEMANTIC_SAVED_CMS_HASH_MISMATCH"
    $receiptData=@{
        format="ads-r0-p03-wave0-owner-semantic-adjudication-receipt-v1"
        packet_sha256=(Get-FileHash -LiteralPath $Packet -Algorithm SHA256).Hash.ToLowerInvariant()
        ciphertext_name=$AdjudicationName
        ciphertext_sha256=$ExpectedSha256.ToLowerInvariant()
        original_first_sha256=$FirstHash
        original_second_sha256=$SecondHash
        paired_comparison_sha256=$ComparisonHash
        substantive_challenge_sha256=$ChallengeHash
    }
    [IO.File]::WriteAllText($Receipt,($receiptData|ConvertTo-Json -Compress)+[Environment]::NewLine,
        [Text.UTF8Encoding]::new($false))
}
if ($Action -eq "Verify") {
    Require-File $Receipt "SEMANTIC_OWNER_RECEIPT_MISSING"
}
try { $receipt=Get-Content -LiteralPath $Receipt -Raw -Encoding UTF8 | ConvertFrom-Json }
catch { Hold "SEMANTIC_RECEIPT_INVALID" }
if (
    $receipt.format -cne "ads-r0-p03-wave0-owner-semantic-adjudication-receipt-v1" -or
    $receipt.ciphertext_name -cne $AdjudicationName -or
    $receipt.original_first_sha256 -cne $FirstHash -or
    $receipt.original_second_sha256 -cne $SecondHash -or
    $receipt.paired_comparison_sha256 -cne $ComparisonHash -or
    $receipt.substantive_challenge_sha256 -cne $ChallengeHash -or
    $receipt.packet_sha256 -cnotmatch '^[0-9a-f]{64}$' -or
    $receipt.ciphertext_sha256 -cnotmatch '^[0-9a-f]{64}$'
) { Hold "SEMANTIC_RECEIPT_SCHEMA_INVALID" }
Require-Hash $Packet $receipt.packet_sha256 "SEMANTIC_PACKET_HASH_DRIFT"
Require-Hash $Adjudication $receipt.ciphertext_sha256 "SEMANTIC_OWNER_CMS_HASH_DRIFT"
$cmd=@("-B","-m",$Decision,"owner-verify",
    "--packet",$Packet,"--public-cert",$Cert,"--private-key",$Key,
    "--ciphertext",$Adjudication,"--expected-sha256",$receipt.ciphertext_sha256,
    "--openssl",$OpenSsl)
Run-Module $cmd
if ($Action -eq "Receive") {
    Write-Output "S1_WAVE0_OWNER_SEMANTIC_ADJUDICATION_RECEIVE=PASS"
} elseif ($Action -eq "Verify") {
    Write-Output "S1_WAVE0_OWNER_SEMANTIC_ADJUDICATION_RECHECK=PASS"
} else { Hold "SEMANTIC_ACTION_INVALID" }
