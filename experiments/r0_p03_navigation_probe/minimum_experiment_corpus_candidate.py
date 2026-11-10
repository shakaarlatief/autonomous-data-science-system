"""Task-independent, exactly pinned R0-P03 minimum experiment-corpus candidate.

This is a concrete original-source cohort for ONE prospective release review,
not another eligibility methodology experiment. Its 80 original Git files are
real, unmodified, equal-input *candidates* only. Source-family quotas are
frozen by this version before scored authoring, reference answers or arm
construction. They do not themselves establish representative truth,
historical currentness, semantic evidence closure or safe author disclosure.

All selected contents and exact paths are stored in a locally ignored ZIP.
Nothing is disclosed to a blind author or scored actor. The public stdout
and safe receipt contain only aggregate counts and cryptographic commitments.
No build/held-out split or scored tasks are drawn before source qualification.
"""
from __future__ import annotations

from collections import Counter, defaultdict
from hashlib import sha256
import json
from pathlib import Path, PurePosixPath
import re
import sys
from zipfile import ZIP_STORED, ZipFile, ZipInfo
from io import BytesIO

from experiments.r0_p03_navigation_probe import (
    historical_evidence_dependency_frontier as graph,
    source_world_coverage_gate as world,
)

ID = "R0_P03_ACTUAL_80_SOURCE_CORPUS_CANDIDATE_V01"
DIR = Path(".venv") / ".r0_p03_eighty_source_candidate_v01"
PACKAGE = "R0_P03_EIGHTY_SOURCE_RESTRICTED_RELEASE_CANDIDATE.zip"
RECEIPT = "R0_P03_EIGHTY_SOURCE.safe-receipt.json"
SALT = "SOURCE_NEUTRAL_EIGHTY_COHORT_PRE_TASK_PRE_ARM_2026_11_10"
FIXED_ZIP_TIME = (2026, 1, 1, 0, 0, 0)
TOTAL = 80

# A candidate evidence mix, not approved category quotas or a scored split.
# Name reflects original-path routing only, not accepted semantic owner role.
QUOTAS = {
    "orientation": 3,
    "governing": 12,
    "product_source": 14,
    "project_source": 12,
    "verification": 10,
    "tooling": 4,
    "historical_status": 10,
    "execution_evidence": 9,
    "source_schema": 3,
    "other": 3,
}
assert sum(QUOTAS.values()) == TOTAL

# These exact central sources were already in the earlier 406-file preliminary
# candidate collection; their inclusion is for source-world coverage, not a
# declaration that they are currently applicable or author-visible.
EXACT_MANDATORY = (
    "README.md",
    "docs/README.md",
    "docs/CONTINUITY.md",
    "docs/DECISIONS.md",
    "docs/specifications/028_v1_project_knowledge_architecture_implementation_and_migration_contract.md",
    "docs/current_routing.json",
)
LEAK = re.compile(
    r"R0[-_ ]?P0?3|Research\s+513|Research\s+217|"
    r"navigation_scenarios|must[_ -]?retrieve|must[_ -]?not[_ -]?retrieve|"
    r"gold[_ -]?(?:answer|label|key)|\bB[0-4]\s*[-\u2013]\s*B[0-4]\b",
    re.I,
)
HIST_ALLOWED = "HISTORICAL_REVIEW_ONLY"
BASE_ALLOWED = "PRELIMINARY_CANDIDATE_UNQUALIFIED"
SOURCE_ROLE_HOLD = "CANDIDATE_REQUIRES_INDEPENDENT_AUTHOR_WORLD_RELEASE"
BRIEF = """# R0-P03 original-source release-review candidate (NOT an author packet)

This is a restricted 80-source prospective experimental-corpus candidate
from one exact historical public Git commit. It has been selected BEFORE
independent primary tasks, gold, held-out carrier split, or B0-B4 arm scores.

Treat every file as an ORIGINAL HISTORICAL SOURCE, not the current workspace.
Filename/family labels, citation graph edges and Git identity are NOT proof
of governing authority, implementation, execution success or source admission.

Review for a prospective *fresh blind primary information-need author*, and
separately for common scored-arm source parity, using the frozen source-family
rule. Critically examine all included original sources, supporting/superseding
witnesses, material omitted dependencies, prospective task capacity, and
CUMULATIVE disclosure. The source set is intentionally not a closed semantic
world: additional source witnesses may be necessary, and MUST be requested
as a HOLD rather than hallucinated.

The local manifest identifies exact version, SHA-256 and path for each source
and every detected literal citation to sources omitted from this candidate.
Sources with recognizable direct R0-P03/legacy-answer leakage markers are
held back by a simple *necessary but insufficient* prefilter. This prefilter
is not a complete disclosure clearance.

No source has been admitted. Do not use this ZIP for scored task authors,
gold/reference annotators, arm developers, model scorers, or browsing.
Do not treat this as a 60/20 build-maintenance split.
"""

def canonical(value: object) -> bytes:
    return (json.dumps(
        value, sort_keys=True, ensure_ascii=True, separators=(",", ":"),
    ) + "\n").encode("ascii")


def order(row: dict, lane: str, pin: str) -> tuple[str, str]:
    """Fixed selection order, never affected by question wording or arm score."""
    key = "\0".join((
        SALT, pin, lane, row["path"], row["git_blob_oid"],
    )).encode("utf-8")
    return sha256(key).hexdigest(), row["path"]


def _safe_original(row: dict, bodies: dict[str, bytes]) -> bool:
    if row.get("flags") or row["visibility"] == world.MODALITY_HOLD:
        return False
    raw = bodies.get(row["path"])
    if not isinstance(raw, bytes):
        return False
    try:
        txt = raw.decode("utf-8")
    except UnicodeDecodeError:
        return False
    return not LEAK.search(txt)


def select(
    ledger: dict, citation_graph: dict,
    bodies: dict[str, bytes],
) -> tuple[list[dict], dict]:
    """Select actual source identities; forbid all automatic release.

    Historical-status exemplars deliberately include both governing/core
    citations and status-to-validation connections, without presuming those
    connections are real semantic or authoritative dependencies.
    """
    rows = ledger["source_records"]
    by_path = {r["path"]: r for r in rows}
    if len(by_path) != len(rows) or ledger["source_count"] != len(rows):
        raise ValueError("Corrupt original source roster")
    if ledger["roster_sha256"] != world._fingerprint(rows):
        raise ValueError("Historical source-roster digest changed")
    if ledger["source_ref"] != world.PIN:
        raise ValueError("Not the preregistered historical source revision")
    available = {role: [] for role in QUOTAS}
    for row in rows:
        family = row["family_hint"]
        if family not in available:
            raise ValueError("Uncontrolled source family")
        if family in {"historical_status", "execution_evidence"}:
            if row["visibility"] != HIST_ALLOWED:
                continue
        elif row["visibility"] != BASE_ALLOWED:
            continue
        if _safe_original(row, bodies):
            available[family].append(row)

    picked: list[dict] = []
    selected: set[str] = set()
    for path in EXACT_MANDATORY:
        row = by_path.get(path)
        if row is None or not _safe_original(row, bodies) or row not in available[row["family_hint"]]:
            raise ValueError("Critical neutral source anchor unavailable or unsafe")
        picked.append(row)
        selected.add(path)

    def take(family: str, candidates: list[dict], n: int, lane: str) -> None:
        if n < 0:
            raise ValueError("Negative cohort quota")
        pool = sorted(
            (r for r in candidates if r["path"] not in selected),
            key=lambda r: order(r, lane, ledger["source_ref"]),
        )
        if len(pool) < n:
            raise ValueError(f"Insufficient unbiased source candidates: {family}/{lane}")
        for row in pool[:n]:
            if row["family_hint"] != family:
                raise ValueError("Cross-family sampling corruption")
            picked.append(row)
            selected.add(row["path"])

    refs = citation_graph["references_by_source"]
    review = {
        r["path"]: r for r in citation_graph["review_candidate_records"]
    }
    historical = available["historical_status"]
    validations = available["execution_evidence"]
    valpaths = {r["path"] for r in validations}
    statpaths = {r["path"] for r in historical}
    outgoing_validation = {
        r["path"] for r in historical
        if any(ref["status"] == "EXACT_RESOLVED"
               and ref["target"] in valpaths for ref in refs.get(r["path"], []))
    }
    core = {
        r["path"] for r in historical
        if review.get(r["path"], {}).get(
            "prospective_evidence_signals", {}
        ).get("direct_core_mention")
    }
    take("historical_status", [r for r in historical
         if r["path"] in outgoing_validation & core], 3, "core_hist_with_validation")
    take("historical_status", [r for r in historical
         if r["path"] in core], 3, "core_hist_other")
    take("historical_status", [r for r in historical
         if r["path"] in outgoing_validation], 4, "linked_hist_other")

    mentioned_validation = {
        r["target"]
        for path in selected & statpaths
        for r in refs.get(path, [])
        if r["status"] == "EXACT_RESOLVED" and r["target"] in valpaths
    }
    linked_validation = {
        r["path"] for r in validations
        if any(hit["target"] in statpaths and hit["status"] == "EXACT_RESOLVED"
               for hit in refs.get(r["path"], []))
    }
    take("execution_evidence",
         [r for r in validations if r["path"] in mentioned_validation],
         min(len(mentioned_validation), 5), "validation_neighbors_of_selected_status")
    take("execution_evidence",
         [r for r in validations if r["path"] in linked_validation],
         QUOTAS["execution_evidence"] -
         sum(r["family_hint"] == "execution_evidence" for r in picked),
         "validation_linked_history")
    for family, target in QUOTAS.items():
        if family in {"historical_status", "execution_evidence"}:
            continue
        already = sum(row["family_hint"] == family for row in picked)
        take(family, available[family], target - already, "fixed_family_source_selection")

    picked.sort(key=lambda r: r["path"])
    count = Counter(r["family_hint"] for r in picked)
    if len(picked) != TOTAL or dict(count) != QUOTAS:
        raise ValueError("Exact representative quota not satisfied")
    if len({r["git_blob_oid"] for r in picked}) != TOTAL:
        # The corpus counts physical carriers and must avoid duplicate
        # identical byte representations giving artificial test coverage.
        raise ValueError("Duplicate historical content selected")
    cross_edges = {
        (p, ref["target"])
        for p in selected & statpaths
        for ref in refs.get(p, [])
        if ref["status"] == "EXACT_RESOLVED"
        and ref["target"] in selected & valpaths
    }
    if len(cross_edges) < 2:
        raise ValueError("Insufficient observed historical-validation source context")
    result = {
        "source_count": len(picked),
        "family_counts": dict(sorted(count.items())),
        "exact_mandatory_anchor_count": len(EXACT_MANDATORY),
        "selected_literal_status_validation_citation_edges": len(cross_edges),
        "literally_connected_status_records": len({s for s, _ in cross_edges}),
        "literally_connected_validation_records": len({t for _, t in cross_edges}),
        "lexical_risk_filter_status": "PASS_NECESSARY_ONLY",
        "semantic_authority_closure": "NOT_PROVEN",
        "combined_author_exposure_clearance": "NOT_PERFORMED",
        "source_admissions": 0,
    }
    return picked, result


def evidence_manifest(
    ledger: dict, graph_data: dict, chosen: list[dict],
    corpus_diagnostic: dict, bodies: dict[str, bytes],
) -> dict:
    selected = {row["path"] for row in chosen}
    known = {row["path"] for row in ledger["source_records"]}
    result = []
    for row in chosen:
        p = row["path"]
        raw = bodies[p]
        if (
            world.sha1git(raw) != row["git_blob_oid"]
            or sha256(raw).hexdigest() != row["sha256"]
            or len(raw) != row["bytes"]
            or not _safe_original(row, bodies)
        ):
            raise ValueError("Unverified or risk-flagged selected content")
        links = {
            ref["target"]
            for ref in graph_data["references_by_source"].get(p, [])
            if ref["status"] == "EXACT_RESOLVED" and ref["target"] != p
        }
        result.append({
            "path": p,
            "git_blob_oid": row["git_blob_oid"],
            "sha256": row["sha256"],
            "bytes": row["bytes"],
            "source_family_path_hint_not_semantic_authority": row["family_hint"],
            "exact_original_text": "sources/" + p,
            "literal_refs_in_selected_original": sorted(links & selected),
            "literal_refs_outside_selected_world": sorted(links & known - selected),
            "family_qualification": "NOT_INDEPENDENTLY_REVIEWED",
            "author_exposure_decision": SOURCE_ROLE_HOLD,
            "current_authority": "UNKNOWN_NOT_PROVEN",
            "implementation_validation": "UNKNOWN_NOT_PROVEN",
            "combined_source_contamination": "UNKNOWN_NOT_PROVEN",
        })
    return {
        "schema_version": 1,
        "identifier": ID,
        "historical_commit": ledger["source_ref"],
        "complete_inventory_sha256": ledger["roster_sha256"],
        "scope": "ONE_REPRESENTATIVE_EXACT_GIT_SOURCE_CORPUS_RELEASE_REVIEW_NOT_A_SCORED_FIXTURE",
        "prospective_capacity_target": {
            "cold_start_current_orientation": 3,
            "cross_plane_discovery": 3,
            "impact_analysis_architecture_evolution": 3,
            "exact_source_authority_recovery": 3,
        },
        "selected_source_count": len(chosen),
        "source_family_quota_hints": dict(sorted(QUOTAS.items())),
        "sampling_note": (
            "Fixed content-pin and family hash selection with three fixed "
            "orientation, decision and routing anchors, plus linked historical "
            "and execution citation exemplars. This does NOT prove task "
            "answerability or authoritative completeness."
        ),
        "audit": corpus_diagnostic,
        "records": result,
        "build_heldout_split": "NOT_DRAWN_BEFORE_SOURCE_ACCEPTANCE",
        "task_authorship": "NOT_STARTED",
        "comparative_arm_scoring": "NOT_STARTED",
        "author_world_release": "PROHIBITED_PENDING_INDEPENDENT_ORIGINAL_SOURCE_REVIEW",
    }


def build(repo: Path, *, verify_only: bool = False) -> dict:
    repo = repo.resolve(strict=True)
    if not (repo / ".git").is_dir():
        raise ValueError("Expected real trusted historical Git repository")
    ledger, receipt = world.compute(repo)
    if receipt["complete_roster_records"] != 2539:
        raise ValueError("Historical source universe drift")
    bodies = graph.exact_blobs(repo, ledger["source_records"])
    g, _ = graph.frontier(ledger, bodies)
    selected, checks = select(ledger, g, bodies)
    manifest = evidence_manifest(ledger, g, selected, checks, bodies)
    contents = {
        "MANIFEST.json": canonical(manifest),
        "SOURCE_RELEASE_REVIEW_BRIEF.md": BRIEF.encode("utf-8"),
    }
    contents.update({"sources/" + row["path"]: bodies[row["path"]]
                     for row in selected})
    output = BytesIO()
    with ZipFile(output, "w") as archive:
        for p, data in sorted(contents.items()):
            info = ZipInfo(p, date_time=FIXED_ZIP_TIME)
            info.compress_type = ZIP_STORED
            info.external_attr = 0o600 << 16
            info.create_system = 3
            archive.writestr(info, data)
    blob = output.getvalue()
    safe = {
        "identifier": ID,
        "historical_commit": ledger["source_ref"],
        "complete_inventory_source_count": 2539,
        "complete_inventory_sha256": ledger["roster_sha256"],
        "candidate_original_source_count": len(selected),
        "source_family_path_hint_counts": checks["family_counts"],
        "candidate_literal_history_validation_edges": checks[
            "selected_literal_status_validation_citation_edges"
        ],
        "distinct_selected_historical_with_linked_validation": checks[
            "literally_connected_status_records"
        ],
        "distinct_selected_validation_with_linked_historical": checks[
            "literally_connected_validation_records"
        ],
        "original_source_byte_total": sum(row["bytes"] for row in selected),
        "candidate_manifest_sha256": sha256(contents["MANIFEST.json"]).hexdigest(),
        "candidate_archive_sha256": sha256(blob).hexdigest(),
        "candidate_archive_bytes": len(blob),
        "selection_status": "DONE_REAL_GIT_REVIEW_CANDIDATE_ONLY",
        "semantic_authority_and_actual_task_capacity": "NOT_PROVEN",
        "cumulative_exposure_qualification": "NOT_PERFORMED",
        "independent_release_reviewer": "NOT_STARTED",
        "source_admissions": 0,
        "author_world": "WORLD_UNFROZEN",
        "scored_tasks": "NONE",
        "build_heldout_split": "NOT_DRAWN",
        "arm_scores": "NONE",
    }
    folder = repo / DIR
    full = folder / PACKAGE
    rpath = folder / RECEIPT
    receipt_data = canonical(safe)
    if verify_only:
        if (
            not full.is_file() or full.read_bytes() != blob
            or not rpath.is_file() or rpath.read_bytes() != receipt_data
        ):
            raise ValueError("Source-world candidate not byte reproducible")
        print("ACTUAL_EIGHTY_SOURCE_CANDIDATE_REPRODUCIBILITY=PASS")
    else:
        if full.exists() or rpath.exists():
            raise FileExistsError("No overwrite of real source-world candidate")
        folder.mkdir(parents=True, exist_ok=True)
        with full.open("xb") as f:
            f.write(blob)
        with rpath.open("xb") as f:
            f.write(receipt_data)
    print(json.dumps(safe, sort_keys=True))
    return safe


if __name__ == "__main__":
    if len(sys.argv) not in (2, 3) or (
        len(sys.argv) == 3 and sys.argv[2] != "--verify-only"
    ):
        raise SystemExit("usage: python -m experiments.r0_p03_navigation_probe."
                         "minimum_experiment_corpus_candidate REPO [--verify-only]")
    build(Path(sys.argv[1]), verify_only=len(sys.argv) == 3)
