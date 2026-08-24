"""Deterministic scoring and frozen gate evaluation for Specification 022."""

from __future__ import annotations

from dataclasses import dataclass
from enum import StrEnum
from typing import Mapping, Sequence

from ads_system.application.horizon_models import HorizonCandidate

from experiments.methodological_navigation_coverage.contract import (
    EvaluatorState,
    FrozenContract,
    MethodologicalCoverageResult,
    SemanticAdjudicationResult,
    normalize_concern_text,
    oracle_items_for_snapshot,
    validate_semantic_adjudication,
)


class AdvancementOutcome(StrEnum):
    PROMOTE = "PROMOTE_STATE_DRIVEN_NAVIGATION_SEAM"
    SAFE = "SAFE_BUT_NOT_DIFFERENTIATED"
    FAIL = "FAIL"
    INCOMPLETE = "INCOMPLETE"


@dataclass(frozen=True, slots=True)
class ScoredObservation:
    condition: str
    episode_id: str
    snapshot_id: str
    repetition: int
    represented_expected: int
    represented_matched: int
    represented_weight: int
    represented_weight_matched: int
    critical_expected: int
    critical_matched: int
    newly_active_expected: int
    newly_active_matched: int
    missing_context_expected: int
    missing_context_recognition_correct: int
    missing_context_question_correct: int
    noise_count: int
    output_count: int
    resolved_persistence_count: int
    resolved_persistence_opportunities: int
    e2_temporal_false_activation_count: int
    horizon_critical_expected: int
    horizon_critical_matched: int
    horizon_weight: int
    horizon_weight_matched: int
    critical_obligation_ids: tuple[str, ...]
    critical_matched_ids: tuple[str, ...]


@dataclass(frozen=True, slots=True)
class ConditionMetrics:
    condition: str
    observation_count: int
    represented_recall: float
    weighted_represented_recall: float
    critical_recall: float
    newly_activated_recall: float
    missing_context_recognition_accuracy: float
    missing_context_question_correctness: float
    noise_ratio: float
    resolved_persistence_ratio: float
    mean_output_concern_count: float
    horizon_critical_recall: float
    horizon_weighted_recall: float
    catastrophic_critical_omissions: int
    majority_critical_omissions: int
    e2_temporal_false_activation_records: int
    per_episode_weighted_recall: Mapping[str, float]


@dataclass(frozen=True, slots=True)
class GateEvaluation:
    gates: Mapping[str, bool]
    positive_signals: Mapping[str, bool]
    outcome: AdvancementOutcome

    @property
    def all_required_gates_passed(self) -> bool:
        return all(self.gates.get(f"MN-G{index:02d}", False) for index in range(1, 16))

    @property
    def positive_signal_count(self) -> int:
        return sum(bool(value) for value in self.positive_signals.values())


def _ratio(numerator: int | float, denominator: int | float) -> float:
    if denominator == 0:
        return 1.0
    return float(numerator) / float(denominator)


def _representation_map(contract: FrozenContract) -> dict[str, tuple[str, ...]]:
    return {
        str(item["oracle_id"]): tuple(map(str, item["stable_keys"]))
        for item in contract.representation_map["mappings"]
    }


def _snapshot_order(contract: FrozenContract, episode_id: str) -> tuple[str, ...]:
    episode = next(
        item for item in contract.episodes["episodes"] if item["episode_id"] == episode_id
    )
    return tuple(str(item["snapshot_id"]) for item in episode["snapshots"])


def _state_at(
    item: Mapping[str, object],
    snapshot_id: str,
    default_state: str,
) -> EvaluatorState:
    state_by_snapshot = item.get("state_by_snapshot", {})
    if not isinstance(state_by_snapshot, Mapping):
        raise ValueError("oracle state_by_snapshot must be a mapping")
    return EvaluatorState(str(state_by_snapshot.get(snapshot_id, default_state)))


def _is_newly_active(
    contract: FrozenContract,
    item: Mapping[str, object],
    episode_id: str,
    snapshot_id: str,
) -> bool:
    order = _snapshot_order(contract, episode_id)
    index = order.index(snapshot_id)
    default_state = str(contract.oracle["default_unspecified_state"])
    current = _state_at(item, snapshot_id, default_state)
    if current not in {EvaluatorState.ACTIVE, EvaluatorState.MISSING_CONTEXT}:
        return False
    previous = (
        EvaluatorState.INACTIVE
        if index == 0
        else _state_at(item, order[index - 1], default_state)
    )
    return previous in {EvaluatorState.INACTIVE, EvaluatorState.RESOLVED}


def _resolved_persistence_opportunity(
    contract: FrozenContract,
    item: Mapping[str, object],
    episode_id: str,
    snapshot_id: str,
) -> bool:
    order = _snapshot_order(contract, episode_id)
    index = order.index(snapshot_id)
    if index == 0:
        return False
    default_state = str(contract.oracle["default_unspecified_state"])
    if _state_at(item, snapshot_id, default_state) is not EvaluatorState.RESOLVED:
        return False
    return any(
        _state_at(item, earlier, default_state)
        in {EvaluatorState.ACTIVE, EvaluatorState.MISSING_CONTEXT}
        for earlier in order[:index]
    )


def deterministic_inactive_control_matches(
    contract: FrozenContract,
    snapshot_id: str,
    result: MethodologicalCoverageResult,
) -> dict[str, str]:
    """Match explicit inactive controls by frozen deterministic text aliases.

    This evaluator-side helper never enters model input. It uses only exact
    normalized asset title, stable key, aliases, and lexical terms. Richer
    semantic inactive-control adjudication would require a separately frozen
    judge contract.
    """

    controls = set(
        map(
            str,
            contract.oracle["inactive_controls_by_snapshot"].get(snapshot_id, []),
        )
    )
    asset_by_key = {
        str(item["stable_key"]): item for item in contract.universe["assets"]
    }
    lookup: dict[str, str] = {}
    for stable_key in sorted(controls):
        asset = asset_by_key[stable_key]
        profile = asset.get("retrieval_profile", {})
        values = [stable_key, str(asset["title"])]
        if isinstance(profile, Mapping):
            values.extend(map(str, profile.get("aliases", [])))
            values.extend(map(str, profile.get("lexical_terms", [])))
        for value in values:
            lookup.setdefault(normalize_concern_text(value), stable_key)

    matches: dict[str, str] = {}
    for concern in result.concerns:
        stable_key = lookup.get(normalize_concern_text(concern.title))
        if stable_key is not None:
            matches[concern.local_concern_id] = stable_key
    return matches


def score_observation(
    *,
    contract: FrozenContract,
    condition: str,
    episode_id: str,
    snapshot_id: str,
    repetition: int,
    result: MethodologicalCoverageResult,
    adjudication: SemanticAdjudicationResult,
    horizon: Sequence[HorizonCandidate] = (),
) -> ScoredObservation:
    oracle_items = oracle_items_for_snapshot(contract, episode_id, snapshot_id)
    validate_semantic_adjudication(adjudication, result, oracle_items)
    mapping = _representation_map(contract)
    weights = {str(key): int(value) for key, value in contract.oracle["importance_weights"].items()}
    item_by_id = {str(item["oracle_id"]): item for item in oracle_items}
    concern_by_id = {item.local_concern_id: item for item in result.concerns}
    match_by_oracle = {match.oracle_id: match for match in adjudication.matches}
    matched_local_ids = {match.local_concern_id for match in adjudication.matches}
    horizon_keys = {item.stable_key for item in horizon}

    represented_expected = 0
    represented_matched = 0
    represented_weight = 0
    represented_weight_matched = 0
    critical_expected = 0
    critical_matched = 0
    newly_active_expected = 0
    newly_active_matched = 0
    missing_expected = 0
    missing_recognition = 0
    missing_question = 0
    horizon_critical_expected = 0
    horizon_critical_matched = 0
    horizon_weight = 0
    horizon_weight_matched = 0
    critical_obligation_ids: list[str] = []
    critical_matched_ids: list[str] = []

    for oracle_id, item in item_by_id.items():
        state = EvaluatorState(str(item["expected_state"]))
        represented_keys = mapping[oracle_id]
        represented = bool(represented_keys)
        expected = state in {EvaluatorState.ACTIVE, EvaluatorState.MISSING_CONTEXT}
        matched = oracle_id in match_by_oracle
        importance = str(item["importance_class"])
        weight = weights[importance]

        if represented and expected:
            represented_expected += 1
            represented_weight += weight
            if matched:
                represented_matched += 1
                represented_weight_matched += weight
            if importance == "CRITICAL_VALIDITY":
                critical_expected += 1
                obligation = f"{snapshot_id}|{oracle_id}"
                critical_obligation_ids.append(obligation)
                if matched:
                    critical_matched += 1
                    critical_matched_ids.append(obligation)
            covered_by_horizon = any(key in horizon_keys for key in represented_keys)
            horizon_weight += weight
            if covered_by_horizon:
                horizon_weight_matched += weight
            if importance == "CRITICAL_VALIDITY":
                horizon_critical_expected += 1
                if covered_by_horizon:
                    horizon_critical_matched += 1
            if _is_newly_active(contract, item, episode_id, snapshot_id):
                newly_active_expected += 1
                if matched:
                    newly_active_matched += 1

        if expected and state is EvaluatorState.MISSING_CONTEXT:
            missing_expected += 1
            match = match_by_oracle.get(oracle_id)
            if match is not None:
                concern = concern_by_id[match.local_concern_id]
                if concern.state == "MISSING_CONTEXT" and match.state_equivalent:
                    missing_recognition += 1
                if match.missing_context_question_equivalent is True:
                    missing_question += 1

    inactive_control_matches = deterministic_inactive_control_matches(
        contract,
        snapshot_id,
        result,
    )
    noise_local_ids = set(adjudication.unsupported_local_concern_ids)
    noise_local_ids.update(adjudication.duplicate_local_concern_ids)
    noise_local_ids.update(inactive_control_matches)
    for match in adjudication.matches:
        item = item_by_id[match.oracle_id]
        state = EvaluatorState(str(item["expected_state"]))
        if state in {EvaluatorState.INACTIVE, EvaluatorState.RESOLVED}:
            noise_local_ids.add(match.local_concern_id)

    resolved_opportunities = 0
    resolved_matches = 0
    for oracle_id, item in item_by_id.items():
        if not mapping[oracle_id]:
            continue
        if _resolved_persistence_opportunity(
            contract,
            item,
            episode_id,
            snapshot_id,
        ):
            resolved_opportunities += 1
            if oracle_id in match_by_oracle:
                resolved_matches += 1

    temporal_false_ids = {
        local_id
        for local_id, stable_key in inactive_control_matches.items()
        if stable_key in {"temporal-validation", "temporal-leakage"}
    }
    if episode_id != "E2":
        temporal_false_ids.clear()

    # A matched record cannot be silently ignored from output accounting even if
    # it is also an inactive-control exact alias. Sets ensure each record is
    # counted at most once as noise, per the frozen definition.
    return ScoredObservation(
        condition=condition,
        episode_id=episode_id,
        snapshot_id=snapshot_id,
        repetition=repetition,
        represented_expected=represented_expected,
        represented_matched=represented_matched,
        represented_weight=represented_weight,
        represented_weight_matched=represented_weight_matched,
        critical_expected=critical_expected,
        critical_matched=critical_matched,
        newly_active_expected=newly_active_expected,
        newly_active_matched=newly_active_matched,
        missing_context_expected=missing_expected,
        missing_context_recognition_correct=missing_recognition,
        missing_context_question_correct=missing_question,
        noise_count=len(noise_local_ids),
        output_count=len(result.concerns),
        resolved_persistence_count=resolved_matches,
        resolved_persistence_opportunities=resolved_opportunities,
        e2_temporal_false_activation_count=len(temporal_false_ids),
        horizon_critical_expected=horizon_critical_expected,
        horizon_critical_matched=horizon_critical_matched,
        horizon_weight=horizon_weight,
        horizon_weight_matched=horizon_weight_matched,
        critical_obligation_ids=tuple(sorted(critical_obligation_ids)),
        critical_matched_ids=tuple(sorted(critical_matched_ids)),
    )


def aggregate_condition(
    scores: Sequence[ScoredObservation],
    *,
    require_complete: bool = True,
) -> ConditionMetrics:
    if not scores:
        raise ValueError("at least one scored observation is required")
    conditions = {item.condition for item in scores}
    if len(conditions) != 1:
        raise ValueError("aggregate_condition requires one condition")
    if require_complete and len(scores) != 36:
        raise ValueError(
            f"complete Specification 022 condition requires 36 observations, got {len(scores)}"
        )

    def total(field: str) -> int:
        return sum(int(getattr(item, field)) for item in scores)

    episode_metrics: dict[str, float] = {}
    for episode_id in sorted({item.episode_id for item in scores}):
        episode_scores = [item for item in scores if item.episode_id == episode_id]
        episode_metrics[episode_id] = _ratio(
            sum(item.represented_weight_matched for item in episode_scores),
            sum(item.represented_weight for item in episode_scores),
        )

    match_counts: dict[str, int] = {}
    obligation_counts: dict[str, int] = {}
    for item in scores:
        for obligation in item.critical_obligation_ids:
            obligation_counts[obligation] = obligation_counts.get(obligation, 0) + 1
        for obligation in item.critical_matched_ids:
            match_counts[obligation] = match_counts.get(obligation, 0) + 1

    catastrophic = 0
    majority = 0
    for obligation, repetitions in obligation_counts.items():
        if require_complete and repetitions != 3:
            raise ValueError(
                f"critical obligation {obligation} expected 3 repetitions, got {repetitions}"
            )
        matched = match_counts.get(obligation, 0)
        if matched == 0:
            catastrophic += 1
        if matched <= 1:
            majority += 1

    return ConditionMetrics(
        condition=next(iter(conditions)),
        observation_count=len(scores),
        represented_recall=_ratio(
            total("represented_matched"),
            total("represented_expected"),
        ),
        weighted_represented_recall=_ratio(
            total("represented_weight_matched"),
            total("represented_weight"),
        ),
        critical_recall=_ratio(
            total("critical_matched"),
            total("critical_expected"),
        ),
        newly_activated_recall=_ratio(
            total("newly_active_matched"),
            total("newly_active_expected"),
        ),
        missing_context_recognition_accuracy=_ratio(
            total("missing_context_recognition_correct"),
            total("missing_context_expected"),
        ),
        missing_context_question_correctness=_ratio(
            total("missing_context_question_correct"),
            total("missing_context_expected"),
        ),
        noise_ratio=_ratio(total("noise_count"), total("output_count")),
        resolved_persistence_ratio=_ratio(
            total("resolved_persistence_count"),
            total("resolved_persistence_opportunities"),
        ),
        mean_output_concern_count=_ratio(total("output_count"), len(scores)),
        horizon_critical_recall=_ratio(
            total("horizon_critical_matched"),
            total("horizon_critical_expected"),
        ),
        horizon_weighted_recall=_ratio(
            total("horizon_weight_matched"),
            total("horizon_weight"),
        ),
        catastrophic_critical_omissions=catastrophic,
        majority_critical_omissions=majority,
        e2_temporal_false_activation_records=total(
            "e2_temporal_false_activation_count"
        ),
        per_episode_weighted_recall=episode_metrics,
    )


def evaluate_frozen_gates(
    metrics_by_condition: Mapping[str, ConditionMetrics],
    *,
    execution_integrity: bool,
) -> GateEvaluation:
    required = {"ADS_HORIZON", "GENERIC", "ORACLE_HORIZON"}
    if set(metrics_by_condition) != required:
        raise ValueError(
            "gate evaluation requires ADS_HORIZON, GENERIC, and ORACLE_HORIZON metrics"
        )
    ads = metrics_by_condition["ADS_HORIZON"]
    generic = metrics_by_condition["GENERIC"]
    complete_matrix = all(
        item.observation_count == 36 for item in metrics_by_condition.values()
    )

    gates = {
        "MN-G01": bool(execution_integrity and complete_matrix),
        "MN-G02": (
            ads.horizon_critical_recall >= 0.90
            and ads.horizon_weighted_recall >= 0.80
        ),
        "MN-G03": ads.critical_recall >= 0.90,
        "MN-G04": ads.weighted_represented_recall >= 0.85,
        "MN-G05": (
            set(ads.per_episode_weighted_recall) == {"E1", "E2", "E3", "E4"}
            and all(value >= 0.75 for value in ads.per_episode_weighted_recall.values())
        ),
        "MN-G06": ads.newly_activated_recall >= 0.80,
        "MN-G07": (
            ads.missing_context_recognition_accuracy >= 0.85
            and ads.missing_context_question_correctness >= 0.80
        ),
        "MN-G08": ads.catastrophic_critical_omissions == 0,
        "MN-G09": ads.noise_ratio <= 0.30,
        "MN-G10": ads.resolved_persistence_ratio <= 0.15,
        "MN-G11": ads.e2_temporal_false_activation_records <= 1,
        "MN-G12": (
            ads.weighted_represented_recall
            >= generic.weighted_represented_recall - 0.03
        ),
        "MN-G13": ads.critical_recall >= generic.critical_recall - 0.03,
        "MN-G14": ads.noise_ratio <= generic.noise_ratio + 0.05,
        "MN-G15": (
            ads.mean_output_concern_count
            <= generic.mean_output_concern_count + 2.0
        ),
    }

    ads_missing_mean = (
        ads.missing_context_recognition_accuracy
        + ads.missing_context_question_correctness
    ) / 2.0
    generic_missing_mean = (
        generic.missing_context_recognition_accuracy
        + generic.missing_context_question_correctness
    ) / 2.0
    positive = {
        "MN-P01": (
            ads.weighted_represented_recall
            >= generic.weighted_represented_recall + 0.05
        ),
        "MN-P02": ads.critical_recall >= generic.critical_recall + 0.05,
        "MN-P03": (
            ads.majority_critical_omissions + ads.catastrophic_critical_omissions
            <= generic.majority_critical_omissions
            + generic.catastrophic_critical_omissions
            - 2
        ),
        "MN-P04": (
            ads.newly_activated_recall >= generic.newly_activated_recall + 0.10
        ),
        "MN-P05": ads_missing_mean >= generic_missing_mean + 0.10,
    }

    if not gates["MN-G01"]:
        outcome = AdvancementOutcome.INCOMPLETE
    elif not all(gates[f"MN-G{index:02d}"] for index in range(2, 16)):
        outcome = AdvancementOutcome.FAIL
    elif any(positive.values()):
        outcome = AdvancementOutcome.PROMOTE
    else:
        outcome = AdvancementOutcome.SAFE
    return GateEvaluation(gates=gates, positive_signals=positive, outcome=outcome)
