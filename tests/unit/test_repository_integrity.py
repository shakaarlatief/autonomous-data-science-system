from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SCRIPT_PATH = ROOT / "scripts" / "repository_integrity.py"
SPEC = importlib.util.spec_from_file_location("repository_integrity_test", SCRIPT_PATH)
assert SPEC is not None and SPEC.loader is not None
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def governed_doc(family: str, number: int, *, scope: bool = True) -> str:
    scope_line = "**Scope:** bounded test scope\n" if scope else ""
    return (
        f"# {family} {number:03d}: Test artifact\n\n"
        "**Date:** 2026-09-01  \n"
        "**Status:** TEST  \n"
        f"{scope_line}\n"
        "## Body\n"
    )


def test_same_family_duplicate_rejected_but_cross_family_same_number_allowed(tmp_path: Path) -> None:
    write(tmp_path / "docs/research/106_alpha.md", governed_doc("Research", 106))
    write(tmp_path / "docs/research/106_beta.md", governed_doc("Research", 106))
    write(
        tmp_path / "docs/specifications/106_other_family.md",
        governed_doc("Specification", 106),
    )

    errors = MODULE.validate_numbered_documents(tmp_path)

    assert any("duplicate family identity" in error for error in errors)
    assert not any("Specification 106: duplicate" in error for error in errors)


def test_post_cutover_metadata_is_strict_and_legacy_is_compatible(tmp_path: Path) -> None:
    write(
        tmp_path / "docs/research/105_legacy.md",
        "# Research 105: Legacy\n\n## Body\n",
    )
    write(
        tmp_path / "docs/research/106_missing_scope.md",
        governed_doc("Research", 106, scope=False),
    )

    errors = MODULE.validate_numbered_documents(tmp_path)

    assert not any("105_legacy" in error for error in errors)
    assert any("106_missing_scope" in error and "Scope" in error for error in errors)


def test_explicit_h1_identity_agreement_is_enforced_only_when_declared(tmp_path: Path) -> None:
    write(
        tmp_path / "docs/research/106_match.md",
        governed_doc("Research", 106),
    )
    write(
        tmp_path / "docs/research/107_mismatch.md",
        governed_doc("Research", 106),
    )
    write(
        tmp_path / "docs/research/108_descriptive_title.md",
        "# Descriptive title without governed numeric identity\n\n"
        "**Date:** 2026-09-01  \n**Status:** TEST  \n**Scope:** test\n",
    )

    errors = MODULE.validate_numbered_documents(tmp_path)

    assert not any("106_match" in error and "identity" in error for error in errors)
    assert any("107_mismatch" in error and "identity" in error for error in errors)
    assert not any("108_descriptive_title" in error and "identity" in error for error in errors)


def create_frozen_legacy_validation_paths(tmp_path: Path) -> Path:
    snapshot_path = ROOT / MODULE.VALIDATION_LEGACY_SNAPSHOT
    data = json.loads(snapshot_path.read_text(encoding="utf-8"))
    for relative in data["legacy_paths"]:
        write(tmp_path / relative, "# Legacy validation\n")
    return snapshot_path


def test_validation_evidence_legacy_snapshot_and_prospective_alternatives(tmp_path: Path) -> None:
    snapshot_path = create_frozen_legacy_validation_paths(tmp_path)
    new_path = tmp_path / "docs/example/validation/001_new_result.md"
    write(
        new_path,
        "# New validation\n\n"
        "**Date:** 2026-09-01  \n"
        "**Classification:** TEST_PASS  \n"
        "**Scope:** prospective test\n",
    )

    errors = MODULE.validate_validation_evidence(tmp_path, snapshot_path)
    assert errors == []

    write(new_path, "# New validation\n\n**Date:** 2026-09-01\n")
    errors = MODULE.validate_validation_evidence(tmp_path, snapshot_path)
    assert any("Status or Classification" in error for error in errors)
    assert any("Research, Specification, or Scope" in error for error in errors)


def test_validation_legacy_snapshot_rejects_mutated_path_set(tmp_path: Path) -> None:
    source = json.loads((ROOT / MODULE.VALIDATION_LEGACY_SNAPSHOT).read_text(encoding="utf-8"))
    source["legacy_paths"][0] = "docs/validation/changed.md"
    source["legacy_paths"] = sorted(source["legacy_paths"])
    snapshot = tmp_path / "changed_snapshot.json"
    snapshot.write_text(json.dumps(source), encoding="utf-8")

    try:
        MODULE.load_validation_legacy_snapshot(tmp_path, snapshot)
    except MODULE.IntegrityConfigurationError as exc:
        assert "path set changed" in str(exc)
    else:
        raise AssertionError("mutated immutable snapshot was accepted")


def test_typed_declared_references_validate_family_targets_and_safe_paths(tmp_path: Path) -> None:
    write(tmp_path / "docs/research/106_target.md", governed_doc("Research", 106))
    write(tmp_path / "docs/CONTINUITY.md", "# Continuity\n")
    documents = MODULE.collect_numbered_documents(tmp_path)

    assert MODULE.validate_reference_token(tmp_path, "research:106", documents) is None
    assert MODULE.validate_reference_token(tmp_path, "path:docs/CONTINUITY.md", documents) is None
    assert "missing" in MODULE.validate_reference_token(tmp_path, "research:107", documents)
    assert "malformed" in MODULE.validate_reference_token(tmp_path, "research:0", documents)
    assert "unsafe" in MODULE.validate_reference_token(tmp_path, "path:../outside.md", documents)
    assert "unsafe" in MODULE.validate_reference_token(tmp_path, "path:C:/outside.md", documents)
    assert "malformed" in MODULE.validate_reference_token(tmp_path, "unknown:106", documents)


def test_declared_references_accept_bounded_whitespace_but_reject_unquoted_text() -> None:
    tokens, error = MODULE.parse_declared_reference_field(
        "`research:106`,   `path:docs/CONTINUITY.md`"
    )
    assert error is None
    assert tokens == ["research:106", "path:docs/CONTINUITY.md"]

    _, error = MODULE.parse_declared_reference_field("research:106")
    assert error is not None


def test_existing_explicit_relationship_fields_validate_only_resolvable_full_values(tmp_path: Path) -> None:
    write(
        tmp_path / "docs/specifications/007_target.md",
        "# Specification 007: Target\n",
    )
    write(
        tmp_path / "docs/specifications/008_valid.md",
        "# Specification 008: Valid\n\n"
        "**Promoted from:** `docs/specifications/007_target.md`\n",
    )
    write(
        tmp_path / "docs/research/105_target.md",
        "# Research 105: Target\n",
    )
    write(
        tmp_path / "docs/local_execution/validation/011_relationship.md",
        "# Validation\n\n"
        "**Research:** `docs/research/105_target.md`\n",
    )
    write(
        tmp_path / "docs/research/104_thread.md",
        "# Research 104: Thread\n\n**Companion thread:** MC-0004\n",
    )
    (tmp_path / "docs/model_collaboration/threads/MC-0004").mkdir(parents=True)

    assert MODULE.validate_declared_relationships(tmp_path) == []

    write(
        tmp_path / "docs/specifications/009_missing.md",
        "# Specification 009: Missing\n\n"
        "**Promoted from:** `docs/specifications/999_missing.md`\n",
    )
    errors = MODULE.validate_declared_relationships(tmp_path)
    assert any("999_missing.md" in error for error in errors)


def test_mixed_narrative_relationship_value_is_not_heuristically_mined(tmp_path: Path) -> None:
    write(
        tmp_path / "docs/research/104_narrative.md",
        "# Research 104: Narrative\n\n"
        "**Governed by:** Research 999 after a later review and promotion decision\n",
    )

    assert MODULE.validate_declared_relationships(tmp_path) == []
