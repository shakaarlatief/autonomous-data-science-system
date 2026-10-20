"""Source-free S1 role and publication-boundary policy simulation.

The inputs are invented identifiers, role assignments, and risk scenarios. This
module does not authenticate anyone, store protected reviewer evidence, inspect
historical project files, read credentials, or release any real source content.

Its purpose is to make intended policy *decisions* explicit and falsifiable
before deciding where authority comes from in a real operating system, service,
agent connector, or owner-controlled review process. A caller able to alter the
fake assignments, event history, or simulated observations can forge the entire
demonstration. In particular, checking a string session identifier is not
authentication and cannot certify independent model context.
"""

from __future__ import annotations

from dataclasses import dataclass, field
import re
from typing import Mapping

FAKE_MARKER = "S1_SYNTHETIC_ROLE_BOUNDARY_NO_PRIVATE_CONTENT"
FAKE_ID = re.compile(r"s1_fake_[a-z0-9_]+\Z")
ROLES = frozenset({
    "REVIEWER", "CHALLENGER", "AUTHORIZER", "BLIND_AUTHOR",
    "PUBLIC_COORDINATOR",
})
ROLE_ACTIONS: Mapping[str, frozenset[str]] = {
    "REVIEWER": frozenset({"READ_REVIEW_BATCH", "WRITE_REVIEW_PROPOSAL"}),
    "CHALLENGER": frozenset({"READ_REVIEW_LEDGER", "WRITE_CHALLENGE"}),
    "AUTHORIZER": frozenset({"READ_CHALLENGED_PACKET", "SIMULATE_AUTHORIZATION"}),
    "BLIND_AUTHOR": frozenset({"READ_SIMULATED_AUTHOR_PACKET"}),
    "PUBLIC_COORDINATOR": frozenset({"READ_NONANSWER_RECEIPT"}),
}
PRIVATE_ACTIONS = frozenset({
    "READ_REVIEW_BATCH", "WRITE_REVIEW_PROPOSAL", "READ_REVIEW_LEDGER",
    "WRITE_CHALLENGE", "READ_CHALLENGED_PACKET", "SIMULATE_AUTHORIZATION",
})
BLIND_ACTIONS = frozenset({"READ_SIMULATED_AUTHOR_PACKET"})


@dataclass(frozen=True)
class AccessResult:
    permitted: bool
    reason: str
    marker: str = FAKE_MARKER


@dataclass(frozen=True)
class Enrollment:
    principal: str
    session: str
    role: str


class FakeRoleDirectory:
    """Model continuity and role incompatibility across fictional sessions.

    Fake principal identifiers represent asserted continuity, not a validated
    identity. The same person can defeat this model by registering a second,
    unlinked principal, and the implementation does not prohibit that attack.
    A real S1 design must qualify a reliable external binding between people,
    sessions, models, apps and exposure history.
    """

    def __init__(self) -> None:
        self._sessions: dict[str, Enrollment] = {}
        self._principal_role: dict[str, str] = {}
        self._exposed: set[str] = set()

    def enroll(self, *, principal: str, session: str, role: str) -> Enrollment:
        if (
            not isinstance(principal, str)
            or not isinstance(session, str)
            or not FAKE_ID.fullmatch(principal)
            or not FAKE_ID.fullmatch(session)
            or role not in ROLES
        ):
            raise ValueError("Only explicitly typed fictional identities are permitted")
        if session in self._sessions:
            raise ValueError("Cannot reassign an existing fictional session")
        previous = self._principal_role.get(principal)
        if previous is not None and previous != role:
            raise ValueError("An already enrolled principal cannot change role")
        if role == "BLIND_AUTHOR" and principal in self._exposed:
            raise ValueError("An exposed principal cannot become a blind author")
        record = Enrollment(principal=principal, session=session, role=role)
        self._sessions[session] = record
        self._principal_role[principal] = role
        return record

    def mark_private_exposure(self, *, session: str) -> None:
        """Persist a mock principal exposure across its future sessions."""
        identity = self._sessions.get(session)
        if identity is None or identity.role not in {
            "REVIEWER", "CHALLENGER", "AUTHORIZER",
        }:
            raise ValueError("Exposure must be attached to a known mock privileged role")
        self._exposed.add(identity.principal)

    def decide(
        self, *, session: str, action: str, claimed_role: str | None = None
    ) -> AccessResult:
        """Ignore a caller's claimed role and consult mock enrollment instead."""
        _ = claimed_role
        identity = self._sessions.get(session)
        if identity is None:
            return AccessResult(False, "SESSION_UNREGISTERED")
        if action not in ROLE_ACTIONS.get(identity.role, frozenset()):
            return AccessResult(False, "ROLE_ACTION_DENIED")
        if action in BLIND_ACTIONS and identity.principal in self._exposed:
            return AccessResult(False, "EXPOSURE_INCOMPATIBLE_WITH_BLIND_ROLE")
        return AccessResult(True, "SIMULATED_POLICY_PERMITS_NOT_OS_AUTHORIZATION")

    def public_summary(self) -> dict[str, str]:
        """Never expose per-principal assignments or exposure mappings."""
        return {
            "marker": FAKE_MARKER,
            "qualification": "S1_REAL_ROLE_ISOLATION_NOT_VERIFIED",
        }


@dataclass(frozen=True)
class ReleaseWitness:
    """Caller-supplied fictional observations, not trusted acceptance evidence."""

    manifest_exact: bool = False
    proposed: bool = False
    independently_challenged: bool = False
    custody_readback: bool = False
    author_render_verified: bool = False
    cumulative_receipt_safe: bool = False
    material_objection: bool = True


def simulate_release_witness(witness: ReleaseWitness) -> AccessResult:
    """Return only a *simulated* readiness outcome, never actual authorization.

    Even an all-True witness is a value supplied by the simulation caller,
    with no trustworthy attestation or enforcement behind it.
    """
    if not isinstance(witness, ReleaseWitness):
        raise TypeError("Only the synthetic release witness type is supported")
    values = tuple(vars(witness).values())
    if any(type(value) is not bool for value in values):
        raise TypeError("Every fictional release-witness field must be an exact boolean")
    ready = (
        witness.manifest_exact
        and witness.proposed
        and witness.independently_challenged
        and witness.custody_readback
        and witness.author_render_verified
        and witness.cumulative_receipt_safe
        and not witness.material_objection
    )
    if ready:
        return AccessResult(True, "SIMULATED_READY_ONLY_NO_RELEASE_CAPABILITY")
    return AccessResult(False, "RELEASE_HOLD_UNQUALIFIED_WITNESS")


def screen_public_receipt(
    *,
    fields: Mapping[str, object],
    previous_receipts: tuple[Mapping[str, object], ...] = (),
) -> AccessResult:
    """Conservatively reject variable public progress from fictional private data.

    This intentionally narrow prototype only admits a fixed, non-informative
    synthetic marker and qualified=false. It rejects detailed counts even when
    any one record looks innocuous, because aggregate changes and joins can
    expose a private source disposition. Real aggregate publication requires
    a much richer and independently challenged release strategy.
    """
    safe = {"marker": FAKE_MARKER, "qualified": False}
    if (
        not isinstance(fields, Mapping)
        or set(fields) != set(safe)
        or type(fields.get("marker")) is not str
        or fields.get("marker") != FAKE_MARKER
        or type(fields.get("qualified")) is not bool
        or fields.get("qualified") is not False
    ):
        return AccessResult(False, "VARIABLE_OR_PRIVATE_PUBLIC_METADATA")
    if not isinstance(previous_receipts, tuple):
        return AccessResult(False, "UNVERIFIED_PUBLIC_HISTORY")
    for receipt in previous_receipts:
        if (
            not isinstance(receipt, Mapping)
            or set(receipt) != set(safe)
            or type(receipt.get("marker")) is not str
            or receipt.get("marker") != FAKE_MARKER
            or type(receipt.get("qualified")) is not bool
            or receipt.get("qualified") is not False
        ):
            return AccessResult(False, "UNVERIFIED_PUBLIC_HISTORY")
    return AccessResult(True, "FIXED_SYNTHETIC_RECEIPT_ONLY")


def observe_route_capabilities(
    *,
    environment_has_separate_identities: bool,
    actual_deny_test_observed: bool,
    durable_confidential_readback_observed: bool,
    separate_anchor_custody_observed: bool,
) -> dict[str, object]:
    """Classify specific *supplied* qualifications without granting authority.

    Caller booleans are untrusted. This function cannot observe or attest
    Windows ACLs, cloud credentials, runtime API restrictions, physical actor
    separation, backup confidentiality or chat-session retention.
    """
    observations = (
        environment_has_separate_identities,
        actual_deny_test_observed,
        durable_confidential_readback_observed,
        separate_anchor_custody_observed,
    )
    if any(type(value) is not bool for value in observations):
        raise TypeError("Source-free capability observations must be exact booleans")
    passed = (
        environment_has_separate_identities
        and actual_deny_test_observed
        and durable_confidential_readback_observed
        and separate_anchor_custody_observed
    )
    return {
        "marker": FAKE_MARKER,
        "simulated_gate_inputs_complete": passed,
        "actual_s1_security_qualified": False,
        "real_content_authorized": False,
    }
