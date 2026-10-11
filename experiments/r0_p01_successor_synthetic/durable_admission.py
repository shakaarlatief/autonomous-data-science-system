"""Experimental durable per-run admission journal for synthetic R0-P01.

SQLite BEGIN IMMEDIATE serializes writers. A commit atomically persists a
consumed acceptance ID, the fully signed record, and the end-of-journal
anchor. Every read cryptographically re-verifies and replays records through
the original V02 Ledger before trusting restored roles and dependencies.

This is NOT a qualified successor implementation. The old signed statement
lacks a unique per-run nonce, so a new unrelated database could accept a
signature from a different run. Hash chains detect accidental corruption but
not malicious database replacement or externally unanchored rollback. The
synthetic prefix prevents accidental live use. Only public credentials and
synthetic proof records should ever reach this prototype.
"""
from __future__ import annotations

import copy
import hashlib
from contextlib import closing
import re
import sqlite3
from pathlib import Path
from typing import Any

from experiments.r0_p01_owner_acceptance_v01 import harness as historical


class DurableJournalError(RuntimeError):
    """Persisted evidence is inconsistent or no longer independently valid."""


class SyntheticDurableLedger:
    """SQLite-backed, replay-verified single-run admission prototype."""

    SCHEMA_VERSION = 1
    GENESIS_DOMAIN = b"ADS-R0-P01-SYNTHETIC-JOURNAL-GENESIS-V01\0"

    def __init__(
        self, path: str | Path, *, run_id: str, fixture: dict,
        arm: str, primary: dict, recovery: dict, a_primary: dict,
        a_recovery: dict, scenario: str = "BURDEN", create: bool = False,
    ) -> None:
        if not re.fullmatch(r"SYNTHETIC-[A-Za-z0-9_-]{8,100}", run_id):
            raise ValueError("only synthetic run IDs permitted")
        if arm not in ("A", "B") or not isinstance(scenario, str) or not scenario:
            raise ValueError("invalid synthetic arm/scenario")
        self.path = Path(path)
        self._config = copy.deepcopy({
            "run_id": run_id, "fixture": fixture, "arm": arm,
            "primary": primary, "recovery": recovery,
            "a_primary": a_primary, "a_recovery": a_recovery,
            "scenario": scenario,
        })
        self._config_bytes = historical.canonical(self._config)
        self._genesis_hash = hashlib.sha256(
            self.GENESIS_DOMAIN + self._config_bytes
        ).hexdigest()
        if not self.path.parent.is_dir():
            raise DurableJournalError("parent directory missing")
        if create:
            try:
                self.path.touch(exist_ok=False)
            except FileExistsError as e:
                raise DurableJournalError("fresh journal path already exists") from e
        elif not self.path.is_file():
            raise DurableJournalError("durable journal missing; restart cannot create blank state")
        self._initialize(create=create)

    def _connect(self) -> sqlite3.Connection:
        conn = sqlite3.connect(str(self.path), timeout=15, isolation_level=None)
        conn.execute("PRAGMA busy_timeout=15000")
        conn.execute("PRAGMA synchronous=FULL")
        conn.execute("PRAGMA foreign_keys=ON")
        return conn

    def _initialize(self, *, create: bool) -> None:
        with closing(self._connect()) as conn:
            try:
                conn.execute("PRAGMA journal_mode=WAL")
                conn.execute("BEGIN IMMEDIATE")
                conn.execute(
                    """CREATE TABLE IF NOT EXISTS journal_identity (
                        id INTEGER PRIMARY KEY CHECK(id=1),
                        schema_version INTEGER NOT NULL,
                        context_blob BLOB NOT NULL,
                        sequence INTEGER NOT NULL,
                        head_sha256 TEXT NOT NULL
                    )"""
                )
                conn.execute(
                    """CREATE TABLE IF NOT EXISTS accepted (
                        sequence INTEGER PRIMARY KEY CHECK(sequence>0),
                        acceptance_id TEXT NOT NULL UNIQUE,
                        record_blob BLOB NOT NULL,
                        record_sha256 TEXT NOT NULL,
                        chain_sha256 TEXT NOT NULL
                    )"""
                )
                row = conn.execute(
                    "SELECT schema_version, context_blob, sequence, head_sha256 "
                    "FROM journal_identity WHERE id=1"
                ).fetchone()
                if row is None:
                    if not create:
                        raise DurableJournalError("reopening journal without genesis forbidden")
                    if conn.execute("SELECT 1 FROM accepted LIMIT 1").fetchone():
                        raise DurableJournalError("missing genesis with accepted rows")
                    conn.execute(
                        "INSERT INTO journal_identity VALUES (1, ?, ?, 0, ?)",
                        (self.SCHEMA_VERSION, self._config_bytes, self._genesis_hash),
                    )
                else:
                    self._check_identity(row)
                conn.commit()
            except Exception:
                conn.rollback()
                raise

    def _check_identity(self, row: tuple[Any, ...]) -> None:
        version, context, sequence, head = row
        if version != self.SCHEMA_VERSION or bytes(context) != self._config_bytes:
            raise DurableJournalError("run, fixture, or initial trust identity changed")
        if (
            not isinstance(sequence, int) or sequence < 0
            or not isinstance(head, str)
            or not re.fullmatch("[0-9a-f]{64}", head)
        ):
            raise DurableJournalError("invalid durable journal header")

    @staticmethod
    def _chain_hash(
        previous: str, sequence: int, acceptance_id: str, payload: bytes
    ) -> str:
        return hashlib.sha256(
            bytes.fromhex(previous)
            + sequence.to_bytes(8, "big")
            + acceptance_id.encode("utf-8") + b"\0" + payload
        ).hexdigest()

    def _reconstruct(self, conn: sqlite3.Connection, node):
        identity = conn.execute(
            "SELECT schema_version, context_blob, sequence, head_sha256 "
            "FROM journal_identity WHERE id=1"
        ).fetchone()
        if identity is None:
            raise DurableJournalError("journal identity missing")
        self._check_identity(identity)
        cfg = self._config
        ledger = historical.Ledger(
            cfg["fixture"], cfg["arm"], cfg["primary"], cfg["recovery"],
            cfg["a_primary"], cfg["a_recovery"], cfg["scenario"],
        )
        count = 0
        head = self._genesis_hash
        for seq, acceptance_id, payload, record_sha, chain_sha in conn.execute(
            "SELECT sequence, acceptance_id, record_blob, record_sha256, "
            "chain_sha256 FROM accepted ORDER BY sequence"
        ):
            count += 1
            if seq != count or not isinstance(acceptance_id, str) or not isinstance(payload, bytes):
                raise DurableJournalError("persisted sequence or record type invalid")
            if hashlib.sha256(payload).hexdigest() != record_sha:
                raise DurableJournalError("persisted record byte digest mismatch")
            head = self._chain_hash(head, count, acceptance_id, payload)
            if head != chain_sha:
                raise DurableJournalError("persisted chain digest mismatch")
            try:
                record = historical.strict_json(payload)
                if historical.canonical(record) != payload:
                    raise DurableJournalError("noncanonical persistent record")
                if record["statement"]["acceptance_id"] != acceptance_id:
                    raise DurableJournalError("persisted acceptance identity mismatch")
                result = ledger.admit(record, node)
            except (KeyError, TypeError, ValueError, historical.IntegrityError) as e:
                raise DurableJournalError("malformed persisted acceptance") from e
            if not result["admitted"]:
                raise DurableJournalError("previously accepted signature/context fails replay")
            if result["sequence"] != count + 1:
                raise DurableJournalError("persisted trust sequence divergence")
        if identity[2] != count or identity[3] != head:
            raise DurableJournalError("journal anchor mismatch or truncated rows")
        return ledger, count, head

    @staticmethod
    def _commit_transaction(conn: sqlite3.Connection) -> None:
        """Separate commit seam for deterministic abrupt-exit test injection."""
        conn.commit()

    def admit(self, record: dict, node) -> dict:
        """Commit one authorized action atomically or reject without mutation."""
        with closing(self._connect()) as conn:
            try:
                conn.execute("BEGIN IMMEDIATE")
                ledger, seq, head = self._reconstruct(conn, node)
                try:
                    payload = historical.canonical(record)
                except (ValueError, TypeError, UnicodeError):
                    conn.rollback()
                    return {"admitted": False, "reason": "MALFORMED_RECORD"}
                outcome = ledger.admit(copy.deepcopy(record), node)
                if not outcome["admitted"]:
                    conn.rollback()
                    return outcome
                acceptance_id = record["statement"]["acceptance_id"]
                next_seq = seq + 1
                next_head = self._chain_hash(head, next_seq, acceptance_id, payload)
                conn.execute(
                    "INSERT INTO accepted VALUES (?, ?, ?, ?, ?)",
                    (next_seq, acceptance_id, payload, hashlib.sha256(payload).hexdigest(), next_head),
                )
                conn.execute(
                    "UPDATE journal_identity SET sequence=?, head_sha256=? WHERE id=1",
                    (next_seq, next_head),
                )
                self._commit_transaction(conn)
                return outcome
            except Exception:
                conn.rollback()
                raise

    def snapshot(self, node) -> dict:
        """Reconstruct public trust state after verifying every durable proof."""
        with closing(self._connect()) as conn:
            try:
                conn.execute("BEGIN")
                ledger, count, head = self._reconstruct(conn, node)
                out = {
                    "run_id": self._config["run_id"],
                    "arm": self._config["arm"],
                    "accepted_count": count,
                    "head_sha256": head,
                    "consumed": sorted(ledger.consumed),
                    "signer_set_version": ledger.version,
                    "members": copy.deepcopy(ledger.members),
                    "effects": copy.deepcopy(ledger.effects),
                    "entries": copy.deepcopy(ledger.entries),
                }
                conn.commit()
                return out
            except Exception:
                conn.rollback()
                raise
