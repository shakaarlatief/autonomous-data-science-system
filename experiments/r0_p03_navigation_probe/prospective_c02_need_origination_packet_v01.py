"""Build one reproducible, new-cohort, source-free independent-author input.

The historical twelve candidate needs and all restricted case-level evidence
remain untouched and inaccessible. Only the previously inspected neutral
historical orientation and a newly versioned author brief are delivered.
The prospective evidence-ceiling commit is fixed before any C02 author output;
it does not itself admit any source or freeze the final scored corpus.

All author-visible text is screened by the existing neutral-input guard.
Owner-private question outputs must remain outside the public repository.
"""
from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path
import sys
from zipfile import ZipFile
from io import BytesIO

from experiments.r0_p03_navigation_probe import (
    neutral_need_origination_packet as v1,
    neutral_need_origination_packet_v02 as v2,
)

IDENTIFIER = "R0_P03_C02_FRESH_NEED_ORIGINATION_INPUT_V01"
COHORT = "R0_P03_PROSPECTIVE_C02_V01_NOT_ADMITTED"
HISTORICAL_CONTEXT_SHA256 = v2.V01_CONTEXT_SHA256
EVIDENCE_CEILING = "47ed6344a9153dcf366769e95722840fbf1a8f8b"
AUTHOR_BRIEF = "PROSPECTIVE_C02_INDEPENDENT_NEED_AUTHOR_BRIEF_V01.md"
ARCHIVE_NAME = "R0_P03_C02_FRESH_NEED_ORIGINATION_INPUT_V01.zip"
FOLDER = Path(".venv") / ".r0_p03_c02_independent_need_input_v01"
UPLOAD_DIR = Path(".venv") / "R0_P03_C02_SELECT_ONE_INPUT_FOR_UPLOAD"
RECEIPT_NAME = "R0_P03_C02_NEED_INPUT_V01.safe-receipt.json"
MANIFEST_NAME = "R0_P03_C02_NEED_INPUT_V01.coordinator_provenance.json"
REQUIRED_BRIEF = (
    "fresh, independent contributor",
    "up to twelve distinct",
    "four areas",
    "NOT_YET_ADJUDICATED",
    "NEED_PROPOSALS_RESTRICTED.md",
    "NEED_ORIGINATION_SAFE_RECEIPT.md",
    "A different independent reviewer",
    "You cannot claim cross-cohort distinctness",
    "not convenient questions",
    "human owner must download",
    "SCORING=NOT_STARTED",
)


def content_and_manifest(repo: Path) -> tuple[dict[str, bytes], dict]:
    """Authenticate the old neutral derivative and validate prospective input."""
    original, previous = v2.contents_and_provenance(repo)
    if sha256(original["NEUTRAL_CONTEXT.md"]).hexdigest() != HISTORICAL_CONTEXT_SHA256:
        raise ValueError("Historical neutral context identity mismatch")
    if v1.git(repo, "rev-parse", "--verify", EVIDENCE_CEILING + "^{commit}").strip().decode("ascii") != EVIDENCE_CEILING:
        raise ValueError("Prospective source ceiling not present as exact immutable commit")
    author = (Path(__file__).resolve().parent / AUTHOR_BRIEF).read_bytes()
    texts = {"AUTHOR_BRIEF.md": author, "NEUTRAL_CONTEXT.md": original["NEUTRAL_CONTEXT.md"]}
    v1.check_author_texts(texts)
    decoded = author.decode("utf-8")
    if not all(item in decoded for item in REQUIRED_BRIEF):
        raise ValueError("Prospective author brief incomplete")
    manifest = {
        "identifier": IDENTIFIER,
        "cohort": COHORT,
        "explicit_owner_decision": "ACCEPT_PROSPECTIVE_INDEPENDENT_COHORT_ROUTE",
        "decision_date": "2026-11-12",
        "old_historical_cohort": "PRESERVED_6_PROVISIONAL_6_MATERIAL_HOLD",
        "prior_author_packet_v02": v2.IDENTIFIER,
        "historical_source_orientation_pin": v1.PIN,
        "historical_context_sha256": HISTORICAL_CONTEXT_SHA256,
        "prospective_source_evidence_ceiling_before_any_new_question": EVIDENCE_CEILING,
        "final_source_corpus": "NOT_QUALIFIED_OR_ADMITTED",
        "source_provenance_checked": previous["verified_source_provenance"],
        "author_visible_sources": 0,
        "author_visible_question_or_answer_material": 0,
        "author_visible_files_sha256": {k: sha256(v).hexdigest() for k, v in sorted(texts.items())},
        "protected_old_cohort_case_text": "NOT_OPENED_OR_TRANSMITTED",
        "new_questions": "NOT_ORIGINATED",
        "role_exposure_qualification": "PENDING_ACTUAL_INDEPENDENT_AUTHOR_INTAKE",
        "cross_cohort_duplicate_adjudication": "PENDING_SEPARATE_PROTECTED_REVIEW",
        "source_admissions": 0,
        "gold": "NONE",
        "scored_tasks": 0,
        "b0_b4_scores": "NONE",
        "owner_private_output_access": "NOT_PLATFORM_ENFORCED",
    }
    return texts, manifest


def build(repo: Path, *, verify_only: bool = False) -> dict:
    """Rebuild or create exact immutable local and one-file owner upload artifacts."""
    repo = repo.resolve(strict=True)
    if not (repo / ".git").is_dir():
        raise ValueError("Expected actual source repository")
    texts, manifest = content_and_manifest(repo)
    raw = v1.zip_data(texts)
    with ZipFile(BytesIO(raw)) as z:
        if z.testzip() is not None or z.namelist() != sorted(texts):
            raise ValueError("Invalid ZIP member roster/CRC")
        if {n: z.read(n) for n in z.namelist()} != texts:
            raise ValueError("ZIP member readback mismatch")
    receipt = {
        "identifier": IDENTIFIER,
        "cohort": COHORT,
        "archive_filename": ARCHIVE_NAME,
        "archive_bytes": len(raw),
        "archive_sha256": sha256(raw).hexdigest(),
        "source_context_sha256": HISTORICAL_CONTEXT_SHA256,
        "prospective_evidence_ceiling": EVIDENCE_CEILING,
        "author_files": sorted(texts),
        "author_originals": 0,
        "old_protected_questions": 0,
        "new_proposals": 0,
        "independent_actor": "NOT_STARTED",
        "source_admissions": 0,
        "reference_gold": "NONE",
        "scored_tasks": "NONE",
        "arm_scores": "NONE",
    }
    files = {
        repo / FOLDER / ARCHIVE_NAME: raw,
        repo / FOLDER / RECEIPT_NAME: v1.stable_json(receipt),
        repo / FOLDER / MANIFEST_NAME: v1.stable_json(manifest),
        repo / UPLOAD_DIR / ARCHIVE_NAME: raw,
    }
    if verify_only:
        for name, expected in files.items():
            if not name.is_file() or name.read_bytes() != expected:
                raise ValueError("Prospective author packet not byte reproducible: " + name.name)
        if {p.name for p in (repo / UPLOAD_DIR).iterdir()} != {ARCHIVE_NAME}:
            raise ValueError("Upload folder must contain exactly one packet")
        print("PROSPECTIVE_C02_NEED_PACKET_REPRODUCIBILITY=PASS")
    else:
        if any(p.exists() or p.is_symlink() for p in files):
            raise FileExistsError("Refusing to overwrite prospective independent input")
        if (repo / UPLOAD_DIR).exists() and any((repo / UPLOAD_DIR).iterdir()):
            raise FileExistsError("Refusing nonempty author upload folder")
        (repo / FOLDER).mkdir(parents=True, exist_ok=True)
        (repo / UPLOAD_DIR).mkdir(parents=True, exist_ok=True)
        for path, content in files.items():
            with path.open("xb") as stream:
                stream.write(content)
            if path.read_bytes() != content:
                raise ValueError("Owner input write/readback mismatch")
    print(json.dumps(receipt, sort_keys=True))
    return receipt


if __name__ == "__main__":
    if len(sys.argv) not in (2, 3) or (len(sys.argv) == 3 and sys.argv[2] != "--verify-only"):
        raise SystemExit("usage: python -m experiments.r0_p03_navigation_probe.prospective_c02_need_origination_packet_v01 REPO [--verify-only]")
    build(Path(sys.argv[1]), verify_only=len(sys.argv) == 3)
