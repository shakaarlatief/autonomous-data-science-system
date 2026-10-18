#Requires -Version 5.1
<#
R0-P03 fake-only recipient setup and exact ciphertext recovery, owner execution.
Never use with real reference answers, credentials or production private keys.
Prepare: make one new protected owner folder, create fake RSA recipient key/cert,
         export ONLY the public certificate to Downloads.
Receive: import one Downloads CMS ciphertext into that specific owner folder,
         authenticate/decrypt in memory and validate all fictional case slots;
         perform a separate-process readback without printing plaintext.
Verify:  owner-side read-only second-process exact readback.
SelfTest: in-memory synthetic contract/negative-control checks, no file writes.
#>
[CmdletBinding()]
param(
    [ValidateSet("Prepare","Receive","Verify","SelfTest")]
    [string]$Action = "Prepare",
    [string]$OwnerDirectory,
    [string]$Ciphertext,
    [ValidatePattern("^[0-9a-fA-F]{64}$")]
    [string]$ExpectedSha256
)
Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

$Prefix = "ADS-P03-FAKE-RECIPIENT-"
$PrivateName = "fake-private-key.pem"
$CertName = "fake-recipient-cert.pem"
$SavedCms = "received-fake-reference.cms"
$SavedReceipt = "received-fake-receipt.json"
$Marker = "SYNTHETIC_R0P03_DEMONSTRATION_ONLY"
$OpenSsl = "C:\Program Files\Git\usr\bin\openssl.exe"
$Utf8 = New-Object System.Text.UTF8Encoding($false, $true)
$Categories = @(
    "cold_start_current_orientation",
    "cross_plane_discovery",
    "impact_analysis_evolution",
    "exact_source_authority_recovery"
)
function Fail([string]$Code) { throw $Code }
function Digest([byte[]]$Body) {
    $sha = [Security.Cryptography.SHA256]::Create()
    try { return [BitConverter]::ToString($sha.ComputeHash($Body)).Replace("-","").ToLowerInvariant() }
    finally { $sha.Dispose() }
}
function Owner-Sid {
    $identity = [Security.Principal.WindowsIdentity]::GetCurrent()
    if ($null -eq $identity.User -or $identity.User.Value -eq "S-1-5-18" -or
        $identity.Name -match '\\CodexSandbox(Offline|Online)$') {
        Fail "OWNER_DESKTOP_IDENTITY_REQUIRED"
    }
    $p = [Security.Principal.WindowsPrincipal]::new($identity)
    if ($p.IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)) {
        Fail "NON_ELEVATED_OWNER_POWERSHELL_REQUIRED"
    }
    return $identity.User
}
function Canonical-OwnerPath([string]$Value) {
    if ([string]::IsNullOrWhiteSpace($Value)) { Fail "OWNER_FOLDER_REQUIRED" }
    $full = [IO.Path]::GetFullPath($Value)
    $parent = [IO.Path]::GetDirectoryName($full).TrimEnd('\')
    if (-not [string]::Equals($parent, ([IO.Path]::GetFullPath($env:LOCALAPPDATA)).TrimEnd('\'),
        [StringComparison]::OrdinalIgnoreCase)) { Fail "OWNER_FOLDER_OUTSIDE_LOCALAPPDATA" }
    if ([IO.Path]::GetFileName($full) -cnotmatch "^ADS-P03-FAKE-RECIPIENT-[a-f0-9]{32}$") {
        Fail "INVALID_OWNER_FOLDER_NAME"
    }
    return $full
}
function Confirm-Acl([string]$Path, [Security.Principal.SecurityIdentifier]$Sid,
    [bool]$IsDirectory) {
    $item = Get-Item -LiteralPath $Path -Force -ErrorAction Stop
    if ($item.PSIsContainer -ne $IsDirectory -or
        ($item.Attributes -band [IO.FileAttributes]::ReparsePoint) -ne 0) {
        Fail "UNEXPECTED_PATH_TYPE"
    }
    $acl = Get-Acl -LiteralPath $Path
    if ($IsDirectory -and -not $acl.AreAccessRulesProtected) {
        Fail "OWNER_DIRECTORY_MUST_HAVE_PROTECTED_DACL"
    }
    $rules = @($acl.GetAccessRules($true, $true,
        [Security.Principal.SecurityIdentifier]))
    $foundOwner = $false
    $foundSystem = $false
    if ($rules.Count -lt 2) { Fail "OWNER_SYSTEM_RULES_MISSING" }
    foreach ($rule in $rules) {
        if ($rule.AccessControlType -ne [Security.AccessControl.AccessControlType]::Allow -or
            $rule.IdentityReference.Value -notin @($Sid.Value,"S-1-5-18")) {
            Fail "UNEXPECTED_ACL_PRINCIPAL_OR_ACE"
        }
        if ($rule.IdentityReference.Value -eq $Sid.Value) { $foundOwner = $true }
        if ($rule.IdentityReference.Value -eq "S-1-5-18") { $foundSystem = $true }
    }
    if (-not $foundOwner -or -not $foundSystem) { Fail "OWNER_SYSTEM_REQUIRED" }
}
function New-OwnerDirectory([string]$Folder,[Security.Principal.SecurityIdentifier]$Sid) {
    if ([IO.Directory]::Exists($Folder) -or [IO.File]::Exists($Folder)) {
        Fail "OWNER_FOLDER_ALREADY_EXISTS"
    }
    $dacl = [Security.AccessControl.DirectorySecurity]::new()
    $dacl.SetAccessRuleProtection($true,$false)
    $inherit = [Security.AccessControl.InheritanceFlags]::ContainerInherit -bor
        [Security.AccessControl.InheritanceFlags]::ObjectInherit
    foreach ($allowed in @($Sid,[Security.Principal.SecurityIdentifier]::new("S-1-5-18"))) {
        $rule = [Security.AccessControl.FileSystemAccessRule]::new(
            $allowed,[Security.AccessControl.FileSystemRights]::FullControl,
            $inherit,[Security.AccessControl.PropagationFlags]::None,
            [Security.AccessControl.AccessControlType]::Allow)
        $dacl.AddAccessRule($rule)
    }
    [IO.Directory]::CreateDirectory($Folder,$dacl) | Out-Null
    Confirm-Acl -Path $Folder -Sid $Sid -IsDirectory $true
}
function Download-Directory {
    $candidate = Join-Path $env:USERPROFILE "Downloads"
    if (-not [IO.Directory]::Exists($candidate)) { Fail "STANDARD_DOWNLOADS_FOLDER_NOT_FOUND" }
    return [IO.Path]::GetFullPath($candidate)
}
function New-ExactFile([string]$Target,[byte[]]$Data) {
    $stream = [IO.FileStream]::new($Target,[IO.FileMode]::CreateNew,
        [IO.FileAccess]::Write,[IO.FileShare]::None)
    try {
        $stream.Write($Data,0,$Data.Length)
        $stream.Flush($true)
    }
    finally { $stream.Dispose() }
}
function Confirm-Fictional([byte[]]$Raw) {
    if ($Raw.Length -lt 10 -or $Raw.Length -gt 131072) { Fail "FAKE_PACKET_SIZE_OUT_OF_RANGE" }
    try {
        $text = $Utf8.GetString($Raw)
        $doc = $text | ConvertFrom-Json
    }
    catch { Fail "INVALID_FAKE_PACKET_JSON" }
    if (@($doc.PSObject.Properties.Name).Count -ne 4 -or
        @("marker","synthetic_only","legacy","primary" | Where-Object {
            $_ -notin @($doc.PSObject.Properties.Name)
        }).Count -ne 0 -or
        $doc.marker -cne $Marker -or $doc.synthetic_only -ne $true) {
        Fail "FAKE_PACKET_SCHEMA_INVALID"
    }
    if (@($doc.legacy).Count -ne 9 -or @($doc.primary).Count -ne 12) {
        Fail "FAKE_CASE_COUNTS_INVALID"
    }
    for ($n=1; $n -le 9; $n++) {
        $case = $doc.legacy[$n-1]
        if (@($case.PSObject.Properties.Name).Count -ne 3 -or
            $case.id -cne ("legacy-{0:D2}" -f $n) -or
            $case.claim -cne ("FAKE_LEGACY_{0:D2}" -f $n) -or
            $case.source -cne "SYNTHETIC_SOURCE_ONLY") {
            Fail "FAKE_LEGACY_SLOT_INVALID"
        }
    }
    for ($n=1; $n -le 12; $n++) {
        $case = $doc.primary[$n-1]
        $category = $Categories[[int][math]::Floor(($n - 1)/3)]
        if (@($case.PSObject.Properties.Name).Count -ne 4 -or
            $case.id -cne ("primary-{0:D2}" -f $n) -or
            $case.claim -cne ("FAKE_PRIMARY_{0:D2}" -f $n) -or
            $case.category -cne $category -or
            $case.source -cne "SYNTHETIC_SOURCE_ONLY") {
            Fail "FAKE_PRIMARY_SLOT_INVALID"
        }
    }
    return (Digest -Body $Raw)
}
function Invoke-FakeCertificateGeneration([string]$PrivateKey, [string]$Certificate) {
    # Windows PowerShell 5.1 can promote native OpenSSL key-generation
    # progress on stderr to an error record when ErrorActionPreference=Stop.
    # Consume both redirected streams asynchronously, and decide success
    # exclusively from the native process exit code and bounded completion.
    $start = [Diagnostics.ProcessStartInfo]::new()
    $start.FileName = $OpenSsl
    $start.Arguments = ('req -new -x509 -newkey rsa:2048 -nodes -keyout "{0}" -out "{1}" -subj /CN=ADS-P03-SYNTHETIC-OWNER-ONLY -days 7' -f
        $PrivateKey,$Certificate)
    $start.RedirectStandardOutput = $true
    $start.RedirectStandardError = $true
    $start.UseShellExecute = $false
    $start.CreateNoWindow = $true
    $process = [Diagnostics.Process]::new()
    $process.StartInfo = $start
    try {
        if (-not $process.Start()) { Fail "FAKE_CERTIFICATE_PROCESS_START_FAILED" }
        # Drain both pipes without printing progress or native stderr. Using
        # asynchronous drains avoids blocking a process on a full pipe.
        $process.BeginOutputReadLine()
        $process.BeginErrorReadLine()
        if (-not $process.WaitForExit(25000)) {
            $process.Kill()
            $process.WaitForExit()
            Fail "FAKE_CERTIFICATE_GENERATION_TIMEOUT"
        }
        $process.WaitForExit()
        if ($process.ExitCode -ne 0) { Fail "FAKE_CERTIFICATE_GENERATION_FAILED" }
    }
    finally { $process.Dispose() }
}
function Decode-Cms([string]$Source,[string]$Certificate,[string]$PrivateKey) {
    $p = [Diagnostics.ProcessStartInfo]::new()
    $p.FileName = $OpenSsl
    $p.Arguments = ('cms -decrypt -binary -inform DER -in "{0}" -recip "{1}" -inkey "{2}"' -f
        $Source,$Certificate,$PrivateKey)
    $p.RedirectStandardOutput = $true
    $p.RedirectStandardError = $true
    $p.UseShellExecute = $false
    $p.CreateNoWindow = $true
    $process = [Diagnostics.Process]::Start($p)
    $mem = [IO.MemoryStream]::new()
    try {
        $process.StandardOutput.BaseStream.CopyTo($mem)
        $null = $process.StandardError.ReadToEnd()
        if (-not $process.WaitForExit(25000)) {
            $process.Kill()
            Fail "OPENSSL_CMS_TIMEOUT"
        }
        if ($process.ExitCode -ne 0) { Fail "CMS_AUTHENTICATION_OR_DECRYPTION_FAILED" }
        return ,$mem.ToArray()
    }
    finally {
        $process.Dispose()
        $mem.Dispose()
    }
}
function Confirm-Recipient([string]$Folder, [Security.Principal.SecurityIdentifier]$Sid) {
    $folder = Canonical-OwnerPath -Value $Folder
    Confirm-Acl -Path $folder -Sid $Sid -IsDirectory $true
    $key = Join-Path $folder $PrivateName
    $cert = Join-Path $folder $CertName
    Confirm-Acl -Path $key -Sid $Sid -IsDirectory $false
    Confirm-Acl -Path $cert -Sid $Sid -IsDirectory $false
    return @($folder,$cert,$key)
}
function Confirm-VerifiedCipher([string]$Folder,[Security.Principal.SecurityIdentifier]$Sid,
    [string]$Cipher, [string]$Expected) {
    $loc = Confirm-Recipient -Folder $Folder -Sid $Sid
    $source = [IO.Path]::GetFullPath($Cipher)
    if (([IO.Path]::GetDirectoryName($source)) -cne $loc[0] -or
        [IO.Path]::GetFileName($source) -cne $SavedCms) {
        Fail "RECEIPT_SOURCE_NOT_THE_OWNER_CIPHERTEXT"
    }
    Confirm-Acl -Path $source -Sid $Sid -IsDirectory $false
    [byte[]]$raw = Decode-Cms -Source $source -Certificate $loc[1] -PrivateKey $loc[2]
    $calculated = Confirm-Fictional -Raw $raw
    if ($calculated -ne $Expected.ToLowerInvariant()) {
        Fail "COMPLETE_REFERENCE_DIGEST_MISMATCH"
    }
    Write-Output "OWNER_FULL_FAKE_PACKET_RECOVERY=PASS"
    Write-Output "OWNER_FAKE_CASES=9_PLUS_12"
    Write-Output "OWNER_FAKE_PACKET_SHA256=$calculated"
}
if ($Action -eq "SelfTest") {
    if ($OwnerDirectory -or $Ciphertext -or $ExpectedSha256) { Fail "SELFTEST_TAKES_NO_PATHS" }
    $example = [ordered]@{
        marker = $Marker
        synthetic_only = $true
        legacy = @(1..9 | ForEach-Object {
            @{ id=("legacy-{0:D2}" -f $_);claim=("FAKE_LEGACY_{0:D2}" -f $_);source="SYNTHETIC_SOURCE_ONLY" }
        })
        primary = @(1..12 | ForEach-Object {
            @{ id=("primary-{0:D2}" -f $_);category=$Categories[[int][math]::Floor(($_-1)/3)];
               claim=("FAKE_PRIMARY_{0:D2}" -f $_);source="SYNTHETIC_SOURCE_ONLY" }
        })
    }
    [byte[]]$good = $Utf8.GetBytes(($example|ConvertTo-Json -Compress -Depth 8)+[char]10)
    $hash = Confirm-Fictional -Raw $good
    [byte[]]$bad = $good.Clone()
    $bad[0] = $bad[0] -bxor 1
    try {
        $null = Confirm-Fictional -Raw $bad
        Fail "CORRUPTED_FAKE_ACCEPTED"
    }
    catch {
        if ($_.Exception.Message -eq "CORRUPTED_FAKE_ACCEPTED") { throw }
    }
    Write-Output "OWNER_FAKE_RECIPIENT_SELFTEST=PASS"
    Write-Output "EXPECTED_CASES=9_PLUS_12"
    return
}
if (-not [IO.File]::Exists($OpenSsl)) { Fail "EXISTING_GIT_OPENSSL_REQUIRED" }
$sid = Owner-Sid
if ($Action -eq "Prepare") {
    if ($OwnerDirectory -or $Ciphertext -or $ExpectedSha256) {
        Fail "PREPARE_FORBIDS_CALLER_CHOSEN_TARGET"
    }
    $folder = Canonical-OwnerPath -Value (Join-Path $env:LOCALAPPDATA (
        $Prefix+[Guid]::NewGuid().ToString("N")))
    New-OwnerDirectory -Folder $folder -Sid $sid
    $key = Join-Path $folder $PrivateName
    $cert = Join-Path $folder $CertName
    Invoke-FakeCertificateGeneration -PrivateKey $key -Certificate $cert
    $null = Confirm-Recipient -Folder $folder -Sid $sid
    $pubName = ("R0_P03_FAKE_RECIPIENT_CERT_{0}.pem" -f
        ([IO.Path]::GetFileName($folder).Substring($Prefix.Length)))
    $publicFile = Join-Path (Download-Directory) $pubName
    New-ExactFile -Target $publicFile -Data ([IO.File]::ReadAllBytes($cert))
    $publicSha = Digest -Body ([IO.File]::ReadAllBytes($publicFile))
    Write-Output "FAKE_PUBLIC_CERT_PREPARED=PASS"
    Write-Output "FAKE_OWNER_PRIVATE_FOLDER=$folder"
    Write-Output "FAKE_PUBLIC_CERT_PATH=$publicFile"
    Write-Output "FAKE_PUBLIC_CERT_SHA256=$publicSha"
    Write-Output "NO_REAL_GOLD_OR_PRODUCTION_KEYS=TRUE"
    return
}
if ($Action -eq "Receive") {
    if (-not $OwnerDirectory -or -not $Ciphertext -or $ExpectedSha256) {
        Fail "RECEIVE_REQUIRES_OWNER_FOLDER_AND_CIPHERTEXT_ONLY"
    }
    $loc = Confirm-Recipient -Folder $OwnerDirectory -Sid $sid
    $downloads = (Download-Directory).TrimEnd('\')
    $source = [IO.Path]::GetFullPath($Ciphertext)
    if (-not [string]::Equals([IO.Path]::GetDirectoryName($source).TrimEnd('\'),
        $downloads,[StringComparison]::OrdinalIgnoreCase) -or
        [IO.Path]::GetFileName($source) -cne "R0_P03_FAKE_AUTHOR_PACKET.cms") {
        Fail "ONLY_EXACT_DOWNLOADS_CMS_FILENAME_PERMITTED"
    }
    $entry = Get-Item -LiteralPath $source -ErrorAction Stop
    if (($entry.Attributes -band [IO.FileAttributes]::ReparsePoint) -ne 0 -or
        $entry.PSIsContainer -or $entry.Length -lt 100 -or $entry.Length -gt 262144) {
        Fail "CMS_FILE_TYPE_OR_SIZE_INVALID"
    }
    [byte[]]$encrypted = [IO.File]::ReadAllBytes($source)
    $stored = Join-Path $loc[0] $SavedCms
    if ([IO.File]::Exists($stored) -or [IO.File]::Exists((Join-Path $loc[0] $SavedReceipt))) {
        Fail "RECEIPT_ALREADY_PRESENT_REFUSE_OVERWRITE"
    }
    # Check AEAD and exact fictional contents *before* retaining the envelope.
    [byte[]]$raw = Decode-Cms -Source $source -Certificate $loc[1] -PrivateKey $loc[2]
    $plainSha = Confirm-Fictional -Raw $raw
    New-ExactFile -Target $stored -Data $encrypted
    $receipt = [ordered]@{
        synthetic_only=$true;marker=$Marker;format="fake-recipient-cms-handoff-v1"
        ciphertext_sha256=(Digest -Body $encrypted);packet_sha256=$plainSha
        fictional_legacy_cases=9;fictional_primary_cases=12
        received_utc=[DateTime]::UtcNow.ToString("o")
    }
    $receiptBytes = $Utf8.GetBytes(($receipt|ConvertTo-Json -Compress -Depth 5)+[char]10)
    New-ExactFile -Target (Join-Path $loc[0] $SavedReceipt) -Data $receiptBytes
    $ownerShell = Join-Path $PSHOME "powershell.exe"
    & $ownerShell -NoProfile -NonInteractive -ExecutionPolicy Bypass -File $PSCommandPath -Action Verify -OwnerDirectory $loc[0] -ExpectedSha256 $plainSha
    if ($LASTEXITCODE -ne 0) { Fail "FRESH_OWNER_PROCESS_RECOVERY_FAILED" }
    Write-Output "FAKE_OWNER_ENCRYPTED_HANDOFF_RECEIVED=PASS"
    Write-Output "FAKE_CMS_SHA256=$($receipt.ciphertext_sha256)"
    Write-Output "FAKE_PACKET_SHA256=$plainSha"
    Write-Output "NO_REAL_GOLD_OR_PRODUCTION_KEYS=TRUE"
    return
}
if ($Action -eq "Verify") {
    if (-not $OwnerDirectory -or -not $ExpectedSha256 -or $Ciphertext) {
        Fail "VERIFY_ARGUMENTS_INVALID"
    }
    $loc = Confirm-Recipient -Folder $OwnerDirectory -Sid $sid
    $saved = Join-Path $loc[0] $SavedCms
    $storedReceipt = Join-Path $loc[0] $SavedReceipt
    Confirm-Acl -Path $storedReceipt -Sid $sid -IsDirectory $false
    $receipt = [IO.File]::ReadAllText($storedReceipt,$Utf8)|ConvertFrom-Json
    if ($receipt.synthetic_only -ne $true -or $receipt.marker -cne $Marker -or
        $receipt.fictional_legacy_cases -ne 9 -or $receipt.fictional_primary_cases -ne 12 -or
        $receipt.packet_sha256 -ne $ExpectedSha256.ToLowerInvariant() -or
        $receipt.ciphertext_sha256 -ne (Digest -Body ([IO.File]::ReadAllBytes($saved)))) {
        Fail "OWNER_FAKE_RECEIPT_MISMATCH"
    }
    Confirm-VerifiedCipher -Folder $loc[0] -Sid $sid -Cipher $saved -Expected $ExpectedSha256
    return
}
Fail "UNKNOWN_ACTION"
