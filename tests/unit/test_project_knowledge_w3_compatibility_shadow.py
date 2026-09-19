from __future__ import annotations

from dataclasses import replace
import json
from pathlib import Path

from tools.project_knowledge.adapters.gitio import commit_snapshot
from tools.project_knowledge.services.compatibility import (
    ARTIFACT_INVENTORY_PATH,
    BLOCKING_CLASSES,
    COMPARISON_REPORT_PATH,
    CURRENT_STATE_PATH,
    KNOWLEDGE_MAP_PATH,
    ROUTING_PATH,
    CompatibilityArtifact,
    DifferenceClass,
    build_compatibility_shadow,
    build_shadow_candidates,
    compare_shadow_to_live,
    materialize_compatibility_shadow,
)


ROOT = Path(__file__).resolve().parents[2]


def _snapshot():
    return commit_snapshot(ROOT, "HEAD")


def test_w3_candidate_generation_does_not_read_live_compatibility_content(monkeypatch) -> None:
    import tools.project_knowledge.services.compatibility as module

    def forbidden(*args, **kwargs):
        raise AssertionError("live compatibility content entered candidate generation")

    monkeypatch.setattr(module, "_read_committed_paths", forbidden)
    source_commit, source_boundary, sources, model, inventory, artifacts = build_shadow_candidates(
        _snapshot()
    )

    assert source_commit
    assert source_boundary.startswith("sha256:")
    assert len(sources) == 10
    assert model["routing"]["current_checkpoint"] == 552
    assert inventory["artifact_count"] > 1000
    assert {item.role for item in artifacts} == {
        "routing",
        "current_state",
        "knowledge_map",
        "artifact_inventory",
    }


def test_w3_routing_candidate_reproduces_exact_live_compatibility_contract() -> None:
    shadow = build_compatibility_shadow(_snapshot())
    candidate = json.loads(shadow.artifact("routing").content)
    live = json.loads((ROOT / "docs/current_routing.json").read_text(encoding="utf-8"))

    assert candidate == live
    assert shadow.artifact("routing").path == ROUTING_PATH


def test_w3_current_state_candidate_is_compact_and_owner_oriented() -> None:
    shadow = build_compatibility_shadow(_snapshot())
    text = shadow.artifact("current_state").content.decode("utf-8")

    assert len(text.encode("utf-8")) < 10_000
    assert "WS-PKA-CURRENT" in text
    assert "WS-COCKPIT-DESIGN" in text
    assert "WS-SOURCE-VAULT-BOOTSTRAP" in text
    assert "SPECIFICATION:028" in text
    assert "EXPERIMENT:192" in text
    assert "AUTHORITY_SWITCH_ALLOWED=false" in text
    assert "Checkpoint 551 accepts" not in text
    assert shadow.artifact("current_state").path == CURRENT_STATE_PATH


def test_w3_knowledge_map_preserves_legacy_reachability_via_artifact_inventory() -> None:
    shadow = build_compatibility_shadow(_snapshot())
    inventory = json.loads(shadow.artifact("artifact_inventory").content)
    paths = {item["path"] for item in inventory["artifacts"]}
    map_candidate = shadow.artifact("knowledge_map").content.decode("utf-8")

    assert shadow.artifact("artifact_inventory").path == ARTIFACT_INVENTORY_PATH
    assert shadow.artifact("knowledge_map").path == KNOWLEDGE_MAP_PATH
    assert not any(
        path.startswith("docs/project_knowledge/generated/")
        for path in paths
    )
    assert "Semantic subjects are multi-axis and non-exclusive." in map_candidate
    assert "artifact inventory" in map_candidate.lower()

    legacy = (ROOT / "docs/KNOWLEDGE_MAP.md").read_text(encoding="utf-8")
    references = set()
    for raw in legacy.splitlines():
        line = raw.strip().replace(chr(96), "")
        if line.startswith("docs/"):
            references.add(line.split()[0])

    for reference in references:
        if reference.endswith("/"):
            assert any(path.startswith(reference) for path in paths), reference
        else:
            assert reference in paths, reference


def test_w3_difference_report_uses_only_frozen_classes_and_has_no_blockers() -> None:
    shadow = build_compatibility_shadow(_snapshot())
    report = json.loads(shadow.artifact("comparison_report").content)
    classifications = {
        DifferenceClass(item["classification"])
        for item in report["differences"]
    }

    assert shadow.artifact("comparison_report").path == COMPARISON_REPORT_PATH
    assert report["source_boundary"] == shadow.source_boundary
    assert shadow.source_commit.encode("ascii") not in shadow.artifact("comparison_report").content
    assert shadow.source_commit.encode("ascii") not in shadow.artifact("artifact_inventory").content
    assert report["blocking"] is False
    assert shadow.blocking is False
    assert classifications <= set(DifferenceClass)
    assert not (classifications & BLOCKING_CLASSES)
    assert DifferenceClass.EQUIVALENT_REPRESENTATION in classifications
    assert DifferenceClass.EXPECTED_SEMANTIC_IMPROVEMENT in classifications
    assert DifferenceClass.LEGACY_DRIFT in classifications


def test_w3_routing_mismatch_is_a_blocking_migration_gap() -> None:
    source_commit, source_boundary, sources, model, inventory, artifacts = build_shadow_candidates(
        _snapshot()
    )
    altered = []
    for artifact in artifacts:
        if artifact.role != "routing":
            altered.append(artifact)
            continue
        value = json.loads(artifact.content)
        value["current_checkpoint"] += 1
        altered.append(
            CompatibilityArtifact(
                artifact.role,
                artifact.path,
                (json.dumps(value, sort_keys=True, indent=2) + "\n").encode("utf-8"),
            )
        )

    differences = compare_shadow_to_live(
        _snapshot(),
        model,
        inventory,
        tuple(altered),
    )
    routing = next(
        item for item in differences
        if item.difference_id == "routing.semantic-parity"
    )
    assert routing.classification == DifferenceClass.MIGRATION_GAP
    assert routing.blocking is True


def test_w3_build_is_byte_deterministic_and_materialization_stays_shadow_only(tmp_path: Path) -> None:
    first = build_compatibility_shadow(_snapshot())
    second = build_compatibility_shadow(_snapshot())

    assert tuple(
        (item.role, item.path, item.content)
        for item in first.artifacts
    ) == tuple(
        (item.role, item.path, item.content)
        for item in second.artifacts
    )

    materialize_compatibility_shadow(tmp_path, first)
    for artifact in first.artifacts:
        assert (tmp_path / artifact.path).read_bytes() == artifact.content

    assert not (tmp_path / "docs/current_routing.json").exists()
    assert not (tmp_path / "docs/CURRENT_STATE.md").exists()
    assert not (tmp_path / "docs/KNOWLEDGE_MAP.md").exists()
