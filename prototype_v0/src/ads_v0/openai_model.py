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

The official OpenAI Python SDK performs automatic retries for several transient
errors by default. Prototype V0 disables those SDK-level retries for clients it
creates itself so the common treatment runner owns one observable retry policy
for B0, B1, and future P0. Provider errors are translated to
``ModelGenerationError`` with a provider-neutral ``retryable`` flag.

Reasoning tokens count against ``max_output_tokens`` and may consume the entire
output budget before any visible structured command is produced. Incomplete
Responses API objects can still contain observable token usage, so the adapter
preserves that usage on ``ModelGenerationError`` rather than silently reporting
zero cost for a failed reasoning attempt.

Responses API objects may contain more than one assistant message/output-text
block. The SDK ``output_text`` convenience property concatenates all such blocks.
That is convenient for ordinary prose, but two independently valid structured
JSON objects become invalid when concatenated. The adapter therefore inspects
message-level output blocks and condition-neutrally collapses exact semantic
duplicates while rejecting genuinely different multiple commands as ambiguous.

The adapter is not imported by the core package and the OpenAI SDK is an
optional dependency. ``OPENAI_API_KEY`` is read by the SDK in the ordinary way
when no client is injected.
"""

from __future__ import annotations

import json
from typing import Any, Mapping, Sequence

from .model import (
    ModelGeneration,
    ModelGenerationError,
    ModelMessage,
    ModelUsage,
)


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
        Per-turn generated-token ceiling. For reasoning models this budget
        includes hidden reasoning tokens, visible output tokens, and formatting
        tokens. The development-calibration default intentionally exceeds the
        25,000-token starting buffer recommended in current OpenAI reasoning
        guidance.
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
    request_timeout_seconds:
        Timeout applied to SDK clients constructed by this adapter. SDK retries
        are disabled so the common experiment runner owns the retry budget.
    client:
        Optional injected SDK-compatible client used by unit tests. When absent,
        the official ``OpenAI`` client is created lazily with ``max_retries=0``.
    """

    def __init__(
        self,
        *,
        model: str = "gpt-5.6-terra",
        reasoning_effort: str = "high",
        max_output_tokens: int = 30_000,
        verbosity: str = "low",
        store: bool = True,
        use_previous_response_id: bool = True,
        request_timeout_seconds: float = 300.0,
        client: Any | None = None,
    ) -> None:
        if max_output_tokens <= 0:
            raise ValueError("max_output_tokens must be positive.")
        if request_timeout_seconds <= 0:
            raise ValueError("request_timeout_seconds must be positive.")
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
            client = OpenAI(max_retries=0, timeout=request_timeout_seconds)

        self.client = client
        self.model_name = model
        self.reasoning_effort = reasoning_effort
        self.max_output_tokens = max_output_tokens
        self.verbosity = verbosity
        self.store = store
        self.use_previous_response_id = use_previous_response_id
        self.request_timeout_seconds = request_timeout_seconds

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

        response = self._create_response(request)
        status = str(getattr(response, "status", ""))
        usage = _usage_from_response(response)
        provider_metadata = self._response_metadata(response, status=status)

        if status != "completed":
            details = getattr(response, "incomplete_details", None)
            incomplete_reason = _optional_attr(details, "reason")
            error_code = str(incomplete_reason or status or "incomplete")
            raise ModelGenerationError(
                (
                    "OpenAI response did not complete successfully: "
                    f"status={status!r}, details={details!r}."
                ),
                retryable=False,
                provider="openai",
                error_code=error_code,
                usage=usage,
                provider_metadata=provider_metadata,
            )

        payload, output_metadata = _parse_structured_response_payload(response)
        provider_metadata.update(output_metadata)
        if payload is None:
            error_code = str(output_metadata.get("structured_output_error") or "invalid_json")
            if error_code == "empty_output":
                message = "OpenAI response contained no structured output text."
            elif error_code == "ambiguous_structured_output":
                message = (
                    "OpenAI response contained multiple distinct structured commands; "
                    "the adapter cannot choose among them without changing semantics."
                )
            else:
                message = "OpenAI structured output was not valid JSON."
            raise ModelGenerationError(
                message,
                retryable=False,
                provider="openai",
                error_code=error_code,
                usage=usage,
                provider_metadata=provider_metadata,
            )

        response_id = getattr(response, "id", None)
        if self.use_previous_response_id:
            if not isinstance(response_id, str) or not response_id:
                raise ModelGenerationError(
                    "OpenAI response did not provide an ID required for threading.",
                    retryable=False,
                    provider="openai",
                    error_code="missing_response_id",
                    usage=usage,
                    provider_metadata=provider_metadata,
                )
            self._previous_response_id = response_id

        self._message_count_at_previous_request = len(messages)

        return ModelGeneration(
            payload=payload,
            model_name=str(getattr(response, "model", self.model_name)),
            usage=usage,
            provider_metadata=provider_metadata,
        )

    def _response_metadata(self, response: Any, *, status: str) -> dict[str, Any]:
        usage_object = getattr(response, "usage", None)
        output_details = _optional_attr(usage_object, "output_tokens_details")
        return {
            "provider": "openai",
            "response_id": getattr(response, "id", None),
            "status": status,
            "reasoning_effort": self.reasoning_effort,
            "reasoning_tokens": _optional_int(output_details, "reasoning_tokens"),
            "threaded_with_previous_response_id": self.use_previous_response_id,
            "sdk_retries_disabled": True,
            "request_timeout_seconds": self.request_timeout_seconds,
            "max_output_tokens": self.max_output_tokens,
        }

    def _create_response(self, request: Mapping[str, Any]) -> Any:
        """Execute one provider request and normalize provider error semantics."""

        try:
            return self.client.responses.create(**dict(request))
        except Exception as exc:
            retryable, error_code = _classify_openai_exception(exc)
            raise ModelGenerationError(
                _safe_openai_error_message(exc, error_code),
                retryable=retryable,
                provider="openai",
                error_code=error_code,
            ) from exc

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
            raise ModelGenerationError(
                "No new provider input messages are available.",
                retryable=False,
                provider="openai",
                error_code="no_new_messages",
            )

        return [
            {"role": message.role, "content": message.content}
            for message in selected
        ]


def _parse_structured_response_payload(
    response: Any,
) -> tuple[Mapping[str, Any] | None, dict[str, Any]]:
    """Normalize a completed Responses API object into one semantic command.

    The SDK ``Response.output_text`` property joins every ``output_text`` block
    across all assistant-message output items. If a provider response contains
    the same structured command twice, that convenience value becomes
    ``{...}{...}`` and is not valid JSON even though each message-level block is
    independently valid and semantically identical.

    The normalization rule is deliberately conservative:

    * prefer the aggregate text when it is valid JSON;
    * otherwise parse each non-empty message-level ``output_text`` block;
    * accept multiple blocks only when every block is valid JSON and all parsed
      payloads are equal;
    * reject multiple distinct valid payloads as ambiguous rather than choosing
      one arbitrarily;
    * reject malformed or absent structured output.

    This is provider normalization, not treatment-specific recovery. B0, B1,
    and future P0 therefore receive the same semantics.
    """

    blocks = _response_output_text_blocks(response)
    metadata: dict[str, Any] = {
        "output_text_block_count": len(blocks),
        "distinct_output_text_block_count": len(set(blocks)),
        "duplicate_identical_output_blocks_collapsed": False,
    }

    if blocks:
        aggregate_text: Any = "".join(blocks)
    else:
        aggregate_text = getattr(response, "output_text", None)

    if not isinstance(aggregate_text, str) or not aggregate_text.strip():
        metadata["structured_output_error"] = "empty_output"
        return None, metadata

    try:
        aggregate_payload = json.loads(aggregate_text)
    except json.JSONDecodeError:
        aggregate_payload = None
    else:
        metadata["structured_output_source"] = "aggregate_output_text"
        return aggregate_payload, metadata

    if not blocks:
        metadata["structured_output_error"] = "invalid_json"
        return None, metadata

    parsed_blocks: list[Any] = []
    for block in blocks:
        try:
            parsed_blocks.append(json.loads(block))
        except json.JSONDecodeError:
            metadata["structured_output_error"] = "invalid_json"
            return None, metadata

    first_payload = parsed_blocks[0]
    if all(payload == first_payload for payload in parsed_blocks[1:]):
        metadata["structured_output_source"] = "deduplicated_output_text_blocks"
        metadata["duplicate_identical_output_blocks_collapsed"] = len(blocks) > 1
        return first_payload, metadata

    metadata["structured_output_error"] = "ambiguous_structured_output"
    return None, metadata


def _response_output_text_blocks(response: Any) -> list[str]:
    """Extract non-empty assistant ``output_text`` blocks without SDK joining."""

    output_items = _optional_attr(response, "output")
    if not isinstance(output_items, Sequence) or isinstance(output_items, (str, bytes)):
        return []

    blocks: list[str] = []
    for output in output_items:
        if _optional_attr(output, "type") != "message":
            continue
        content_items = _optional_attr(output, "content")
        if not isinstance(content_items, Sequence) or isinstance(
            content_items, (str, bytes)
        ):
            continue
        for content in content_items:
            if _optional_attr(content, "type") != "output_text":
                continue
            text = _optional_attr(content, "text")
            if isinstance(text, str) and text.strip():
                blocks.append(text)
    return blocks


def _classify_openai_exception(exc: Exception) -> tuple[bool, str | int | None]:
    """Map current OpenAI SDK error classes/statuses to common retry semantics."""

    status_code = getattr(exc, "status_code", None)
    error_code: str | int | None = status_code or type(exc).__name__

    # Import lazily so the module remains importable without the optional SDK
    # when a test injects a fake client.
    try:
        import openai
    except ImportError:  # pragma: no cover - optional dependency not installed
        return False, error_code

    retryable_types = tuple(
        error_type
        for error_type in (
            getattr(openai, "APIConnectionError", None),
            getattr(openai, "APITimeoutError", None),
            getattr(openai, "RateLimitError", None),
            getattr(openai, "InternalServerError", None),
        )
        if isinstance(error_type, type)
    )
    if retryable_types and isinstance(exc, retryable_types):
        return True, error_code

    if isinstance(status_code, int):
        if status_code in {408, 409, 429} or status_code >= 500:
            return True, status_code
        return False, status_code

    return False, error_code


def _safe_openai_error_message(
    exc: Exception,
    error_code: str | int | None,
) -> str:
    """Return a credential-safe provider diagnostic for experiment traces."""

    return (
        "OpenAI generation request failed: "
        f"{type(exc).__name__}"
        + (f" (code={error_code})" if error_code is not None else "")
    )


def _usage_from_response(response: Any) -> ModelUsage:
    usage_object = getattr(response, "usage", None)
    return ModelUsage(
        input_tokens=_optional_int(usage_object, "input_tokens"),
        output_tokens=_optional_int(usage_object, "output_tokens"),
        total_tokens=_optional_int(usage_object, "total_tokens"),
    )


def _optional_attr(value: Any, attribute: str) -> Any:
    if value is None:
        return None
    item = getattr(value, attribute, None)
    if item is None and isinstance(value, Mapping):
        item = value.get(attribute)
    return item


def _optional_int(value: Any, attribute: str) -> int | None:
    item = _optional_attr(value, attribute)
    return int(item) if item is not None else None
