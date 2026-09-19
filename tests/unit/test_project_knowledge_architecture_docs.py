"""Static qualification for Specification 028 PKA-G015 architecture documentation."""

from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
ARCH = ROOT / "docs/project_knowledge/architecture"

REQUIRED = (
    "README.md",
    "whole_architecture.md",
    "semantic_authority_model.md",
    "knowledge_lifecycle.md",
    "reconstruction_and_action.md",
    "migration_and_cutover.md",
)
MERMAID_FENCE = chr(96) * 3 + "mermaid"


def text(name):
    return (ARCH / name).read_text(encoding="utf-8")


def test_required_architecture_document_set_exists_and_is_navigable():
    assert tuple(sorted(path.name for path in ARCH.glob("*.md"))) == tuple(sorted(REQUIRED))
    readme = text("README.md")
    for name in REQUIRED[1:]:
        assert f"]({name})" in readme
    assert "logical architecture" in readme.lower()
    assert "physical implementation" in readme.lower()
    assert "AUTHORITY_SWITCH_ALLOWED=false" in readme


def test_whole_architecture_has_version_controlled_source_and_required_boundaries():
    value = text("whole_architecture.md")
    assert value.count(MERMAID_FENCE) == 1
    for marker in (
        "Canonical sources",
        "Semantic control",
        "Derived access",
        "Reconstruction and action",
        "Migration and control",
    ):
        assert marker in value
    assert "logical concepts above are not defined by these paths" in value
    assert "source_catalog.json" in value
    assert "CURRENT_STATE_CORE.md" in value


def test_semantic_authority_diagram_separates_identity_authority_and_retrieval():
    value = text("semantic_authority_model.md")
    assert value.count(MERMAID_FENCE) == 1
    assert "Identity transition graph" in value
    assert "Task-scoped authority resolver" in value
    assert "Retrieval / subject index / model nomination" in value
    assert "relevance only" in value
    assert "cannot directly create authority" in value
    assert "Identity is not authority" in value
    assert "Retrieval remains subordinate" in value


def test_lifecycle_diagram_preserves_capture_non_authority_until_promotion():
    value = text("knowledge_lifecycle.md")
    assert value.count(MERMAID_FENCE) == 1
    assert "capture.v1" in value
    assert "structurally non-authoritative" in value
    assert "cannot enter authority resolver" in value
    assert "Explicit canonical edit / promotion" in value
    assert "Canonical semantic owner" in value
    assert "W0 implements and validates a prospective" in value


def test_reconstruction_diagram_distinguishes_all_three_task_classes_and_action_gate():
    value = text("reconstruction_and_action.md")
    assert value.count(MERMAID_FENCE) == 1
    for marker in ("BROAD_CONTINUATION", "NARROW_GOVERNED_TASK", "EXPLORATORY_RESEARCH"):
        assert marker in value
    assert "Authority resolver" in value
    assert "AuthorityReceipt" in value
    assert "expected revision" in value.lower()
    assert "not all exposed by the current G014 CLI" in value


def test_migration_diagram_makes_shadow_cutover_and_rollback_explicit():
    value = text("migration_and_cutover.md")
    assert value.count(MERMAID_FENCE) == 1
    for marker in (
        "Current continuity architecture",
        "W2 shadow derived views",
        "W3 compatibility shadow",
        "W7 production qualification",
        "W8 explicit authority-switch decision",
        "Rollback candidate",
    ):
        assert marker in value
    assert "AUTHORITY_SWITCH_ALLOWED=false" in value
    assert "W1 has not started" in value


def test_no_rendered_visual_is_committed_as_independent_truth_at_g015():
    rendered = tuple(
        path for path in ARCH.iterdir()
        if path.suffix.lower() in {".svg", ".png"}
    )
    assert rendered == ()
