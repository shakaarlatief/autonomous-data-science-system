"""Fault-injection unit tests for the non-executing R0-P01 Q0 trace guard.

These tests do not load the owner harness, start the WebAuthn server, generate
credentials, read owner evidence or obtain actual owner proofs. Each negative
case modifies an isolated in-memory copy of a public/synthetic reference
document to ensure the guard detects a prohibited contract drift.
"""

from __future__ import annotations

import copy
from pathlib import Path

import pytest

from scripts.check_r0_p01_successor_trace import (
    OLD_FIXTURE,
    OLD_INVENTORY,
    OLD_RESULT,
    RECEIPT_PATH,
    ROOT,
    TRACE_PATH,
    check_repository,
    read_json,
    validate_documents,
)


@pytest.fixture
def public_documents() -> dict[str, dict]:
    """Load immutable input documents into private test-owned Python objects."""

    return {
        "trace": read_json(ROOT, TRACE_PATH),
        "fixture": read_json(ROOT, OLD_FIXTURE),
        "result": read_json(ROOT, OLD_RESULT),
        "inventory": read_json(ROOT, OLD_INVENTORY),
        "approval": read_json(ROOT, RECEIPT_PATH),
    }


def defects(documents: dict[str, dict]) -> list[str]:
    """Validate only mutable test copies, never mutate repository documents."""

    d = copy.deepcopy(documents)
    return validate_documents(
        d["trace"], d["fixture"], d["result"], d["inventory"], d["approval"]
    )


def test_checked_in_trace_is_consistent_and_has_no_owner_execution() -> None:
    assert check_repository() == []


def test_remove_frozen_control_is_detected(public_documents: dict) -> None:
    d = copy.deepcopy(public_documents)
    d["trace"]["security_controls"].pop(4)
    assert "thirteen frozen security controls differ" in defects(d)


def test_rename_required_source_trace_id_is_detected(public_documents: dict) -> None:
    d = copy.deepcopy(public_documents)
    d["trace"]["requirements"][0]["id"] = "C99"
    assert "missing, extra, or renamed traceability requirement IDs" in defects(d)


def test_missing_synthetic_test_coverage_is_detected(public_documents: dict) -> None:
    d = copy.deepcopy(public_documents)
    d["trace"]["requirements"][0]["synthetic_test_ids"] = []
    assert any("missing list synthetic_test_ids" in e for e in defects(d))


def test_frozen_small_timing_gate_drift_is_detected(public_documents: dict) -> None:
    d = copy.deepcopy(public_documents)
    d["result"]["cryptographic_eligibility"][
        "median_small_mechanical_seconds_lte"
    ] = 70
    assert any("median_small_mechanical_seconds_lte" in e for e in defects(d))


def test_frozen_volume_source_drift_is_detected(public_documents: dict) -> None:
    d = copy.deepcopy(public_documents)
    d["inventory"]["frozen_inventory"]["projected_acceptance_count"] = 96
    assert "original frozen volume inventory changed: projected_acceptance_count" in defects(d)


def test_missing_human_b02_approval_is_detected(public_documents: dict) -> None:
    d = copy.deepcopy(public_documents)
    d["approval"]["decisions"]["B02"]["status"] = "PENDING"
    assert any("B02: expected human approval" in e for e in defects(d))


def test_fake_owner_execution_authorization_is_detected(public_documents: dict) -> None:
    d = copy.deepcopy(public_documents)
    d["approval"]["lifecycle"]["owner_execution_authorized"] = True
    assert "receipt improperly claims owner_execution_authorized" in defects(d)


def test_trace_cannot_claim_qualified_future_implementation(
    public_documents: dict,
) -> None:
    d = copy.deepcopy(public_documents)
    d["trace"]["requirements"][5]["status"] = "PASS"
    assert any("premature implementation qualification" in e for e in defects(d))


def test_duplicate_json_keys_are_rejected(tmp_path: Path) -> None:
    """Duplicate status keys must not allow silently changing authority."""

    (tmp_path / "malformed.json").write_text(
        '{"status":"UNFROZEN","status":"FROZEN"}', encoding="utf-8"
    )
    with pytest.raises(ValueError, match="duplicate JSON key"):
        read_json(tmp_path, "malformed.json")


def test_clause_inventory_detects_omitted_normative_unit(public_documents: dict) -> None:
    """Dropping a source paragraph must fail, even if the row list is unchanged."""

    from scripts.r0_p01_clause_guard import validate_clause_index
    from scripts.r0_p01_clause_inventory import source_units

    d = copy.deepcopy(public_documents["trace"])
    d["normative_clause_index"].pop(5)
    errors = validate_clause_index(d, source_units(ROOT))
    assert any("clause index missing" in error for error in errors)


def test_clause_inventory_detects_changed_approved_unit(public_documents: dict) -> None:
    """Unit-level hashes bind mappings to immutable approved text and JSON."""

    from scripts.r0_p01_clause_guard import validate_clause_index
    from scripts.r0_p01_clause_inventory import source_units

    d = copy.deepcopy(public_documents["trace"])
    d["normative_clause_index"][0]["source_sha256"] = "0" * 64
    errors = validate_clause_index(d, source_units(ROOT))
    assert any("changed normative source clause" in error for error in errors)


def test_clause_inventory_detects_orphan_requirement(public_documents: dict) -> None:
    from scripts.r0_p01_clause_guard import validate_clause_index
    from scripts.r0_p01_clause_inventory import source_units

    d = copy.deepcopy(public_documents["trace"])
    for clause in d["normative_clause_index"]:
        clause["requirement_ids"] = [
            x for x in clause["requirement_ids"] if x != "R40"
        ]
    assert any(
        "orphan requirement" in error
        for error in validate_clause_index(d, source_units(ROOT))
    )


def test_test_catalogue_detects_orphan_test(public_documents: dict) -> None:
    from scripts.r0_p01_clause_guard import validate_clause_index
    from scripts.r0_p01_clause_inventory import source_units

    d = copy.deepcopy(public_documents["trace"])
    d["test_catalogue"].pop()
    assert any(
        "catalogue and requirements" in error
        for error in validate_clause_index(d, source_units(ROOT))
    )


def test_hard_control_key_position_is_checked(public_documents: dict) -> None:
    from scripts.r0_p01_clause_guard import validate_clause_index
    from scripts.r0_p01_clause_inventory import source_units

    d = copy.deepcopy(public_documents["trace"])
    d["security_control_key_bindings"]["C07"] = "VALID_ACCEPTANCE"
    assert any(
        "positional control key" in error
        for error in validate_clause_index(d, source_units(ROOT))
    )


def test_source_hash_uses_committed_blob_not_checkout_line_endings() -> None:
    """Source identity remains the same under Windows working-tree CRLF."""

    from scripts.r0_p01_clause_inventory import CONTRACT, blob, h

    committed = blob(ROOT, CONTRACT)
    assert h(committed.decode("utf-8")) == (
        "9160a30c481c1c67c2ec857238f5a04b44f618b2ef589ef4f1c514eb3b3d6175"
    )
    assert b"\r\n" not in committed
    transformed_checkout = committed.replace(b"\n", b"\r\n")
    assert h(transformed_checkout.decode("utf-8")) != h(committed.decode("utf-8"))


def test_provisional_freezes_and_arm_b_p5_dependency_are_guarded(
    public_documents: dict,
) -> None:
    from scripts.r0_p01_clause_guard import validate_clause_index
    from scripts.r0_p01_clause_inventory import source_units

    d = copy.deepcopy(public_documents["trace"])
    d["freeze_boundaries"]["F2"]["status"] = "FROZEN"
    d["B_arm_P5_rotation_dependency"]["if_absent"] = "PASS"
    errors = validate_clause_index(d, source_units(ROOT))
    assert any("prematurely frozen" in error for error in errors)
    assert any("P5 missing-key dependency" in error for error in errors)
