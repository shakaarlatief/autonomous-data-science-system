"""Read-only contract guard for the prospective R0-P01 Q0 requirements trace.

The guard verifies that a proposed successor's requirements inventory remains
traceable to exactly the owner-approved REV04 input bytes and to the historical
frozen V02 fixture, result contract, and reference implementation. It neither
imports the owner harness nor executes credential handling, verifier ceremonies,
synthetic signer generation, or independent score classification.

A passing check establishes consistency of an unfrozen requirements inventory.
It does not qualify a future source implementation, prove that the new scorer
implements its declared decision policy, or authorize an owner trial.

The historical code hashes act as *baseline comparison identities*, not
instructions to reuse that code or preserve its source organization.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any

try:
    from scripts import r0_p01_clause_inventory as clause_inventory
    from scripts import r0_p01_clause_guard as clause_guard
except ModuleNotFoundError:
    import r0_p01_clause_inventory as clause_inventory
    import r0_p01_clause_guard as clause_guard


ROOT = Path(__file__).resolve().parents[1]
TRACE_PATH = (
    "docs/research/r0_p01_successor_design/"
    "R0_P01_Q0_REQUIREMENTS_TRACE_REV02_UNFROZEN.json"
)
RECEIPT_PATH = (
    "docs/research/r0_p01_successor_design/"
    "R0_P01_PREFREEZE_OWNER_DECISIONS_RECEIPT_20261010.json"
)
OLD_FIXTURE = "experiments/r0_p01_owner_acceptance_v01/fixture.json"
OLD_RESULT = "experiments/r0_p01_owner_acceptance_v01/result_contract.json"
OLD_INVENTORY = (
    "experiments/r0_p01_owner_acceptance_v01/"
    "legacy_volume_inventory_rule.json"
)
APPROVED_CONTRACT_SHA256 = (
    "9160a30c481c1c67c2ec857238f5a04b44f618b2ef589ef4f1c514eb3b3d6175"
)
APPROVED_POLICY_SHA256 = (
    "9b5bbc4d2c4802fc80b46bcaa3d003640c33e8e4784d39ef7995dbf193dff86c"
)

EXPECTED_REQUIREMENTS = {
    *(f"C{i:02d}" for i in range(1, 14)),
    *(f"R{i:02d}" for i in range(1, 41)),
}
EXPECTED_EFFECT_COUNTS = {"S01": 1, "S02": 2, "S03": 4, "L01": 30}
EXPECTED_VOLUME = {
    "projected_acceptance_count": 97,
    "projected_effect_count": 157,
    "effects_per_acceptance_distribution": {"1": 62, "2": 17, "3": 11, "4": 7},
}


def sha256(data: bytes) -> str:
    """Digest exact bytes without converting LF/CRLF or normalizing JSON."""

    return hashlib.sha256(data).hexdigest()


def read_json(root: Path, relative_path: str) -> dict[str, Any]:
    """Read a repository-relative document without importing executable code.

    JSON duplicate object keys are rejected rather than silently overwritten.
    This matters for status fields and the binding of claim and source hashes.
    """

    def unique_pairs(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
        result: dict[str, Any] = {}
        for key, value in pairs:
            if key in result:
                raise ValueError(f"duplicate JSON key: {key!r}")
            result[key] = value
        return result

    source = root / relative_path
    return json.loads(source.read_text(encoding="utf-8"), object_pairs_hook=unique_pairs)


def validate_documents(
    trace: dict[str, Any],
    fixture: dict[str, Any],
    result: dict[str, Any],
    inventory: dict[str, Any],
    approval: dict[str, Any],
) -> list[str]:
    """Find specification inconsistencies without mutating source records.

    This validation checks coverage and retained protocol invariants, not live
    owner behavior. The old fixture and result contract are independent
    reference inputs whose controls/trials must remain represented, whereas
    the approved successor decision receipt controls what is authorized.
    """

    issues: list[str] = []
    if trace.get("status") != "Q0_REV02_PROVISIONAL_NOT_FROZEN":
        issues.append("Q0 trace may not claim a frozen or executable status")
    if trace.get("owner_claim_status") != "NOT_AUTHORIZED":
        issues.append("Q0 trace must not authorize owner claims")
    if trace.get("actual_successor_fixture_frozen") is not False:
        issues.append("Q0 trace must not claim an implementation freeze")

    requirements = trace.get("requirements", [])
    ids = [r.get("id") for r in requirements if isinstance(r, dict)]
    if len(ids) != len(requirements) or len(ids) != len(set(ids)):
        issues.append("requirement IDs must be unique and all rows structured")
    if set(ids) != EXPECTED_REQUIREMENTS:
        issues.append("missing, extra, or renamed traceability requirement IDs")
    aliases = set(trace.get("sources", {}))
    for row in requirements:
        if not isinstance(row, dict):
            continue
        if row.get("status") != "QUALIFICATION_REQUIRED":
            issues.append(f"{row.get('id')}: premature implementation qualification claim")
        for field in ("sources", "evidence_requirements", "synthetic_test_ids"):
            if not row.get(field) or not isinstance(row[field], list):
                issues.append(f"{row.get('id')}: missing list {field}")
        if not set(row.get("sources", [])).issubset(aliases):
            issues.append(f"{row.get('id')}: unknown source alias")
    if trace.get("security_controls") != fixture.get("security_controls"):
        issues.append("thirteen frozen security controls differ")
    old_controls = fixture.get("security_controls", [])
    if len(old_controls) != 13 or len(set(old_controls)) != 13:
        issues.append("historical fixture has invalid control count")
    if result.get("cryptographic_proof_viability", {}).get("required_controls") != old_controls[:10]:
        issues.append("historical proof viability ten-control basis differs")

    trial_effects = {
        row["trial_id"]: len(row["effects"])
        for row in fixture.get("owner_trials", [])
        if isinstance(row, dict) and "trial_id" in row and isinstance(row.get("effects"), list)
    }
    if trial_effects != EXPECTED_EFFECT_COUNTS:
        issues.append("frozen owner-trial count/effect sizes differ")
    if [
        (row.get("trial_id"), row.get("effects")) for row in trace.get("owner_trials", [])
    ] != list(EXPECTED_EFFECT_COUNTS.items()):
        issues.append("Q0 trial sizes/order differ")

    gates = result.get("cryptographic_eligibility", {})
    for field, expected in (
        ("median_small_mechanical_seconds_lte", 60),
        ("max_small_mechanical_seconds_lte", 120),
        ("large_mechanical_seconds_lte", 120),
        ("manual_metadata_edits", 0),
    ):
        if gates.get(field) != expected:
            issues.append(f"historical numeric hard gate {field} changed")
    frozen_volume = inventory.get("frozen_inventory", {})
    for field, expected in EXPECTED_VOLUME.items():
        if frozen_volume.get(field) != expected:
            issues.append(f"original frozen volume inventory changed: {field}")

    for arm, source_hash, expectation in (
        ("B01", APPROVED_CONTRACT_SHA256, "ACCEPTED"),
        ("B02", APPROVED_POLICY_SHA256, "ACCEPTED"),
    ):
        decision = approval.get("decisions", {}).get(arm, {})
        if decision.get("status") != expectation or decision.get("source_sha256") != source_hash:
            issues.append(f"{arm}: expected human approval or exact source hash missing")
    if approval.get("human_reply_exact") != "ACCEPT_B01 and ACCEPT_B02":
        issues.append("human approval statement is not the recorded exact reply")
    if trace.get("approved_sha256") != {
        "contract": APPROVED_CONTRACT_SHA256, "policy": APPROVED_POLICY_SHA256
    }:
        issues.append("trace source hashes differ from owner-approved hashes")
    lifecycle = approval.get("lifecycle", {})
    for forbidden in (
        "successor_fixture_frozen",
        "successor_implementation_qualified",
        "attempt_002_claimed",
        "owner_execution_authorized",
        "physical_target_selected",
    ):
        if lifecycle.get(forbidden) is not False:
            issues.append(f"receipt improperly claims {forbidden}")
    return issues


def check_repository(root: Path = ROOT) -> list[str]:
    """Verify source-byte identities and trace semantics in a read-only pass."""

    if sha256(b"abc") != "ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad":
        return ["SHA256 known-answer self-test failed"]
    trace = read_json(root, TRACE_PATH)
    approval = read_json(root, RECEIPT_PATH)
    fixture = read_json(root, OLD_FIXTURE)
    result = read_json(root, OLD_RESULT)
    inventory = read_json(root, OLD_INVENTORY)
    issues = validate_documents(trace, fixture, result, inventory, approval)

    old_hashes = trace.get("historical_artifacts", {})
    expected_paths = {
        OLD_FIXTURE,
        OLD_RESULT,
        OLD_INVENTORY,
        "experiments/r0_p01_owner_acceptance_v01/harness.py",
        "experiments/r0_p01_owner_acceptance_v01/score.py",
        "experiments/r0_p01_owner_acceptance_v01/webauthn_server.mjs",
        "experiments/r0_p01_owner_acceptance_v01/implementation_contract_addendum_v02.md",
    }
    if set(old_hashes) != expected_paths:
        issues.append("historical baseline artifact set differs")
    for path, expected_hash in old_hashes.items():
        actual = sha256(clause_inventory.blob(root, path))
        if actual != expected_hash:
            issues.append(f"historical baseline byte mismatch: {path}")

    for arm in ("B01", "B02"):
        record = approval["decisions"][arm]
        path = record["source"]
        actual = sha256(clause_inventory.blob(root, path))
        if actual != record["source_sha256"]:
            issues.append(f"{arm}: accepted prospective source bytes changed")
    issues += clause_guard.validate_clause_index(trace, clause_inventory.source_units(root))
    return issues


def main() -> int:
    """Return nonzero on any reproducibility or governance mismatch."""

    issues = check_repository()
    if issues:
        for problem in issues:
            print(f"R0_P01_Q0_FAIL: {problem}")
        return 1
    print(
        "R0_P01_Q0_TRACE_GUARD=PASS "
        "requirements=53 controls=13 clauses=351 catalogued_tests=105 "
        "approved_sources=2 historical_artifacts=7"
    )
    print("QUALIFICATION_SCOPE=STATIC_TRACEABILITY_ONLY_NOT_OWNER_EXECUTION")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
