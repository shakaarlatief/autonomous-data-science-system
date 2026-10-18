"""Deterministic, non-scored prospective author source-window expansion.

Adds the *entire* historical textual frontend source family to Research 583's
196-carrier candidate. No task- or model-dependent selection, old gold, user
secrets, semantic source/authority acceptance or scored task freeze occurs.
"""
from __future__ import annotations

from collections import Counter
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import sys

from experiments.r0_p03_navigation_probe import (
    primary_author_source_readiness_candidate as prior,
)

IDENTIFIER = "R0_P03_NEUTRAL_SOURCE_FAMILY_FRONTEND_EXPANSION_CANDIDATE_V1"
EXTENSIONS = frozenset({".md", ".json", ".ts", ".tsx", ".js", ".jsx", ".css", ".html"})
FRONTEND_ROOT = "frontend/"
FORBIDDEN_DESIGN = re.compile(
    r"R0[-_ ]?P0?3|Research\s*513|Research\s*217|"
    r"\bB[0-4]\s*[-\u2013]\s*B[0-4]\b|"
    r"must[_ -]retrieve|must[_ -]not[_ -]retrieve|gold[_ -](?:answer|label|key)",
    re.IGNORECASE,
)
OUT_DIR = Path(".venv") / ".r0_p03_source_family_expansion"
OUT_NAME = "R0_P03_AUTHOR_SOURCE_FAMILY_EXPANSION_CANDIDATE.zip"


def _frontend(repo: Path, pin: str) -> tuple[dict[str, tuple[str, bytes]], list[str]]:
    raw_tree = prior.base.git(repo, "ls-tree", "-rz", pin, "--", "frontend")
    discovered: dict[str, str] = {}
    unsupported: list[str] = []
    for record in raw_tree.split(b"\0"):
        if not record:
            continue
        meta, path_bytes = record.split(b"\t", 1)
        mode, kind, oid = meta.decode("ascii").split()
        path = path_bytes.decode("utf-8")
        parts = PurePosixPath(path)
        if (not path.startswith(FRONTEND_ROOT) or path.startswith("/")
                or "\\" in path or ".." in parts.parts):
            raise ValueError("Unsafe frontend path")
        if kind != "blob" or mode not in {"100644", "100755"}:
            raise ValueError("Non-regular frontend source encountered")
        if parts.suffix.lower() not in EXTENSIONS:
            unsupported.append(path)
            continue
        discovered[path] = oid
    if not discovered or len(discovered) != len(set(discovered)):
        raise ValueError("Front-end source family incomplete or duplicated")
    if any(PurePosixPath(x).suffix != ".png" for x in unsupported):
        raise ValueError("Review unsupported frontend modalities before expansion")
    # Resolve in one batch and compare every complete Git blob byte identity.
    oids = sorted(set(discovered.values()))
    batch = prior.base.git(
        repo, "cat-file", "--batch",
        input_bytes=("\n".join(oids) + "\n").encode("ascii"),
    )
    pos = 0
    blobs: dict[str, bytes] = {}
    for expected in oids:
        stop = batch.index(b"\n", pos)
        header = batch[pos:stop].decode("ascii").split()
        if len(header) != 3:
            raise ValueError("Malformed batch blob header")
        actual, typ, size_text = header
        length = int(size_text)
        start, end = stop + 1, stop + 1 + length
        raw = batch[start:end]
        if (actual != expected or typ != "blob" or len(raw) != length
                or batch[end:end + 1] != b"\n"
                or hashlib.sha1(b"blob " + str(length).encode() + b"\0" + raw).hexdigest() != expected):
            raise ValueError("Pinned frontend Git blob does not match")
        if length > prior.base.MAX_FILE or b"\0" in raw:
            raise ValueError("Unsupported frontend textual blob")
        blobs[expected] = raw
        pos = end + 1
    if pos != len(batch):
        raise ValueError("Additional unexpected Git batch bytes")

    records: dict[str, tuple[str, bytes]] = {}
    for path, oid in sorted(discovered.items()):
        raw = blobs[oid]
        decoded = raw.decode("utf-8")
        if FORBIDDEN_DESIGN.search(decoded):
            raise ValueError("Explicit design/scoring leakage in frontend candidate: " + path)
        records[path] = (oid, raw)
    return records, sorted(unsupported)


def build(repo: Path, *, pin: str = prior.base.PIN, verify_only: bool = False,
          root_override: Path | None = None) -> dict[str, object]:
    repo = repo.resolve()
    if not (repo / ".git").is_dir():
        raise ValueError("Must run against the existing Git workspace")
    original = prior.source_window(repo, pin=pin)
    new, unsupported = _frontend(repo, pin)
    if not set(original).isdisjoint(new):
        raise ValueError("Source family unexpectedly overlaps prior candidate")
    complete = dict(sorted({**original, **new}.items()))
    count = sum(len(body) for _, body in complete.values())
    if count > prior.base.MAX_TOTAL:
        raise ValueError("Source-window byte limit exceeded")
    manifest = {
        "classification": "UNSCORED_SOURCE_FAMILY_EXPANSION_CANDIDATE_NOT_SCORED_AUTHOR_FIXTURE",
        "identifier": IDENTIFIER,
        "source_ref": pin,
        "file_count": len(complete),
        "previous_source_count": len(original),
        "frontend_text_file_count": len(new),
        "frontend_media_excluded": unsupported,
        "source_bytes": count,
        "readiness": "CANDIDATE_NO_TASK_CLOSURE_NO_AUTHORITY_OR_SCORING_ADMISSION",
        "not_admitted_evidence_classes": [
            "historical_checkpoints_and_research",
            "runtime_validation_proof_beyond_included_sources",
            "unsupported_binary_frontend_media",
        ],
        "files": [
            {"path": path, "git_blob_oid": oid,
             "sha256": hashlib.sha256(body).hexdigest(), "bytes": len(body)}
            for path, (oid, body) in complete.items()
        ],
    }
    intro = (
        "# R0-P03 prospective source family expansion: NOT a scored task packet\n\n"
        "This archive adds all historical textual frontend carriers, not topical\n"
        "or pilot-derived selected files, to a 196-carrier readiness candidate.\n"
        "It is historical source evidence only, not current-state authority.\n"
        "The four frontend PNGs are excluded media and remain non-readable here.\n"
        "Historical checkpoint, research, validation and task-complete authority\n"
        "closures are NOT QUALIFIED: do not independently generate scored tasks\n"
        "from this package and do not claim a complete answer world.\n"
        "No questions, gold, rubrics, scores, comparison arms or prior pilot\n"
        "outputs are included. A later prospective independent admission is\n"
        "required before authoring or scoring.\n"
    ).encode("utf-8")
    files = {
        "SOURCE_WINDOW_README.md": intro,
        "SOURCE_MANIFEST.json": (
            json.dumps(manifest, indent=2, ensure_ascii=False) + "\n"
        ).encode("utf-8"),
    }
    files.update({"sources/" + p: body for p, (_, body) in complete.items()})
    archive = prior.base.deterministic_zip(files)
    receipt = {
        "identifier": IDENTIFIER,
        "source_ref": pin,
        "source_count": len(complete),
        "prior_source_count": len(original),
        "frontend_text_count": len(new),
        "frontend_unsupported_media_count": len(unsupported),
        "source_bytes": count,
        "zip_bytes": len(archive),
        "zip_sha256": hashlib.sha256(archive).hexdigest(),
        "manifest_sha256": hashlib.sha256(files["SOURCE_MANIFEST.json"]).hexdigest(),
        "status": "NON_SCORED_CANDIDATE_ONLY",
    }
    outdir = (root_override or (repo / OUT_DIR)).resolve()
    if root_override is not None and (outdir == repo or outdir.is_relative_to(repo)):
        raise ValueError("Test output override may not be inside the repository")
    file = outdir / OUT_NAME
    receipt_file = outdir / "R0_P03_AUTHOR_SOURCE_FAMILY_EXPANSION.receipt.json"
    if verify_only:
        if not file.is_file() or file.read_bytes() != archive:
            raise ValueError("Not the exact deterministically regenerated source archive")
        if (not receipt_file.is_file() or
                json.loads(receipt_file.read_text(encoding="utf-8")) != receipt):
            raise ValueError("Source expansion receipt drift")
        print("SOURCE_FAMILY_EXPANSION_REPRODUCIBLE=PASS")
    else:
        if file.exists() or receipt_file.exists():
            raise FileExistsError("Refuse overwrite of existing source packet")
        outdir.mkdir(parents=True, exist_ok=True)
        file.write_bytes(archive)
        receipt_file.write_text(
            json.dumps(receipt, indent=2) + "\n", encoding="utf-8", newline="\n",
        )
        print("SOURCE_FAMILY_EXPANSION_CREATED", file)
    print(json.dumps(receipt, sort_keys=True))
    return receipt


if __name__ == "__main__":
    if len(sys.argv) not in {2, 3} or (len(sys.argv) == 3 and sys.argv[2] != "--verify-only"):
        raise SystemExit("usage: python -m experiments.r0_p03_navigation_probe.primary_author_frontend_expansion_candidate REPO [--verify-only]")
    build(Path(sys.argv[1]), verify_only=len(sys.argv) == 3)
