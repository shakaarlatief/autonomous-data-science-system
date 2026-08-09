from __future__ import annotations

import json
from pathlib import Path

import pytest

from ads_v0.casegen import CaseConfig, generate_case_bundle
from ads_v0.model import ModelGeneration, ModelUsage, ScriptedModel
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


def _empty_patch() -> dict:
    return {
        "creates": [],
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


def test_open_feature_eligibility_question_becomes_repair_priority_after_invalidation(
    case_bundle: Path,
) -> None:
    runner = P0TreatmentRunner(
        bundle_dir=case_bundle,
        model=ScriptedModel([]),
        run_id="p0-open-feature-repair",
        max_model_calls=1,
    )

    train = runner.state.artifact_object("train.csv")
    assert train is not None
    runner.state.add_tags(
        train.id,
        ["metadata_inspected"],
        reason="Schema inspected.",
        trigger="train.csv",
    )
    runner.state.create_object(
        state_type="FACT",
        status="ACTIVE",
        scope="project",
        content="Prediction occurs at the beginning of the scoring period.",
        tags=["prediction_moment"],
    )
    runner.knowledge.evaluate(runner.state)
    activation = runner.knowledge.activations[("K-INFO-003", "project")]
    question_id = activation.instance_object_ids[0]
    assert runner.state.objects[question_id].status == "OPEN"
    assert "priority:repair" not in runner.state.objects[question_id].tags

    assumption = runner.state.create_object(
        state_type="ASSUMPTION",
        status="PROVISIONAL",
        scope="project",
        content="A candidate feature is available at prediction time.",
        tags=["feature_eligibility"],
    )
    changed = runner.state.update_status(
        assumption.id,
        "INVALIDATED",
        reason="Authoritative timing evidence invalidates the assumption.",
        trigger="timing_notice",
    )

    runner._reopen_knowledge_after_patch(runner.state, runner.knowledge, changed)

    question = runner.state.objects[question_id]
    assert question.status == "OPEN"
    assert "priority:repair" in question.tags


def test_action_can_resolve_the_pre_patch_motivator_that_generated_it(
    case_bundle: Path,
) -> None:
    runner = P0TreatmentRunner(
        bundle_dir=case_bundle,
        model=ScriptedModel([]),
        run_id="p0-prepatch-motivator",
        max_model_calls=1,
    )
    question = runner.state.create_object(
        state_type="QUESTION",
        status="OPEN",
        scope="project",
        content="Has the current blocking concern been resolved by existing evidence?",
        tags=["priority:blocking"],
    )

    result, completed = runner._process_payload(
        {
            "rationale": "Existing evidence resolves the question; continue inspection.",
            "state_patch": {
                "creates": [],
                "status_updates": [
                    {
                        "object_id": question.id,
                        "new_status": "RESOLVED",
                        "reason": "The required evidence was established on the prior turn.",
                        "source_refs": ["prior_harness_result"],
                    }
                ],
                "add_relations": [],
                "remove_relations": [],
            },
            "motivator_ids": [question.id],
            "command": {"type": "list_artifacts"},
        }
    )

    assert not completed
    assert result["status"] == "ok"
    assert runner.state.objects[question.id].status == "RESOLVED"
    actions = [obj for obj in runner.state.objects.values() if obj.type == "ACTION"]
    assert len(actions) == 1
    assert actions[0].status == "EXECUTED"
    assert actions[0].source_refs == [question.id]
    assert not any(
        event.event_type == "P0_STATE_CONTROL_ERROR"
        for event in runner.workspace.events
    )


def test_model_state_view_excludes_audit_only_actions_and_closed_controls(
    case_bundle: Path,
) -> None:
    runner = P0TreatmentRunner(
        bundle_dir=case_bundle,
        model=ScriptedModel([]),
        run_id="p0-compact-state-view",
        max_model_calls=1,
    )
    active_fact = runner.state.create_object(
        state_type="FACT",
        status="ACTIVE",
        scope="project",
        content="A current semantic fact that must remain visible.",
    )
    resolved_question = runner.state.create_object(
        state_type="QUESTION",
        status="RESOLVED",
        scope="project",
        content="A closed question whose semantic answer should live elsewhere in state.",
    )
    action = runner.state.create_action(
        command={
            "type": "execute_python",
            "input_artifacts": ["train.csv"],
            "category": "INSPECTION",
            "purpose": "Large historical action payload used only for audit.",
            "code": "print('audit-only-marker')\n" * 500,
        },
        motivator_ids=["O-0001"],
        status="EXECUTED",
        rationale="Historical controller action.",
    )

    full_snapshot_ids = {obj["id"] for obj in runner.state.snapshot()["objects"]}
    assert resolved_question.id in full_snapshot_ids
    assert action.id in full_snapshot_ids

    message = runner._state_view_message()
    payload = json.loads(message.content.split("\n", 1)[1])
    visible_objects = payload["state"]["objects"]
    visible_ids = {obj["id"] for obj in visible_objects}

    assert active_fact.id in visible_ids
    assert "O-0001" in visible_ids
    assert resolved_question.id not in visible_ids
    assert action.id not in visible_ids
    assert "audit-only-marker" not in message.content
    assert "recent_changes" not in payload["state"]
    assert all("created_step" not in obj for obj in visible_objects)
    assert all("updated_step" not in obj for obj in visible_objects)
    assert all(
        relation["source_id"] != action.id and relation["target_id"] != action.id
        for relation in payload["state"]["relations"]
    )


def test_next_state_view_exposes_client_ref_to_canonical_id_handoff(
    case_bundle: Path,
) -> None:
    runner = P0TreatmentRunner(
        bundle_dir=case_bundle,
        model=ScriptedModel([]),
        run_id="p0-client-ref-handoff",
        max_model_calls=1,
    )

    result, completed = runner._process_payload(
        {
            "rationale": "Record one observed fact and continue.",
            "state_patch": {
                "creates": [
                    {
                        "client_ref": "observed_fact",
                        "type": "FACT",
                        "status": "ACTIVE",
                        "scope": "project",
                        "content": "An observed fact requiring a canonical state ID.",
                        "source_refs": ["project_evidence"],
                        "tags": [],
                    }
                ],
                "status_updates": [],
                "add_relations": [],
                "remove_relations": [],
            },
            "motivator_ids": ["O-0001"],
            "command": {"type": "list_artifacts"},
        }
    )

    assert result["status"] == "ok"
    assert not completed
    message = runner._state_view_message()
    payload = json.loads(message.content.split("\n", 1)[1])
    mapping = payload["last_patch_client_ref_map"]
    assert mapping.keys() == {"observed_fact"}
    canonical_id = mapping["observed_fact"]
    assert canonical_id in runner.state.objects
    assert runner.state.objects[canonical_id].content.startswith("An observed fact")


class _UsageScriptedModel:
    def __init__(self, responses: list[dict], total_tokens: list[int]) -> None:
        self.responses = list(responses)
        self.total_tokens = list(total_tokens)
        self.index = 0

    def generate(self, messages):
        payload = self.responses[self.index]
        total = self.total_tokens[self.index]
        self.index += 1
        return ModelGeneration(
            payload=payload,
            model_name="usage-scripted-model",
            usage=ModelUsage(
                input_tokens=total,
                output_tokens=0,
                total_tokens=total,
            ),
        )


def test_terminal_completion_call_above_token_ceiling_is_budget_exceeded(
    case_bundle: Path,
) -> None:
    responses = [
        {
            "rationale": "Close provisional development.",
            "state_patch": _empty_patch(),
            "motivator_ids": ["O-0001"],
            "command": {
                "type": "phase_1_complete",
                "report": {
                    "summary": "Provisional position.",
                    "selected_features": ["tenure_months"],
                    "validation_approach": "Temporal development validation.",
                    "development_evidence": "Development-only evidence.",
                    "unresolved_issues": [],
                },
            },
        },
        {
            "rationale": "Lock development before final evaluation.",
            "state_patch": _empty_patch(),
            "motivator_ids": ["O-0001"],
            "command": {
                "type": "final_model_locked",
                "report": {
                    "summary": "Locked model.",
                    "selected_features": ["tenure_months"],
                    "validation_approach": "Temporal development validation.",
                    "development_evidence": "Development-only evidence.",
                    "limitations": [],
                },
            },
        },
        {
            "rationale": "Submit the terminal report.",
            "state_patch": _empty_patch(),
            "motivator_ids": ["O-0001"],
            "command": {
                "type": "submit_final_report",
                "report": {
                    "summary": "Project complete.",
                    "final_test_evidence": "Terminal accounting test.",
                    "claim_scope": "Accounting test only.",
                    "limitations": [],
                },
            },
        },
    ]
    runner = P0TreatmentRunner(
        bundle_dir=case_bundle,
        model=_UsageScriptedModel(responses, [10, 10, 90]),
        run_id="p0-terminal-budget-crossing",
        max_model_calls=5,
        max_total_tokens=100,
    )

    result = runner.run()

    assert result.completed
    assert result.total_tokens == 110
    assert result.budget_exhausted
    assert not result.completed_within_budget
    budget_events = [
        event
        for event in result.workspace.events
        if event.event_type == "RESOURCE_BUDGET_EXHAUSTED"
    ]
    assert len(budget_events) == 1
    assert (
        budget_events[0].blocked_reason
        == "total_token_budget_crossed_by_completed_terminal_call"
    )


def test_persistent_client_ref_alias_resolves_in_later_patch(case_bundle: Path) -> None:
    runner = P0TreatmentRunner(
        bundle_dir=case_bundle,
        model=ScriptedModel([]),
        run_id="p0-persistent-alias",
        max_model_calls=1,
    )

    first, _ = runner._process_payload(
        {
            "rationale": "Create a fact with a model-side alias.",
            "state_patch": {
                "creates": [
                    {
                        "client_ref": "F_alias",
                        "type": "FACT",
                        "status": "ACTIVE",
                        "scope": "project",
                        "content": "A durable fact referenced on a later turn.",
                        "source_refs": ["evidence"],
                        "tags": [],
                    }
                ],
                "status_updates": [],
                "add_relations": [],
                "remove_relations": [],
            },
            "motivator_ids": ["O-0001"],
            "command": {"type": "list_artifacts"},
        }
    )
    assert first["status"] == "ok"
    fact_id = runner._client_ref_aliases["F_alias"]

    second, _ = runner._process_payload(
        {
            "rationale": "Use the remembered fact alias in a later relation.",
            "state_patch": {
                "creates": [
                    {
                        "client_ref": "D_alias",
                        "type": "DECISION",
                        "status": "ACCEPTED",
                        "scope": "project",
                        "content": "A decision supported by the earlier fact.",
                        "source_refs": ["evidence"],
                        "tags": [],
                    }
                ],
                "status_updates": [],
                "add_relations": [
                    {
                        "source_ref": "F_alias",
                        "relation": "SUPPORTS",
                        "target_ref": "D_alias",
                    }
                ],
                "remove_relations": [],
            },
            "motivator_ids": ["O-0001"],
            "command": {"type": "list_artifacts"},
        }
    )

    assert second["status"] == "ok"
    decision_id = runner._client_ref_aliases["D_alias"]
    assert any(
        edge.source_id == fact_id
        and edge.relation == "SUPPORTS"
        and edge.target_id == decision_id
        for edge in runner.state.relations
    )
    payload = json.loads(runner._state_view_message().content.split("\n", 1)[1])
    assert payload["client_ref_aliases"]["F_alias"] == fact_id
    assert payload["client_ref_aliases"]["D_alias"] == decision_id


def test_same_patch_motivator_is_supplemental_when_current_motivator_exists(
    case_bundle: Path,
) -> None:
    runner = P0TreatmentRunner(
        bundle_dir=case_bundle,
        model=ScriptedModel([]),
        run_id="p0-supplemental-local-motivator",
        max_model_calls=1,
    )

    result, _ = runner._process_payload(
        {
            "rationale": "Record a new question while continuing the existing deliverable.",
            "state_patch": {
                "creates": [
                    {
                        "client_ref": "Q_local",
                        "type": "QUESTION",
                        "status": "OPEN",
                        "scope": "project",
                        "content": "A newly surfaced question for subsequent work.",
                        "source_refs": ["current_observation"],
                        "tags": [],
                    }
                ],
                "status_updates": [],
                "add_relations": [],
                "remove_relations": [],
            },
            "motivator_ids": ["O-0001", "Q_local"],
            "command": {"type": "list_artifacts"},
        }
    )

    assert result["status"] == "ok"
    question_id = runner._client_ref_aliases["Q_local"]
    actions = [obj for obj in runner.state.objects.values() if obj.type == "ACTION"]
    assert actions[-1].status == "EXECUTED"
    assert actions[-1].source_refs == ["O-0001", question_id]


def test_same_patch_only_motivator_cannot_bypass_prepatch_frontier(
    case_bundle: Path,
) -> None:
    runner = P0TreatmentRunner(
        bundle_dir=case_bundle,
        model=ScriptedModel([]),
        run_id="p0-no-retroactive-motivator",
        max_model_calls=1,
    )

    result, _ = runner._process_payload(
        {
            "rationale": "Attempt to invent the only motivator in the same response.",
            "state_patch": {
                "creates": [
                    {
                        "client_ref": "Q_local",
                        "type": "QUESTION",
                        "status": "OPEN",
                        "scope": "project",
                        "content": "A same-turn question cannot justify its own action alone.",
                        "source_refs": ["current_observation"],
                        "tags": [],
                    }
                ],
                "status_updates": [],
                "add_relations": [],
                "remove_relations": [],
            },
            "motivator_ids": ["Q_local"],
            "command": {"type": "list_artifacts"},
        }
    )

    assert result["status"] == "error"
    assert "Every P0 action must cite at least one current motivator ID" in result["error"]
    assert not any(
        obj.type == "QUESTION" and obj.content.startswith("A same-turn question")
        for obj in runner.state.objects.values()
    )


def test_support_loss_to_obligation_does_not_create_open_repair_blocker(
    case_bundle: Path,
) -> None:
    runner = P0TreatmentRunner(
        bundle_dir=case_bundle,
        model=ScriptedModel([]),
        run_id="p0-obligation-support-reassessment",
        max_model_calls=1,
    )
    old_decision = runner.state.create_object(
        state_type="DECISION",
        status="ACCEPTED",
        scope="project",
        content="Old project decision supporting the deliverable.",
    )
    runner.state.add_relation(old_decision.id, "SUPPORTS", "O-0001")

    result, _ = runner._process_payload(
        {
            "rationale": "Replace the old decision with current support for the deliverable.",
            "state_patch": {
                "creates": [
                    {
                        "client_ref": "replacement",
                        "type": "DECISION",
                        "status": "ACCEPTED",
                        "scope": "project",
                        "content": "Replacement project decision.",
                        "source_refs": ["new_evidence"],
                        "tags": [],
                    }
                ],
                "status_updates": [
                    {
                        "object_id": old_decision.id,
                        "new_status": "SUPERSEDED",
                        "reason": "Replacement evidence supports a new decision.",
                        "source_refs": ["new_evidence"],
                    }
                ],
                "add_relations": [
                    {
                        "source_ref": "replacement",
                        "relation": "SUPPORTS",
                        "target_ref": "O-0001",
                    }
                ],
                "remove_relations": [],
            },
            "motivator_ids": ["O-0001"],
            "command": {"type": "list_artifacts"},
        }
    )

    assert result["status"] == "ok"
    reassessments = [
        obj
        for obj in runner.state.objects.values()
        if obj.type == "OBLIGATION"
        and any(
            tag.endswith(":O-0001") and tag.startswith("support_reassessment:")
            for tag in obj.tags
        )
    ]
    assert len(reassessments) == 1
    assert reassessments[0].status == "SATISFIED"
    assert reassessments[0].id not in runner.state.frontier()["all_motivator_ids"]
