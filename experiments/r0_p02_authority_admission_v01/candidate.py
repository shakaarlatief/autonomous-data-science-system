"""Deterministic R0-P02 architecture probe; no production authority.

PROBE_JSON_V01_SORTED_KEYS_COMPACT_UTF8_TEST_ONLY and
TEST_HMAC_SHA256_NOT_PRODUCTION are synthetic probe machinery only.

The permitted contract supplies operation kinds but does not enumerate result
labels (apart from the fresh-verifier pair) or concrete record layouts. This
candidate uses ADMITTED for admission, CHAIN_VALID for verified history,
NOT_STARTED/DONE/PARTIAL/UNKNOWN for recovery, and explicit failure reasons.
Latestness is NOT_APPLICABLE outside history verification, LATESTNESS_UNPROVEN
without a trusted witness, WITNESS_CONFIRMED against a matching witness, or
ROLLBACK_DETECTED against a newer witness. Records below are internal probe
representations of the Research 512 fields, not a production schema selection.
Each fixture case starts independently; concurrent proposals share one base.
"""

import copy
import hashlib
import hmac
import json


_CANONICALIZATION = "PROBE_JSON_V01_SORTED_KEYS_COMPACT_UTF8_TEST_ONLY"
_SIGNATURE = "TEST_HMAC_SHA256_NOT_PRODUCTION"
_ACCEPTANCE_CONTEXT = "ADS-GOVERNING-ACCEPTANCE/v1"
_CHECKPOINT_CONTEXT = "ADS-LEDGER-CHECKPOINT/v1"
_ZERO_DIGEST = "0" * 64
_ISSUED_AT = "2026-10-04T00:00:00Z"  # Fixed provenance; never ordering input.


class _ProbeFailure(Exception):
    def __init__(self, reason):
        super().__init__(reason)
        self.reason = reason


def _require(condition, reason):
    if not condition:
        raise _ProbeFailure(reason)


def _canonical(value):
    """Probe-only sorted-key, compact, literal UTF-8 JSON (no NaN/Infinity)."""
    return json.dumps(value, sort_keys=True, separators=(",", ":"),
                      ensure_ascii=False, allow_nan=False).encode("utf-8")


def _digest(value):
    return hashlib.sha256(_canonical(value)).hexdigest()


def _bytes_digest(value):
    return hashlib.sha256(value).hexdigest()


def _sign(statement, fixture):
    """Synthetic test HMAC; this is not owner-exclusive production proof."""
    return hmac.new(fixture["test_secret"].encode("utf-8"),
                    _canonical(statement), hashlib.sha256).hexdigest()


def _verify_proof(statement, proof, fixture):
    _require(isinstance(proof, dict), "INVALID_SIGNATURE")
    _require(proof.get("profile") == _SIGNATURE, "INVALID_SIGNATURE")
    _require(proof.get("signer_id") == fixture["test_signer_id"],
             "INVALID_SIGNATURE")
    signature = proof.get("signature")
    _require(isinstance(signature, str) and len(signature) == 64
             and all(c in "0123456789abcdef" for c in signature),
             "INVALID_SIGNATURE")
    _require(hmac.compare_digest(signature, _sign(statement, fixture)),
             "INVALID_SIGNATURE")


def _proof(statement, fixture):
    return {"profile": _SIGNATURE, "signer_id": fixture["test_signer_id"],
            "signature": _sign(statement, fixture)}


def _initial_state(fixture):
    state = copy.deepcopy(fixture["base_state"])
    effects = state["effects"]
    _require(len({effect["effect_id"] for effect in effects}) == len(effects),
             "DUPLICATE_EFFECT")
    state["effects"] = {effect["effect_id"]: effect for effect in effects}
    return state


def _semantic_base(state, dependencies, fixture):
    """Only named effects plus the governing versions used by every proposal.

    Effect identity, status, lineage and pinned contract revision all enter the
    digest. Carrier metadata, other effects and the chain head do not.
    """
    declared = sorted(set(dependencies))
    _require(all(effect_id in state["effects"] for effect_id in declared),
             "UNKNOWN_DEPENDENCY")
    return _digest({
        "effects": [state["effects"][effect_id] for effect_id in declared],
        "grammar_version": state["grammar_version"],
        "predicate_semantics_version": state["predicate_semantics_version"],
        "signer_set_version": fixture["signer_set_version"],
    })


def _render(envelope):
    # The synthetic signing client displays these exact deterministic bytes.
    return b"R0-P02 SYNTHETIC OWNER VIEW\n" + _canonical(envelope)


def _prepare(state, dependencies, acceptance_id, fixture, *, genesis=False):
    declared = sorted(set(dependencies))
    updates = []
    if not genesis:
        for effect_id in declared:
            old = state["effects"][effect_id]
            updates.append({
                "effect_id": effect_id,
                "predecessor_lineage_head": old["lineage_head"],
                "lineage_head": _digest({"acceptance_id": acceptance_id,
                                         "predecessor": old["lineage_head"],
                                         "effect_id": effect_id}),
                "status": "CURRENT",
                "contract_revision": old["contract_revision"],
            })
    envelope = {
        "kind": "GENESIS" if genesis else "ACCEPTANCE",
        "project_id": fixture["project_id"],
        "acceptance_id": acceptance_id,
        "decision": "ACCEPT",
        "depends_on": declared,
        "semantic_base_digest": _semantic_base(state, declared, fixture),
        "updates": updates,
    }
    if genesis:
        # Configured genesis trust pins both the signer set and initial state.
        envelope["initial_state_digest"] = _digest(state)
        envelope["signer_id"] = fixture["test_signer_id"]
    statement = {
        "context": _ACCEPTANCE_CONTEXT,
        "project_id": envelope["project_id"],
        "acceptance_id": acceptance_id,
        "envelope_digest": _digest(envelope),
        "shown_digest": _bytes_digest(_render(envelope)),
        "decision": envelope["decision"],
        "semantic_base_digest": envelope["semantic_base_digest"],
        "signer_set_version": fixture["signer_set_version"],
        "issued_at": _ISSUED_AT,
    }
    return {"envelope": envelope, "statement": statement,
            "proof": _proof(statement, fixture), "decision": "ACCEPT"}


def _verify_acceptance(packet, fixture):
    statement = packet["statement"]
    envelope = packet["envelope"]
    _verify_proof(statement, packet.get("proof"), fixture)
    _require(set(statement) == {"context", "project_id", "acceptance_id",
                               "envelope_digest", "shown_digest", "decision",
                               "semantic_base_digest", "signer_set_version",
                               "issued_at"}
             and isinstance(statement["issued_at"], str)
             and isinstance(statement["acceptance_id"], str)
             and bool(statement["acceptance_id"]), "INVALID_STATEMENT")
    _require(statement.get("context") == _ACCEPTANCE_CONTEXT,
             "INVALID_CONTEXT")
    _require(statement.get("project_id") == fixture["project_id"]
             and envelope.get("project_id") == fixture["project_id"],
             "PROJECT_MISMATCH")
    _require(statement.get("acceptance_id") == envelope.get("acceptance_id"),
             "ACCEPTANCE_ID_MISMATCH")
    _require(statement.get("signer_set_version") == fixture["signer_set_version"],
             "SIGNER_SET_MISMATCH")
    _require(statement.get("decision") in {"ACCEPT", "AMEND", "REJECT"}
             and statement["decision"] == packet.get("decision")
             and statement["decision"] == envelope.get("decision"),
             "DECISION_MISMATCH")
    _require(statement.get("envelope_digest") == _digest(envelope),
             "ENVELOPE_DIGEST_MISMATCH")
    _require(statement.get("shown_digest") == _bytes_digest(_render(envelope)),
             "SHOWN_DIGEST_MISMATCH")
    _require(statement.get("semantic_base_digest")
             == envelope.get("semantic_base_digest"), "SEMANTIC_BASE_MISMATCH")


def _entry_digest(entry):
    return _digest({key: value for key, value in entry.items()
                    if key != "entry_digest"})


def _entry(sequence_no, packet, previous):
    entry = {"sequence_no": sequence_no,
             "acceptance_id": packet["statement"]["acceptance_id"],
             "envelope_digest": packet["statement"]["envelope_digest"],
             "prev_entry_digest": previous}
    entry["entry_digest"] = _entry_digest(entry)
    return entry


class _Ledger:
    """Atomic in-memory admission with one current lineage per effect."""

    def __init__(self, fixture):
        self.fixture = fixture
        self.state = _initial_state(fixture)
        self.entries = []
        self.acceptances = {}

    @property
    def head(self):
        return self.entries[-1]["entry_digest"] if self.entries else _ZERO_DIGEST

    def admit(self, packet):
        _verify_acceptance(packet, self.fixture)
        envelope = packet["envelope"]
        acceptance_id = envelope["acceptance_id"]
        _require(acceptance_id not in self.acceptances, "DUPLICATE_ACCEPTANCE")
        _require(envelope["semantic_base_digest"] == _semantic_base(
            self.state, envelope["depends_on"], self.fixture),
            "STALE_SEMANTIC_BASE")
        _require(envelope["decision"] == "ACCEPT", "DECISION_NOT_ACCEPTED")
        next_state = copy.deepcopy(self.state)
        if not self.entries:
            _require(envelope["kind"] == "GENESIS", "GENESIS_REQUIRED")
            _require(envelope.get("initial_state_digest") == _digest(self.state)
                     and envelope.get("signer_id") == self.fixture["test_signer_id"]
                     and not envelope["updates"], "INVALID_GENESIS")
        else:
            _require(envelope["kind"] == "ACCEPTANCE", "DUPLICATE_GENESIS")
            changed = set()
            for update in envelope["updates"]:
                effect_id = update["effect_id"]
                _require(effect_id in envelope["depends_on"]
                         and effect_id not in changed, "INVALID_TRANSITION")
                old = next_state["effects"][effect_id]
                _require(old["status"] == "CURRENT"
                         and old["lineage_head"] == update["predecessor_lineage_head"]
                         and update["lineage_head"] != old["lineage_head"]
                         and update["status"] == "CURRENT", "LINEAGE_CONFLICT")
                next_state["effects"][effect_id] = {
                    "effect_id": effect_id, "lineage_head": update["lineage_head"],
                    "status": update["status"],
                    "contract_revision": update["contract_revision"],
                }
                changed.add(effect_id)
        entry = _entry(len(self.entries) + 1, packet, self.head)
        # Validation completes before any part of the authoritative state moves.
        self.state = next_state
        self.entries.append(entry)
        self.acceptances[acceptance_id] = copy.deepcopy(packet)
        return "ADMITTED"


def _checkpoint(ledger, checkpoint_class="ORDINARY"):
    statement = {
        "context": _CHECKPOINT_CONTEXT,
        "project_id": ledger.fixture["project_id"],
        "sequence_no": len(ledger.entries), "chain_head_digest": ledger.head,
        "signer_set_version": ledger.fixture["signer_set_version"],
        "checkpoint_class": checkpoint_class, "issued_at": _ISSUED_AT,
    }
    return {"statement": statement, "proof": _proof(statement, ledger.fixture)}


def _verify_checkpoint(checkpoint, fixture):
    statement = checkpoint["statement"]
    _verify_proof(statement, checkpoint.get("proof"), fixture)
    _require(statement.get("context") == _CHECKPOINT_CONTEXT,
             "INVALID_CHECKPOINT")
    _require(statement.get("project_id") == fixture["project_id"],
             "PROJECT_MISMATCH")
    _require(statement.get("signer_set_version") == fixture["signer_set_version"],
             "SIGNER_SET_MISMATCH")
    sequence = statement.get("sequence_no")
    head = statement.get("chain_head_digest")
    _require(type(sequence) is int and sequence >= 1
             and isinstance(head, str) and len(head) == 64
             and all(c in "0123456789abcdef" for c in head)
             and statement.get("checkpoint_class") in {"GENESIS", "ORDINARY"}
             and isinstance(statement.get("issued_at"), str), "INVALID_CHECKPOINT")
    return statement


def _verify_chain(entries, acceptances, checkpoints, fixture, witness=None):
    """Replay authenticity and admission, then compare checkpoints/witness.

    Same-repository checkpoints authenticate presented history, never latestness.
    A supplied witness is trusted by the caller outside the carrier snapshot.
    """
    _require(bool(entries), "GENESIS_REQUIRED")
    rebuilt = _Ledger(fixture)
    for expected_sequence, entry in enumerate(entries, 1):
        _require(type(entry.get("sequence_no")) is int
                 and entry["sequence_no"] == expected_sequence,
                 "INVALID_SEQUENCE")
        _require(entry.get("prev_entry_digest") == rebuilt.head,
                 "BROKEN_PREV_DIGEST")
        _require(entry.get("entry_digest") == _entry_digest(entry),
                 "ENTRY_DIGEST_MISMATCH")
        packet = acceptances.get(entry.get("acceptance_id"))
        _require(packet is not None, "MISSING_ACCEPTANCE")
        _require(entry.get("envelope_digest")
                 == packet["statement"]["envelope_digest"],
                 "ENVELOPE_DIGEST_MISMATCH")
        rebuilt.admit(packet)
        _require(entry == rebuilt.entries[-1], "ENTRY_BINDING_MISMATCH")
    genesis_checkpoint_seen = False
    for checkpoint in checkpoints:
        statement = _verify_checkpoint(checkpoint, fixture)
        sequence = statement["sequence_no"]
        _require(sequence <= len(entries)
                 and entries[sequence - 1]["entry_digest"]
                 == statement["chain_head_digest"], "CHECKPOINT_MISMATCH")
        if sequence == 1 and statement["checkpoint_class"] == "GENESIS":
            genesis_checkpoint_seen = True
    _require(genesis_checkpoint_seen, "GENESIS_CHECKPOINT_REQUIRED")
    latestness = "LATESTNESS_UNPROVEN"
    if witness is not None:
        statement = _verify_checkpoint(witness, fixture)
        sequence = statement["sequence_no"]
        if sequence > len(entries):
            return rebuilt, "ROLLBACK_DETECTED", "ROLLBACK_DETECTED"
        _require(entries[sequence - 1]["entry_digest"]
                 == statement["chain_head_digest"], "WITNESS_MISMATCH")
        latestness = "WITNESS_CONFIRMED"
    return rebuilt, "CHAIN_VALID", latestness


def _recover(ledger, packet, genesis_checkpoint):
    """Observe the carrier by replay; never infer DONE from a convenient retry."""
    try:
        rebuilt, _, _ = _verify_chain(ledger.entries, ledger.acceptances,
                                     [genesis_checkpoint], ledger.fixture)
        _verify_acceptance(packet, ledger.fixture)
    except _ProbeFailure:
        return "UNKNOWN"
    acceptance_id = packet["envelope"]["acceptance_id"]
    recorded = rebuilt.acceptances.get(acceptance_id)
    if recorded is not None:
        return "DONE" if recorded == packet else "UNKNOWN"
    if acceptance_id in ledger.acceptances:
        return "PARTIAL"
    return "NOT_STARTED"


def _seed(fixture):
    ledger = _Ledger(fixture)
    ledger.admit(_prepare(ledger.state, [], "GENESIS", fixture, genesis=True))
    return ledger, _checkpoint(ledger, "GENESIS")


def _dependencies(case, fixture):
    # Negative/recovery cases omit dependencies; choose from supplied state.
    return case.get("depends_on", [fixture["base_state"]["effects"][0]["effect_id"]])


def _rehash(entries):
    """Attacker can recompute unkeyed chain hashes, but cannot re-sign proofs."""
    previous = _ZERO_DIGEST
    for entry in entries:
        entry["prev_entry_digest"] = previous
        entry["entry_digest"] = _entry_digest(entry)
        previous = entry["entry_digest"]


def _evaluate_case(case, fixture):
    ledger, genesis_checkpoint = _seed(fixture)
    kind = case["kind"]
    latestness = "NOT_APPLICABLE"
    unverified_history = False
    try:
        if kind == "GENESIS_VALID":
            ledger, _, _ = _verify_chain(ledger.entries, ledger.acceptances,
                                         [genesis_checkpoint], fixture)
            outcome = "ADMITTED"
        elif kind in {"BASE_ACCEPTANCE_VALID", "UNRELATED_NON_GOVERNING_DOES_NOT_STALE",
                      "UNRELATED_GOVERNING_DOES_NOT_STALE", "CONFLICT_A_ADMITS",
                      "CONFLICT_B_STALE_AFTER_A"}:
            dependencies = _dependencies(case, fixture)
            proposal = _prepare(ledger.state, dependencies, "PROPOSAL", fixture)
            if kind in {"CONFLICT_A_ADMITS", "CONFLICT_B_STALE_AFTER_A"}:
                competitor = _prepare(ledger.state, dependencies, "COMPETITOR", fixture)
            if kind == "UNRELATED_NON_GOVERNING_DOES_NOT_STALE":
                proposal["carrier_metadata"] = {"knowledge_revision": "CHANGED"}
            elif kind == "UNRELATED_GOVERNING_DOES_NOT_STALE":
                unrelated = _prepare(ledger.state, [case["unrelated_effect"]],
                                     "UNRELATED", fixture)
                ledger.admit(unrelated)
            elif kind == "CONFLICT_B_STALE_AFTER_A":
                ledger.admit(competitor)
            outcome = ledger.admit(proposal)
        elif kind in {"FORGED_SIGNATURE_REJECT", "CHANGED_ENVELOPE_REJECT",
                      "DECISION_SUBSTITUTION_REJECT", "CROSS_PROJECT_REPLAY_REJECT",
                      "ACCEPTANCE_ID_REPLAY_REJECT", "HOST_TRANSFORM_INVARIANT",
                      "RECOVER_NOT_STARTED", "RECOVER_DONE_NO_DUPLICATE"}:
            proposal = _prepare(ledger.state, _dependencies(case, fixture),
                                "PROPOSAL", fixture)
            if kind == "FORGED_SIGNATURE_REJECT":
                old = proposal["proof"]["signature"]
                proposal["proof"]["signature"] = ("0" if old[0] != "0" else "1") + old[1:]
            elif kind == "CHANGED_ENVELOPE_REJECT":
                proposal["envelope"]["updates"][0]["contract_revision"] += "-TAMPERED"
            elif kind == "DECISION_SUBSTITUTION_REJECT":
                proposal["decision"] = "REJECT"
            elif kind == "CROSS_PROJECT_REPLAY_REJECT":
                other_fixture = dict(fixture, project_id=fixture["wrong_project_id"])
                proposal = _prepare(ledger.state, _dependencies(case, fixture),
                                    "PROPOSAL", other_fixture)
            elif kind == "ACCEPTANCE_ID_REPLAY_REJECT":
                ledger.admit(proposal)
            elif kind == "HOST_TRANSFORM_INVARIANT":
                # Only carrier topology changes; signed semantic bytes are exact.
                before = _canonical(proposal)
                carrier = {"commit": "BEFORE-SQUASH", "parents": ["PARENT"],
                           "payload": copy.deepcopy(proposal)}
                carrier["commit"] = "AFTER-SQUASH"
                carrier["parents"] = ["OTHER-PARENT"]
                _require(before == _canonical(carrier["payload"]), "HOST_PAYLOAD_CHANGED")
                proposal = carrier["payload"]
            elif kind == "RECOVER_DONE_NO_DUPLICATE":
                ledger.admit(proposal)
            if kind in {"RECOVER_NOT_STARTED", "RECOVER_DONE_NO_DUPLICATE"}:
                prior_count = len(ledger.entries)
                outcome = _recover(ledger, proposal, genesis_checkpoint)
                _require(len(ledger.entries) == prior_count, "RECOVERY_MUTATED_LEDGER")
            else:
                outcome = ledger.admit(proposal)
        elif kind in {"DUPLICATE_SEQUENCE_REJECT", "BROKEN_PREV_DIGEST_REJECT",
                      "MIDDLE_CHAIN_REWRITE_DETECT", "PRIOR_WITNESS_TRUNCATION_DETECT",
                      "FRESH_VERIFIER_TRUNCATION_LIMIT",
                      "EXTERNAL_HEAD_WITNESS_TRUNCATION_DETECT"}:
            proposal = _prepare(ledger.state, _dependencies(case, fixture),
                                "PROPOSAL", fixture)
            ledger.admit(proposal)
            successor = _prepare(ledger.state, _dependencies(case, fixture),
                                 "SUCCESSOR", fixture)
            ledger.admit(successor)
            full_checkpoint = _checkpoint(ledger)
            entries = copy.deepcopy(ledger.entries)
            acceptances = copy.deepcopy(ledger.acceptances)
            checkpoints = [genesis_checkpoint, full_checkpoint]
            witness = None
            if kind == "DUPLICATE_SEQUENCE_REJECT":
                entries[-1]["sequence_no"] = entries[-2]["sequence_no"]
                entries[-1]["entry_digest"] = _entry_digest(entries[-1])
            elif kind == "BROKEN_PREV_DIGEST_REJECT":
                entries[-1]["prev_entry_digest"] = _ZERO_DIGEST
                entries[-1]["entry_digest"] = _entry_digest(entries[-1])
            elif kind == "MIDDLE_CHAIN_REWRITE_DETECT":
                # Even a fully rehashed suffix must bind authenticated envelopes.
                entries[1]["envelope_digest"] = _digest({"replacement": "unsigned"})
                _rehash(entries)
            else:
                entries = entries[:2]
                included_ids = {entry["acceptance_id"] for entry in entries}
                acceptances = {key: value for key, value in acceptances.items()
                               if key in included_ids}
                # A suppressed newer same-carrier checkpoint cannot be assumed.
                checkpoints = [genesis_checkpoint]
                if kind != "FRESH_VERIFIER_TRUNCATION_LIMIT":
                    witness = full_checkpoint
            unverified_history = True
            ledger, outcome, latestness = _verify_chain(
                entries, acceptances, checkpoints, fixture, witness)
            unverified_history = False
        else:
            raise ValueError("Unsupported fixture operation kind: " + str(kind))

        # All successful incremental folds must reproduce exactly on full replay.
        rebuilt, _, _ = _verify_chain(ledger.entries, ledger.acceptances,
                                     [genesis_checkpoint], fixture)
        _require(rebuilt.state == ledger.state and rebuilt.head == ledger.head,
                 "REBUILD_MISMATCH")
    except _ProbeFailure as failure:
        outcome = failure.reason
    return {"case_id": case["case_id"], "outcome": outcome,
            "latestness": latestness,
            "semantic_state_digest": None if unverified_history else _digest(ledger.state),
            "chain_head_digest": None if unverified_history else ledger.head}


def evaluate_fixture(fixture: dict) -> dict:
    """Evaluate only supplied data; no I/O, clocks, subprocesses or model calls."""
    if fixture.get("canonicalization_profile") != _CANONICALIZATION:
        raise ValueError("Unsupported probe canonicalization profile")
    if fixture.get("signature_profile") != _SIGNATURE:
        raise ValueError("Unsupported synthetic signature profile")
    if fixture.get("schema_version") != 1 or fixture.get("protocol") != "R0-P02-V01":
        raise ValueError("Unsupported fixture protocol/schema")
    return {"schema_version": 1, "protocol": "R0-P02-V01",
            "cases": [_evaluate_case(case, fixture) for case in fixture["cases"]]}
