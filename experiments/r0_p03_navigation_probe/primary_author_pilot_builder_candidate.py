"""Build and verify a non-scored, source-only R0-P03 fresh-author rehearsal packet.

The snapshot uses exact historical Git blobs. It deliberately excludes the
experiment's design, other-arm outputs, historical reference answers, current
mutable worktree and scoring fixtures. This is not a scored source corpus.
"""
from __future__ import annotations

import hashlib
import io
import json
from pathlib import Path, PurePosixPath
import re
import subprocess
import sys
import zipfile

PIN = "c57556a8bf993a1d327e9197acb7b7c745071cd8"
ID = "r0-p03-fresh-author-source-only-pilot-v1"
ESSENTIAL = frozenset({
    "docs/DECISIONS.md",
    "docs/current_routing.json",
    "docs/specifications/028_v1_project_knowledge_architecture_implementation_and_migration_contract.md",
})
TOP_DOCS = frozenset({
    "docs/DECISIONS.md", "docs/current_routing.json", "docs/PRINCIPLES.md",
    "docs/VISION.md", "docs/DEVELOPMENT_METHOD.md",
})
SUFFIXES = {".md", ".json", ".py", ".sql", ".toml", ".yaml", ".yml"}
MAX_FILE = 2_000_000
MAX_TOTAL = 50_000_000
OUTPUT_SUBDIR = Path(".venv") / ".r0_p03_author_pilot"
BRIEF = Path(__file__).with_name("PRIMARY_AUTHOR_PILOT_BRIEF.md")


def admissible(path: str) -> bool:
    p = PurePosixPath(path)
    if not path or path.startswith("/") or "\\" in path or ".." in p.parts or p.suffix.lower() not in SUFFIXES:
        return False
    if path in TOP_DOCS:
        return True
    if path.startswith(("docs/specifications/", "docs/foundations/")):
        return re.fullmatch(r"\d{3}_[a-zA-Z0-9_+.-]+\.(md|json)", p.name) is not None
    if path.startswith(("src/ads_system/", "tools/project_knowledge/", "schemas/project_knowledge/")):
        return True
    if path.startswith("tests/unit/"):
        return p.name.startswith("test_project_knowledge_") and p.suffix == ".py"
    return False


def git(repo: Path, *argv: str, input_bytes: bytes | None = None) -> bytes:
    result = subprocess.run(
        ["git", *argv], cwd=repo, input=input_bytes, capture_output=True, check=True
    )
    return result.stdout


def sources_at_pin(repo: Path, pin: str = PIN) -> dict[str, tuple[str, bytes]]:
    if git(repo, "rev-parse", "--verify", pin + "^{commit}").strip().decode() != pin:
        raise ValueError("Pinned commit resolution mismatch")
    tree = git(repo, "ls-tree", "-rz", pin, "--", "docs", "src", "tools", "schemas", "tests")
    selected: dict[str, str] = {}
    for record in tree.split(b"\0"):
        if not record:
            continue
        meta, raw_path = record.split(b"\t", 1)
        mode, kind, blob = meta.decode("ascii").split()
        path = raw_path.decode("utf-8")
        if admissible(path):
            if kind != "blob" or mode not in {"100644", "100755"}:
                raise ValueError("Nonregular selected source: " + path)
            selected[path] = blob
    if not ESSENTIAL.issubset(selected):
        raise ValueError("Mandatory neutral source absent: " + repr(sorted(ESSENTIAL - selected.keys())))

    objects = sorted(set(selected.values()))
    batch = git(repo, "cat-file", "--batch", input_bytes=("\n".join(objects) + "\n").encode("ascii"))
    buffer = memoryview(batch)
    pos = 0
    loaded: dict[str, bytes] = {}
    for oid in objects:
        stop = batch.index(b"\n", pos)
        actual, kind, size_str = batch[pos:stop].decode("ascii").split()
        size = int(size_str)
        data_start, data_end = stop + 1, stop + 1 + size
        body = bytes(buffer[data_start:data_end])
        if (actual != oid or kind != "blob" or len(body) != size
            or batch[data_end:data_end + 1] != b"\n"
            or hashlib.sha1(b"blob " + str(size).encode() + b"\0" + body).hexdigest() != oid):
            raise ValueError("Incorrect Git object body: " + oid)
        loaded[oid] = body
        pos = data_end + 1
    if pos != len(batch):
        raise ValueError("Unexpected Git object bytes")
    total = 0
    sources: dict[str, tuple[str, bytes]] = {}
    for path, oid in sorted(selected.items()):
        body = loaded[oid]
        if len(body) > MAX_FILE or b"\0" in body:
            raise ValueError("Unsupported selected source: " + path)
        body.decode("utf-8")
        total += len(body)
        if total > MAX_TOTAL:
            raise ValueError("Too many source bytes")
        sources[path] = oid, body
    return sources


def deterministic_zip(files: dict[str, bytes]) -> bytes:
    output = io.BytesIO()
    with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=6) as archive:
        for path, content in sorted(files.items()):
            info = zipfile.ZipInfo(path, date_time=(1980, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, content)
    return output.getvalue()


def build(repo: Path, *, pin: str = PIN, verify_only: bool = False,
          root_override: Path | None = None) -> dict:
    repo = repo.resolve()
    if not (repo / ".git").is_dir():
        raise ValueError("Not the existing ADS repository")
    source_records = sources_at_pin(repo, pin)
    manifest = {
        "classification": "UNSCORED_SOURCE_ONLY_REHEARSAL_NOT_SCORED_PRIMARY_FIXTURE",
        "format": ID,
        "source_ref": pin,
        "selection_basis": "whole allowed source families, not task-conditioned anchors",
        "file_count": len(source_records),
        "source_bytes": sum(len(data) for _, data in source_records.values()),
        "files": [
            {"path": p, "git_blob_oid": oid, "sha256": hashlib.sha256(data).hexdigest(), "bytes": len(data)}
            for p, (oid, data) in source_records.items()
        ],
    }
    brief = BRIEF.read_bytes()
    brief.decode("utf-8")
    content = {
        "AUTHOR_BRIEF.md": brief,
        "SOURCE_MANIFEST.json": (json.dumps(manifest, ensure_ascii=False, indent=2) + "\n").encode(),
    }
    for path, (_, body) in source_records.items():
        content["sources/" + path] = body
    package = deterministic_zip(content)
    receipt = {
        "classification": manifest["classification"],
        "source_ref": pin,
        "file_count": len(source_records),
        "source_bytes": manifest["source_bytes"],
        "package_sha256": hashlib.sha256(package).hexdigest(),
        "package_bytes": len(package),
        "manifest_sha256": hashlib.sha256(content["SOURCE_MANIFEST.json"]).hexdigest(),
        "author_brief_sha256": hashlib.sha256(brief).hexdigest(),
    }
    folder = root_override.resolve() if root_override is not None else repo / OUTPUT_SUBDIR
    if root_override is not None and (folder == repo or folder.is_relative_to(repo)):
        raise ValueError("Test output override cannot target ADS repository content")
    output = folder / "R0_P03_FRESH_AUTHOR_PILOT.zip"
    receipt_path = folder / "R0_P03_FRESH_AUTHOR_PILOT.receipt.json"
    if verify_only:
        if not output.is_file() or output.read_bytes() != package:
            raise ValueError("Generated source package differs from pinned verified output")
        if not receipt_path.is_file() or json.loads(receipt_path.read_text(encoding="utf-8")) != receipt:
            raise ValueError("Coordinator receipt differs from pinned verified output")
        print("VERIFICATION_PASS")
    else:
        if output.exists() or receipt_path.exists():
            raise FileExistsError("Refusing to overwrite an existing author packet or receipt")
        folder.mkdir(parents=True, exist_ok=True)
        output.write_bytes(package)
        receipt_path.write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8", newline="\n")
        print("CREATED", output)
    print(json.dumps(receipt, indent=2))
    return receipt


if __name__ == "__main__":
    if len(sys.argv) not in {2, 3} or (len(sys.argv) == 3 and sys.argv[2] != "--verify-only"):
        raise SystemExit("usage: primary_author_pilot_builder_candidate.py REPO [--verify-only]")
    build(Path(sys.argv[1]), verify_only=len(sys.argv) == 3)
