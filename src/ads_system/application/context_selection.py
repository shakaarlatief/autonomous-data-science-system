"""Task-specific relevance filtering and selective methodological context assembly.

This module implements Specification 013's minimum-complexity RH-C candidate:
explicit task reasoning functions select primary Horizon candidates, bounded
``REQUIRES_CONCEPT`` support keeps required conceptual context, and only the
surviving exact revisions are materialized into the model-facing context pack.

The selection report intentionally remains richer than the serialized pack.
Omission reasons belong to system observability and do not need to consume LLM
context on every reasoning call.
"""

from __future__ import annotations

import hashlib
import json
from collections.abc import Callable, Sequence
from typing import Any

from ads_system.application.context_models import (
    ContextKnowledgeAsset,
    ContextSelectionDecision,
    ContextSelectionResult,
    MethodologicalContextPack,
    MethodologicalContextRequest,
    SelectedContextKnowledge,
    SerializedMethodologicalContextPack,
)
from ads_system.application.horizon_models import HorizonCandidate, MethodologicalHorizon
from ads_system.application.ports import UnitOfWork

UnitOfWorkFactory = Callable[[], UnitOfWork]

PRIMARY_FUNCTION_MATCH = "PRIMARY_FUNCTION_MATCH"
REQUIRED_CONCEPT_SUPPORT = "REQUIRED_CONCEPT_SUPPORT"
NO_REASONING_FUNCTION_MATCH = "NO_REASONING_FUNCTION_MATCH"
BUDGET_LIMIT = "BUDGET_LIMIT"
INAPPLICABLE = "INAPPLICABLE"


class ContextSelectionError(ValueError):
    """Raised when a context request or Horizon cannot satisfy the frozen contract."""


class StaleContextKnowledgeError(ContextSelectionError):
    """Raised when selected Horizon identity no longer resolves exactly current."""


def select_methodological_context(
    horizon: MethodologicalHorizon,
    request: MethodologicalContextRequest,
    *,
    uow_factory: UnitOfWorkFactory,
) -> ContextSelectionResult:
    """Select and materialize a bounded task-specific methodological context.

    Selection itself uses only lightweight metadata already present on the
    Horizon candidate. Full reasoning content is fetched only after the hard
    budget has been applied, so omitted candidates do not require full content
    materialization in the production path.
    """

    requested_functions = _validate_request(request)
    requested_set = set(requested_functions)

    primary = tuple(
        sorted(
            (
                candidate
                for candidate in horizon.included
                if requested_set.intersection(candidate.reasoning_functions)
            ),
            key=_candidate_order,
        )
    )
    primary_keys = {candidate.stable_key for candidate in primary}

    support = tuple(
        sorted(
            (
                candidate
                for candidate in horizon.included
                if candidate.stable_key not in primary_keys
                and candidate.origin == "RELATION"
                and candidate.relation_type == "REQUIRES_CONCEPT"
                and candidate.relation_source_key in primary_keys
            ),
            key=_candidate_order,
        )
    )

    relevant: tuple[tuple[HorizonCandidate, str], ...] = tuple(
        (candidate, PRIMARY_FUNCTION_MATCH) for candidate in primary
    ) + tuple((candidate, REQUIRED_CONCEPT_SUPPORT) for candidate in support)

    selected_plan = relevant[: request.max_assets]
    budget_omitted = {
        candidate.stable_key for candidate, _ in relevant[request.max_assets :]
    }
    relevant_keys = {candidate.stable_key for candidate, _ in relevant}
    selected_reason_by_key = {
        candidate.stable_key: reason for candidate, reason in selected_plan
    }

    selected_items = _materialize_selected(
        selected_plan,
        uow_factory=uow_factory,
    )
    aggregate_missing = tuple(
        sorted(
            {
                key
                for item in selected_items
                for key in item.missing_context_keys
            }
        )
    )

    pack = MethodologicalContextPack(
        schema_version=1,
        task_id=request.task_id,
        requested_reasoning_functions=requested_functions,
        knowledge=selected_items,
        missing_context_keys=aggregate_missing,
    )

    decisions: list[ContextSelectionDecision] = []
    for candidate in sorted(horizon.included, key=_candidate_order):
        if candidate.stable_key in selected_reason_by_key:
            selected = True
            reason = selected_reason_by_key[candidate.stable_key]
        elif candidate.stable_key in budget_omitted:
            selected = False
            reason = BUDGET_LIMIT
        elif candidate.stable_key in relevant_keys:
            # Defensive branch: all relevant candidates must be selected or
            # budget-omitted under the frozen single hard budget.
            raise ContextSelectionError(
                f"Relevant candidate {candidate.stable_key!r} has no selection decision"
            )
        else:
            selected = False
            reason = NO_REASONING_FUNCTION_MATCH

        decisions.append(
            ContextSelectionDecision(
                stable_key=candidate.stable_key,
                revision_id=candidate.revision_id,
                selected=selected,
                reason=reason,
                origin=candidate.origin,
                applicability_state=candidate.applicability_state,
                missing_context_keys=candidate.missing_context_keys,
            )
        )

    for candidate in sorted(horizon.excluded, key=_candidate_order):
        decisions.append(
            ContextSelectionDecision(
                stable_key=candidate.stable_key,
                revision_id=candidate.revision_id,
                selected=False,
                reason=INAPPLICABLE,
                origin=candidate.origin,
                applicability_state=candidate.applicability_state,
                missing_context_keys=candidate.missing_context_keys,
            )
        )

    return ContextSelectionResult(
        request=request,
        pack=pack,
        decisions=tuple(decisions),
    )


def serialize_methodological_context_pack(
    pack: MethodologicalContextPack,
) -> SerializedMethodologicalContextPack:
    """Return canonical compact JSON plus deterministic size/hash diagnostics."""

    payload = methodological_context_pack_payload(pack)
    text = json.dumps(
        payload,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    )
    encoded = text.encode("utf-8")
    return SerializedMethodologicalContextPack(
        text=text,
        utf8_bytes=len(encoded),
        character_count=len(text),
        sha256=hashlib.sha256(encoded).hexdigest(),
    )


def methodological_context_pack_payload(
    pack: MethodologicalContextPack,
) -> dict[str, Any]:
    """Project a context pack to the exact model-facing JSON schema.

    Omission decisions, retrieval cues/scores, governance events, source locators,
    timestamps, and storage metadata are absent because they are not fields of
    this projection.
    """

    return {
        "knowledge": [_selected_item_payload(item) for item in pack.knowledge],
        "missing_context_keys": list(pack.missing_context_keys),
        "requested_reasoning_functions": list(pack.requested_reasoning_functions),
        "schema_version": pack.schema_version,
        "task_id": pack.task_id,
    }


def _materialize_selected(
    selected_plan: Sequence[tuple[HorizonCandidate, str]],
    *,
    uow_factory: UnitOfWorkFactory,
) -> tuple[SelectedContextKnowledge, ...]:
    items: list[SelectedContextKnowledge] = []
    with uow_factory() as uow:
        for candidate, selection_reason in selected_plan:
            asset = uow.navigation.get_context_asset(
                candidate.stable_key,
                candidate.revision_id,
            )
            if asset is None:
                raise StaleContextKnowledgeError(
                    f"Selected context candidate {candidate.stable_key!r} revision "
                    f"{candidate.revision_id!r} is no longer current accepted"
                )
            if asset.title != candidate.title:
                raise StaleContextKnowledgeError(
                    f"Selected context candidate {candidate.stable_key!r} title no longer "
                    "matches the exact accepted revision"
                )
            if tuple(asset.reasoning_functions) != tuple(candidate.reasoning_functions):
                raise StaleContextKnowledgeError(
                    f"Selected context candidate {candidate.stable_key!r} reasoning "
                    "functions do not match the Horizon projection"
                )

            items.append(
                SelectedContextKnowledge(
                    asset=asset,
                    selection_reason=selection_reason,
                    origin=candidate.origin,
                    applicability_state=candidate.applicability_state,
                    missing_context_keys=candidate.missing_context_keys,
                    relation_source_key=candidate.relation_source_key,
                    relation_type=candidate.relation_type,
                    relation_revision_id=candidate.relation_revision_id,
                )
            )
    return tuple(items)


def _validate_request(request: MethodologicalContextRequest) -> tuple[str, ...]:
    task_id = request.task_id.strip()
    if not task_id:
        raise ContextSelectionError("task_id must be non-empty")
    if task_id != request.task_id:
        raise ContextSelectionError("task_id must not contain leading/trailing whitespace")
    if request.max_assets <= 0:
        raise ContextSelectionError("max_assets must be positive")
    if not request.requested_reasoning_functions:
        raise ContextSelectionError("requested_reasoning_functions must be non-empty")

    normalized: list[str] = []
    seen: set[str] = set()
    for value in request.requested_reasoning_functions:
        if not isinstance(value, str) or not value.strip():
            raise ContextSelectionError(
                "requested_reasoning_functions must contain non-empty strings"
            )
        if value != value.strip():
            raise ContextSelectionError(
                "reasoning function names must not contain leading/trailing whitespace"
            )
        if value in seen:
            raise ContextSelectionError(
                f"duplicate requested reasoning function: {value!r}"
            )
        seen.add(value)
        normalized.append(value)

    return tuple(sorted(normalized))


def _candidate_order(candidate: HorizonCandidate) -> tuple[int, str]:
    origin_priority = 0 if candidate.origin == "DIRECT" else 1
    return origin_priority, candidate.stable_key


def _selected_item_payload(item: SelectedContextKnowledge) -> dict[str, Any]:
    asset = item.asset
    return {
        "applicability_state": item.applicability_state,
        "components": [
            {
                "body": component.body,
                "component_key": component.component_key,
                "component_kind": component.component_kind,
                "reasoning_functions": list(component.reasoning_functions),
                "revision_id": component.revision_id,
            }
            for component in asset.components
        ],
        "context_requirements": [
            {
                "description": requirement.description,
                "key": requirement.key,
                "required_for": list(requirement.required_for),
            }
            for requirement in asset.context_requirements
        ],
        "intrinsic_kind": asset.intrinsic_kind,
        "limitations": list(asset.limitations),
        "missing_context_keys": list(item.missing_context_keys),
        "narrative_facets": [
            {
                "body": facet.body,
                "facet_kind": facet.facet_kind,
                "position": facet.position,
            }
            for facet in asset.narrative_facets
        ],
        "origin": item.origin,
        "purpose": asset.purpose,
        "reasoning_functions": list(asset.reasoning_functions),
        "relation_revision_id": item.relation_revision_id,
        "relation_source_key": item.relation_source_key,
        "relation_type": item.relation_type,
        "revision_id": asset.revision_id,
        "rules": [
            {
                "condition": rule.condition,
                "consequence_payload": rule.consequence_payload,
                "consequence_type": rule.consequence_type,
                "force": rule.force,
                "rationale": rule.rationale,
                "rule_key": rule.rule_key,
                "rule_spec_id": rule.rule_spec_id,
                "unknown_behavior": rule.unknown_behavior,
            }
            for rule in asset.rules
        ],
        "scope": asset.scope,
        "selection_reason": item.selection_reason,
        "semantic_checks": list(asset.semantic_checks),
        "stable_key": asset.stable_key,
        "title": asset.title,
    }
