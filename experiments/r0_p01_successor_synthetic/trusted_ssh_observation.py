"""Bounded OpenSSH-sourced verification observations for synthetic R0-P01 F1.

Unlike caller-authored receipt dictionaries, the proof verdict here is derived
from an actual subprocess invocation over the exact trusted expected statement,
a caller-supplied proof, and a separately supplied trusted public signer.
It is an input-to-cryptographic-verifier observation, not an attestation of
which human initiated the signing operation or whether a P0/S01/S02/S03
event was terminal. Consequently, callers must not automatically convert a
VALID result into a completed F1 event without independent event-lifecycle
evidence.

This experimental boundary uses only synthetic run-bound statements and
public material. It neither enrolls real owner credentials nor changes the
historical V02 evidence or the successor authority contract. Its scratch
directory is explicitly supplied under a permitted workspace because the
runtime's read-only profile may not create host temporary files.

For OpenSSH verification, a nonzero return code alone is ambiguous: it might
represent a cryptographically rejected signature, a malformed proof, or a
broken verifier. Only recognized verifier-specific rejection messages are
classified INVALID. Unknown failures are conservatively ERROR, never silently
called a failed owner proof. Text recognition is scoped to the observed English
Windows OpenSSH output and is intentionally fail-closed if the runtime changes.
"""
from __future__ import annotations

import hashlib
import subprocess
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import Literal

from experiments.r0_p01_owner_acceptance_v01 import harness as legacy
from experiments.r0_p01_successor_synthetic import run_bound_acceptance as rb

Verdict = Literal["VALID", "INVALID", "ERROR"]
Reason = Literal[
    "VERIFIED", "UNTRUSTED_SIGNER", "CLAIM_MISMATCH",
    "MALFORMED_PROOF", "CRYPTOGRAPHIC_REJECTION", "OPENSSH_REJECTION", "VERIFIER_FAILURE",
]


@dataclass(frozen=True)
class SSHVerificationObservation:
    """Immutable local observation, not a remotely authenticated receipt.

    Evidence digests identify the exact bytes the verifier was asked to
    examine. These fields support re-verification but do not independently
    attest the machine or process that emitted a serialized observation.
    """

    verdict: Verdict
    reason: Reason
    expected_statement_sha256: str
    proof_sha256: str | None
    trusted_signer_id: str
    verifier_exit_code: int | None


def observe_ssh_verification(
    *,
    trusted_expected: dict,
    presented: dict,
    trusted_credential: dict,
    submitted_credential: dict,
    proof: dict,
    scratch_root: str | Path,
) -> SSHVerificationObservation:
    """Derive an SSH proof observation from a trusted run and actual OpenSSH.

    The trusted expected statement and trusted public credential must come
    from independent issuance/enrollment authority. No statement or signer is
    selected from within a submitted signature. The returned observation is
    not itself a durable trusted producer attestation and makes no claim
    about WebAuthn, capability, owner presence, terminal event completion,
    or the overall B01 score.
    """
    if not rb.valid_shape(trusted_expected):
        raise ValueError("trusted expected statement has invalid protocol/shape")
    if type(trusted_credential) is not dict or (
        trusted_credential.get("kind") != "SSH_ED25519"
        or not legacy.valid_credential(trusted_credential)
    ):
        raise ValueError("trusted enrolled public signer invalid")
    message = legacy.canonical(trusted_expected)
    expected_hash = hashlib.sha256(message).hexdigest()
    signature = proof.get("sshsig") if type(proof) is dict else None
    signature_bytes = None
    if type(signature) is str:
        try:
            signature_bytes = signature.encode("ascii")
        except UnicodeEncodeError:
            pass
    proof_hash = hashlib.sha256(signature_bytes).hexdigest() if signature_bytes is not None else None

    def outcome(verdict: Verdict, reason: Reason, code: int | None = None) -> SSHVerificationObservation:
        return SSHVerificationObservation(
            verdict, reason, expected_hash, proof_hash,
            trusted_credential["public_id"], code
        )

    if submitted_credential != trusted_credential:
        return outcome("INVALID", "UNTRUSTED_SIGNER")
    if not rb.valid_shape(presented) or presented != trusted_expected:
        return outcome("INVALID", "CLAIM_MISMATCH")
    if (
        type(proof) is not dict
        or proof.get("kind") != "SSH_ED25519"
        or signature_bytes is None
        or len(signature_bytes) > 20000
        or not signature_bytes.startswith(b"-----BEGIN SSH SIGNATURE-----")
        or not signature_bytes.rstrip().endswith(b"-----END SSH SIGNATURE-----")
    ):
        return outcome("INVALID", "MALFORMED_PROOF")

    root = Path(scratch_root)
    if not root.is_dir():
        return outcome("ERROR", "VERIFIER_FAILURE")
    try:
        with tempfile.TemporaryDirectory(prefix="p01-ssh-verifier-", dir=root) as tmp:
            location = Path(tmp)
            (location / "allowed").write_text(
                "r0-p01 " + trusted_credential["public_key"] + "\n",
                encoding="utf-8"
            )
            (location / "proof").write_bytes(signature_bytes)
            result = subprocess.run(
                [
                    "ssh-keygen", "-Y", "verify", "-f", str(location / "allowed"),
                    "-I", "r0-p01", "-n", rb.SSH_NAMESPACE,
                    "-s", str(location / "proof"),
                ],
                input=message,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                env=legacy.no_agent_env(),
                timeout=10,
            )
    except (OSError, subprocess.TimeoutExpired, ValueError):
        return outcome("ERROR", "VERIFIER_FAILURE")

    if result.returncode == 0:
        expected_prefix = f'Good "{rb.SSH_NAMESPACE}" signature for r0-p01 with ED25519 key '.encode("ascii")
        if result.stdout.startswith(expected_prefix) and not result.stderr.strip():
            return outcome("VALID", "VERIFIED", result.returncode)
        return outcome("ERROR", "VERIFIER_FAILURE", result.returncode)

    # A changing/unknown CLI failure must not be confused with a verified
    # cryptographic rejection. The exact known messages are restrictive.
    stderr = result.stderr
    if b"Signature verification failed: incorrect signature" in stderr:
        return outcome("INVALID", "CRYPTOGRAPHIC_REJECTION", result.returncode)
    if b"Couldn't parse signature:" in stderr or b"sig_verify: sshsig_armor:" in stderr:
        return outcome("INVALID", "MALFORMED_PROOF", result.returncode)
    if not stderr.strip() and result.stdout.strip() == b"Could not verify signature.":
        # OpenSSH also emits this generic refusal for a valid signature
        # whose embedded public signer is not in the allowed signer set.
        # Do not claim the cause was a malformed or bad cryptographic proof.
        return outcome("INVALID", "OPENSSH_REJECTION", result.returncode)
    return outcome("ERROR", "VERIFIER_FAILURE", result.returncode)
