"""Invented-only common lexical substrate implementation and negative controls."""
from __future__ import annotations

from hashlib import sha256
import sqlite3

import pytest

from experiments.r0_p03_navigation_probe import (
    neutral_readonly_retrieval_candidate as neutral,
    source_world_coverage_gate as world,
)


def fabricated() -> tuple[dict, dict[str, bytes]]:
    samples = {
        "README.md": b"Fictional project orientation and neutral definitions\n",
        "docs/checkpoints/001_fiction.md": (
            b"Fictional historical checkpoint evidence for recovery.\n"
        ),
        "src/ads_system/synthetic.py": (
            b"# Fictional source implementation of a recovery helper\n"
        ),
        "docs/research/002_unsupported.png": b"\x89PNG",
    }
    records = []
    bodies = {}
    for path, raw in samples.items():
        unsupported = path.endswith(".png")
        records.append({
            "path": path, "git_blob_oid": world.sha1git(raw),
            "sha256": sha256(raw).hexdigest() if not unsupported else None,
            "bytes": len(raw) if not unsupported else None,
            "family_hint": world.family(path),
            "visibility": world.MODALITY_HOLD if unsupported
                else "PRELIMINARY_CANDIDATE_UNQUALIFIED",
            "status": world.NO_ADMISSION,
            "flags": [],
        })
        if not unsupported:
            bodies[path] = raw
    records.sort(key=lambda r: r["path"])
    return {
        "source_ref": "a" * 40,
        "roster_sha256": world._fingerprint(records),
        "source_count": len(records),
        "source_records": records,
    }, bodies


def test_fictional_query_contains_provenance_not_authority():
    ledger, bodies = fabricated()
    index = neutral.NeutralReadOnlyIndex(ledger, bodies)
    try:
        hits = index.search("fictional recovery", limit=3)
        assert len(hits) == 2
        assert all(hit["git_commit"] == "a" * 40 for hit in hits)
        assert all(hit["source_admission"] == "NO_AUTHOR_RELEASE" for hit in hits)
        assert all(hit["authority_status"] == neutral.UNKNOWN for hit in hits)
        assert all("accepted_effect" not in hit for hit in hits)
        assert all("gold" not in hit for hit in hits)
    finally:
        index.close()


def test_fictional_derived_orientation_is_common_and_non_authoritative():
    ledger, bodies = fabricated()
    index = neutral.NeutralReadOnlyIndex(ledger, bodies)
    try:
        orientation = index.orientation()
        assert orientation["derived_non_authoritative_label"] is True
        assert orientation["source_admission"] == "NO_AUTHOR_RELEASE"
        assert orientation["current_governing_summary"] == neutral.UNKNOWN
        assert orientation["staleness_visible"] == "HISTORICAL_PIN_NOT_LIVE_CURRENTNESS"
        assert orientation["navigation_entry_points"] == []
        assert set(orientation["shared_capabilities"]) == set(neutral.SHARED_CAPABILITIES)
        assert all(
            v == "SEMANTIC_GROUND_TRUTH_NOT_QUALIFIED"
            for k, v in orientation["shared_capabilities"].items()
            if k in neutral.UNQUALIFIED_CONCEPTS
        )
        assert orientation["readable_source_count"] == 3
        assert orientation["unsupported_source_count"] == 1
        record = index.carrier_identity("src/ads_system/synthetic.py")
        assert record is not None
        assert record["information_role"] == neutral.UNKNOWN
        assert record["natural_owner"] == neutral.UNKNOWN
        assert record["authority_currentness_basis"] == neutral.UNKNOWN
        assert record["source_admission"] == "NO_AUTHOR_RELEASE"
        assert index.carrier_identity("docs/research/002_unsupported.png") is None
    finally:
        index.close()


def test_equivalent_common_views_after_ephemeral_index_deletion_and_rebuild():
    ledger, bodies = fabricated()
    first = neutral.NeutralReadOnlyIndex(ledger, bodies)
    original = first.orientation()
    hits = first.search("fictional recovery")
    first.close()
    second = neutral.NeutralReadOnlyIndex(
        ledger, dict(reversed(list(bodies.items())))
    )
    try:
        assert original == second.orientation()
        assert hits == second.search("fictional recovery")
    finally:
        second.close()


def test_queries_are_tokenized_not_executed_as_sql_or_fts_operators():
    ledger, bodies = fabricated()
    index = neutral.NeutralReadOnlyIndex(ledger, bodies)
    try:
        assert index.search("fictional") != []
        assert index.search('fictional" OR src') == []
        assert index.search("fictional OR recovery") == []
        with pytest.raises(ValueError, match="Invalid lexical query"):
            index.search("!!!")
        with pytest.raises(ValueError, match="Invalid retrieval limit"):
            index.search("fictional", limit=0)
        with pytest.raises(ValueError, match="Invalid retrieval limit"):
            index.search("fictional", limit=True)
        with pytest.raises(ValueError, match="Lexical query length"):
            index.search("a" * 300)
    finally:
        index.close()


def test_index_is_query_only_after_construction():
    ledger, bodies = fabricated()
    index = neutral.NeutralReadOnlyIndex(ledger, bodies)
    try:
        with pytest.raises(sqlite3.OperationalError):
            index._conn.execute(
                "INSERT INTO carriers(path,git_blob_oid,sha256,bytes) VALUES(?,?,?,?)",
                ("invented.md", "a" * 40, "0" * 64, 1),
            )
    finally:
        index.close()


def test_forged_source_admission_rejected_before_index_build():
    ledger, bodies = fabricated()
    record = ledger["source_records"][0]
    record["status"] = "ADMITTED"
    ledger["roster_sha256"] = world._fingerprint(ledger["source_records"])
    with pytest.raises(ValueError, match="promotion"):
        neutral.NeutralReadOnlyIndex(ledger, bodies)


def test_missing_changed_and_unpinned_source_body_rejected():
    ledger, bodies = fabricated()
    del bodies["README.md"]
    with pytest.raises(ValueError, match="roster"):
        neutral.NeutralReadOnlyIndex(ledger, bodies)
    ledger, bodies = fabricated()
    bodies["README.md"] = b"Fictional changed document"
    with pytest.raises(ValueError, match="Unpinned"):
        neutral.NeutralReadOnlyIndex(ledger, bodies)
    ledger, bodies = fabricated()
    ledger["source_ref"] = "invalid"
    with pytest.raises(ValueError, match="ledger"):
        neutral.NeutralReadOnlyIndex(ledger, bodies)


def test_historical_binary_representation_cannot_be_silently_promoted():
    ledger, bodies = fabricated()
    media = next(r for r in ledger["source_records"]
                 if r["visibility"] == world.MODALITY_HOLD)
    bodies[media["path"]] = b"FAKE IMAGE TEXT"
    with pytest.raises(ValueError, match="roster"):
        neutral.NeutralReadOnlyIndex(ledger, bodies)


def test_no_hidden_task_or_arm_scoring_mechanics_in_candidate():
    ledger, bodies = fabricated()
    index = neutral.NeutralReadOnlyIndex(ledger, bodies)
    try:
        orientation = index.orientation()
        assert orientation["experiment_role"] == "UNSCORED_COMMON_SUBSTRATE_ENGINEERING_ONLY"
        assert orientation["scored_tasks"] == "NONE"
        assert orientation["authority_replacement"] == "NONE"
        assert "topical_memberships" not in str(orientation)
        assert "semantic_similarity_rankings" not in str(orientation)
        assert "preferred_subject" not in str(orientation)
    finally:
        index.close()
