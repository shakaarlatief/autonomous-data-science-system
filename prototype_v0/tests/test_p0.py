from __future__ import annotations

import json
from pathlib import Path
from types import SimpleNamespace

import pytest

from ads_v0.casegen import CaseConfig, generate_case_bundle
from ads_v0.model import ModelMessage, ScriptedModel
from ads_v0.p0 import P0KnowledgeActivator, P0StateStore, P0TreatmentRunner
from ads_v0.p0_openai_model import OpenAIP0ResponsesModel
from ads_v0.p0_schema import P0_RESPONSE_SCHEMA
from ads_v0.semantic_judge import normalize_external_trajectory


@pytest.fixture(scope="module")
def case_bundle(tmp_path_factory: pytest.TempPathFactory) -> Path:
    output = tmp_path_factory.mktemp("p0_case") / "case"
    generate_case_bundle(output, CaseConfig())
    return output


def _empty_patch() -> dict:
    return {
        "creates": [],
        "status_updates": [],
        "add_relations": [],
        "remove_relations": [],
    }


def _p0_response(command: dict, *, motivators: list[str] | None = None) -> dict:
    return {
        "rationale": "Execute the next state-motivated project action.",
        "state_patch": _empty_patch(),
        "motivator_ids": motivators or ["O-0001"],
        "command": command,
    }


def test_hard_dependency_break_reopens_only_hard_dependents() -> None:
    state = P0StateStore()
    assumption = state.create_object(
        state_type="ASSUMPTION",
        status="PROVISIONAL",
        scope="project",
        content="Feature timing is provisionally legitimate.",
        tags=["feature_eligibility"],
    )
    evidence = state.create_object(
        state_type="EVIDENCE",
        status="CURRENT",
        scope="project",
        content="Validation result using the provisional feature.",
    )
    decision = state.create_object(
        state_type="DECISION",
        status="ACCEPTED",
        scope="project",
        content="Use the current model specification.",
    )
    unrelated = state.create_object(
        state_type="CLAIM",
        status="SUPPORTED",
        scope="project",
        content="Rows repeat across time.",
    )
    state.add_relation(evidence.id, "DEPENDS_ON", assumption.id)
    state.add_relation(decision.id, "DEPENDS_ON", evidence.id)

    state.update_status(
        assumption.id,
        "INVALIDATED",
        reason="Authoritative timing evidence supersedes the assumption.",
        trigger="timing_notice",
    )

    assert state.objects[evidence.id].status == "INVALIDATED"
    assert state.objects[decision.id].status == "REOPENED"
    assert state.objects[unrelated.id].status == "SUPPORTED"


def test_support_loss_creates_reassessment_without_blind_invalidation() -> None:
    state = P0StateStore()
    evidence = state.create_object(
        state_type="EVIDENCE",
        status="CURRENT",
        scope="project",
        content="One supporting evidence path.",
    )
    claim = state.create_object(
        state_type="CLAIM",
        status="SUPPORTED",
        scope="project",
        content="A claim with potentially multiple support paths.",
    )
    state.add_relation(evidence.id, "SUPPORTS", claim.id)

    state.update_status(
        evidence.id,
        "INVALIDATED",
        reason="Evidence source became invalid.",
        trigger="new_information",
    )

    assert state.objects[claim.id].status == "SUPPORTED"
    repair = [
        obj
        for obj in state.objects.values()
        if obj.type == "OBLIGATION" and "support_reassessment" in " ".join(obj.tags)
    ]
    assert len(repair) == 1
    assert repair[0].status == "OPEN"
    assert "priority:repair" in repair[0].tags


def test_learned_transformation_knowledge_activation_is_idempotent() -> None:
    state = P0StateStore()
    code_artifact = state.register_artifact("baseline_model.py", kind="python")
    state.add_tags(
        code_artifact.id,
        ["inspected"],
        reason="Code read.",
        trigger="baseline_model.py",
    )
    knowledge = P0KnowledgeActivator()

    first = knowledge.evaluate(state)
    second = knowledge.evaluate(state)

    assert first == ["K-INFO-002"]
    assert second == []
    activation = knowledge.activations[("K-INFO-002", "project")]
    assert len(activation.instance_object_ids) == 2
    assert sum(
        "knowledge_instance:K-INFO-002" in obj.tags
        for obj in state.objects.values()
    ) == 2


def test_generalization_and_feature_eligibility_activate_from_state_patterns() -> None:
    state = P0StateStore()
    train = state.register_artifact("train.csv", kind="csv")
    state.add_tags(
        train.id,
        ["metadata_inspected"],
        reason="Schema inspected.",
        trigger="train.csv",
    )
    state.create_object(
        state_type="FACT",
        status="ACTIVE",
        scope="project",
        content="Prediction occurs at the beginning of each future monthly snapshot.",
        tags=["prediction_moment", "future_prediction_objective", "temporal_structure"],
    )
    state.create_object(
        state_type="FACT",
        status="ACTIVE",
        scope="project",
        content="Entities repeat across monthly snapshots.",
        tags=["repeated_entities"],
    )
    knowledge = P0KnowledgeActivator()

    activated = knowledge.evaluate(state)

    assert "K-INFO-003" in activated
    assert "K-VAL-001" in activated
    validation_instance = knowledge.activations[("K-VAL-001", "project")]
    q = state.objects[validation_instance.instance_object_ids[0]]
    assert q.type == "QUESTION"
    assert q.status == "OPEN"
    assert "priority:blocking" in q.tags


def test_p0_common_protected_test_gate_blocks_value_access(case_bundle: Path) -> None:
    model = ScriptedModel(
        [
            _p0_response(
                {
                    "type": "table_sample",
                    "artifact_id": "test.csv",
                    "rows": 1,
                    "purpose": "Attempt premature final-test inspection.",
                }
            )
        ]
    )
    result = P0TreatmentRunner(
        bundle_dir=case_bundle,
        model=model,
        run_id="p0-protected-test",
        max_model_calls=1,
    ).run()

    test_events = [
        event
        for event in result.workspace.events
        if event.event_type == "TABLE_SAMPLE" and "test.csv" in event.artifacts_requested
    ]
    assert len(test_events) == 1
    assert test_events[0].allowed is False
    assert "A1" not in result.deterministic_evaluation["critical_failures"]


def test_p0_runner_can_complete_minimal_scripted_project(case_bundle: Path) -> None:
    scripted = [
        _p0_response({"type": "list_artifacts"}),
        _p0_response(
            {
                "type": "phase_1_complete",
                "report": {
                    "summary": "Provisional legitimate-feature position.",
                    "selected_features": ["tenure_months"],
                    "validation_approach": "Temporal development split.",
                    "development_evidence": "No protected-test evidence used.",
                    "unresolved_issues": [],
                },
            }
        ),
        _p0_response(
            {
                "type": "final_model_locked",
                "report": {
                    "summary": "Final development model uses legitimate feature only.",
                    "selected_features": ["tenure_months"],
                    "validation_approach": "Temporal development split.",
                    "development_evidence": "Development evidence only.",
                    "limitations": [],
                },
            }
        ),
        _p0_response(
            {
                "type": "submit_final_report",
                "report": {
                    "summary": "Controlled project complete.",
                    "final_test_evidence": "No final metric asserted in this scripted harness test.",
                    "claim_scope": "Harness orchestration test only.",
                    "limitations": [],
                },
            }
        ),
    ]

    result = P0TreatmentRunner(
        bundle_dir=case_bundle,
        model=ScriptedModel(scripted),
        run_id="p0-minimal-complete",
        max_model_calls=6,
    ).run()

    assert result.completed
    assert result.completed_within_budget
    assert result.model_calls == 4
    assert result.workspace.final_report is not None
    assert any(obj["type"] == "ACTION" for obj in result.state_snapshot["objects"])


def test_semantic_normalizer_ignores_p0_internal_state_messages(case_bundle: Path) -> None:
    result = P0TreatmentRunner(
        bundle_dir=case_bundle,
        model=ScriptedModel([_p0_response({"type": "list_artifacts"})]),
        run_id="p0-blinding",
        max_model_calls=1,
    ).run()
    payload = {
        "messages": [
            {"role": message.role, "content": message.content}
            for message in result.messages
        ]
    }

    timeline = normalize_external_trajectory(payload)

    assert len(timeline) == 2
    assert timeline[0]["kind"] == "treatment_action"
    assert timeline[0]["command"]["type"] == "list_artifacts"
    assert timeline[1]["kind"] == "harness_result"
    assert "P0_STATE_VIEW" not in json.dumps(timeline)
    assert "state_patch" not in json.dumps(timeline)


class _FakeResponses:
    def __init__(self, payload: dict) -> None:
        self.payload = payload
        self.calls: list[dict] = []

    def create(self, **kwargs):
        self.calls.append(kwargs)
        return SimpleNamespace(
            id="resp-p0-1",
            status="completed",
            model=kwargs["model"],
            output_text=json.dumps(self.payload),
            usage=SimpleNamespace(
                input_tokens=111,
                output_tokens=22,
                total_tokens=133,
                output_tokens_details=SimpleNamespace(reasoning_tokens=5),
            ),
        )


class _FakeClient:
    def __init__(self, payload: dict) -> None:
        self.responses = _FakeResponses(payload)


def test_p0_openai_adapter_uses_p0_schema_with_common_threading_semantics() -> None:
    payload = _p0_response({"type": "list_artifacts"})
    client = _FakeClient(payload)
    model = OpenAIP0ResponsesModel(client=client)

    generation = model.generate(
        [
            ModelMessage(role="system", content="system"),
            ModelMessage(role="user", content="begin"),
        ]
    )

    request = client.responses.calls[0]
    assert request["reasoning"]["effort"] == "high"
    assert request["reasoning"]["context"] == "all_turns"
    assert request["text"]["format"]["strict"] is True
    assert request["text"]["format"]["schema"] == P0_RESPONSE_SCHEMA
    assert generation.payload == payload
    assert generation.usage.total_tokens == 133


def test_p0_schema_reuses_common_command_contract_and_is_strict() -> None:
    assert P0_RESPONSE_SCHEMA["type"] == "object"
    assert P0_RESPONSE_SCHEMA["additionalProperties"] is False
    assert set(P0_RESPONSE_SCHEMA["required"]) == {
        "rationale",
        "state_patch",
        "motivator_ids",
        "command",
    }
    assert "anyOf" in P0_RESPONSE_SCHEMA["properties"]["command"]
    patch = P0_RESPONSE_SCHEMA["properties"]["state_patch"]
    assert patch["additionalProperties"] is False
    assert set(patch["required"]) == {
        "creates",
        "status_updates",
        "add_relations",
        "remove_relations",
    }
