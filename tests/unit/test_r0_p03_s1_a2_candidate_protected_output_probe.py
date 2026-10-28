"""Bounded source-free protected-output capability tests for S1 A2.

No test invokes owner-controlled Prepare, accesses an actual owner key, writes
into LocalAppData, sends data to a model session, or asserts clean-room actor
independence. Ephemeral RSA credentials exist only in pytest-owned ignored
.venv scratch and are used solely to verify the already established OpenSSL
CMS mechanism against a different variable-length report format.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import shutil
import subprocess
from copy import deepcopy

import pytest

from experiments.r0_p03_navigation_probe import (
    s1_a2_candidate_protected_output_probe as probe,
)

ROOT = Path(__file__).resolve().parents[2]
FIXTURE = ROOT / "experiments" / "r0_p03_navigation_probe"
TEXT = FIXTURE / "a2_source_free_fidelity_unicode_crlf.txt"
PNG = FIXTURE / "a2_source_free_fidelity_pattern.png"
OPENSSL = shutil.which("openssl")
if not OPENSSL:
    git_openssl = Path(r"C:\Program Files\Git\usr\bin\openssl.exe")
    if git_openssl.is_file():
        OPENSSL = str(git_openssl)


def _report(extra: int = 1) -> bytes:
    return probe.build_source_free_report(TEXT.read_bytes(), PNG.read_bytes(),
                                          optional_missing=extra)


@pytest.mark.parametrize("extra", [0, 1, 2, 3])
def test_distinct_fictional_report_lengths_and_explicit_optional_holds(extra: int) -> None:
    raw = _report(extra)
    report = probe.validate_report(raw)
    assert report["synthetic_only"] is True
    assert report["real_source_reviewed"] is False
    assert report["challenge_state"] == "NOT_CHALLENGED"
    assert len(report["records"]) == extra + 2
    assert len({row["private_canary"] for row in report["records"]}) == extra + 2
    assert report["records"][0]["byte_count"] == 193
    assert report["records"][1]["byte_count"] == 291
    assert all(row["delivered"] is False for row in report["records"][2:])


def test_real_or_modified_source_bytes_are_rejected_before_report_creation() -> None:
    with pytest.raises(probe.ProbeHold, match="RECEIVED_FAKE_SOURCE_MISMATCH"):
        probe.build_source_free_report(TEXT.read_bytes() + b"x", PNG.read_bytes())
    with pytest.raises(probe.ProbeHold, match="RECEIVED_FAKE_SOURCE_MISMATCH"):
        probe.build_source_free_report(TEXT.read_bytes(), b"actual source bytes")


@pytest.mark.parametrize("extra", [-1, 4, True])
def test_invalid_variable_count_denied(extra: int) -> None:
    with pytest.raises(probe.ProbeHold, match="OPTIONAL_COUNT_INVALID"):
        _report(extra)


@pytest.mark.parametrize("mutate", [
    lambda d: d.update(real_source_reviewed=True),
    lambda d: d.update(actual_independence_qualified=True),
    lambda d: d.update(restricted_output_qualified=True),
    lambda d: d.update(candidate_actor="ADMITTED_REVIEWER"),
    lambda d: d.update(challenge_state="CHALLENGED_ACCEPTED"),
    lambda d: d.update(real_content="unauthorized"),
    lambda d: d["records"][0].update(fixture_id="docs/private_review.md"),
    lambda d: d["records"][0].update(source_sha256="0" * 64),
    lambda d: d["records"][0].update(delivered=False),
    lambda d: d["records"][2].update(inspected=True),
    lambda d: d["records"][2].update(disposition="FAKE_HOLD_PENDING_CHALLENGE"),
    lambda d: d["records"][1].update(private_canary=d["records"][0]["private_canary"]),
    lambda d: d["records"].pop(0),
    lambda d: d["records"].reverse(),
])
def test_out_of_scope_report_or_incomplete_record_denied(mutate) -> None:
    parsed = json.loads(_report())
    mutate(parsed)
    with pytest.raises(probe.ProbeHold):
        probe.validate_report(probe._canonical(parsed))


def test_duplicate_json_keys_and_noncanonical_rendering_denied() -> None:
    raw = _report()
    duplicate = raw.replace(b'"synthetic_only":true', b'"synthetic_only":true,"synthetic_only":true')
    with pytest.raises(probe.ProbeHold):
        probe.validate_report(duplicate)
    with pytest.raises(probe.ProbeHold, match="NONCANONICAL_REPORT"):
        probe.validate_report(b" " + raw)


def test_each_fresh_report_has_new_private_canaries_without_public_defaults() -> None:
    one = probe.validate_report(_report())
    two = probe.validate_report(_report())
    assert one["report_nonce"] != two["report_nonce"]
    assert {x["private_canary"] for x in one["records"]}.isdisjoint(
        {x["private_canary"] for x in two["records"]}
    )


@pytest.mark.skipif(not OPENSSL, reason="OpenSSL CMS not available in test environment")
def test_actual_source_free_cms_encrypt_and_owner_readback(tmp_path: Path) -> None:
    """The old hardcoded three-record fake recipient is not reused here."""
    key = tmp_path / "throwaway-test-only.pem"
    cert = tmp_path / "throwaway-test-only-cert.pem"
    # This password is a deliberately public test constant, not owner material.
    fake_password = b"source-free-test-password-only"
    x = subprocess.run(
        [OPENSSL, "req", "-new", "-x509", "-newkey", "rsa:2048",
         "-passout", "pass:source-free-test-password-only",
         "-keyout", str(key), "-out", str(cert),
         "-subj", "/CN=ADS-A2-SOURCE-FREE-TEST-ONLY", "-days", "1"],
        capture_output=True, timeout=25, check=False,
    )
    assert x.returncode == 0, "test-only OpenSSL keygen failed"
    report = _report(3)
    output = tmp_path / probe.OUTPUT_NAME
    receipt = probe.seal_report(report, cert, output, executable=OPENSSL)
    assert receipt["owner_private_custody_qualified"] is False
    assert receipt["private_report_printed"] is False
    assert len(output.read_bytes()) == receipt["ciphertext_bytes"]
    assert hashlib.sha256(output.read_bytes()).hexdigest() == receipt["ciphertext_sha256"]
    assert b"A2_FICTIONAL_PRIVATE_CANARY" not in output.read_bytes()
    assert report not in output.read_bytes()
    recovered = probe.owner_verify_ciphertext(
        output, cert, key, receipt["ciphertext_sha256"],
        passphrase=fake_password, executable=OPENSSL
    )
    assert recovered["owner_full_readback"] == "PASS"
    assert recovered["record_count"] == 5
    assert recovered["private_canary_records_validated"] == 5
    assert recovered["author_route_access_denial_proven"] is False
    assert "A2_FICTIONAL_PRIVATE_CANARY_" not in str(receipt) + str(recovered)
    with pytest.raises(probe.ProbeHold, match="OUTPUT_LOCATION_OR_VERSION_INVALID"):
        probe.seal_report(_report(0), cert, output, executable=OPENSSL)
    with pytest.raises(probe.ProbeHold, match="CIPHERTEXT_INTEGRITY_MISMATCH"):
        probe.owner_verify_ciphertext(
            output, cert, key, "f" * 64,
            passphrase=fake_password, executable=OPENSSL
        )
    with pytest.raises(probe.ProbeHold, match="CMS_AUTHENTICATION_FAILED"):
        probe.owner_verify_ciphertext(
            output, cert, key, receipt["ciphertext_sha256"],
            passphrase=b"wrong-source-free-password", executable=OPENSSL,
        )
    with pytest.raises(probe.ProbeHold, match="OWNER_PASSPHRASE_INPUT_INVALID"):
        probe.owner_verify_ciphertext(
            output, cert, key, receipt["ciphertext_sha256"],
            passphrase=b"bad\nvalue", executable=OPENSSL,
        )
    changed = bytearray(output.read_bytes())
    changed[-7] ^= 1
    output.write_bytes(changed)
    with pytest.raises(probe.ProbeHold, match="CMS_AUTHENTICATION_FAILED"):
        probe.owner_verify_ciphertext(
            output, cert, key, probe.digest(changed),
            passphrase=fake_password, executable=OPENSSL
        )


def test_public_script_does_not_qualify_custody_or_real_source_intake() -> None:
    raw = Path(probe.__file__).read_text(encoding="utf-8")
    assert 'owner_exclusive_access_proven": False' in raw
    assert 'author_route_access_denial_proven": False' in raw
    assert 'real_source_reviewed": False' in raw
    assert 'owner_private_custody_qualified": False' in raw
    assert "with output.open(\"xb\")" in raw
    assert 'input=raw, capture_output=True' in raw
