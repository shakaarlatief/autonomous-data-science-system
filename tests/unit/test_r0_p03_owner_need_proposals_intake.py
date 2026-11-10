"""Bounded fake-only preflight for private, not-yet-scored need proposals.

The test intentionally never calls Import or Verify on real owner content.
It cannot attest the actual private downloaded artifact or OS ACL until the
owner runs the separate opt-in command in ordinary Windows PowerShell.
"""
from __future__ import annotations

import os
from pathlib import Path
import shutil
import subprocess

import pytest

ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / "scripts/r0_p03_owner_need_proposals_intake.ps1"
EXPECTED_SHA = "819ee551af64f87571df281dfdda75af8f5aa6088202b924bc09e2209cea0c86"


def test_script_is_specific_to_reported_private_candidate_identity() -> None:
    source = SCRIPT.read_text(encoding="utf-8")
    assert source.endswith("\n") and "\r\n" not in source
    assert EXPECTED_SHA in source
    assert "$ExpectedBytes = 12684" in source
    assert "NEED_PROPOSALS_RESTRICTED.md" in source
    assert "UNADJUDICATED_NEED_PROPOSALS_NOT_GOLD" in source
    assert "OWNER_PRIVATE_DIRECTORY=$folder" in source
    assert "LOCAL_OWNER_INTAKE_IS_NOT_QUALIFIED_REAL_GOLD_CUSTODY=TRUE" in source
    assert "source_receipt_provenance" in source
    assert "owner_only_platform_permissions" in source


def test_script_is_owner_local_non_elevated_no_public_repo_custody() -> None:
    source = SCRIPT.read_text(encoding="utf-8")
    for marker in (
        "OWNER_INTERACTIVE_IDENTITY_REQUIRED",
        "NON_ELEVATED_OWNER_POWERSHELL_REQUIRED",
        "CodexSandbox(Offline|Online)",
        "CUSTODY_FOLDER_MUST_BE_DIRECT_LOCALAPPDATA_CHILD",
        "IMPORT_FORBIDS_CALLER_CHOSEN_DESTINATION",
        "DO_NOT_STAGE_RESTRICTED_PROPOSALS_INSIDE_PUBLIC_ADS_WORKTREE",
        "UNEXPECTED_FILE_TYPE_OR_REPARSE",
        "SetAccessRuleProtection($true,$false)",
        "[IO.Directory]::CreateDirectory($Folder,$acl)",
        "[IO.FileMode]::CreateNew",
        "OWNER_AND_SYSTEM_REQUIRED",
        "UNEXPECTED_CUSTODY_PERMISSION",
        "OWNER_SECOND_PROCESS_READBACK_FAILED",
    ):
        assert marker in source
    assert "Remove-Item" not in source
    assert "Copy-Item" not in source
    assert "Set-ExecutionPolicy" not in source


@pytest.mark.skipif(os.name != "nt" or not shutil.which("powershell.exe"),
                    reason="Requires Windows PowerShell")
def test_real_powershell_parser_and_fake_only_selftest() -> None:
    binary = shutil.which("powershell.exe")
    assert binary
    parser = subprocess.run(
        [binary, "-NoProfile", "-NonInteractive", "-Command",
         "$t=$null;$e=$null;"
         "[System.Management.Automation.Language.Parser]::ParseFile("
         "'scripts/r0_p03_owner_need_proposals_intake.ps1',"
         "[ref]$t,[ref]$e)|Out-Null;"
         "if($e.Count){$e|ForEach-Object{$_.ToString()};exit 2};"
         "'SCRIPT_PARSE_PASS'"],
        cwd=ROOT, capture_output=True, text=True, check=False, timeout=20,
    )
    assert parser.returncode == 0, parser.stderr
    assert "SCRIPT_PARSE_PASS" in parser.stdout
    fake = subprocess.run(
        [binary, "-NoProfile", "-NonInteractive",
         "-ExecutionPolicy", "Bypass",
         "-File", str(SCRIPT), "-Action", "SelfTest"],
        cwd=ROOT, capture_output=True, text=True, check=False, timeout=20,
    )
    assert fake.returncode == 0, fake.stderr
    assert "OWNER_NEED_INTAKE_SYNTHETIC_SELFTEST=PASS" in fake.stdout
    assert "OWNER_NEED_PROPOSALS_IMPORT=PASS" not in fake.stdout


@pytest.mark.skipif(os.name != "nt" or not shutil.which("powershell.exe"),
                    reason="Requires Windows PowerShell")
def test_selftest_rejects_owner_path_argument_without_touching_files() -> None:
    binary = shutil.which("powershell.exe")
    assert binary
    result = subprocess.run(
        [binary, "-NoProfile", "-NonInteractive",
         "-ExecutionPolicy", "Bypass",
         "-File", str(SCRIPT), "-Action", "SelfTest",
         "-SourcePath", "C:\\nonexistent_private_proposals.md"],
        cwd=ROOT, capture_output=True, text=True, check=False, timeout=20,
    )
    assert result.returncode != 0
    assert "SELFTEST_FORBIDS_PATH_ARGUMENTS" in result.stderr
