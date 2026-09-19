"""W2 qualification for materialized structural shadow views."""

from __future__ import annotations

import json
from pathlib import Path

from tools.project_knowledge.adapters.gitio import commit_snapshot
from tools.project_knowledge.services.generation import generate_views
from tools.project_knowledge.views import production_view_specifications


ROOT = Path(__file__).resolve().parents[2]
GENERATED = ROOT / "docs/project_knowledge/generated"
MANIFESTS = GENERATED / "manifests"
OLD_CURRENT_CORE_ORACLE = (
    ROOT
    / "docs/research/project_knowledge_candidate_01_current_state_core_v01"
    / "CURRENT_STATE_CORE_ORACLE_V01.json"
)
OLD_Q4_DAG = (
    ROOT
    / "docs/research/project_knowledge_candidate_01_q4_real_v01"
    / "SHADOW_Q4_WORKSTREAM_DAG.json"
)

COMPATIBILITY_PATHS = {
    "docs/CURRENT_STATE.md",
    "docs/current_routing.json",
    "docs/KNOWLEDGE_MAP.md",
    "docs/CONTINUITY.md",
}

EXPECTED_SOURCE_IDS = {
    "COCKPIT:DESIGN-EXPLORATION-RESUME",
    "D-035",
    "EXPERIMENT:192",
    "PROCEDURE:PERMANENT-SOURCE-VAULT-BOOTSTRAP",
    "PROJECT-INTEGRATION-BOUNDARY",
    "SOURCE-VAULT:REVIEWED-INGESTION",
    "SPECIFICATION:028",
    "WS-COCKPIT-DESIGN",
    "WS-PKA-CURRENT",
    "WS-SOURCE-VAULT-BOOTSTRAP",
}


def _json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def _materialized_json(name: str):
    return _json(GENERATED / name)


def test_w2_materialized_structural_views_match_exact_committed_rebuild() -> None:
    specifications = production_view_specifications()
    builds = generate_views(commit_snapshot(ROOT, "HEAD"), specifications)
    by_id = {build.view_id: build for build in builds}

    assert len(specifications) == len(builds) == 8
    assert set(by_id) == {spec.view_id for spec in specifications}

    for spec in specifications:
        build = by_id[spec.view_id]
        assert (ROOT / spec.view_path).read_bytes() == build.view_bytes
        assert (ROOT / spec.manifest_path).read_bytes() == build.manifest_bytes
        assert spec.view_path.startswith("docs/project_knowledge/generated/")
        assert spec.manifest_path.startswith("docs/project_knowledge/generated/manifests/")
        assert spec.view_path not in COMPATIBILITY_PATHS
        assert spec.manifest_path not in COMPATIBILITY_PATHS


def test_w2_manifests_bind_successor_sources_not_live_compatibility_surfaces() -> None:
    manifests = tuple(sorted(MANIFESTS.glob("*.json")))
    assert len(manifests) == 8

    binding_sets = []
    for path in manifests:
        manifest = _json(path)
        bindings = {
            binding["source_path"]
            for binding in manifest["input_bindings"]
        }
        binding_sets.append(bindings)
        assert not (bindings & COMPATIBILITY_PATHS)
        assert all(
            not source_path.startswith("docs/project_knowledge/generated/")
            for source_path in bindings
        )

    assert all(bindings == binding_sets[0] for bindings in binding_sets)
    assert len(binding_sets[0]) == 10


def test_w2_current_state_core_matches_live_control_state_and_stable_shadow_facts() -> None:
    core = _materialized_json("current_state_core.json")
    routing = _json(ROOT / "docs/current_routing.json")
    old_oracle = _json(OLD_CURRENT_CORE_ORACLE)["expectations"]["current_state_core"]

    assert core["active_workstream"]["semantic_id"] == "WS-PKA-CURRENT"
    assert core["active_workstream"]["state"] == "ACTIVE"
    assert core["active_workstream"]["execution_anchor"] == {
        "checkpoint": routing["current_checkpoint"],
        "development_branch": routing["active_development_branch"],
        "pull_request": routing["active_pr"],
        "current_boundary": routing["current_boundary"],
    }
    assert core["active_workstream"]["stage"] == {
        "stage_id": "SPECIFICATION:028",
        "stage_state": "W1_ACCEPTED",
    }

    assert core["integration_boundary"] == {
        "semantic_id": "PROJECT-INTEGRATION-BOUNDARY",
        "promoted_branch": routing["promoted_integration_branch"],
        "promoted_commit": routing["promoted_integration_sha"],
    }
    assert core["current_specification"] == {"semantic_id": "SPECIFICATION:028"}
    assert core["current_experiment"] == {
        "semantic_id": "EXPERIMENT:192",
        "outcome": routing["latest_experiment_outcome"],
    }

    assert core["integration_boundary"]["promoted_branch"] == old_oracle[
        "promoted_integration_branch"
    ]
    assert core["integration_boundary"]["promoted_commit"] == old_oracle[
        "promoted_integration_sha"
    ]
    assert core["current_experiment"]["outcome"] == old_oracle[
        "latest_experiment_outcome"
    ]

    paused = {
        item["semantic_id"]: item
        for item in core["paused_workstreams"]
    }
    assert set(paused) == {
        "WS-COCKPIT-DESIGN",
        "WS-SOURCE-VAULT-BOOTSTRAP",
    }
    source_vault = paused["WS-SOURCE-VAULT-BOOTSTRAP"]
    assert source_vault["state"] == old_oracle["paused_workstreams"][0]["state"]
    assert source_vault["orientation_milestones"] == [
        {"milestone_id": "COURSE:2", "state": "BLOCKED"},
        {"milestone_id": "SOURCE-VAULT:INGESTION", "state": "NOT_STARTED"},
    ]


def test_w2_workstream_projection_preserves_qualified_resume_semantics() -> None:
    graph = _materialized_json("workstream_graph.json")
    old_dag = _json(OLD_Q4_DAG)
    old_by_id = {
        item["semantic_id"]: item
        for item in old_dag["workstreams"]
    }
    nodes = {
        item["semantic_id"]: item
        for item in graph["nodes"]
    }

    assert graph["active_ready_set"] == ["WS-PKA-CURRENT"]
    assert graph["route"] == {
        "branches": ["WS-PKA-CURRENT"],
        "disposition": "UNIQUE_PRIMARY_ROUTE",
        "primary": "WS-PKA-CURRENT",
    }
    assert set(nodes) == {
        "WS-COCKPIT-DESIGN",
        "WS-PKA-CURRENT",
        "WS-SOURCE-VAULT-BOOTSTRAP",
    }
    assert nodes["WS-PKA-CURRENT"]["readiness"] == "RUNNABLE"

    for semantic_id in ("WS-COCKPIT-DESIGN", "WS-SOURCE-VAULT-BOOTSTRAP"):
        assert nodes[semantic_id]["state"] == old_by_id[semantic_id]["state"] == "PAUSED"
        assert nodes[semantic_id]["expected_to_resume"] is True

    cockpit_target = (
        ROOT / "docs/cockpit/COCKPIT_DESIGN_RESUME_TARGET.md"
    ).read_text(encoding="utf-8")
    cockpit_branch, _, cockpit_head = old_by_id["WS-COCKPIT-DESIGN"][
        "resume_target"
    ].partition("@")
    assert cockpit_branch
    assert cockpit_head
    assert f"branch   {cockpit_branch}" in cockpit_target
    assert f"head     {cockpit_head}" in cockpit_target

    source_vault_target = (
        ROOT / "docs/source_universe/SOURCE_VAULT_REVIEWED_INGESTION.md"
    ).read_text(encoding="utf-8")
    assert old_by_id["WS-SOURCE-VAULT-BOOTSTRAP"]["resume_target"] in source_vault_target


def test_w2_catalog_identity_authority_subject_and_obligation_views_cover_live_slice() -> None:
    catalog = _materialized_json("source_catalog.json")
    identity = _materialized_json("identity_index.json")
    authority = _materialized_json("authority_index.json")
    subject = _materialized_json("subject_index.json")
    risk = _materialized_json("risk_obligation_index.json")

    catalog_ids = {item["semantic_id"] for item in catalog["sources"]}
    identity_ids = {item["semantic_id"] for item in identity["identities"]}
    authority_ids = {item["semantic_id"] for item in authority["candidates"]}

    assert catalog_ids == identity_ids == authority_ids == EXPECTED_SOURCE_IDS

    memberships = subject["memberships"]
    for semantic_id in EXPECTED_SOURCE_IDS:
        axes = {
            item["axis"]
            for item in memberships
            if item["semantic_id"] == semantic_id
        }
        assert {"kind", "profile"} <= axes

    mandatory = [
        item["constraint_id"]
        for item in risk["obligations"]
        if item["category"] == "MANDATORY_CONSTRAINT"
    ]
    assert mandatory == [
        "FIRST_CORPUS_ACCOUNTED",
        "WORKING_AUDIT_CLEAN",
        "INDEPENDENT_BACKUP_ROUND_TRIP",
        "CLEAN_RESTORE",
        "RESTORED_AUDIT_CLEAN",
        "SAFE_EVIDENCE_PRESERVED",
    ]
    assert {
        item["semantic_id"]
        for item in risk["obligations"]
        if item["category"] == "RETURN_CONDITION"
    } == {
        "WS-COCKPIT-DESIGN",
        "WS-SOURCE-VAULT-BOOTSTRAP",
    }
