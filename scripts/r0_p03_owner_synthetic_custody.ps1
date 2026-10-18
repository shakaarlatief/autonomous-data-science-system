#Requires -Version 5.1
<#
Owner-executed R0-P03 synthetic custody trial. No real gold or production keys.
Create makes only a new owner-only folder with an atomic protected directory ACL.
Verify checks existing fake 9+12 bytes and manifest without modifying them.
SelfTest tests content generation entirely in memory.
Do not run Create under an ADS agent, Codex sandbox or service identity.
#>
[CmdletBinding()]
param(
    [ValidateSet("Create","Verify","SelfTest")][string]$Action = "Create",
    [string]$Directory,
    [ValidatePattern("^[0-9a-fA-F]{64}$")][string]$ExpectedSha256
)
Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

$Prefix = "ADS-P03-CUSTODY-SYNTHETIC-"
$PacketName = "synthetic-21-reference.json"
$ManifestName = "synthetic-custody-manifest.json"
$Marker = "SYNTHETIC_ONLY_R0_P03_NO_REAL_GOLD"
$Utf8 = New-Object System.Text.UTF8Encoding($false)

function Get-Sha256([byte[]]$Bytes) {
    $h = [System.Security.Cryptography.SHA256]::Create()
    try { return [BitConverter]::ToString($h.ComputeHash($Bytes)).Replace("-","").ToLowerInvariant() }
    finally { $h.Dispose() }
}
function New-FakePacket([string]$Version) {
    if ($Version -notmatch "^ADS-P03-CUSTODY-SYNTHETIC-[a-f0-9]{32}$") {
        throw "INVALID_SYNTHETIC_VERSION"
    }
    $categories = @("cold_start_current_orientation","cross_plane_discovery",
        "impact_analysis_evolution","exact_source_authority_recovery")
    $legacy = @(1..9 | ForEach-Object {
        [ordered]@{
            id = ("legacy-{0:D2}" -f $_)
            claimed_reference = ("FAKE_LEGACY_REFERENCE_{0:D2}" -f $_)
            evidence = "SYNTHETIC_SOURCE_ONLY"
        }
    })
    $primary = @(1..12 | ForEach-Object {
        $n = $_
        [ordered]@{
            id = ("primary-{0:D2}" -f $n)
            category = $categories[[int][math]::Floor(($n - 1) / 3)]
            claimed_reference = ("FAKE_PRIMARY_REFERENCE_{0:D2}" -f $n)
            evidence = "SYNTHETIC_SOURCE_ONLY"
        }
    })
    return [ordered]@{
        synthetic_only = $true
        marker = $Marker
        format = "r0-p03-fabricated-full-reference-v1"
        version = $Version
        source_revision = "SYNTHETIC_SOURCE_ONLY"
        legacy = $legacy
        primary = $primary
    }
}
function Get-PacketBytes([string]$Version) {
    $packet = New-FakePacket -Version $Version
    if ($packet.legacy.Count -ne 9 -or $packet.primary.Count -ne 12) {
        throw "SYNTHETIC_SLOT_COUNT_MISMATCH"
    }
    $categoryCounts = @{}
    foreach ($case in $packet.primary) {
        $name = [string]$case["category"]
        if (-not $categoryCounts.ContainsKey($name)) { $categoryCounts[$name] = 0 }
        $categoryCounts[$name]++
    }
    if ($categoryCounts.Count -ne 4 -or
        @($categoryCounts.Values | Where-Object { $_ -ne 3 }).Count -ne 0) {
        throw "SYNTHETIC_CATEGORY_DISTRIBUTION_MISMATCH"
    }
    [byte[]]$bytes = $Utf8.GetBytes(($packet | ConvertTo-Json -Depth 8 -Compress) + [char]10)
    return ,$bytes
}
function Assert-FakeNegativeControls([byte[]]$Bytes, [string]$Digest) {
    [byte[]]$modified = $Bytes.Clone()
    $modified[0] = $modified[0] -bxor 1
    if ((Get-Sha256 -Bytes $modified) -eq $Digest) { throw "MODIFICATION_NOT_DETECTED" }
    [byte[]]$short = New-Object byte[] ($Bytes.Length - 1)
    [Array]::Copy($Bytes, $short, $short.Length)
    if ((Get-Sha256 -Bytes $short) -eq $Digest) { throw "TRUNCATION_NOT_DETECTED" }
}
function Get-OwnerSid {
    $identity = [System.Security.Principal.WindowsIdentity]::GetCurrent()
    $sid = $identity.User
    if ($null -eq $sid -or $sid.Value -eq "S-1-5-18") {
        throw "OWNER_WINDOWS_IDENTITY_INVALID"
    }
    if ($identity.Name -match '\\CodexSandbox(Offline|Online)$') {
        throw "AGENT_SANDBOX_CANNOT_OWN_CUSTODY"
    }
    $principal = [System.Security.Principal.WindowsPrincipal]::new($identity)
    if ($principal.IsInRole([System.Security.Principal.WindowsBuiltInRole]::Administrator)) {
        throw "RUN_FROM_NON_ELEVATED_OWNER_POWERSHELL"
    }
    return $sid
}
function Confirm-OwnerFolder([string]$Path) {
    if ([string]::IsNullOrWhiteSpace($Path)) { throw "OWNER_FOLDER_REQUIRED" }
    $full = [IO.Path]::GetFullPath($Path)
    $parent = [IO.Path]::GetDirectoryName($full).TrimEnd('\')
    $expected = [IO.Path]::GetFullPath($env:LOCALAPPDATA).TrimEnd('\')
    if (-not [string]::Equals($parent, $expected,
        [StringComparison]::OrdinalIgnoreCase)) { throw "OWNER_FOLDER_OUTSIDE_LOCALAPPDATA" }
    if ([IO.Path]::GetFileName($full) -cnotmatch "^ADS-P03-CUSTODY-SYNTHETIC-[a-f0-9]{32}$") {
        throw "INVALID_OWNER_FOLDER_NAME"
    }
    return $full
}
function Confirm-RestrictedAcl([string]$Path, [System.Security.Principal.SecurityIdentifier]$Owner,
    [bool]$DirectoryRequired) {
    $entry = Get-Item -LiteralPath $Path -Force
    if ($entry.PSIsContainer -ne $DirectoryRequired -or
        ($entry.Attributes -band [IO.FileAttributes]::ReparsePoint) -ne 0) {
        throw "UNEXPECTED_FILE_TYPE_OR_REPARSE_POINT"
    }
    $acl = Get-Acl -LiteralPath $Path
    if ($DirectoryRequired -and -not $acl.AreAccessRulesProtected) {
        throw "OWNER_DIRECTORY_INHERITED_ACL"
    }
    $rules = @($acl.GetAccessRules($true, $true,
        [System.Security.Principal.SecurityIdentifier]))
    if ($rules.Count -lt 2) { throw "OWNER_OR_SYSTEM_ACCESS_MISSING" }
    $ownerFound = $false
    $systemFound = $false
    foreach ($rule in $rules) {
        $sid = $rule.IdentityReference.Value
        if ($rule.AccessControlType -ne [Security.AccessControl.AccessControlType]::Allow -or
            $sid -notin @($Owner.Value, "S-1-5-18")) {
            throw "UNEXPECTED_ACCESS_RULE"
        }
        if ($sid -eq $Owner.Value) { $ownerFound = $true }
        if ($sid -eq "S-1-5-18") { $systemFound = $true }
    }
    if (-not $ownerFound -or -not $systemFound) {
        throw "REQUIRED_OWNER_OR_SYSTEM_RULE_MISSING"
    }
}
function New-RestrictedDirectory([string]$Path,
    [System.Security.Principal.SecurityIdentifier]$Owner) {
    if ([IO.File]::Exists($Path) -or [IO.Directory]::Exists($Path)) {
        throw "EXISTING_DIRECTORY_REFUSED"
    }
    $acl = [Security.AccessControl.DirectorySecurity]::new()
    $acl.SetAccessRuleProtection($true, $false)
    $flags = [Security.AccessControl.InheritanceFlags]::ContainerInherit -bor
        [Security.AccessControl.InheritanceFlags]::ObjectInherit
    foreach ($sid in @($Owner,
        [Security.Principal.SecurityIdentifier]::new("S-1-5-18"))) {
        $acl.AddAccessRule([Security.AccessControl.FileSystemAccessRule]::new(
            $sid, [Security.AccessControl.FileSystemRights]::FullControl,
            $flags, [Security.AccessControl.PropagationFlags]::None,
            [Security.AccessControl.AccessControlType]::Allow))
    }
    [IO.Directory]::CreateDirectory($Path, $acl) | Out-Null
    Confirm-RestrictedAcl -Path $Path -Owner $Owner -DirectoryRequired $true
}
function Write-CreateNewBytes([string]$Path, [byte[]]$Bytes) {
    $stream = [IO.FileStream]::new($Path, [IO.FileMode]::CreateNew,
        [IO.FileAccess]::Write, [IO.FileShare]::None)
    try {
        $stream.Write($Bytes, 0, $Bytes.Length)
        $stream.Flush($true)
    }
    finally { $stream.Dispose() }
}
function Verify-OwnerPacket([string]$Path, [string]$Expected) {
    $path = Confirm-OwnerFolder -Path $Path
    $owner = Get-OwnerSid
    Confirm-RestrictedAcl -Path $path -Owner $owner -DirectoryRequired $true
    $names = @((Get-ChildItem -LiteralPath $path -Force).Name)
    if ($names.Count -ne 2 -or
        @($names | Where-Object { $_ -notin @($PacketName,$ManifestName) }).Count -ne 0) {
        throw "UNEXPECTED_CUSTODY_FILE_ROSTER"
    }
    $packetPath = Join-Path $path $PacketName
    $manifestPath = Join-Path $path $ManifestName
    Confirm-RestrictedAcl -Path $packetPath -Owner $owner -DirectoryRequired $false
    Confirm-RestrictedAcl -Path $manifestPath -Owner $owner -DirectoryRequired $false
    [byte[]]$raw = [IO.File]::ReadAllBytes($packetPath)
    $digest = Get-Sha256 -Bytes $raw
    if ($digest -ne $Expected.ToLowerInvariant()) {
        throw "OWNER_PACKET_DIGEST_MISMATCH"
    }
    $version = [IO.Path]::GetFileName($path)
    [byte[]]$again = Get-PacketBytes -Version $version
    if ($raw.Length -ne $again.Length -or $digest -ne (Get-Sha256 -Bytes $again)) {
        throw "NON_SYNTHETIC_PACKET_OR_CONTENT_CHANGE"
    }
    $manifest = [IO.File]::ReadAllText($manifestPath, $Utf8) | ConvertFrom-Json
    if ($manifest.synthetic_only -ne $true -or $manifest.marker -ne $Marker -or
        $manifest.version -ne $version -or $manifest.packet_file -ne $PacketName -or
        $manifest.packet_sha256 -ne $digest -or $manifest.packet_bytes -ne $raw.Length -or
        $manifest.legacy_count -ne 9 -or $manifest.primary_count -ne 12) {
        throw "CUSTODY_MANIFEST_MISMATCH"
    }
    Assert-FakeNegativeControls -Bytes $raw -Digest $digest
    Write-Output "COMPLETE_SYNTHETIC_PACKET_READBACK=PASS"
    Write-Output "NINE_PLUS_TWELVE_CASES=PASS"
    Write-Output "CUSTODY_PACKET_SHA256=$digest"
}
if ($Action -eq "SelfTest") {
    [byte[]]$bytes = Get-PacketBytes -Version ($Prefix + ("a" * 32))
    Assert-FakeNegativeControls -Bytes $bytes -Digest (Get-Sha256 -Bytes $bytes)
    Write-Output "SYNTHETIC_SELFTEST=PASS"
    Write-Output "NINE_PLUS_TWELVE_CASES=PASS"
    return
}
if ($Action -eq "Verify") {
    if (-not $ExpectedSha256) { throw "EXPECTED_SHA256_REQUIRED" }
    Verify-OwnerPacket -Path $Directory -Expected $ExpectedSha256
    return
}
if ($Directory -or $ExpectedSha256) {
    throw "CREATE_FORBIDS_CALLER_SELECTED_FOLDER_OR_DIGEST"
}
$ownerSid = Get-OwnerSid
$folder = Confirm-OwnerFolder -Path (Join-Path $env:LOCALAPPDATA (
    $Prefix + [Guid]::NewGuid().ToString("N")))
New-RestrictedDirectory -Path $folder -Owner $ownerSid
$version = [IO.Path]::GetFileName($folder)
[byte[]]$packet = Get-PacketBytes -Version $version
$sha = Get-Sha256 -Bytes $packet
$manifest = [ordered]@{
    marker = $Marker
    synthetic_only = $true
    version = $version
    packet_file = $PacketName
    packet_sha256 = $sha
    packet_bytes = $packet.Length
    legacy_count = 9
    primary_count = 12
    source_scope = "SYNTHETIC_SOURCE_ONLY"
    created_utc = [DateTime]::UtcNow.ToString("o")
}
[byte[]]$manifestBytes = $Utf8.GetBytes(
    ($manifest | ConvertTo-Json -Compress -Depth 5) + [char]10)
Write-CreateNewBytes -Path (Join-Path $folder $PacketName) -Bytes $packet
Write-CreateNewBytes -Path (Join-Path $folder $ManifestName) -Bytes $manifestBytes

# A fresh PowerShell process verifies the exact completed packet. The process-
# scoped execution-policy argument makes no persistent system policy change.
$binary = Join-Path $PSHOME "powershell.exe"
& $binary -NoProfile -NonInteractive -ExecutionPolicy Bypass -File $PSCommandPath -Action Verify -Directory $folder -ExpectedSha256 $sha
if ($LASTEXITCODE -ne 0) { throw "NEW_PROCESS_RECOVERY_FAILED" }
Write-Output "OWNER_SYNTHETIC_CUSTODY_DIRECTORY=$folder"
Write-Output "OWNER_SYNTHETIC_CUSTODY_SHA256=$sha"
Write-Output "OWNER_SYNTHETIC_CUSTODY_CREATION=PASS"
Write-Output "REAL_GOLD_OR_KEYS_USED=FALSE"
