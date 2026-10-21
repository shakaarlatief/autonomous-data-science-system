#Requires -Version 5.1
<#
A narrowly bounded, owner-executed recipient for ONE fictional-only R0-P03
source-status reviewer handoff. Not a real-source reviewer store or gold handler.

SelfTest: Pure fake JSON parsing and rejection checks; no owner files or keys.
Prepare:  Non-elevated owner creates a NEW LocalAppData direct child with an
          owner+SYSTEM-only protected DACL and disposable fake RSA key/cert.
          Export only a public certificate into the standard Downloads folder.
Receive:  Owner imports the exact named fake CMS from Downloads, checks the
          supplied ciphertext SHA-256, authenticates CMS AEAD, validates the
          COMPLETE three-record fictional report, stores ciphertext only,
          then verifies in a new owner PowerShell process.
Verify:   Reopens the exact owner's saved ciphertext/receipt, reauthenticates
          the FULL fictional report, and prints a fixed success status.

Never attach/share private keys, private owner paths or decrypted report text.
This is intentionally separate from r0_p03_fake_public_recipient.ps1, which
retains the old, incompatible fixed 9+12 reference-packet format.
#>
[CmdletBinding()]
param(
    [ValidateSet("SelfTest","Prepare","Receive","Verify")]
    [string]$Action = "SelfTest",
    [string]$OwnerDirectory,
    [string]$Ciphertext,
    [ValidatePattern("^[0-9a-fA-F]{64}$")]
    [string]$ExpectedSha256
)
Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

$OwnerPrefix = "ADS-P03-FAKE-REVIEW-"
$PublicPrefix = "R0_P03_FAKE_REVIEW_RECIPIENT_CERT_"
$ExpectedCmsName = "R0_P03_FAKE_REVIEWER_REPORT.cms"
$SavedCmsName = "received-fake-reviewer-report.cms"
$SavedReceiptName = "received-fake-reviewer-receipt.json"
$PrivateKeyName = "fake-reviewer-private.pem"
$PublicCertName = "fake-reviewer-public.pem"
$Marker = "S1_FICTIONAL_REVIEWER_REPORT_NO_REAL_PROJECT_MATERIAL"
$Format = "s1-fictional-reviewer-report-v1"
$Manifest = "s1-fictional-three-record-source-manifest-v1"
$OpenSsl = "C:\Program Files\Git\usr\bin\openssl.exe"
$Utf8 = New-Object System.Text.UTF8Encoding($false, $true)
$FakeSourceDigests = @{
    s1_fake_history = "d34d29ed3ed27585db4133db17aaefa93f12bad830caec08f838a51cd1794adc"
    s1_fake_rule = "ba73e1e610e2f462dbc70a7690a600d378aab350238fc5601fab35f849d2b875"
    s1_fake_design = "4c4a59a8983a20c37fe21653467eb26286e3e685c0d99752df3754ea508890de"
}
$KnownNotes = @(
    "FAKE_NOTE_OBSERVATION_ONLY",
    "FAKE_NOTE_CONTROLLING_EXCEPTION",
    "FAKE_NOTE_RESTRICTED_DESIGN_CUE",
    "FAKE_NOTE_MISSING_SOURCE_BYTES",
    "FAKE_NOTE_UNINSPECTED_REPRESENTATION"
)
$DispositionTokens = @(
    "CANDIDATE_FULL", "CANDIDATE_EXCERPT", "AUXILIARY_EVIDENCE_ONLY",
    "PROHIBIT_DESIGN_OR_GOLD", "HOLD_FOR_SOURCE_REVIEW", "UNSUPPORTED_REPRESENTATION"
)

function Fail([string]$Code) { throw $Code }
function Get-Digest([byte[]]$Bytes) {
    $hash = [Security.Cryptography.SHA256]::Create()
    try { return [BitConverter]::ToString($hash.ComputeHash($Bytes)).Replace("-","").ToLowerInvariant() }
    finally { $hash.Dispose() }
}
function Require-ExactFields([object]$Object,[string[]]$Expected,[string]$Reason) {
    if ($null -eq $Object -or $Object -isnot [pscustomobject]) { Fail $Reason }
    $actual = @($Object.PSObject.Properties.Name)
    if ($actual.Count -ne $Expected.Count) { Fail $Reason }
    foreach ($field in $Expected) {
        if ($field -cnotin $actual) { Fail $Reason }
    }
}
function Assert-Bool([object]$Value,[bool]$MustEqual,[bool]$RequireValue) {
    if ($Value -isnot [bool]) { Fail "FAKE_BOOLEAN_TYPE_INVALID" }
    if ($RequireValue -and $Value -ne $MustEqual) { Fail "FAKE_BOOLEAN_VALUE_INVALID" }
}
function Confirm-FakeReviewerReport([byte[]]$Raw) {
    # This function validates an invented closed schema only. It cannot
    # adjudicate real documents or validate independent reviewer identities.
    if ($null -eq $Raw -or $Raw.Length -lt 50 -or $Raw.Length -gt 16384) {
        Fail "FAKE_REVIEWER_REPORT_SIZE_INVALID"
    }
    try {
        $text = $Utf8.GetString($Raw)
        $obj = $text | ConvertFrom-Json -ErrorAction Stop
    }
    catch { Fail "FAKE_REVIEWER_REPORT_JSON_INVALID" }
    Require-ExactFields -Object $obj -Expected @(
        "format","marker","manifest","synthetic_only","reviewer_exposure",
        "challenge","actual_independent_actor_verified",
        "real_source_reviewed","source_world_admitted","records"
    ) -Reason "FAKE_REVIEWER_REPORT_TOP_FIELDS_INVALID"
    if ($obj.format -cne $Format -or $obj.marker -cne $Marker -or
        $obj.manifest -cne $Manifest -or $obj.reviewer_exposure -cnotin
        @("DECLARED_SYNTHETIC_ONLY_UNVERIFIED","UNKNOWN") -or
        $obj.challenge -cnotin @("NOT_CHALLENGED","DISPUTED")) {
        Fail "FAKE_REVIEWER_REPORT_IDENTITY_INVALID"
    }
    Assert-Bool -Value $obj.synthetic_only -MustEqual $true -RequireValue $true
    foreach ($property in @(
        "actual_independent_actor_verified","real_source_reviewed","source_world_admitted"
    )) {
        Assert-Bool -Value $obj.$property -MustEqual $false -RequireValue $true
    }
    if ($obj.records -isnot [array] -or @($obj.records).Count -ne 3) {
        Fail "FAKE_REVIEWER_REPORT_INCOMPLETE"
    }
    $seen = @{}
    foreach ($rec in $obj.records) {
        Require-ExactFields -Object $rec -Expected @(
            "source_id","source_sha256","delivered","inspected",
            "scope","disposition","private_notes"
        ) -Reason "FAKE_REVIEWER_RECORD_FIELDS_INVALID"
        $sourceId = $rec.source_id
        if ($sourceId -isnot [string] -or -not $FakeSourceDigests.ContainsKey($sourceId) -or
            $seen.ContainsKey($sourceId)) { Fail "FAKE_REVIEWER_SOURCE_ROSTER_INVALID" }
        $seen[$sourceId] = $true
        if ($rec.source_sha256 -cne $FakeSourceDigests[$sourceId]) {
            Fail "FAKE_REVIEWER_SOURCE_SHA256_INVALID"
        }
        Assert-Bool -Value $rec.delivered -MustEqual $false -RequireValue $false
        Assert-Bool -Value $rec.inspected -MustEqual $false -RequireValue $false
        if ($rec.scope -cnotin @("COMPLETE_FILE","EXACT_SPAN","REPRESENTATION_COMPONENT") -or
            $rec.disposition -cnotin $DispositionTokens) {
            Fail "FAKE_REVIEWER_DISPOSITION_INVALID"
        }
        if (-not $rec.delivered) {
            if ($rec.inspected -or $rec.disposition -cne "HOLD_FOR_SOURCE_REVIEW") {
                Fail "FAKE_REVIEWER_MISSING_SOURCE_MUST_HOLD"
            }
        }
        elseif (-not $rec.inspected -and $rec.disposition -cnotin
            @("HOLD_FOR_SOURCE_REVIEW","UNSUPPORTED_REPRESENTATION")) {
            Fail "FAKE_REVIEWER_UNINSPECTED_SOURCE_MUST_HOLD"
        }
        if (($rec.disposition -ceq "CANDIDATE_FULL" -and
                $rec.scope -cne "COMPLETE_FILE") -or
            ($rec.disposition -ceq "CANDIDATE_EXCERPT" -and
                $rec.scope -cne "EXACT_SPAN") -or
            ($rec.disposition -ceq "UNSUPPORTED_REPRESENTATION" -and
                $rec.scope -cne "REPRESENTATION_COMPONENT")) {
            Fail "FAKE_REVIEWER_SCOPE_INVALID"
        }
        if ($rec.private_notes -isnot [array] -or
            @($rec.private_notes).Count -lt 1 -or @($rec.private_notes).Count -gt 3) {
            Fail "FAKE_REVIEWER_PRIVATE_NOTE_SHAPE_INVALID"
        }
        $usedNotes = @{}
        foreach ($note in $rec.private_notes) {
            if ($note -isnot [string] -or $note -cnotin $KnownNotes -or
                $usedNotes.ContainsKey($note)) {
                Fail "FAKE_REVIEWER_PRIVATE_NOTE_INVALID"
            }
            $usedNotes[$note] = $true
        }
    }
    if ($seen.Count -ne 3) { Fail "FAKE_REVIEWER_ROSTER_INCOMPLETE" }
    return (Get-Digest -Bytes $Raw)
}
function Owner-Sid {
    $identity = [Security.Principal.WindowsIdentity]::GetCurrent()
    if ($null -eq $identity.User -or $identity.User.Value -eq "S-1-5-18" -or
        $identity.Name -match '\\CodexSandbox(Offline|Online)$') {
        Fail "OWNER_DESKTOP_IDENTITY_REQUIRED"
    }
    $principal = [Security.Principal.WindowsPrincipal]::new($identity)
    if ($principal.IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)) {
        Fail "NON_ELEVATED_OWNER_POWERSHELL_REQUIRED"
    }
    return $identity.User
}
function Get-OwnerRoot([string]$OwnerFolder) {
    if ([string]::IsNullOrWhiteSpace($OwnerFolder)) { Fail "OWNER_FOLDER_REQUIRED" }
    $full = [IO.Path]::GetFullPath($OwnerFolder)
    $parent = [IO.Path]::GetDirectoryName($full).TrimEnd('\')
    $local = ([IO.Path]::GetFullPath($env:LOCALAPPDATA)).TrimEnd('\')
    if (-not [string]::Equals($parent,$local,[StringComparison]::OrdinalIgnoreCase) -or
        [IO.Path]::GetFileName($full) -cnotmatch
        "^ADS-P03-FAKE-REVIEW-[a-f0-9]{32}$") {
        Fail "FAKE_REVIEWER_OWNER_FOLDER_NOT_APPROVED"
    }
    return $full
}
function Confirm-OwnerAcl([string]$Path,[Security.Principal.SecurityIdentifier]$Sid,
    [bool]$IsDirectory) {
    $item = Get-Item -LiteralPath $Path -Force -ErrorAction Stop
    if ($item.PSIsContainer -ne $IsDirectory -or
        ($item.Attributes -band [IO.FileAttributes]::ReparsePoint) -ne 0) {
        Fail "FAKE_REVIEWER_UNEXPECTED_PATH_TYPE"
    }
    $acl = Get-Acl -LiteralPath $Path
    if ($IsDirectory -and -not $acl.AreAccessRulesProtected) {
        Fail "FAKE_REVIEWER_ACL_INHERITANCE_NOT_DISABLED"
    }
    $rules = @($acl.GetAccessRules($true,$true,
        [Security.Principal.SecurityIdentifier]))
    if ($rules.Count -lt 2) { Fail "FAKE_REVIEWER_ACL_RULES_MISSING" }
    $foundOwner = $false
    $foundSystem = $false
    foreach ($rule in $rules) {
        if ($rule.AccessControlType -ne [Security.AccessControl.AccessControlType]::Allow -or
            $rule.IdentityReference.Value -notin @($Sid.Value,"S-1-5-18")) {
            Fail "FAKE_REVIEWER_ACL_UNEXPECTED_PRINCIPAL"
        }
        if ($rule.IdentityReference.Value -eq $Sid.Value) { $foundOwner = $true }
        if ($rule.IdentityReference.Value -eq "S-1-5-18") { $foundSystem = $true }
    }
    if (-not $foundOwner -or -not $foundSystem) { Fail "FAKE_REVIEWER_ACL_INCOMPLETE" }
}
function New-OwnerFolder([string]$Folder,[Security.Principal.SecurityIdentifier]$Sid) {
    if ([IO.Directory]::Exists($Folder) -or [IO.File]::Exists($Folder)) {
        Fail "FAKE_REVIEWER_OWNER_FOLDER_EXISTS"
    }
    $dacl = [Security.AccessControl.DirectorySecurity]::new()
    $dacl.SetAccessRuleProtection($true,$false)
    $inherit = [Security.AccessControl.InheritanceFlags]::ObjectInherit -bor
        [Security.AccessControl.InheritanceFlags]::ContainerInherit
    foreach ($allowed in @($Sid,[Security.Principal.SecurityIdentifier]::new("S-1-5-18"))) {
        $dacl.AddAccessRule([Security.AccessControl.FileSystemAccessRule]::new(
            $allowed,[Security.AccessControl.FileSystemRights]::FullControl,
            $inherit,[Security.AccessControl.PropagationFlags]::None,
            [Security.AccessControl.AccessControlType]::Allow))
    }
    [IO.Directory]::CreateDirectory($Folder,$dacl) | Out-Null
    Confirm-OwnerAcl -Path $Folder -Sid $Sid -IsDirectory $true
}
function Write-NewFile([string]$Target,[byte[]]$Data) {
    $file = [IO.FileStream]::new($Target,[IO.FileMode]::CreateNew,
        [IO.FileAccess]::Write,[IO.FileShare]::None)
    try {
        $file.Write($Data,0,$Data.Length)
        $file.Flush($true)
    }
    finally { $file.Dispose() }
}
function Get-Downloads {
    $download = Join-Path $env:USERPROFILE "Downloads"
    if (-not [IO.Directory]::Exists($download)) { Fail "OWNER_STANDARD_DOWNLOADS_MISSING" }
    return [IO.Path]::GetFullPath($download)
}
function Invoke-NewFakeCertificate([string]$Private,[string]$Certificate) {
    # Native OpenSSL keygen emits progress on stderr. Windows PowerShell 5.1
    # may turn redirected progress into a terminating NativeCommandError.
    # Use direct process APIs and determine outcome solely from exit status.
    $psi = [Diagnostics.ProcessStartInfo]::new()
    $psi.FileName = $OpenSsl
    $psi.Arguments = ('req -new -x509 -newkey rsa:2048 -nodes -keyout "{0}" -out "{1}" -subj /CN=ADS-P03-S1-FAKE-REVIEWER -days 7' -f $Private,$Certificate)
    $psi.RedirectStandardOutput = $true
    $psi.RedirectStandardError = $true
    $psi.UseShellExecute = $false
    $psi.CreateNoWindow = $true
    $process = [Diagnostics.Process]::new()
    $process.StartInfo = $psi
    try {
        if (-not $process.Start()) { Fail "FAKE_REVIEWER_OPENSSL_START_FAILED" }
        $process.BeginOutputReadLine()
        $process.BeginErrorReadLine()
        if (-not $process.WaitForExit(25000)) {
            $process.Kill()
            $process.WaitForExit()
            Fail "FAKE_REVIEWER_OPENSSL_KEYGEN_TIMEOUT"
        }
        $process.WaitForExit()
        if ($process.ExitCode -ne 0) { Fail "FAKE_REVIEWER_OPENSSL_KEYGEN_FAILED" }
    }
    finally { $process.Dispose() }
}
function Decode-FakeCms([string]$Saved,[string]$Cert,[string]$Private) {
    $psi = [Diagnostics.ProcessStartInfo]::new()
    $psi.FileName = $OpenSsl
    $psi.Arguments = ('cms -decrypt -binary -inform DER -in "{0}" -recip "{1}" -inkey "{2}"' -f $Saved,$Cert,$Private)
    $psi.RedirectStandardOutput = $true
    $psi.RedirectStandardError = $true
    $psi.UseShellExecute = $false
    $psi.CreateNoWindow = $true
    $process = [Diagnostics.Process]::Start($psi)
    $memory = [IO.MemoryStream]::new()
    try {
        $process.StandardOutput.BaseStream.CopyTo($memory)
        $null = $process.StandardError.ReadToEnd()
        if (-not $process.WaitForExit(25000)) {
            $process.Kill()
            Fail "FAKE_REVIEWER_CMS_TIMEOUT"
        }
        if ($process.ExitCode -ne 0) {
            # OpenSSL AEAD can produce unauthenticated provisional stdout.
            # It must NEVER be returned, printed or saved on failure.
            Fail "FAKE_REVIEWER_CMS_AUTHENTICATION_FAILED"
        }
        if ($memory.Length -gt 16384) { Fail "FAKE_REVIEWER_CMS_CONTENT_TOO_LARGE" }
        return ,$memory.ToArray()
    }
    finally {
        $process.Dispose()
        $memory.Dispose()
    }
}
function Get-Recipient([string]$OwnerFolder,[Security.Principal.SecurityIdentifier]$Sid) {
    $root = Get-OwnerRoot -OwnerFolder $OwnerFolder
    Confirm-OwnerAcl -Path $root -Sid $Sid -IsDirectory $true
    $key = Join-Path $root $PrivateKeyName
    $cert = Join-Path $root $PublicCertName
    Confirm-OwnerAcl -Path $key -Sid $Sid -IsDirectory $false
    Confirm-OwnerAcl -Path $cert -Sid $Sid -IsDirectory $false
    return @($root,$cert,$key)
}
function Verify-Saved([string]$Folder,[Security.Principal.SecurityIdentifier]$Sid,
    [string]$Expected) {
    $loc = Get-Recipient -OwnerFolder $Folder -Sid $Sid
    $source = Join-Path $loc[0] $SavedCmsName
    $receipt = Join-Path $loc[0] $SavedReceiptName
    Confirm-OwnerAcl -Path $source -Sid $Sid -IsDirectory $false
    Confirm-OwnerAcl -Path $receipt -Sid $Sid -IsDirectory $false
    $saved = [IO.File]::ReadAllBytes($source)
    if ($saved.Length -lt 100 -or $saved.Length -gt 65536 -or
        (Get-Digest -Bytes $saved) -cne $Expected.ToLowerInvariant()) {
        Fail "FAKE_REVIEWER_SAVED_CIPHERTEXT_MISMATCH"
    }
    try { $record = [IO.File]::ReadAllText($receipt,$Utf8) | ConvertFrom-Json -ErrorAction Stop }
    catch { Fail "FAKE_REVIEWER_RECEIPT_INVALID" }
    Require-ExactFields -Object $record -Expected @(
        "synthetic_only","report_format","ciphertext_sha256","private_report_sha256"
    ) -Reason "FAKE_REVIEWER_RECEIPT_FIELDS_INVALID"
    Assert-Bool -Value $record.synthetic_only -MustEqual $true -RequireValue $true
    if ($record.report_format -cne $Format -or
        $record.ciphertext_sha256 -cne $Expected.ToLowerInvariant() -or
        $record.private_report_sha256 -cnotmatch "^[0-9a-f]{64}$") {
        Fail "FAKE_REVIEWER_RECEIPT_HASH_INVALID"
    }
    [byte[]]$raw = Decode-FakeCms -Saved $source -Cert $loc[1] -Private $loc[2]
    $plainSha = Confirm-FakeReviewerReport -Raw $raw
    if ($plainSha -cne $record.private_report_sha256) {
        Fail "FAKE_REVIEWER_COMPLETE_READBACK_MISMATCH"
    }
    Write-Output "S1_OWNER_FAKE_REVIEWER_FULL_READBACK=PASS"
    Write-Output "S1_OWNER_FAKE_RECORDS=3"
    Write-Output "S1_OWNER_REAL_REVIEW_CUSTODY_QUALIFIED=FALSE"
}
if ($Action -eq "SelfTest") {
    if ($OwnerDirectory -or $Ciphertext -or $ExpectedSha256) { Fail "SELFTEST_FORBIDS_PATH_ARGUMENTS" }
    $test = [ordered]@{
        format=$Format; marker=$Marker; manifest=$Manifest
        synthetic_only=$true
        reviewer_exposure="DECLARED_SYNTHETIC_ONLY_UNVERIFIED"
        challenge="NOT_CHALLENGED"
        actual_independent_actor_verified=$false
        real_source_reviewed=$false
        source_world_admitted=$false
        records=@(
            [ordered]@{
                source_id="s1_fake_history";source_sha256=$FakeSourceDigests["s1_fake_history"]
                delivered=$true;inspected=$true;scope="COMPLETE_FILE"
                disposition="CANDIDATE_FULL";private_notes=@("FAKE_NOTE_OBSERVATION_ONLY")
            },
            [ordered]@{
                source_id="s1_fake_rule";source_sha256=$FakeSourceDigests["s1_fake_rule"]
                delivered=$false;inspected=$false;scope="EXACT_SPAN"
                disposition="HOLD_FOR_SOURCE_REVIEW";private_notes=@("FAKE_NOTE_MISSING_SOURCE_BYTES")
            },
            [ordered]@{
                source_id="s1_fake_design";source_sha256=$FakeSourceDigests["s1_fake_design"]
                delivered=$true;inspected=$true;scope="COMPLETE_FILE"
                disposition="PROHIBIT_DESIGN_OR_GOLD";private_notes=@("FAKE_NOTE_RESTRICTED_DESIGN_CUE")
            }
        )
    }
    [byte[]]$payload = $Utf8.GetBytes(($test | ConvertTo-Json -Compress -Depth 12)+[char]10)
    $null = Confirm-FakeReviewerReport -Raw $payload
    $bad = $Utf8.GetBytes(($test | ConvertTo-Json -Compress -Depth 12).Replace(
        "FAKE_NOTE_RESTRICTED_DESIGN_CUE","NOT_A_VALID_FAKE_NOTE")+[char]10)
    $rejected = $false
    try { $null = Confirm-FakeReviewerReport -Raw $bad }
    catch { $rejected = $true }
    if (-not $rejected) { Fail "FAKE_REVIEWER_SELFTEST_NEGATIVE_FAILED" }
    Write-Output "S1_FAKE_REVIEWER_RECIPIENT_SELFTEST=PASS"
    Write-Output "S1_OWNER_ACCOUNT_AND_FILES_UNTOUCHED=TRUE"
    return
}
if (-not [IO.File]::Exists($OpenSsl)) { Fail "EXISTING_GIT_OPENSSL_REQUIRED" }
$sid = Owner-Sid
if ($Action -eq "Prepare") {
    if ($OwnerDirectory -or $Ciphertext -or $ExpectedSha256) {
        Fail "PREPARE_FORBIDS_CALLER_PATHS"
    }
    $root = Get-OwnerRoot -OwnerFolder (Join-Path $env:LOCALAPPDATA (
        $OwnerPrefix+[Guid]::NewGuid().ToString("N")))
    New-OwnerFolder -Folder $root -Sid $sid
    $private = Join-Path $root $PrivateKeyName
    $public = Join-Path $root $PublicCertName
    Invoke-NewFakeCertificate -Private $private -Certificate $public
    $null = Get-Recipient -OwnerFolder $root -Sid $sid
    $file = Join-Path (Get-Downloads) (
        $PublicPrefix+[IO.Path]::GetFileName($root).Substring($OwnerPrefix.Length)+".pem")
    Write-NewFile -Target $file -Data ([IO.File]::ReadAllBytes($public))
    Write-Output "S1_FAKE_REVIEW_RECIPIENT_PREPARED=PASS"
    Write-Output "S1_FAKE_OWNER_DIRECTORY=$root"
    Write-Output "S1_FAKE_PUBLIC_CERT_PATH=$file"
    Write-Output "S1_FAKE_PUBLIC_CERT_SHA256=$(Get-Digest -Bytes ([IO.File]::ReadAllBytes($file)))"
    Write-Output "S1_REAL_SOURCE_OR_GOLD=NONE"
    return
}
if ($Action -eq "Receive") {
    if (-not $OwnerDirectory -or -not $Ciphertext -or -not $ExpectedSha256) {
        Fail "RECEIVE_REQUIRES_EXACT_OWNER_CIPHERTEXT_AND_SHA256"
    }
    $loc = Get-Recipient -OwnerFolder $OwnerDirectory -Sid $sid
    $src = [IO.Path]::GetFullPath($Ciphertext)
    if (-not [string]::Equals([IO.Path]::GetDirectoryName($src).TrimEnd('\'),
        (Get-Downloads).TrimEnd('\'),[StringComparison]::OrdinalIgnoreCase) -or
        [IO.Path]::GetFileName($src) -cne $ExpectedCmsName) {
        Fail "FAKE_REVIEWER_ONLY_EXACT_DOWNLOADS_CMS_ALLOWED"
    }
    $file = Get-Item -LiteralPath $src -ErrorAction Stop
    if ($file.PSIsContainer -or
        ($file.Attributes -band [IO.FileAttributes]::ReparsePoint) -ne 0 -or
        $file.Length -lt 100 -or $file.Length -gt 65536) {
        Fail "FAKE_REVIEWER_CIPHERTEXT_FILE_INVALID"
    }
    [byte[]]$sealed = [IO.File]::ReadAllBytes($src)
    if ((Get-Digest -Bytes $sealed) -cne $ExpectedSha256.ToLowerInvariant()) {
        Fail "FAKE_REVIEWER_INBOUND_CIPHERTEXT_SHA_MISMATCH"
    }
    $saved = Join-Path $loc[0] $SavedCmsName
    $receiptPath = Join-Path $loc[0] $SavedReceiptName
    if ([IO.File]::Exists($saved) -or [IO.File]::Exists($receiptPath)) {
        Fail "FAKE_REVIEWER_RECEIPT_ALREADY_EXISTS"
    }
    # Authenticate the entire envelope and validate invented source-only
    # report BEFORE persisting any ciphertext or private receipt.
    [byte[]]$raw = Decode-FakeCms -Saved $src -Cert $loc[1] -Private $loc[2]
    $plainSha = Confirm-FakeReviewerReport -Raw $raw
    Write-NewFile -Target $saved -Data $sealed
    $rec = [ordered]@{
        synthetic_only=$true;report_format=$Format
        ciphertext_sha256=$ExpectedSha256.ToLowerInvariant()
        private_report_sha256=$plainSha
    }
    [byte[]]$receiptBytes = $Utf8.GetBytes(($rec|ConvertTo-Json -Compress -Depth 4)+[char]10)
    Write-NewFile -Target $receiptPath -Data $receiptBytes
    $ownerPowershell = Join-Path $PSHOME "powershell.exe"
    & $ownerPowershell -NoProfile -NonInteractive -ExecutionPolicy Bypass -File $PSCommandPath -Action Verify -OwnerDirectory $loc[0] -ExpectedSha256 $ExpectedSha256
    if ($LASTEXITCODE -ne 0) { Fail "FAKE_REVIEWER_SEPARATE_OWNER_READBACK_FAILED" }
    Write-Output "S1_FAKE_REVIEW_RECIPIENT_RECEIVED=PASS"
    Write-Output "S1_FAKE_CIPHERTEXT_SHA256=$($rec.ciphertext_sha256)"
    Write-Output "S1_REAL_SOURCE_OR_GOLD=NONE"
    return
}
if ($Action -eq "Verify") {
    if (-not $OwnerDirectory -or -not $ExpectedSha256 -or $Ciphertext) {
        Fail "VERIFY_ARGUMENTS_INVALID"
    }
    Verify-Saved -Folder $OwnerDirectory -Sid $sid -Expected $ExpectedSha256
    return
}
Fail "UNKNOWN_ACTION"
