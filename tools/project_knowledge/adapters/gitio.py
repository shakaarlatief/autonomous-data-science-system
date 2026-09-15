"""Exact Git snapshot enumeration and blob reads; no checkout-byte fallback."""

from pathlib import Path
import subprocess

from ..model import RepositorySnapshot, SnapshotEntry, SnapshotMode, SubstrateError, validate_source_path


def _git(root: Path, *args: str, input_bytes: bytes | None = None) -> bytes:
    result = subprocess.run(["git", "-C", str(root), *args], input=input_bytes, capture_output=True, check=False)
    if result.returncode:
        raise SubstrateError("GIT_READ_FAILED", result.stderr.decode("utf-8", errors="replace").strip())
    return result.stdout


def commit_snapshot(root: Path, ref: str) -> RepositorySnapshot:
    commit = _git(root, "rev-parse", "--verify", "--end-of-options", f"{ref}^{{commit}}").decode("ascii").strip()
    entries = []
    for record in _git(root, "ls-tree", "-r", "-z", "--full-tree", commit).split(b"\0"):
        if record:
            metadata, raw_path = record.split(b"\t", 1)
            mode, _, oid = metadata.decode("ascii").split()
            try:
                path = raw_path.decode("utf-8", errors="strict")
            except UnicodeDecodeError as error:
                raise SubstrateError("INVALID_SOURCE_PATH", "Git path is not UTF-8") from error
            entries.append(SnapshotEntry(path, oid, mode))
    return RepositorySnapshot(root.resolve(), SnapshotMode.COMMIT_SNAPSHOT, tuple(entries), commit)


def worktree_snapshot(root: Path) -> RepositorySnapshot:
    """Capture membership; materialization is read at validation time, not atomically."""
    try:
        paths = _git(root, "ls-files", "-z", "--cached", "--others", "--exclude-standard").decode("utf-8").split("\0")
    except UnicodeDecodeError as error:
        raise SubstrateError("INVALID_SOURCE_PATH", "Git path is not UTF-8") from error
    entries = tuple(SnapshotEntry(path) for path in sorted(set(paths) - {""}))
    return RepositorySnapshot(root.resolve(), SnapshotMode.WORKTREE_SNAPSHOT, entries)


def read_blob(root: Path, entry: SnapshotEntry) -> bytes:
    if entry.git_mode not in {"100644", "100755"} or entry.blob_id is None:
        raise SubstrateError("UNSUPPORTED_SOURCE_MODE", "Only regular Git blob carriers are supported")
    return _git(root, "cat-file", "blob", entry.blob_id)


def read_blobs(root: Path, entries: tuple[SnapshotEntry, ...]) -> dict[str, bytes]:
    """Read regular blobs in one Git process, using size-framed binary output.

    Identical objects are requested once. No text decoding, line-ending
    conversion, filters, or working-tree materialization touches blob content.
    """
    if any(e.git_mode not in {"100644", "100755"} or e.blob_id is None for e in entries):
        raise SubstrateError("UNSUPPORTED_SOURCE_MODE", "Only regular Git blob carriers are supported")
    object_ids = tuple(dict.fromkeys(e.blob_id for e in entries))
    if not object_ids:
        return {}
    output = _git(root, "cat-file", "--batch", input_bytes=("\n".join(object_ids) + "\n").encode("ascii"))
    blobs = {}
    offset = 0
    for oid in object_ids:
        end = output.find(b"\n", offset)
        header = output[offset:end].split() if end >= 0 else []
        if len(header) != 3 or header[:2] != [oid.encode("ascii"), b"blob"] or not header[2].isdigit():
            raise SubstrateError("GIT_READ_FAILED", f"Invalid or unavailable batch blob: {oid}")
        start = end + 1
        stop = start + int(header[2])
        if output[stop:stop + 1] != b"\n":
            raise SubstrateError("GIT_READ_FAILED", f"Truncated batch blob: {oid}")
        blobs[oid] = output[start:stop]
        offset = stop + 1
    if offset != len(output):
        raise SubstrateError("GIT_READ_FAILED", "Unexpected trailing Git batch output")
    return blobs


def read_committed_path(root: Path, commit: str, source_path: str) -> bytes:
    validate_source_path(source_path)
    snapshot = commit_snapshot(root, commit)
    if snapshot.source_commit != commit:
        raise SubstrateError("INVALID_SOURCE_COMMIT", "Revision must name the exact commit, not an alias")
    for entry in snapshot.entries:
        if entry.path == source_path:
            return read_blob(root, entry)
    raise SubstrateError("SOURCE_NOT_IN_COMMIT", f"Source is absent from commit: {source_path}")
