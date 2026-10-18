"""Read-only checks for owner-only fictional CMS recipient workflow.

No Prepare/Receive/Verify operation is executed from an agent identity. This
test cannot qualify real recipient custody or simulate OS permission isolation.
"""
from __future__ import annotations

import os
from pathlib import Path
import shutil
import subprocess

import pytest

SCRIPT = Path(__file__).parents[2] / "scripts/r0_p03_fake_public_recipient.ps1"


def test_owner_procedure_has_explicit_fake_only_boundaries() -> None:
    body = SCRIPT.read_text(encoding="utf-8")
    assert body.endswith("\n")
    for required in (
        "OWNER_DESKTOP_IDENTITY_REQUIRED",
        "NON_ELEVATED_OWNER_POWERSHELL_REQUIRED",
        "SetAccessRuleProtection($true,$false)",
        "[IO.Directory]::CreateDirectory($Folder,$dacl)",
        "OWNER_DIRECTORY_MUST_HAVE_PROTECTED_DACL",
        "OWNER_FOLDER_ALREADY_EXISTS",
        "PREPARE_FORBIDS_CALLER_CHOSEN_TARGET",
        "RECEIVE_REQUIRES_OWNER_FOLDER_AND_CIPHERTEXT_ONLY",
        "ONLY_EXACT_DOWNLOADS_CMS_FILENAME_PERMITTED",
        "CMS_AUTHENTICATION_OR_DECRYPTION_FAILED",
        "FAKE_PACKET_SCHEMA_INVALID",
        "FAKE_CASE_COUNTS_INVALID",
        "FAKE_LEGACY_SLOT_INVALID",
        "FAKE_PRIMARY_SLOT_INVALID",
        "FRESH_OWNER_PROCESS_RECOVERY_FAILED",
        "OWNER_FULL_FAKE_PACKET_RECOVERY=PASS",
    ):
        assert required in body
    assert "ADS-P03-FAKE-RECIPIENT-" in body
    assert "SYNTHETIC_R0P03_DEMONSTRATION_ONLY" in body
    assert 'Write-Output "REAL_GOLD_OR_PRODUCTION_KEYS=TRUE"' not in body
    assert "R0_P03_FAKE_AUTHOR_PACKET.cms" in body


@pytest.mark.skipif(os.name != "nt" or shutil.which("powershell.exe") is None,
                    reason="Native Windows PowerShell 5.1 required")
def test_owner_receiver_parser_and_in_memory_contract() -> None:
    ps = shutil.which("powershell.exe")
    assert ps is not None
    parsed = subprocess.run(
        [ps, "-NoProfile", "-NonInteractive", "-Command",
         "$t=$null;$e=$null;"
         "[Management.Automation.Language.Parser]::ParseFile("
         "'scripts/r0_p03_fake_public_recipient.ps1',[ref]$t,[ref]$e)|Out-Null;"
         "if($e.Count){$e|ForEach-Object{$_.ToString()};exit 2};"
         "Write-Output 'PARSER_PASS'"],
        cwd=SCRIPT.parents[1], text=True, capture_output=True, timeout=30,
        check=False,
    )
    assert parsed.returncode == 0, parsed.stderr
    assert "PARSER_PASS" in parsed.stdout
    checked = subprocess.run(
        [ps, "-NoProfile", "-NonInteractive", "-ExecutionPolicy", "Bypass",
         "-File", str(SCRIPT), "-Action", "SelfTest"],
        cwd=SCRIPT.parents[1], text=True, capture_output=True, timeout=30,
        check=False,
    )
    assert checked.returncode == 0, checked.stderr
    assert "OWNER_FAKE_RECIPIENT_SELFTEST=PASS" in checked.stdout
    assert "EXPECTED_CASES=9_PLUS_12" in checked.stdout
    assert "FAKE_OWNER_PRIVATE_FOLDER=" not in checked.stdout


@pytest.mark.skipif(os.name != "nt" or shutil.which("powershell.exe") is None,
                    reason="Native Windows PowerShell 5.1 required")
def test_prepare_refuses_caller_chosen_existing_folder_without_mutation() -> None:
    ps = shutil.which("powershell.exe")
    assert ps is not None
    call = subprocess.run(
        [ps, "-NoProfile", "-NonInteractive", "-ExecutionPolicy", "Bypass",
         "-File", str(SCRIPT), "-Action", "Prepare",
         "-OwnerDirectory", "C:\\do-not-create-recipient-dir"],
        cwd=SCRIPT.parents[1], text=True, capture_output=True, timeout=30,
        check=False,
    )
    assert call.returncode != 0
    # Either argument rejection or sandbox-principal rejection must fail
    # before any local private key/certificate is created.
    assert (
        "OWNER_DESKTOP_IDENTITY_REQUIRED" in call.stderr
        or "PREPARE_FORBIDS_CALLER_CHOSEN_TARGET" in call.stderr
        or "NON_ELEVATED_OWNER_POWERSHELL_REQUIRED" in call.stderr
    )
