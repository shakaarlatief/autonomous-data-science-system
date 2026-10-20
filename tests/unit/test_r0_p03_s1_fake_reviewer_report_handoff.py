"""Bounded tests of the fictional S1 reviewer-report CMS output boundary.

These tests assert schema completeness, source-free identifiers, private/public
field separation, authenticated ciphertext recovery, and fail-closed behavior.
An OpenSSL run with a throwaway self-signed certificate is a mechanics check:
the private key remains in ignored pytest scratch and is not owner production
custody or proof of independent agent/session identity.
"""
from __future__ import annotations

from copy import deepcopy
import hashlib
import json
from pathlib import Path
import subprocess
import sys

import pytest

from experiments.r0_p03_navigation_probe import s1_fake_reviewer_report_handoff as s1
from experiments.r0_p03_navigation_probe import synthetic_cms_recipient_preflight as cms


def _alter(mutator):
    report = deepcopy(s1.fake_report())
    mutator(report)
    return report


def _certificates(path: Path) -> tuple[Path, Path]:
    private = path / "fake_private.pem"
    certificate = path / "fake_public.pem"
    proc = subprocess.run(
        [str(cms.OPENSSL), "req", "-new", "-x509",
         "-newkey", "rsa:2048", "-nodes",
         "-keyout", str(private), "-out", str(certificate),
         "-subj", "/CN=S1-FICTIONAL-REVIEWER", "-days", "1"],
        capture_output=True, timeout=25, check=False,
    )
    assert proc.returncode == 0
    return certificate, private


def test_three_fixed_sources_and_private_notes_are_only_fictional():
    data = s1.fake_report()
    assert s1.validate_fake_report(data) == data
    assert {r["source_id"] for r in data["records"]} == set(s1.FAKE_SOURCES)
    assert all(v.startswith(b"S1_FAKE_SOURCE_") for v in s1.FAKE_SOURCES.values())
    raw = s1.canonical_fake_bytes(data)
    assert b"FAKE_NOTE_RESTRICTED_DESIGN_CUE" in raw
    assert raw.endswith(b"\n")
    assert len(raw) < s1.MAX_PLAINTEXT


def test_real_source_name_and_unexpected_plaintext_field_rejected():
    with pytest.raises(s1.FakeReportError):
        s1.canonical_fake_bytes(_alter(
            lambda r: r["records"][0].update(source_id="docs/real_project.md")
        ))
    with pytest.raises(s1.FakeReportError):
        s1.canonical_fake_bytes(_alter(
            lambda r: r["records"][0].update(real_source_body="unapproved")
        ))
    with pytest.raises(s1.FakeReportError):
        s1.canonical_fake_bytes(_alter(
            lambda r: r.update(unapproved_plaintext="old expected answer")
        ))
    with pytest.raises(s1.FakeReportError):
        s1.canonical_fake_bytes(_alter(
            lambda r: r["records"][0].update(private_notes=["REAL_GOLD"])
        ))


def test_missing_duplicate_record_and_source_hash_mismatch_rejected():
    for change in [
        lambda r: r["records"].pop(),
        lambda r: r["records"][1].update(source_id="s1_fake_history"),
        lambda r: r["records"][0].update(source_sha256="0" * 64),
    ]:
        with pytest.raises(s1.FakeReportError):
            s1.canonical_fake_bytes(_alter(change))


def test_true_source_flags_and_missing_delivery_consistency():
    with pytest.raises(s1.FakeReportError):
        s1.canonical_fake_bytes(_alter(
            lambda r: r.update(real_source_reviewed=True)
        ))
    with pytest.raises(s1.FakeReportError):
        s1.canonical_fake_bytes(_alter(
            lambda r: r.update(actual_independent_actor_verified=True)
        ))
    with pytest.raises(s1.FakeReportError):
        s1.canonical_fake_bytes(_alter(
            lambda r: r["records"][1].update(delivered=False, inspected=True)
        ))
    with pytest.raises(s1.FakeReportError):
        s1.canonical_fake_bytes(_alter(
            lambda r: r["records"][1].update(delivered=False, inspected=False)
        ))


def test_variable_hold_record_remains_complete_and_can_be_sealed():
    report = _alter(
        lambda r: r["records"][1].update(
            delivered=False, inspected=False, disposition="HOLD_FOR_SOURCE_REVIEW",
            private_notes=["FAKE_NOTE_MISSING_SOURCE_BYTES"],
        )
    )
    assert len(s1.validate_fake_report(report)["records"]) == 3
    assert report["records"][1]["delivered"] is False
    assert report["records"][1]["disposition"] == "HOLD_FOR_SOURCE_REVIEW"


def test_typed_dispositions_cannot_be_misassigned():
    for change in [
        lambda r: r["records"][0].update(scope="EXACT_SPAN"),
        lambda r: r["records"][1].update(scope="COMPLETE_FILE"),
        lambda r: r["records"][1].update(disposition="UNSUPPORTED_REPRESENTATION"),
        lambda r: r["records"][0].update(inspected=False),
    ]:
        with pytest.raises(s1.FakeReportError):
            s1.validate_fake_report(_alter(change))


def test_fictional_scope_component_may_be_unsupported_without_admission():
    report = _alter(
        lambda r: r["records"][2].update(
            scope="REPRESENTATION_COMPONENT", inspected=False,
            disposition="UNSUPPORTED_REPRESENTATION",
            private_notes=["FAKE_NOTE_UNINSPECTED_REPRESENTATION"],
        )
    )
    assert s1.validate_fake_report(report)["records"][2]["inspected"] is False


def test_typed_booleans_reject_truthy_strings_and_integer_zero():
    for change in [
        lambda r: r.update(synthetic_only=1),
        lambda r: r.update(real_source_reviewed=0),
        lambda r: r["records"][0].update(inspected="yes"),
    ]:
        with pytest.raises(s1.FakeReportError):
            s1.validate_fake_report(_alter(change))


def test_public_receipt_rejects_private_notes_and_variable_statuses():
    base = {
        "synthetic_only": True, "report_format": s1.FORMAT,
        "ciphertext_filename": s1.OUTPUT, "ciphertext_sha256": "a" * 64,
        "ciphertext_bytes": 1000,
        "private_report_printed": False, "real_custody_qualified": False,
    }
    assert s1.validate_public_receipt(base) == base
    for unsafe in [
        {**base, "private_notes": ["FAKE_NOTE_RESTRICTED_DESIGN_CUE"]},
        {**base, "prohibited_count": 1},
        {**base, "source_id": "s1_fake_design"},
        {**base, "synthetic_only": 1},
        {**base, "real_custody_qualified": 0},
        {**base, "ciphertext_sha256": "g" * 64},
    ]:
        with pytest.raises(s1.FakeReportError):
            s1.validate_public_receipt(unsafe)


@pytest.mark.skipif(not cms.OPENSSL.is_file(), reason="Existing Git OpenSSL unavailable")
def test_real_aead_fake_report_handoff_private_readback_and_tamper(tmp_path, monkeypatch):
    certificate, key = _certificates(tmp_path)
    monkeypatch.setattr(s1.shutil, "which", lambda executable:
                        str(cms.OPENSSL) if executable == "openssl" else None)
    output = tmp_path / s1.OUTPUT
    public = s1.seal_fake_report(s1.fake_report(), certificate, output)
    assert public["synthetic_only"] is True
    assert public["private_report_printed"] is False
    assert public["real_custody_qualified"] is False
    assert hashlib.sha256(output.read_bytes()).hexdigest() == public["ciphertext_sha256"]
    assert s1.owner_fake_readback(
        output, certificate, key, public["ciphertext_sha256"]
    )
    assert not s1.owner_fake_readback(
        output, certificate, key, "0" * 64,
    )

    blob = bytearray(output.read_bytes())
    blob[-1] ^= 1
    output.write_bytes(blob)
    assert not s1.owner_fake_readback(
        output, certificate, key, hashlib.sha256(blob).hexdigest()
    )
    with pytest.raises(FileExistsError):
        s1.seal_fake_report(s1.fake_report(), certificate, output)

    text = json.dumps(public)
    assert "FAKE_NOTE_" not in text
    assert "s1_fake_design" not in text
    assert not (tmp_path / "plaintext_report.json").exists()


@pytest.mark.skipif(not cms.OPENSSL.is_file(), reason="Existing Git OpenSSL unavailable")
def test_real_cli_private_recipient_readback_prints_status_only(tmp_path):
    certificate, key = _certificates(tmp_path)
    module = "experiments.r0_p03_navigation_probe.s1_fake_reviewer_report_handoff"
    output = tmp_path / s1.OUTPUT
    report = json.dumps(s1.fake_report()).encode()
    source_root = Path(__file__).resolve().parents[2]
    env = None
    # Running the sender as a separate Python process tests the actual
    # public CLI contract rather than only the imported function.
    send = subprocess.run(
        [sys.executable, "-B", "-m", module,
         "send", "--cert", str(certificate), "--output", str(output)],
        input=report, capture_output=True, cwd=source_root, timeout=25,
        env=env, check=False,
    )
    assert send.returncode == 0, send.stderr.decode(errors="replace")
    receipt = json.loads(send.stdout)
    s1.validate_public_receipt(receipt)
    assert b"FAKE_NOTE" not in send.stdout
    assert b"FAKE_NOTE" not in send.stderr

    verify = subprocess.run(
        [sys.executable, "-B", "-m", module,
         "verify", "--cert", str(certificate),
         "--private-key", str(key), "--ciphertext", str(output),
         "--expected-ciphertext-sha256", receipt["ciphertext_sha256"]],
        capture_output=True, cwd=source_root, timeout=25, check=False,
    )
    assert verify.returncode == 0
    assert verify.stdout.strip() == b"S1_FAKE_OWNER_REVIEW_READBACK=PASS"
    assert b"FAKE_NOTE" not in verify.stdout + verify.stderr


def test_public_certificate_rejects_private_material_and_missing_file(tmp_path):
    target = tmp_path / s1.OUTPUT
    secret = tmp_path / "wrong.pem"
    secret.write_text("-----BEGIN PRIVATE KEY-----\nSECRET\n", encoding="utf-8")
    with pytest.raises(s1.FakeReportError):
        s1.seal_fake_report(s1.fake_report(), secret, target)
    with pytest.raises(s1.FakeReportError):
        s1.seal_fake_report(s1.fake_report(), tmp_path / "absent.pem", target)
