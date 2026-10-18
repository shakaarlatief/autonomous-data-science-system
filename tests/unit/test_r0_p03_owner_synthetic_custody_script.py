"""Non-mutating preflight for the owner-executed R0-P03 synthetic custody script.

The test never runs Create, changes NTFS ACLs, writes owner-local files or
pretends to qualify complete reference custody. It exercises only fixed
fictional packet construction and fail-closed input guards.
"""
from __future__ import annotations

import os
from pathlib import Path
import shutil
import subprocess

import pytest

SCRIPT = Path(__file__).parents[2] / "scripts" / "r0_p03_owner_synthetic_custody.ps1"


def test_script_contract_keeps_owner_acl_change_bounded() -> None:
    source = SCRIPT.read_text(encoding="utf-8")
    assert source.endswith("\n")
    assert "SetAccessRuleProtection($true, $false)" in source
    assert "[IO.Directory]::CreateDirectory($Path, $acl)" in source
    assert "[IO.FileMode]::CreateNew" in source
    assert "Confirm-OwnerFolder" in source
    assert "OWNER_FOLDER_OUTSIDE_LOCALAPPDATA" in source
    assert "EXISTING_DIRECTORY_REFUSED" in source
    assert "SYNTHETIC_ONLY_R0_P03_NO_REAL_GOLD" in source
    assert "COMPLETE_SYNTHETIC_PACKET_READBACK=PASS" in source
    assert "NEW_PROCESS_RECOVERY_FAILED" in source
    assert "Get-Acl" in source
    assert "9" in source and "12" in source
    assert "Win32_LogicalDisk" not in source


@pytest.mark.skipif(os.name != "nt" or shutil.which("powershell.exe") is None,
                    reason="Owner custody script requires Windows PowerShell 5.1")
def test_owner_script_synthetic_selftest_no_owner_files() -> None:
    executable = shutil.which("powershell.exe")
    assert executable is not None
    syntax = subprocess.run(
        [executable, "-NoProfile", "-NonInteractive", "-Command",
         "$t=$null;$e=$null;"
         "[System.Management.Automation.Language.Parser]::ParseFile("
         "'scripts/r0_p03_owner_synthetic_custody.ps1',[ref]$t,[ref]$e)|Out-Null;"
         "if($e.Count){$e|ForEach-Object{$_.ToString()};exit 2};"
         "Write-Output 'SCRIPT_PARSE_PASS'"],
        cwd=SCRIPT.parents[1], capture_output=True, text=True, timeout=30,
        check=False,
    )
    assert syntax.returncode == 0, syntax.stderr
    assert "SCRIPT_PARSE_PASS" in syntax.stdout

    verification = subprocess.run(
        [executable, "-NoProfile", "-NonInteractive",
         "-ExecutionPolicy", "Bypass", "-File", str(SCRIPT),
         "-Action", "SelfTest"],
        cwd=SCRIPT.parents[1], capture_output=True, text=True, timeout=30,
        check=False,
    )
    assert verification.returncode == 0, verification.stderr
    assert "SYNTHETIC_SELFTEST=PASS" in verification.stdout
    assert "NINE_PLUS_TWELVE_CASES=PASS" in verification.stdout
    assert "OWNER_SYNTHETIC_CUSTODY_CREATION=PASS" not in verification.stdout


@pytest.mark.skipif(os.name != "nt" or shutil.which("powershell.exe") is None,
                    reason="Owner custody script requires Windows PowerShell 5.1")
def test_caller_selected_owner_path_rejected_before_any_create() -> None:
    executable = shutil.which("powershell.exe")
    assert executable is not None
    proc = subprocess.run(
        [executable, "-NoProfile", "-NonInteractive",
         "-ExecutionPolicy", "Bypass", "-File", str(SCRIPT),
         "-Action", "Create", "-Directory", "C:\\not-a-custody-directory"],
        cwd=SCRIPT.parents[1], capture_output=True, text=True, timeout=30,
        check=False,
    )
    assert proc.returncode != 0
    assert "CREATE_FORBIDS_CALLER_SELECTED_FOLDER_OR_DIGEST" in proc.stderr
