#Requires -Version 5.1
<#
Owner-executed source-specific historical byte export. Use normal non-elevated
Windows PowerShell, not the exposed Runtime Bridge or a model tool.

The separately retained NEED_SOURCE_BYTE_REQUEST.json is from the original
independent adjudicator. It contains only up to 64 sorted exact historical
paths, no question text, reference answers or scored results. The source
capsule must remain owner-private and is NOT a scored-author source release.
#>
[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)]
    [string]$RequestPath
)
Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"
$Filename = "NEED_SOURCE_BYTE_REQUEST.json"
$ArchiveName = "NEED_SOURCE_EXACT_ORIGINAL_BYTES_RESTRICTED.zip"
$Root = [IO.Path]::GetFullPath((Join-Path $PSScriptRoot "..")).TrimEnd('\')
$Python = Join-Path $Root ".venv\Scripts\python.exe"
if (-not [IO.File]::Exists($Python)) { throw "TRUSTED_REPOSITORY_VENV_PYTHON_MISSING" }
if ([string]::IsNullOrWhiteSpace($env:LOCALAPPDATA)) { throw "OWNER_LOCALAPPDATA_UNAVAILABLE" }
$Id = [Security.Principal.WindowsIdentity]::GetCurrent()
if ($null -eq $Id.User -or $Id.User.Value -eq "S-1-5-18" -or
    $Id.Name -match '\\CodexSandbox(Offline|Online)$') {
    throw "INTERACTIVE_OWNER_PROCESS_REQUIRED"
}
$Principal = [Security.Principal.WindowsPrincipal]::new($Id)
if ($Principal.IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)) {
    throw "NON_ELEVATED_OWNER_POWERSHELL_REQUIRED"
}
$Candidate = (Resolve-Path -LiteralPath $RequestPath -ErrorAction Stop).ProviderPath
$Item = Get-Item -LiteralPath $Candidate -Force
if ($Item.PSIsContainer -or ($Item.Attributes -band [IO.FileAttributes]::ReparsePoint) -ne 0) {
    throw "ORIGINAL_REVIEWER_REQUEST_REGULAR_FILE_REQUIRED"
}
if ([IO.Path]::GetFileName($Candidate) -cne $Filename) {
    throw "UNEXPECTED_RESTRICTED_REQUEST_FILENAME"
}
if ($Candidate.StartsWith(($Root + '\'),[StringComparison]::OrdinalIgnoreCase)) {
    throw "REVIEWER_REQUEST_MUST_NOT_ENTER_PUBLIC_REPOSITORY"
}
if ($Item.Length -lt 25 -or $Item.Length -gt 28000) {
    throw "REVIEWER_REQUEST_FILE_SIZE_OUT_OF_BOUNDS"
}
$Folder = Join-Path $env:LOCALAPPDATA ("ADS-P03-REVIEWED-SOURCE-BYTES-" + [Guid]::NewGuid().ToString("N"))
if ([IO.Directory]::Exists($Folder) -or [IO.File]::Exists($Folder)) {
    throw "NEW_OWNER_FOLDER_COLLISION"
}
$Acl = [Security.AccessControl.DirectorySecurity]::new()
$Acl.SetAccessRuleProtection($true,$false)
$Flags = [Security.AccessControl.InheritanceFlags]::ContainerInherit -bor
    [Security.AccessControl.InheritanceFlags]::ObjectInherit
foreach ($Sid in @($Id.User,[Security.Principal.SecurityIdentifier]::new("S-1-5-18"))) {
    $Rule = [Security.AccessControl.FileSystemAccessRule]::new(
        $Sid,[Security.AccessControl.FileSystemRights]::FullControl,$Flags,
        [Security.AccessControl.PropagationFlags]::None,
        [Security.AccessControl.AccessControlType]::Allow)
    $Acl.AddAccessRule($Rule)
}
[IO.Directory]::CreateDirectory($Folder,$Acl) | Out-Null
$Actual = Get-Acl -LiteralPath $Folder
if (-not $Actual.AreAccessRulesProtected) { throw "OWNER_SOURCE_FOLDER_ACL_INHERITANCE_NOT_PROTECTED" }
$Rules = @($Actual.GetAccessRules($true,$true,[Security.Principal.SecurityIdentifier]))
$AllowSids = @($Id.User.Value,"S-1-5-18")
if (@($Rules | Where-Object {
    $_.AccessControlType -ne [Security.AccessControl.AccessControlType]::Allow -or
    $_.IdentityReference.Value -notin $AllowSids
}).Count -gt 0) { throw "OWNER_SOURCE_FOLDER_UNEXPECTED_ACCESS_RULE" }
foreach ($Wanted in $AllowSids) {
    if ($Wanted -notin @($Rules | ForEach-Object { $_.IdentityReference.Value })) {
        throw "OWNER_SOURCE_FOLDER_EXPECTED_PRINCIPAL_MISSING"
    }
}
Push-Location -LiteralPath $Root
try {
    & $Python -B -m experiments.r0_p03_navigation_probe.need_adjudication_exact_source_bytes . --request $Candidate --owner-destination $Folder
    if ($LASTEXITCODE -ne 0) { throw "EXACT_ORIGINAL_SOURCE_EXPORT_FAILED" }
}
finally { Pop-Location }
$Archive = Join-Path $Folder $ArchiveName
$Contents = @(Get-ChildItem -LiteralPath $Folder -Force)
if ($Contents.Count -ne 1 -or $Contents[0].Name -cne $ArchiveName) {
    throw "OWNER_PRIVATE_SOURCE_FOLDER_UNEXPECTED_MEMBERS"
}
$ActualSource = Get-Item -LiteralPath $Archive -Force
if ($ActualSource.PSIsContainer -or $ActualSource.Length -lt 100) {
    throw "OWNER_RESTRICTED_SOURCE_CAPSULE_NOT_CREATED"
}
$Hash = (Get-FileHash -LiteralPath $Archive -Algorithm SHA256).Hash.ToLowerInvariant()
if ($Hash -notmatch '^[0-9a-f]{64}$') { throw "SOURCE_CAPSULE_HASH_INVALID" }
Write-Output "OWNER_PRIVATE_EXACT_SOURCE_CAPSULE=PASS"
Write-Output "OWNER_SOURCE_CAPSULE_SHA256=$Hash"
Write-Output "OWNER_PRIVATE_SOURCE_CAPSULE_PATH=$Archive"
Write-Output "DO_NOT_PASTE_OWNER_PRIVATE_PATH_OR_SOURCE_REQUEST_IN_COORDINATING_CHAT=TRUE"
