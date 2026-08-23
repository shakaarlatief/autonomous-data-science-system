"""ADS-owned request, result, usage, and trace models for reasoning runtimes.

The objects in this module deliberately describe ADS semantics rather than any
provider or agent-framework API. Infrastructure adapters translate these
objects to and from concrete runtime implementations.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
from enum import Enum
import hashlib
import json
from types import MappingProxyType
from typing import Any, Mapping

from ads_system.application.recommendation import RecommendationActionResult


@dataclass(frozen=True, slots=True)
class KnowledgeRevisionPointer:
    """Exact reusable-knowledge revision supplied to one reasoning call."""

    stable_key: str
    revision_id: str

    def __post_init__(self) -> None:
        if not self.stable_key.strip():
            raise ValueError("stable_key must be non-empty")
        if not self.revision_id.strip():
            raise ValueError("revision_id must be non-empty")


@dataclass(frozen=True, slots=True)
class ReasoningModelConfiguration:
    """Provider-neutral model settings that materially define an ADS run."""

    requested_model: str
    reasoning_effort: str
    verbosity: str
    max_output_tokens: int
    store: bool = False

    def __post_init__(self) -> None:
        if not self.requested_model.strip():
            raise ValueError("requested_model must be non-empty")
        if not self.reasoning_effort.strip():
            raise ValueError("reasoning_effort must be non-empty")
        if self.verbosity not in {"low", "medium", "high"}:
            raise ValueError("verbosity must be low, medium, or high")
        if self.max_output_tokens <= 0:
            raise ValueError("max_output_tokens must be positive")


@dataclass(frozen=True, slots=True)
class ReasoningContextValueResult:
    """Structured reasoning output used by the first context-value slice."""

    answer: str
    proposed_actions: tuple[str, ...]
    required_clarifications: tuple[str, ...]
    warnings: tuple[str, ...]
    methodological_basis: tuple[str, ...]

    def __post_init__(self) -> None:
        if not self.answer.strip():
            raise ValueError("answer must be non-empty")
        for field_name in (
            "proposed_actions",
            "required_clarifications",
            "warnings",
            "methodological_basis",
        ):
            values = getattr(self, field_name)
            if any(not value.strip() for value in values):
                raise ValueError(f"{field_name} cannot contain empty strings")
            if len(values) != len(set(values)):
                raise ValueError(f"{field_name} must not contain duplicates")

    def to_payload(self) -> dict[str, object]:
        return {
            "answer": self.answer,
            "proposed_actions": list(self.proposed_actions),
            "required_clarifications": list(self.required_clarifications),
            "warnings": list(self.warnings),
            "methodological_basis": list(self.methodological_basis),
        }


class ReasoningOutputKind(str, Enum):
    """ADS-owned structured result family requested from a reasoning runtime."""

    CONTEXT_VALUE = "CONTEXT_VALUE"
    RECOMMENDATION_ACTION = "RECOMMENDATION_ACTION"


@dataclass(frozen=True, slots=True)
class ReasoningRequest:
    """Complete authoritative input for one stateless reasoning call."""

    run_id: str
    run_nonce: str
    system_instruction: str
    user_task: str
    project_evidence: Mapping[str, object]
    methodological_context_payload: Mapping[str, object]
    methodological_context_sha256: str
    knowledge_revisions: tuple[KnowledgeRevisionPointer, ...]
    model_configuration: ReasoningModelConfiguration
    task_payload: Mapping[str, object] | None = None
    structured_output_kind: ReasoningOutputKind = ReasoningOutputKind.CONTEXT_VALUE

    def __post_init__(self) -> None:
        if not self.run_id.strip():
            raise ValueError("run_id must be non-empty")
        if not self.run_nonce.strip():
            raise ValueError("run_nonce must be non-empty")
        if not self.system_instruction.strip():
            raise ValueError("system_instruction must be non-empty")
        if not self.user_task.strip():
            raise ValueError("user_task must be non-empty")
        if len(self.methodological_context_sha256) != 64:
            raise ValueError("methodological_context_sha256 must be a SHA-256 hex digest")
        try:
            int(self.methodological_context_sha256, 16)
        except ValueError as exc:
            raise ValueError(
                "methodological_context_sha256 must be a SHA-256 hex digest"
            ) from exc

        if not isinstance(self.structured_output_kind, ReasoningOutputKind):
            try:
                normalized_kind = ReasoningOutputKind(self.structured_output_kind)
            except (TypeError, ValueError) as exc:
                raise ValueError(
                    f"unsupported structured_output_kind: {self.structured_output_kind!r}"
                ) from exc
            object.__setattr__(self, "structured_output_kind", normalized_kind)

        keys = [item.stable_key for item in self.knowledge_revisions]
        if len(keys) != len(set(keys)):
            raise ValueError("knowledge_revisions must contain unique stable keys")

        object.__setattr__(
            self,
            "project_evidence",
            MappingProxyType(dict(self.project_evidence)),
        )
        object.__setattr__(
            self,
            "methodological_context_payload",
            MappingProxyType(dict(self.methodological_context_payload)),
        )
        if self.task_payload is not None:
            object.__setattr__(
                self,
                "task_payload",
                MappingProxyType(dict(self.task_payload)),
            )

    def canonical_model_input(self) -> str:
        """Return deterministic condition-neutral input for the runtime adapter.

        ``task_payload`` is optional so the already-promoted Specification 014
        envelope remains byte-compatible when no structured task-specific menu
        is required. Specification 015 uses this field for the candidate action,
        blocked-scope, and clarification menus shared by all three conditions.
        """

        payload: dict[str, object] = {
            "experiment_run_nonce": self.run_nonce,
            "user_task": self.user_task,
            "project_evidence": dict(self.project_evidence),
        }
        if self.task_payload is not None:
            payload["task_payload"] = dict(self.task_payload)
        payload["methodological_context"] = dict(self.methodological_context_payload)
        return json.dumps(
            payload,
            sort_keys=True,
            separators=(",", ":"),
            ensure_ascii=False,
        )

    def semantic_digest(self) -> str:
        payload = {
            "run_id": self.run_id,
            "system_instruction": self.system_instruction,
            "model_input": self.canonical_model_input(),
            "context_sha256": self.methodological_context_sha256,
            "knowledge_revisions": [asdict(item) for item in self.knowledge_revisions],
            "model_configuration": asdict(self.model_configuration),
            "structured_output_kind": self.structured_output_kind.value,
        }
        canonical = json.dumps(
            payload,
            sort_keys=True,
            separators=(",", ":"),
            ensure_ascii=False,
        )
        return hashlib.sha256(canonical.encode("utf-8")).hexdigest()


@dataclass(frozen=True, slots=True)
class ReasoningUsage:
    """Normalized provider usage for one completed runtime call."""

    input_tokens: int
    output_tokens: int
    total_tokens: int
    cached_input_tokens: int | None = None
    reasoning_tokens: int | None = None
    service_tier: str | None = None
    raw_provider_usage: Mapping[str, Any] | None = None

    def __post_init__(self) -> None:
        for name in ("input_tokens", "output_tokens", "total_tokens"):
            if getattr(self, name) < 0:
                raise ValueError(f"{name} cannot be negative")
        for name in ("cached_input_tokens", "reasoning_tokens"):
            value = getattr(self, name)
            if value is not None and value < 0:
                raise ValueError(f"{name} cannot be negative")
        if self.raw_provider_usage is not None:
            object.__setattr__(
                self,
                "raw_provider_usage",
                MappingProxyType(dict(self.raw_provider_usage)),
            )


@dataclass(frozen=True, slots=True)
class ReasoningTrace:
    """Stable ADS trace for a completed stateless reasoning call."""

    run_id: str
    request_digest: str
    methodological_context_sha256: str
    knowledge_revisions: tuple[KnowledgeRevisionPointer, ...]
    requested_model: str
    provider_model: str
    runtime_name: str
    runtime_version: str
    provider_response_ids: tuple[str, ...] = ()
    provider_request_ids: tuple[str, ...] = ()


StructuredReasoningResult = ReasoningContextValueResult | RecommendationActionResult


@dataclass(frozen=True, slots=True)
class ReasoningOutcome:
    """Completed ADS reasoning result normalized from any runtime provider."""

    result: StructuredReasoningResult
    usage: ReasoningUsage
    trace: ReasoningTrace
    latency_seconds: float

    def __post_init__(self) -> None:
        if self.latency_seconds < 0:
            raise ValueError("latency_seconds cannot be negative")


def validate_methodological_basis(
    result: StructuredReasoningResult,
    supplied_revisions: tuple[KnowledgeRevisionPointer, ...],
) -> None:
    """Reject model references to methodological knowledge outside supplied context."""

    supplied = {item.stable_key for item in supplied_revisions}
    referenced = set(result.methodological_basis)
    unsupported = sorted(referenced - supplied)
    if unsupported:
        raise ValueError(
            "reasoning output references methodological basis outside supplied context: "
            f"{unsupported}"
        )
