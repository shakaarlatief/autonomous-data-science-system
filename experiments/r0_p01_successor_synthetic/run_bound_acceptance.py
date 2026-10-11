"""Synthetic fresh-run owner-acceptance signing and verification boundary.

This candidate adds two signed fields to the historical acceptance statement:
protocol (explicit domain separation) and claim_nonce (32 random bytes of
lowercase hexadecimal). The verifier receives an independent trusted
expected statement and refuses to treat values inside an untrusted proof
as authority for selecting the intended run.

It uses real Windows OpenSSH SSHSIG verification for Ed25519 and Node built-in
crypto for WebAuthn-shaped P-256 assertions. Keys are ephemeral, in-memory,
synthetic KeyObjects only. No hardware authenticator or owner credentials.

Fresh random nonces do not themselves guarantee durable one-time issuance,
protect a maliciously rolled-back issuer or complete successor scoring.
"""
from __future__ import annotations

import copy
import json
import re
import secrets
import subprocess
import tempfile
from pathlib import Path

from experiments.r0_p01_owner_acceptance_v01 import harness as historical

PROTOCOL = "ADS-R0-P01-RUN-BOUND-STATEMENT-V01"
SSH_NAMESPACE = "ads-r0-p01-claimed-run-v1"
WORKER = Path(__file__).with_name("run_bound_crypto.mjs")
FIELDS = set(historical.STATEMENT_FIELDS) | {"protocol", "claim_nonce"}
DIGEST_FIELDS = ("envelope_digest", "shown_digest", "semantic_base_digest")


def fresh_claim_nonce() -> str:
    """Generate an unpredictable, nonsecret identifier for one new claim."""
    return secrets.token_hex(32)


def new_run_statement(legacy_template: dict, *, claim_nonce: str) -> dict:
    """Build a distinct signed successor statement; never edit original V02."""
    if not isinstance(claim_nonce, str) or re.fullmatch(r"[0-9a-f]{64}", claim_nonce) is None:
        raise ValueError("claim_nonce must be exactly 32 bytes of lowercase hex")
    if set(legacy_template) != set(historical.STATEMENT_FIELDS):
        raise ValueError("historical comparison template must have exact expected fields")
    statement = {**copy.deepcopy(legacy_template), "protocol": PROTOCOL, "claim_nonce": claim_nonce}
    if not valid_shape(statement):
        raise ValueError("invalid new run-bound signed statement shape")
    return statement


def valid_shape(statement: dict) -> bool:
    """Validate the exact signed field set and cryptographic inputs."""
    return (
        isinstance(statement, dict)
        and set(statement) == FIELDS
        and all(isinstance(x, str) for x in statement.values())
        and statement["protocol"] == PROTOCOL
        and re.fullmatch(r"[0-9a-f]{64}", statement["claim_nonce"]) is not None
        and statement["decision"] in historical.DECISIONS
        and all(
            re.fullmatch(r"[0-9a-f]{64}", statement[key]) is not None
            for key in DIGEST_FIELDS
        )
    )


class SyntheticRunCrypto:
    """In-memory test signer and P-256 cryptographic verifier process."""

    def __init__(self) -> None:
        self.process = subprocess.Popen(
            ["node", str(WORKER), "--synthetic-rpc"],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding="utf-8",
        )

    def __enter__(self):
        return self

    def __exit__(self, *_):
        self.close()

    def call(self, method: str, **fields) -> dict:
        if self.process.poll() is not None:
            raise RuntimeError("synthetic signer unavailable")
        assert self.process.stdin is not None
        assert self.process.stdout is not None
        self.process.stdin.write(
            json.dumps({"method": method, **fields}, ensure_ascii=False) + "\n"
        )
        self.process.stdin.flush()
        line = self.process.stdout.readline()
        if not line:
            raise RuntimeError("synthetic signer terminated without reply")
        response = historical.strict_json(line)
        if response.get("ok") is not True:
            raise ValueError("synthetic signer input validation rejected")
        return response["result"]

    def close(self) -> None:
        if self.process.poll() is None:
            assert self.process.stdin is not None
            self.process.stdin.close()
            try:
                self.process.wait(timeout=5)
            except subprocess.TimeoutExpired:
                self.process.kill()
                self.process.wait(timeout=5)
        for stream in (self.process.stdout, self.process.stderr):
            if stream:
                stream.close()


def verify_for_run(
    *,
    presented: dict,
    trusted_expected: dict,
    proof: dict,
    credential: dict,
    node: SyntheticRunCrypto,
) -> bool:
    """Require a valid signature and exact trusted statement for this run.

    trusted_expected must originate from a trusted run controller, never be
    inferred from the presented proof or signed statement itself.
    """
    try:
        if not valid_shape(trusted_expected) or not valid_shape(presented):
            return False
        if presented != trusted_expected:
            return False
        if not isinstance(proof, dict) or not isinstance(credential, dict):
            return False
        if not historical.valid_credential(credential) or proof.get("kind") != credential.get("kind"):
            return False
        if credential["kind"] == "WEBAUTHN_ES256":
            return node.call(
                "verify_es256", statement=trusted_expected,
                proof=proof, credential=credential
            ).get("valid") is True
        if credential["kind"] != "SSH_ED25519":
            return False
        armor = proof.get("sshsig")
        if not isinstance(armor, str) or len(armor) > 20000:
            return False
        # Temporary files contain only public credential, proof and canonical
        # statement. No synthetic private key leaves the Node subprocess.
        with tempfile.TemporaryDirectory(prefix="r0-p01-synthetic-bound-verify-") as temp:
            directory = Path(temp)
            (directory / "allowed").write_text(
                "r0-p01 " + credential["public_key"] + "\n", encoding="utf-8"
            )
            (directory / "proof").write_text(armor, encoding="ascii")
            result = subprocess.run(
                [
                    "ssh-keygen", "-Y", "verify", "-f", str(directory / "allowed"),
                    "-I", "r0-p01", "-n", SSH_NAMESPACE,
                    "-s", str(directory / "proof")
                ],
                input=historical.canonical(trusted_expected),
                stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                env=historical.no_agent_env(), timeout=10,
            )
            return result.returncode == 0
    except (ValueError, KeyError, TypeError, UnicodeError, OSError, subprocess.TimeoutExpired, historical.IntegrityError):
        return False
