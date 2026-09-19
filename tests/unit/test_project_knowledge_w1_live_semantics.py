from __future__ import annotations

import json
from pathlib import Path

from tools.project_knowledge.adapters.gitio import worktree_snapshot
from tools.project_knowledge.model import AuthorityClass, LifecycleState, Profile, SemanticId
from tools.project_knowledge.services.semantic_validation import validate_project_knowledge


ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / "docs/project_knowledge/selected_architecture_workstream.md"
BOUNDARY_SOURCE = ROOT / "docs/project_knowledge/project_integration_boundary.md"
SOURCE_VAULT_WORKSTREAM = ROOT / "docs/source_universe/SOURCE_VAULT_BOOTSTRAP_WORKSTREAM.md"
SOURCE_VAULT_RESUME_TARGET = ROOT / "docs/source_universe/SOURCE_VAULT_REVIEWED_INGESTION.md"
SOURCE_VAULT_RUNBOOK = ROOT / "docs/source_universe/PERMANENT_VAULT_BOOTSTRAP.md"


def test_w1_selected_architecture_workstream_is_one_live_canonical_owner() -> None:
    result = validate_project_knowledge(worktree_snapshot(ROOT))

    assert result.ok
    owners = tuple(
        source
        for source in result.repository.sources
        if source.semantic_id == SemanticId("WS-PKA-CURRENT")
    )
    assert len(owners) == 1

    owner = owners[0]
    assert owner.carrier_path == "docs/project_knowledge/selected_architecture_workstream.md"
    assert owner.profile == Profile.WORKSTREAM
    assert owner.authority_class == AuthorityClass.CANONICAL
    assert owner.state == LifecycleState.ACTIVE
    assert owner.kind == "PROJECT_KNOWLEDGE_ARCHITECTURE_WORKSTREAM"

    fields = owner.declaration.fields
    assert fields["scope"] == {
        "architecture": "PKA-CANDIDATE-01",
        "program": "project-knowledge-architecture",
    }
    assert "path:docs/DECISIONS.md#D-035" in fields["provenance"]
    assert "specification:028" in fields["provenance"]


def test_g101_owner_preserves_current_operational_authority_boundary() -> None:
    text = SOURCE.read_text(encoding="utf-8")

    assert "CURRENT_OPERATIONAL_AUTHORITY=CURRENT_CONTINUITY_ARCHITECTURE" in text
    assert "AUTHORITY_SWITCH_ALLOWED=false" in text
    assert "D-035 remains the natural owner" in text


def test_g102_project_integration_boundary_is_one_natural_canonical_owner() -> None:
    result = validate_project_knowledge(worktree_snapshot(ROOT))

    assert result.ok
    owners = tuple(
        source
        for source in result.repository.sources
        if source.semantic_id == SemanticId("PROJECT-INTEGRATION-BOUNDARY")
    )
    assert len(owners) == 1

    owner = owners[0]
    assert owner.carrier_path == "docs/project_knowledge/project_integration_boundary.md"
    assert owner.profile == Profile.PROJECT_BOUNDARY
    assert owner.authority_class == AuthorityClass.CANONICAL
    assert owner.state == LifecycleState.ACTIVE
    assert owner.kind == "PROJECT_INTEGRATION_BOUNDARY"

    fields = owner.declaration.fields
    assert fields["promoted_branch"] == "v1-frontend-spike"
    assert fields["promoted_commit"] == "2480109fadeee1e480ef03b82e335aacdf9adf91"


def test_g102_boundary_matches_live_compatibility_projection_without_broad_control_claims() -> None:
    routing = json.loads((ROOT / "docs/current_routing.json").read_text(encoding="utf-8"))
    result = validate_project_knowledge(worktree_snapshot(ROOT))
    owner = next(
        source
        for source in result.repository.sources
        if source.semantic_id == SemanticId("PROJECT-INTEGRATION-BOUNDARY")
    )
    fields = owner.declaration.fields
    text = BOUNDARY_SOURCE.read_text(encoding="utf-8")

    assert fields["promoted_branch"] == routing["promoted_integration_branch"]
    assert fields["promoted_commit"] == routing["promoted_integration_sha"]
    assert "does not own the active development branch" in text
    assert "broad project-control registry" in text


def test_g103_source_vault_paused_resume_semantics_reproduce_qualified_state() -> None:
    result = validate_project_knowledge(worktree_snapshot(ROOT))

    assert result.ok
    owners = tuple(
        source
        for source in result.repository.sources
        if source.semantic_id == SemanticId("WS-SOURCE-VAULT-BOOTSTRAP")
    )
    assert len(owners) == 1

    owner = owners[0]
    assert owner.carrier_path == "docs/source_universe/SOURCE_VAULT_BOOTSTRAP_WORKSTREAM.md"
    assert owner.profile == Profile.WORKSTREAM
    assert owner.authority_class == AuthorityClass.CANONICAL
    assert owner.state == LifecycleState.PAUSED
    assert owner.kind == "SOURCE_VAULT_BOOTSTRAP_WORKSTREAM"

    fields = owner.declaration.fields
    assert fields["expected_to_resume"] is True
    assert fields["return_condition"] == (
        "Resume only when project routing explicitly returns to the Source Vault bootstrap workstream."
    )
    assert fields["resume_target"] == "SOURCE-VAULT:REVIEWED-INGESTION"
    assert fields["governing_procedure"] == "PROCEDURE:PERMANENT-SOURCE-VAULT-BOOTSTRAP"
    assert tuple(
        (item["milestone_id"], item["state"])
        for item in fields["orientation_milestones"]
    ) == (
        ("SOURCE-VAULT:INGESTION", "NOT_STARTED"),
        ("COURSE:2", "BLOCKED"),
    )


def test_g103_resume_target_and_governing_procedure_are_resolvable_natural_owners() -> None:
    result = validate_project_knowledge(worktree_snapshot(ROOT))

    by_id = {
        source.semantic_id.value: source
        for source in result.repository.sources
        if source.semantic_id is not None
    }

    resume_target = by_id["SOURCE-VAULT:REVIEWED-INGESTION"]
    assert resume_target.carrier_path == "docs/source_universe/SOURCE_VAULT_REVIEWED_INGESTION.md"
    assert resume_target.profile == Profile.SEMANTIC_SOURCE
    assert resume_target.authority_class == AuthorityClass.CANONICAL
    assert resume_target.state == LifecycleState.ACTIVE

    procedure = by_id["PROCEDURE:PERMANENT-SOURCE-VAULT-BOOTSTRAP"]
    assert procedure.carrier_path == "docs/source_universe/PERMANENT_VAULT_BOOTSTRAP.md"
    assert procedure.profile == Profile.GOVERNING_PROCEDURE
    assert procedure.authority_class == AuthorityClass.CANONICAL
    assert procedure.state == LifecycleState.ACTIVE

    fields = procedure.declaration.fields
    assert tuple(fields["governed_action_classes"]) == ("COURSE2_ADMISSION_DECISION",)
    assert tuple(item["constraint_id"] for item in fields["mandatory_constraints"]) == (
        "FIRST_CORPUS_ACCOUNTED",
        "WORKING_AUDIT_CLEAN",
        "INDEPENDENT_BACKUP_ROUND_TRIP",
        "CLEAN_RESTORE",
        "RESTORED_AUDIT_CLEAN",
        "SAFE_EVIDENCE_PRESERVED",
    )


def test_g103_source_vault_rich_source_preserves_qualified_real_state_without_private_values() -> None:
    text = SOURCE_VAULT_WORKSTREAM.read_text(encoding="utf-8")
    for expected in (
        "source registry                          MIGRATED_VERIFIED",
        "Alembic head                             0003_source_universe",
        "SQLite table count                       33",
        "first-corpus prospective compare         20 / 20 MATCH",
        "source ingestion                         NOT_STARTED",
        "working-store integrity audit            PENDING",
        "independent encrypted backup proof       PENDING",
        "clean restore + restored audit           PENDING",
        "Course 2                                 BLOCKED",
        "private dependency                       RESOLVED_PRIVATE",
        "reviewed ingestion of the frozen 20-entry first corpus",
    ):
        assert expected in text

    assert "Exact private paths" in text
    assert "credentials" in text


def test_g103_course2_action_contract_is_bounded_to_existing_runbook_gate() -> None:
    text = SOURCE_VAULT_RUNBOOK.read_text(encoding="utf-8")

    assert "bounded authoritative projection of the Course 2 admission gate" in text
    assert "does not replace the richer operational procedure" in text
    assert "## 13. Course 2 admission gate" in text
    assert "No additional educational course batch should be admitted until" in text
