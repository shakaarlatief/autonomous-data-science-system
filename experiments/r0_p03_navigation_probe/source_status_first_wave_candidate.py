"""Prepare a bounded, exact-Git first source-status review wave, never an author packet.

The output is a non-scored owner-local REVIEW_ONLY candidate, selected without
tasks, old gold, arm results, semantic inclusion decisions, or manual source
cherry-picking. Each supported role contributes at most one lexically flagged
and one unflagged textual carrier. This coverage exercise is intentionally not
a statistically representative sample or a prospective 60/20 cohort.

Potentially answer-bearing original source bytes belong in the ignored local
staging ZIP, not public Git, stdout, a model coordinator, or the blind author.
Delivery to any external reviewer requires a separate owner authorization.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import sys

from experiments.r0_p03_navigation_probe import (
    primary_author_historical_evidence_review_candidate as historical,
)

PIN = historical.expanded.prior.base.PIN
ROLES = (
    "historical_checkpoint_evidence",
    "historical_research_and_decision_basis",
    "execution_validation_evidence",
    "execution_or_build_tool",
    "test_source_or_fixture",
    "machine_schema",
)
BANDS = ("flagged", "unflagged")
MAX_SOURCE_BYTES = 48 * 1024
OUTPUT_DIR = Path(".venv") / ".r0_p03_source_status_wave0"
ARCHIVE_NAME = "R0_P03_SOURCE_STATUS_FIRST_WAVE_REVIEW_ONLY.zip"
RECEIPT_NAME = "R0_P03_SOURCE_STATUS_FIRST_WAVE.receipt.json"
ID = "R0_P03_FIRST_SOURCE_STATUS_REVIEW_WAVE_CANDIDATE_V1"


def select(records: list[dict]) -> tuple[list[dict], list[dict]]:
    """Return deterministic strata representatives and explicit held strata.

    Only text that is already REVIEW_ONLY_NOT_ADMITTED is eligible. Hash order
    depends solely on the exact original path/blob, pinned revision and stratum.
    File-size limits are declared in advance to control first-wave inspection.
    An empty stratum stays held; neither a different role nor an unsuitable
    oversized file is silently substituted. No source semantics are inferred.
    """
    chosen = []
    holds = []
    for role in ROLES:
        for band in BANDS:
            matches = [
                r for r in records
                if r.get("role_hint") == role
                and r.get("status") == "REVIEW_ONLY_NOT_ADMITTED"
                and bool(r.get("review_flags")) == (band == "flagged")
                and isinstance(r.get("bytes"), int)
                and 0 <= r["bytes"] <= MAX_SOURCE_BYTES
            ]
            if not matches:
                holds.append({"role_hint": role, "band": band,
                              "state": "NO_SIZE_ELIGIBLE_REVIEW_ONLY_RECORD"})
                continue
            def order(r: dict) -> tuple[str, str]:
                token = "\0".join((ID, PIN, role, band, r["path"],
                                    r["git_blob_oid"])).encode("utf-8")
                return (hashlib.sha256(token).hexdigest(), r["path"])
            chosen.append(min(matches, key=order))
    if len({r["path"] for r in chosen}) != len(chosen):
        raise ValueError("Duplicate source across strata")
    return chosen, holds


def build(repo: Path, *, verify_only: bool = False) -> dict:
    repo = repo.resolve(strict=True)
    source = historical.audit(repo, pin=PIN)
    if source["source_ref"] != PIN or source["review_record_count"] != 2133:
        raise ValueError("Historical population drift")
    selected, holds = select(source["review_records"])
    contents = {}
    manifest_rows = []
    for entry in selected:
        path = entry["path"]
        if path.startswith("/") or "\\" in path or ".." in Path(path).parts:
            raise ValueError("Unsafe exact source path")
        raw = historical.expanded.prior.base.git(repo, "show",
                                                  f"{PIN}:{path}")
        oid = hashlib.sha1(
            b"blob " + str(len(raw)).encode("ascii") + b"\0" + raw
        ).hexdigest()
        if (oid != entry["git_blob_oid"] or len(raw) != entry["bytes"]
                or hashlib.sha256(raw).hexdigest() != entry["sha256"]):
            raise ValueError("Pinned source blob identity mismatch")
        contents["sources/" + path] = raw
        manifest_rows.append({
            "path": path,
            "git_blob_oid": oid,
            "sha256": entry["sha256"],
            "bytes": len(raw),
            "role_hint_not_authority": entry["role_hint"],
            "lexical_risk_flags_not_verdict": entry["review_flags"],
            "admission": "REVIEW_ONLY_NOT_ADMITTED",
        })
    metadata = {
        "schema_version": 1,
        "identifier": ID,
        "source_ref": PIN,
        "classification": "OWNER_LOCAL_FIRST_WAVE_REVIEW_INPUT_NOT_AUTHOR_PACKET",
        "selection_rule": "one_SHA256_ranked_size_bounded_record_per_role_x_lexical_band",
        "max_source_bytes": MAX_SOURCE_BYTES,
        "population_review_records": source["review_record_count"],
        "population_source_admissions": 0,
        "selected_count": len(manifest_rows),
        "unrepresented_strata": holds,
        "source_manifest": manifest_rows,
        "instructions": [
            "For independently qualified source-status review only, not a blind author.",
            "Inspect original context and source status. All candidate outputs remain HOLD.",
            "A lexical flag is not a contamination verdict. Its absence is not safe release.",
            "Return restricted source-specific reasoning only to an owner-approved private destination.",
            "No historical source is authorized for external transfer by constructing this ZIP.",
            "Neither source eligibility nor task answerability nor 60/20 membership is decided.",
        ],
    }
    data = (json.dumps(metadata, sort_keys=True, ensure_ascii=False,
                       indent=2) + "\n").encode("utf-8")
    contents["SOURCE_MANIFEST.json"] = data
    archive = historical.expanded.prior.base.deterministic_zip(contents)
    receipt = {
        "identifier": ID,
        "source_ref": PIN,
        "classification": "OWNER_LOCAL_REVIEW_ONLY_NOT_AUTHOR_ADMITTED",
        "population_review_records": source["review_record_count"],
        "selected_text_carriers": len(selected),
        "unrepresented_strata": len(holds),
        "manifest_sha256": hashlib.sha256(data).hexdigest(),
        "zip_bytes": len(archive),
        "zip_sha256": hashlib.sha256(archive).hexdigest(),
        "historical_source_delivery": "NOT_AUTHORIZED",
        "scoring": "NOT_STARTED",
    }
    out = repo / OUTPUT_DIR
    zip_path, receipt_path = out / ARCHIVE_NAME, out / RECEIPT_NAME
    if verify_only:
        if (not zip_path.is_file() or zip_path.read_bytes() != archive
                or not receipt_path.is_file()
                or json.loads(receipt_path.read_text("utf-8")) != receipt):
            raise ValueError("First-wave saved source/receipt reproducibility mismatch")
        print("SOURCE_STATUS_FIRST_WAVE_REPRODUCIBILITY=PASS")
    else:
        if zip_path.exists() or receipt_path.exists():
            raise FileExistsError("Refuse to overwrite first-wave source review")
        out.mkdir(parents=True, exist_ok=True)
        zip_path.write_bytes(archive)
        receipt_path.write_text(json.dumps(receipt, sort_keys=True,
                             indent=2) + "\n", encoding="utf-8", newline="\n")
    # Safe aggregate: no selected paths, flags by individual file, source text,
    # old answer labels, or task-specific inference.
    print(json.dumps(receipt, sort_keys=True))
    return receipt


if __name__ == "__main__":
    if len(sys.argv) not in (2, 3) or (
        len(sys.argv) == 3 and sys.argv[2] != "--verify-only"
    ):
        raise SystemExit("usage: python -m experiments.r0_p03_navigation_probe."
                         "source_status_first_wave_candidate REPO [--verify-only]")
    build(Path(sys.argv[1]), verify_only=len(sys.argv) == 3)
