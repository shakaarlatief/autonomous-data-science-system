"""Non-gating attribution diagnostics for Specification 022.

These helpers are intentionally downstream of raw evidence preservation. They
separate catalog gaps, navigation gaps, reasoning-use gaps, semantic inactive
controls, and surface latency without changing any frozen advancement gate.
"""

from __future__ import annotations

from dataclasses import dataclass, replace
from typing import Mapping, Sequence

from ads_system.application.horizon_models import HorizonCandidate

from experiments.methodological_navigation_coverage.adjudication import (
    FinalizedAdjudication,
)
from experiments.methodological_navigation_coverage.contract import (
    EvaluatorState,
    FrozenContract,
    MethodologicalCoverageResult,
    oracle_items_for_snapshot,
)
from experiments.methodological_navigation_coverage.scoring import (
    ScoredObservation,
    deterministic_inactive_control_matches,
    score_observation,
)


@dataclass(frozen=True, slots=True)
class ObservationAttribution:
    condition: str
    episode_id: str
    snapshot_id: str
    repetition: int
    matched_oracle_ids: tuple[str, ...]
    catalog_gap_expected_ids: tuple[str, ...]
    catalog_gap_recovered_ids: tuple[str, ...]
    navigation_gap_ids: tuple[str, ...]
    reasoning_use_gap_ids: tuple[str, ...]
    inactive_control_matches: Mapping[str, str]


def _representation_map(contract: FrozenContract) -> dict[str, tuple[str, ...]]:
    return {
        str(item["oracle_id"]): tuple(map(str, item["stable_keys"]))
        for item in contract.representation_map["mappings"]
    }


def score_with_semantic_inactive_controls(
    *,
    contract: FrozenContract,
    condition: str,
    episode_id: str,
    snapshot_id: str,
    repetition: int,
    result: MethodologicalCoverageResult,
    finalized: FinalizedAdjudication,
    horizon: Sequence[HorizonCandidate] = (),
) -> ScoredObservation:
    """Apply frozen scoring while adding semantically judged inactive controls."""

    base = score_observation(
        contract=contract,
        condition=condition,
        episode_id=episode_id,
        snapshot_id=snapshot_id,
        repetition=repetition,
        result=result,
        adjudication=finalized.adjudication,
        horizon=horizon,
    )
    oracle_items = oracle_items_for_snapshot(contract, episode_id, snapshot_id)
    item_by_id = {str(item["oracle_id"]): item for item in oracle_items}
    noise_ids = set(finalized.adjudication.unsupported_local_concern_ids)
    noise_ids.update(finalized.adjudication.duplicate_local_concern_ids)

    deterministic_controls = deterministic_inactive_control_matches(
        contract, snapshot_id, result
    )
    all_controls = dict(deterministic_controls)
    all_controls.update(finalized.inactive_control_matches)
    noise_ids.update(all_controls)

    for match in finalized.adjudication.matches:
        item = item_by_id[match.oracle_id]
        state = EvaluatorState(str(item["expected_state"]))
        if state in {EvaluatorState.INACTIVE, EvaluatorState.RESOLVED}:
            noise_ids.add(match.local_concern_id)

    temporal_false_ids = {
        local_id
        for local_id, stable_key in all_controls.items()
        if stable_key in {"temporal-validation", "temporal-leakage"}
    }
    if episode_id != "E2":
        temporal_false_ids.clear()

    return replace(
        base,
        noise_count=len(noise_ids),
        e2_temporal_false_activation_count=len(temporal_false_ids),
    )


def build_observation_attribution(
    *,
    contract: FrozenContract,
    condition: str,
    episode_id: str,
    snapshot_id: str,
    repetition: int,
    finalized: FinalizedAdjudication,
    horizon: Sequence[HorizonCandidate] = (),
) -> ObservationAttribution:
    mapping = _representation_map(contract)
    matched = {item.oracle_id for item in finalized.adjudication.matches}
    horizon_keys = {item.stable_key for item in horizon}
    catalog_expected: list[str] = []
    catalog_recovered: list[str] = []
    navigation_gaps: list[str] = []
    reasoning_use_gaps: list[str] = []

    for item in oracle_items_for_snapshot(contract, episode_id, snapshot_id):
        oracle_id = str(item["oracle_id"])
        state = EvaluatorState(str(item["expected_state"]))
        expected = state in {EvaluatorState.ACTIVE, EvaluatorState.MISSING_CONTEXT}
        if not expected:
            continue
        represented_keys = mapping[oracle_id]
        if not represented_keys:
            catalog_expected.append(oracle_id)
            if oracle_id in matched:
                catalog_recovered.append(oracle_id)
            continue
        if condition != "ADS_HORIZON":
            continue
        covered = any(key in horizon_keys for key in represented_keys)
        if not covered:
            navigation_gaps.append(oracle_id)
        elif oracle_id not in matched:
            reasoning_use_gaps.append(oracle_id)

    return ObservationAttribution(
        condition=condition,
        episode_id=episode_id,
        snapshot_id=snapshot_id,
        repetition=repetition,
        matched_oracle_ids=tuple(sorted(matched)),
        catalog_gap_expected_ids=tuple(sorted(catalog_expected)),
        catalog_gap_recovered_ids=tuple(sorted(catalog_recovered)),
        navigation_gap_ids=tuple(sorted(navigation_gaps)),
        reasoning_use_gap_ids=tuple(sorted(reasoning_use_gaps)),
        inactive_control_matches=dict(finalized.inactive_control_matches),
    )


def _snapshot_order(contract: FrozenContract, episode_id: str) -> tuple[str, ...]:
    episode = next(
        item
        for item in contract.episodes["episodes"]
        if str(item["episode_id"]) == episode_id
    )
    return tuple(str(item["snapshot_id"]) for item in episode["snapshots"])


def _expected_state(
    contract: FrozenContract,
    item: Mapping[str, object],
    snapshot_id: str,
) -> EvaluatorState:
    state_by_snapshot = item.get("state_by_snapshot", {})
    if not isinstance(state_by_snapshot, Mapping):
        raise ValueError("oracle state_by_snapshot must be a mapping")
    return EvaluatorState(
        str(
            state_by_snapshot.get(
                snapshot_id,
                contract.oracle["default_unspecified_state"],
            )
        )
    )


def build_diagnostic_summary(
    contract: FrozenContract,
    attributions: Sequence[ObservationAttribution],
) -> dict[str, object]:
    """Aggregate frozen descriptive diagnostics without affecting advancement."""

    by_condition: dict[str, dict[str, object]] = {}
    for condition in sorted({item.condition for item in attributions}):
        subset = [item for item in attributions if item.condition == condition]
        catalog_expected = sum(len(item.catalog_gap_expected_ids) for item in subset)
        catalog_recovered = sum(len(item.catalog_gap_recovered_ids) for item in subset)
        by_condition[condition] = {
            "catalog_gap_expected": catalog_expected,
            "catalog_gap_recovered": catalog_recovered,
            "catalog_gap_recovery_rate": (
                1.0 if catalog_expected == 0 else catalog_recovered / catalog_expected
            ),
            "navigation_gap_count": sum(
                len(item.navigation_gap_ids) for item in subset
            ),
            "reasoning_use_gap_count": sum(
                len(item.reasoning_use_gap_ids) for item in subset
            ),
            "semantic_inactive_control_match_count": sum(
                len(item.inactive_control_matches) for item in subset
            ),
        }

    oracle_by_episode: dict[str, list[Mapping[str, object]]] = {}
    for raw in contract.oracle["items"]:
        oracle_by_episode.setdefault(str(raw["episode_id"]), []).append(raw)

    latency_records: list[dict[str, object]] = []
    for condition in sorted({item.condition for item in attributions}):
        for episode_id in sorted(oracle_by_episode):
            order = _snapshot_order(contract, episode_id)
            for oracle_item in oracle_by_episode[episode_id]:
                active_indices = [
                    index
                    for index, snapshot_id in enumerate(order)
                    if _expected_state(contract, oracle_item, snapshot_id)
                    in {EvaluatorState.ACTIVE, EvaluatorState.MISSING_CONTEXT}
                ]
                if not active_indices:
                    continue
                first_active_index = min(active_indices)
                first_active_snapshot = order[first_active_index]
                oracle_id = str(oracle_item["oracle_id"])
                for repetition in (1, 2, 3):
                    matched_indices = [
                        index
                        for index, snapshot_id in enumerate(order)
                        for attribution in attributions
                        if attribution.condition == condition
                        and attribution.episode_id == episode_id
                        and attribution.snapshot_id == snapshot_id
                        and attribution.repetition == repetition
                        and oracle_id in attribution.matched_oracle_ids
                    ]
                    premature = any(index < first_active_index for index in matched_indices)
                    eligible = [
                        index for index in matched_indices if index >= first_active_index
                    ]
                    first_surfaced_index = min(eligible) if eligible else None
                    latency_records.append(
                        {
                            "condition": condition,
                            "episode_id": episode_id,
                            "oracle_id": oracle_id,
                            "repetition": repetition,
                            "first_active_snapshot": first_active_snapshot,
                            "first_surfaced_snapshot": (
                                None
                                if first_surfaced_index is None
                                else order[first_surfaced_index]
                            ),
                            "surface_latency": (
                                None
                                if first_surfaced_index is None
                                else first_surfaced_index - first_active_index
                            ),
                            "prematurely_surfaced": premature,
                            "never_surfaced_after_activation": first_surfaced_index is None,
                        }
                    )

    return {
        "by_condition": by_condition,
        "surface_latency_records": latency_records,
    }
