"""R0-P03 source-family qualification frontier, not source admission.

Trace explicit citations between complete pinned public source-world records
without authoring questions, selecting gold, or changing the future source
world. This makes *candidate* historical/validation dependencies inspectable
and gives an independent adjudicator an evidence-bound review frontier.

A textual citation is not proof of authority, a realization edge, acceptance
or task answer. Absence of citations is NOT proof a source is unneeded.
All per-source paths and edges stay under ignored local engineering scratch.
The aggregate public receipt includes no source-specific path or text.
"""
from __future__ import annotations

from collections import Counter, defaultdict
from hashlib import sha256
import json
from pathlib import Path, PurePosixPath
import posixpath
import re
import subprocess
import sys

from experiments.r0_p03_navigation_probe import source_world_coverage_gate as world

IDENTIFIER = "R0_P03_PINNED_HISTORICAL_EVIDENCE_DEPENDENCY_FRONTIER_V2"
OUTDIR = Path(".venv") / ".r0_p03_historical_dependency_frontier_v02"
INTERNAL = "R0_P03_HISTORICAL_DEPENDENCY_FRONTIER_NON_ADMISSION.json"
RECEIPT = "R0_P03_HISTORICAL_DEPENDENCY_FRONTIER.safe-receipt.json"
MAX_BATCH_BYTES = 100_000_000
MAX_BLOB_BYTES = 8_000_000

# Intentionally conservative: only explicit references in Markdown/plain
# documentary text. Code syntax references, implicit semantic dependencies,
# shorthand ledger IDs, and absent/old representations may be missed.
DOCUMENT_SUFFIXES = frozenset({".md", ".txt"})
DIRECT = re.compile(
    r"(?<![\w./])(?P<path>(?:docs|src|frontend|tools|schemas|tests|scripts|migrations)"
    r"/[A-Za-z0-9_.+/\-]+)"
)
NUMBER = re.compile(
    r"\b(?P<type>Research|Checkpoint|Validation|Specification|Foundation)"
    r"\s+(?P<number>\d{1,4})\b", re.I
)
LINK = re.compile(r"\[[^\]]{1,200}\]\((?P<target>[^)\s]{1,260})\)")
RELATIVE = re.compile(r"(?<![\w/])(?P<rel>(?:\.\./|\./)[A-Za-z0-9_.+/\-]+\.(?:md|txt|json|py))")
NUMBER_PATH = re.compile(r"^(\d{1,4})_")
TYPES = {
    "research": "docs/research/",
    "checkpoint": "docs/checkpoints/",
    "validation": "docs/local_execution/validation/",
    "specification": "docs/specifications/",
    "foundation": "docs/foundations/",
}
CRITICAL = frozenset({"historical_status", "execution_evidence"})
CORE = frozenset({"orientation", "governing"})


def canonical(value: object) -> bytes:
    return (json.dumps(value, sort_keys=True, ensure_ascii=True,
                       separators=(",", ":")) + "\n").encode("ascii")


def exact_blobs(repo: Path, rows: list[dict]) -> dict[str, bytes]:
    """Read exact historical Git blobs in a single bounded batch.

    Every returned blob is independently checked against the pinned OID,
    SHA-256 and size in the prior complete non-admission ledger.
    Unsupported representations are explicitly left unread, not inferred.
    """
    checks: dict[str, list[dict]] = defaultdict(list)
    for row in rows:
        if row["visibility"] == world.MODALITY_HOLD:
            continue
        oid = row["git_blob_oid"]
        if not re.fullmatch(r"[0-9a-f]{40}", oid):
            raise ValueError("Invalid source blob id")
        checks[oid].append(row)
    ordered = sorted(checks)
    p = subprocess.run(
        ["git", "cat-file", "--batch"], cwd=repo,
        input=("\n".join(ordered) + "\n").encode("ascii"),
        capture_output=True, check=True, timeout=45,
    )
    if len(p.stdout) > MAX_BATCH_BYTES:
        raise ValueError("Git source batch exceeds bound")
    offset = 0
    by_oid: dict[str, bytes] = {}
    for oid in ordered:
        end = p.stdout.find(b"\n", offset)
        if end < 0:
            raise ValueError("Missing Git source header")
        fields = p.stdout[offset:end].decode("ascii").split()
        if len(fields) != 3 or fields[0] != oid or fields[1] != "blob":
            raise ValueError("Unexpected pinned Git object")
        size = int(fields[2])
        if size < 0 or size > MAX_BLOB_BYTES:
            raise ValueError("Unbounded Git blob content")
        start, stop = end + 1, end + 1 + size
        raw = p.stdout[start:stop]
        if (
            len(raw) != size or p.stdout[stop:stop + 1] != b"\n"
            or world.sha1git(raw) != oid
        ):
            raise ValueError("Pinned Git content integrity failure")
        for row in checks[oid]:
            if row.get("sha256") != sha256(raw).hexdigest() or row.get("bytes") != size:
                raise ValueError("Pinned source metadata differs from Git bytes")
        by_oid[oid] = raw
        offset = stop + 1
    if offset != len(p.stdout):
        raise ValueError("Unexpected Git source trailer")
    return {r["path"]: by_oid[r["git_blob_oid"]] for r in rows
            if r["visibility"] != world.MODALITY_HOLD}


def numbered_index(paths: set[str]) -> dict[tuple[str, int], list[str]]:
    table: dict[tuple[str, int], list[str]] = defaultdict(list)
    for path in sorted(paths):
        for typ, prefix in TYPES.items():
            if path.startswith(prefix) and "/" not in path[len(prefix):]:
                m = NUMBER_PATH.match(path[len(prefix):])
                if m:
                    table[(typ, int(m.group(1)))].append(path)
    return dict(table)


def _resolve_reference(
    token: str, typ: str, *, origin: str,
    paths: set[str], index: dict[tuple[str, int], list[str]],
) -> tuple[str, str | None]:
    """Resolve one explicit citation; unknowns are not silently repaired."""
    if typ == "numbered":
        match = NUMBER.fullmatch(token)
        if match is None:
            raise ValueError("Invalid numbered reference")
        target = index.get((match.group("type").lower(),
                            int(match.group("number"))), [])
        if len(target) == 1:
            return "EXACT_RESOLVED", target[0]
        return ("AMBIGUOUS_NUMBERED" if target else "UNRESOLVED_NUMBERED"), None

    normalized = token
    if typ in {"markdown_link", "relative_path"}:
        normalized = token.split("#", 1)[0].split("?", 1)[0]
        if not normalized or re.match(r"^[a-z][a-z0-9+.-]*:", normalized, re.I):
            return "EXTERNAL_OR_FRAGMENT_LINK", None
        if normalized.startswith("/"):
            return "OUTSIDE_RELATIVE_SCOPE", None
        # Anchors include repository-root-relative paths and document-relative
        # links. Both are strictly resolved against the recorded source path.
        if normalized.startswith(("docs/", "src/", "frontend/", "tests/",
                                  "schemas/", "scripts/", "tools/", "migrations/")):
            pass
        else:
            normalized = posixpath.join(posixpath.dirname(origin), normalized)
    normalized = posixpath.normpath(normalized).rstrip(".,;:")
    if not world.safe_path(normalized) or normalized.startswith("./"):
        return "OUTSIDE_RELATIVE_SCOPE", None
    if normalized in paths:
        return "EXACT_RESOLVED", normalized
    if any(p.startswith(normalized.rstrip("/") + "/") for p in paths):
        return "DIRECTORY_ONLY", None
    return "UNRESOLVED_PATH", None


def references(
    text: str, origin: str, paths: set[str],
    index: dict[tuple[str, int], list[str]],
) -> list[dict]:
    """Record grounded lexical reference *occurrences*, never semantic edges."""
    found = []
    for line_number, line in enumerate(text.splitlines(), 1):
        candidates = (
            [("direct", match.group("path")) for match in DIRECT.finditer(line)]
            + [("numbered", match.group(0)) for match in NUMBER.finditer(line)]
            + [("markdown_link", match.group("target")) for match in LINK.finditer(line)]
            + [("relative_path", match.group("rel")) for match in RELATIVE.finditer(line)]
        )
        for typ, token in candidates:
            status, target = _resolve_reference(
                token, typ, origin=origin, paths=paths, index=index,
            )
            # Two mentions on one line may resolve to the same target.
            found.append({
                "line": line_number, "kind": typ, "status": status,
                "target": target,
                # Only local diagnostic receives tokens; public receipt
                # contains no source-specific names or user text.
                "literal_reference": token,
            })
    return sorted(
        {json.dumps(item, sort_keys=True): item for item in found}.values(),
        key=lambda v: (v["line"], v["kind"], v["literal_reference"]),
    )


def frontier(ledger: dict, bodies: dict[str, bytes]) -> tuple[dict, dict]:
    """Compute a conservative two-hop qualification frontier.

    A two-hop result is a review priority signal, NOT a verified dependency
    nor permission to exclude sources outside the frontier.
    """
    rows = ledger.get("source_records")
    if (
        not isinstance(rows, list) or
        ledger.get("roster_sha256") != world._fingerprint(rows) or
        ledger.get("source_count") != len(rows) or
        ledger.get("source_ref") is None or
        len({r["path"] for r in rows}) != len(rows)
    ):
        raise ValueError("Coverage ledger identity or population mismatch")
    paths = {r["path"] for r in rows}
    expected = {r["path"] for r in rows if r["visibility"] != world.MODALITY_HOLD}
    if set(bodies) != expected:
        raise ValueError("Incomplete or inappropriate text source body population")
    by_path = {r["path"]: r for r in rows}
    index = numbered_index(paths)
    outbound: dict[str, list[dict]] = {}
    targeted: dict[str, set[str]] = {}
    source_status_counts = Counter()
    unresolved = Counter()
    for row in rows:
        path = row["path"]
        if row["visibility"] == world.MODALITY_HOLD:
            outbound[path] = []
            targeted[path] = set()
            source_status_counts["UNSUPPORTED_NOT_INSPECTED"] += 1
            continue
        raw = bodies[path]
        if (
            sha256(raw).hexdigest() != row["sha256"] or
            len(raw) != row["bytes"] or world.sha1git(raw) != row["git_blob_oid"]
        ):
            raise ValueError("Blob evidence was not authenticated")
        if PurePosixPath(path).suffix.lower() not in DOCUMENT_SUFFIXES:
            outbound[path] = []
            targeted[path] = set()
            source_status_counts["NON_DOCUMENT_TEXT_NOT_PARSED"] += 1
            continue
        try:
            text = raw.decode("utf-8")
        except UnicodeDecodeError as exc:
            raise ValueError("Non-UTF8 previously admitted as text") from exc
        matches = references(text, path, paths, index)
        outbound[path] = matches
        source_status_counts["DOCUMENT_TEXT_SCANNED"] += 1
        targeted[path] = {m["target"] for m in matches
                          if m["status"] == "EXACT_RESOLVED"
                          and m["target"] != path}
        unresolved.update(m["status"] for m in matches
                          if m["status"] != "EXACT_RESOLVED")
    seeds = {r["path"] for r in rows
             if r["family_hint"] in CORE and
             r["visibility"] == "PRELIMINARY_CANDIDATE_UNQUALIFIED"}
    first = set().union(*(targeted[p] for p in seeds)) if seeds else set()
    second = set(first)
    for p in first:
        second.update(targeted[p])
    second.difference_update(seeds)
    critical = sorted(r["path"] for r in rows
                      if r["family_hint"] in CRITICAL)
    counts = defaultdict(Counter)
    review_rows = []
    for p in critical:
        row = by_path[p]
        evidence = {
            "direct_core_mention": p in first,
            "two_hop_core_mention": p in second and p not in first,
            "historical_lexical_or_path_flag": bool(row["flags"]),
            "unsupported_representation": row["visibility"] == world.MODALITY_HOLD,
            "no_detected_core_path": p not in second,
        }
        active = [k for k, v in evidence.items() if v]
        counts[row["family_hint"]]["TOTAL"] += 1
        for k in active:
            counts[row["family_hint"]][k] += 1
        review_rows.append({
            "path": p,
            "git_blob_oid": row["git_blob_oid"],
            "sha256": row["sha256"],
            "family_hint": row["family_hint"],
            "visibility": row["visibility"],
            "prospective_evidence_signals": evidence,
            "flags": row["flags"],
            "status": world.NO_ADMISSION,
            "source_specific_owner_or_non_arm_qualification": "PENDING",
        })
    if len(critical) != sum(v["TOTAL"] for v in counts.values()):
        raise ValueError("Critical historical sources not fully accounted for")
    body = {
        "schema_version": 1,
        "identifier": IDENTIFIER,
        "source_ref": ledger["source_ref"],
        "parent_roster_sha256": ledger["roster_sha256"],
        "classification": "NONSCORING_REVIEW_PRIORITY_EVIDENCE_NOT_AUTHOR_PACKET",
        "source_count": len(rows),
        "document_scan_counts": dict(sorted(source_status_counts.items())),
        "references_by_source": outbound,
        "review_candidate_records": review_rows,
        "unresolved_reference_counts": dict(sorted(unresolved.items())),
        "source_admissions": 0,
        "author_world": world.ROSTER_NOT_FROZEN,
        "limitations": [
            "Direct and two-hop references are lexical/citation mentions, not accepted semantic dependencies.",
            "Core anchor sources are unqualified, even when they resemble accepted governing or orientation sources.",
            "Unreferenced sources remain in the review population and cannot be declared irrelevant.",
            "References in code, implicit dependencies, exact D-IDs and alternative media may be missed.",
            "The frontier is a review-routing diagnostic, not a scored task or independent eligibility result.",
        ],
    }
    public = {
        "schema_version": 1,
        "identifier": IDENTIFIER,
        "source_ref": ledger["source_ref"],
        "parent_roster_sha256": ledger["roster_sha256"],
        "classification": "PUBLIC_SAFE_SOURCE_FREE_REVIEW_ROUTING_RECEIPT",
        "source_count": len(rows),
        "historical_critical_family_total": len(critical),
        "critical_family_signals": {
            family: dict(sorted(c.items())) for family, c in sorted(counts.items())
        },
        "document_scan_counts": dict(sorted(source_status_counts.items())),
        "unresolved_reference_counts": dict(sorted(unresolved.items())),
        "frontier_sha256": sha256(canonical(body)).hexdigest(),
        "source_admissions": 0,
        "author_world": world.ROSTER_NOT_FROZEN,
        "scored_author_packet": "NOT_CONSTRUCTED",
        "task_answerability": "NOT_PROVEN",
    }
    return body, public


def cross_family_summary(body: dict) -> dict:
    """Aggregate citation co-mentions between status and validation records.

    This is not evidence that a validation ran, a report passed, a project
    claim is true, or any source should be admitted. No source names emerge.
    """
    records = body.get("review_candidate_records")
    by_source = body.get("references_by_source")
    if not isinstance(records, list) or not isinstance(by_source, dict):
        raise ValueError("Incomplete source frontier")
    families = {r["path"]: r["family_hint"] for r in records}
    if len(families) != len(records):
        raise ValueError("Duplicate critical source record")
    edges = {
        (source, r["target"])
        for source, refs in by_source.items()
        for r in refs
        if r["status"] == "EXACT_RESOLVED"
        and r["target"] and r["target"] != source
    }
    status_to_validation = {
        (s, t) for s, t in edges
        if families.get(s) == "historical_status"
        and families.get(t) == "execution_evidence"
    }
    validation_to_status = {
        (s, t) for s, t in edges
        if families.get(s) == "execution_evidence"
        and families.get(t) == "historical_status"
    }
    validations = {
        p for p, role in families.items() if role == "execution_evidence"
    }
    referenced_validations = {t for _, t in status_to_validation}
    referencing_validations = {s for s, _ in validation_to_status}
    return {
        "classification": "SOURCE_FREE_TEXTUAL_CITATION_CO_MENTION_DIAGNOSTIC",
        "exact_resolved_reference_edges_all_families": len(edges),
        "status_to_validation_reference_edges": len(status_to_validation),
        "validation_to_status_reference_edges": len(validation_to_status),
        "distinct_status_documents_citing_validation": len({
            s for s, _ in status_to_validation
        }),
        "distinct_validation_documents_cited_by_status": len(
            referenced_validations
        ),
        "distinct_validation_documents_citing_status": len(
            referencing_validations
        ),
        "distinct_status_documents_cited_by_validation": len({
            t for _, t in validation_to_status
        }),
        "reciprocal_status_validation_pairs": len({
            (s, t) for s, t in status_to_validation
            if (t, s) in validation_to_status
        }),
        "validation_records_total": len(validations),
        "validation_with_detected_status_reference_either_direction": len(
            referenced_validations | referencing_validations
        ),
        "validation_without_detected_status_reference": len(
            validations - referenced_validations - referencing_validations
        ),
        "source_admissions": 0,
        "scientific_authority_and_answerability": "NOT_ESTABLISHED",
    }


def compute(repo: Path) -> tuple[dict, dict]:
    ledger, _ = world.compute(repo)
    return frontier(ledger, exact_blobs(repo, ledger["source_records"]))


def emit(repo: Path, *, verify_only: bool = False) -> dict:
    repo = repo.resolve(strict=True)
    if not (repo / ".git").is_dir():
        raise ValueError("Not a Git repository")
    output = repo / OUTDIR
    body, receipt = compute(repo)
    raw = canonical(body)
    safe = canonical(receipt)
    if verify_only:
        if (
            not (output / INTERNAL).is_file()
            or (output / INTERNAL).read_bytes() != raw
            or not (output / RECEIPT).is_file()
            or (output / RECEIPT).read_bytes() != safe
        ):
            raise ValueError("Historical dependency frontier not byte-reproducible")
        print("HISTORICAL_DEPENDENCY_FRONTIER_REPRODUCIBILITY=PASS")
    else:
        if (output / INTERNAL).exists() or (output / RECEIPT).exists():
            raise FileExistsError("Refusing to overwrite previous frontier")
        output.mkdir(parents=True, exist_ok=True)
        with (output / INTERNAL).open("xb") as f:
            f.write(raw)
        with (output / RECEIPT).open("xb") as f:
            f.write(safe)
    print(json.dumps(receipt, sort_keys=True))
    return receipt


if __name__ == "__main__":
    if len(sys.argv) not in (2, 3) or (
        len(sys.argv) == 3
        and sys.argv[2] not in {"--verify-only", "--cross-family"}
    ):
        raise SystemExit(
            "usage: python -m experiments.r0_p03_navigation_probe."
            "historical_evidence_dependency_frontier "
            "REPO [--verify-only|--cross-family]"
        )
    requested = sys.argv[2] if len(sys.argv) == 3 else None
    repo = Path(sys.argv[1])
    emit(repo, verify_only=requested is not None)
    if requested == "--cross-family":
        local = json.loads((repo.resolve() / OUTDIR / INTERNAL).read_text(
            encoding="utf-8"
        ))
        print(json.dumps(cross_family_summary(local), sort_keys=True))
