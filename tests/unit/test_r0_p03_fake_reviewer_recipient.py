"""Source-free qualification of the new, owner-executable fictional reviewer recipient.

Never execute Prepare, Receive or Verify in these tests. Those operations are
reserved for separately approved owner-desktop handling, and the OS/ACL/owner
boundary is not qualified here. Extract only function definitions and fixture
constants for isolated PowerShell cross-language parsing and fake-keygen tests.
"""
from __future__ import annotations

from copy import deepcopy
import base64
from pathlib import Path
import shutil
import subprocess
import tempfile

import pytest

from experiments.r0_p03_navigation_probe import s1_fake_reviewer_report_handoff as sender

ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / "scripts" / "r0_p03_fake_reviewer_recipient.ps1"
POWERSHELL = shutil.which("powershell.exe")


def _run_ps(script: str, *, timeout: int = 25) -> subprocess.CompletedProcess[str]:
    # A complete isolated PowerShell function prelude exceeds Windows'
    # process command-line limit when passed as -EncodedCommand. Keep all
    # invented test data inside ignored .venv scratch and invoke a short
    # -File argument instead. Never run recipient Prepare/Receive/Verify.
    with tempfile.TemporaryDirectory(dir=ROOT / ".venv",
                                     prefix=".s1-owner-ps-fake-") as location:
        trial = Path(location) / "isolated_fake_contract.ps1"
        trial.write_text(script, encoding="utf-8")
        return subprocess.run(
            [POWERSHELL, "-NoProfile", "-NonInteractive",
             "-ExecutionPolicy", "Bypass", "-File", str(trial)],
            text=True, capture_output=True, timeout=timeout, check=False,
        )


def _functions_only() -> str:
    source = SCRIPT.read_text(encoding="utf-8-sig")
    boundary = 'if ($Action -eq "SelfTest") {'
    assert source.count(boundary) == 1
    return source.split(boundary, 1)[0]


def _parse_python_report(report: object, *, accepted: bool) -> None:
    raw = sender.canonical_fake_bytes(report) if accepted else None
    if raw is None:
        # A deliberately wrong report may be rejected by the Python sender
        # before reaching PowerShell; preserve the recipient's own negative
        # test by serializing only the mutated fictional fields.
        import json
        raw = (json.dumps(report, sort_keys=True, separators=(",", ":")) + "\n").encode()
    b64 = base64.b64encode(raw).decode()
    attempt = _run_ps(
        _functions_only() +
        "\n$bytes=[Convert]::FromBase64String('" + b64 + "')\n" +
        "try { $null=Confirm-FakeReviewerReport -Raw $bytes; " +
        "Write-Output 'S1_VALID=TRUE' } catch { Write-Output 'S1_VALID=FALSE' }\n"
    )
    assert attempt.returncode == 0, attempt.stderr[-600:]
    assert attempt.stdout.strip() == (
        "S1_VALID=TRUE" if accepted else "S1_VALID=FALSE"
    )
    assert "FAKE_NOTE_" not in attempt.stdout + attempt.stderr


@pytest.mark.skipif(not POWERSHELL, reason="Windows PowerShell required")
def test_source_parses_and_selftest_makes_no_owner_folder():
    static = _run_ps(
        "$e=$null;$t=$null;" +
        "[System.Management.Automation.Language.Parser]::ParseFile('" +
        str(SCRIPT).replace("'", "''") +
        "',[ref]$t,[ref]$e)|Out-Null;" +
        "if($e.Count){exit 2};Write-Output 'S1_PS_PARSE=PASS'"
    )
    assert static.returncode == 0
    assert static.stdout.strip() == "S1_PS_PARSE=PASS"
    run = subprocess.run(
        [POWERSHELL, "-NoProfile", "-NonInteractive", "-ExecutionPolicy", "Bypass",
         "-File", str(SCRIPT), "-Action", "SelfTest"],
        text=True, capture_output=True, timeout=25, check=False,
    )
    assert run.returncode == 0, run.stderr[-600:]
    assert "S1_FAKE_REVIEWER_RECIPIENT_SELFTEST=PASS" in run.stdout
    assert "S1_OWNER_ACCOUNT_AND_FILES_UNTOUCHED=TRUE" in run.stdout


@pytest.mark.skipif(not POWERSHELL, reason="Windows PowerShell required")
def test_python_canonical_report_is_accepted_by_powershell():
    _parse_python_report(sender.fake_report(), accepted=True)


@pytest.mark.skipif(not POWERSHELL, reason="Windows PowerShell required")
def test_python_canonical_partial_source_hold_accepted_by_powershell():
    report = deepcopy(sender.fake_report())
    report["records"][1].update({
        "delivered": False,
        "inspected": False,
        "disposition": "HOLD_FOR_SOURCE_REVIEW",
        "private_notes": ["FAKE_NOTE_MISSING_SOURCE_BYTES"],
    })
    _parse_python_report(report, accepted=True)


@pytest.mark.skipif(not POWERSHELL, reason="Windows PowerShell required")
@pytest.mark.parametrize("change", [
    lambda r: r["records"].pop(),
    lambda r: r["records"][0].update(source_id="docs/actual.md"),
    lambda r: r["records"][0].update(source_sha256="0" * 64),
    lambda r: r["records"][1].update(delivered=False),
    lambda r: r["records"][2].update(private_notes=["UNAPPROVED_PRIVATE_NOTE"]),
    lambda r: r["records"][2].update(inspected="yes"),
    lambda r: r["records"][0].update(scope="EXACT_SPAN"),
    lambda r: r.update(actual_independent_actor_verified=True),
    lambda r: r.update(real_source_reviewed=True),
    lambda r: r.update(extra_gold="real secret"),
])
def test_powershell_rejects_invalid_python_fictional_report(change):
    report = deepcopy(sender.fake_report())
    change(report)
    _parse_python_report(report, accepted=False)


@pytest.mark.skipif(not POWERSHELL, reason="Windows PowerShell required")
def test_owner_actions_are_explicitly_outside_automated_test_execution():
    source = SCRIPT.read_text(encoding="utf-8-sig")
    assert 'if ($Action -eq "Prepare")' in source
    assert 'if ($Action -eq "Receive")' in source
    assert 'if ($Action -eq "Verify")' in source
    assert "OWNER_DESKTOP_IDENTITY_REQUIRED" in source
    assert "NON_ELEVATED_OWNER_POWERSHELL_REQUIRED" in source
    assert "SetAccessRuleProtection($true,$false)" in source
    assert "RECEIPT_ALREADY_EXISTS" in source
    assert "CMS_AUTHENTICATION_FAILED" in source
    assert "SELFTEST_FORBIDS_PATH_ARGUMENTS" in source
    assert "r0_p03_fake_public_recipient.ps1" in source
    assert "$ExpectedCmsName = \"R0_P03_FAKE_REVIEWER_REPORT.cms\"" in source
    assert "$PrivateKeyName = \"fake-reviewer-private.pem\"" in source


@pytest.mark.skipif(not POWERSHELL, reason="Windows PowerShell required")
def test_keygen_native_stderr_drained_without_owner_setup(tmp_path: Path):
    from experiments.r0_p03_navigation_probe import synthetic_cms_recipient_preflight as cms

    if not cms.OPENSSL.is_file():
        pytest.skip("Previously qualified Git OpenSSL is unavailable")
    key = tmp_path / "synthetic-private.pem"
    cert = tmp_path / "synthetic-public.pem"
    script = (
        _functions_only() +
        "\nInvoke-NewFakeCertificate -Private '" + str(key).replace("'", "''") +
        "' -Certificate '" + str(cert).replace("'", "''") + "'\n" +
        "if(-not (Test-Path -LiteralPath '" + str(key).replace("'", "''") +
        "') -or -not (Test-Path -LiteralPath '" +
        str(cert).replace("'", "''") +
        "')){exit 2}; Write-Output 'S1_FAKE_KEYGEN=PASS'"
    )
    res = _run_ps(script)
    assert res.returncode == 0, res.stderr[-600:]
    assert res.stdout.strip() == "S1_FAKE_KEYGEN=PASS"
    assert b"BEGIN PRIVATE KEY" in key.read_bytes()
    assert b"BEGIN CERTIFICATE" in cert.read_bytes()



@pytest.mark.skipif(not POWERSHELL, reason="Windows PowerShell required")
def test_python_cms_power_shell_authenticated_readback_and_tamper(tmp_path: Path):
    """PowerShell decrypts the Python-created AES-GCM envelope using fake keys.

    This runs ONLY the source-file function prelude under ignored pytest
    scratch. In particular, no code path calls owner-only Prepare or writes
    inside owner LocalAppData.
    """
    from experiments.r0_p03_navigation_probe import synthetic_cms_recipient_preflight as cms

    if not cms.OPENSSL.is_file():
        pytest.skip("Existing Git OpenSSL unavailable")
    private = tmp_path / "fake_mock_private.pem"
    cert = tmp_path / "fake_mock_public.pem"
    generated = subprocess.run(
        [str(cms.OPENSSL), "req", "-new", "-x509", "-newkey", "rsa:2048",
         "-nodes", "-keyout", str(private), "-out", str(cert),
         "-subj", "/CN=S1-FAKE-RECIPIENT-CROSSLANG", "-days", "1"],
        capture_output=True, timeout=25, check=False,
    )
    assert generated.returncode == 0
    outgoing = tmp_path / sender.OUTPUT
    receipt = sender.seal_fake_report(sender.fake_report(), cert, outgoing)

    def powershell_open(path: Path) -> subprocess.CompletedProcess[str]:
        prelude = _functions_only()
        operation = (
            "\ntry {\n" +
            "  $target='" + str(path).replace("'", "''") + "'\n" +
            "  $cert='" + str(cert).replace("'", "''") + "'\n" +
            "  $key='" + str(private).replace("'", "''") + "'\n" +
            "  $raw=Decode-FakeCms -Saved $target -Cert $cert -Private $key\n" +
            "  $digest=Confirm-FakeReviewerReport -Raw $raw\n" +
            "  if($digest -eq '" + sender._sha(sender.canonical_fake_bytes(sender.fake_report())) +
            "') { Write-Output 'S1_POWER_SHELL_READBACK=PASS' } " +
            "else { Write-Output 'S1_POWER_SHELL_READBACK=FAIL' }\n" +
            "} catch { Write-Output 'S1_POWER_SHELL_READBACK=FAIL' }\n"
        )
        return _run_ps(prelude + operation, timeout=25)

    accepted = powershell_open(outgoing)
    assert accepted.returncode == 0, accepted.stderr[-500:]
    assert accepted.stdout.strip() == "S1_POWER_SHELL_READBACK=PASS"
    assert "FAKE_NOTE_" not in accepted.stdout + accepted.stderr

    altered = bytearray(outgoing.read_bytes())
    altered[-1] ^= 1
    corrupted = tmp_path / "fake_tampered.cms"
    corrupted.write_bytes(altered)
    denied = powershell_open(corrupted)
    assert denied.returncode == 0
    assert denied.stdout.strip() == "S1_POWER_SHELL_READBACK=FAIL"
    assert "FAKE_NOTE_" not in denied.stdout + denied.stderr
    assert receipt["real_custody_qualified"] is False
