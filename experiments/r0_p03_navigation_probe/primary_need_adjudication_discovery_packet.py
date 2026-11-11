"""Exact pinned-Git source discovery INDEX for a separate need-source judge.

The independent reviewer, not this exposed coordinator, receives private
candidate wording in owner-controlled delivery. This builder NEVER accepts,
reads or stores those questions. Its index is task-neutral, contains only
unqualified historical source locator identities, and is never a source
release, reference answer, eligible corpus, or scored arm.

Original source contents are intentionally NOT bundled. A source-specific
non-arm reference adjudicator may request exact indexed evidence via narrow
read-only raw Git fetches at the historical pin. If actual access is not
available, no semantic closure may be claimed. Old comparison/gold and known
risk-flagged sources are excluded even as locators.
"""
from __future__ import annotations

from collections import Counter
from hashlib import sha256
from io import BytesIO
import json
from pathlib import Path
import re
import sys
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo

from experiments.r0_p03_navigation_probe import source_world_coverage_gate as world

IDENTIFIER = "R0_P03_PRIVATE_NEED_ADJUDICATION_DISCOVERY_INDEX_V01"
FOLDER = Path(".venv") / ".r0_p03_need_adjudication_discovery_v01"
ARCHIVE_NAME = "R0_P03_NEED_ADJUDICATION_DISCOVERY_V01.zip"
RECEIPT_NAME = "R0_P03_NEED_ADJUDICATION_DISCOVERY.safe-receipt.json"
FIXED_TIME = (2026, 1, 1, 0, 0, 0)
# Explicit narrow old-scoring and experimental-design path terms. These are
# necessary lexical exclusions, not sufficient substantive contamination tests.
PATH_EXCLUDE = re.compile(
    r"(?:r0[_-]?p0?3|navigation[_-]?scenarios|corpus[_-]?annotations|"
    r"w5[_-]?t1|w5[_-]?subject|subject[_-]?vocab|"
    r"(?:^|/)docs/research/(?:21[0-8])_|"
    r"(?:^|/)docs/local_execution/validation/(?:2[4-6][0-9])_r0[_-]p0?3)",
    re.I,
)
ARCHIVE_BRIEF = """# Independent need-specific source and authority adjudication

You are a NEW non-arm reference/evidence adjudicator, distinct from the
independent need-originating actor and exposed R0-P03 engineering coordinator.

## Actual inputs and independence

The human owner may provide this exact discovery ZIP and the separately
owner-retained NEED_PROPOSALS_RESTRICTED.md. These twelve candidate requests
are unadjudicated, NOT twelve preaccepted scored questions. Do not upload or
publish them in any public repository or share with arm authors/evaluators.
Before opening them, declare your relevant actual prior exposure, available
tools, context, limitations and allowed source-access route. No previous W5
gold, P03 comparisons, old reference answers or project design solutions may
be consulted. Available-but-unused generic tools are not proof of exposure.

This archive includes an INDEX.json of path@blob@SHA-256 historical
source LOCATORS ONLY. It has ZERO original source bodies, zero proposal
wording and no reference answers. The index is a subset of a 2,539-entry
historical source census, chosen by task-independent exclusion of explicit
comparison/answer risk flags and path markers. A listed entry is NEVER
admitted, independently authenticated operative authority or a required
source. Omitted records are not automatically irrelevant or inadmissible.
The old 80-source author release remains on HOLD.

## Direct source access, not a new guessed corpus

For one candidate information need at a time, discover possible evidence by
inspecting the indexed source paths and requesting exact original pinned
file bytes for materials actually relevant to the need. The ONLY network
read permitted for original content is a direct read-only raw Git URL of the
form:

https://raw.githubusercontent.com/shakaarlatief/autonomous-data-science-system/c57556a8bf993a1d327e9197acb7b7c745071cd8/<INDEXED_EXACT_PATH>

Use only exact paths from INDEX.json. Do not search the web, follow unrelated
links, switch to dynamic HEAD, query old B1/W5/P03 comparison results, or
use other repositories/connected apps. Verify actual fetched byte lengths
and SHA-256 against the index, where technically possible. A URL or hash
without actually reading its original contents is NOT substantive evidence.
Record any inability to access/verify a source. If this restricted direct
fetch route is unavailable, STOP the factual/source-closure assessment and
report that blocker; do not manufacture answers or call source names proof.

This index is for source **discovery**, not an all-needed source universe:
if material original evidence is absent, record an exact private
MISSING_EVIDENCE/HOLD request. DO NOT bypass the permitted path list by
accessing old experimental/gold files. A separately owner-scoped exact
original evidence handoff is required for off-index witnesses.

## Actual adjudication

Inspect the twelve original proposed needs WITHOUT rewriting them to make
answers easy. For each, independently assess origin/exposure quality,
meaningful distinctness, category match, historical time scope, whether the
claim requires current versus historical authority, minimum original
source/revision/span closure, counterevidence, actual implementation versus
proposal, and negative/validation/rollback evidence. Determine:
SOURCE_CLOSED, MATERIAL_HOLD or UNANSWERABLE_AS_STATED, plus any
INDEPENDENCE_OR_CONTAMINATION_STOP. Do not silently narrow, substitute
another question or make a historical report into a verified execution.
An exact source passage is not automatically governing truth; all sources
remain NOT_ADMITTED until a separate qualification decision.

Do not claim a closed set, independent gold, scoring readiness or all twelve
answerable merely from the ZIP index. The R0-P03 scientific threshold remains
3 genuinely qualified needs per each of four categories, then separate
reference custody, fair common source selection and B0-B4 execution.

## Outputs and role segregation

Produce two separately downloadable Markdown files:

1. NEED_SOURCE_ADJUDICATION_RESTRICTED.md: owner-private per-need full
   wording/identity, source passages and exact blob/hash/span evidence,
   contradictions, missing original witnesses, rationale, specific decision,
   contamination and limitations. Not for public Git or future arm authors.
2. NEED_SOURCE_ADJUDICATION_AGGREGATE.md: source-free counts by category and
   disposition, actual sources fetched/verified, missing evidence family
   types, general contamination/role constraints, all file sizes+SHA-256 and
   conclusion. No candidate question wording, source-specific names/paths,
   relevant-source labels, source quotations, hidden answers or private
   owner-folder locations.

If the requested evidence is unavailable or a necessary eligibility boundary
would be crossed, give a precise material HOLD, not a convenient completion.
Do NOT assume this chat platform guarantees owner-only downloaded files.
The owner must download and maintain the restricted report separately.
Do not act as a scored agent, arm author or blind evaluator afterward.
"""


def canonical(value: object) -> bytes:
    return (json.dumps(
        value, sort_keys=True, ensure_ascii=True, separators=(",", ":")
    ) + "\n").encode("ascii")


def indexed(ledger: dict) -> list[dict]:
    if (ledger["source_ref"] != world.PIN or ledger["source_count"] != 2539
            or ledger["roster_sha256"] != world._fingerprint(
                ledger["source_records"])):
        raise ValueError("Historical source census identity not qualified")
    out: list[dict] = []
    for row in ledger["source_records"]:
        if (row["visibility"] == world.MODALITY_HOLD
                or row["flags"] or PATH_EXCLUDE.search(row["path"])):
            continue
        if (row["status"] != world.NO_ADMISSION
                or not world.safe_path(row["path"])
                or not isinstance(row["sha256"], str)
                or not isinstance(row["bytes"], int)):
            raise ValueError("Corrupt non-admission source locator")
        out.append({
            "path": row["path"],
            "git_blob_oid": row["git_blob_oid"],
            "sha256": row["sha256"],
            "bytes": row["bytes"],
            "path_family_hint_not_authority": row["family_hint"],
            "qualification": "NOT_ADMITTED_REVIEW_ONLY_LOCATOR",
        })
    out.sort(key=lambda r: r["path"])
    if not out or len(out) != len({r["path"] for r in out}):
        raise ValueError("Empty or duplicate source locator index")
    return out


def zip_bytes(members: dict[str, bytes]) -> bytes:
    output = BytesIO()
    with ZipFile(output, "w") as z:
        for name, raw in sorted(members.items()):
            info = ZipInfo(name, date_time=FIXED_TIME)
            info.compress_type = ZIP_DEFLATED
            info.create_system = 3
            info.external_attr = 0o100644 << 16
            z.writestr(info, raw)
    return output.getvalue()


def build(repo: Path, *, verify_only: bool = False) -> dict:
    repo = repo.resolve(strict=True)
    if not (repo / ".git").is_dir():
        raise ValueError("A real original-source Git repository is required")
    ledger, _ = world.compute(repo)
    records = indexed(ledger)
    counts = dict(sorted(Counter(
        x["path_family_hint_not_authority"] for x in records
    ).items()))
    index = {
        "schema_version": 1,
        "identifier": IDENTIFIER,
        "historical_git_revision": world.PIN,
        "full_historical_records": ledger["source_count"],
        "historical_roster_sha256": ledger["roster_sha256"],
        "index_record_count": len(records),
        "excluded_or_unsupported_count": ledger["source_count"] - len(records),
        "exact_source_bytes_in_archive": 0,
        "private_candidate_questions_in_archive": 0,
        "known_scored_gold_or_comparison_in_archive": 0,
        "index_entry_semantic_status": "NOT_ADMITTED_AND_NOT_ALL_POSSIBLE_EVIDENCE",
        "explicit_exclusion_is_not_semantic_evidence": True,
        "files": records,
    }
    index_raw = canonical(index)
    members = {
        "INDEX.json": index_raw,
        "ADJUDICATOR_BRIEF.md": ARCHIVE_BRIEF.encode("utf-8"),
    }
    archive = zip_bytes(members)
    receipt = {
        "identifier": IDENTIFIER,
        "filename": ARCHIVE_NAME,
        "archive_bytes": len(archive),
        "archive_sha256": sha256(archive).hexdigest(),
        "index_sha256": sha256(index_raw).hexdigest(),
        "indexed_source_paths": len(records),
        "total_historical_source_records": ledger["source_count"],
        "excluded_or_unsupported_source_records": ledger["source_count"] - len(records),
        "index_families": counts,
        "actual_original_source_bodies_delivered": 0,
        "private_questions_delivered": 0,
        "source_admissions": 0,
        "source_closure": "NOT_EXAMINED",
        "source_reader": "INDEPENDENT_REVIEWER_MUST_EXACT_GIT_FETCH_AND_VERIFY",
        "independent_reference_review": "NOT_STARTED",
        "scored_tasks": "NONE",
        "arm_results": "NONE",
    }
    folder = repo / FOLDER
    files = {
        folder / ARCHIVE_NAME: archive,
        folder / RECEIPT_NAME: canonical(receipt),
    }
    if verify_only:
        if any(not path.is_file() or path.read_bytes() != raw
               for path, raw in files.items()):
            raise ValueError("Source discovery index does not byte-rebuild")
        print("PRIVATE_NEED_SOURCE_DISCOVERY_INDEX_REPRODUCIBILITY=PASS")
    else:
        if any(path.exists() for path in files):
            raise FileExistsError("No overwrite of original adjudicator index")
        folder.mkdir(parents=True, exist_ok=True)
        for path, raw in files.items():
            with path.open("xb") as f:
                f.write(raw)
    print(json.dumps(receipt, sort_keys=True))
    return receipt


if __name__ == "__main__":
    if len(sys.argv) not in (2, 3) or (
        len(sys.argv) == 3 and sys.argv[2] != "--verify-only"
    ):
        raise SystemExit(
            "usage: python -m experiments.r0_p03_navigation_probe."
            "primary_need_adjudication_discovery_packet . [--verify-only]"
        )
    build(Path(sys.argv[1]), verify_only=len(sys.argv) == 3)
