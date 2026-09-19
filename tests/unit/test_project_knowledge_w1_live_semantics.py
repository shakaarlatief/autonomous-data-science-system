from __future__ import annotations

from pathlib import Path

from tools.project_knowledge.adapters.gitio import worktree_snapshot
from tools.project_knowledge.model import AuthorityClass, LifecycleState, Profile, SemanticId
from tools.project_knowledge.services.semantic_validation import validate_project_knowledge


ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / "docs/project_knowledge/selected_architecture_workstream.md"


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
