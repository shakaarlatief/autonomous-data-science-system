#Requires -Version 5.1
<#
Owner-only local import of the independent, still UNADJUDICATED twelve-need
candidate file. This is NOT the protected gold store or scored author input.

Execute Import and Verify only from a normal non-elevated owner PowerShell
process, never through ADS agent/Runtime Bridge. Nothing here accesses the
coordinating chat or prints candidate wording. All output files are under
a new uniquely named LocalAppData folder with an owner-and-SYSTEM-only ACL.
This cannot establish model/account/provider isolation or remove the original
download or its copies, logs, backups, and chat-platform retained attachments.
#>
[CmdletBinding()]
param(
    [ValidateSet("SelfTest","Import","Verify")][string]$Action = "SelfTest",
    [string]$SourcePath,
    [string]$Directory
)
Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"
$ExpectedBytes = 12684
$ExpectedSha256 = "819ee551af64f87571df281dfdda75af8f5aa6088202b924bc09e2209cea0c86"
$OriginalFilename = "NEED_PROPOSALS_RESTRICTED.md"
$ManifestFilename = "owner-intake-manifest.json"
$Prefix = "ADS-P03-PRIVATE-NEEDS-"

function Get-Digest([byte[]]$Bytes) {
    $h = [Security.Cryptography.SHA256]::Create()
    try { return [BitConverter]::ToString($h.ComputeHash($Bytes)).Replace("-","").ToLowerInvariant() }
    finally { $h.Dispose() }
}

function Assert-ExactBytes([byte[]]$Bytes) {
    if ($Bytes.Length -ne $ExpectedBytes -or (Get-Digest $Bytes) -cne $ExpectedSha256) {
        throw "PROPOSAL_BYTES_OR_SHA256_NOT_RECEIPT_IDENTITY"
    }
}

function Get-OwnerSid {
    $identity = [Security.Principal.WindowsIdentity]::GetCurrent()
    if ($null -eq $identity.User -or $identity.User.Value -eq "S-1-5-18" -or
        $identity.Name -match '\\CodexSandbox(Offline|Online)$') {
        throw "OWNER_INTERACTIVE_IDENTITY_REQUIRED"
    }
    $principal = [Security.Principal.WindowsPrincipal]::new($identity)
    if ($principal.IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)) {
        throw "NON_ELEVATED_OWNER_POWERSHELL_REQUIRED"
    }
    return $identity.User
}

function Assert-BoundedOwnerDirectory([string]$Path) {
    if ([string]::IsNullOrWhiteSpace($Path)) { throw "OWNER_DIRECTORY_REQUIRED" }
    $full = [IO.Path]::GetFullPath($Path)
    $parent = [IO.Path]::GetDirectoryName($full).TrimEnd('\')
    $base = [IO.Path]::GetFullPath($env:LOCALAPPDATA).TrimEnd('\')
    if (-not [string]::Equals($parent,$base,[StringComparison]::OrdinalIgnoreCase)) {
        throw "CUSTODY_FOLDER_MUST_BE_DIRECT_LOCALAPPDATA_CHILD"
    }
    if ([IO.Path]::GetFileName($full) -cnotmatch "^ADS-P03-PRIVATE-NEEDS-[0-9a-f]{32}$") {
        throw "INVALID_OWNER_INTAKE_FOLDER"
    }
    return $full
}

function Assert-Acl([string]$Path, [Security.Principal.SecurityIdentifier]$Sid, [bool]$DirectoryExpected) {
    $item = Get-Item -LiteralPath $Path -Force
    if ($item.PSIsContainer -ne $DirectoryExpected -or
        ($item.Attributes -band [IO.FileAttributes]::ReparsePoint) -ne 0) {
        throw "UNEXPECTED_FILE_TYPE_OR_REPARSE"
    }
    $acl = Get-Acl -LiteralPath $Path
    if ($DirectoryExpected -and -not $acl.AreAccessRulesProtected) {
        throw "OWNER_DIRECTORY_INHERITS_UNEXPECTED_PERMISSIONS"
    }
    $rules = @($acl.GetAccessRules($true,$true,[Security.Principal.SecurityIdentifier]))
    $sids = @($rules | ForEach-Object { $_.IdentityReference.Value })
    if ($rules.Count -lt 2 -or $Sid.Value -notin $sids -or "S-1-5-18" -notin $sids) {
        throw "OWNER_AND_SYSTEM_REQUIRED"
    }
    foreach ($rule in $rules) {
        if ($rule.AccessControlType -ne [Security.AccessControl.AccessControlType]::Allow -or
            $rule.IdentityReference.Value -notin @($Sid.Value, "S-1-5-18")) {
            throw "UNEXPECTED_CUSTODY_PERMISSION"
        }
    }
}

function New-BoundedFolder([string]$Folder, [Security.Principal.SecurityIdentifier]$Sid) {
    if ([IO.Directory]::Exists($Folder) -or [IO.File]::Exists($Folder)) {
        throw "EXISTING_OWNER_INTAKE_FOLDER_REFUSED"
    }
    $acl = [Security.AccessControl.DirectorySecurity]::new()
    $acl.SetAccessRuleProtection($true,$false)
    $inherit = [Security.AccessControl.InheritanceFlags]::ContainerInherit -bor
        [Security.AccessControl.InheritanceFlags]::ObjectInherit
    foreach ($principal in @($Sid,[Security.Principal.SecurityIdentifier]::new("S-1-5-18"))) {
        $acl.AddAccessRule([Security.AccessControl.FileSystemAccessRule]::new(
            $principal,[Security.AccessControl.FileSystemRights]::FullControl,
            $inherit,[Security.AccessControl.PropagationFlags]::None,
            [Security.AccessControl.AccessControlType]::Allow))
    }
    [IO.Directory]::CreateDirectory($Folder,$acl) | Out-Null
    Assert-Acl -Path $Folder -Sid $Sid -DirectoryExpected $true
}

function Write-NewBytes([string]$Path, [byte[]]$Bytes) {
    $stream = [IO.FileStream]::new($Path,[IO.FileMode]::CreateNew,
        [IO.FileAccess]::Write,[IO.FileShare]::None)
    try {
        $stream.Write($Bytes,0,$Bytes.Length)
        $stream.Flush($true)
    }
    finally { $stream.Dispose() }
}

function Verify-Intake([string]$Path) {
    $sid = Get-OwnerSid
    $folder = Assert-BoundedOwnerDirectory $Path
    Assert-Acl -Path $folder -Sid $sid -DirectoryExpected $true
    $items = @(Get-ChildItem -LiteralPath $folder -Force)
    if ($items.Count -ne 2 -or
        @($items | Where-Object { $_.Name -notin @($OriginalFilename,$ManifestFilename) }).Count -ne 0) {
        throw "UNEXPECTED_OWNER_PRIVATE_INTAKE_FILES"
    }
    $file = Join-Path $folder $OriginalFilename
    $manifestFile = Join-Path $folder $ManifestFilename
    Assert-Acl -Path $file -Sid $sid -DirectoryExpected $false
    Assert-Acl -Path $manifestFile -Sid $sid -DirectoryExpected $false
    [byte[]]$data = [IO.File]::ReadAllBytes($file)
    Assert-ExactBytes $data
    $manifest = [IO.File]::ReadAllText($manifestFile) | ConvertFrom-Json
    if ($manifest.schema_version -ne 1 -or
        $manifest.content_type -ne "UNADJUDICATED_NEED_PROPOSALS_NOT_GOLD" -or
        $manifest.original_filename -cne $OriginalFilename -or
        $manifest.byte_count -ne $ExpectedBytes -or
        $manifest.sha256 -cne $ExpectedSha256 -or
        $manifest.source_receipt_provenance -ne "INDEPENDENT_AUTHOR_REPORTED_NOT_COORDINATOR_READ") {
        throw "OWNER_PRIVATE_MANIFEST_MISMATCH"
    }
    Write-Output "OWNER_NEED_PROPOSALS_FULL_BYTE_READBACK=PASS"
    Write-Output "OWNER_NEED_PROPOSALS_EXACT_RECEIPT_IDENTITY=PASS"
    Write-Output "CANDIDATES_NOT_GOLD=TRUE"
}

if ($Action -eq "SelfTest") {
    if ($SourcePath -or $Directory) { throw "SELFTEST_FORBIDS_PATH_ARGUMENTS" }
    [byte[]]$fake = [Text.Encoding]::UTF8.GetBytes("FICTITIOUS_NEED_WITH_NO_ADS_CONTENT")
    $expected = Get-Digest $fake
    [byte[]]$changed = [byte[]]$fake.Clone()
    $changed[0] = $changed[0] -bxor 1
    if ((Get-Digest $changed) -ceq $expected) { throw "SYNTHETIC_TAMPER_UNDETECTED" }
    Write-Output "OWNER_NEED_INTAKE_SYNTHETIC_SELFTEST=PASS"
    return
}

if ($Action -eq "Verify") {
    if ($SourcePath) { throw "VERIFY_FORBIDS_SOURCE_PATH" }
    Verify-Intake -Path $Directory
    return
}

if ($Directory) { throw "IMPORT_FORBIDS_CALLER_CHOSEN_DESTINATION" }
$sid = Get-OwnerSid
if ([string]::IsNullOrWhiteSpace($SourcePath)) { throw "DOWNLOAD_FILE_PATH_REQUIRED" }
$source = (Resolve-Path -LiteralPath $SourcePath -ErrorAction Stop).ProviderPath
$sourceItem = Get-Item -LiteralPath $source -Force
if ($sourceItem.PSIsContainer -or ($sourceItem.Attributes -band [IO.FileAttributes]::ReparsePoint) -ne 0) {
    throw "SOURCE_MUST_BE_REGULAR_DOWNLOADED_FILE"
}
if ([IO.Path]::GetFileName($source) -cne $OriginalFilename) {
    throw "EXPECTED_EXACT_RESTRICTED_DOWNLOAD_FILENAME"
}
$repoRoot = [IO.Path]::GetFullPath((Join-Path $PSScriptRoot "..")).TrimEnd('\') + '\'
if ($source.StartsWith($repoRoot,[StringComparison]::OrdinalIgnoreCase)) {
    throw "DO_NOT_STAGE_RESTRICTED_PROPOSALS_INSIDE_PUBLIC_ADS_WORKTREE"
}
[byte[]]$raw = [IO.File]::ReadAllBytes($source)
Assert-ExactBytes $raw

$folder = Assert-BoundedOwnerDirectory (Join-Path $env:LOCALAPPDATA (
    $Prefix + [Guid]::NewGuid().ToString("N")))
New-BoundedFolder -Folder $folder -Sid $sid
$manifest = [ordered]@{
    schema_version = 1
    content_type = "UNADJUDICATED_NEED_PROPOSALS_NOT_GOLD"
    original_filename = $OriginalFilename
    byte_count = $ExpectedBytes
    sha256 = $ExpectedSha256
    source_receipt_provenance = "INDEPENDENT_AUTHOR_REPORTED_NOT_COORDINATOR_READ"
    owner_only_platform_permissions = "NOT_CLAIMED"
    scored_tasks = 0
    reference_answers = 0
}
[byte[]]$manifestBytes = [Text.UTF8Encoding]::new($false).GetBytes(
    ($manifest | ConvertTo-Json -Compress -Depth 4) + [char]10)
Write-NewBytes -Path (Join-Path $folder $OriginalFilename) -Bytes $raw
Write-NewBytes -Path (Join-Path $folder $ManifestFilename) -Bytes $manifestBytes
# Verify without sending proposal content to the exposed ADS coordinator.
$binary = Join-Path $PSHOME "powershell.exe"
& $binary -NoProfile -NonInteractive -ExecutionPolicy Bypass -File $PSCommandPath -Action Verify -Directory $folder
if ($LASTEXITCODE -ne 0) { throw "OWNER_SECOND_PROCESS_READBACK_FAILED" }
Write-Output "OWNER_NEED_PROPOSALS_IMPORT=PASS"
Write-Output "ORIGINAL_DOWNLOAD_REMAINS_AT_SOURCE=TRUE"
Write-Output "LOCAL_OWNER_INTAKE_IS_NOT_QUALIFIED_REAL_GOLD_CUSTODY=TRUE"
Write-Output "OWNER_PRIVATE_DIRECTORY=$folder"
