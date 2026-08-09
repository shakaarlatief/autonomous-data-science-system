"""OpenAI Responses API adapter for the structured P0 response contract.

The implementation subclasses the already calibrated common OpenAI adapter so
client creation, provider retry semantics, threading behavior, error
classification, duplicate-output normalization, and usage accounting remain the
same as B0/B1. Only the strict response schema differs because P0 returns a state
patch and motivator references in addition to the same common treatment command.
"""

from __future__ import annotations

from typing import Any

from .model import ModelGeneration, ModelGenerationError
from .openai_model import (
    OpenAIResponsesModel,
    _optional_attr,
    _parse_structured_response_payload,
    _usage_from_response,
)
from .p0_schema import P0_RESPONSE_SCHEMA


class OpenAIP0ResponsesModel(OpenAIResponsesModel):
    """Use the common calibrated provider semantics with the P0 JSON schema."""

    def generate(self, messages):  # type: ignore[override]
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
                    "name": "prototype_v0_p0_treatment_command",
                    "strict": True,
                    "schema": P0_RESPONSE_SCHEMA,
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
                    "OpenAI P0 response did not complete successfully: "
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
            error_code = str(
                output_metadata.get("structured_output_error") or "invalid_json"
            )
            raise ModelGenerationError(
                "OpenAI P0 structured output was not one valid semantic response.",
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
                    "OpenAI P0 response did not provide an ID required for threading.",
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
