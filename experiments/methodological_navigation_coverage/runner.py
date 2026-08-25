"""Provider-neutral executable runner for frozen Specification 022.

The runner composes the already frozen benchmark, experiment-local knowledge
store, accepted lexical retrieval, injected dense retrieval, accepted Horizon
builder, ADS-owned ReasoningRuntime, stage-separated blinded adjudication, and
frozen scoring rules.

No provider runtime or provider credential is imported by this module. The same
entry point is exercised with fake runtimes in ordinary CI and may later be
called by a separately governed live entry point. All raw requests, navigation
traces, attempts, structured outputs, and usage metadata are sealed before any
scientific scoring or advancement classification is written.
"""

from __future__ import annotations

import copy
from collections.abc import Callable, Mapping, Sequence
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import platform
import subprocess
import tempfile
from typing import Any

from alembic import command
from alembic.config import Config

from ads_system.application.knowledge_interchange import (
    accept_candidate_bundle,
    export_current_accepted_snapshot,
    import_candidate_bundle,
)
from ads_system.application.ports import ReasoningRuntime
from ads_system.application.reasoning import (
    ReasoningOutcome,
    ReasoningRequest,
)
from ads_system.infrastructure.interchange.knowledge_bundle import (
    semantic_digest,
    validate_bundle,
    validate_import_safety,
)
from ads_system.infrastructure.persistence.engine import (
    create_operational_engine,
    sqlite_database_url,
)
from ads_system.infrastructure.persistence.uow import SqlAlchemyUnitOfWork
from ads_system.infrastructure.retrieval.sqlite_fts import SqliteFtsKnowledgeRetrieval

from experiments.methodological_navigation_coverage.adjudication import (
    BlindedCoverageJudgeResult,
    FinalizedAdjudication,
    build_stage2_judge_request,
    finalize_stage2_adjudication,
)
from experiments.methodological_navigation_coverage.artifacts import (
    AttemptBudget,
    RawEvidenceWriter,
)
from experiments.methodological_navigation_coverage.contract import (
    EXPECTED_CANONICAL_SHA256,
    MAX_TOTAL_PROVIDER_ATTEMPTS,
    PLANNED_JUDGE_OBSERVATIONS,
    PLANNED_REASONER_OBSERVATIONS,
    MethodologicalCoverageResult,
    ReasonerPlanEntry,
    build_reasoner_plan,
    build_reasoner_request,
    canonical_json_bytes,
    canonical_sha256,
    deterministic_prematch,
    load_frozen_contract,
    oracle_items_for_snapshot,
    serialize_reasoner_plan,
    snapshot_by_id,
    validate_result_grounding,
)
from experiments.methodological_navigation_coverage.diagnostics import (
    ObservationAttribution,
    build_diagnostic_summary,
    build_observation_attribution,
    score_with_semantic_inactive_controls,
)
from experiments.methodological_navigation_coverage.navigation import (
    MethodologicalHorizonContext,
    RetrievalPort,
    build_ads_horizon_context,
    build_oracle_horizon_context,
    empty_generic_context,
)
from experiments.methodological_navigation_coverage.scoring import (
    ScoredObservation,
    aggregate_condition,
    evaluate_frozen_gates,
)


ROOT = Path(__file__).resolve().parents[2]
RETRYABLE_REASONS = {
    "TRANSIENT_PROVIDER_FAILURE",
    "INVALID_STRUCTURED_OUTPUT",
}


@dataclass(frozen=True, slots=True)
class CompletedObservation:
    entry: ReasonerPlanEntry
    result: MethodologicalCoverageResult
    finalized: FinalizedAdjudication
    horizon: tuple[Any, ...]


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _source_head() -> str:
    try:
        completed = subprocess.run(
            ["git", "rev-parse", "HEAD"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
        )
        return completed.stdout.strip()
    except (OSError, subprocess.CalledProcessError):
        return "UNKNOWN"


def _upgrade(database_url: str) -> None:
    config = Config(str(ROOT / "alembic.ini"))
    config.set_main_option("script_location", str(ROOT / "migrations"))
    config.set_main_option("sqlalchemy.url", database_url)
    os.environ["ADS_DATABASE_URL"] = database_url
    try:
        command.upgrade(config, "head")
    finally:
        os.environ.pop("ADS_DATABASE_URL", None)


def _json_safe(value: Any) -> Any:
    if isinstance(value, Mapping):
        return {str(key): _json_safe(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [_json_safe(item) for item in value]
    if isinstance(value, (str, int, float, bool)) or value is None:
        return value
    return str(value)


def _usage_payload(outcome: ReasoningOutcome) -> dict[str, object]:
    usage = outcome.usage
    return {
        "input_tokens": usage.input_tokens,
        "output_tokens": usage.output_tokens,
        "total_tokens": usage.total_tokens,
        "cached_input_tokens": usage.cached_input_tokens,
        "reasoning_tokens": usage.reasoning_tokens,
        "service_tier": usage.service_tier,
        "raw_provider_usage": _json_safe(usage.raw_provider_usage),
    }


def _trace_payload(outcome: ReasoningOutcome) -> dict[str, object]:
    trace = outcome.trace
    return {
        "run_id": trace.run_id,
        "request_digest": trace.request_digest,
        "methodological_context_sha256": trace.methodological_context_sha256,
        "knowledge_revisions": [asdict(item) for item in trace.knowledge_revisions],
        "requested_model": trace.requested_model,
        "provider_model": trace.provider_model,
        "runtime_name": trace.runtime_name,
        "runtime_version": trace.runtime_version,
        "provider_response_ids": list(trace.provider_response_ids),
        "provider_request_ids": list(trace.provider_request_ids),
    }


def _structured_payload(result: Any) -> Mapping[str, object]:
    method = getattr(result, "to_payload", None)
    if not callable(method):
        raise ValueError("structured result does not expose to_payload")
    payload = method()
    if not isinstance(payload, Mapping):
        raise ValueError("structured result payload must be a mapping")
    return payload


def _request_record(
    *,
    role: str,
    observation_id: str,
    request: ReasoningRequest,
) -> dict[str, object]:
    return {
        "record_type": "REQUEST",
        "role": role,
        "observation_id": observation_id,
        "run_id": request.run_id,
        "request_digest": request.semantic_digest(),
        "system_instruction": request.system_instruction,
        "canonical_model_input": request.canonical_model_input(),
        "methodological_context_sha256": request.methodological_context_sha256,
        "knowledge_revisions": [asdict(item) for item in request.knowledge_revisions],
        "model_configuration": asdict(request.model_configuration),
        "structured_output_schema_id": request.structured_output_schema_id,
    }


def _context_record(
    episode_id: str,
    snapshot_id: str,
    context: MethodologicalHorizonContext,
) -> dict[str, object]:
    return {
        "episode_id": episode_id,
        "snapshot_id": snapshot_id,
        "condition": context.condition,
        "methodological_context_sha256": context.methodological_context_sha256,
        "knowledge_revisions": [asdict(item) for item in context.knowledge_revisions],
        "model_facing_payload": _json_safe(context.methodological_context_payload),
        "system_trace": _json_safe(context.system_trace),
    }


def _common_outcome_validation(
    request: ReasoningRequest,
    outcome: ReasoningOutcome,
) -> None:
    if outcome.trace.run_id != request.run_id:
        raise ValueError("runtime trace run_id does not match request")
    if outcome.trace.request_digest != request.semantic_digest():
        raise ValueError("runtime trace request digest does not match request")
    if (
        outcome.trace.methodological_context_sha256
        != request.methodological_context_sha256
    ):
        raise ValueError("runtime trace context digest does not match request")
    if outcome.trace.knowledge_revisions != request.knowledge_revisions:
        raise ValueError("runtime trace knowledge revisions do not match request")
    if outcome.trace.requested_model != request.model_configuration.requested_model:
        raise ValueError("runtime trace requested model does not match request")
    if not outcome.trace.provider_model.strip():
        raise ValueError("runtime trace provider model is empty")
    if not outcome.trace.runtime_name.strip() or not outcome.trace.runtime_version.strip():
        raise ValueError("runtime identity is incomplete")
    if outcome.usage.input_tokens <= 0 or outcome.usage.total_tokens <= 0:
        raise ValueError("runtime usage must report positive input and total tokens")


def _classify_runtime_exception(exc: Exception) -> str | None:
    if isinstance(exc, ValueError):
        return "INVALID_STRUCTURED_OUTPUT"
    if isinstance(exc, (TimeoutError, ConnectionError, OSError)):
        return "TRANSIENT_PROVIDER_FAILURE"
    name = type(exc).__name__.casefold()
    module = type(exc).__module__.casefold()
    message = str(exc).casefold()
    if any(
        token in name or token in message
        for token in (
            "modelbehavior",
            "structured output",
            "structured_output",
            "output validation",
        )
    ):
        return "INVALID_STRUCTURED_OUTPUT"
    if (
        module.startswith("openai")
        or module.startswith("agents")
        or any(
            token in name
            for token in (
                "apierror",
                "ratelimit",
                "apiconnection",
                "timeout",
            )
        )
    ):
        return "TRANSIENT_PROVIDER_FAILURE"
    return None


def _attempt_record(
    *,
    role: str,
    observation_id: str,
    request: ReasoningRequest,
    attempt_number: int,
    global_attempt: int,
    retry_reason: str | None,
    status: str,
    outcome: ReasoningOutcome | None = None,
    failure_category: str | None = None,
    failure: Exception | None = None,
) -> dict[str, object]:
    payload: dict[str, object] = {
        "role": role,
        "observation_id": observation_id,
        "run_id": request.run_id,
        "attempt_number": attempt_number,
        "global_provider_attempt": global_attempt,
        "retry_reason": retry_reason,
        "timestamp_utc": _utc_now(),
        "status": status,
        "request_digest": request.semantic_digest(),
    }
    if outcome is not None:
        payload["trace"] = _trace_payload(outcome)
        payload["latency_seconds"] = outcome.latency_seconds
        try:
            payload["structured_result"] = _json_safe(
                _structured_payload(outcome.result)
            )
        except ValueError:
            payload["structured_result_type"] = (
                f"{type(outcome.result).__module__}."
                f"{type(outcome.result).__qualname__}"
            )
    if failure_category is not None:
        payload["failure_category"] = failure_category
    if failure is not None:
        payload["failure_type"] = type(failure).__name__
        payload["failure_message"] = str(failure)
    return payload


async def _run_with_retry(
    *,
    runtime: ReasoningRuntime,
    request: ReasoningRequest,
    role: str,
    observation_id: str,
    budget: AttemptBudget,
    writer: RawEvidenceWriter,
    validator: Callable[[ReasoningOutcome], Any],
) -> tuple[ReasoningOutcome | None, Any | None]:
    retry_reason: str | None = None
    stream = "reasoner_attempts" if role == "reasoner" else "judge_attempts"
    for _ in range(2):
        if budget.total_attempts >= MAX_TOTAL_PROVIDER_ATTEMPTS:
            return None, None
        record = budget.record_attempt(
            role=role,
            observation_id=observation_id,
            retry_reason=retry_reason,
        )
        global_attempt = budget.total_attempts
        try:
            outcome = await runtime.run(request)
        except Exception as exc:
            category = _classify_runtime_exception(exc)
            if category is None:
                raise
            writer.append(
                stream,
                _attempt_record(
                    role=role,
                    observation_id=observation_id,
                    request=request,
                    attempt_number=record.attempt_number,
                    global_attempt=global_attempt,
                    retry_reason=record.retry_reason,
                    status="FAILED",
                    failure_category=category,
                    failure=exc,
                ),
            )
            if record.attempt_number == 1 and category in RETRYABLE_REASONS:
                retry_reason = category
                continue
            return None, None

        try:
            _common_outcome_validation(request, outcome)
            validated = validator(outcome)
        except ValueError as exc:
            category = "INVALID_STRUCTURED_OUTPUT"
            writer.append(
                stream,
                _attempt_record(
                    role=role,
                    observation_id=observation_id,
                    request=request,
                    attempt_number=record.attempt_number,
                    global_attempt=global_attempt,
                    retry_reason=record.retry_reason,
                    status="FAILED",
                    outcome=outcome,
                    failure_category=category,
                    failure=exc,
                ),
            )
            writer.append(
                "usage",
                {
                    "role": role,
                    "observation_id": observation_id,
                    "attempt_number": record.attempt_number,
                    "global_provider_attempt": global_attempt,
                    "usage": _usage_payload(outcome),
                },
            )
            if record.attempt_number == 1:
                retry_reason = category
                continue
            return None, None

        writer.append(
            stream,
            _attempt_record(
                role=role,
                observation_id=observation_id,
                request=request,
                attempt_number=record.attempt_number,
                global_attempt=global_attempt,
                retry_reason=record.retry_reason,
                status="SUCCESS",
                outcome=outcome,
            ),
        )
        writer.append(
            "usage",
            {
                "role": role,
                "observation_id": observation_id,
                "attempt_number": record.attempt_number,
                "global_provider_attempt": global_attempt,
                "usage": _usage_payload(outcome),
            },
        )
        return outcome, validated
    return None, None


def _condition_metrics_payload(metrics) -> dict[str, object]:
    payload = asdict(metrics)
    payload["per_episode_weighted_recall"] = dict(
        metrics.per_episode_weighted_recall
    )
    return payload


def _gate_payload(gate) -> dict[str, object]:
    return {
        "gates": dict(gate.gates),
        "positive_signals": dict(gate.positive_signals),
        "all_required_gates_passed": gate.all_required_gates_passed,
        "positive_signal_count": gate.positive_signal_count,
        "outcome": gate.outcome.value,
    }


def _technical_preflight(
    *,
    contract,
    plan: Sequence[ReasonerPlanEntry],
    contexts: Mapping[tuple[str, str, str], MethodologicalHorizonContext],
    requests: Mapping[str, ReasoningRequest],
    accepted_snapshot: Mapping[str, object],
) -> dict[str, bool]:
    accepted_assets = {
        (str(item["stable_key"]), str(item["revision_id"]))
        for item in accepted_snapshot["assets"]
    }
    frozen_assets = {
        (str(item["stable_key"]), str(item["revision_id"]))
        for item in contract.universe["assets"]
    }
    matched_state_equal = True
    for episode_id in ("E1", "E2", "E3", "E4"):
        for snapshot_id in (
            f"{episode_id}-S0",
            f"{episode_id}-S1",
            f"{episode_id}-S2",
        ):
            for repetition in (1, 2, 3):
                group = [
                    requests[item.observation_id]
                    for item in plan
                    if item.episode_id == episode_id
                    and item.snapshot_id == snapshot_id
                    and item.repetition == repetition
                ]
                state_bytes = {
                    canonical_json_bytes(dict(item.project_evidence)) for item in group
                }
                if len(state_bytes) != 1:
                    matched_state_equal = False

    return {
        "MN-INV-01_exact_frozen_fixture_hashes": all(
            len(value) == 64 for value in EXPECTED_CANONICAL_SHA256.values()
        ),
        "MN-INV-02_exact_108_reasoner_plan": len(plan)
        == PLANNED_REASONER_OBSERVATIONS,
        "MN-INV-03_unique_observation_and_run_ids": (
            len({item.observation_id for item in plan}) == len(plan)
            and len({item.run_id for item in plan}) == len(plan)
        ),
        "MN-INV-04_exact_36_snapshot_condition_contexts": len(contexts) == 36,
        "MN-INV-05_accepted_universe_exactly_frozen": accepted_assets
        == frozen_assets,
        "MN-INV-06_matched_project_state_bytes_equal": matched_state_equal,
        "MN-INV-07_no_oracle_in_generic_or_ads_reasoner_inputs": all(
            "oracle" not in request.canonical_model_input().casefold()
            for item in plan
            if item.condition in {"GENERIC", "ADS_HORIZON"}
            for request in (requests[item.observation_id],)
        ),
        "MN-INV-08_generic_has_no_methodological_context": all(
            not request.knowledge_revisions
            and dict(request.methodological_context_payload) == {}
            for item in plan
            if item.condition == "GENERIC"
            for request in (requests[item.observation_id],)
        ),
        "MN-INV-09_non_generic_context_is_nonempty": all(
            bool(request.knowledge_revisions)
            and bool(dict(request.methodological_context_payload))
            for item in plan
            if item.condition != "GENERIC"
            for request in (requests[item.observation_id],)
        ),
        "MN-INV-10_reasoner_model_treatment_exact": all(
            request.model_configuration.requested_model == "gpt-5.6-sol"
            and request.model_configuration.reasoning_effort == "medium"
            and request.model_configuration.verbosity == "low"
            and request.model_configuration.max_output_tokens == 5000
            for request in requests.values()
        ),
    }


def _ensure_empty_output_dir(output_dir: Path) -> None:
    if output_dir.exists() and any(output_dir.iterdir()):
        raise RuntimeError(
            "Specification 022 output directory must be empty to preserve append-only raw evidence"
        )
    output_dir.mkdir(parents=True, exist_ok=True)


async def execute_experiment(
    *,
    output_dir: Path,
    reasoner_runtime: ReasoningRuntime,
    judge_runtime: ReasoningRuntime,
    dense_retriever_factory: Callable[
        [Sequence[Mapping[str, Any]]], RetrievalPort
    ],
    execution_mode: str = "injected-provider-free",
) -> dict[str, object]:
    """Execute the exact frozen design through explicitly injected runtime ports."""

    _ensure_empty_output_dir(output_dir)
    writer = RawEvidenceWriter(output_dir)
    contract = load_frozen_contract()
    source_head = _source_head()
    started_at = _utc_now()
    plan = build_reasoner_plan(contract)
    plan_text, plan_sha256 = serialize_reasoner_plan(plan)
    writer.append(
        "requests",
        {
            "record_type": "REASONER_PLAN",
            "plan_sha256": plan_sha256,
            "entries": json.loads(plan_text),
        },
    )

    engine = None
    contexts: dict[tuple[str, str, str], MethodologicalHorizonContext] = {}
    requests: dict[str, ReasoningRequest] = {}
    accepted_snapshot: Mapping[str, object]
    accepted_digest: str

    with tempfile.TemporaryDirectory(prefix="ads-spec022-") as temp_dir:
        database_url = sqlite_database_url(Path(temp_dir) / "spec022.sqlite3")
        _upgrade(database_url)
        engine = create_operational_engine(database_url)
        uow_factory = lambda: SqlAlchemyUnitOfWork(engine)
        lexical = SqliteFtsKnowledgeRetrieval(engine)
        try:
            candidate = copy.deepcopy(dict(contract.universe))
            candidate["bundle_kind"] = "CANDIDATE_SET"
            validate_bundle(candidate)
            validate_import_safety(candidate)
            import_candidate_bundle(candidate, uow_factory=uow_factory)
            if lexical.rebuild() != 0:
                raise RuntimeError("candidate benchmark knowledge entered lexical authority")
            accept_candidate_bundle(candidate, uow_factory=uow_factory)
            if lexical.rebuild() != 28 or lexical.indexed_document_count() != 28:
                raise RuntimeError("accepted benchmark lexical index is not exactly 28 assets")
            accepted_snapshot = export_current_accepted_snapshot(uow_factory=uow_factory)
            accepted_digest = semantic_digest(accepted_snapshot)
            dense = dense_retriever_factory(contract.universe["assets"])

            for episode in contract.episodes["episodes"]:
                episode_id = str(episode["episode_id"])
                for snapshot in episode["snapshots"]:
                    snapshot_id = str(snapshot["snapshot_id"])
                    generic = empty_generic_context()
                    ads = build_ads_horizon_context(
                        episode_id=episode_id,
                        snapshot=snapshot,
                        lexical_retriever=lexical,
                        dense_retriever=dense,
                        uow_factory=uow_factory,
                    )
                    oracle = build_oracle_horizon_context(
                        contract=contract,
                        episode_id=episode_id,
                        snapshot=snapshot,
                        uow_factory=uow_factory,
                    )
                    for context in (generic, ads, oracle):
                        key = (episode_id, snapshot_id, context.condition)
                        contexts[key] = context
                        writer.append(
                            "navigation",
                            _context_record(episode_id, snapshot_id, context),
                        )

            for entry in plan:
                snapshot = snapshot_by_id(
                    contract, entry.episode_id, entry.snapshot_id
                )
                context = contexts[
                    (entry.episode_id, entry.snapshot_id, entry.condition)
                ]
                request = build_reasoner_request(
                    entry=entry,
                    snapshot=snapshot,
                    methodological_context_payload=context.methodological_context_payload,
                    knowledge_revisions=context.knowledge_revisions,
                )
                requests[entry.observation_id] = request
                writer.append(
                    "requests",
                    _request_record(
                        role="reasoner",
                        observation_id=entry.observation_id,
                        request=request,
                    ),
                )

            technical_preflight = _technical_preflight(
                contract=contract,
                plan=plan,
                contexts=contexts,
                requests=requests,
                accepted_snapshot=accepted_snapshot,
            )
            if not all(technical_preflight.values()):
                failed = sorted(
                    key for key, value in technical_preflight.items() if not value
                )
                raise RuntimeError(
                    f"Specification 022 technical preflight failed: {failed}"
                )

            budget = AttemptBudget()
            reasoner_successes = 0
            judge_successes = 0
            completed: list[CompletedObservation] = []

            for entry in plan:
                if budget.total_attempts >= MAX_TOTAL_PROVIDER_ATTEMPTS:
                    break
                snapshot = snapshot_by_id(
                    contract, entry.episode_id, entry.snapshot_id
                )
                reasoner_request = requests[entry.observation_id]

                def validate_reasoner(outcome: ReasoningOutcome):
                    if not isinstance(outcome.result, MethodologicalCoverageResult):
                        raise ValueError(
                            "reasoner did not return MethodologicalCoverageResult"
                        )
                    validate_result_grounding(outcome.result, snapshot)
                    return outcome.result

                _, reasoner_result = await _run_with_retry(
                    runtime=reasoner_runtime,
                    request=reasoner_request,
                    role="reasoner",
                    observation_id=entry.observation_id,
                    budget=budget,
                    writer=writer,
                    validator=validate_reasoner,
                )
                if reasoner_result is None:
                    continue
                reasoner_successes += 1

                oracle_items = oracle_items_for_snapshot(
                    contract, entry.episode_id, entry.snapshot_id
                )
                prematches = deterministic_prematch(
                    reasoner_result, oracle_items
                )
                judge_request, control_map = build_stage2_judge_request(
                    contract=contract,
                    entry=entry,
                    snapshot=snapshot,
                    result=reasoner_result,
                    oracle_items=oracle_items,
                    prematches=prematches,
                )
                writer.append(
                    "requests",
                    _request_record(
                        role="judge",
                        observation_id=entry.observation_id,
                        request=judge_request,
                    ),
                )

                def validate_judge(outcome: ReasoningOutcome):
                    if not isinstance(outcome.result, BlindedCoverageJudgeResult):
                        raise ValueError(
                            "judge did not return BlindedCoverageJudgeResult"
                        )
                    return finalize_stage2_adjudication(
                        judge_result=outcome.result,
                        reasoner_result=reasoner_result,
                        oracle_items=oracle_items,
                        prematches=prematches,
                        control_map=control_map,
                    )

                _, finalized = await _run_with_retry(
                    runtime=judge_runtime,
                    request=judge_request,
                    role="judge",
                    observation_id=entry.observation_id,
                    budget=budget,
                    writer=writer,
                    validator=validate_judge,
                )
                if finalized is None:
                    continue
                judge_successes += 1
                context = contexts[
                    (entry.episode_id, entry.snapshot_id, entry.condition)
                ]
                completed.append(
                    CompletedObservation(
                        entry=entry,
                        result=reasoner_result,
                        finalized=finalized,
                        horizon=tuple(context.included),
                    )
                )

            accepted_after = export_current_accepted_snapshot(
                uow_factory=uow_factory
            )
            authoritative_knowledge_unchanged = (
                accepted_after == accepted_snapshot
                and semantic_digest(accepted_after) == accepted_digest
            )
        finally:
            engine.dispose()

    raw_manifest = writer.seal()
    raw_manifest_sha256 = canonical_sha256(raw_manifest)
    execution_complete = (
        reasoner_successes == PLANNED_REASONER_OBSERVATIONS
        and judge_successes == PLANNED_JUDGE_OBSERVATIONS
        and len(completed) == PLANNED_REASONER_OBSERVATIONS
    )
    execution_integrity = bool(
        execution_complete
        and all(technical_preflight.values())
        and authoritative_knowledge_unchanged
        and budget.total_attempts <= MAX_TOTAL_PROVIDER_ATTEMPTS
        and writer.sealed
    )

    result: dict[str, object] = {
        "specification": "022-v0.1",
        "source_head": source_head,
        "started_at_utc": started_at,
        "finished_at_utc": _utc_now(),
        "execution_mode": execution_mode,
        "python_version": platform.python_version(),
        "reasoner_plan_sha256": plan_sha256,
        "fixture_canonical_sha256": dict(EXPECTED_CANONICAL_SHA256),
        "accepted_benchmark_snapshot_semantic_digest": accepted_digest,
        "raw_manifest_sha256": raw_manifest_sha256,
        "counts": {
            "planned_reasoner_observations": PLANNED_REASONER_OBSERVATIONS,
            "successful_reasoner_observations": reasoner_successes,
            "planned_judge_observations": PLANNED_JUDGE_OBSERVATIONS,
            "successful_judge_observations": judge_successes,
            "completed_reasoner_judge_pairs": len(completed),
        },
        "provider_attempts": {
            "used": budget.total_attempts,
            "maximum": MAX_TOTAL_PROVIDER_ATTEMPTS,
            "exhausted": budget.total_attempts >= MAX_TOTAL_PROVIDER_ATTEMPTS,
            "records": [asdict(item) for item in budget.records],
        },
        "technical_preflight": technical_preflight,
        "authoritative_knowledge_unchanged": authoritative_knowledge_unchanged,
        "execution_complete": execution_complete,
        "execution_integrity": execution_integrity,
        "gate_evaluation": None,
        "condition_metrics": None,
        "diagnostics": None,
        "advancement_outcome": None,
    }

    if execution_integrity:
        scores: list[ScoredObservation] = []
        attributions: list[ObservationAttribution] = []
        for item in completed:
            entry = item.entry
            score = score_with_semantic_inactive_controls(
                contract=contract,
                condition=entry.condition,
                episode_id=entry.episode_id,
                snapshot_id=entry.snapshot_id,
                repetition=entry.repetition,
                result=item.result,
                finalized=item.finalized,
                horizon=item.horizon if entry.condition == "ADS_HORIZON" else (),
            )
            scores.append(score)
            attributions.append(
                build_observation_attribution(
                    contract=contract,
                    condition=entry.condition,
                    episode_id=entry.episode_id,
                    snapshot_id=entry.snapshot_id,
                    repetition=entry.repetition,
                    finalized=item.finalized,
                    horizon=item.horizon if entry.condition == "ADS_HORIZON" else (),
                )
            )
        metrics_by_condition = {
            condition: aggregate_condition(
                [item for item in scores if item.condition == condition]
            )
            for condition in ("ADS_HORIZON", "GENERIC", "ORACLE_HORIZON")
        }
        gate = evaluate_frozen_gates(
            metrics_by_condition,
            execution_integrity=True,
        )
        diagnostics = build_diagnostic_summary(contract, attributions)
        result["condition_metrics"] = {
            key: _condition_metrics_payload(value)
            for key, value in metrics_by_condition.items()
        }
        result["gate_evaluation"] = _gate_payload(gate)
        result["diagnostics"] = diagnostics
        result["advancement_outcome"] = gate.outcome.value

    writer.write_interpretation("result.json", result)
    return result
