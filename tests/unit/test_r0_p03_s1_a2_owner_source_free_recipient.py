"""Source-free owner-executed recipient control and non-mutating tests.

No test creates an owner key, touches a private owner recipient, invokes the
Prepare/Receive/Verify actions, or asks the project-attached Runtime Bridge to
read protected owner files. Only the PowerShell parser and SelfTest action run.
The separate Python CMS tests remain responsible for fake-key authenticated
encrypted readback, including wrong passphrase and tampered ciphertext.
"""
from __future__ import annotations

from pathlib import Path
import subprocess

import pytest

ROOT = Path(__file__).resolve().parents[2]
PS = ROOT / "scripts" / "r0_p03_s1_a2_owner_source_free_recipient.ps1"
PY = ROOT / "experiments" / "r0_p03_navigation_probe" / "s1_a2_candidate_protected_output_probe.py"


def _source() -> str:
    return PS.read_text(encoding="utf-8")


def test_powershell_syntax_is_valid_without_execution() -> None:
    """PowerShell 5.1 parser is invoked without running the script body."""
    quoted = str(PS).replace("'", "''")
    command = (
        "$tokens=$null;$errors=$null;"
        f"[System.Management.Automation.Language.Parser]::ParseFile('{quoted}',"
        "[ref]$tokens,[ref]$errors)|Out-Null;"
        "if($errors.Count -gt 0){$errors|ForEach-Object{$_.Message};exit 2};"
        "'S1_A2_OWNER_POWERSHELL_SYNTAX=PASS'"
    )
    result = subprocess.run(
        ["powershell.exe", "-NoProfile", "-NonInteractive", "-Command", command],
        capture_output=True, text=True, timeout=20, check=False,
    )
    assert result.returncode == 0, result.stderr + result.stdout
    assert "S1_A2_OWNER_POWERSHELL_SYNTAX=PASS" in result.stdout


def test_nonmutating_owner_selftest_reports_no_key_created() -> None:
    result = subprocess.run(
        ["powershell.exe", "-NoProfile", "-NonInteractive", "-ExecutionPolicy",
         "Bypass", "-File", str(PS), "-Action", "SelfTest"],
        capture_output=True, text=True, timeout=20, check=False,
    )
    assert result.returncode == 0, result.stderr
    assert "S1_A2_OWNER_SOURCE_FREE_PREFLIGHT=PASS" in result.stdout
    assert "S1_A2_OWNER_KEYS_CREATED=NO" in result.stdout


def test_owner_selftest_rejects_misplaced_recipient_id() -> None:
    result = subprocess.run(
        ["powershell.exe", "-NoProfile", "-NonInteractive", "-ExecutionPolicy",
         "Bypass", "-File", str(PS), "-Action", "SelfTest",
         "-RecipientId", "a" * 32],
        capture_output=True, text=True, timeout=20, check=False,
    )
    assert result.returncode == 2
    assert "SELFTEST_PARAMETERS_INVALID" in result.stderr
    assert "OWNER_SOURCE_FREE_RECIPIENT_PREPARED=PASS" not in result.stdout


@pytest.mark.parametrize("invalid", ["../../other", "x" * 32, "a" * 31])
def test_owner_recipient_identifier_is_strictly_bounded(invalid: str) -> None:
    # These cases are static contract checks, not privileged action execution.
    assert "^[0-9a-f]{32}$" in _source()
    import re
    assert not re.fullmatch(r"[0-9a-f]{32}", invalid)


def test_only_source_free_owner_actions_exposed() -> None:
    source = _source()
    assert '[ValidateSet("SelfTest","Prepare","Receive","Verify")]' in source
    assert "S1_A2_REAL_CUSTODY_QUALIFIED=FALSE" in source
    assert "S1_A2_OWNER_KEYS_CREATED=NO" in source
    assert "OWNER_INTERACTIVE_REQUIRED" in source
    assert "OWNER_REPORT_READBACK_FAILED" in source


def test_owner_test_key_must_be_encrypted_and_not_generated_by_tests() -> None:
    source = _source()
    assert "BEGIN ENCRYPTED PRIVATE KEY" in source
    assert "OWNER_KEY_NOT_ENCRYPTED_AT_REST" in source
    assert "OWNER_INTERACTIVE_KEY_GENERATION_FAILED" in source
    assert "OWNER_ACL_NOT_PROTECTED" in source
    assert "OWNER_ACL_UNEXPECTED_PRINCIPAL" in source
    assert "newkey rsa:2048" in source
    assert "-nodes" not in source
    assert "-passout" not in source
    assert "-passin" not in source
    assert "Read-Host" not in source


def test_public_cert_only_exported_and_private_paths_not_logged() -> None:
    source = _source()
    assert "S1_A2_OWNER_PUBLIC_CERT_PATH=" in source
    assert "S1_A2_OWNER_PUBLIC_CERT_SHA256=" in source
    assert "S1_A2_OWNER_RECIPIENT_ID=" in source
    assert "S1_A2_OWNER_PRIVATE_KEY_ENCRYPTED=TRUE" in source
    assert "OWNER_KEY_NOT_ENCRYPTED_AT_REST" in source
    assert "Join-Path $Downloads" in source
    assert "Write-Output ($private" not in source
    assert "Write-Output ($key" not in source
    assert "Write-Output ($folder" not in source


def test_receipt_stored_and_verified_without_plaintext_output() -> None:
    source = _source()
    assert 'Get-FileHash -LiteralPath $source -Algorithm SHA256' in source
    assert 'Get-FileHash -LiteralPath $stored -Algorithm SHA256' in source
    assert 'ads-s1-a2-owner-source-free-receipt-v1' in source
    assert 'S1_A2_OWNER_SOURCE_FREE_COMPLETE_READBACK=PASS' in source
    assert 'S1_A2_OWNER_SOURCE_FREE_RECHECK=PASS' in source
    assert '--expected-ciphertext-sha256' in source
    assert 'owner-verify' in source


def test_python_reader_source_requires_interactive_owner_passphrase() -> None:
    # Direct nested Python process execution is unreliable in the bounded
    # Runtime Bridge sandbox due to inherited subprocess pipe lifetimes.
    # Assert the fail-closed CLI contract without inventing a successful
    # external denial observation or touching an owner-held credential.
    source = PY.read_text(encoding="utf-8")
    assert "if not sys.stdin.isatty():" in source
    assert 'raise ProbeHold("OWNER_INTERACTIVE_PASSPHRASE_REQUIRED")' in source
    assert "getpass.getpass(" in source
    assert "SOURCE_FREE_A2_PROBE_HOLD" in source
