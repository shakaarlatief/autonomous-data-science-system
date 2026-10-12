"""Read-only, claim-bound SSH proof assessment of a synthetic issuer journal.

This is an experimental verification consumer, NOT a trusted receipt issuer.
It reconstructs the exact signed statement from an independently supplied
synthetic issuer context and the journal's recorded nonce. It then checks
record structure, sequence, expected bytes, trust-root binding and every
recorded SSH admission using real OpenSSH. The source database is opened with
SQLite mode=ro, and the program never starts a signing operation.

Proof validity is distinct from producer authenticity. The journal's local
origin, original issuance event, real owner identity, human decision ceremony,
and external freshness are not attested by this source. A locally rewritten
journal accompanied by a valid previously obtained proof is not excluded
without a separate independent witness or authenticated issuer. In particular,
the result must never be promoted into an R0-P01 terminal event or F1 score.
"""
from __future__ import annotations

import hashlib
import re
import sqlite3
from contextlib import closing
from dataclasses import dataclass
from pathlib import Path

from experiments.r0_p01_owner_acceptance_v01 import harness as legacy
from experiments.r0_p01_successor_synthetic import run_bound_acceptance as run
from experiments.r0_p01_successor_synthetic.trusted_claim_store import (
    SyntheticClaimStore,
)
from experiments.r0_p01_successor_synthetic.trusted_ssh_observation import (
    observe_ssh_verification,
)


class UnqualifiedSourceError(RuntimeError):
    """No supported source-bound conclusion can be made from this journal."""


@dataclass(frozen=True)
class SSHClaimAssessment:
    """Limited assessment: an SSH proof is valid *as presented in the source*.

    `source_origin_authenticated=False` is deliberately unconditional:
    cryptographic proof validity cannot authenticate the writer of SQLite
    rows, assert that a browser ran, or exclude rollback of the entire store.
    """

    issuer_genesis_sha256: str
    claim_nonce: str
    claim_sequence: int
    acceptance_id: str
    journal_status: str
    expected_statement_sha256: str
    admitted_proof_sha256: str | None
    proof_verification: str
    source_origin_authenticated: bool = False


def _digest(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def _require(condition: bool, description: str) -> None:
    if not condition:
        raise UnqualifiedSourceError(description)


def assess_ssh_claim(
    *,
    journal_path: str | Path,
    issuer_id: str,
    legacy_template: dict,
    enrolled_credential: dict,
    require_governed_issuance: bool,
    trusted_claim_nonce: str,
    trusted_acceptance_id: str,
    scratch_root: str | Path,
) -> SSHClaimAssessment:
    """Verify a single known claim from a complete, coherent read-only view.

    All trust inputs are distinct from journal content. Callers must source
    them from an authorized controller, not from the submitted proof or a
    JSON wrapper around the journal. The trusted nonce is chosen by the
    controller, and must not be inferred by picking an arbitrary ADMITTED
    row. The journal provides the presented status and public signature.

    Every stored SSH admission is reverified. A corrupt unrelated admitted
    proof prevents success for the selected claim; selective success over an
    inconsistent journal is not allowed. The SQLite read transaction gives
    a coherent snapshot under ordinary concurrent writer operation.
    """
    _require(
        type(issuer_id) is str
        and re.fullmatch(r"SYNTHETIC-[A-Za-z0-9_-]{8,100}", issuer_id) is not None,
        "invalid synthetic trust anchor",
    )
    _require(type(require_governed_issuance) is bool, "invalid issuer policy")
    _require(
        type(enrolled_credential) is dict
        and enrolled_credential.get("kind") == "SSH_ED25519",
        "not a synthetic SSH enrolled signer",
    )
    try:
        _require(legacy.valid_credential(enrolled_credential), "untrusted SSH credential")
        run.new_run_statement(legacy_template, claim_nonce="0" * 64)
    except (ValueError, TypeError, KeyError, IndexError, legacy.IntegrityError) as exc:
        raise UnqualifiedSourceError("invalid trusted issuer genesis") from exc
    _require(
        type(trusted_claim_nonce) is str
        and re.fullmatch(r"[0-9a-f]{64}", trusted_claim_nonce) is not None,
        "invalid externally selected claim nonce",
    )
    _require(
        type(trusted_acceptance_id) is str
        and legacy_template["acceptance_id"] == trusted_acceptance_id,
        "trusted acceptance identity mismatch",
    )
    context = {
        "issuer_id": issuer_id,
        "template": legacy_template,
        "trusted_credential": enrolled_credential,
        "protocol": run.PROTOCOL,
        "require_governed_issuance": require_governed_issuance,
    }
    context_bytes = legacy.canonical(context)
    genesis_sha = _digest(SyntheticClaimStore.DOMAIN + context_bytes)
    source_path = Path(journal_path)
    _require(source_path.is_file(), "missing journal (must not be recreated)")

    try:
        # Open the current SQLite database and WAL under read-only permissions.
        with closing(sqlite3.connect(
            source_path.resolve().as_uri() + "?mode=ro", uri=True,
            isolation_level=None, timeout=10,
        )) as connection:
            connection.execute("PRAGMA query_only=ON")
            connection.execute("BEGIN")
            identity = connection.execute(
                "SELECT version,context_blob,sequence FROM identity WHERE id=1"
            ).fetchone()
            _require(identity is not None and len(identity) == 3, "issuer genesis absent")
            _require(
                type(identity[0]) is int and identity[0] == SyntheticClaimStore.VERSION
                and type(identity[1]) is bytes and identity[1] == context_bytes
                and type(identity[2]) is int and identity[2] >= 0,
                "issuer identity or sequence mismatch",
            )
            rows = connection.execute(
                "SELECT seq,nonce,expected_blob,expected_sha256,status,"
                "admission_blob,admission_sha256 FROM claims ORDER BY seq"
            ).fetchall()
            _require(len(rows) == identity[2], "claim count mismatch")
            seen = set()
            active = 0
            selected = None
            for index, (
                seq, nonce, expected_blob, expected_hash,
                status, admitted_blob, admitted_hash,
            ) in enumerate(rows, start=1):
                _require(
                    type(seq) is int and seq == index
                    and type(nonce) is str
                    and re.fullmatch(r"[0-9a-f]{64}", nonce) is not None
                    and nonce not in seen,
                    "invalid or repeated claim sequence/nonce",
                )
                seen.add(nonce)
                statement = run.new_run_statement(legacy_template, claim_nonce=nonce)
                source_statement = legacy.canonical(statement)
                _require(
                    type(expected_blob) is bytes
                    and expected_blob == source_statement
                    and type(expected_hash) is str
                    and expected_hash == _digest(source_statement),
                    "stored expected statement differs from trusted issuer",
                )
                _require(status in {"ISSUED", "SUPERSEDED", "ADMITTED"}, "invalid claim lifecycle")
                admission_digest = None
                verdict = "NOT_RUN"
                if status == "ADMITTED":
                    _require(
                        type(admitted_blob) is bytes
                        and type(admitted_hash) is str
                        and admitted_hash == _digest(admitted_blob),
                        "admitted proof bytes/hash mismatch",
                    )
                    try:
                        record = legacy.strict_json(admitted_blob)
                        _require(
                            legacy.canonical(record) == admitted_blob
                            and type(record) is dict
                            and set(record) == {"presented", "proof", "credential"}
                            and record["presented"] == statement
                            and record["credential"] == enrolled_credential,
                            "admitted proof does not match trusted signed statement/signer",
                        )
                        observed = observe_ssh_verification(
                            trusted_expected=statement,
                            presented=record["presented"],
                            trusted_credential=enrolled_credential,
                            submitted_credential=record["credential"],
                            proof=record["proof"],
                            scratch_root=scratch_root,
                        )
                    except (ValueError, TypeError, KeyError, UnicodeError,
                            legacy.IntegrityError) as exc:
                        raise UnqualifiedSourceError("malformed recorded signature") from exc
                    _require(
                        observed.verdict == "VALID",
                        "recorded admission has no presently valid native SSH proof",
                    )
                    admission_digest = _digest(admitted_blob)
                    verdict = observed.verdict
                else:
                    _require(
                        admitted_blob is None and admitted_hash is None,
                        "nonadmitted claim contains proof material",
                    )
                if status == "ISSUED":
                    active += 1
                    _require(index == len(rows), "older issued claim not superseded")
                if nonce == trusted_claim_nonce:
                    selected = SSHClaimAssessment(
                        issuer_genesis_sha256=genesis_sha,
                        claim_nonce=nonce,
                        claim_sequence=index,
                        acceptance_id=trusted_acceptance_id,
                        journal_status=status,
                        expected_statement_sha256=_digest(source_statement),
                        admitted_proof_sha256=admission_digest,
                        proof_verification=verdict,
                    )
            _require(active <= 1, "multiple currently issued claims")
            # Auxiliary records cannot be ignored in a journal-wide statement
            # of coherence. Their hashes/relationships are checked, but their
            # own authorization source remains synthetic/unattested.
            authorizations = connection.execute(
                "SELECT claim_seq,authorization_blob,authorization_sha256 "
                "FROM run_authorizations ORDER BY claim_seq"
            ).fetchall()
            _require(
                len(authorizations) == (len(rows) if require_governed_issuance else 0),
                "wrong governed-authorization count",
            )
            refs = set()
            for index, (seq, blob, sha) in enumerate(authorizations, start=1):
                _require(
                    type(seq) is int and seq == index
                    and type(blob) is bytes and _digest(blob) == sha,
                    "invalid authorization sequence/hash",
                )
                authorization = legacy.strict_json(blob)
                _require(
                    legacy.canonical(authorization) == blob
                    and SyntheticClaimStore._valid_authorization(authorization)
                    and authorization["authorization_ref"] not in refs,
                    "invalid synthetic authorization evidence",
                )
                refs.add(authorization["authorization_ref"])
                if authorization["purpose"] == "REPLACEMENT":
                    _require(
                        authorization["replacement_of"] in set(x[1] for x in rows[:index-1]),
                        "replacement does not reference earlier known claim",
                    )
            observations = connection.execute(
                "SELECT seq,claim_nonce,kind,observation_blob,observation_sha256 "
                "FROM observations ORDER BY seq"
            ).fetchall()
            for index, (seq, nonce, kind, blob, sha) in enumerate(observations, start=1):
                _require(
                    type(seq) is int and seq == index
                    and nonce in seen and type(blob) is bytes and _digest(blob) == sha,
                    "invalid synthetic observation sequence/hash",
                )
                observation = legacy.strict_json(blob)
                _require(
                    legacy.canonical(observation) == blob
                    and SyntheticClaimStore._valid_observation(observation)
                    and observation["claim_nonce"] == nonce
                    and observation["kind"] == kind,
                    "invalid synthetic observation content",
                )
            _require(selected is not None, "trusted claim not found in issuer source")
            connection.commit()
            return selected
    except sqlite3.Error as exc:
        raise UnqualifiedSourceError("source database is unavailable or corrupt") from exc
    except (ValueError, TypeError, KeyError, IndexError, UnicodeError,
            legacy.IntegrityError) as exc:
        raise UnqualifiedSourceError("source journal has malformed evidence") from exc
