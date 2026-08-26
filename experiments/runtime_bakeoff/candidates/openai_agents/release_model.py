"""Minimal deterministic model double for released OpenAI Agents SDK 0.19.4.

The current SDK documentation describes ``agents.testing.ScriptedModel``, but
that module is not shipped in the 0.19.4 PyPI distribution used by this bakeoff.
This experiment-local model therefore implements the public ``Model`` boundary
exposed by the released package. It is intentionally much smaller than the
SDK repository's own test fake and supports only the non-streaming output
sequence needed by the ADS representative workload.
"""

from __future__ import annotations

from collections.abc import AsyncIterator, Mapping, Sequence
from copy import deepcopy
import json
from typing import Any

from openai.types.responses import (
    ResponseFunctionToolCall,
    ResponseOutputMessage,
    ResponseOutputText,
)

from agents.agent_output import AgentOutputSchemaBase
from agents.handoffs import Handoff
from agents.items import (
    ModelResponse,
    TResponseInputItem,
    TResponseOutputItem,
    TResponseStreamEvent,
)
from agents.model_settings import ModelSettings
from agents.models.interface import Model, ModelTracing
from agents.tool import Tool
from agents.usage import Usage


class ReleaseScriptedModel(Model):
    """FIFO deterministic model double against the 0.19.4 public Model API."""

    def __init__(self, steps: Sequence[Sequence[TResponseOutputItem]]) -> None:
        self._steps = [list(step) for step in steps]
        self.calls: list[dict[str, Any]] = []

    @property
    def first_call(self) -> dict[str, Any] | None:
        return deepcopy(self.calls[0]) if self.calls else None

    @property
    def last_call(self) -> dict[str, Any] | None:
        return deepcopy(self.calls[-1]) if self.calls else None

    def assert_complete(self) -> None:
        if self._steps:
            raise AssertionError(
                f"{len(self._steps)} deterministic model step(s) were not consumed"
            )

    async def get_response(
        self,
        system_instructions: str | None,
        input: str | list[TResponseInputItem],
        model_settings: ModelSettings,
        tools: list[Tool],
        output_schema: AgentOutputSchemaBase | None,
        handoffs: list[Handoff],
        tracing: ModelTracing,
        *,
        previous_response_id: str | None,
        conversation_id: str | None,
        prompt: Any | None,
    ) -> ModelResponse:
        self.calls.append(
            {
                "system_instructions": system_instructions,
                "input": deepcopy(input),
                "tool_names": [getattr(candidate, "name", type(candidate).__name__) for candidate in tools],
                "has_output_schema": output_schema is not None,
                "previous_response_id": previous_response_id,
                "conversation_id": conversation_id,
            }
        )
        if not self._steps:
            raise AssertionError("ReleaseScriptedModel received an unexpected model call")
        output = self._steps.pop(0)
        return ModelResponse(
            output=deepcopy(output),
            usage=Usage(requests=1),
            response_id=f"ads-scripted-{len(self.calls)}",
        )

    async def stream_response(
        self,
        system_instructions: str | None,
        input: str | list[TResponseInputItem],
        model_settings: ModelSettings,
        tools: list[Tool],
        output_schema: AgentOutputSchemaBase | None,
        handoffs: list[Handoff],
        tracing: ModelTracing,
        *,
        previous_response_id: str | None = None,
        conversation_id: str | None = None,
        prompt: Any | None = None,
    ) -> AsyncIterator[TResponseStreamEvent]:
        raise NotImplementedError("The ADS 0.19.4 candidate gate is non-streaming")
        yield  # pragma: no cover


def function_call(
    name: str,
    arguments: str | Mapping[str, Any],
    *,
    call_id: str,
) -> TResponseOutputItem:
    serialized = (
        arguments
        if isinstance(arguments, str)
        else json.dumps(arguments, ensure_ascii=False, separators=(",", ":"))
    )
    return ResponseFunctionToolCall(
        id=call_id,
        call_id=call_id,
        type="function_call",
        name=name,
        arguments=serialized,
    )


def assistant_message(text: str, *, item_id: str = "ads-scripted-message") -> TResponseOutputItem:
    return ResponseOutputMessage(
        id=item_id,
        type="message",
        role="assistant",
        status="completed",
        content=[
            ResponseOutputText(
                text=text,
                type="output_text",
                annotations=[],
                logprobs=[],
            )
        ],
    )
