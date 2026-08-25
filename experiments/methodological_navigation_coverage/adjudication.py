"""Stage-separated blinded semantic adjudication for Specification 022.

Specification 022 freezes a two-stage evaluator:

1. deterministic normalized exact/alias prematching;
2. one blinded semantic-judge call for the remaining unmatched concern/oracle
   candidates, while still asking the judge to assess state/question equivalence
   for the fixed Stage-1 pairs.

This module makes that separation explicit. It also exposes explicit inactive
controls to the judge through opaque evaluator-local control IDs rather than
methodological stable keys. The stable-key mapping remains system-owned and is
used only after the provider response has been preserved.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
import hashlib
from typing import Any, Mapping, Sequence

from ads_system.application.reasoning import ReasoningRequest

from experiments.methodological_navigation_coverage.contract import (
    FrozenContract,
    JUDGE_MODEL,
    MethodologicalConcern,
    MethodologicalCoverageResult,
    Prematch,
    SemanticAdjudicationResult,
    SemanticMatch,
    canonical_project_state,
    methodology_payload_sha256,
    validate_result_grounding,
    validate_semantic_adjudication,
)


STAGE2_JUDGE_INSTRUCTION = (
    "Act only as a blinded semantic adjudicator for methodological-coverage "
    "scoring. Stage-1 exact/alias pairs supplied under fixed_prematches are "
    "already matched and MUST NOT be remapped; assess only their state and, "
    "where applicable, missing-context-question equivalence. Perform semantic "
    "matching only between unmatched_reasoner_concerns and "
    "unmatched_oracle_concerns. Separately identify reasoner concerns that "
    "semantically activate any supplied explicit inactive control. Mark "
    "unsupported output records and additional semantic duplicates. Do not "
    "score prose style, infer a treatment condition, or invent project facts."
)


@dataclass(frozen=True, slots=True)
class InactiveControlJudgment:
    """Judge-side match to one opaque explicit inactive-control identity."""

    local_concern_id: str
    control_id: str


@dataclass(frozen=True, slots=True)
class BlindedCoverageJudgeResult:
    """Structured Stage-2 output with Stage-1 and semantic matches separated."""

    fixed_prematch_assessments: tuple[SemanticMatch, ...]
    semantic_matches: tuple[SemanticMatch, ...]
    inactive_control_matches: tuple[InactiveControlJudgment, ...]
    unsupported_local_concern_ids: tuple[str, ...]
    duplicate_local_concern_ids: tuple[str, ...]

    def to_payload(self) -> dict[str, object]:
        return {
            "fixed_prematch_assessments": [
                asdict(item) for item in self.fixed_prematch_assessments
            ],
            "semantic_matches": [asdict(item) for item in self.semantic_matches],
            "inactive_control_matches": [
                asdict(item) for item in self.inactive_control_matches
            ],
            "unsupported_local_concern_ids": list(
                self.unsupported_local_concern_ids
            ),
            "duplicate_local_concern_ids": list(self.duplicate_local_concern_ids),
        }


@dataclass(frozen=True, slots=True)
class FinalizedAdjudication:
    """System-owned combination of deterministic and blinded judge evidence."""

    adjudication: SemanticAdjudicationResult
    inactive_control_matches: Mapping[str, str]


def _oracle_projection(
    item: Mapping[str, Any],
    snapshot_id: str,
) -> dict[str, object]:
    return {
        "oracle_id": str(item["oracle_id"]),
        "canonical_concern": str(item["canonical_concern"]),
        "acceptable_aliases": list(item["acceptable_aliases"]),
        "expected_state": str(item["expected_state"]),
        "missing_context_question_semantics": item.get(
            "missing_context_question_semantics"
        ),
        "grounding_project_object_ids": list(
            item.get("grounding_project_object_ids_by_snapshot", {}).get(
                snapshot_id, []
            )
        ),
    }


def _control_id(snapshot_id: str, stable_key: str) -> str:
    digest = hashlib.sha256(
        f"spec022-inactive-control|{snapshot_id}|{stable_key}".encode("utf-8")
    ).hexdigest()
    return f"ctl-{digest[:18]}"


def inactive_control_projection(
    contract: FrozenContract,
    snapshot_id: str,
) -> tuple[tuple[dict[str, object], ...], Mapping[str, str]]:
    """Return blinded control descriptions plus a system-owned identity map."""

    stable_keys = tuple(
        sorted(
            map(
                str,
                contract.oracle["inactive_controls_by_snapshot"].get(
                    snapshot_id, []
                ),
            )
        )
    )
    asset_by_key = {
        str(item["stable_key"]): item for item in contract.universe["assets"]
    }
    projection: list[dict[str, object]] = []
    control_map: dict[str, str] = {}
    for stable_key in stable_keys:
        asset = asset_by_key[stable_key]
        control_id = _control_id(snapshot_id, stable_key)
        profile = asset.get("retrieval_profile") or {}
        aliases: list[str] = []
        lexical_terms: list[str] = []
        semantic_cues: list[str] = []
        if isinstance(profile, Mapping):
            aliases = list(map(str, profile.get("aliases", [])))
            lexical_terms = list(map(str, profile.get("lexical_terms", [])))
            semantic_cues = list(map(str, profile.get("semantic_cues", [])))
        projection.append(
            {
                "control_id": control_id,
                "title": str(asset["title"]),
                "purpose": str(asset["purpose"]),
                "aliases": aliases,
                "lexical_terms": lexical_terms,
                "semantic_cues": semantic_cues,
            }
        )
        control_map[control_id] = stable_key
    return tuple(projection), control_map


def build_stage2_judge_request(
    *,
    contract: FrozenContract,
    entry,
    snapshot: Mapping[str, Any],
    result: MethodologicalCoverageResult,
    oracle_items: Sequence[Mapping[str, Any]],
    prematches: Sequence[Prematch],
) -> tuple[ReasoningRequest, Mapping[str, str]]:
    """Build the condition-blind Stage-2 request from disjoint candidate pools."""

    validate_result_grounding(result, snapshot)
    concern_by_id = {
        item.local_concern_id: item for item in result.concerns
    }
    oracle_by_id = {
        str(item["oracle_id"]): item for item in oracle_items
    }
    prematched_local_ids = {item.local_concern_id for item in prematches}
    prematched_oracle_ids = {item.oracle_id for item in prematches}
    if len(prematched_local_ids) != len(tuple(prematches)):
        raise ValueError("prematches contain duplicate local concern IDs")
    if len(prematched_oracle_ids) != len(tuple(prematches)):
        raise ValueError("prematches contain duplicate oracle IDs")

    fixed_pairs: list[dict[str, object]] = []
    for prematch in prematches:
        concern = concern_by_id.get(prematch.local_concern_id)
        oracle = oracle_by_id.get(prematch.oracle_id)
        if concern is None or oracle is None:
            raise ValueError("prematch references an unknown concern or oracle item")
        fixed_pairs.append(
            {
                "reasoner_concern": concern.to_payload(),
                "oracle_concern": _oracle_projection(
                    oracle, str(snapshot["snapshot_id"])
                ),
            }
        )

    unmatched_concerns = [
        item.to_payload()
        for item in result.concerns
        if item.local_concern_id not in prematched_local_ids
    ]
    unmatched_oracles = [
        _oracle_projection(item, str(snapshot["snapshot_id"]))
        for item in oracle_items
        if str(item["oracle_id"]) not in prematched_oracle_ids
    ]
    controls, control_map = inactive_control_projection(
        contract, str(snapshot["snapshot_id"])
    )

    anonymous_digest = hashlib.sha256(
        f"spec022-stage2-judge|{entry.observation_id}".encode("utf-8")
    ).hexdigest()
    evidence = {
        "anonymized_observation_id": f"obs-{anonymous_digest[44:64]}",
        "project_state": canonical_project_state(entry.episode_id, snapshot),
        "fixed_prematches": fixed_pairs,
        "unmatched_reasoner_concerns": unmatched_concerns,
        "unmatched_oracle_concerns": unmatched_oracles,
        "explicit_inactive_controls": list(controls),
    }
    request = ReasoningRequest(
        run_id=f"judge-{anonymous_digest[:20]}",
        run_nonce=f"judge-nonce-{anonymous_digest[20:44]}",
        system_instruction=STAGE2_JUDGE_INSTRUCTION,
        user_task=(
            "Assess fixed Stage-1 pair state/question equivalence, semantically "
            "match only the remaining unmatched candidates, identify explicit "
            "inactive-control activations, and mark unsupported or duplicate "
            "reasoner concerns."
        ),
        project_evidence=evidence,
        methodological_context_payload={},
        methodological_context_sha256=methodology_payload_sha256({}),
        knowledge_revisions=(),
        model_configuration=JUDGE_MODEL,
        structured_output_type=BlindedCoverageJudgeResult,
    )
    visible = request.canonical_model_input()
    for forbidden in (
        "ADS_HORIZON",
        "GENERIC",
        "ORACLE_HORIZON",
        "stable_key",
        "stable_keys",
        "representation_map",
        "retrieval_query",
        "rrf_score",
    ):
        if forbidden in visible:
            raise ValueError(
                f"blinded Stage-2 judge input leaked forbidden token: {forbidden}"
            )
    return request, control_map


def finalize_stage2_adjudication(
    *,
    judge_result: BlindedCoverageJudgeResult,
    reasoner_result: MethodologicalCoverageResult,
    oracle_items: Sequence[Mapping[str, Any]],
    prematches: Sequence[Prematch],
    control_map: Mapping[str, str],
) -> FinalizedAdjudication:
    """Validate and combine fixed Stage-1 and semantic Stage-2 evidence."""

    valid_local_ids = {
        item.local_concern_id for item in reasoner_result.concerns
    }
    valid_oracle_ids = {
        str(item["oracle_id"]) for item in oracle_items
    }
    expected_fixed = {
        (item.local_concern_id, item.oracle_id) for item in prematches
    }
    observed_fixed = {
        (item.local_concern_id, item.oracle_id)
        for item in judge_result.fixed_prematch_assessments
    }
    if observed_fixed != expected_fixed:
        raise ValueError(
            "judge fixed-prematch assessments must preserve every exact Stage-1 pair"
        )
    if len(judge_result.fixed_prematch_assessments) != len(expected_fixed):
        raise ValueError("judge returned duplicate fixed-prematch assessments")

    prematched_local_ids = {item[0] for item in expected_fixed}
    prematched_oracle_ids = {item[1] for item in expected_fixed}
    semantic_local_ids: list[str] = []
    semantic_oracle_ids: list[str] = []
    for match in judge_result.semantic_matches:
        if match.local_concern_id not in valid_local_ids:
            raise ValueError("semantic judge matched an unknown local concern")
        if match.oracle_id not in valid_oracle_ids:
            raise ValueError("semantic judge matched an unknown oracle item")
        if match.local_concern_id in prematched_local_ids:
            raise ValueError("semantic judge rematched a fixed Stage-1 local concern")
        if match.oracle_id in prematched_oracle_ids:
            raise ValueError("semantic judge rematched a fixed Stage-1 oracle item")
        semantic_local_ids.append(match.local_concern_id)
        semantic_oracle_ids.append(match.oracle_id)
    if len(semantic_local_ids) != len(set(semantic_local_ids)):
        raise ValueError("semantic judge matched one local concern more than once")
    if len(semantic_oracle_ids) != len(set(semantic_oracle_ids)):
        raise ValueError("semantic judge matched one oracle item more than once")

    matched_local_ids = prematched_local_ids | set(semantic_local_ids)
    unsupported = set(judge_result.unsupported_local_concern_ids)
    duplicates = set(judge_result.duplicate_local_concern_ids)
    if not unsupported.issubset(valid_local_ids) or not duplicates.issubset(
        valid_local_ids
    ):
        raise ValueError("judge unsupported/duplicate IDs must reference supplied concerns")
    if unsupported & duplicates:
        raise ValueError("one concern cannot be both unsupported and duplicate")
    if (unsupported | duplicates) & matched_local_ids:
        raise ValueError("matched concerns cannot also be unsupported or duplicate")

    inactive_matches: dict[str, str] = {}
    for item in judge_result.inactive_control_matches:
        if item.local_concern_id not in valid_local_ids:
            raise ValueError("inactive-control match references unknown local concern")
        stable_key = control_map.get(item.control_id)
        if stable_key is None:
            raise ValueError("inactive-control match references unknown opaque control")
        existing = inactive_matches.get(item.local_concern_id)
        if existing is not None and existing != stable_key:
            raise ValueError("one concern matched multiple inactive controls")
        inactive_matches[item.local_concern_id] = stable_key

    adjudication = SemanticAdjudicationResult(
        matches=tuple(
            [*judge_result.fixed_prematch_assessments, *judge_result.semantic_matches]
        ),
        unsupported_local_concern_ids=judge_result.unsupported_local_concern_ids,
        duplicate_local_concern_ids=judge_result.duplicate_local_concern_ids,
    )
    validate_semantic_adjudication(
        adjudication,
        reasoner_result,
        oracle_items,
    )
    return FinalizedAdjudication(
        adjudication=adjudication,
        inactive_control_matches=inactive_matches,
    )
