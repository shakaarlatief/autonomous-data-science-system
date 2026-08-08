from __future__ import annotations

import json
from types import SimpleNamespace

import pytest

from ads_v0.model import ModelMessage
from ads_v0.openai_model import OpenAIResponsesModel, TREATMENT_RESPONSE_SCHEMA


class FakeResponses:
    def __init__(self, payloads: list[dict]) -> None:
        self.payloads = list(payloads)
        self.calls: list[dict] = []

    def create(self, **kwargs):
        self.calls.append(kwargs)
        index = len(self.calls)
        payload = self.payloads[index - 1]
        return SimpleNamespace(
            id=f"resp-{index}",
            status="completed",
            model=kwargs["model"],
            output_text=json.dumps(payload),
            usage=SimpleNamespace(
                input_tokens=100 + index,
                output_tokens=20 + index,
                total_tokens=120 + 2 * index,
            ),
        )


class FakeClient:
    def __init__(self, payloads: list[dict]) -> None:
        self.responses = FakeResponses(payloads)


def test_openai_adapter_uses_strict_structured_outputs_and_threads_context() -> None:
    client = FakeClient(
        [
            {
                "rationale": "Inspect the artifact inventory.",
                "command": {"type": "list_artifacts"},
            },
            {
                "rationale": "Inspect training schema.",
                "command": {
                    "type": "table_metadata",
                    "artifact_id": "train.csv",
                    "purpose": "Understand the table structure.",
                },
            },
        ]
    )
    model = OpenAIResponsesModel(client=client)

    first_messages = [
        ModelMessage(role="system", content="system instructions"),
        ModelMessage(role="user", content="begin project"),
    ]
    first = model.generate(first_messages)

    first_request = client.responses.calls[0]
    assert first_request["model"] == "gpt-5.6-terra"
    assert first_request["reasoning"]["effort"] == "high"
    assert first_request["reasoning"]["context"] == "all_turns"
    assert first_request["text"]["format"]["type"] == "json_schema"
    assert first_request["text"]["format"]["strict"] is True
    assert first_request["text"]["format"]["schema"] == TREATMENT_RESPONSE_SCHEMA
    assert "previous_response_id" not in first_request
    assert first.payload["command"]["type"] == "list_artifacts"
    assert first.usage.input_tokens == 101

    second_messages = [
        *first_messages,
        ModelMessage(
            role="assistant",
            content=json.dumps(first.payload),
        ),
        ModelMessage(
            role="user",
            content='HARNESS_RESULT\n{"status":"ok","artifacts":[]}',
        ),
    ]
    second = model.generate(second_messages)

    second_request = client.responses.calls[1]
    assert second_request["previous_response_id"] == "resp-1"
    assert second_request["input"] == [
        {
            "role": "user",
            "content": 'HARNESS_RESULT\n{"status":"ok","artifacts":[]}',
        }
    ]
    assert second.payload["command"]["type"] == "table_metadata"
    assert second.usage.total_tokens == 124


def test_openai_adapter_rejects_threading_without_storage() -> None:
    with pytest.raises(ValueError, match="store=True"):
        OpenAIResponsesModel(
            client=FakeClient([]),
            store=False,
            use_previous_response_id=True,
        )


def test_openai_structured_schema_has_object_root_and_nested_anyof() -> None:
    assert TREATMENT_RESPONSE_SCHEMA["type"] == "object"
    assert TREATMENT_RESPONSE_SCHEMA["additionalProperties"] is False
    command_schema = TREATMENT_RESPONSE_SCHEMA["properties"]["command"]
    assert "anyOf" in command_schema
    assert len(command_schema["anyOf"]) == 8
    for variant in command_schema["anyOf"]:
        assert variant["type"] == "object"
        assert variant["additionalProperties"] is False
        assert set(variant["required"]) == set(variant["properties"])
