"""Arm-neutral non-scored lexical retrieval and derived-orientation preflight.

This adapter is deliberately not called an executed B0/B1/B2/B3/B4 arm.
It uses the complete historically pinned non-admission source population
as a LOCAL ENGINEERING SMOKE only. It has no scoring, author-facing interface,
gold, source admission, status oracle, J1 authority, J2 proof, or navigation
augmentation. All eventual arms must use an identical admitted corpus and
share the same lexical substrate before comparing semantic additions.

Source evidence remains exact path@commit@blob and content digests. File path
is never promoted to semantic identity or governing truth. In-memory FTS5
can be discarded and rebuilt without any source or authority mutation.
"""
from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path, PurePosixPath
import re
import sqlite3
import sys

from experiments.r0_p03_navigation_probe import (
    historical_evidence_dependency_frontier as frontier,
    source_world_coverage_gate as world,
)

IDENTIFIER = "R0_P03_NEUTRAL_UNSCORED_COMMON_LEXICAL_READONLY_V1"
UNKNOWN = "UNKNOWN_UNQUALIFIED"
NO_RELEASE = "NO_AUTHOR_RELEASE"
MAX_COUNT = 10_000
MAX_TOTAL_BYTES = 75_000_000
MAX_TERMS = 16
MAX_TERM_LENGTH = 96

# These nine shared capabilities are defined by Research 513, but only exact
# Git-source provenance and lexical full-text are exercised in this preflight.
SHARED_CAPABILITIES = (
    "information_role_and_natural_owner",
    "accepted_effect_id_and_exact_governed_subject",
    "lineage_and_currentness", "completion", "j2_coverage",
    "evidence_receipts", "authority_class_labels", "lexical_full_text",
    "connector_readable_derived_orientation",
)

UNQUALIFIED_CONCEPTS = (
    "information_role_and_natural_owner",
    "accepted_effect_id_and_exact_governed_subject",
    "lineage_and_currentness", "completion", "j2_coverage",
    "evidence_receipts", "authority_class_labels",
)


def canonical(value: object) -> bytes:
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), ensure_ascii=True,
    ).encode("ascii")


def _query_terms(query: str) -> str:
    """Escape all user input as literal FTS tokens, never an FTS expression."""
    if not isinstance(query, str) or len(query) > 256:
        raise ValueError("Lexical query length invalid")
    terms = re.findall(r"\w+", query, flags=re.UNICODE)
    if not 1 <= len(terms) <= MAX_TERMS or any(
        len(term) > MAX_TERM_LENGTH for term in terms
    ):
        raise ValueError("Invalid lexical query terms")
    return " AND ".join('"' + t.replace('"', '""') + '"' for t in terms)


def _check_rows(
    ledger: dict, bodies: dict[str, bytes],
) -> tuple[list[dict], str]:
    rows = ledger.get("source_records")
    if (
        not isinstance(rows, list) or not rows or len(rows) > MAX_COUNT
        or ledger.get("roster_sha256") != world._fingerprint(rows)
        or ledger.get("source_count") != len(rows)
        or not re.fullmatch("[0-9a-f]{40}", str(ledger.get("source_ref", "")))
    ):
        raise ValueError("Unqualified source ledger")
    eligible = [r for r in rows if r["visibility"] != world.MODALITY_HOLD]
    if set(bodies) != {r["path"] for r in eligible}:
        raise ValueError("Full, exact readable roster required for engineering test")
    if len({r["path"] for r in rows}) != len(rows):
        raise ValueError("Duplicate source identities")
    if sum(len(raw) for raw in bodies.values()) > MAX_TOTAL_BYTES:
        raise ValueError("Excessive candidate text")
    checked = []
    for r in sorted(eligible, key=lambda r: r["path"]):
        path = r["path"]
        if (
            not world.safe_path(path)
            or r["status"] != world.NO_ADMISSION
            or r["visibility"] not in {
                "PRELIMINARY_CANDIDATE_UNQUALIFIED", "HISTORICAL_REVIEW_ONLY",
            }
        ):
            raise ValueError("Attempted candidate source promotion")
        raw = bodies[path]
        if (
            not isinstance(raw, bytes)
            or sha256(raw).hexdigest() != r["sha256"]
            or world.sha1git(raw) != r["git_blob_oid"]
            or len(raw) != r["bytes"]
        ):
            raise ValueError("Unpinned lexical source content")
        try:
            raw.decode("utf-8")
        except UnicodeError as exc:
            raise ValueError("Unreadable lexical source content") from exc
        checked.append(r)
    return checked, sha256(canonical([
        {"path": r["path"], "blob_oid": r["git_blob_oid"],
         "sha256": r["sha256"], "bytes": r["bytes"]}
        for r in checked
    ])).hexdigest()


class NeutralReadOnlyIndex:
    """An ephemeral FTS5 source-index with no semantic authority semantics.

    The only mutable operation is construction. The index is switched to
    SQLite query_only immediately after ingestion. Rebuild must instantiate
    a new adapter from the unchanged pinned source objects.
    """

    def __init__(self, ledger: dict, bodies: dict[str, bytes]) -> None:
        checked, self.source_digest = _check_rows(ledger, bodies)
        self.source_ref = ledger["source_ref"]
        self.roster_digest = ledger["roster_sha256"]
        self.unsupported_count = len(ledger["source_records"]) - len(checked)
        self.readable_count = len(checked)
        self.total_bytes = sum(r["bytes"] for r in checked)
        self._conn = sqlite3.connect(":memory:")
        try:
            self._conn.execute(
                "CREATE TABLE carriers (path TEXT PRIMARY KEY, "
                "git_blob_oid TEXT NOT NULL, sha256 TEXT NOT NULL, "
                "bytes INTEGER NOT NULL)"
            )
            self._conn.execute(
                "CREATE VIRTUAL TABLE lex USING fts5(path UNINDEXED, "
                "content, tokenize='unicode61')"
            )
            for r in checked:
                path = r["path"]
                text = bodies[path].decode("utf-8")
                self._conn.execute(
                    "INSERT INTO carriers(path,git_blob_oid,sha256,bytes) "
                    "VALUES(?,?,?,?)",
                    (path, r["git_blob_oid"], r["sha256"], r["bytes"]),
                )
                self._conn.execute(
                    "INSERT INTO lex(path,content) VALUES(?,?)",
                    (path, text),
                )
            self._conn.commit()
            self._conn.execute("PRAGMA query_only=ON")
        except BaseException:
            self._conn.close()
            raise

    def search(self, query: str, *, limit: int = 10) -> list[dict]:
        """Lexical evidence candidates only; never claims of relevance or truth."""
        if type(limit) is not int or not 1 <= limit <= 50:
            raise ValueError("Invalid retrieval limit")
        fts = _query_terms(query)
        found = self._conn.execute(
            "SELECT c.path,c.git_blob_oid,c.sha256,c.bytes,bm25(lex) as score "
            "FROM lex JOIN carriers AS c ON lex.path=c.path "
            "WHERE lex MATCH ? ORDER BY score ASC,c.path ASC LIMIT ?",
            (fts, limit),
        ).fetchall()
        return [
            {
                "source_path": path,
                "git_commit": self.source_ref,
                "git_blob_oid": blob_oid,
                "sha256": digest,
                "bytes": byte_count,
                "lexical_score": score,
                "authority_status": UNKNOWN,
                "source_admission": NO_RELEASE,
            }
            for path, blob_oid, digest, byte_count, score in found
        ]

    def orientation(self) -> dict:
        """Connector-readable derived orientation, deliberately no truth claims."""
        return {
            "schema_version": 1,
            "identifier": IDENTIFIER,
            "source_head_or_checkpoint": self.source_ref,
            "generated_from_source_digests": {
                "full_nonadmission_roster": self.roster_digest,
                "readable_text_subset": self.source_digest,
            },
            "derived_non_authoritative_label": True,
            "current_governing_summary": UNKNOWN,
            "navigation_entry_points": [],
            "staleness_visible": "HISTORICAL_PIN_NOT_LIVE_CURRENTNESS",
            "shared_capabilities": {
                item: (
                    "ENGINEERING_IMPLEMENTATION_ONLY"
                    if item in {"lexical_full_text", "connector_readable_derived_orientation"}
                    else "SEMANTIC_GROUND_TRUTH_NOT_QUALIFIED"
                )
                for item in SHARED_CAPABILITIES
            },
            "readable_source_count": self.readable_count,
            "unsupported_source_count": self.unsupported_count,
            "source_admission": NO_RELEASE,
            "experiment_role": "UNSCORED_COMMON_SUBSTRATE_ENGINEERING_ONLY",
            "scored_tasks": "NONE",
            "authority_replacement": "NONE",
        }

    def carrier_identity(self, path: str) -> dict | None:
        """Provenance only; no source owner or accepted-effect inference."""
        if not world.safe_path(path):
            raise ValueError("Invalid source identity path")
        row = self._conn.execute(
            "SELECT git_blob_oid,sha256,bytes FROM carriers WHERE path=?",
            (path,),
        ).fetchone()
        if row is None:
            return None
        return {
            "source_path": path, "git_commit": self.source_ref,
            "git_blob_oid": row[0], "sha256": row[1], "bytes": row[2],
            "information_role": UNKNOWN, "natural_owner": UNKNOWN,
            "evidence_class": "PINNED_HISTORICAL_TEXT_UNQUALIFIED",
            "authority_currentness_basis": UNKNOWN,
            "source_admission": NO_RELEASE,
        }

    def close(self) -> None:
        self._conn.close()


def run_real_preflight(repo: Path) -> dict:
    """Build, validate, discard, and rebuild the same common index.

    No task queries, scored evals, per-source contents, source decisions or
    author-facing packets may leave this operation.
    """
    repo = repo.resolve(strict=True)
    ledger, source_receipt = world.compute(repo)
    bodies = frontier.exact_blobs(repo, ledger["source_records"])
    index = NeutralReadOnlyIndex(ledger, bodies)
    first = index.orientation()
    try:
        if (
            index.readable_count + index.unsupported_count
            != source_receipt["complete_roster_records"]
        ):
            raise ValueError("Index population drift")
        # This operation verifies the FTS5 engine without authoring any task.
        # No query hits or source identities are printed or scored.
        assert index._conn.execute(
            "SELECT COUNT(*) FROM carriers"
        ).fetchone()[0] == index.readable_count
        assert index._conn.execute(
            "SELECT COUNT(*) FROM lex"
        ).fetchone()[0] == index.readable_count
    finally:
        index.close()
    second_index = NeutralReadOnlyIndex(ledger, bodies)
    try:
        second = second_index.orientation()
        if canonical(first) != canonical(second):
            raise ValueError("Ephemeral lexical common substrate rebuild drift")
    finally:
        second_index.close()
    report = {
        "identifier": IDENTIFIER,
        "source_ref": world.PIN,
        "source_world_digest": first["generated_from_source_digests"][
            "full_nonadmission_roster"],
        "text_digest": first["generated_from_source_digests"]["readable_text_subset"],
        "readable_text_count": first["readable_source_count"],
        "unsupported_count": first["unsupported_source_count"],
        "fts5_engine": sqlite3.sqlite_version,
        "ephemeral_delete_and_rebuild_parity": "PASS",
        "common_orientation_equal": True,
        "authority_currentness": UNKNOWN,
        "source_admission": NO_RELEASE,
        "scored_task_or_arm_execution": "NONE",
    }
    print(json.dumps(report, sort_keys=True))
    return report


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("usage: python -m experiments.r0_p03_navigation_probe."
                         "neutral_readonly_retrieval_candidate REPO")
    run_real_preflight(Path(sys.argv[1]))
