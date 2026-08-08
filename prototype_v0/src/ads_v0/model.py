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

from dataclasses import dataclass
from typing import Any, Mapping, Protocol, Sequence


@dataclass(frozen=True)
class ModelMessage:
    """One provider-neutral conversation message."""

    role: str
    content: str


class ModelClient(Protocol):
    """Minimal model interface required by the Version 0 treatment loop."""

    def generate(self, messages: Sequence[ModelMessage]) -> Mapping[str, Any]:
        """Return one structured treatment command.

        Implementations must return a JSON-serializable mapping following the
        treatment command contract documented in ``treatments.py``.
        """


class ScriptedModel:
    """Deterministic model double that emits a predefined command sequence.

    Besides making unit tests reproducible, the scripted model lets the project
    verify that B0 and B1 runners can complete the exact same runtime before a
    provider-specific adapter is introduced.
    """

    def __init__(self, responses: Sequence[Mapping[str, Any]]) -> None:
        self._responses = [dict(response) for response in responses]
        self._index = 0
        self.received_messages: list[tuple[ModelMessage, ...]] = []

    def generate(self, messages: Sequence[ModelMessage]) -> Mapping[str, Any]:
        self.received_messages.append(tuple(messages))
        if self._index >= len(self._responses):
            raise RuntimeError("ScriptedModel exhausted its predefined responses.")

        response = self._responses[self._index]
        self._index += 1
        return dict(response)
