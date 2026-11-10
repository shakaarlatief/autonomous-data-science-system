"""Reproducible V02 neutral need-origination handoff after a safe V01 stop.

V01's original archive remains immutable evidence of an over-restrictive
author-role admission instruction. V02 changes ONLY the prospective author
instructions for tool availability and practical owner-held output custody.
It retains the byte-identical source-free historical orientation.
"""
from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path
import sys

from experiments.r0_p03_navigation_probe import neutral_need_origination_packet as v1

IDENTIFIER = "R0_P03_FRESH_NEED_ORIGINATION_INPUT_V02"
FOLDER = Path(".venv") / ".r0_p03_fresh_need_origination_v02"
ARCHIVE_NAME = "R0_P03_FRESH_NEED_ORIGINATION_INPUT_V02.zip"
RECEIPT_NAME = "R0_P03_FRESH_NEED_ORIGINATION_V02.safe-receipt.json"
MANIFEST_NAME = "R0_P03_FRESH_NEED_ORIGINATION_V02.coordinator_provenance.json"
V01_CONTEXT_SHA256 = "ebb835437ab5c42b913bc76a3da6ceb8fae02af230e7ab2176385bc3f82af730"
V01_ARCHIVE_SHA256 = "56c3c6fe3955ff8746bedb426df23e953555a6a67dce16d6b04d63a4ea4c25be"


def contents_and_provenance(repo: Path) -> tuple[dict[str, bytes], dict]:
    source = Path(__file__).resolve().parent
    # The originals are verified again under the same historical exact pin,
    # not reinterpreted or disclosed in the author packet.
    evidence = v1.verify_originals(repo)
    original_context = (source / "NEED_ORIGINATION_NEUTRAL_CONTEXT_V01.md").read_bytes()
    if sha256(original_context).hexdigest() != V01_CONTEXT_SHA256:
        raise ValueError("Original neutral context was mutated")
    author = (source / "NEED_ORIGINATION_INDEPENDENT_AUTHOR_BRIEF_V02.md").read_bytes()
    texts = {"AUTHOR_BRIEF.md": author, "NEUTRAL_CONTEXT.md": original_context}
    v1.check_author_texts(texts)
    required = (
        "available but unused general-purpose capability",
        "not by itself disqualifying",
        "Stop without originating proposals",
        "human owner must download",
        "cryptographically enforced owner-only access",
        "If you cannot create the two separate downloadable files",
    )
    t = author.decode("utf-8")
    if not all(s in t for s in required):
        raise ValueError("V02 prospectively corrected boundary is incomplete")
    manifest = {
        "identifier": IDENTIFIER,
        "prior_attempt": "V01_STOPPED_ZERO_NEEDS_NO_EXTERNAL_ACCESS",
        "prior_archive_sha256": V01_ARCHIVE_SHA256,
        "change": "PROSPECTIVE_AUTHOR_BRIEF_ONLY",
        "neutral_context_sha256_unchanged": V01_CONTEXT_SHA256,
        "original_source_pin": v1.PIN,
        "verified_source_provenance": evidence,
        "delivered_original_source_files": 0,
        "delivered_source_specific_answers": 0,
        "delivered_file_count": 2,
        "author_input_hashes": {
            path: sha256(raw).hexdigest() for path, raw in sorted(texts.items())
        },
        "independent_actor_exposure": "MUST_BE_ACTUALLY_DECLARED",
        "semantic_isolation": "NOT_FORMALLY_CERTIFIED",
        "owner_only_platform_access": "NOT_CLAIMED",
        "owner_transfer_authorization": "OWNER_ACTION_REQUIRED",
        "source_admissions": 0,
        "scored_tasks": 0,
        "b0_b4_scores": "NONE",
    }
    return texts, manifest


def build(repo: Path, *, verify_only: bool = False) -> dict:
    repo = repo.resolve(strict=True)
    if not (repo / ".git").is_dir():
        raise ValueError("Expected trusted Git repository")
    texts, manifest = contents_and_provenance(repo)
    archive = v1.zip_data(texts)
    receipt = {
        "identifier": IDENTIFIER,
        "archive_filename": ARCHIVE_NAME,
        "archive_bytes": len(archive),
        "archive_sha256": sha256(archive).hexdigest(),
        "v01_stopped_not_mutated": True,
        "neutral_context_unchanged": True,
        "author_visible_entries": sorted(texts),
        "author_visible_source_originals": 0,
        "original_source_pin": v1.PIN,
        "new_actual_author": "NOT_STARTED",
        "owner_upload": "NOT_PERFORMED",
        "owner_only_file_access": "NOT_CLAIMED",
        "task_proposals": 0,
        "scored_tasks": 0,
        "source_admissions": 0,
        "arm_scores": "NONE",
    }
    folder = repo / FOLDER
    paths = {
        folder / ARCHIVE_NAME: archive,
        folder / RECEIPT_NAME: v1.stable_json(receipt),
        folder / MANIFEST_NAME: v1.stable_json(manifest),
    }
    if verify_only:
        for path, raw in paths.items():
            if not path.is_file() or path.read_bytes() != raw:
                raise ValueError(f"V02 artifact not exactly reproducible: {path.name}")
        print("NEUTRAL_NEED_ORIGINATION_V02_REPRODUCIBILITY=PASS")
    else:
        if any(p.exists() for p in paths):
            raise FileExistsError("Refusing to overwrite V02 author handoff")
        folder.mkdir(parents=True, exist_ok=True)
        for path, raw in paths.items():
            with path.open("xb") as f:
                f.write(raw)
    print(json.dumps(receipt, sort_keys=True))
    return receipt


if __name__ == "__main__":
    if len(sys.argv) not in (2, 3) or (
        len(sys.argv) == 3 and sys.argv[2] != "--verify-only"
    ):
        raise SystemExit("usage: python -m experiments.r0_p03_navigation_probe."
                         "neutral_need_origination_packet_v02 REPO [--verify-only]")
    build(Path(sys.argv[1]), verify_only=len(sys.argv) == 3)
