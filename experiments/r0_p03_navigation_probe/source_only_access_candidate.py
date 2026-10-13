"""Bounded in-memory access to verified historical sources, not reviewer isolation.

Only request(list/read/search) is intended for a future tool host. Construction
is a trusted coordinator operation: no model may choose the capsule or manifest.
This library installs no tools, starts no model/server, calls no Git/network,
writes no output packet, and does not constrain other tools in a host process.
"""
from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path
import stat
from types import MappingProxyType

from experiments.r0_p03_navigation_probe.source_only_capsule_candidate import (
    ALLOWED_TOP_LEVEL,
    _safe_relative_source_path,
)

MANIFEST = Path(__file__).with_name("legacy_blinded_intake_candidate.json")
HISTORICAL_REF = "4b94ffe183ff7af72cef6ee7492b4ba2f30c11ef"
MANIFEST_DIGEST = "f108da7fb37999c499737b6406eb4cd99ae5c0885590e1b7b933117d3253338d"
CONTENT_DIGEST = "baf2b893435c1951b52814a3de897f7684890b1449bb437b46948cc868d304d3"
MAX_RESULTS = 20
MAX_TEXT = 16_384


class SourceAccessError(ValueError):
    """A stable error code without host paths or exception details."""


def _regular(path: Path, *, directory: bool = False) -> None:
    if path.is_symlink() or path.is_junction():
        raise SourceAccessError("LINK_FORBIDDEN")
    mode = path.lstat().st_mode
    if not (stat.S_ISDIR(mode) if directory else stat.S_ISREG(mode)):
        raise SourceAccessError("NOT_REGULAR")


def _integer(value: object, low: int, high: int) -> int:
    if type(value) is not int or not low <= value <= high:
        raise SourceAccessError("INVALID_RANGE")
    return value


class SourceOnlyAccess:
    """Verify the entire closed corpus once; serve only immutable memory after that."""

    def __init__(self, capsule: Path):
        try:
            _regular(capsule, directory=True)
            if {p.name for p in capsule.iterdir()} != ALLOWED_TOP_LEVEL:
                raise SourceAccessError("CAPSULE_ROSTER_MISMATCH")
            for name in ALLOWED_TOP_LEVEL - {"sources"}:
                _regular(capsule / name)
            source_root = capsule / "sources"
            _regular(source_root, directory=True)
            manifest = json.loads(MANIFEST.read_bytes())
            corpus = manifest["corpus"]
            packed = "".join(f"{r['source_path']}\0{r['source_blob_oid']}\n" for r in corpus)
            if (manifest["historical_source_ref"] != HISTORICAL_REF or len(corpus) != 65
                    or hashlib.sha256(packed.encode()).hexdigest() != MANIFEST_DIGEST):
                raise SourceAccessError("TRUSTED_MANIFEST_MISMATCH")
            expected = {r["source_path"] for r in corpus}
            directories = {p.as_posix() for name in expected
                           for p in Path(name).parents if p != Path(".")}
            actual = set()
            for parent, dirs, files in os.walk(source_root, followlinks=False):
                for name in dirs + files:
                    path = Path(parent) / name
                    relative = path.relative_to(source_root).as_posix()
                    _safe_relative_source_path(relative)
                    _regular(path, directory=name in dirs)
                    if name in dirs:
                        if relative not in directories:
                            raise SourceAccessError("SOURCE_ROSTER_MISMATCH")
                    else:
                        actual.add(relative)
            if actual != expected:
                raise SourceAccessError("SOURCE_ROSTER_MISMATCH")

            sources = {}
            commitment = []
            total = 0
            for item in corpus:
                name = item["source_path"]
                raw = (source_root / _safe_relative_source_path(name)).read_bytes()
                oid = hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()
                if oid != item["source_blob_oid"]:
                    raise SourceAccessError("SOURCE_BLOB_MISMATCH")
                digest = hashlib.sha256(raw).hexdigest()
                sources[name] = (oid, digest, tuple(raw.decode("utf-8").splitlines(keepends=True)))
                commitment.append(f"{name}\0{digest}\n")
                total += len(raw)
            if total != 1_725_920 or hashlib.sha256("".join(commitment).encode()).hexdigest() != CONTENT_DIGEST:
                raise SourceAccessError("CONTENT_COMMITMENT_MISMATCH")
            self._sources = MappingProxyType(sources)
            self._paths = tuple(sorted(sources))
        except SourceAccessError:
            raise
        except (OSError, ValueError, KeyError, TypeError) as exc:
            raise SourceAccessError("CAPSULE_UNREADABLE_OR_INVALID") from exc

    def _identity(self, path: str) -> dict[str, object]:
        oid, digest, _ = self._sources[path]
        return {"path": path, "source_blob_oid": oid, "sha256": digest,
                "historical_source_ref": HISTORICAL_REF}

    def request(self, operation: str, **params: object) -> dict[str, object]:
        """Dispatch only three explicit operations; reject all unknown parameters."""
        try:
            if operation == "list" and set(params) <= {"offset", "limit"}:
                offset = _integer(params.get("offset", 0), 0, 65)
                limit = _integer(params.get("limit", MAX_RESULTS), 1, MAX_RESULTS)
                end = min(offset + limit, 65)
                payload = {"sources": [self._identity(p) for p in self._paths[offset:end]],
                           "next_offset": end if end < 65 else None, "total": 65}
            elif operation == "read" and set(params) <= {"path", "start_line", "max_lines"}:
                path = params.get("path")
                if not isinstance(path, str) or path not in self._sources:
                    raise SourceAccessError("SOURCE_NOT_ALLOWED")
                lines = self._sources[path][2]
                start = _integer(params.get("start_line", 1), 1, max(1, len(lines)))
                count = _integer(params.get("max_lines", 40), 1, 100)
                selected = lines[start - 1:start - 1 + count]
                value = "".join(selected)
                if len(value) > MAX_TEXT:
                    raise SourceAccessError("READ_OUTPUT_LIMIT")
                payload = {**self._identity(path), "start_line": start,
                           "end_line": start - 1 + len(selected), "total_lines": len(lines),
                           "text": value}
            elif operation == "search" and set(params) <= {"query", "limit"}:
                query = params.get("query")
                if not isinstance(query, str) or not 1 <= len(query) <= 128 or not query.strip():
                    raise SourceAccessError("INVALID_QUERY")
                limit = _integer(params.get("limit", MAX_RESULTS), 1, MAX_RESULTS)
                hits = []
                truncated = False
                for path in self._paths:
                    for number, line in enumerate(self._sources[path][2], 1):
                        position = line.find(query)
                        if position < 0:
                            continue
                        if len(hits) == limit:
                            truncated = True
                            break
                        snippet_start = max(0, position - 32)
                        hits.append({**self._identity(path), "line": number,
                                     "snippet": line[snippet_start:snippet_start + 160]})
                    if truncated:
                        break
                payload = {"hits": hits, "truncated": truncated, "match_mode": "LITERAL_CASE_SENSITIVE"}
            else:
                raise SourceAccessError("OPERATION_OR_PARAMETERS_NOT_ALLOWED")
            return {"ok": True, "scope": "SOURCE_API_ONLY_NOT_EXECUTION_ISOLATION", **payload}
        except SourceAccessError as exc:
            return {"ok": False, "error": str(exc)}
