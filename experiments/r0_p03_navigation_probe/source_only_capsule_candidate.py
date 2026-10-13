"""Export a reproducible source-only W5 reviewer capsule without historical gold.

This exporter separates the content surface that a future fresh reviewer SHOULD
see from the original public Git repository and its historical B1 annotations.
It is an experimental staging utility, not an access-control system: source
copying does not prevent a reviewer with ambient filesystem, Git, web, or prior
conversation access from acquiring extra context. Such isolation and exposure
qualification must be established by the actual reviewer execution environment.

The source corpus and topic hints are fixed at immutable Git commits. The
exporter never reads working-tree source bytes, rewrites historical W5 fixtures,
selects a new task, constructs a scoring answer, or touches the private
knowledge-companion repository.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from pathlib import Path

from experiments.r0_p03_navigation_probe.independent_reference_intake_candidate import (
    INPUT_REF,
    build_intake,
)

ALLOWED_TOP_LEVEL = frozenset({"sources", "reviewer_intake.json", "capsule_integrity.json"})
FORBIDDEN_INPUT_KEYS = frozenset({
    "candidate_subjects", "legacy_topics", "subjects", "preferred_subject",
    "must_retrieve", "must_not_retrieve", "gold_answers", "gold_labels",
    "scored_results", "answer_keys", "heldout_paths",
})


def git_show_bytes(repository: Path, source_ref: str, source_path: str) -> bytes:
    return subprocess.run(
        ["git", "show", f"{source_ref}:{source_path}"],
        cwd=repository, capture_output=True, check=True,
    ).stdout


def _safe_relative_source_path(source_path: str) -> Path:
    if not source_path or "\\" in source_path or ":" in source_path:
        raise ValueError("Noncanonical source path")
    # Validate the raw Git spelling before Path can discard empty/dot segments
    # or interpret a drive-relative/rooted Windows path.
    parts = source_path.split("/")
    if any(part in ("", ".", "..") or part.casefold() == ".git" for part in parts):
        raise ValueError("Invalid source location")
    candidate = Path(source_path)
    if candidate.is_absolute():
        raise ValueError("Invalid source location")
    if candidate.parts[0].startswith("."):
        raise ValueError("Hidden source location")
    return candidate


def export_source_capsule(repository: Path, destination: Path) -> dict[str, object]:
    """Create an entirely new capsule directory and verify every source byte.

    Destination must not already exist and its parent must be inside the
    current repository's ignored .venv scratch root. A new directory is
    prepared only after checking the parent is not a symlink; no
    preexisting contents are altered.
    Every selected source is read directly from the immutable historical Git
    object. Staging is atomic to the extent the platform supports an exclusive
    mkdir; on interruption, the new, incomplete directory must be discarded
    rather than used for review.
    """
    repository = repository.resolve(strict=True)
    intake = build_intake(repository, INPUT_REF)
    assert intake["input_ref"] == INPUT_REF
    destination = destination.absolute()
    if destination.exists() or destination.is_symlink():
        raise FileExistsError(f"Refuse to overwrite existing capsule: {destination}")
    if not destination.parent.is_dir() or destination.parent.is_symlink():
        raise ValueError("Capsule parent must be an existing real directory")
    # This prototype may materialize only in the repository's existing
    # Git-ignored virtual-environment scratch root. It must not silently write
    # to the private companion, a project source folder, or an unregistered
    # external directory. A real reviewer handoff requires a separate,
    # positively qualified destination and access contract.
    scratch_root = (repository / ".venv").resolve(strict=True)
    parent = destination.parent.resolve(strict=True)
    if not parent.is_relative_to(scratch_root):
        raise PermissionError("Capsule prototype destination must be inside .venv")
    destination.mkdir(mode=0o700)

    source_root = destination / "sources"
    source_root.mkdir()
    source_hashes = []
    for item in intake["corpus"]:
        relative = _safe_relative_source_path(item["source_path"])
        path = source_root / relative
        content = git_show_bytes(repository, intake["historical_source_ref"], item["source_path"])
        actual_oid = subprocess.run(
            ["git", "hash-object", "--stdin"],
            cwd=repository, input=content, capture_output=True, check=True,
        ).stdout.decode("ascii").strip()
        if actual_oid != item["source_blob_oid"]:
            raise ValueError(f"Git blob mismatch: {item['source_path']}")
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("xb") as handle:
            handle.write(content)
        if path.read_bytes() != content:
            raise ValueError(f"Saved source byte mismatch: {item['source_path']}")
        source_hashes.append({
            "path": item["source_path"],
            "blob_oid": item["source_blob_oid"],
            "sha256": hashlib.sha256(content).hexdigest(),
            "byte_count": len(content),
        })

    reviewer_input = {
        "schema_version": 1,
        "status": "SOURCE_ONLY_LEGACY_INTAKE_NOT_GOLD",
        "historical_source_ref": intake["historical_source_ref"],
        "corpus_manifest_sha256": intake["corpus_manifest_sha256"],
        "themes": intake["themes"],
        "instructions": (
            "The nine themes are old B1-origin topic hints, not independently "
            "authored questions. Inspect only the staged sources and create "
            "source-cited neutral information needs and reference answers; "
            "do not infer old B1 membership relevance."
        ),
    }
    if FORBIDDEN_INPUT_KEYS & set(reviewer_input):
        raise ValueError("Historical gold leaked into capsule intake")

    integrity = {
        "schema_version": 1,
        "status": "UNFROZEN_SOURCE_CAPSULE_MECHANICS_ONLY",
        "source_count": len(source_hashes),
        "theme_count": len(reviewer_input["themes"]),
        "historical_source_ref": intake["historical_source_ref"],
        "source_manifest_sha256": intake["corpus_manifest_sha256"],
        "source_bytes_sha256": hashlib.sha256(
            "".join(
                f"{entry['path']}\0{entry['sha256']}\n" for entry in source_hashes
            ).encode("utf-8")
        ).hexdigest(),
        "source_sizes_total_bytes": sum(entry["byte_count"] for entry in source_hashes),
        "limitations": [
            "This verifies only selected source content, not actual reviewer isolation.",
            "No independent author, private gold, answer adjudication, task or scorer exists.",
            "A reviewer with wider Git, internet, tool or historical context access may still encounter original W5 gold.",
        ],
    }
    for name, data in (
        ("reviewer_intake.json", reviewer_input),
        ("capsule_integrity.json", integrity),
    ):
        with (destination / name).open("x", encoding="utf-8", newline="\n") as handle:
            json.dump(data, handle, indent=2, ensure_ascii=False)
            handle.write("\n")
    if {p.name for p in destination.iterdir()} != ALLOWED_TOP_LEVEL:
        raise ValueError("Unexpected capsule root content")
    if not all((source_root / _safe_relative_source_path(entry["path"])).is_file() for entry in source_hashes):
        raise ValueError("Incomplete source capsule")
    return integrity


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repository", type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument("--destination", type=Path, required=True)
    args = parser.parse_args()
    print(json.dumps(export_source_capsule(args.repository, args.destination), indent=2))


if __name__ == "__main__":
    main()
