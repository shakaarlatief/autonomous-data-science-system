"""Task-independent original-source corpus candidate invariants.

All synthetic source texts, paths and links in these tests are invented.
The actual pinned 80-source corpus is separately materialized and byte-
recomputed from real Git objects, not from this simulated case population.
"""
from __future__ import annotations

from collections import Counter
from copy import deepcopy
from hashlib import sha256

import pytest

from experiments.r0_p03_navigation_probe import (
    minimum_experiment_corpus_candidate as candidate,
    source_world_coverage_gate as world,
)


def fixture():
    rows = []
    bodies = {}
    paths = set()
    pin = world.PIN

    def add(path, role, *, flags=(), visibility=None):
        assert path not in paths
        paths.add(path)
        raw = ("Fictional documentation for " + path + "\n").encode()
        if visibility is None:
            visibility = (
                "HISTORICAL_REVIEW_ONLY" if role in
                {"historical_status", "execution_evidence"}
                else "PRELIMINARY_CANDIDATE_UNQUALIFIED"
            )
        row = {
            "path": path, "family_hint": role,
            "git_blob_oid": world.sha1git(raw),
            "sha256": sha256(raw).hexdigest(), "bytes": len(raw),
            "visibility": visibility,
            "flags": list(flags), "status": world.NO_ADMISSION,
        }
        rows.append(row)
        bodies[path] = raw
        return row

    for path in candidate.EXACT_MANDATORY:
        add(path, world.family(path))
    origins = {
        "governing": "docs/specifications/",
        "product_source": "frontend/src/",
        "project_source": "src/ads_system/",
        "verification": "tests/unit/",
        "tooling": "tools/project_knowledge/",
        "historical_status": "docs/research/",
        "execution_evidence": "docs/local_execution/validation/",
        "source_schema": "schemas/project_knowledge/",
        "other": "docs/other/",
    }
    for role, prefix in origins.items():
        count = candidate.QUOTAS[role] + 8
        for i in range(count):
            add(f"{prefix}{i+100:03}_invented_{role}.md", role)
    rows.sort(key=lambda x: x["path"])
    lookup = {r["path"]: r for r in rows}
    status = [r["path"] for r in rows if r["family_hint"] == "historical_status"]
    validation = [r["path"] for r in rows if r["family_hint"] == "execution_evidence"]
    refs = {r["path"]: [] for r in rows}
    for i, path in enumerate(status):
        if i < 4 or i >= 8:
            for k in range(3):
                refs[path].append({
                    "status": "EXACT_RESOLVED",
                    "target": validation[(i + k) % len(validation)],
                })
    for i, path in enumerate(validation):
        refs[path] = [{
            "status": "EXACT_RESOLVED",
            "target": status[(i * 2) % len(status)],
        }]
    review = []
    for i, path in enumerate(status):
        review.append({
            "path": path,
            "prospective_evidence_signals": {
                "direct_core_mention": i < 8
            }
        })
    graph = {
        "references_by_source": refs,
        "review_candidate_records": review,
    }
    ledger = {
        "source_ref": pin, "source_records": rows, "source_count": len(rows),
        "roster_sha256": world._fingerprint(rows),
    }
    return ledger, graph, bodies


def test_representative_original_source_quota_no_auto_admission():
    ledger, graph, bodies = fixture()
    chosen, check = candidate.select(ledger, graph, bodies)
    assert len(chosen) == 80
    assert check["source_count"] == 80
    assert check["source_admissions"] == 0
    assert check["family_counts"] == candidate.QUOTAS
    assert all(r["status"] == "NOT_ADMITTED" for r in chosen)
    assert set(candidate.EXACT_MANDATORY).issubset({x["path"] for x in chosen})
    assert check["selected_literal_status_validation_citation_edges"] >= 2
    assert check["semantic_authority_closure"] == "NOT_PROVEN"
    assert check["combined_author_exposure_clearance"] == "NOT_PERFORMED"


def test_selections_are_stable_across_inventory_order():
    ledger, graph, bodies = fixture()
    chosen1, result1 = candidate.select(ledger, graph, bodies)
    ledger["source_records"].reverse()
    # The roster commitment intentionally binds record order; recompute
    # the synthetic commitment to isolate selection from source order.
    ledger["roster_sha256"] = world._fingerprint(ledger["source_records"])
    chosen2, result2 = candidate.select(ledger, graph, bodies)
    assert [r["path"] for r in chosen1] == [r["path"] for r in chosen2]
    assert result1 == result2


def test_original_manifest_records_missing_original_context_explicitly():
    ledger, graph, bodies = fixture()
    chosen, checks = candidate.select(ledger, graph, bodies)
    manifest = candidate.evidence_manifest(ledger, graph, chosen, checks, bodies)
    assert manifest["selected_source_count"] == 80
    assert manifest["task_authorship"] == "NOT_STARTED"
    assert manifest["author_world_release"] == (
        "PROHIBITED_PENDING_INDEPENDENT_ORIGINAL_SOURCE_REVIEW"
    )
    assert manifest["build_heldout_split"] == (
        "NOT_DRAWN_BEFORE_SOURCE_ACCEPTANCE"
    )
    assert len(manifest["records"]) == 80
    assert all(
        r["author_exposure_decision"] ==
        "CANDIDATE_REQUIRES_INDEPENDENT_AUTHOR_WORLD_RELEASE"
        for r in manifest["records"]
    )
    assert all(r["git_blob_oid"] == world.sha1git(bodies[r["path"]])
               for r in manifest["records"])
    assert any(r["literal_refs_outside_selected_world"]
               for r in manifest["records"])


def test_risk_flag_and_direct_old_answer_hazard_cannot_be_promoted():
    ledger, graph, bodies = fixture()
    first = next(x for x in ledger["source_records"]
                 if x["family_hint"] == "governing"
                 and x["path"] not in candidate.EXACT_MANDATORY)
    first["flags"] = ["LEGACY_W5_REFERENCE"]
    ledger["roster_sha256"] = world._fingerprint(ledger["source_records"])
    selected, _ = candidate.select(ledger, graph, bodies)
    assert first["path"] not in {x["path"] for x in selected}
    ledger, graph, bodies = fixture()
    bodies["README.md"] = b"This includes Research 217 old navigation solutions"
    with pytest.raises(ValueError, match="anchor"):
        candidate.select(ledger, graph, bodies)


def test_missing_anchor_or_malformed_source_ref_fails_closed():
    ledger, graph, bodies = fixture()
    ledger["source_records"] = [
        r for r in ledger["source_records"] if r["path"] != "docs/DECISIONS.md"
    ]
    ledger["source_count"] -= 1
    ledger["roster_sha256"] = world._fingerprint(ledger["source_records"])
    with pytest.raises(ValueError, match="anchor"):
        candidate.select(ledger, graph, bodies)
    ledger, graph, bodies = fixture()
    ledger["source_ref"] = "a" * 40
    with pytest.raises(ValueError, match="historical source revision"):
        candidate.select(ledger, graph, bodies)


def test_selected_blob_tampering_rejected_at_evidence_manifest():
    ledger, graph, bodies = fixture()
    chosen, checks = candidate.select(ledger, graph, bodies)
    forged = dict(bodies)
    forged["README.md"] = b"Another fictional source unrelated to original"
    with pytest.raises(ValueError, match="Unverified"):
        candidate.evidence_manifest(ledger, graph, chosen, checks, forged)


def test_unverified_source_family_exclusion_does_not_fake_low_capacity():
    ledger, graph, bodies = fixture()
    # Simulated explicit flags on every historical candidate cause a HOLD,
    # rather than inventing historical question/answer capacity.
    for row in ledger["source_records"]:
        if row["family_hint"] == "historical_status":
            row["flags"] = ["SOURCE_NOT_QUALIFIED"]
    ledger["roster_sha256"] = world._fingerprint(ledger["source_records"])
    with pytest.raises(ValueError, match="Insufficient"):
        candidate.select(ledger, graph, bodies)


def test_manifests_do_not_include_synthetic_gold_or_splits():
    ledger, graph, bodies = fixture()
    chosen, checks = candidate.select(ledger, graph, bodies)
    manifest = candidate.evidence_manifest(ledger, graph, chosen, checks, bodies)
    text = candidate.canonical(manifest).decode()
    assert "source_admission" not in text or checks["source_admissions"] == 0
    assert "gold_answer" not in text
    assert "build_heldout_split" in text
    assert "NOT_DRAWN_BEFORE_SOURCE_ACCEPTANCE" in text
    assert all(row["current_authority"] == "UNKNOWN_NOT_PROVEN"
               for row in manifest["records"])
