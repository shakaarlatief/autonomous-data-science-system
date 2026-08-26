"""Framework-neutral harness for Specification 005 runtime evaluation.

The types in this module are experiment contracts, not the final production
ReasoningRuntime API. Their purpose is to make the bakeoff compare candidate
runtimes against the same ADS-owned workload, provenance, interruption, and
side-effect semantics without allowing framework-native Agent, Session,
Thread, Graph, or checkpoint types to become project/domain authority.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from enum import StrEnum
import hashlib
import json
from typing import Protocol


class RuntimeStatus(StrEnum):
    COMPLETED = "COMPLETED"
    INTERRUPTED = "INTERRUPTED"
    CANCELLED = "CANCELLED"
    FAILED = "FAILED"


class ApprovalDecision(StrEnum):
    APPROVE = "APPROVE"
    REJECT = "REJECT"


@dataclass(frozen=True)
class KnowledgeRevisionRef:
    asset_key: str
    revision_id: str


@dataclass(frozen=True)
class ProjectContextSnapshot:
    project_id: str
    snapshot_id: str
    facts: dict[str, str]


@dataclass(frozen=True)
class MethodologicalContextPack:
    pack_id: str
    revisions: tuple[KnowledgeRevisionRef, ...]
    rationale: tuple[str, ...]
    hard_constraints: tuple[str, ...]

    def semantic_digest(self) -> str:
        payload = {
            "pack_id": self.pack_id,
            "revisions": [asdict(item) for item in self.revisions],
            "rationale": list(self.rationale),
            "hard_constraints": list(self.hard_constraints),
        }
        canonical = json.dumps(
            payload,
            sort_keys=True,
            separators=(",", ":"),
            ensure_ascii=False,
        )
        return hashlib.sha256(canonical.encode("utf-8")).hexdigest()


@dataclass(frozen=True)
class RuntimeWorkloadInput:
    run_id: str
    user_intent: str
    project: ProjectContextSnapshot
    context_pack: MethodologicalContextPack


@dataclass(frozen=True)
class RuntimeRecommendation:
    next_investigation: str
    validation_implication: str
    reasons: tuple[str, ...]
    referenced_revision_ids: tuple[str, ...]


@dataclass(frozen=True)
class RuntimeInterrupt:
    interrupt_id: str
    kind: str
    tool_name: str
    arguments: dict[str, str]
    reason: str


@dataclass(frozen=True)
class RuntimeResumeToken:
    run_id: str
    next_step: int
    interrupt: RuntimeInterrupt
    context_pack_id: str
    context_pack_digest: str
    project_snapshot_id: str
    proposal_idempotency_key: str
    execution_state: dict[str, object] = field(default_factory=dict)

    def to_json(self) -> str:
        return json.dumps(asdict(self), sort_keys=True, separators=(",", ":"))

    @classmethod
    def from_json(cls, payload: str) -> "RuntimeResumeToken":
        raw = json.loads(payload)
        raw["interrupt"] = RuntimeInterrupt(**raw["interrupt"])
        return cls(**raw)


@dataclass(frozen=True)
class RuntimeTraceEvent:
    sequence: int
    kind: str
    name: str
    detail: str


@dataclass
class RuntimeTrace:
    run_id: str
    project_snapshot_id: str
    context_pack_id: str
    context_pack_digest: str
    knowledge_revision_ids: tuple[str, ...]
    events: list[RuntimeTraceEvent] = field(default_factory=list)

    def record(self, kind: str, name: str, detail: str) -> None:
        self.events.append(
            RuntimeTraceEvent(
                sequence=len(self.events) + 1,
                kind=kind,
                name=name,
                detail=detail,
            )
        )


@dataclass(frozen=True)
class RuntimeOutcome:
    status: RuntimeStatus
    trace: RuntimeTrace
    recommendation: RuntimeRecommendation | None = None
    interruption: RuntimeInterrupt | None = None
    resume_token: RuntimeResumeToken | None = None
    error: str | None = None


class MethodologicalReferenceGateway(Protocol):
    def lookup(self, query: str) -> str:
        """Return a side-effect-free reference result."""


class InMemoryReferenceGateway:
    """Deterministic pre-MCP gateway used to validate the harness itself."""

    def __init__(self, references: dict[str, str], *, fail_first: bool = False) -> None:
        self._references = references
        self._failures_remaining = 1 if fail_first else 0
        self.calls = 0

    def lookup(self, query: str) -> str:
        self.calls += 1
        if self._failures_remaining:
            self._failures_remaining -= 1
            raise RuntimeError("synthetic transient reference failure")
        return self._references.get(query, "no reference found")


class ProposalLedger:
    """ADS-owned at-most-once ledger for the approval-gated side effect."""

    def __init__(self) -> None:
        self._created: dict[str, dict[str, str]] = {}
        self.execution_attempts = 0

    def create_once(self, idempotency_key: str, proposal: dict[str, str]) -> bool:
        self.execution_attempts += 1
        if idempotency_key in self._created:
            return False
        self._created[idempotency_key] = dict(proposal)
        return True

    def get(self, idempotency_key: str) -> dict[str, str] | None:
        value = self._created.get(idempotency_key)
        return dict(value) if value is not None else None

    @property
    def created_count(self) -> int:
        return len(self._created)


class DirectControlRuntime:
    """Minimal deterministic control for the framework bakeoff.

    This is intentionally not a general agent framework. It implements only
    the representative Specification 005 workload and the execution semantics
    needed to establish what candidate runtimes must improve upon.
    """

    def __init__(
        self,
        reference_gateway: MethodologicalReferenceGateway,
        proposal_ledger: ProposalLedger,
        *,
        max_reference_attempts: int = 2,
    ) -> None:
        self._reference_gateway = reference_gateway
        self._proposal_ledger = proposal_ledger
        self._max_reference_attempts = max_reference_attempts
        self._cancelled_runs: set[str] = set()
        self._traces: dict[str, RuntimeTrace] = {}

    def cancel(self, run_id: str) -> None:
        self._cancelled_runs.add(run_id)

    def run(self, workload: RuntimeWorkloadInput) -> RuntimeOutcome:
        trace = self._new_trace(workload)
        self._traces[workload.run_id] = trace
        trace.record("runtime", "start", "direct-control")

        if self._is_cancelled(workload.run_id, trace):
            return RuntimeOutcome(RuntimeStatus.CANCELLED, trace)

        prediction_moment = self._inspect_project_fact(
            workload,
            "prediction_moment",
            trace,
        )
        missingness = self._inspect_project_fact(
            workload,
            "production_missingness",
            trace,
        )

        reference = self._lookup_with_retry(
            "missingness validation leakage",
            trace,
        )
        if isinstance(reference, RuntimeOutcome):
            return reference

        if self._is_cancelled(workload.run_id, trace):
            return RuntimeOutcome(RuntimeStatus.CANCELLED, trace)

        interrupt = RuntimeInterrupt(
            interrupt_id=f"approval:{workload.run_id}:proposal",
            kind="TOOL_APPROVAL",
            tool_name="create_investigation_proposal",
            arguments={
                "title": "Investigate production-time missingness before validation design",
                "prediction_moment": prediction_moment,
                "missingness": missingness,
                "reference": reference,
            },
            reason="Creating a project Investigation proposal is an authoritative side effect.",
        )
        token = RuntimeResumeToken(
            run_id=workload.run_id,
            next_step=1,
            interrupt=interrupt,
            context_pack_id=workload.context_pack.pack_id,
            context_pack_digest=workload.context_pack.semantic_digest(),
            project_snapshot_id=workload.project.snapshot_id,
            proposal_idempotency_key=f"proposal:{workload.run_id}:production-missingness",
        )
        trace.record("interrupt", interrupt.tool_name, interrupt.interrupt_id)
        return RuntimeOutcome(
            RuntimeStatus.INTERRUPTED,
            trace,
            interruption=interrupt,
            resume_token=token,
        )

    def resume(
        self,
        workload: RuntimeWorkloadInput,
        serialized_token: str,
        decision: ApprovalDecision,
    ) -> RuntimeOutcome:
        token = RuntimeResumeToken.from_json(serialized_token)
        self._validate_resume_token(workload, token)
        trace = self._traces.get(workload.run_id) or self._new_trace(workload)
        self._traces[workload.run_id] = trace
        trace.record("runtime", "resume", decision.value)

        if self._is_cancelled(workload.run_id, trace):
            return RuntimeOutcome(RuntimeStatus.CANCELLED, trace)

        if decision is ApprovalDecision.REJECT:
            trace.record("approval", token.interrupt.tool_name, "rejected")
            return RuntimeOutcome(
                RuntimeStatus.COMPLETED,
                trace,
                recommendation=self._recommendation(workload, proposal_created=False),
            )

        created = self._proposal_ledger.create_once(
            token.proposal_idempotency_key,
            {
                "title": token.interrupt.arguments["title"],
                "source_run_id": workload.run_id,
                "project_snapshot_id": workload.project.snapshot_id,
                "context_pack_digest": workload.context_pack.semantic_digest(),
            },
        )
        trace.record(
            "approval",
            token.interrupt.tool_name,
            "executed" if created else "already-executed",
        )
        return RuntimeOutcome(
            RuntimeStatus.COMPLETED,
            trace,
            recommendation=self._recommendation(workload, proposal_created=True),
        )

    def _new_trace(self, workload: RuntimeWorkloadInput) -> RuntimeTrace:
        return RuntimeTrace(
            run_id=workload.run_id,
            project_snapshot_id=workload.project.snapshot_id,
            context_pack_id=workload.context_pack.pack_id,
            context_pack_digest=workload.context_pack.semantic_digest(),
            knowledge_revision_ids=tuple(
                revision.revision_id for revision in workload.context_pack.revisions
            ),
        )

    @staticmethod
    def _inspect_project_fact(
        workload: RuntimeWorkloadInput,
        key: str,
        trace: RuntimeTrace,
    ) -> str:
        value = workload.project.facts[key]
        trace.record("tool", "inspect_project_fact", key)
        return value

    def _lookup_with_retry(
        self,
        query: str,
        trace: RuntimeTrace,
    ) -> str | RuntimeOutcome:
        for attempt in range(1, self._max_reference_attempts + 1):
            try:
                result = self._reference_gateway.lookup(query)
                trace.record("tool", "lookup_methodological_reference", query)
                return result
            except RuntimeError as exc:
                trace.record("retry", "lookup_methodological_reference", f"attempt={attempt}")
                if attempt == self._max_reference_attempts:
                    return RuntimeOutcome(
                        RuntimeStatus.FAILED,
                        trace,
                        error=str(exc),
                    )
        raise AssertionError("unreachable")

    def _is_cancelled(self, run_id: str, trace: RuntimeTrace) -> bool:
        if run_id not in self._cancelled_runs:
            return False
        trace.record("runtime", "cancel", "requested")
        return True

    @staticmethod
    def _validate_resume_token(
        workload: RuntimeWorkloadInput,
        token: RuntimeResumeToken,
    ) -> None:
        expected = (
            workload.run_id,
            workload.project.snapshot_id,
            workload.context_pack.pack_id,
            workload.context_pack.semantic_digest(),
        )
        observed = (
            token.run_id,
            token.project_snapshot_id,
            token.context_pack_id,
            token.context_pack_digest,
        )
        if observed != expected:
            raise ValueError("resume token does not match authoritative workload context")

    @staticmethod
    def _recommendation(
        workload: RuntimeWorkloadInput,
        *,
        proposal_created: bool,
    ) -> RuntimeRecommendation:
        reasons = [
            "Production-time missingness can change what information is legitimately available at prediction time.",
            "Validation design should reflect the prediction moment and the production feature-availability process.",
        ]
        if proposal_created:
            reasons.append("The investigation proposal was approved and recorded exactly once.")
        else:
            reasons.append("The investigation was recommended but project-state creation was not approved.")
        return RuntimeRecommendation(
            next_investigation="Characterize production-time missingness and feature availability before finalizing validation.",
            validation_implication="Reassess chronological validation and feature construction against the confirmed prediction moment.",
            reasons=tuple(reasons),
            referenced_revision_ids=tuple(
                item.revision_id for item in workload.context_pack.revisions
            ),
        )
