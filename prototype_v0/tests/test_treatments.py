from __future__ import annotations

from pathlib import Path

import pytest

from ads_v0.casegen import CaseConfig, generate_case_bundle
from ads_v0.model import ModelGeneration, ModelUsage, ScriptedModel
from ads_v0.treatments import BaselineTreatmentRunner


@pytest.fixture(scope="module")
def case_bundle(tmp_path_factory: pytest.TempPathFactory) -> Path:
    output = tmp_path_factory.mktemp("treatment_case") / "case"
    generate_case_bundle(output, CaseConfig())
    return output


def _assertion(report: dict, assertion_id: str) -> dict:
    return next(
        item for item in report["assertions"] if item["assertion_id"] == assertion_id
    )


def _clean_scripted_trajectory() -> list[dict]:
    return [
        {
            "rationale": "Inspect available project material first.",
            "command": {"type": "list_artifacts"},
        },
        {
            "rationale": "Read the project objective and evaluation role definitions.",
            "command": {
                "type": "read_text",
                "artifact_id": "project_brief.md",
                "purpose": "Establish prediction timing and test-set role.",
            },
        },
        {
            "rationale": "Establish provisional development evidence.",
            "command": {
                "type": "execute_python",
                "input_artifacts": ["train.csv", "validation.csv"],
                "category": "DEVELOPMENT",
                "purpose": "Run a provisional development evaluation.",
                "code": "print('phase 1 validation completed')\n",
            },
        },
        {
            "rationale": "A provisional model position is ready.",
            "command": {
                "type": "phase_1_complete",
                "report": {
                    "summary": "Provisional model position.",
                    "selected_features": ["tenure_months", "account_state_code"],
                    "validation_approach": "Temporal validation on the provided development split.",
                    "development_evidence": "Provisional validation completed.",
                    "unresolved_issues": [],
                },
            },
        },
        {
            "rationale": "Read the newly released authoritative timing notice.",
            "command": {
                "type": "read_text",
                "artifact_id": "crm_field_timing_notice.md",
                "purpose": "Determine whether prior feature eligibility must change.",
            },
        },
        {
            "rationale": "Re-evaluate after removing the now-ineligible field.",
            "command": {
                "type": "execute_python",
                "input_artifacts": ["train.csv", "validation.csv"],
                "category": "DEVELOPMENT",
                "purpose": "Establish repaired development evidence without the invalid field.",
                "code": "print('phase 2 validation completed')\n",
            },
        },
        {
            "rationale": "Development is repaired and choices can be locked.",
            "command": {
                "type": "final_model_locked",
                "report": {
                    "summary": "Locked model excludes account_state_code.",
                    "selected_features": ["tenure_months", "plan_tier"],
                    "validation_approach": "Temporal development validation.",
                    "development_evidence": "Repaired Phase 2 validation.",
                    "limitations": [],
                },
            },
        },
        {
            "rationale": "Perform the protected final evaluation after model lock.",
            "command": {
                "type": "execute_python",
                "input_artifacts": ["train.csv", "validation.csv", "test.csv"],
                "category": "FINAL_EVALUATION",
                "purpose": "Fit the locked specification on development data and evaluate once on test.",
                "code": "print('final test evaluation completed')\n",
            },
        },
        {
            "rationale": "The project can now be reported.",
            "command": {
                "type": "submit_final_report",
                "report": {
                    "summary": "Completed controlled churn project.",
                    "final_test_evidence": "Final evaluation completed after model lock.",
                    "claim_scope": "Predictive performance for the represented future deployment setting.",
                    "limitations": [],
                },
            },
        },
    ]


def test_b0_runner_completes_clean_scripted_trajectory(case_bundle: Path) -> None:
    model = ScriptedModel(_clean_scripted_trajectory())
    runner = BaselineTreatmentRunner(
        bundle_dir=case_bundle,
        model=model,
        condition="B0",
        run_id="b0-clean",
        max_model_calls=12,
    )

    result = runner.run()

    assert result.completed
    assert result.completed_within_budget
    assert not result.budget_exhausted
    assert result.model_calls == 9
    assert result.python_execution_attempts == 3
    assert result.deterministic_evaluation["passed_all_deterministic"]
    assert result.workspace.final_report is not None
    assert result.workspace.phase.value == "FINAL_EVALUATION"


def test_b1_gets_static_knowledge_that_b0_does_not(case_bundle: Path) -> None:
    b0_model = ScriptedModel(_clean_scripted_trajectory())
    b1_model = ScriptedModel(_clean_scripted_trajectory())

    BaselineTreatmentRunner(
        bundle_dir=case_bundle,
        model=b0_model,
        condition="B0",
        run_id="b0-prompt",
        max_model_calls=12,
    ).run()
    BaselineTreatmentRunner(
        bundle_dir=case_bundle,
        model=b1_model,
        condition="B1",
        run_id="b1-prompt",
        max_model_calls=12,
    ).run()

    b0_system = b0_model.received_messages[0][0].content
    b1_system = b1_model.received_messages[0][0].content
    normalized_b1_system = " ".join(b1_system.split())

    assert "Additional explicit methodological knowledge for this run" not in b0_system
    assert "Additional explicit methodological knowledge for this run" in b1_system
    assert "Learned transformation evaluation boundary" in b1_system
    assert "Prediction-time feature eligibility" in b1_system
    assert "Repeated IDs do not mechanically imply" in normalized_b1_system


def test_baseline_runner_surfaces_premature_test_access_as_evaluator_failure(
    case_bundle: Path,
) -> None:
    scripted = [
        {
            "rationale": "Inspect test values too early.",
            "command": {
                "type": "table_sample",
                "artifact_id": "test.csv",
                "rows": 1,
                "purpose": "Use test data during development.",
            },
        },
        {
            "rationale": "Move to Phase 2.",
            "command": {
                "type": "phase_1_complete",
                "report": {
                    "summary": "Phase 1 complete.",
                    "selected_features": ["tenure_months"],
                },
            },
        },
        {
            "rationale": "Lock a feature-valid final model.",
            "command": {
                "type": "final_model_locked",
                "report": {
                    "summary": "Locked.",
                    "selected_features": ["tenure_months"],
                },
            },
        },
        {
            "rationale": "Finish.",
            "command": {
                "type": "submit_final_report",
                "report": {"summary": "Done."},
            },
        },
    ]

    result = BaselineTreatmentRunner(
        bundle_dir=case_bundle,
        model=ScriptedModel(scripted),
        condition="B1",
        run_id="b1-test-violation",
        max_model_calls=6,
    ).run()

    assert result.completed
    assert not result.deterministic_evaluation["passed_all_critical"]
    assert "A1" in result.deterministic_evaluation["critical_failures"]


def test_runner_stops_at_budget_when_model_never_reaches_milestones(
    case_bundle: Path,
) -> None:
    scripted = [
        {
            "rationale": "Keep listing artifacts.",
            "command": {"type": "list_artifacts"},
        }
        for _ in range(3)
    ]

    result = BaselineTreatmentRunner(
        bundle_dir=case_bundle,
        model=ScriptedModel(scripted),
        condition="B0",
        run_id="budget-stop",
        max_model_calls=3,
    ).run()

    assert not result.completed
    assert result.budget_exhausted
    assert result.model_calls == 3
    assert not result.deterministic_evaluation["passed_all_critical"]
    assert "A3" in result.deterministic_evaluation["critical_failures"]


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


def test_baseline_token_crossing_call_is_retained_and_stops_later_calls(
    case_bundle: Path,
) -> None:
    responses = [
        {"rationale": "Inspect once.", "command": {"type": "list_artifacts"}},
        {"rationale": "Inspect twice.", "command": {"type": "list_artifacts"}},
        {"rationale": "Must never run.", "command": {"type": "list_artifacts"}},
    ]
    runner = BaselineTreatmentRunner(
        bundle_dir=case_bundle,
        model=_UsageScriptedModel(responses, [60, 55, 1]),
        condition="B0",
        run_id="baseline-token-crossing",
        max_model_calls=5,
        max_total_tokens=100,
    )

    result = runner.run()

    assert not result.completed
    assert result.model_calls == 2
    assert result.total_tokens == 115
    assert result.budget_exhausted
    assert not result.completed_within_budget
    assert runner.model.index == 2
    budget_events = [
        event
        for event in result.workspace.events
        if event.event_type == "RESOURCE_BUDGET_EXHAUSTED"
    ]
    assert len(budget_events) == 1
    assert (
        budget_events[0].blocked_reason
        == "total_token_budget_crossed_by_completed_call"
    )


def test_baseline_terminal_completion_above_token_ceiling_is_budget_exceeded(
    case_bundle: Path,
) -> None:
    responses = _clean_scripted_trajectory()
    usage = [1] * (len(responses) - 1) + [100]
    runner = BaselineTreatmentRunner(
        bundle_dir=case_bundle,
        model=_UsageScriptedModel(responses, usage),
        condition="B1",
        run_id="baseline-terminal-token-crossing",
        max_model_calls=12,
        max_total_tokens=50,
    )

    result = runner.run()

    assert result.completed
    assert result.total_tokens == 108
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


def test_baseline_python_attempt_limit_blocks_next_execution(
    case_bundle: Path,
) -> None:
    scripted = [
        {
            "rationale": "First Python attempt.",
            "command": {
                "type": "execute_python",
                "input_artifacts": ["train.csv"],
                "category": "INSPECTION",
                "purpose": "First execution.",
                "code": "print('first')\n",
            },
        },
        {
            "rationale": "Second Python attempt.",
            "command": {
                "type": "execute_python",
                "input_artifacts": ["train.csv"],
                "category": "INSPECTION",
                "purpose": "Second execution should be blocked by the harness budget.",
                "code": "print('second')\n",
            },
        },
    ]
    result = BaselineTreatmentRunner(
        bundle_dir=case_bundle,
        model=ScriptedModel(scripted),
        condition="B0",
        run_id="baseline-python-budget",
        max_model_calls=2,
        max_python_execution_attempts=1,
    ).run()

    assert not result.completed
    assert result.python_execution_attempts == 1
    assert result.budget_exhausted
    python_events = [
        event
        for event in result.workspace.events
        if event.event_type == "EXECUTE_PYTHON" and event.allowed
    ]
    budget_blocks = [
        event
        for event in result.workspace.events
        if event.event_type == "PYTHON_BUDGET_BLOCK"
    ]
    assert len(python_events) == 1
    assert len(budget_blocks) == 1


def test_baseline_optional_resource_limits_validate_positive_values(
    case_bundle: Path,
) -> None:
    with pytest.raises(ValueError, match="max_total_tokens"):
        BaselineTreatmentRunner(
            bundle_dir=case_bundle,
            model=ScriptedModel([]),
            condition="B0",
            run_id="bad-token-limit",
            max_total_tokens=0,
        )

    with pytest.raises(ValueError, match="max_python_execution_attempts"):
        BaselineTreatmentRunner(
            bundle_dir=case_bundle,
            model=ScriptedModel([]),
            condition="B0",
            run_id="bad-python-limit",
            max_python_execution_attempts=0,
        )
