"""Bounded, fictional-only S1 transport and journal mechanics demonstrator.

This module deliberately does not operate on the Autonomous Data Science System
historical corpus.  Its three source files are constants defined here; no Git
revision, project document, network resource, connected account, key, or
reviewer-private note is an input.  The demonstration explores failure modes
that a future S1 implementation must address, without implying that local
filesystem writes, Python actor labels, or SHA-256 chains establish actual
confidentiality, non-repudiation, process isolation, or independent judgment.

The verification routines are strict about manifest identity, delivered bytes,
undisclosed extra content, and append-only event ordering.  This is not a source
classifier, author packet builder, credential manager, or release endpoint.
"""
from __future__ import annotations

from dataclasses import dataclass
import hashlib
import json
import os
from pathlib import Path
import re
from typing import Mapping

SYNTHETIC_MARKER = "S1_FICTIONAL_ONLY_NO_REAL_PROJECT_SOURCES_OR_GOLD"
SYNTHETIC_REF = "synthetic-s1-fixture-v1"
JOURNAL_FILENAME = "synthetic_s1_events.jsonl"
ZERO_HASH = "0" * 64
ACTORS = frozenset({"SIMULATED_REVIEWER", "SIMULATED_CHALLENGER", "SIMULATED_AUTHORIZER"})
SUBJECT_PATTERN = re.compile(r"s1_fake_[a-z0-9_]+\Z")
KNOWN_ACTIONS = frozenset(
    {"PROPOSE", "CHALLENGE_ACCEPT", "CHALLENGE_DISPUTE", "SIMULATED_READY", "INVALIDATE"}
)
FAKE_SOURCE_BYTES: Mapping[str, bytes] = {
    "fictional_observation.txt": (
        f"{SYNTHETIC_MARKER}\nFictional river height was recorded on day 4.\n"
    ).encode("utf-8"),
    "fictional_rule.txt": (
        f"{SYNTHETIC_MARKER}\nThe fictional bridge gate opens at dusk.\n"
        "Exceptions are declared separately in fictional_exception.txt.\n"
    ).encode("utf-8"),
    "fictional_exception.txt": (
        f"{SYNTHETIC_MARKER}\nFictional bridge exceptions apply on festival days.\n"
    ).encode("utf-8"),
}


def _sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _git_blob_oid(data: bytes) -> str:
    """Compute Git's uncompressed blob identity, not a commit or source authority."""
    return hashlib.sha1(b"blob " + str(len(data)).encode("ascii") + b"\0" + data).hexdigest()


@dataclass(frozen=True)
class FixtureRecord:
    path: str
    byte_count: int
    sha256: str
    git_blob_oid: str


@dataclass(frozen=True)
class SyntheticManifest:
    marker: str
    ref: str
    sources: tuple[FixtureRecord, ...]
    digest: str


@dataclass(frozen=True)
class DeliveryReport:
    status: str
    missing: tuple[str, ...]
    modified: tuple[str, ...]
    unexpected: tuple[str, ...]
    verified_count: int


def build_fixed_manifest() -> SyntheticManifest:
    """Bind the only authorized trial inputs to exact byte and Git-blob hashes."""
    records = tuple(
        FixtureRecord(name, len(blob), _sha256(blob), _git_blob_oid(blob))
        for name, blob in sorted(FAKE_SOURCE_BYTES.items())
    )
    payload = {
        "marker": SYNTHETIC_MARKER,
        "ref": SYNTHETIC_REF,
        "sources": [record.__dict__ for record in records],
    }
    digest = _sha256(json.dumps(payload, sort_keys=True, separators=(",", ":")).encode())
    return SyntheticManifest(SYNTHETIC_MARKER, SYNTHETIC_REF, records, digest)


def verify_delivery(
    manifest: SyntheticManifest, received: Mapping[str, bytes]
) -> DeliveryReport:
    """Fail closed on absent, changed, incorrectly typed, or unexpected bytes.

    A verified manifest is not proof that anyone read or understood the text.
    This function accepts only the fixed fictional manifest to ensure the
    demo cannot be invoked as an authorization path for actual ADS sources.
    """
    if manifest != build_fixed_manifest():
        raise ValueError("Only the exact fixed fictional manifest is permitted")
    if not isinstance(received, Mapping):
        raise TypeError("Received batch must be an in-memory mapping")
    known = {item.path: item for item in manifest.sources}
    missing = tuple(sorted(set(known) - set(received)))
    unexpected = tuple(sorted(set(received) - set(known)))
    modified: list[str] = []
    verified = 0
    for name in sorted(set(received) & set(known)):
        blob = received[name]
        identity = known[name]
        if (
            not isinstance(blob, bytes)
            or len(blob) != identity.byte_count
            or _sha256(blob) != identity.sha256
            or _git_blob_oid(blob) != identity.git_blob_oid
            or not blob.startswith(SYNTHETIC_MARKER.encode())
        ):
            modified.append(name)
        else:
            verified += 1
    status = "PASS" if not (missing or unexpected or modified) else "HOLD_DELIVERY"
    return DeliveryReport(status, missing, tuple(modified), unexpected, verified)


@dataclass(frozen=True)
class ScopeScreen:
    status: str
    blockers: tuple[str, ...]


def screen_fictional_scope(
    *,
    delivery_complete: bool,
    confirmed_protected_in_exposure: bool,
    material_possible_leak: bool = False,
    context_complete: bool = True,
) -> ScopeScreen:
    """Preserve a confirmed synthetic prohibition even if delivery is incomplete.

    The inputs are manually supplied simulated observations, NOT contamination
    or context judgments inferred by code.  The result is a typed trial
    screening outcome, not permission to release even these fictional files.
    """
    blockers = []
    if confirmed_protected_in_exposure:
        blockers.append("CONFIRMED_PROTECTED_EXPOSURE")
    if not delivery_complete:
        blockers.append("MISSING_BYTES")
    if material_possible_leak:
        blockers.append("MATERIAL_POSSIBLE_DISCLOSURE")
    if not context_complete:
        blockers.append("CONTEXT_DEPENDENCY_OPEN")
    if confirmed_protected_in_exposure:
        status = "PROHIBITED_EXPOSURE"
    elif blockers:
        status = "RELEASE_HOLD"
    else:
        status = "ELIGIBLE_PROPOSED"
    return ScopeScreen(status, tuple(blockers))


def screen_fictional_author_view(
    *,
    dynamic_loaded_asset: bool = False,
    navigable_unfrozen_link: bool = False,
    generated_metadata_leak: bool = False,
    public_receipt_join_leak: bool = False,
    inert_nonmaterial_citation: bool = False,
) -> ScopeScreen:
    """Model distinct disclosure channels without making real network requests."""
    blockers = tuple(
        name for condition, name in (
            (dynamic_loaded_asset, "DYNAMIC_LOADED_ASSET"),
            (navigable_unfrozen_link, "NAVIGABLE_UNFROZEN_LINK"),
            (generated_metadata_leak, "VIEWER_GENERATED_METADATA_LEAK"),
            (public_receipt_join_leak, "PUBLIC_RECEIPT_JOIN_LEAK"),
        )
        if condition
    )
    # An actual inert citation is never navigable, loaded, or context-material.
    # Its presence alone is not an independent disclosure risk.
    _ = inert_nonmaterial_citation
    return ScopeScreen("RELEASE_HOLD" if blockers else "ELIGIBLE_PROPOSED", blockers)


def screen_fictional_bundle(
    *, members: frozenset[str], required_members: frozenset[str],
    prohibited_members: frozenset[str] = frozenset(),
) -> ScopeScreen:
    """Evaluate an atomic conditional bundle instead of a circular item-by-item release.

    This only checks an explicitly enumerated fake dependency set.  It does
    not prove that all real governing qualifications have been discovered.
    """
    if not members or any(not SUBJECT_PATTERN.fullmatch(s) for s in members | required_members | prohibited_members):
        raise ValueError("Only explicitly enumerated fictional subjects are supported")
    blockers = []
    if prohibited_members & members:
        blockers.append("CONFIRMED_PROTECTED_COMPONENT")
    if not required_members <= members:
        blockers.append("MISSING_REQUIRED_CONTEXT")
    if prohibited_members & members:
        return ScopeScreen("PROHIBITED_EXPOSURE", tuple(blockers))
    return ScopeScreen("RELEASE_HOLD" if blockers else "CONDITIONALLY_ELIGIBLE", tuple(blockers))


def _canonical(obj: object) -> bytes:
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=True).encode()


class JournalError(ValueError):
    """A synthetic append-only journal or state transition is invalid."""


class SyntheticJournal:
    """Persist *fictional* event identities with sequential hash-linked records.

    The format detects accidental edits, partial writes and missing/reordered
    records when verified against the observed prior digest.  A malicious
    writer able to replace all file bytes can recompute the hashes, so it does
    NOT establish tamper-proof storage, authentication, confidentiality or
    separation of Windows accounts.  Actor strings are mock labels only.

    Every append is fsynced and replayed on read.  Incomplete final JSONL
    records fail closed; there is intentionally no implicit truncate/recover
    path that might silently accept or lose a reviewer decision.  Actual
    durable recovery would require a separately qualified private store,
    atomic commit and external digest/counter custody.
    """

    def __init__(self, path: Path) -> None:
        if path.name != JOURNAL_FILENAME or not path.parent.is_dir():
            raise JournalError("Only a test-owned, explicitly named synthetic journal is supported")
        self.path = path
        if not path.exists():
            with path.open("xb"):
                pass
        self.events = self._read_verified()

    def _read_verified(self) -> list[dict]:
        content = self.path.read_bytes()
        if content and not content.endswith(b"\n"):
            raise JournalError("Torn final journal record")
        previous = ZERO_HASH
        seen: set[str] = set()
        events: list[dict] = []
        for line in content.splitlines():
            try:
                row = json.loads(line.decode("ascii"))
            except (ValueError, UnicodeDecodeError) as exc:
                raise JournalError("Invalid journal record") from exc
            if not isinstance(row, dict) or set(row) != {"core", "hash"}:
                raise JournalError("Unexpected journal record fields")
            core = row["core"]
            if not isinstance(core, dict) or set(core) != {
                "marker", "seq", "previous", "event_id", "action", "actor",
                "subject", "dependencies",
            }:
                raise JournalError("Unexpected journal event fields")
            if (
                core["marker"] != SYNTHETIC_MARKER
                or type(core["seq"]) is not int or core["seq"] != len(events) + 1
                or core["previous"] != previous
                or not isinstance(core["event_id"], str)
                or not SUBJECT_PATTERN.fullmatch(core["event_id"])
                or not isinstance(core["subject"], str)
                or not SUBJECT_PATTERN.fullmatch(core["subject"])
                or core["action"] not in KNOWN_ACTIONS
                or core["actor"] not in ACTORS
                or not isinstance(core["dependencies"], list)
                or any(not isinstance(d, str) or not SUBJECT_PATTERN.fullmatch(d) for d in core["dependencies"])
                or core["event_id"] in seen
            ):
                raise JournalError("Invalid event identity, marker, actor or sequence")
            expected = _sha256(core["previous"].encode("ascii") + b":" + _canonical(core))
            if row["hash"] != expected:
                raise JournalError("Hash-chain mismatch")
            self._validate_transition(events, core)
            events.append(core)
            seen.add(core["event_id"])
            previous = expected
        return events

    @staticmethod
    def _validate_transition(history: list[dict], candidate: dict) -> None:
        action, actor, subject = candidate["action"], candidate["actor"], candidate["subject"]
        previous_subject = [e for e in history if e["subject"] == subject]
        last = previous_subject[-1]["action"] if previous_subject else None
        if action == "PROPOSE":
            if actor != "SIMULATED_REVIEWER" or (last is not None and last != "INVALIDATE"):
                raise JournalError("A proposal must be reviewer-authored and new or invalidated")
            if subject in candidate["dependencies"]:
                raise JournalError("Self-dependency is not a valid fictional trial")
        elif action in {"CHALLENGE_ACCEPT", "CHALLENGE_DISPUTE"}:
            if actor != "SIMULATED_CHALLENGER" or last != "PROPOSE" or candidate["dependencies"]:
                raise JournalError("Only an independent mock challenger can challenge a proposal")
        elif action == "SIMULATED_READY":
            if actor != "SIMULATED_AUTHORIZER" or last != "CHALLENGE_ACCEPT" or candidate["dependencies"]:
                raise JournalError("A simulated release requires a mock accepted challenge")
        elif action == "INVALIDATE":
            if actor not in {"SIMULATED_REVIEWER", "SIMULATED_CHALLENGER"} or last is None or last == "INVALIDATE" or candidate["dependencies"]:
                raise JournalError("Invalid source revision/invalidation transition")
        if action != "PROPOSE" and candidate["dependencies"]:
            raise JournalError("Only proposals may declare dependencies")

    def append(
        self, *, event_id: str, subject: str, actor: str,
        action: str, dependencies: tuple[str, ...] = (),
    ) -> str:
        """Append and fsync one validated fictional event; return its chain digest."""
        if not SUBJECT_PATTERN.fullmatch(event_id) or not SUBJECT_PATTERN.fullmatch(subject):
            raise JournalError("Actual source identifiers are forbidden in synthetic events")
        if actor not in ACTORS or action not in KNOWN_ACTIONS:
            raise JournalError("Unrecognized fictional actor/action")
        if any(not SUBJECT_PATTERN.fullmatch(d) for d in dependencies):
            raise JournalError("Nonfictional dependency identifier")
        self.events = self._read_verified()
        previous = ZERO_HASH if not self.events else self._latest_digest()
        core = {
            "marker": SYNTHETIC_MARKER,
            "seq": len(self.events) + 1,
            "previous": previous,
            "event_id": event_id,
            "action": action,
            "actor": actor,
            "subject": subject,
            "dependencies": list(dependencies),
        }
        if any(e["event_id"] == event_id for e in self.events):
            raise JournalError("Duplicate event/replay refused")
        self._validate_transition(self.events, core)
        digest = _sha256(previous.encode("ascii") + b":" + _canonical(core))
        with self.path.open("ab") as handle:
            handle.write(_canonical({"core": core, "hash": digest}) + b"\n")
            handle.flush()
            os.fsync(handle.fileno())
        self.events = self._read_verified()
        return digest

    def _latest_digest(self) -> str:
        if not self.events:
            return ZERO_HASH
        core = self.events[-1]
        return _sha256(core["previous"].encode("ascii") + b":" + _canonical(core))

    def verify_external_anchor(self, *, expected_digest: str, expected_event_count: int) -> bool:
        """Verify a caller-provided expected journal head, not just internal links.

        A valid shorter journal is internally consistent, so detecting silent
        truncation requires a separately preserved expected sequence and digest.
        This function proves only comparison correctness.  It does not protect
        that expected anchor from forgery or establish independent custody.
        """
        self.events = self._read_verified()
        if (
            type(expected_event_count) is not int
            or len(self.events) != expected_event_count
            or not isinstance(expected_digest, str)
            or self._latest_digest() != expected_digest
        ):
            raise JournalError("Independent expected journal anchor mismatch")
        return True

    def inspect_restricted_events(self, role: str) -> tuple[dict, ...]:
        """A simulated policy check, emphatically NOT an operating-system ACL."""
        if role not in ACTORS:
            raise PermissionError("Mock author or other actor has no simulated ledger read access")
        self.events = self._read_verified()
        return tuple(dict(e) for e in self.events)

    def simulated_release_ready(self, subject: str) -> bool:
        """Check fake local event prerequisites and dependency invalidations.

        This is intentionally named 'simulated': a True value is NOT an
        authorization, and it cannot export or disclose source content.
        """
        self.events = self._read_verified()
        latest = {event["subject"]: event for event in self.events}
        def ready(key: str, visiting: frozenset[str]) -> bool:
            if key in visiting or key not in latest or latest[key]["action"] != "SIMULATED_READY":
                return False
            proposals = [e for e in self.events if e["subject"] == key and e["action"] == "PROPOSE"]
            if not proposals:
                return False
            for dep in proposals[-1]["dependencies"]:
                if not ready(dep, visiting | {key}):
                    return False
                # Parent reapproval after this dependent was authorized must
                # never reactivate the old dependent decision.  Even if the
                # parent is now valid again, the changed evidence/context
                # requires a fresh dependent challenge and approval event.
                if latest[dep]["seq"] > latest[key]["seq"]:
                    return False
            return True
        return ready(subject, frozenset())
