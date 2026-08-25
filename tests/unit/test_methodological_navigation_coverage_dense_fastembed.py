from __future__ import annotations

import math

import pytest

from experiments.methodological_navigation_coverage.contract import load_frozen_contract
from experiments.methodological_navigation_coverage.dense_fastembed import (
    EXPECTED_DIMENSION,
    FASTEMBED_VERSION,
    MODEL_NAME,
    FastEmbedDenseRetriever,
    asset_passage,
)


def _unit_vector(index: int) -> list[float]:
    values = [0.0] * EXPECTED_DIMENSION
    values[index] = 1.0
    return values


class FakeEmbeddingModel:
    def __init__(self, document_count: int) -> None:
        self.document_count = document_count
        self.query_calls: list[str] = []

    def passage_embed(self, passages):
        passages = list(passages)
        assert len(passages) == self.document_count
        return [_unit_vector(index) for index in range(len(passages))]

    def query_embed(self, query: str):
        self.query_calls.append(query)
        return [_unit_vector(0)]


def test_fastembed_adapter_exact_contract_with_injected_model() -> None:
    contract = load_frozen_contract()
    assets = contract.universe["assets"]
    model = FakeEmbeddingModel(len(assets))
    retriever = FastEmbedDenseRetriever(
        assets,
        model=model,
        observed_version=FASTEMBED_VERSION,
    )

    assert retriever.package_version == "0.8.0"
    assert retriever.model_name == MODEL_NAME
    hits = retriever.search("deterministic query", limit=6)
    assert len(hits) == 6
    assert hits[0].score == pytest.approx(1.0)
    assert hits[0].channel == "DENSE_FASTEMBED"
    assert len({item.stable_key for item in hits}) == 6
    assert all(item.revision_id for item in hits)
    assert model.query_calls == ["deterministic query"]
    assert math.isfinite(hits[-1].score)


def test_fastembed_adapter_rejects_version_and_dimension_drift() -> None:
    contract = load_frozen_contract()
    assets = contract.universe["assets"]
    with pytest.raises(ValueError, match="exact frozen FastEmbed version"):
        FastEmbedDenseRetriever(
            assets,
            model=FakeEmbeddingModel(len(assets)),
            observed_version="0.7.0",
        )

    class BadDimensionModel(FakeEmbeddingModel):
        def passage_embed(self, passages):
            passages = list(passages)
            return [[1.0, 0.0] for _ in passages]

    with pytest.raises(ValueError, match="384-dimensional"):
        FastEmbedDenseRetriever(
            assets,
            model=BadDimensionModel(len(assets)),
            observed_version=FASTEMBED_VERSION,
        )


def test_semantic_passage_projection_is_nonempty_for_all_frozen_assets() -> None:
    contract = load_frozen_contract()
    passages = [asset_passage(item) for item in contract.universe["assets"]]
    assert len(passages) == 28
    assert all(item.strip() for item in passages)
    assert any("Prediction" in item or "prediction" in item for item in passages)
