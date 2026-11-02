#Requires -Version 5.1
<#
OWNER-ONLY Wave0 dual-review authenticated comparison.

Run ONLY in an owner's ordinary interactive PowerShell. NEVER through an
exposed coordinator/Runtime Bridge/agent, challenger or source-reviewer chat.
Uses the existing owner encrypted key and certificate; does NOT create or
export keys. No plaintext source-status report or paired disagreement is
printed or saved; output is one owner-local AES-256-GCM CMS dossier.

The comparison is mechanical and cannot accept source status or certify
semantic correctness. A later protected adversarial challenge remains needed.
#>
[CmdletBinding()]
param(
    [ValidateSet("SelfTest","Compare","Verify")]
    [string] $Action = "SelfTest",
    [ValidatePattern('^[0-9a-f]{32}$')]
    [string] $RecipientId
)
Set-StrictMode -Version Latest
$ErrorActionPreference="Stop"
$Repo=Split-Path -Parent $PSScriptRoot
$Python=Join-Path $Repo ".venv\Scripts\python.exe"
$OpenSsl="C:\Program Files\Git\usr\bin\openssl.exe"
$Tool=Join-Path $Repo "experiments\r0_p03_navigation_probe\s1_wave0_owner_private_compare.py"
$Module="experiments.r0_p03_navigation_probe.s1_wave0_owner_private_compare"
$Wave=Join-Path $Repo ".venv\.r0_p03_source_status_wave0\R0_P03_SOURCE_STATUS_FIRST_WAVE_REVIEW_ONLY.zip"
$WaveSha="c90c2d7120ffd32657e6506f876acd10e9779dc968ba9da8fb7f12604aa58387"
$ReviewerSha="9194093b4a4b452b90638bf80eb491d0898c0a7330a77275be74ac9f4aa5a366"
$ChallengerSha="50952716754e72a6df915928d1e86c612b510aedc6b3f11c012d9d08b537da64"

function Fail([string]$Code) {
    [Console]::Error.WriteLine("S1_WAVE0_OWNER_PRIVATE_COMPARISON_HOLD="+$Code)
    exit 2
}
function Require-File([string]$Name,[string]$Code) {
    if (-not [IO.File]::Exists($Name)) { Fail $Code }
    if (([IO.File]::GetAttributes($Name) -band [IO.FileAttributes]::ReparsePoint) -ne 0) {
        Fail $Code
    }
}
function Require-Hash([string]$Name,[string]$Expected,[string]$Code) {
    Require-File $Name $Code
    $digest=(Get-FileHash -LiteralPath $Name -Algorithm SHA256).Hash.ToLowerInvariant()
    if ($digest -cne $Expected) { Fail $Code }
}
foreach($p in @($Python,$OpenSsl,$Tool)) { Require-File $p "OWNER_COMPARISON_PREREQUISITE_MISSING" }
Require-Hash $Wave $WaveSha "OWNER_COMPARISON_WAVE0_SOURCE_DRIFT"
if ($Action -eq "SelfTest") {
    if ($RecipientId) { Fail "OWNER_COMPARISON_SELFTEST_ARGUMENTS_INVALID" }
    # Verify the actual module launcher and both imports before any owner
    # protected report or key is opened. This is safe even when run without
    # an owner recipient. Direct script execution cannot import experiments.
    Push-Location -LiteralPath $Repo
    try {
        & $Python -B -m $Module --help | Out-Null
        $probeCode=$LASTEXITCODE
    } finally {
        Pop-Location
    }
    if ($probeCode -ne 0) { Fail "OWNER_COMPARISON_MODULE_LAUNCH_FAILED" }
    Write-Output "S1_WAVE0_OWNER_PRIVATE_COMPARISON_MODULE_LAUNCH=PASS"
    Write-Output "S1_WAVE0_OWNER_PRIVATE_COMPARISON_PREFLIGHT=PASS"
    Write-Output "S1_WAVE0_OWNER_PRIVATE_COMPARISON_NEW_KEYS=NO"
    Write-Output "S1_WAVE0_OWNER_PRIVATE_COMPARISON_REPORTS_OPENED=NO"
    return
}
if (-not [Environment]::UserInteractive) { Fail "OWNER_COMPARISON_INTERACTIVE_TERMINAL_REQUIRED" }
if (-not $RecipientId -or -not $env:LOCALAPPDATA) { Fail "OWNER_COMPARISON_RECIPIENT_MISSING" }
$Folder=Join-Path $env:LOCALAPPDATA ("ADS-R0-P03-S1-REAL-REVIEW-"+$RecipientId)
if (-not [IO.Directory]::Exists($Folder) -or
    (([IO.File]::GetAttributes($Folder) -band [IO.FileAttributes]::ReparsePoint) -ne 0)) {
    Fail "OWNER_COMPARISON_DIRECTORY_MISSING"
}
$acl=Get-Acl -LiteralPath $Folder
if (-not $acl.AreAccessRulesProtected) { Fail "OWNER_COMPARISON_ACL_UNPROTECTED" }
$me=[Security.Principal.WindowsIdentity]::GetCurrent().User.Value
$aces=@($acl.GetAccessRules($true,$true,[Security.Principal.SecurityIdentifier]))
$principals=@($aces | ForEach-Object {$_.IdentityReference.Value})
if ($me -notin $principals -or "S-1-5-18" -notin $principals) {
    Fail "OWNER_COMPARISON_ACL_PRINCIPALS_MISSING"
}
foreach($ace in $aces) {
    if ($ace.IdentityReference.Value -notin @($me,"S-1-5-18") -or
        $ace.AccessControlType -ne [Security.AccessControl.AccessControlType]::Allow) {
        Fail "OWNER_COMPARISON_ACL_UNEXPECTED_PRINCIPAL"
    }
}
$Key=Join-Path $Folder "owner-review-encrypted-key.pem"
$Cert=Join-Path $Folder "owner-review-public-cert.pem"
$Reviewer=Join-Path $Folder "R0_P03_S1_WAVE0_OWNER_REVIEW.cms"
$Challenger=Join-Path $Folder "R0_P03_S1_WAVE0_OWNER_CHALLENGER_FIRST_PASS.cms"
$Comparison=Join-Path $Folder "R0_P03_S1_WAVE0_OWNER_PRIVATE_COMPARISON.cms"
Require-File $Key "OWNER_COMPARISON_ENCRYPTED_KEY_MISSING"
Require-File $Cert "OWNER_COMPARISON_CERT_MISSING"
if (-not [IO.File]::ReadAllText($Key).StartsWith("-----BEGIN ENCRYPTED PRIVATE KEY-----")) {
    Fail "OWNER_COMPARISON_KEY_UNENCRYPTED"
}
Require-Hash $Reviewer $ReviewerSha "OWNER_COMPARISON_REVIEWER_CMS_MISMATCH"
Require-Hash $Challenger $ChallengerSha "OWNER_COMPARISON_CHALLENGER_CMS_MISMATCH"

# Execute through -m from repository root. When executing a .py path,
# Python puts the script directory (not the repository root) on sys.path,
# and the absolute experiments import fails before opening any owner file.
$args=@("-B","-m",$Module,"--action",$Action,"--batch-zip",$Wave,
    "--reviewer-cms",$Reviewer,"--challenger-cms",$Challenger,
    "--public-cert",$Cert,"--private-key",$Key,
    "--comparison-cms",$Comparison,"--openssl",$OpenSsl)
$old=$ErrorActionPreference
try {
    $ErrorActionPreference="Continue"
    Push-Location -LiteralPath $Repo
    try {
        & $Python @args
        $code=$LASTEXITCODE
    } finally {
        Pop-Location
    }
} finally {
    $ErrorActionPreference=$old
}
if ($code -ne 0) { Fail "OWNER_PRIVATE_COMPARISON_OPERATION_FAILED" }
Write-Output ("S1_WAVE0_OWNER_PRIVATE_COMPARISON_"+$Action.ToUpperInvariant()+"=PASS")
