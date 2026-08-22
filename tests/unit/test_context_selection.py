from __future__ import annotations

from dataclasses import dataclass

import pytest

from ads_system.application.context_models import (
    ContextKnowledgeAsset,
    MethodologicalContextRequest,
)
from ads_system.application.context_selection import (
    BUDGET_LIMIT,
    ContextSelectionError,
    NO_REASONING_FUNCTION_MATCH,
    select_methodological_context,
)
from ads_system.application.horizon_models import HorizonCandidate, MethodologicalHorizon


class _FakeNavigation:
    def __init__(self, assets: dict[tuple[str, str], ContextKnowledgeAsset]) -> None:
        self.assets = assets
        self.context_reads: list[tuple[str, str]] = []

    def get_context_asset(
        self, stable_key: str, revision_id: str
    ) -> ContextKnowledgeAsset | None:
        self.context_reads.append((stable_key, revision_id))
        return self.assets.get((stable_key, revision_id))


@dataclass
class _FakeUow:
    navigation: _FakeNavigation

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb) -> None:
        return None


def _asset(stable_key: str, revision_id: str, *functions: str) -> ContextKnowledgeAsset:
    return ContextKnowledgeAsset(
        stable_key=stable_key,
        revision_id=revision_id,
        title=stable_key.title(),
        intrinsic_kind="METHOD",
        purpose=f"Purpose for {stable_key}",
        scope=None,
        reasoning_functions=tuple(functions),
        context_requirements=(),
        semantic_checks=(),
        limitations=(),
        narrative_facets=(),
        components=(),
        rules=(),
    )


def _candidate(
    stable_key: str,
    revision_id: str,
    *functions: str,
) -> HorizonCandidate:
    return HorizonCandidate(
        stable_key=stable_key,
        revision_id=revision_id,
        title=stable_key.title(),
        origin="DIRECT",
        relation_type=None,
        relation_revision_id=None,
        applicability_state="POSSIBLY_APPLICABLE",
        missing_context_keys=(),
        relation_source_key=None,
        reasoning_functions=tuple(functions),
    )


def test_budget_overflow_is_explicit_and_only_selected_content_is_materialized() -> None:
    alpha = _candidate("alpha", "rev-alpha", "MODEL_OPTION")
    beta = _candidate("beta", "rev-beta", "MODEL_OPTION")
    gamma = _candidate("gamma", "rev-gamma", "EVIDENCE_OPTION")
    horizon = MethodologicalHorizon(included=(alpha, beta, gamma), excluded=())

    navigation = _FakeNavigation(
        {
            ("alpha", "rev-alpha"): _asset("alpha", "rev-alpha", "MODEL_OPTION"),
            ("beta", "rev-beta"): _asset("beta", "rev-beta", "MODEL_OPTION"),
            ("gamma", "rev-gamma"): _asset("gamma", "rev-gamma", "EVIDENCE_OPTION"),
        }
    )
    result = select_methodological_context(
        horizon,
        MethodologicalContextRequest(
            task_id="model-choice",
            requested_reasoning_functions=("MODEL_OPTION",),
            max_assets=1,
        ),
        uow_factory=lambda: _FakeUow(navigation),
    )

    assert [item.asset.stable_key for item in result.pack.knowledge] == ["alpha"]
    decisions = {decision.stable_key: decision for decision in result.decisions}
    assert decisions["alpha"].selected is True
    assert decisions["beta"].selected is False
    assert decisions["beta"].reason == BUDGET_LIMIT
    assert decisions["gamma"].selected is False
    assert decisions["gamma"].reason == NO_REASONING_FUNCTION_MATCH

    # Full reasoning content is fetched after budgeting. The relevant candidate
    # dropped by the hard budget is therefore not materialized unnecessarily.
    assert navigation.context_reads == [("alpha", "rev-alpha")]


def test_context_request_rejects_duplicate_reasoning_functions() -> None:
    horizon = MethodologicalHorizon(included=(), excluded=())
    navigation = _FakeNavigation({})

    with pytest.raises(ContextSelectionError, match="duplicate requested reasoning function"):
        select_methodological_context(
            horizon,
            MethodologicalContextRequest(
                task_id="duplicate-functions",
                requested_reasoning_functions=("MODEL_OPTION", "MODEL_OPTION"),
                max_assets=1,
            ),
            uow_factory=lambda: _FakeUow(navigation),
        )
