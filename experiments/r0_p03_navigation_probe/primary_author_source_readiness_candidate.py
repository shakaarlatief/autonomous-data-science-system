"""Non-scored primary-author readiness window with source-backed reconstruction files.

This deliberately does not freeze scored tasks or decide full answer closure.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import re
import sys
import zipfile

from experiments.r0_p03_navigation_probe import primary_author_pilot_builder_candidate as base

ADDITIONS = (
    "README.md",
    "docs/README.md",
    "docs/CONTINUITY.md",
)
WITHHELD = frozenset({
    "docs/CURRENT_STATE.md",
    "docs/KNOWLEDGE_MAP.md",
})
IDENTIFIER = "R0_P03_PRIMARY_AUTHOR_READINESS_SOURCE_WINDOW_CANDIDATE_V1"
DEFAULT_DIR = Path(".venv") / ".r0_p03_author_readiness"
PROHIBITED_EXPLICIT = re.compile(r"R0[-_]?P0?3|Research 513|Research 217", re.IGNORECASE)
NAME = "R0_P03_AUTHOR_READINESS_SOURCE_WINDOW.zip"


def source_window(repo: Path, *, pin: str = base.PIN) -> dict[str, tuple[str, bytes]]:
    result = dict(base.sources_at_pin(repo, pin))
    if not WITHHELD.isdisjoint(result):
        raise ValueError("Design-leaking orientation entered the source roster")
    for path in ADDITIONS:
        oid = base.git(repo, "rev-parse", "--verify", f"{pin}:{path}").strip().decode("ascii")
        if not re.fullmatch("[0-9a-f]{40}", oid):
            raise ValueError("Invalid exact Git blob ID")
        raw = base.git(repo, "cat-file", "blob", oid)
        text = raw.decode("utf-8")
        if hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest() != oid:
            raise ValueError("Git blob mismatch")
        if len(raw) > base.MAX_FILE or "\0" in text or PROHIBITED_EXPLICIT.search(text):
            raise ValueError(f"Unsafe added source: {path}")
        if path in result:
            raise ValueError("Duplicate source path")
        result[path] = oid, raw
    return dict(sorted(result.items()))


def build(repo: Path, *, pin: str = base.PIN, verify_only: bool = False,
          root_override: Path | None = None) -> dict:
    repo = repo.resolve()
    if not (repo / ".git").is_dir():
        raise ValueError("Not a Git repository")
    sources = source_window(repo, pin=pin)
    manifest = {
        "classification": "UNSCORED_PRIMARY_AUTHOR_SOURCE_READINESS_CANDIDATE_NOT_SCORED_FIXTURE",
        "identifier": IDENTIFIER,
        "source_ref": pin,
        "selection": "full predeclared source families plus three exact reconstruction documents",
        "exclusions": sorted(WITHHELD),
        "admission_status": "SOURCE_ROSTER_VERIFIED_TASK_CLOSURE_AND_CUSTODY_NOT_QUALIFIED",
        "file_count": len(sources),
        "files": [
            {"path": path, "git_blob_oid": oid, "sha256": hashlib.sha256(raw).hexdigest(),
             "bytes": len(raw)}
            for path, (oid, raw) in sources.items()
        ],
    }
    intro = (
        "# Source-readiness packet for independent R0-P03 authorship\n\n"
        "This is a source-only engineering candidate, NOT an authorized scored task packet.\n"
        "No existing pilot questions, answers, gold, B0-B4 comparator designs, or scored reference lists are included.\n"
        "The additional README and CONTINUITY documents provide source-world reconstruction context.\n"
        "The source commit is historical. Do not infer the present operating state.\n"
        "Source paths and Git blobs establish bytes, not scope-complete governing authority.\n"
        "A separate prospective independence/custody/closure admission is required before scored tasks.\n"
        "Do not use this packet to generate scored tasks unless that admission is explicitly established.\n"
    ).encode()
    files = {
        "SOURCE_WINDOW_README.md": intro,
        "SOURCE_MANIFEST.json": (json.dumps(manifest, indent=2, ensure_ascii=False) + "\n").encode(),
    }
    files.update({"sources/" + path: raw for path, (_, raw) in sources.items()})
    archive = base.deterministic_zip(files)
    receipt = {
        "classification": manifest["classification"],
        "source_ref": pin,
        "source_count": len(sources),
        "source_bytes": sum(len(raw) for _, raw in sources.values()),
        "added_reconstruction_paths": list(ADDITIONS),
        "package_sha256": hashlib.sha256(archive).hexdigest(),
        "package_bytes": len(archive),
        "manifest_sha256": hashlib.sha256(files["SOURCE_MANIFEST.json"]).hexdigest(),
    }
    folder = root_override.resolve() if root_override else repo / DEFAULT_DIR
    if root_override is not None and (folder == repo or folder.is_relative_to(repo)):
        raise ValueError("Test output override cannot target repository content")
    packet = folder / NAME
    rpath = folder / "R0_P03_AUTHOR_READINESS_SOURCE_WINDOW.receipt.json"
    if verify_only:
        if not packet.is_file() or packet.read_bytes() != archive:
            raise ValueError("Pinned author-readiness archive mismatch")
        if not rpath.is_file() or json.loads(rpath.read_text(encoding="utf-8")) != receipt:
            raise ValueError("Pinned author-readiness receipt mismatch")
        print("SOURCE_WINDOW_REPRODUCIBLE=PASS")
    else:
        if packet.exists() or rpath.exists():
            raise FileExistsError("Refusing to overwrite an author-readiness packet")
        folder.mkdir(parents=True, exist_ok=True)
        packet.write_bytes(archive)
        rpath.write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8", newline="\n")
        print("SOURCE_WINDOW_CREATED", packet)
    print(json.dumps(receipt, indent=2))
    return receipt


if __name__ == "__main__":
    if len(sys.argv) not in {2, 3} or (len(sys.argv) == 3 and sys.argv[2] != "--verify-only"):
        raise SystemExit("usage: python -m experiments.r0_p03_navigation_probe.primary_author_source_readiness_candidate REPO [--verify-only]")
    build(Path(sys.argv[1]), verify_only=len(sys.argv) == 3)
