from __future__ import annotations

import asyncio
import json
from pathlib import Path

from ads_system.application.reasoning import (
    ReasoningOutcome,
    ReasoningRequest,
    ReasoningTrace,
    ReasoningUsage,
)
from ads_system.application.retrieval import KnowledgeRetrievalHit
from experiments.methodological_navigation_coverage.adjudication import (
    BlindedCoverageJudgeResult,
)
from experiments.methodological_navigation_coverage.contract import (
    EvaluatorState,
    MethodologicalConcern,
    MethodologicalCoverageResult,
    SemanticMatch,
    load_frozen_contract,
    oracle_items_for_snapshot,
)
from experiments.methodological_navigation_coverage.runner import execute_experiment


class DeterministicDenseRetriever:
    """Small provider-free dense port used only to exercise orchestration."""

    def __init__(self, assets) -> None:
        ordered = sorted(assets, key=lambda item: item["stable_key"])
        self.assets = ordered

    def search(self, query: str, *, limit: int = 10):
        assert query
        return tuple(
            KnowledgeRetrievalHit(
                stable_key=str(item["stable_key"]),
                revision_id=str(item["revision_id"]),
                title=str(item["title"]),
                score=1.0 / rank,
                channel="DENSE_TEST_DOUBLE",
            )
            for rank, item in enumerate(self.assets[:limit], start=1)
        )


class FrozenTruthHarnessRuntime:
    """Evaluator-informed fake used only to test execution plumbing.

    This runtime is not scientific evidence. It deliberately uses frozen oracle
    truth for reasoner calls so all 108 observations reach the judge and the
    runner's complete scoring path is exercised without a provider.
    """

    def __init__(self, *, fail_first_once: bool = False) -> None:
        self.contract = load_frozen_contract()
        self.fail_first_once = fail_first_once
        self.failed = False
        self.calls = 0

    async def run(self, request: ReasoningRequest) -> ReasoningOutcome:
        self.calls += 1
        if self.fail_first_once and not self.failed:
            self.failed = True
            raise TimeoutError("deliberate provider-free transient failure")

        if request.structured_output_type is MethodologicalCoverageResult:
            result = self._reasoner_result(request)
        elif request.structured_output_type is BlindedCoverageJudgeResult:
            result = self._judge_result(request)
        else:
            raise AssertionError(
                f"unexpected structured output type: {request.structured_output_type}"
            )

        return ReasoningOutcome(
            result=result,
            usage=ReasoningUsage(
                input_tokens=160,
                output_tokens=40,
                total_tokens=200,
                cached_input_tokens=8,
                reasoning_tokens=12,
                service_tier="default",
                raw_provider_usage={
                    "responses": [
                        {
                            "input_tokens": 160,
                            "output_tokens": 40,
                            "service_tier": "default",
                        }
                    ]
                },
            ),
            trace=ReasoningTrace(
                run_id=request.run_id,
                request_digest=request.semantic_digest(),
                methodological_context_sha256=request.methodological_context_sha256,
                knowledge_revisions=request.knowledge_revisions,
                requested_model=request.model_configuration.requested_model,
                provider_model=request.model_configuration.requested_model,
                runtime_name="spec022-frozen-truth-harness-runtime",
                runtime_version="1.0",
            ),
            latency_seconds=0.001,
        )

    def _reasoner_result(self, request: ReasoningRequest) -> MethodologicalCoverageResult:
        evidence = dict(request.project_evidence)
        episode_id = str(evidence["episode_id"])
        snapshot_id = str(evidence["snapshot_id"])
        snapshot_objects = {
            str(item["object_id"]): item for item in evidence["objects"]
        }
        concerns: list[MethodologicalConcern] = []
        for item in oracle_items_for_snapshot(
            self.contract, episode_id, snapshot_id
        ):
            state = EvaluatorState(str(item["expected_state"]))
            if state not in {EvaluatorState.ACTIVE, EvaluatorState.MISSING_CONTEXT}:
                continue
            grounding = tuple(
                map(
                    str,
                    item["grounding_project_object_ids_by_snapshot"].get(
                        snapshot_id, []
                    ),
                )
            )
            if not grounding:
                grounding = (next(iter(snapshot_objects)),)
            question = None
            concern_state = "CURRENT"
            if state is EvaluatorState.MISSING_CONTEXT:
                concern_state = "MISSING_CONTEXT"
                question = str(
                    item.get("missing_context_question_semantics")
                    or "What missing prerequisite information is required?"
                )
            concerns.append(
                MethodologicalConcern(
                    local_concern_id=f"c-{item['oracle_id']}",
                    title=str(item["canonical_concern"]),
                    explanation=str(item["rationale"]),
                    state=concern_state,
                    grounding_project_object_ids=grounding,
                    missing_context_question=question,
                )
            )
        assert 1 <= len(concerns) <= 12
        return MethodologicalCoverageResult(
            summary="Frozen-truth fake output for execution-harness validation only.",
            concerns=tuple(concerns),
            warnings=(),
        )

    @staticmethod
    def _judge_result(request: ReasoningRequest) -> BlindedCoverageJudgeResult:
        evidence = dict(request.project_evidence)
        fixed = evidence["fixed_prematches"]
        assessments = []
        for pair in fixed:
            reasoner = pair["reasoner_concern"]
            oracle = pair["oracle_concern"]
            expected_state = str(oracle["expected_state"])
            assessments.append(
                SemanticMatch(
                    local_concern_id=str(reasoner["local_concern_id"]),
                    oracle_id=str(oracle["oracle_id"]),
                    state_equivalent=(
                        (expected_state == "MISSING_CONTEXT" and reasoner["state"] == "MISSING_CONTEXT")
                        or (expected_state != "MISSING_CONTEXT" and reasoner["state"] == "CURRENT")
                    ),
                    missing_context_question_equivalent=(
                        True if expected_state == "MISSING_CONTEXT" else None
                    ),
                )
            )
        return BlindedCoverageJudgeResult(
            fixed_prematch_assessments=tuple(assessments),
            semantic_matches=(),
            inactive_control_matches=(),
            unsupported_local_concern_ids=(),
            duplicate_local_concern_ids=(),
        )


def _dense_factory(assets):
    return DeterministicDenseRetriever(assets)


def test_spec022_runner_completes_216_call_matrix_and_seals_raw_first(
    tmp_path: Path,
) -> None:
    runtime = FrozenTruthHarnessRuntime()
    output_dir = tmp_path / "run"
    result = asyncio.run(
        execute_experiment(
            output_dir=output_dir,
            reasoner_runtime=runtime,
            judge_runtime=runtime,
            dense_retriever_factory=_dense_factory,
        )
    )

    assert result["execution_complete"] is True
    assert result["execution_integrity"] is True
    assert result["counts"] == {
        "planned_reasoner_observations": 108,
        "successful_reasoner_observations": 108,
        "planned_judge_observations": 108,
        "successful_judge_observations": 108,
        "completed_reasoner_judge_pairs": 108,
    }
    assert result["provider_attempts"]["used"] == 216
    assert result["provider_attempts"]["exhausted"] is False
    assert result["advancement_outcome"] is not None
    assert result["condition_metrics"] is not None
    assert result["gate_evaluation"] is not None
    assert result["diagnostics"] is not None
    assert runtime.calls == 216

    manifest = json.loads(
        (output_dir / "raw_manifest.json").read_text(encoding="utf-8")
    )
    assert manifest["raw_evidence_sealed"] is True
    assert set(manifest["files"]) == {
        "judge_attempts.jsonl",
        "navigation.jsonl",
        "reasoner_attempts.jsonl",
        "requests.jsonl",
        "usage.jsonl",
    }
    assert (output_dir / "interpretation" / "result.json").exists()

    judge_requests = [
        json.loads(line)
        for line in (output_dir / "raw" / "requests.jsonl")
        .read_text(encoding="utf-8")
        .splitlines()
        if '"role":"judge"' in line
    ]
    assert len(judge_requests) == 108
    visible = "\n".join(item["canonical_model_input"] for item in judge_requests)
    assert "ADS_HORIZON" not in visible
    assert "GENERIC" not in visible
    assert "ORACLE_HORIZON" not in visible
    assert "stable_key" not in visible
    assert "representation_map" not in visible

    usage_lines = (
        output_dir / "raw" / "usage.jsonl"
    ).read_text(encoding="utf-8")
    assert "raw_provider_usage" in usage_lines
    assert "service_tier" in usage_lines


def test_spec022_runner_preserves_retry_and_still_completes(tmp_path: Path) -> None:
    runtime = FrozenTruthHarnessRuntime(fail_first_once=True)
    output_dir = tmp_path / "retry"
    result = asyncio.run(
        execute_experiment(
            output_dir=output_dir,
            reasoner_runtime=runtime,
            judge_runtime=runtime,
            dense_retriever_factory=_dense_factory,
        )
    )

    assert result["execution_complete"] is True
    assert result["execution_integrity"] is True
    assert result["provider_attempts"]["used"] == 217
    assert runtime.calls == 217
    failed = [
        json.loads(line)
        for line in (output_dir / "raw" / "reasoner_attempts.jsonl")
        .read_text(encoding="utf-8")
        .splitlines()
        if '"status":"FAILED"' in line
    ]
    assert len(failed) == 1
    assert failed[0]["failure_category"] == "TRANSIENT_PROVIDER_FAILURE"
