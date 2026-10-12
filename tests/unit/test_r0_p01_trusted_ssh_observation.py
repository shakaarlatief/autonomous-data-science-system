"""Real non-owner OpenSSH observations, source-error and forgery negatives.

The test's expected verdicts are authored separately from the historical V02
harness and the synthetic receipt-interpretation reference. The positive proof
comes from a separate ephemeral Node Ed25519 signer; neither private keys nor
owner devices are exercised, and no real R0-P01 attempt is initiated.
"""
from __future__ import annotations

import copy
import json
import shutil
import subprocess
from pathlib import Path

import pytest

from experiments.r0_p01_owner_acceptance_v01 import harness as legacy
from experiments.r0_p01_successor_synthetic import run_bound_acceptance as rb
from experiments.r0_p01_successor_synthetic import trusted_ssh_observation as observer


@pytest.fixture(scope="module")
def signed():
    if not shutil.which("node") or not shutil.which("ssh-keygen"):
        pytest.skip("Node and OpenSSH required for actual source verification")
    template = json.loads(
        (Path(legacy.HERE) / "clarification_vectors_v02.json").read_text(encoding="utf-8")
    )["statement"]
    statement = rb.new_run_statement(template, claim_nonce="1" * 64)
    with rb.SyntheticRunCrypto() as node:
        primary = node.call(
            "sign_ssh",
            label="SYNTHETIC-NON-OWNER-SSH-RECEIPT-PRIMARY-001",
            statement=statement,
        )
        foreign = node.call(
            "sign_ssh",
            label="SYNTHETIC-NON-OWNER-SSH-RECEIPT-FOREIGN-001",
            statement=statement,
        )
    yield statement, primary, foreign


def observe(tmp_path, material, *, presented=None, credential=None, proof=None, root=None):
    statement, primary, _ = material
    return observer.observe_ssh_verification(
        trusted_expected=statement,
        presented=statement if presented is None else presented,
        trusted_credential=primary["credential"],
        submitted_credential=primary["credential"] if credential is None else credential,
        proof=primary["proof"] if proof is None else proof,
        scratch_root=tmp_path if root is None else root,
    )


def test_real_openssh_positive_returns_verifier_derived_valid_with_exact_sha(signed, tmp_path):
    statement, primary, _ = signed
    result = observe(tmp_path, signed)
    assert result.verdict == "VALID"
    assert result.reason == "VERIFIED"
    assert result.verifier_exit_code == 0
    assert result.trusted_signer_id == primary["credential"]["public_id"]
    assert result.expected_statement_sha256 == legacy.sha(legacy.canonical(statement))
    assert result.proof_sha256 == legacy.sha(primary["proof"]["sshsig"].encode("ascii"))


def test_changed_decision_rejects_at_trusted_expected_boundary(signed, tmp_path):
    statement, _, _ = signed
    altered = copy.deepcopy(statement)
    altered["decision"] = "REJECT"
    result = observe(tmp_path, signed, presented=altered)
    assert (result.verdict, result.reason) == ("INVALID", "CLAIM_MISMATCH")
    assert result.verifier_exit_code is None


def test_foreign_public_signer_is_not_authorized(signed, tmp_path):
    _, _, foreign = signed
    assert (observe(tmp_path, signed, credential=foreign["credential"]).verdict) == "INVALID"


def test_foreign_valid_signature_under_enrolled_public_key_is_rejected(signed, tmp_path):
    _, _, foreign = signed
    result = observe(tmp_path, signed, proof=foreign["proof"])
    assert (result.verdict, result.reason) == ("INVALID", "OPENSSH_REJECTION")


def test_well_formed_signature_for_different_semantic_statement_is_invalid(signed, tmp_path):
    statement, primary, _ = signed
    changed = copy.deepcopy(statement)
    changed["decision"] = "REJECT"
    # The presented message is accepted only as an exact trusted expected
    # statement. Deliberately change the expected trusted message too, so the
    # signature must actually be rejected by the external cryptographic tool.
    result = observer.observe_ssh_verification(
        trusted_expected=changed,
        presented=changed,
        trusted_credential=primary["credential"],
        submitted_credential=primary["credential"],
        proof=primary["proof"],
        scratch_root=tmp_path,
    )
    assert (result.verdict, result.reason) == ("INVALID", "CRYPTOGRAPHIC_REJECTION")


@pytest.mark.parametrize("bad", [
    {"kind": "SSH_ED25519", "sshsig": "NOT-SSHSIG"},
    {"kind": "SSH_ED25519"},
    {"kind": "WEBAUTHN_ES256", "sshsig": "bogus"},
])
def test_malformed_or_wrong_mechanism_is_not_valid(signed, tmp_path, bad):
    result = observe(tmp_path, signed, proof=bad)
    assert (result.verdict, result.reason) == ("INVALID", "MALFORMED_PROOF")


def test_malformed_armor_in_existing_headers_is_not_verified(signed, tmp_path):
    _, primary, _ = signed
    forged = copy.deepcopy(primary["proof"])
    forged["sshsig"] = forged["sshsig"].replace(
        "-----BEGIN SSH SIGNATURE-----",
        "-----BEGIN SSH SIGNATURE-----\nNOT-BASE64",
    )
    result = observe(tmp_path, signed, proof=forged)
    assert result.verdict == "INVALID"


def test_unavailable_binary_is_error_not_invalid_signature(signed, tmp_path, monkeypatch):
    def unavailable(*args, **kwargs):
        raise FileNotFoundError("synthetic verifier unavailable")
    monkeypatch.setattr(observer.subprocess, "run", unavailable)
    result = observe(tmp_path, signed)
    assert (result.verdict, result.reason) == ("ERROR", "VERIFIER_FAILURE")


def test_time_out_is_error_not_invalid_signature(signed, tmp_path, monkeypatch):
    def timeout(*args, **kwargs):
        raise subprocess.TimeoutExpired(cmd="ssh-keygen", timeout=10)
    monkeypatch.setattr(observer.subprocess, "run", timeout)
    result = observe(tmp_path, signed)
    assert (result.verdict, result.reason) == ("ERROR", "VERIFIER_FAILURE")


def test_unknown_nonzero_exit_is_error_not_invalid_proof(signed, tmp_path, monkeypatch):
    def failure(*args, **kwargs):
        return subprocess.CompletedProcess(
            args=args, returncode=91, stdout=b"", stderr=b"unknown I/O failure"
        )
    monkeypatch.setattr(observer.subprocess, "run", failure)
    result = observe(tmp_path, signed)
    assert result.verdict == "ERROR"
    assert result.verifier_exit_code == 91


def test_forged_success_exit_without_expected_verifier_output_fails_closed(
    signed, tmp_path, monkeypatch,
):
    def forged_success(*args, **kwargs):
        return subprocess.CompletedProcess(args=args, returncode=0, stdout=b"", stderr=b"")
    monkeypatch.setattr(observer.subprocess, "run", forged_success)
    assert observe(tmp_path, signed).verdict == "ERROR"


def test_inaccessible_scratch_fails_as_verifier_error(signed, tmp_path):
    result = observe(tmp_path, signed, root=tmp_path / "nonexistent")
    assert (result.verdict, result.reason) == ("ERROR", "VERIFIER_FAILURE")


def test_original_synthetic_receipt_derivation_remains_separate(signed, tmp_path):
    result = observe(tmp_path, signed)
    assert result.verdict == "VALID"
    assert not hasattr(result, "event_terminal")
    assert not hasattr(result, "setup")
    assert not hasattr(result, "rp_consumed")
