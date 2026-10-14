"""Proof-oriented tests for fake-only public-recipient CMS preflight."""
from __future__ import annotations

import hashlib
from pathlib import Path
import subprocess

import pytest

import experiments.r0_p03_navigation_probe.synthetic_cms_recipient_preflight as cms


def test_safe_decrypt_discards_provisional_plaintext_on_failure(monkeypatch, tmp_path):
    """Crypto tool errors may still leave provisional stdout in memory."""
    leaked = b"FAKE_UNTRUSTED_PROVISIONAL_BYTES"
    monkeypatch.setattr(
        cms, "_invoke",
        lambda args: subprocess.CompletedProcess(args, 4, stdout=leaked, stderr=b"decryption failed"),
    )
    result = cms._safe_decrypt(
        tmp_path / "fake.cms", tmp_path / "fake.pem",
        tmp_path / "fake.key", hashlib.sha256(leaked).hexdigest(),
    )
    assert result is None


def test_safe_decrypt_refuses_success_with_wrong_commitment(monkeypatch, tmp_path):
    packet = cms.FAKE_PACKET
    monkeypatch.setattr(
        cms, "_invoke",
        lambda args: subprocess.CompletedProcess(args, 0, stdout=packet, stderr=b""),
    )
    result = cms._safe_decrypt(
        tmp_path / "fake.cms", tmp_path / "fake.pem",
        tmp_path / "fake.key", hashlib.sha256(b"other payload").hexdigest(),
    )
    assert result is None


def test_safe_decrypt_accepts_success_with_exact_commitment(monkeypatch, tmp_path):
    packet = cms.FAKE_PACKET
    monkeypatch.setattr(
        cms, "_invoke",
        lambda args: subprocess.CompletedProcess(args, 0, stdout=packet, stderr=b""),
    )
    result = cms._safe_decrypt(
        tmp_path / "fake.cms", tmp_path / "fake.pem",
        tmp_path / "fake.key", hashlib.sha256(packet).hexdigest(),
    )
    assert result == packet


@pytest.mark.skipif(not cms.OPENSSL.is_file(), reason="Git-for-Windows OpenSSL required")
def test_actual_disposable_gcm_recipient_round_trip(capsys):
    receipt = cms.run_demo()
    assert receipt["synthetic_only"] is True
    assert receipt["rsa_certificate_generated"] is True
    assert receipt["aes_256_gcm_confirmed"] is True
    assert receipt["fake_packet_digest_verified"] is True
    assert receipt["separate_subprocess_recovery_pass"] is True
    assert receipt["tampered_ciphertext_rejected"] is True
    assert receipt["unsafe_plaintext_returned_to_safe_caller"] is False
    assert receipt["mock_encryptor_private_key_file_present"] is False
    assert receipt["plaintext_packet_file_created"] is False
    assert receipt["different_os_principals_tested"] is False
    assert receipt["owner_key_custody_qualified"] is False
    assert receipt["real_gold_custody_qualified"] is False
    assert capsys.readouterr().out == ""
