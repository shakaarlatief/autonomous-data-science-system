"""Construct non-scored, source-bound intake metadata for an independent P03 annotator.

This module reads ONLY immutable historical Git object bytes and deliberately
transfers no historical B1 annotation/membership, old required-source sets,
distractor sets, scenario-to-source mappings, or per-arm expected outputs into
the fresh annotator intake. It produces historical world source identities and
nine *theme hints*, not nine fully specified questions or their neutral gold.

No author independence can be established by a local script. Reviewer exposure,
role conflicts, answer justification, and secure separation of private gold
must be qualified independently before R0-P03's exact fixture freeze.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
from pathlib import Path
from typing import Any

INPUT_REF = "54b603c5fe550af963aac808b1fe7cacb516c6d4"
HISTORICAL_REF = "4b94ffe183ff7af72cef6ee7492b4ba2f30c11ef"
SCENARIO_PATH = "experiments/project_knowledge_subject_navigation_t1_v02/navigation_scenarios_v02.json"
ANNOTATIONS_PATH = "experiments/project_knowledge_subject_navigation_t1_v02/corpus_annotations_v02.json"
FULL_SHA = re.compile(r"[0-9a-f]{40}\Z")
THEME_SLUG = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*\Z")


def git_file(repository: Path, source_ref: str, path: str) -> bytes:
    if not FULL_SHA.fullmatch(source_ref):
        raise ValueError("Source ref must be a full immutable lowercase Git commit ID")
    if not path or path.startswith("/") or ".." in path.split("/"):
        raise ValueError("Invalid repository-relative source path")
    return subprocess.run(
        ["git", "show", f"{source_ref}:{path}"],
        cwd=repository, capture_output=True, check=True,
    ).stdout


def git_blobs(repository: Path, source_ref: str) -> dict[str, str]:
    if not FULL_SHA.fullmatch(source_ref):
        raise ValueError("Historical ref must be full immutable Git commit ID")
    result = subprocess.run(
        ["git", "ls-tree", "-r", "-z", source_ref],
        cwd=repository, capture_output=True, check=True,
    )
    blobs = {}
    for record in result.stdout.split(b"\0"):
        if not record:
            continue
        meta, name = record.split(b"\t", 1)
        mode, kind, oid = meta.decode("ascii").split(" ")
        if kind == "blob" and mode in {"100644", "100755"}:
            blobs[name.decode("utf-8")] = oid
    return blobs


def build_intake(repository: Path, input_ref: str = INPUT_REF) -> dict[str, Any]:
    """Emit evidence-world roster and theme hints only, never historical gold.

    The historical scenario and annotation JSON files are consulted **only**
    for their scenario IDs, corpus source paths and historical source ref.
    No original labels, membership arrays or relevance decisions leave
    this routine. A future fresh neutralizer must explicitly admit the nine
    themes as information needs, not mechanically assume they are questions.
    """
    raw_scenarios = git_file(repository, input_ref, SCENARIO_PATH)
    raw_annotations = git_file(repository, input_ref, ANNOTATIONS_PATH)
    scenarios = json.loads(raw_scenarios)
    annotations = json.loads(raw_annotations)

    historical = scenarios.get("source_boundary")
    if historical != HISTORICAL_REF or annotations.get("source_boundary") != historical:
        raise ValueError("Unexpected historical source boundary")
    original_scenarios = scenarios.get("scenarios")
    original_annotations = annotations.get("annotations")
    if not isinstance(original_scenarios, list) or len(original_scenarios) != 9:
        raise ValueError("Expected exactly the historical nine distinct themes")
    if not isinstance(original_annotations, list) or len(original_annotations) != 65:
        raise ValueError("Expected exactly the historical 65 source carriers")

    themes: list[dict[str, str]] = []
    for position, record in enumerate(original_scenarios, 1):
        identifier = record["id"]
        if not THEME_SLUG.fullmatch(identifier):
            raise ValueError("Invalid legacy theme identifier")
        themes.append({
            "case_id": f"legacy-{position:02d}",
            "neutral_theme_hint": identifier.replace("-", " "),
            "question_status": "NOT_YET_AUTHORED_BY_FRESH_NEUTRALIZER",
        })

    if len({t["case_id"] for t in themes}) != 9:
        raise ValueError("Repeated historical theme")
    paths = [record["path"] for record in original_annotations]
    if len(paths) != len(set(paths)) or not all(isinstance(p, str) for p in paths):
        raise ValueError("Repeated or invalid historical source path")

    historical_blobs = git_blobs(repository, historical)
    if any(path not in historical_blobs for path in paths):
        raise ValueError("Historical corpus contains missing source at historical revision")

    corpus = [
        {"source_path": p, "source_blob_oid": historical_blobs[p]}
        for p in sorted(paths)
    ]
    packed = "".join(
        f"{r['source_path']}\0{r['source_blob_oid']}\n" for r in corpus
    ).encode("utf-8")

    return {
        "schema_version": 1,
        "state": "PREFREEZE_SCRUBBED_INTAKE_CANDIDATE_NOT_AN_INDEPENDENT_REFERENCE",
        "authority": "Research fixture preparation only; historical W5 source world, not accepted new P03 gold",
        "input_ref": input_ref,
        "historical_source_ref": historical,
        "historical_input_blob_sha256": {
            "original_scenarios_input": hashlib.sha256(raw_scenarios).hexdigest(),
            "original_corpus_input": hashlib.sha256(raw_annotations).hexdigest(),
        },
        "corpus_manifest_sha256": hashlib.sha256(packed).hexdigest(),
        "historical_source_count": len(corpus),
        "theme_count": len(themes),
        "corpus": corpus,
        "themes": themes,
        "limitations": [
            "The theme hint words originate in B1 subject names but case IDs are neutral aliases; neither provides an independently expressed historical owner question.",
            "An independent neutralizer must formulate meaningful natural-language questions from these hints and the historical source world without old B1 relevance answers.",
            "Neither the historical B1 must-retrieve/distractor sets nor subject membership labels or preferred routes are part of this intake.",
            "This public intake has no selected primary tasks, independently accepted legacy gold, actual external author, answer labels, heldout paths or scorer output.",
            "A fresh assessor must read source blobs through an isolated read/list/search world excluding the original research-fixture annotations/gold and P03 design materials.",
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repository", type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument("--input-ref", default=INPUT_REF)
    args = parser.parse_args()
    print(json.dumps(build_intake(args.repository.resolve(), args.input_ref), indent=2))


if __name__ == "__main__":
    main()
