from __future__ import annotations

from dataclasses import replace
import json

import pytest

from ads_system.application.reasoning import KnowledgeRevisionPointer
from experiments.methodological_navigation_coverage.artifacts import (
    AttemptBudget,
    RawEvidenceWriter,
)
from experiments.methodological_navigation_coverage.contract import (
    CONDITIONS,
    EXPECTED_CANONICAL_SHA256,
    MethodologicalConcern,
    MethodologicalCoverageResult,
    Prematch,
    ReasonerPlanEntry,
    SemanticAdjudicationResult,
    SemanticMatch,
    build_blinded_judge_request,
    build_reasoner_plan,
    build_reasoner_request,
    canonical_json_bytes,
    canonical_project_state_bytes,
    deterministic_prematch,
    load_frozen_contract,
    oracle_items_for_snapshot,
    project_state_to_retrieval_text,
    public_reasoner_builder_parameters,
    serialize_reasoner_plan,
    snapshot_by_id,
    validate_result_grounding,
)
from experiments.methodological_navigation_coverage.scoring import (
    AdvancementOutcome,
    ConditionMetrics,
    deterministic_inactive_control_matches,
    evaluate_frozen_gates,
    score_observation,
)


def _valid_result() -> MethodologicalCoverageResult:
    return MethodologicalCoverageResult(
        summary="The operational cutoff must be made explicit.",
        concerns=(
            MethodologicalConcern(
                local_concern_id="c1",
                title="define the operational prediction moment",
                explanation="The scoring cutoff controls which information is legitimate.",
                state="CURRENT",
                grounding_project_object_ids=("E1-O1", "E1-O3"),
                missing_context_question=None,
            ),
        ),
        warnings=(),
    )


def _metrics(
    condition: str,
    *,
    weighted: float = 0.90,
    critical: float = 0.95,
    newly: float = 0.90,
    missing_recognition: float = 0.90,
    missing_question: float = 0.90,
    noise: float = 0.10,
    resolved: float = 0.05,
    mean_count: float = 7.0,
    horizon_critical: float = 0.95,
    horizon_weighted: float = 0.90,
    catastrophic: int = 0,
    majority: int = 0,
    temporal_false: int = 0,
) -> ConditionMetrics:
    return ConditionMetrics(
        condition=condition,
        observation_count=36,
        represented_recall=weighted,
        weighted_represented_recall=weighted,
        critical_recall=critical,
        newly_activated_recall=newly,
        missing_context_recognition_accuracy=missing_recognition,
        missing_context_question_correctness=missing_question,
        noise_ratio=noise,
        resolved_persistence_ratio=resolved,
        mean_output_concern_count=mean_count,
        horizon_critical_recall=horizon_critical,
        horizon_weighted_recall=horizon_weighted,
        catastrophic_critical_omissions=catastrophic,
        majority_critical_omissions=majority,
        e2_temporal_false_activation_records=temporal_false,
        per_episode_weighted_recall={
            "E1": weighted,
            "E2": weighted,
            "E3": weighted,
            "E4": weighted,
        },
    )


def test_frozen_contract_exact_counts_hashes_and_grounding() -> None:
    contract = load_frozen_contract()
    assert len(contract.universe["assets"]) == 28
    assert len(contract.universe["relations"]) == 15
    assert len(contract.episodes["episodes"]) == 4
    assert sum(len(item["snapshots"]) for item in contract.episodes["episodes"]) == 12
    assert len(contract.oracle["items"]) == 33
    assert sum(
        not item["stable_keys"] for item in contract.representation_map["mappings"]
    ) == 2
    assert {
        name: item["canonical_sha256"]
        for name, item in contract.manifest["files"].items()
    } == EXPECTED_CANONICAL_SHA256


def test_project_state_projection_is_deterministic_and_generic() -> None:
    contract = load_frozen_contract()
    snapshot = snapshot_by_id(contract, "E2", "E2-S0")
    first = project_state_to_retrieval_text("E2", snapshot)
    second = project_state_to_retrieval_text("E2", json.loads(json.dumps(snapshot)))
    assert first == second
    assert first.startswith("EPISODE: E2\nSNAPSHOT: E2-S0\nTRANSITION:")
    assert "FACT: project.generalization.is_future_facing=false" in first
    assert "OBJECT: E2-O3 | Variable | Inspection date metadata" in first
    assert "oracle" not in first.casefold()
    assert "stable_key" not in first


def test_reasoner_plan_is_exact_reproducible_108_matrix() -> None:
    contract = load_frozen_contract()
    first = build_reasoner_plan(contract)
    second = build_reasoner_plan(contract)
    assert first == second
    assert len(first) == 108
    assert len({item.observation_id for item in first}) == 108
    assert len({item.run_id for item in first}) == 108
    matrix = {
        (item.episode_id, item.snapshot_id, item.repetition, item.condition)
        for item in first
    }
    assert len(matrix) == 108
    assert {item.condition for item in first} == set(CONDITIONS)
    assert all(
        sum(
            item.episode_id == episode
            and item.snapshot_id == snapshot
            and item.repetition == repetition
            for item in first
        )
        == 3
        for episode in ("E1", "E2", "E3", "E4")
        for snapshot in (f"{episode}-S0", f"{episode}-S1", f"{episode}-S2")
        for repetition in (1, 2, 3)
    )
    text, digest = serialize_reasoner_plan(first)
    assert len(digest) == 64
    assert json.loads(text)[0]["observation_id"] == first[0].observation_id


def test_structured_result_validation_and_project_grounding() -> None:
    contract = load_frozen_contract()
    snapshot = snapshot_by_id(contract, "E1", "E1-S0")
    valid = _valid_result()
    validate_result_grounding(valid, snapshot)

    with pytest.raises(ValueError, match="CURRENT concern"):
        MethodologicalConcern(
            local_concern_id="bad",
            title="x",
            explanation="y",
            state="CURRENT",
            grounding_project_object_ids=("E1-O1",),
            missing_context_question="should be null",
        )
    with pytest.raises(ValueError, match="requires a concrete"):
        MethodologicalConcern(
            local_concern_id="bad",
            title="x",
            explanation="y",
            state="MISSING_CONTEXT",
            grounding_project_object_ids=("E1-O1",),
            missing_context_question=None,
        )
    invalid_grounding = MethodologicalCoverageResult(
        summary="x",
        concerns=(
            MethodologicalConcern(
                local_concern_id="bad",
                title="x",
                explanation="y",
                state="CURRENT",
                grounding_project_object_ids=("E1-UNKNOWN",),
                missing_context_question=None,
            ),
        ),
        warnings=(),
    )
    with pytest.raises(ValueError, match="unknown project-object IDs"):
        validate_result_grounding(invalid_grounding, snapshot)


def test_condition_project_state_is_byte_identical_and_oracle_not_in_ads_builder() -> None:
    contract = load_frozen_contract()
    snapshot = snapshot_by_id(contract, "E1", "E1-S0")
    plan = build_reasoner_plan(contract)
    matched = [
        item
        for item in plan
        if item.episode_id == "E1"
        and item.snapshot_id == "E1-S0"
        and item.repetition == 1
    ]
    generic_entry = next(item for item in matched if item.condition == "GENERIC")
    ads_entry = next(item for item in matched if item.condition == "ADS_HORIZON")
    generic = build_reasoner_request(
        entry=generic_entry,
        snapshot=snapshot,
        methodological_context_payload={},
        knowledge_revisions=(),
    )
    ads = build_reasoner_request(
        entry=ads_entry,
        snapshot=snapshot,
        methodological_context_payload={
            "methodological_horizon": [
                {
                    "title": "Prediction moment",
                    "purpose": "Define the operational prediction boundary.",
                    "applicability_state": "POSSIBLY_APPLICABLE",
                    "missing_context_keys": [],
                }
            ]
        },
        knowledge_revisions=(
            KnowledgeRevisionPointer(
                stable_key="prediction-moment",
                revision_id="00000000-0000-0000-0000-000000000001",
            ),
        ),
    )
    assert canonical_json_bytes(dict(generic.project_evidence)) == canonical_json_bytes(
        dict(ads.project_evidence)
    )
    assert canonical_project_state_bytes("E1", snapshot) == canonical_json_bytes(
        dict(ads.project_evidence)
    )
    assert "oracle" not in public_reasoner_builder_parameters()
    assert "representation_map" not in public_reasoner_builder_parameters()


def test_exact_alias_prematch_and_judge_blinding() -> None:
    contract = load_frozen_contract()
    snapshot = snapshot_by_id(contract, "E1", "E1-S0")
    entry = next(
        item
        for item in build_reasoner_plan(contract)
        if item.episode_id == "E1"
        and item.snapshot_id == "E1-S0"
        and item.repetition == 1
        and item.condition == "ADS_HORIZON"
    )
    result = _valid_result()
    oracle_items = oracle_items_for_snapshot(contract, "E1", "E1-S0")
    prematches = deterministic_prematch(result, oracle_items)
    assert prematches == (
        Prematch(
            local_concern_id="c1",
            oracle_id="E1-C01",
            matched_text="define the operational prediction moment",
        ),
    )
    judge = build_blinded_judge_request(
        entry=entry,
        snapshot=snapshot,
        result=result,
        oracle_items=oracle_items,
        prematches=prematches,
    )
    visible = judge.canonical_model_input()
    assert "ADS_HORIZON" not in visible
    assert "GENERIC" not in visible
    assert "ORACLE_HORIZON" not in visible
    assert "stable_keys" not in visible
    assert "representation_map" not in visible
    assert dict(judge.methodological_context_payload) == {}
    assert judge.knowledge_revisions == ()


def test_scoring_counts_recall_and_inactive_temporal_noise() -> None:
    contract = load_frozen_contract()
    e1_result = _valid_result()
    e1_adjudication = SemanticAdjudicationResult(
        matches=(
            SemanticMatch(
                local_concern_id="c1",
                oracle_id="E1-C01",
                state_equivalent=True,
                missing_context_question_equivalent=None,
            ),
        ),
        unsupported_local_concern_ids=(),
        duplicate_local_concern_ids=(),
    )
    score = score_observation(
        contract=contract,
        condition="GENERIC",
        episode_id="E1",
        snapshot_id="E1-S0",
        repetition=1,
        result=e1_result,
        adjudication=e1_adjudication,
    )
    assert score.represented_expected > 1
    assert score.represented_matched == 1
    assert score.critical_matched == 1
    assert score.output_count == 1

    e2_result = MethodologicalCoverageResult(
        summary="A time split is proposed incorrectly.",
        concerns=(
            MethodologicalConcern(
                local_concern_id="t1",
                title="Temporal Validation",
                explanation="Use a temporal split.",
                state="CURRENT",
                grounding_project_object_ids=("E2-O1", "E2-O3"),
                missing_context_question=None,
            ),
        ),
        warnings=(),
    )
    assert deterministic_inactive_control_matches(
        contract, "E2-S0", e2_result
    ) == {"t1": "temporal-validation"}
    e2_score = score_observation(
        contract=contract,
        condition="ADS_HORIZON",
        episode_id="E2",
        snapshot_id="E2-S0",
        repetition=1,
        result=e2_result,
        adjudication=SemanticAdjudicationResult(
            matches=(),
            unsupported_local_concern_ids=("t1",),
            duplicate_local_concern_ids=(),
        ),
    )
    assert e2_score.noise_count == 1
    assert e2_score.e2_temporal_false_activation_count == 1


def test_frozen_gate_outcome_taxonomy() -> None:
    promote = evaluate_frozen_gates(
        {
            "ADS_HORIZON": _metrics(
                "ADS_HORIZON",
                weighted=0.95,
                critical=1.00,
                newly=0.95,
                missing_recognition=0.95,
                missing_question=0.90,
                majority=0,
            ),
            "GENERIC": _metrics(
                "GENERIC",
                weighted=0.85,
                critical=0.90,
                newly=0.80,
                missing_recognition=0.80,
                missing_question=0.75,
                majority=3,
            ),
            "ORACLE_HORIZON": _metrics("ORACLE_HORIZON", weighted=0.98),
        },
        execution_integrity=True,
    )
    assert promote.all_required_gates_passed
    assert promote.positive_signal_count >= 1
    assert promote.outcome is AdvancementOutcome.PROMOTE

    equal = _metrics("ADS_HORIZON", weighted=0.90, critical=0.95)
    generic_equal = replace(equal, condition="GENERIC")
    oracle_equal = replace(equal, condition="ORACLE_HORIZON")
    safe = evaluate_frozen_gates(
        {
            "ADS_HORIZON": equal,
            "GENERIC": generic_equal,
            "ORACLE_HORIZON": oracle_equal,
        },
        execution_integrity=True,
    )
    assert safe.all_required_gates_passed
    assert safe.positive_signal_count == 0
    assert safe.outcome is AdvancementOutcome.SAFE

    failed = evaluate_frozen_gates(
        {
            "ADS_HORIZON": _metrics("ADS_HORIZON", weighted=0.80),
            "GENERIC": _metrics("GENERIC", weighted=0.90),
            "ORACLE_HORIZON": _metrics("ORACLE_HORIZON", weighted=0.95),
        },
        execution_integrity=True,
    )
    assert not failed.gates["MN-G04"]
    assert failed.outcome is AdvancementOutcome.FAIL

    incomplete = evaluate_frozen_gates(
        {
            "ADS_HORIZON": equal,
            "GENERIC": generic_equal,
            "ORACLE_HORIZON": oracle_equal,
        },
        execution_integrity=False,
    )
    assert incomplete.outcome is AdvancementOutcome.INCOMPLETE


def test_attempt_budget_and_raw_before_interpretation(tmp_path) -> None:
    budget = AttemptBudget()
    first = budget.record_attempt(role="reasoner", observation_id="obs-1")
    second = budget.record_attempt(
        role="reasoner",
        observation_id="obs-1",
        retry_reason="INVALID_STRUCTURED_OUTPUT",
    )
    assert first.attempt_number == 1
    assert second.attempt_number == 2
    with pytest.raises(RuntimeError, match="retry ceiling"):
        budget.record_attempt(
            role="reasoner",
            observation_id="obs-1",
            retry_reason="TRANSIENT_PROVIDER_FAILURE",
        )

    writer = RawEvidenceWriter(tmp_path / "run")
    writer.append("requests", {"observation_id": "obs-1"})
    writer.append("reasoner_attempts", {"attempt": 1, "ok": True})
    with pytest.raises(RuntimeError, match="sealed before interpretation"):
        writer.write_interpretation("result.json", {"outcome": "SHOULD_NOT_WRITE"})
    manifest = writer.seal()
    assert manifest["raw_evidence_sealed"] is True
    assert "requests.jsonl" in manifest["files"]
    with pytest.raises(RuntimeError, match="cannot be modified"):
        writer.append("usage", {"tokens": 1})
    path = writer.write_interpretation("result.json", {"outcome": "SAFE"})
    assert json.loads(path.read_text(encoding="utf-8"))["outcome"] == "SAFE"
