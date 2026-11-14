"""Source-grounded documentary relation checks and non-promotion controls.

The locally ignored selection fixture is an exposed, unscored engineering
candidate. Tests establish exact Git blob/line proof and typed documentary
links, not independent owner acceptance, executed historical CI, or approved
J1/J2 realization semantics. Public test output stays source-free.
"""
from __future__ import annotations

from copy import deepcopy
from hashlib import sha256
import json
import subprocess

import pytest

from experiments.r0_p03_navigation_probe import (
    historical_semantic_evidence_chain_v01 as probe,
)


@pytest.fixture(scope="module")
def candidate() -> dict:
    return json.loads(probe.exact_sha(probe.PRIVATE_SPEC, probe.SELECTION_SHA256))


@pytest.fixture(scope="module")
def reviewed(candidate: dict) -> tuple[dict, dict]:
    return probe.build(probe.ROOT, candidate)


def test_frozen_original_line_witnesses_and_documentary_relations(reviewed: tuple) -> None:
    public, private = reviewed
    assert public["source_carrier_count"] == 10
    assert public["source_witness_count"] == 19
    assert public["documentary_relation_count"] == 11
    assert len(private["witnesses"]) == 19
    assert len(private["documentary_relations"]) == 11
    assert all(item["accepted_j2_realization"] is False for item in private["documentary_relations"])
    assert all(item["accepted_governing_effect"] is False for item in private["documentary_relations"])
    assert all(item["historical_ci_execution_independently_verified"] is False for item in private["documentary_relations"])
    assert set(public["documentary_relation_type_counts"]) == set(probe.RELATIONS)
    assert public["actual_v03_common_substrate_complete"] is False


def test_at_pinned_original_source_routing_newer_than_derived_projection(reviewed: tuple) -> None:
    public, _ = reviewed
    comparison = public["negative_original_checkpoint_comparison"]
    assert comparison["generated_checkpoint_at_original_pin"] == 564
    assert comparison["routing_checkpoint_at_original_pin"] == 895
    assert comparison["delta_checkpoints_not_time_or_semantic_staleness_proof"] == 331
    assert "NOT_OPERATIVE_AUTHORITY" in comparison["interpretation"]


def test_mutated_exact_source_quote_rejected(candidate: dict) -> None:
    bad = deepcopy(candidate)
    bad["witnesses"][0]["expected_excerpt"] += " NOT_PRESENT_IN_ORIGINAL_GIT"
    with pytest.raises(ValueError, match="Git-pinned lines"):
        probe.build(probe.ROOT, bad)


def test_unexpected_promotion_key_rejected(candidate: dict) -> None:
    bad = deepcopy(candidate)
    bad["relations"][0]["j1_acceptance"] = "ACTIVE"
    with pytest.raises(ValueError, match="authority admission"):
        probe.build(probe.ROOT, bad)


def test_unqualified_reclassification_rejected(candidate: dict) -> None:
    bad = deepcopy(candidate)
    bad["relations"][0]["status"] = "ACCEPTED_EFFECT"
    with pytest.raises(ValueError, match="authority-promoted relation"):
        probe.build(probe.ROOT, bad)


def test_invalid_relation_source_kind_mixture_rejected(candidate: dict) -> None:
    bad = deepcopy(candidate)
    row = next(r for r in bad["relations"] if r["type"] == "TEST_SOURCE_IMPORTS_IMPLEMENTATION")
    row["witness_ids"] = [
        w["id"] for w in bad["witnesses"]
        if w["kind"] in ("UNACCEPTED_PROPOSAL", "IMPLEMENTATION_SOURCE")
    ][:2]
    with pytest.raises(ValueError, match="Source-kind requirements"):
        probe.build(probe.ROOT, bad)


def test_invented_realization_edge_kind_rejected(candidate: dict) -> None:
    bad = deepcopy(candidate)
    bad["relations"][0]["type"] = "J2_REALIZES"
    with pytest.raises(ValueError, match="authority-promoted relation"):
        probe.build(probe.ROOT, bad)


def test_original_git_pin_change_rejected(candidate: dict) -> None:
    bad = deepcopy(candidate)
    bad["source_pin"] = "0" * 40
    with pytest.raises(ValueError, match="Source-world scope"):
        probe.build(probe.ROOT, bad)


@pytest.mark.parametrize(
    "path",
    ["", "../escape", "dir/../bad", "/absolute", "dir\\bad",
     "dir//double", "dir/./normalized", "a\x00b"],
)
def test_unsafe_original_git_paths_rejected(path: str) -> None:
    assert probe.safe_path(path) is False


def test_historical_commit_and_current_snapshot_code_identical(candidate: dict) -> None:
    # Compare against the specific immutable development commit where this
    # unscored probe began, never HEAD of a future moving branch.
    snapshot = "4a2fd324b2d36482a4b24fc8753252e8e0938802"
    source_paths = {
        w["path"] for w in candidate["witnesses"]
        if w["kind"] in {"TEST_SOURCE", "IMPLEMENTATION_SOURCE"}
    }
    assert len(source_paths) == 2
    for path in source_paths:
        original = subprocess.check_output(
            ["git", "rev-parse", f"{probe.ORIGINAL_PIN}:{path}"],
            cwd=probe.ROOT, timeout=12,
        ).strip()
        snapshot_oid = subprocess.check_output(
            ["git", "rev-parse", f"{snapshot}:{path}"],
            cwd=probe.ROOT, timeout=12,
        ).strip()
        assert original == snapshot_oid


def test_public_output_has_no_original_paths_or_quotes(reviewed: tuple) -> None:
    public, private = reviewed
    safe = probe.canonical(public).decode("ascii")
    assert public["independently_attested_owner_decision"] == "NOT_ESTABLISHED_BY_THIS_SOURCE_SET"
    assert public["historical_ci_execution_verified"] == "NOT_ESTABLISHED_BY_THIS_SOURCE_SET"
    assert public["accepted_j1_effect_relations"] == 0
    assert public["accepted_j2_realization_relations"] == 0
    assert public["formal_R0_P03_task_or_arm_scoring"] is False
    for original in private["witnesses"]:
        assert original["original_source_path"] not in safe
        assert original["exact_original_excerpt"] not in safe
    assert len(public["architecture_reconsideration_triggers"]) >= 6


def test_original_private_and_public_byte_replay(reviewed: tuple) -> None:
    public, private = reviewed
    raw = probe.canonical(private)
    assert probe.PRIVATE_RESULT.read_bytes() == raw
    safe = deepcopy(public)
    safe["private_result_bytes_receipt_only"] = len(raw)
    safe["private_result_sha256_receipt_only"] = sha256(raw).hexdigest()
    assert probe.PUBLIC_RESULT.read_bytes() == probe.canonical(safe)
    assert sha256(probe.PUBLIC_RESULT.read_bytes()).hexdigest() == "522c9181aa26bf939d394275cf584f5005ec53236339e57b3ba278c015e56837"
