"""Task-independent R0-P03 prospective author-source-world closure diagnostic.

This real, pinned-Git *engineering* audit uses the prior two reproducing
source populations (406 candidate text files and 2,133 additional historical
records at the historical ref). It DOES NOT select a scored task, construct a
future author packet, infer source authority or admit a document.

Its purpose is to make material source-family gaps explicit, accountable
and testable, before a qualified independent source-world decision. Outputs
containing exact per-source paths or risk flags stay in ignored local scratch.
The public-safe receipt has only families/capacity flags and counts.

A complete roster is a necessary but insufficient condition for closure.
No source has been semantically accepted by running this command.
"""
from __future__ import annotations

from collections import Counter, defaultdict
from hashlib import sha256
import json
from pathlib import Path, PurePosixPath
import re
import sys

from experiments.r0_p03_navigation_probe import (
    primary_author_frontend_expansion_candidate as frontend,
    primary_author_historical_evidence_review_candidate as history,
)

IDENTIFIER = "R0_P03_TASK_INDEPENDENT_SOURCE_WORLD_COVERAGE_V1"
PIN = frontend.prior.base.PIN
OUTPUT = Path(".venv") / ".r0_p03_source_world_coverage"
LEDGER = "R0_P03_SOURCE_WORLD_COVERAGE_NON_ADMISSION_LEDGER.json"
RECEIPT = "R0_P03_SOURCE_WORLD_COVERAGE.safe-receipt.json"
NO_ADMISSION = "NOT_ADMITTED"
ROSTER_NOT_FROZEN = "WORLD_UNFROZEN"
MODALITY_HOLD = "UNSUPPORTED_REPRESENTATION"
REVIEW_HOLD = "NEEDS_INDEPENDENT_SOURCE_QUALIFICATION"
SCORING_HOLD = "SCORED_AUTHOR_WORLD_NOT_READY"
REFERENCE_SCHEMA = "v1-task-independent-source-family-evidence"

# These are family-presence diagnostics, NOT lists of subjects or task stems.
# The schema is prospective, fixed before task authorship or score observation.
REQUIRED_CAPACITY = {
    "cold_start_current_orientation": (
        "orientation", "governing", "historical_status",
    ),
    "cross_plane_discovery": (
        "product_source", "project_source", "verification",
    ),
    "impact_analysis_architecture_evolution": (
        "governing", "historical_status", "verification",
    ),
    "exact_source_authority_recovery": (
        "orientation", "historical_status", "execution_evidence",
    ),
}
EXTRA_FAMILIES = ("other", "source_schema", "tooling")
ALL_FAMILIES = set(EXTRA_FAMILIES) | {
    x for families in REQUIRED_CAPACITY.values() for x in families
}


def family(path: str) -> str:
    """Path-only scheduling hint, never authority or task answer evidence."""
    if path.startswith("frontend/"):
        return "product_source"
    if path.startswith("src/"):
        return "project_source"
    if path in {"README.md", "docs/README.md", "docs/CONTINUITY.md"}:
        return "orientation"
    if path.startswith("docs/checkpoints/") or path.startswith("docs/research/"):
        return "historical_status"
    if path.startswith("docs/local_execution/validation/"):
        return "execution_evidence"
    if path.startswith("tests/"):
        return "verification"
    if path.startswith("schemas/"):
        return "source_schema"
    if path.startswith("tools/") or path.startswith("scripts/"):
        return "tooling"
    if path == "docs/DECISIONS.md" or path.startswith("docs/specifications/"):
        return "governing"
    if path.startswith("docs/"):
        return "orientation" if path.endswith("README.md") else "other"
    return "other"


def safe_path(path: str) -> bool:
    parts = PurePosixPath(path)
    return (
        bool(path) and not path.startswith("/") and "\\" not in path
        and ".." not in parts.parts and str(parts) == path
    )


def _fingerprint(rows: list[dict]) -> str:
    """Bind exact source status and identity without exposing paths publicly."""
    normalized = [
        {
            "path": r["path"], "git_blob_oid": r["git_blob_oid"],
            "sha256": r.get("sha256"), "bytes": r.get("bytes"),
            "family_hint": r["family_hint"], "visibility": r["visibility"],
            "flags": r["flags"], "status": r["status"],
        }
        for r in rows
    ]
    return sha256(json.dumps(
        normalized, sort_keys=True, ensure_ascii=True,
        separators=(",", ":"),
    ).encode("utf-8")).hexdigest()


def reconcile(
    primary: dict[str, tuple[str, bytes]],
    supplemental: dict,
    *, source_ref: str,
) -> tuple[dict, dict]:
    """Account for both rosters, with zero automatic source-world admissions.

    Fail closed for every duplicate, malformed record, unsupported status,
    missing hash, wrong blob length or incoherent reviewer inventory.
    """
    if not re.fullmatch("[0-9a-f]{40}", source_ref):
        raise ValueError("Unpinned source world")
    if supplemental.get("source_ref") != source_ref:
        raise ValueError("Historical source ref mismatch")
    if supplemental.get("admission_decision") != "NONE_ADMITTED_BY_LEXICAL_OR_PATH_CENSUS":
        raise ValueError("Unexpected source admission in historical inventory")
    original = supplemental.get("review_records")
    if not isinstance(original, list):
        raise ValueError("Missing historical inventory")
    if supplemental.get("review_record_count") != len(original):
        raise ValueError("Historical inventory count drift")
    if not primary:
        raise ValueError("Empty source candidate")
    source_rows: list[dict] = []
    present: set[str] = set()
    for path, (oid, raw) in sorted(primary.items()):
        if (
            not safe_path(path) or path in present
            or not re.fullmatch("[0-9a-f]{40}", oid)
            or not isinstance(raw, bytes)
            or sha1git(raw) != oid
        ):
            raise ValueError("Unqualified candidate source identity")
        present.add(path)
        source_rows.append({
            "path": path, "git_blob_oid": oid,
            "sha256": sha256(raw).hexdigest(), "bytes": len(raw),
            "family_hint": family(path),
            "visibility": "PRELIMINARY_CANDIDATE_UNQUALIFIED",
            "status": NO_ADMISSION,
            "flags": [],
        })
    for r in original:
        if not isinstance(r, dict):
            raise ValueError("Malformed historical inventory row")
        path, oid = r.get("path"), r.get("git_blob_oid")
        status = r.get("status")
        if (
            not isinstance(path, str) or not safe_path(path) or path in present
            or not isinstance(oid, str)
            or re.fullmatch("[0-9a-f]{40}", oid) is None
            or status not in {"REVIEW_ONLY_NOT_ADMITTED",
                              "NON_TEXT_UNSUPPORTED_NOT_ADMITTED"}
            or r.get("role_hint") != history._role(path)
            or not isinstance(r.get("review_flags"), list)
            or any(not isinstance(x, str) for x in r["review_flags"])
        ):
            raise ValueError("Overlapping, corrupt, or admitted historical record")
        if status == "REVIEW_ONLY_NOT_ADMITTED":
            if (
                not isinstance(r.get("sha256"), str)
                or re.fullmatch(r"[0-9a-f]{64}", r["sha256"]) is None
                or type(r.get("bytes")) is not int or r["bytes"] < 0
            ):
                raise ValueError("Missing text evidence identity")
        else:
            if "sha256" in r or "bytes" in r:
                raise ValueError("Unexpected unsupported content claim")
        present.add(path)
        source_rows.append({
            "path": path, "git_blob_oid": oid,
            "sha256": r.get("sha256"), "bytes": r.get("bytes"),
            "family_hint": family(path),
            "visibility": (
                "HISTORICAL_REVIEW_ONLY" if status == "REVIEW_ONLY_NOT_ADMITTED"
                else MODALITY_HOLD
            ),
            "status": NO_ADMISSION, "flags": sorted(set(r["review_flags"])),
        })
    source_rows.sort(key=lambda row: row["path"])
    if len(source_rows) != len(present):
        raise ValueError("Duplicate source world identity")
    groups: dict[str, Counter[str]] = defaultdict(Counter)
    for row in source_rows:
        groups[row["family_hint"]][row["visibility"]] += 1
    if not set(groups).issubset(ALL_FAMILIES):
        raise ValueError("Unspecified source family")
    coverage = {}
    for category, requirements in REQUIRED_CAPACITY.items():
        missing, blocked, candidate = [], [], []
        for need in requirements:
            if sum(groups[need].values()) == 0:
                missing.append(need)
            elif not groups[need]["PRELIMINARY_CANDIDATE_UNQUALIFIED"]:
                blocked.append(need)
            else:
                candidate.append(need)
        coverage[category] = {
            "required_family_count": len(requirements),
            "missing_family_hints": missing,
            "review_only_or_unsupported_family_hints": blocked,
            "unqualified_candidate_family_hints": candidate,
            "semantic_authority_coverage": "NOT_PROVEN",
            "task_answerability": "NOT_PROVEN",
        }
    visibility_counts = Counter(x["visibility"] for x in source_rows)
    total = len(source_rows)
    digest = _fingerprint(source_rows)
    ledger = {
        "schema_version": 1,
        "identifier": IDENTIFIER,
        "source_ref": source_ref,
        "classification": "OWNER_LOCAL_TASK_INDEPENDENT_NON_ADMISSION_LEDGER",
        "source_count": total,
        "preliminary_candidate_count": len(primary),
        "additional_review_count": len(original),
        "roster_sha256": digest,
        "source_records": source_rows,
        "notes": [
            "This ledger contains exact source paths and exposure hints; do not send it to a future fresh author.",
            "Every source remains NOT_ADMITTED regardless of lexical/path flags.",
            "Incomplete or unsupported representations remain unqualified, not irrelevant.",
            "Source-family presence does not prove governing truth, currentness, validation or task answerability.",
        ],
    }
    receipt = {
        "schema_version": 1,
        "identifier": IDENTIFIER,
        "source_ref": source_ref,
        "classification": "PUBLIC_SAFE_AGGREGATE_NO_SOURCE_ADMISSIONS",
        "complete_roster_records": total,
        "preliminary_candidate_unqualified": len(primary),
        "historical_review_only": visibility_counts["HISTORICAL_REVIEW_ONLY"],
        "unsupported_historical": visibility_counts[MODALITY_HOLD],
        "historical_total": len(original),
        "family_visibility_counts": {
            key: dict(sorted(count.items())) for key, count in sorted(groups.items())
        },
        "task_category_capacity_diagnostics": coverage,
        "roster_sha256": digest,
        "release_status": SCORING_HOLD,
        "world_status": ROSTER_NOT_FROZEN,
        "source_admissions": 0,
        "task_authorship": "NOT_STARTED",
        "evaluation": "NOT_STARTED",
        "interpretation": (
            "Task-independent path-family capacity only. This is no proof of "
            "semantic authority, source neutrality, complete answer context "
            "or task capacity. Separate independent source decisions required."
        ),
    }
    if receipt["preliminary_candidate_unqualified"] + receipt["historical_total"] != total:
        raise ValueError("Population accounting failure")
    return ledger, receipt


def sha1git(raw: bytes) -> str:
    from hashlib import sha1
    return sha1(b"blob " + str(len(raw)).encode("ascii") + b"\0" + raw).hexdigest()


def compute(repo: Path, *, pin: str = PIN) -> tuple[dict, dict]:
    repo = repo.resolve(strict=True)
    if pin != PIN:
        raise ValueError("Historical source pin changed")
    if not (repo / ".git").exists():
        raise ValueError("Not a Git checkout")
    initial = frontend.prior.source_window(repo, pin=pin)
    expanded, unsupported_media = frontend._frontend(repo, pin)
    if set(initial) & set(expanded):
        raise ValueError("Overlapping frontend candidate")
    candidate = {**initial, **expanded}
    audited = history.audit(repo, pin=pin)
    ledger, receipt = reconcile(candidate, audited, source_ref=pin)
    # The real census contains 406 and 2133. Abort rather than produce
    # misleading real-world metrics if historical assumptions drift.
    if (len(candidate), len(audited["review_records"])) != (406, 2133):
        raise ValueError("Historical candidate universe drift")
    if len(unsupported_media) != 4:
        raise ValueError("Historical frontend representation drift")
    return ledger, receipt


def emit(
    repo: Path, *, verify_only: bool = False,
    output_override: Path | None = None,
) -> dict:
    repo = repo.resolve(strict=True)
    if output_override is None:
        folder = (repo / OUTPUT).resolve()
    else:
        folder = output_override.resolve()
        if folder == repo or folder.is_relative_to(repo):
            raise ValueError("External output override must not point inside repository")
    ledger, receipt = compute(repo)
    raw = (json.dumps(ledger, sort_keys=True, ensure_ascii=True,
                      separators=(",", ":")) + "\n").encode("ascii")
    receipt_raw = (json.dumps(receipt, sort_keys=True, ensure_ascii=True,
                              indent=2) + "\n").encode("ascii")
    if verify_only:
        if (
            not (folder / LEDGER).is_file()
            or (folder / LEDGER).read_bytes() != raw
            or not (folder / RECEIPT).is_file()
            or (folder / RECEIPT).read_bytes() != receipt_raw
        ):
            raise ValueError("Source-world ledger or receipt not reproducible")
        print("SOURCE_WORLD_COVERAGE_REPRODUCIBILITY=PASS")
    else:
        if (folder / LEDGER).exists() or (folder / RECEIPT).exists():
            raise FileExistsError("Refusing to overwrite existing source-world audit")
        folder.mkdir(parents=True, exist_ok=True)
        with (folder / LEDGER).open("xb") as target:
            target.write(raw)
        with (folder / RECEIPT).open("xb") as target:
            target.write(receipt_raw)
    print(json.dumps(receipt, sort_keys=True))
    return receipt


if __name__ == "__main__":
    if len(sys.argv) not in (2, 3) or (
        len(sys.argv) == 3 and sys.argv[2] != "--verify-only"
    ):
        raise SystemExit("usage: python -m experiments.r0_p03_navigation_probe."
                         "source_world_coverage_gate REPO [--verify-only]")
    emit(Path(sys.argv[1]), verify_only=len(sys.argv) == 3)
