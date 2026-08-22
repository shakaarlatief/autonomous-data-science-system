"""Deterministic applicability assessment and first MethodologicalHorizon builder.

The application layer intentionally operates on storage-neutral accepted-current
knowledge projections. Retrieval technology, SQL persistence details, embedding
models, and fusion algorithms remain below this boundary.
"""

from __future__ import annotations

from collections.abc import Callable, Mapping, Sequence
from typing import Any, Literal

from ads_system.application.horizon_models import (
    ApplicabilityAssessment,
    HorizonCandidate,
    HorizonSeed,
    MethodologicalHorizon,
    NavigableKnowledgeAsset,
)
from ads_system.application.ports import UnitOfWork

ConditionTruth = Literal["TRUE", "FALSE", "UNKNOWN"]
UnitOfWorkFactory = Callable[[], UnitOfWork]


class ApplicabilityEvaluationError(ValueError):
    """Raised when a knowledge applicability expression exceeds the frozen evaluator."""


class StaleKnowledgeCandidateError(ValueError):
    """Raised when a Horizon seed is no longer the current accepted revision."""


def assess_applicability(
    asset: NavigableKnowledgeAsset,
    known_context: Mapping[str, object],
) -> ApplicabilityAssessment:
    """Assess one accepted-current asset without collapsing unknown into false.

    The first evaluator supports only the structural boolean-expression subset
    frozen in Specification 012. Predicate names map exactly to context keys.
    Richer predicate semantics require an explicit later evaluator extension.
    """

    truth, unknown_predicates = _evaluate_expression(asset.applicability, known_context)

    if truth == "FALSE":
        return ApplicabilityAssessment(
            state="INAPPLICABLE",
            missing_context_keys=(),
            unknown_predicate_keys=(),
        )

    required_context_keys = {
        requirement.key
        for requirement in asset.context_requirements
        if {"APPLICABILITY", "RULE_EVALUATION"}.intersection(
            requirement.required_for
        )
    }
    missing_requirements = {
        key for key in required_context_keys if key not in known_context
    }
    missing = tuple(sorted(set(unknown_predicates).union(missing_requirements)))

    if truth == "UNKNOWN" or missing:
        return ApplicabilityAssessment(
            state="MISSING_CONTEXT",
            missing_context_keys=missing,
            unknown_predicate_keys=tuple(sorted(unknown_predicates)),
        )

    return ApplicabilityAssessment(
        state="POSSIBLY_APPLICABLE",
        missing_context_keys=(),
        unknown_predicate_keys=(),
    )


def build_methodological_horizon(
    seeds: Sequence[HorizonSeed],
    *,
    known_context: Mapping[str, object],
    uow_factory: UnitOfWorkFactory,
) -> MethodologicalHorizon:
    """Build the first one-hop, applicability-aware MethodologicalHorizon.

    Direct candidates are verified against accepted-current knowledge. Only
    outbound one-hop relations from direct seeds are expanded. Relation-added
    candidates are never recursively expanded in this implementation.
    """

    direct_assets: dict[str, NavigableKnowledgeAsset] = {}
    relation_assets: dict[
        str,
        tuple[NavigableKnowledgeAsset, str, str],
    ] = {}

    with uow_factory() as uow:
        for seed in seeds:
            current = uow.navigation.get_current_asset(seed.stable_key)
            if current is None:
                raise StaleKnowledgeCandidateError(
                    f"Horizon seed {seed.stable_key!r} has no current accepted revision"
                )
            if current.revision_id != seed.revision_id:
                raise StaleKnowledgeCandidateError(
                    f"Horizon seed {seed.stable_key!r} references revision "
                    f"{seed.revision_id!r}, current accepted is {current.revision_id!r}"
                )
            if current.title != seed.title:
                raise StaleKnowledgeCandidateError(
                    f"Horizon seed {seed.stable_key!r} title does not match current revision"
                )

            existing = direct_assets.get(seed.stable_key)
            if existing is not None and existing.revision_id != current.revision_id:
                raise StaleKnowledgeCandidateError(
                    f"Conflicting direct Horizon seeds for {seed.stable_key!r}"
                )
            direct_assets[seed.stable_key] = current

        # Expansion is deliberately restricted to the direct seed set. Newly
        # related assets are not visited recursively.
        for stable_key in sorted(direct_assets):
            for related in uow.navigation.get_outbound_related_assets(stable_key):
                if related.stable_key in direct_assets:
                    continue
                if related.stable_key in relation_assets:
                    continue

                target = uow.navigation.get_current_asset(related.stable_key)
                if target is None or target.revision_id != related.revision_id:
                    raise StaleKnowledgeCandidateError(
                        f"Related asset {related.stable_key!r} is not current accepted"
                    )
                relation_assets[related.stable_key] = (
                    target,
                    related.relation_type,
                    related.relation_revision_id,
                )

    candidates: list[HorizonCandidate] = []
    for stable_key in sorted(direct_assets):
        asset = direct_assets[stable_key]
        assessment = assess_applicability(asset, known_context)
        candidates.append(
            HorizonCandidate(
                stable_key=asset.stable_key,
                revision_id=asset.revision_id,
                title=asset.title,
                origin="DIRECT",
                relation_type=None,
                relation_revision_id=None,
                applicability_state=assessment.state,
                missing_context_keys=assessment.missing_context_keys,
            )
        )

    for stable_key in sorted(relation_assets):
        asset, relation_type, relation_revision_id = relation_assets[stable_key]
        assessment = assess_applicability(asset, known_context)
        candidates.append(
            HorizonCandidate(
                stable_key=asset.stable_key,
                revision_id=asset.revision_id,
                title=asset.title,
                origin="RELATION",
                relation_type=relation_type,
                relation_revision_id=relation_revision_id,
                applicability_state=assessment.state,
                missing_context_keys=assessment.missing_context_keys,
            )
        )

    included = tuple(
        candidate
        for candidate in candidates
        if candidate.applicability_state != "INAPPLICABLE"
    )
    excluded = tuple(
        candidate
        for candidate in candidates
        if candidate.applicability_state == "INAPPLICABLE"
    )
    return MethodologicalHorizon(included=included, excluded=excluded)


def _evaluate_expression(
    expression: Mapping[str, Any] | None,
    known_context: Mapping[str, object],
) -> tuple[ConditionTruth, set[str]]:
    if expression is None:
        return "TRUE", set()
    if not isinstance(expression, Mapping):
        raise ApplicabilityEvaluationError(
            "Applicability expression must be an object or null"
        )

    if "predicate" in expression:
        unexpected = set(expression).difference({"predicate", "arguments"})
        if unexpected:
            raise ApplicabilityEvaluationError(
                f"Unsupported predicate expression fields: {sorted(unexpected)!r}"
            )
        predicate = expression.get("predicate")
        arguments = expression.get("arguments", {})
        if not isinstance(predicate, str) or not predicate:
            raise ApplicabilityEvaluationError("Predicate name must be a non-empty string")
        if not isinstance(arguments, Mapping):
            raise ApplicabilityEvaluationError("Predicate arguments must be an object")
        if arguments:
            raise ApplicabilityEvaluationError(
                f"Predicate arguments are not supported in v0.1: {predicate!r}"
            )
        if predicate not in known_context:
            return "UNKNOWN", {predicate}
        value = known_context[predicate]
        if value is True:
            return "TRUE", set()
        if value is False:
            return "FALSE", set()
        raise ApplicabilityEvaluationError(
            f"Predicate {predicate!r} requires an explicit boolean context value"
        )

    if "all" in expression:
        if set(expression) != {"all"}:
            raise ApplicabilityEvaluationError("'all' expression has unsupported fields")
        children = expression["all"]
        if not isinstance(children, list) or not children:
            raise ApplicabilityEvaluationError("'all' requires a non-empty expression list")
        results = [_evaluate_expression(child, known_context) for child in children]
        unknown = set().union(*(keys for _, keys in results))
        if any(truth == "FALSE" for truth, _ in results):
            return "FALSE", unknown
        if any(truth == "UNKNOWN" for truth, _ in results):
            return "UNKNOWN", unknown
        return "TRUE", unknown

    if "any" in expression:
        if set(expression) != {"any"}:
            raise ApplicabilityEvaluationError("'any' expression has unsupported fields")
        children = expression["any"]
        if not isinstance(children, list) or not children:
            raise ApplicabilityEvaluationError("'any' requires a non-empty expression list")
        results = [_evaluate_expression(child, known_context) for child in children]
        unknown = set().union(*(keys for _, keys in results))
        if any(truth == "TRUE" for truth, _ in results):
            return "TRUE", unknown
        if any(truth == "UNKNOWN" for truth, _ in results):
            return "UNKNOWN", unknown
        return "FALSE", unknown

    if "not" in expression:
        if set(expression) != {"not"}:
            raise ApplicabilityEvaluationError("'not' expression has unsupported fields")
        truth, unknown = _evaluate_expression(expression["not"], known_context)
        if truth == "TRUE":
            return "FALSE", unknown
        if truth == "FALSE":
            return "TRUE", unknown
        return "UNKNOWN", unknown

    raise ApplicabilityEvaluationError(
        f"Unsupported applicability expression shape: {sorted(expression)!r}"
    )
