"""Actual reproducibility and inference boundaries for a legacy retrieval pilot.

The same real 65-carrier historical Git snapshot and nine already-used W5
research scenarios are verified against a saved two-mechanism execution.
These are engineering tests only. They do not establish independent primary
task answers, true authority, provenance correctness, or B0-B4 equivalence.
"""
from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path

from experiments.r0_p03_navigation_probe.exploratory_legacy_b0_b1_live_comparison import (
    OUT,
    PILOT_ID,
    run,
)

ROOT = Path(__file__).resolve().parents[2]
REPORT_SHA256 = "498bb12d906639642da943e8366194ec8b0c7f6817d20ae5b8fa89a43f8a2acb"
PIN = "4b94ffe183ff7af72cef6ee7492b4ba2f30c11ef"


def test_actual_persisted_output_is_exactly_reproducible() -> None:
    raw = OUT.read_bytes()
    assert len(raw) == 18712
    assert sha256(raw).hexdigest() == REPORT_SHA256
    saved = json.loads(raw)
    recomputed = run()
    assert recomputed == saved
    assert raw.endswith(b"\n") and b"\r\n" not in raw
    assert saved["pilot_id"] == PILOT_ID
    assert saved["source_revision"] == PIN
    assert saved["same_historical_source_count"] == 65
    assert saved["retrieval_limit"] == 10
    assert len(saved["scenarios"]) == 9


def test_actual_measured_scoring_not_guessed() -> None:
    value = json.loads(OUT.read_text(encoding="utf-8"))
    b0, b1 = value["aggregate"]["b0_like"], value["aggregate"]["b1_like"]
    assert b0["strict_complete_scenario_passes"] == 1
    assert b1["strict_complete_scenario_passes"] == 9
    assert b0["positive_instances_found_at_10"] == 28
    assert b1["positive_instances_found_at_10"] == 39
    assert b0["total_required_positive_instances"] == 39
    assert b1["total_required_positive_instances"] == 39
    assert b0["explicit_negative_intrusions"] == 4
    assert b1["explicit_negative_intrusions"] == 0
    assert b0["returned_carriers_total"] == 90
    assert b1["returned_carriers_total"] == 51
    assert b0["micro_recall_at_10"] == 0.717949
    assert b1["micro_recall_at_10"] == 1.0


def test_scoring_is_from_frozen_legacy_paths_and_does_not_overrun_budget() -> None:
    value = json.loads(OUT.read_text(encoding="utf-8"))
    fixture = json.loads(
        (ROOT / "experiments/project_knowledge_subject_navigation_t1_v02/navigation_scenarios_v02.json").read_text(encoding="utf-8")
    )
    by_id = {x["id"]: x for x in fixture["scenarios"]}
    for row in value["scenarios"]:
        assert row["scenario"] in by_id
        assert len(row["b0_ranked_paths"]) <= 10
        assert len(row["b1_ranked_paths"]) <= 10
        assert len(row["b0_ranked_paths"]) == len(set(row["b0_ranked_paths"]))
        assert len(row["b1_ranked_paths"]) == len(set(row["b1_ranked_paths"]))
        for arm in ("b0_like", "b1_like"):
            must = set(by_id[row["scenario"]]["must_retrieve"])
            forbidden = set(by_id[row["scenario"]]["must_not_retrieve"])
            ranked = set(row["b0_ranked_paths"] if arm == "b0_like" else row["b1_ranked_paths"])
            scored = row[arm]
            assert scored["true_positive_count"] == len(ranked & must)
            assert scored["explicit_negative_intrusions"] == len(ranked & forbidden)
            assert scored["strict_pass"] == (must <= ranked and not forbidden & ranked)


def test_explicit_nonselection_and_not_original_r0_p03_classification() -> None:
    value = json.loads(OUT.read_text(encoding="utf-8"))
    assert "NOT_ORIGINAL_R0_P03_SCORED_B0_B4_EXPERIMENT" in value["not"]
    assert "NOT_BLIND_OR_INDEPENDENT_REFERENCE_GOLD" in value["not"]
    assert "NOT_B2_B3_B4_IMPLEMENTATION_OR_COMPARISON" in value["not"]
    research = (ROOT / "docs/research/642_r0_p03_execution_first_exploratory_legacy_b0_b1_results_and_protocol_boundary.md").read_text(encoding="utf-8")
    assert "ORIGINAL_R0_P03_12_PRIMARY_ADMISSIONS=0" in research
    assert "COMPLETE_B0_B4_COMPARISON=NOT_EXECUTED" in research
    assert "B1's annotations have sunk human authoring effort" in research
