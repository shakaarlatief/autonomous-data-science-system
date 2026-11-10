"""Source-grounded citation frontier tests with fictional Git evidence only."""
from __future__ import annotations

from copy import deepcopy
from hashlib import sha256
from pathlib import Path
import subprocess

import pytest

from experiments.r0_p03_navigation_probe import (
    historical_evidence_dependency_frontier as frontier,
    source_world_coverage_gate as world,
)


def invented() -> tuple[dict, dict[str, bytes]]:
    bodies = {
        "README.md": (
            b"# Fictional orientation\n"
            b"See Research 001, Checkpoint 001, Research 999 and "
            b"docs/research/001_history.md.\n"
        ),
        "docs/DECISIONS.md": b"# Fictional policy\nSee Research 001.\n",
        "docs/checkpoints/001_history.md": (
            b"# Fictional checkpoint\n"
            b"See Validation 001 and ../research/002_secondary.md.\n"
        ),
        "docs/research/001_history.md": (
            b"# Fictional research\n"
            b"Read [follow-up](002_secondary.md#details).\n"
        ),
        "docs/research/002_secondary.md": b"# Other fictional history\n",
        "docs/local_execution/validation/001_report.md": (
            b"# Fictional evidence receipt\nNo real test was run.\n"
        ),
        "docs/research/003_unlinked.md": (
            b"# Unlinked fictional evidence\nNot necessarily irrelevant.\n"
        ),
        "docs/research/004_media.png": b"\x89PNG\x00NOT_REAL_IMAGE",
        "frontend/src/demo.tsx": b"export default null;\n",
    }
    rows = []
    for path, raw in bodies.items():
        unsupported = path.endswith(".png")
        rows.append({
            "path": path, "git_blob_oid": world.sha1git(raw),
            "sha256": sha256(raw).hexdigest() if not unsupported else None,
            "bytes": len(raw) if not unsupported else None,
            "family_hint": world.family(path),
            "visibility": (
                world.MODALITY_HOLD if unsupported
                else "HISTORICAL_REVIEW_ONLY"
                if path.startswith(("docs/checkpoints/", "docs/research/",
                                    "docs/local_execution/validation/"))
                else "PRELIMINARY_CANDIDATE_UNQUALIFIED"
            ),
            "status": world.NO_ADMISSION,
            "flags": ["FICTIONAL_REVIEW_FLAG"]
                if path == "docs/research/003_unlinked.md" else [],
        })
    rows.sort(key=lambda r: r["path"])
    ledger = {
        "source_ref": "a" * 40,
        "source_count": len(rows),
        "source_records": rows,
        "roster_sha256": world._fingerprint(rows),
    }
    return ledger, {p: raw for p, raw in bodies.items() if not p.endswith(".png")}


def test_fictional_first_second_hop_and_full_accounting():
    ledger, bodies = invented()
    local, safe = frontier.frontier(ledger, bodies)
    assert safe["source_count"] == 9
    assert safe["historical_critical_family_total"] == 6
    by_path = {r["path"]: r for r in local["review_candidate_records"]}
    assert by_path["docs/research/001_history.md"][
        "prospective_evidence_signals"]["direct_core_mention"]
    assert by_path["docs/checkpoints/001_history.md"][
        "prospective_evidence_signals"]["direct_core_mention"]
    assert by_path["docs/research/002_secondary.md"][
        "prospective_evidence_signals"]["two_hop_core_mention"]
    assert by_path["docs/local_execution/validation/001_report.md"][
        "prospective_evidence_signals"]["two_hop_core_mention"]
    assert by_path["docs/research/003_unlinked.md"][
        "prospective_evidence_signals"]["no_detected_core_path"]
    assert by_path["docs/research/003_unlinked.md"][
        "prospective_evidence_signals"]["historical_lexical_or_path_flag"]
    assert by_path["docs/research/004_media.png"][
        "prospective_evidence_signals"]["unsupported_representation"]
    assert len(local["review_candidate_records"]) == 6
    assert all(r["status"] == "NOT_ADMITTED" for r in local["review_candidate_records"])
    assert safe["source_admissions"] == 0
    assert safe["task_answerability"] == "NOT_PROVEN"
    assert safe["scored_author_packet"] == "NOT_CONSTRUCTED"
    assert "docs/research/001_history.md" not in str(safe)


def test_explicit_missing_and_relative_reference_parsing():
    ledger, bodies = invented()
    index = frontier.numbered_index({r["path"] for r in ledger["source_records"]})
    origins = {r["path"] for r in ledger["source_records"]}
    references = frontier.references(
        bodies["README.md"].decode(), "README.md", origins, index
    )
    assert any(r["status"] == "UNRESOLVED_NUMBERED"
               for r in references)
    assert sum(r["status"] == "EXACT_RESOLVED" for r in references) >= 3
    historical = frontier.references(
        bodies["docs/checkpoints/001_history.md"].decode(),
        "docs/checkpoints/001_history.md", origins, index
    )
    assert any(r["target"] == "docs/research/002_secondary.md"
               for r in historical)
    md = frontier.references(
        bodies["docs/research/001_history.md"].decode(),
        "docs/research/001_history.md", origins, index
    )
    assert any(r["target"] == "docs/research/002_secondary.md" for r in md)


def test_no_citation_does_not_authorize_exclusion():
    ledger, bodies = invented()
    _, safe = frontier.frontier(ledger, bodies)
    row = safe["critical_family_signals"]["historical_status"]
    assert row["no_detected_core_path"] > 0
    assert safe["author_world"] == "WORLD_UNFROZEN"
    assert safe["source_admissions"] == 0


def test_missing_text_bad_sha_and_stale_ledger_rejected():
    ledger, bodies = invented()
    del bodies["docs/DECISIONS.md"]
    with pytest.raises(ValueError, match="Incomplete"):
        frontier.frontier(ledger, bodies)
    ledger, bodies = invented()
    bodies["docs/DECISIONS.md"] = b"TAMPERED"
    with pytest.raises(ValueError, match="not authenticated"):
        frontier.frontier(ledger, bodies)
    ledger, bodies = invented()
    ledger["roster_sha256"] = "0" * 64
    with pytest.raises(ValueError, match="identity"):
        frontier.frontier(ledger, bodies)


def test_malformed_reference_and_ambiguous_number_not_silently_resolved():
    ledger, bodies = invented()
    known = {r["path"] for r in ledger["source_records"]}
    idx = frontier.numbered_index(known)
    idx[("research", 1)].append("docs/research/001_second_representation.md")
    result = frontier.references("Research 001", "README.md", known, idx)
    assert result[0]["status"] == "AMBIGUOUS_NUMBERED"
    assert result[0]["target"] is None
    out = frontier.references("[bad](../../unsafe.md)", "README.md", known, idx)
    assert out[0]["status"] == "OUTSIDE_RELATIVE_SCOPE"


def test_deterministic_receipt_and_no_source_text_leak():
    ledger, bodies = invented()
    local1, safe1 = frontier.frontier(ledger, bodies)
    local2, safe2 = frontier.frontier(deepcopy(ledger), dict(reversed(list(bodies.items()))))
    assert safe1 == safe2
    assert local1 == local2
    assert sha256(frontier.canonical(local1)).hexdigest() == safe1["frontier_sha256"]
    assert "Fictional" not in str(safe1)
    assert "FICTIONAL_REVIEW_FLAG" not in str(safe1)
    assert all("literal_reference" not in v for v in safe1.values() if isinstance(v, dict))


def git(repo: Path, *args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=repo).decode().strip()


def test_actual_git_blob_reader_uses_commit_not_worktree(tmp_path: Path):
    repo = tmp_path / "repo"
    repo.mkdir()
    git(repo, "init", "-q")
    git(repo, "config", "user.name", "Fictional")
    git(repo, "config", "user.email", "fixture@example.invalid")
    p = repo / "README.md"
    original = b"# Fictional pinned source\n"
    p.write_bytes(original)
    git(repo, "add", ".")
    git(repo, "commit", "-qm", "Fixture")
    oid = git(repo, "rev-parse", "HEAD:README.md")
    row = {
        "path": "README.md", "git_blob_oid": oid,
        "sha256": sha256(original).hexdigest(), "bytes": len(original),
        "visibility": "PRELIMINARY_CANDIDATE_UNQUALIFIED",
    }
    assert frontier.exact_blobs(repo, [row]) == {"README.md": original}
    p.write_text("WRONG WORKTREE CONTENT", encoding="utf-8")
    assert frontier.exact_blobs(repo, [row]) == {"README.md": original}
    row["sha256"] = "0" * 64
    with pytest.raises(ValueError, match="differs from Git bytes"):
        frontier.exact_blobs(repo, [row])


def test_unsupported_must_not_be_parsed_or_pretended_text():
    ledger, bodies = invented()
    unsupported = next(r for r in ledger["source_records"]
                       if r["visibility"] == world.MODALITY_HOLD)
    assert unsupported["path"] not in bodies
    body, safe = frontier.frontier(ledger, bodies)
    assert safe["document_scan_counts"]["UNSUPPORTED_NOT_INSPECTED"] == 1
    assert body["source_admissions"] == 0
    bodies[unsupported["path"]] = b"Not really a parseable image"
    with pytest.raises(ValueError, match="Inappropriate|Incomplete|inappropriate"):
        frontier.frontier(ledger, bodies)


def test_cross_family_validation_mentions_are_not_equated_with_authority():
    ledger, bodies = invented()
    local, _ = frontier.frontier(ledger, bodies)
    summary = frontier.cross_family_summary(local)
    assert summary["validation_records_total"] == 1
    assert summary["status_to_validation_reference_edges"] == 1
    assert summary["validation_to_status_reference_edges"] == 0
    assert summary[
        "validation_with_detected_status_reference_either_direction"
    ] == 1
    assert summary["validation_without_detected_status_reference"] == 0
    assert summary["source_admissions"] == 0
    assert summary["scientific_authority_and_answerability"] == "NOT_ESTABLISHED"
    assert "docs/" not in str(summary)
    with pytest.raises(ValueError, match="Incomplete"):
        frontier.cross_family_summary({"review_candidate_records": []})
