"""W1 G106 qualification against the live canonical semantic owners."""

from __future__ import annotations

import json
from pathlib import Path

from tools.project_knowledge.adapters.gitio import commit_snapshot
from tools.project_knowledge.services.generation import generate_views
from tools.project_knowledge.views import (
    current_state_core_markdown_specification,
    current_state_core_specification,
    workstream_graph_specification,
)


ROOT = Path(__file__).resolve().parents[2]
SPECS = (
    workstream_graph_specification(),
    current_state_core_specification(),
    current_state_core_markdown_specification(),
)


def _builds():
    return generate_views(commit_snapshot(ROOT, "HEAD"), SPECS)


def _by_id(rows):
    return {row.view_id: row for row in rows}


def test_g106_live_w1_workstream_and_current_core_views_are_byte_deterministic() -> None:
    first = _by_id(_builds())
    second = _by_id(_builds())

    assert tuple(first) == tuple(second)
    for view_id in first:
        assert first[view_id].view_bytes == second[view_id].view_bytes
        assert first[view_id].manifest_bytes == second[view_id].manifest_bytes


def test_g106_current_state_core_is_derived_from_live_w1_canonical_owners() -> None:
    builds = _by_id(_builds())
    core = json.loads(builds["current_state_core"].view_bytes)
    routing = json.loads((ROOT / "docs/current_routing.json").read_text(encoding="utf-8"))

    active = core["active_workstream"]
    assert active["semantic_id"] == "WS-PKA-CURRENT"
    assert active["state"] == "ACTIVE"
    assert active["execution_anchor"] == {
        "checkpoint": routing["current_checkpoint"],
        "development_branch": routing["active_development_branch"],
        "pull_request": routing["active_pr"],
        "current_boundary": routing["current_boundary"],
    }
    assert active["stage"] == {
        "stage_id": "SPECIFICATION:028",
        "stage_state": "W1_IN_PROGRESS",
    }

    assert core["integration_boundary"] == {
        "semantic_id": "PROJECT-INTEGRATION-BOUNDARY",
        "promoted_branch": routing["promoted_integration_branch"],
        "promoted_commit": routing["promoted_integration_sha"],
    }
    assert core["current_specification"] == {"semantic_id": "SPECIFICATION:028"}
    assert core["current_experiment"] == {
        "semantic_id": "EXPERIMENT:192",
        "outcome": "INCOMPLETE",
    }

    paused = {item["semantic_id"]: item for item in core["paused_workstreams"]}
    assert set(paused) == {"WS-COCKPIT-DESIGN", "WS-SOURCE-VAULT-BOOTSTRAP"}
    assert paused["WS-COCKPIT-DESIGN"]["resume_target"] == "COCKPIT:DESIGN-EXPLORATION-RESUME"
    assert paused["WS-SOURCE-VAULT-BOOTSTRAP"]["resume_target"] == "SOURCE-VAULT:REVIEWED-INGESTION"
    assert paused["WS-SOURCE-VAULT-BOOTSTRAP"]["orientation_milestones"] == [
        {"milestone_id": "COURSE:2", "state": "BLOCKED"},
        {"milestone_id": "SOURCE-VAULT:INGESTION", "state": "NOT_STARTED"},
    ]

    bindings = {
        item["source_path"]
        for item in builds["current_state_core"].manifest.fields["input_bindings"]
    }
    for path in (
        "docs/project_knowledge/selected_architecture_workstream.md",
        "docs/project_knowledge/project_integration_boundary.md",
        "docs/source_universe/SOURCE_VAULT_BOOTSTRAP_WORKSTREAM.md",
        "docs/source_universe/SOURCE_VAULT_REVIEWED_INGESTION.md",
        "docs/source_universe/PERMANENT_VAULT_BOOTSTRAP.md",
        "docs/cockpit/README.md",
        "docs/cockpit/COCKPIT_DESIGN_RESUME_TARGET.md",
        "docs/DECISIONS.md",
        "docs/specifications/028_v1_project_knowledge_architecture_implementation_and_migration_contract.md",
        "docs/checkpoints/192_specification_022_incomplete_result_preservation_promotion_candidate.md",
    ):
        assert path in bindings

    for compatibility_path in (
        "docs/CURRENT_STATE.md",
        "docs/current_routing.json",
        "docs/KNOWLEDGE_MAP.md",
        "docs/CONTINUITY.md",
    ):
        assert compatibility_path not in bindings


def test_g106_workstream_graph_and_markdown_project_same_live_w1_state() -> None:
    builds = _by_id(_builds())
    graph = json.loads(builds["workstream_graph"].view_bytes)
    markdown = builds["current_state_core_markdown"].view_bytes.decode("utf-8")
    routing = json.loads((ROOT / "docs/current_routing.json").read_text(encoding="utf-8"))

    assert graph["active_ready_set"] == ["WS-PKA-CURRENT"]
    assert graph["route"] == {
        "branches": ["WS-PKA-CURRENT"],
        "disposition": "UNIQUE_PRIMARY_ROUTE",
        "primary": "WS-PKA-CURRENT",
    }

    nodes = {item["semantic_id"]: item for item in graph["nodes"]}
    assert set(nodes) == {"WS-COCKPIT-DESIGN", "WS-PKA-CURRENT", "WS-SOURCE-VAULT-BOOTSTRAP"}
    assert nodes["WS-PKA-CURRENT"]["readiness"] == "RUNNABLE"
    assert nodes["WS-COCKPIT-DESIGN"]["readiness"] == "PAUSED"
    assert nodes["WS-SOURCE-VAULT-BOOTSTRAP"]["readiness"] == "PAUSED"

    for expected in (
        "- Semantic ID: WS-PKA-CURRENT",
        "- Stage: SPECIFICATION:028",
        f"- Checkpoint: {routing['current_checkpoint']}",
        "- Specification: SPECIFICATION:028",
        "- Experiment: EXPERIMENT:192",
        "- Outcome: INCOMPLETE",
        "- WS-COCKPIT-DESIGN -> COCKPIT:DESIGN-EXPLORATION-RESUME",
        "- WS-SOURCE-VAULT-BOOTSTRAP -> SOURCE-VAULT:REVIEWED-INGESTION",
    ):
        assert expected in markdown
