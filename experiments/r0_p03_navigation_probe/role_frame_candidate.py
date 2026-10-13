"""Non-scored, source-ref-bound candidate R0-P03 role and modality census.

This deliberately replaces neither Research 513 nor the historical Markdown-only
feasibility module. It surveys textual public Git carriers by *potential*
information role, separates explicit evaluation leakage and auxiliary assets,
and reports candidate coverage without selecting any experimental source.

A path-family classification is only a review-routing hint. It cannot settle
source authority, currentness, accepted J1 identities, J2 realization links,
or whether a source is a legitimate gold/heldout carrier. A qualified non-arm
extractor must ground those conclusions in exact source provenance later.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
from collections import Counter, defaultdict
from pathlib import Path

SOURCE_REF = "c57556a8bf993a1d327e9197acb7b7c745071cd8"
SOURCE_ROOTS = (
    "docs", "tools", "schemas", "src", "tests", "scripts",
    "frontend", "migrations", "experiments",
)
REVIEWABLE_SUFFIXES = frozenset({
    ".md", ".json", ".jsonl", ".py", ".ts", ".tsx", ".js", ".mjs",
    ".sql", ".toml", ".yaml", ".yml", ".txt", ".html", ".css",
    ".mako", ".ps1", ".sh",
})
REVISION = re.compile(r"[a-f0-9]{40}\Z")
NUMBERED = re.compile(r"^(\d{3})_")
MODEL_MESSAGES = re.compile(r"^docs/model_collaboration/threads/MC-0030/messages/(\d{3})_")
LEAKAGE_RESEARCH_IDS = frozenset({556, 557, 558, 559})
SPECIAL_NAVIGATION = frozenset({
    "docs/CURRENT_STATE.md",
    "docs/KNOWLEDGE_MAP.md",
    "docs/ARCHITECTURE_PROGRAM_OVERVIEW.md",
    "docs/CONTINUITY.md",
})


def numbered(path: str) -> int | None:
    hit = NUMBERED.match(path.rsplit("/", 1)[-1])
    return int(hit.group(1)) if hit else None


def leakage_reason(path: str) -> str | None:
    """Flag explicit contemporary R0-P03 content, not all historical research."""
    n = numbered(path)
    if path.startswith("experiments/r0_p03_") or path.startswith("tests/unit/test_r0_p03_"):
        return "P03_DESIGN_AND_HARNESS"
    if path.startswith("docs/research/") and (
        n in LEAKAGE_RESEARCH_IDS or "r0_p03_" in path.lower()
    ):
        return "P03_RESEARCH_DESIGN"
    if path.startswith("docs/checkpoints/") and n is not None and n >= 892:
        return "P03_CONTEMPORARY_CHECKPOINT"
    if path.startswith("docs/local_execution/validation/") and n is not None and n >= 244:
        return "P03_CONTEMPORARY_VALIDATION"
    match = MODEL_MESSAGES.match(path)
    if match and int(match.group(1)) >= 61:
        return "P03_MODEL_DESIGN_MESSAGE"
    return None


def proposed_family(path: str) -> tuple[str, str, str]:
    """Return eligibility bucket, path-derived role hint and lifecycle qualifier.

    No bucket means the path is authoritative. No code-source role proves
    REALIZES/COVERS and no existing generated view becomes current merely
    because the containing Git commit is the census reference.
    """
    if path == "docs/current_routing.json":
        return ("REVIEW", "operational_routing_source", "SOURCE_STATUS_REVIEW")
    if path in SPECIAL_NAVIGATION:
        return ("REVIEW_WITH_CONTAMINATION_CONTROL", "navigation_or_orientation", "SOURCE_STATUS_REVIEW")
    if path.startswith("docs/project_knowledge/generated/"):
        return ("REVIEW", "derived_project_knowledge_view", "DERIVED_NOT_GOVERNING")
    if path.startswith("docs/project_knowledge/"):
        return ("REVIEW", "incumbent_project_knowledge_source", "SOURCE_STATUS_REVIEW")
    if path == "docs/DECISIONS.md":
        return ("REVIEW", "governing_decision_carrier", "DECISION_SCOPE_REVIEW")
    if path.startswith("docs/specifications/"):
        return ("REVIEW", "specification_carrier", "CONTRACT_EFFECT_REVIEW")
    if path.startswith("docs/research/"):
        return ("REVIEW", "research_proposal_or_result", "ACCEPTANCE_CURRENTNESS_REVIEW")
    if path.startswith("docs/foundations/"):
        return ("REVIEW", "foundation", "ACCEPTANCE_CURRENTNESS_REVIEW")
    if path.startswith("docs/checkpoints/"):
        return ("REVIEW", "historical_progress_evidence", "HISTORICAL_CARRIER_NOT_CURRENTNESS")
    if path.startswith("docs/local_execution/") or path.startswith("docs/model_collaboration/"):
        return ("REVIEW", "engineering_or_collaboration_evidence", "EVIDENCE_SCOPE_REVIEW")
    if path.startswith("docs/source_universe/") or path.startswith("docs/cockpit/") or path.startswith("docs/methodological_knowledge/"):
        return ("REVIEW", "domain_or_structured_project_source", "SOURCE_STATUS_REVIEW")
    if path.startswith("schemas/"):
        return ("REVIEW", "machine_schema_realization", "NOT_PROVEN_COVERAGE")
    if path.startswith("tools/"):
        return ("REVIEW", "project_tool_realizer_candidate", "NOT_PROVEN_COVERAGE")
    if path.startswith("tests/"):
        return ("REVIEW", "verification_or_test_carrier", "RESULT_NOT_ASSUMED")
    if path.startswith("scripts/"):
        return ("REVIEW", "developer_tool_or_qualification", "NOT_PROVEN_COVERAGE")
    if path.startswith("migrations/"):
        return ("REVIEW", "database_migration_or_schema", "NOT_PROVEN_COVERAGE")
    if path.startswith("src/") or path.startswith("frontend/"):
        return ("REVIEW", "product_or_cross_plane_realizer", "NOT_PROVEN_COVERAGE")
    if path.startswith("experiments/"):
        return ("AUXILIARY_NOT_SAMPLED", "historical_fixture_or_probe", "NO_PROSPECTIVE_GOLD_INFERENCE")
    return ("REVIEW", "other_project_document", "SOURCE_STATUS_REVIEW")


def committed_paths(repo: Path, source_ref: str) -> dict[str, str]:
    if not REVISION.fullmatch(source_ref):
        raise ValueError("source_ref must be an exact lowercase Git SHA")
    result = subprocess.run(
        ["git", "ls-tree", "-r", "-z", source_ref, "--", *SOURCE_ROOTS],
        cwd=repo, check=True, capture_output=True,
    )
    paths = {}
    for entry in result.stdout.split(b"\0"):
        if not entry:
            continue
        meta, name = entry.split(b"\t", 1)
        mode, kind, oid = meta.decode("ascii").split(" ")
        path = name.decode("utf-8")
        if kind == "blob" and mode in {"100644", "100755"}:
            paths[path] = oid
    if not paths:
        raise ValueError("No Git source files at exact ref")
    return paths


def build_role_census(repo: Path, source_ref: str) -> dict[str, object]:
    tracked = committed_paths(repo, source_ref)
    groups: dict[str, Counter[str]] = defaultdict(Counter)
    lifecycle_hints: dict[str, Counter[str]] = defaultdict(Counter)
    withheld = Counter()
    provenance = []
    text_candidates = 0
    for path, oid in sorted(tracked.items()):
        if Path(path).suffix.lower() not in REVIEWABLE_SUFFIXES:
            withheld["NON_TEXT_OR_UNSUPPORTED"] += 1
            continue
        leaked = leakage_reason(path)
        if leaked:
            withheld[leaked] += 1
            continue
        bucket, role, lifecycle = proposed_family(path)
        groups[bucket][role] += 1
        lifecycle_hints[role][lifecycle] += 1
        if bucket.startswith("REVIEW"):
            text_candidates += 1
        provenance.append(f"{path}\0{oid}\n")
    return {
        "schema_version": 1,
        "classification": "UNFROZEN_ROLE_FRAME_CENSUS_NONSCORING",
        "source_ref": source_ref,
        "source_scope": list(SOURCE_ROOTS),
        "tracked_path_count": len(tracked),
        "candidate_text_path_count": text_candidates,
        "path_family_counts": {
            k: dict(sorted(v.items())) for k, v in sorted(groups.items())
        },
        "lifecycle_review_hints_by_role": {
            k: dict(sorted(v.items())) for k, v in sorted(lifecycle_hints.items())
        },
        "excluded_or_withheld_counts": dict(sorted(withheld.items())),
        "included_path_blob_digest_sha256": hashlib.sha256(
            "".join(provenance).encode("utf-8")
        ).hexdigest(),
        "limitations": [
            "Path-derived role hints do not certify currentness, governing authority, eligibility, accepted J1 identities, J2 coverage or evidence validity.",
            "Generated/derived paths must be checked against source digests and never elevated to governing authority.",
            "Contemporary R0-P03 design, tests and messages are withheld from the future closed scoring world; historical W5 has a separate 65-source immutable world.",
            "Eligible review paths are not an exact 60/20 corpus or task-source closure. No selected build or heldout path, seed, task, gold answer, evaluator or score is emitted.",
            "The source referee must separately resolve cross-plane Product/Project scope, historical status, privacy/permission and source role before any fixture freeze.",
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-ref", default=SOURCE_REF)
    parser.add_argument("--repository", type=Path, default=Path(__file__).resolve().parents[2])
    args = parser.parse_args()
    print(json.dumps(build_role_census(args.repository.resolve(), args.source_ref), indent=2))


if __name__ == "__main__":
    main()
