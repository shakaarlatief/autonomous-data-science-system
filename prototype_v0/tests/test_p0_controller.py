from __future__ import annotations

from pathlib import Path

import pytest

from ads_v0.casegen import CaseConfig, generate_case_bundle
from ads_v0.model import ScriptedModel
from ads_v0.p0_controller import P0TreatmentRunner


@pytest.fixture(scope="module")
def case_bundle(tmp_path_factory: pytest.TempPathFactory) -> Path:
    output = tmp_path_factory.mktemp("p0_controller_case") / "case"
    generate_case_bundle(output, CaseConfig())
    return output


def _activation_patch() -> dict:
    return {
        "creates": [
            {
                "client_ref": "future_fact",
                "type": "FACT",
                "status": "ACTIVE",
                "scope": "project",
                "content": "The objective is future monthly prediction over time.",
                "source_refs": ["observed_project_evidence"],
                "tags": ["future_prediction_objective", "temporal_structure"],
            },
            {
                "client_ref": "repeat_fact",
                "type": "FACT",
                "status": "ACTIVE",
                "scope": "project",
                "content": "Entities repeat across temporal observations.",
                "source_refs": ["observed_project_evidence"],
                "tags": ["repeated_entities"],
            },
        ],
        "status_updates": [],
        "add_relations": [],
        "remove_relations": [],
    }


def test_new_blocker_from_current_patch_applies_on_next_action_not_same_motivator_check(
    case_bundle: Path,
) -> None:
    response = {
        "rationale": "Record newly established temporal facts and continue inspection.",
        "state_patch": _activation_patch(),
        "motivator_ids": ["O-0001"],
        "command": {"type": "list_artifacts"},
    }
    result = P0TreatmentRunner(
        bundle_dir=case_bundle,
        model=ScriptedModel([response]),
        run_id="p0-activation-order",
        max_model_calls=1,
    ).run()

    assert any(event.event_type == "LIST_ARTIFACTS" for event in result.workspace.events)
    assert any(
        activation["component_id"] == "K-VAL-001"
        for activation in result.knowledge_activations
    )
    validation_questions = [
        obj
        for obj in result.state_snapshot["objects"]
        if "knowledge_instance:K-VAL-001" in obj["tags"]
    ]
    assert len(validation_questions) == 1
    assert validation_questions[0]["status"] == "OPEN"


def test_newly_activated_blocker_can_prevent_phase_transition(case_bundle: Path) -> None:
    response = {
        "rationale": "Record temporal facts and attempt to close Phase 1.",
        "state_patch": _activation_patch(),
        "motivator_ids": ["O-0001"],
        "command": {
            "type": "phase_1_complete",
            "report": {
                "summary": "Premature phase close.",
                "selected_features": ["tenure_months"],
                "validation_approach": "Temporal validation not yet fully resolved.",
                "development_evidence": "Provisional evidence.",
                "unresolved_issues": [],
            },
        },
    }
    result = P0TreatmentRunner(
        bundle_dir=case_bundle,
        model=ScriptedModel([response]),
        run_id="p0-new-blocker-phase-gate",
        max_model_calls=1,
    ).run()

    assert result.workspace.phase.value == "PHASE_1_PROVISIONAL_DEVELOPMENT"
    blocked_actions = [
        obj
        for obj in result.state_snapshot["objects"]
        if obj["type"] == "ACTION" and obj["status"] == "BLOCKED"
    ]
    assert len(blocked_actions) == 1
