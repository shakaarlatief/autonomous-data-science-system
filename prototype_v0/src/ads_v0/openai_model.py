"""OpenAI Responses API adapter for Prototype V0 calibration.

This adapter is intentionally isolated from the treatment runner. The treatment
architecture depends only on ``ModelClient`` and can therefore be calibrated
with a different provider later without changing the benchmark, workspace, or
B0/B1 logic.

The first provisional calibration configuration uses a GPT-5.6 family model
through the Responses API with Structured Outputs. The adapter can chain
responses with ``previous_response_id`` so multi-turn reasoning context remains
available without teaching the treatment runner about provider-specific response
objects.

The adapter is not imported by the core package and the OpenAI SDK is an
optional dependency. ``OPENAI_API_KEY`` is read by the SDK in the ordinary way
when no client is injected.
"""

from __future__ import annotations

import json
from typing import Any, Mapping, Sequence

from .model import ModelGeneration, ModelMessage, ModelUsage


_ACTION_CATEGORIES = [
    "INSPECTION",
    "DEVELOPMENT",
    "FINAL_EVALUATION",
    "REPORTING",
]


def _report_schema(properties: Mapping[str, Any]) -> dict[str, Any]:
    """Build a strict Structured Outputs object schema."""

    return {
        "type": "object",
        "properties": dict(properties),
        "required": list(properties),
        "additionalProperties": False,
    }


_PHASE_1_REPORT_SCHEMA = _report_schema(
    {
        "summary": {"type": "string"},
        "selected_features": {"type": "array", "items": {"type": "string"}},
        "validation_approach": {"type": "string"},
        "development_evidence": {"type": "string"},
        "unresolved_issues": {"type": "array", "items": {"type": "string"}},
    }
)

_FINAL_LOCK_REPORT_SCHEMA = _report_schema(
    {
        "summary": {"type": "string"},
        "selected_features": {"type": "array", "items": {"type": "string"}},
        "validation_approach": {"type": "string"},
        "development_evidence": {"type": "string"},
        "limitations": {"type": "array", "items": {"type": "string"}},
    }
)

_FINAL_REPORT_SCHEMA = _report_schema(
    {
        "summary": {"type": "string"},
        "final_test_evidence": {"type": "string"},
        "claim_scope": {"type": "string"},
        "limitations": {"type": "array", "items": {"type": "string"}},
    }
)


def _command_variant(command_type: str, properties: Mapping[str, Any]) -> dict[str, Any]:
    command_properties = {
        "type": {"type": "string", "enum": [command_type]},
        **dict(properties),
    }
    return {
        "type": "object",
        "properties": command_properties,
        "required": list(command_properties),
        "additionalProperties": False,
    }


TREATMENT_RESPONSE_SCHEMA: dict[str, Any] = {
    "type": "object",
    "properties": {
        "rationale": {
            "type": "string",
            "description": "Brief decision rationale. Do not include private chain-of-thought.",
        },
        "command": {
            "anyOf": [
                _command_variant("list_artifacts", {}),
                _command_variant(
                    "read_text",
                    {
                        "artifact_id": {"type": "string"},
                        "purpose": {"type": "string"},
                    },
                ),
                _command_variant(
                    "table_metadata",
                    {
                        "artifact_id": {"type": "string"},
                        "purpose": {"type": "string"},
                    },
                ),
                _command_variant(
                    "table_sample",
                    {
                        "artifact_id": {"type": "string"},
                        "rows": {"type": "integer"},
                        "purpose": {"type": "string"},
                    },
                ),
                _command_variant(
                    "execute_python",
                    {
                        "input_artifacts": {
                            "type": "array",
                            "items": {"type": "string"},
                        },
                        "category": {
                            "type": "string",
                            "enum": _ACTION_CATEGORIES,
                        },
                        "purpose": {"type": "string"},
                        "code": {"type": "string"},
                    },
                ),
                _command_variant(
                    "phase_1_complete",
                    {"report": _PHASE_1_REPORT_SCHEMA},
                ),
                _command_variant(
                    "final_model_locked",
                    {"report": _FINAL_LOCK_REPORT_SCHEMA},
                ),
                _command_variant(
                    "submit_final_report",
                    {"report": _FINAL_REPORT_SCHEMA},
                ),
            ]
        },
    },
    "required": ["rationale", "command"],
    "additionalProperties": False,
}


class OpenAIResponsesModel:
    """Provider adapter implementing the Prototype V0 ``ModelClient`` protocol.

    Parameters
    ----------
    model:
        OpenAI model identifier. The experiment configuration may change this
        without changing B0/B1/P0 treatment logic.
    reasoning_effort:
        Explicit reasoning effort passed to GPT-5.6-family requests.
    max_output_tokens:
        Per-turn output ceiling. Each turn produces only one treatment command,
        but Python code may be several thousand tokens long.
    verbosity:
        Responses API text verbosity setting.
    store:
        Whether Responses API objects are stored server-side. Threading with
        ``previous_response_id`` currently requires ``store=True`` in this
        adapter. The benchmark contains synthetic data only.
    use_previous_response_id:
        Whether to chain Responses API calls so prior response reasoning/context
        remains available. This is enabled for the first calibration because
        the task is explicitly multi-turn.
    client:
        Optional injected SDK-compatible client used by unit tests. When absent,
        the official ``OpenAI`` client is created lazily.
    """

    def __init__(
        self,
        *,
        model: str = "gpt-5.6-terra",
        reasoning_effort: str = "high",
        max_output_tokens: int = 12_000,
        verbosity: str = "low",
        store: bool = True,
        use_previous_response_id: bool = True,
        client: Any | None = None,
    ) -> None:
        if max_output_tokens <= 0:
            raise ValueError("max_output_tokens must be positive.")
        if use_previous_response_id and not store:
            raise ValueError(
                "This Version 0 adapter requires store=True when "
                "use_previous_response_id=True."
            )

        if client is None:
            try:
                from openai import OpenAI
            except ImportError as exc:  # pragma: no cover - exercised only without extra
                raise ImportError(
                    "Install the optional OpenAI dependency with "
                    "`python -m pip install -e \".[openai]\"`."
                ) from exc
            client = OpenAI()

        self.client = client
        self.model_name = model
        self.reasoning_effort = reasoning_effort
        self.max_output_tokens = max_output_tokens
        self.verbosity = verbosity
        self.store = store
        self.use_previous_response_id = use_previous_response_id

        self._previous_response_id: str | None = None
        self._message_count_at_previous_request = 0

    def generate(self, messages: Sequence[ModelMessage]) -> ModelGeneration:
        """Generate one strict structured treatment command."""

        input_items = self._input_for_request(messages)
        request: dict[str, Any] = {
            "model": self.model_name,
            "input": input_items,
            "reasoning": {
                "effort": self.reasoning_effort,
                "context": "all_turns",
            },
            "text": {
                "verbosity": self.verbosity,
                "format": {
                    "type": "json_schema",
                    "name": "prototype_v0_treatment_command",
                    "strict": True,
                    "schema": TREATMENT_RESPONSE_SCHEMA,
                },
            },
            "max_output_tokens": self.max_output_tokens,
            "store": self.store,
        }
        if self._previous_response_id is not None and self.use_previous_response_id:
            request["previous_response_id"] = self._previous_response_id

        response = self.client.responses.create(**request)
        status = str(getattr(response, "status", ""))
        if status != "completed":
            details = getattr(response, "incomplete_details", None)
            raise RuntimeError(
                f"OpenAI response did not complete successfully: status={status!r}, "
                f"details={details!r}."
            )

        output_text = getattr(response, "output_text", None)
        if not isinstance(output_text, str) or not output_text.strip():
            raise RuntimeError("OpenAI response contained no structured output text.")

        try:
            payload = json.loads(output_text)
        except json.JSONDecodeError as exc:
            raise RuntimeError("OpenAI structured output was not valid JSON.") from exc

        usage_object = getattr(response, "usage", None)
        usage = ModelUsage(
            input_tokens=_optional_int(usage_object, "input_tokens"),
            output_tokens=_optional_int(usage_object, "output_tokens"),
            total_tokens=_optional_int(usage_object, "total_tokens"),
        )

        response_id = getattr(response, "id", None)
        if self.use_previous_response_id:
            if not isinstance(response_id, str) or not response_id:
                raise RuntimeError(
                    "OpenAI response did not provide an ID required for threading."
                )
            self._previous_response_id = response_id

        self._message_count_at_previous_request = len(messages)

        return ModelGeneration(
            payload=payload,
            model_name=str(getattr(response, "model", self.model_name)),
            usage=usage,
            provider_metadata={
                "provider": "openai",
                "response_id": response_id,
                "status": status,
                "reasoning_effort": self.reasoning_effort,
                "threaded_with_previous_response_id": self.use_previous_response_id,
            },
        )

    def _input_for_request(self, messages: Sequence[ModelMessage]) -> list[dict[str, str]]:
        if self._previous_response_id is None or not self.use_previous_response_id:
            selected = list(messages)
        else:
            delta = list(messages[self._message_count_at_previous_request :])
            # The previous OpenAI response already contains the assistant output.
            # The runner mirrors that output into its provider-neutral transcript,
            # so only newly appended non-assistant messages should be sent when
            # continuing via previous_response_id.
            selected = [message for message in delta if message.role != "assistant"]

        if not selected:
            raise RuntimeError("No new provider input messages are available.")

        return [
            {"role": message.role, "content": message.content}
            for message in selected
        ]


def _optional_int(value: Any, attribute: str) -> int | None:
    if value is None:
        return None
    item = getattr(value, attribute, None)
    if item is None and isinstance(value, Mapping):
        item = value.get(attribute)
    return int(item) if item is not None else None
