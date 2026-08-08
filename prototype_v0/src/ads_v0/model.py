"""Provider-neutral model protocol for Prototype V0 treatment runners.

Prototype V0 should compare methodological operationalization rather than model
providers. The treatment runtime therefore depends on a minimal protocol that
can later be implemented by any sufficiently capable model adapter.

The first concrete implementation in this module is ``ScriptedModel``. It is a
deterministic test double used to validate treatment orchestration before any
real provider is connected. Provider selection remains experiment configuration
rather than part of the semantic architecture.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Mapping, Protocol, Sequence


@dataclass(frozen=True)
class ModelMessage:
    """One provider-neutral conversation message."""

    role: str
    content: str


@dataclass(frozen=True)
class ModelUsage:
    """Provider-neutral accounting information for one model generation."""

    input_tokens: int | None = None
    output_tokens: int | None = None
    total_tokens: int | None = None


@dataclass(frozen=True)
class ModelGeneration:
    """One structured model response plus experiment-accounting metadata."""

    payload: Mapping[str, Any]
    model_name: str
    usage: ModelUsage = field(default_factory=ModelUsage)
    provider_metadata: Mapping[str, Any] = field(default_factory=dict)


class ModelGenerationError(RuntimeError):
    """Provider-neutral failure raised by a model adapter.

    Parameters
    ----------
    message:
        Human-readable diagnostic suitable for experiment logs. It must never
        contain credentials or secret request headers.
    retryable:
        Whether repeating the same semantic generation request can reasonably
        recover from the failure. Examples include transient connection errors,
        rate limits, and server errors. Authentication, permission, invalid-model,
        or malformed-request failures should normally be non-retryable.
    provider:
        Optional provider label used only for diagnostics.
    error_code:
        Optional provider-neutral or HTTP-style code used for diagnostics.

    Centralizing this distinction prevents provider SDK retry behavior from
    silently creating different reliability conditions for B0, B1, and P0.
    """

    def __init__(
        self,
        message: str,
        *,
        retryable: bool,
        provider: str | None = None,
        error_code: str | int | None = None,
    ) -> None:
        super().__init__(message)
        self.retryable = retryable
        self.provider = provider
        self.error_code = error_code


class ModelClient(Protocol):
    """Minimal model interface required by the Version 0 treatment loop."""

    def generate(self, messages: Sequence[ModelMessage]) -> ModelGeneration:
        """Return one structured treatment command and usage metadata.

        ``payload`` must follow the treatment command contract documented in
        ``treatments.py``. Provider-specific response objects should be reduced
        to this representation before entering the experiment runner.
        """


class ScriptedModel:
    """Deterministic model double that emits a predefined command sequence.

    Besides making unit tests reproducible, the scripted model lets the project
    verify that B0 and B1 runners can complete the exact same runtime before a
    provider-specific adapter is introduced.
    """

    def __init__(
        self,
        responses: Sequence[Mapping[str, Any]],
        *,
        model_name: str = "scripted-model",
    ) -> None:
        self._responses = [dict(response) for response in responses]
        self._index = 0
        self.model_name = model_name
        self.received_messages: list[tuple[ModelMessage, ...]] = []

    def generate(self, messages: Sequence[ModelMessage]) -> ModelGeneration:
        self.received_messages.append(tuple(messages))
        if self._index >= len(self._responses):
            raise RuntimeError("ScriptedModel exhausted its predefined responses.")

        response = self._responses[self._index]
        self._index += 1
        return ModelGeneration(
            payload=dict(response),
            model_name=self.model_name,
            usage=ModelUsage(input_tokens=0, output_tokens=0, total_tokens=0),
        )
