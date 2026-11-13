"""Reproduce the path-only original-Git index for an unscored fresh-question pilot.

The coordinator is exposed to earlier R0-P03 answers and may not author
independent original questions or gold. This code therefore chooses a small
historical source index by a fixed digest order, without reading source text,
query outputs, prior scored results, or answer-bearing source snippets. The
index helps an independently started question writer understand what source
families exist. Its paths and titles are not reference answers or evidence
of authority, and this is NOT a representative scored R0-P03 task cohort.

The script is intentionally one-shot. It uses exclusive file creation and
does not silently regenerate/replace an already frozen index.
"""
from __future__ import annotations

from collections import Counter
from hashlib import sha256
import json
from pathlib import Path
import subprocess

PIN = "47ed6344a9153dcf366769e95722840fbf1a8f8b"
VERSION = "R0_P03_NONSCORING_FRESH_QUESTION_ORIGINATION_INDEX_V01"
SALT = b"r0-p03-fresh-question-origination-unscored-path-only-v01\0"
STRATA = (
    ("FOUNDATION", "docs/foundations/"),
    ("SPECIFICATION", "docs/specifications/"),
    ("RESEARCH", "docs/research/"),
    ("CHECKPOINT", "docs/checkpoints/"),
    ("VALIDATION", "docs/local_execution/validation/"),
)
PER_STRATUM = 10
ANCHORS = ("docs/CURRENT_STATE.md", "docs/DECISIONS.md")
OUTPUT = Path("experiments/r0_p03_navigation_probe/fresh_reference_need_index_pilot_v01.json")


def original_git_inventory() -> dict[str, str]:
    """Enumerate path and immutable Git blob IDs, with no original source reads."""
    result = subprocess.run(
        ["git", "ls-tree", "-r", "-z", PIN, "--", "docs"],
        capture_output=True,
        check=True,
    ).stdout
    inventory: dict[str, str] = {}
    for raw in result.split(b"\0"):
        if not raw:
            continue
        metadata, path_raw = raw.split(b"\t", 1)
        mode, kind, oid = metadata.decode("ascii").split(" ")
        path = path_raw.decode("utf-8")
        if kind != "blob" or mode not in {"100644", "100755"}:
            continue
        if path in inventory:
            raise ValueError("Duplicate source Git path")
        inventory[path] = oid
    return inventory


def build() -> dict:
    all_paths = original_git_inventory()
    selected: list[dict[str, object]] = []
    population: dict[str, int] = {}
    for label, prefix in STRATA:
        eligible = [
            (path, sha)
            for path, sha in all_paths.items()
            if path.startswith(prefix) and path.endswith(".md")
        ]
        if len(eligible) < PER_STRATUM:
            raise ValueError(f"Insufficient original Git source population: {label}")
        population[label] = len(eligible)
        # Stable digest sampling uses exact Git path and pinned original blob
        # identity; no source text, question answer or historical evaluation.
        eligible.sort(
            key=lambda e: (
                sha256(SALT + PIN.encode("ascii") + b"\0"
                       + label.encode("ascii") + b"\0"
                       + e[0].encode("utf8") + b"\0"
                       + e[1].encode("ascii")).hexdigest(),
                e[0],
            )
        )
        for rank, (path, oid) in enumerate(eligible[:PER_STRATUM], 1):
            selected.append({
                "stratum": label,
                "sampling_rank": rank,
                "original_git_path": path,
                "original_blob_oid": oid,
            })
    for path in ANCHORS:
        if path not in all_paths:
            raise ValueError(f"Missing original path anchor: {path}")
        selected.append({
            "stratum": "ORIENTATION_ANCHOR",
            "sampling_rank": 0,
            "original_git_path": path,
            "original_blob_oid": all_paths[path],
        })
    if len(selected) != 52 or len({x["original_git_path"] for x in selected}) != 52:
        raise ValueError("Index size or source uniqueness drift")
    return {
        "id": VERSION,
        "scientific_class": "UNSCORED_SOURCE_PATH_ONLY_NEED_ORIGINATION_FEASIBILITY_PILOT",
        "original_source_git_pin": PIN,
        "selection_basis": "exact_blob_path_SHA256_order_v01_no_source_content",
        "eligible_stratum_population_counts": population,
        "selection_per_stratum": PER_STRATUM,
        "two_additional_orientation_path_anchors": list(ANCHORS),
        "path_index_only": True,
        "original_source_bodies_present": False,
        "original_answer_text_present": False,
        "existing_twelve_B0_B1_questions_or_answers_present": False,
        "source_role_labels_are_not_authority_evidence": True,
        "original_R0_P03_scoring_result": "INCOMPLETE",
        "the_four_need_categories": [
            "COLD_START_CURRENT_ORIENTATION",
            "CROSS_PLANE_DISCOVERY",
            "IMPACT_ANALYSIS_ARCHITECTURE_EVOLUTION",
            "EXACT_SOURCE_AUTHORITY_RECOVERY",
        ],
        "items": selected,
    }


def main() -> None:
    result = build()
    raw = (json.dumps(result, sort_keys=True, indent=2, ensure_ascii=True) + "\n").encode("utf8")
    with OUTPUT.open("xb") as target:
        target.write(raw)
    print(json.dumps({
        "status": "CREATED_WITH_EXCLUSIVE_WRITE",
        "path": str(OUTPUT),
        "bytes": len(raw),
        "sha256": sha256(raw).hexdigest(),
        "source_paths": len(result["items"]),
        "original_source_bodies": False,
        "formal_R0_P03_gold_created": False,
        "original_source_git_pin": PIN,
        "stratum_counts": dict(Counter(x["stratum"] for x in result["items"])),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
