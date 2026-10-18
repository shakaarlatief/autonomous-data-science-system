"""Synthetic Temporary Chat sender with fake CMS envelope and no real gold."""
import hashlib
from pathlib import Path
import shutil
import subprocess

import pytest

from experiments.r0_p03_navigation_probe import temporary_author_fake_cms_sender as sender
from experiments.r0_p03_navigation_probe import synthetic_output_collector_candidate as collector
from experiments.r0_p03_navigation_probe import synthetic_cms_recipient_preflight as cms


def test_sender_payload_matches_prior_strict_fake_final():
    assert sender.fictional_payload() == collector.extract_synthetic_final(
        collector.fake_stream()
    )


def test_public_certificate_invalid_and_unexpected_output_rejected(tmp_path: Path):
    cert = tmp_path / "fake.pem"
    cert.write_text("-----BEGIN PRIVATE KEY-----\nINVALID\n")
    with pytest.raises(ValueError):
        sender.sender(cert, tmp_path / sender.FILENAME)
    with pytest.raises(ValueError):
        sender.sender(cert, tmp_path / "not-fixed.cms")


@pytest.mark.skipif(not cms.OPENSSL.is_file(), reason="Existing Git OpenSSL unavailable")
def test_real_sender_to_existing_cms_verifier(tmp_path: Path, monkeypatch):
    process = subprocess.run(
        [str(cms.OPENSSL), "req", "-new", "-x509", "-newkey", "rsa:2048",
         "-nodes", "-keyout", str(tmp_path / "fake-owner-private.pem"),
         "-out", str(tmp_path / "fake-owner-public.pem"),
         "-subj", "/CN=FAKE-ONLY-TEMP-SENDER", "-days", "1"],
        capture_output=True, timeout=25, check=False,
    )
    assert process.returncode == 0
    monkeypatch.setattr(sender.shutil, "which",
                        lambda name: str(cms.OPENSSL) if name == "openssl" else None)
    target = tmp_path / sender.FILENAME
    receipt = sender.sender(tmp_path / "fake-owner-public.pem", target)
    assert receipt["fake_legacy_slots"] == 9 and receipt["fake_primary_slots"] == 12
    assert receipt["private_key_available_to_sender"] is False
    assert receipt["custody_qualified"] is False
    assert hashlib.sha256(target.read_bytes()).hexdigest() == receipt["ciphertext_sha256"]
    expected = hashlib.sha256(sender.fictional_payload()).hexdigest()
    recovered = cms._safe_decrypt(
        target, tmp_path / "fake-owner-public.pem",
        tmp_path / "fake-owner-private.pem", expected,
    )
    assert recovered == sender.fictional_payload()
    with pytest.raises(FileExistsError):
        sender.sender(tmp_path / "fake-owner-public.pem", target)
