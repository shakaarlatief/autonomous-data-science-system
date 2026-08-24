"""Exact experiment-local FastEmbed dense retrieval for Specification 022.

The adapter preserves Specification 010's semantic passage projection and the
Specification 022 dense treatment while keeping FastEmbed outside the locked
production dependency set. Provider-free repository CI can import this module
without FastEmbed installed because all package/model imports are lazy.
"""

from __future__ import annotations

from collections.abc import Iterable, Mapping, Sequence
from importlib import import_module
from importlib.metadata import PackageNotFoundError, version
import math
from typing import Any, Callable

from ads_system.application.retrieval import KnowledgeRetrievalHit

FASTEMBED_PACKAGE = "fastembed"
FASTEMBED_VERSION = "0.8.0"
MODEL_NAME = "BAAI/bge-small-en-v1.5"
EXPECTED_DIMENSION = 384
PROVIDERS = ("CPUExecutionProvider",)
THREADS = 1


def _strings(value: Any) -> list[str]:
    if value is None:
        return []
    if isinstance(value, str):
        return [value]
    if isinstance(value, Mapping):
        result: list[str] = []
        for key in sorted(value):
            result.extend(_strings(value[key]))
        return result
    if isinstance(value, Iterable) and not isinstance(value, (bytes, bytearray)):
        result: list[str] = []
        for item in value:
            result.extend(_strings(item))
        return result
    return []


def asset_passage(asset: Mapping[str, Any]) -> str:
    """Build the unchanged Specification 010 semantic passage projection."""

    parts: list[str] = []
    for key in ("stable_key", "title", "purpose", "scope"):
        parts.extend(_strings(asset.get(key)))
    parts.extend(_strings(asset.get("limitations")))

    profile = asset.get("retrieval_profile") or {}
    if isinstance(profile, Mapping):
        for key in ("lexical_terms", "aliases", "semantic_cues"):
            parts.extend(_strings(profile.get(key)))

    parts.extend(_strings(asset.get("reasoning_functions")))
    for requirement in asset.get("context_requirements") or []:
        if isinstance(requirement, Mapping):
            for key in ("key", "description", "required_for"):
                parts.extend(_strings(requirement.get(key)))
    parts.extend(_strings(asset.get("semantic_checks")))

    for facet in asset.get("narrative_facets") or []:
        if isinstance(facet, Mapping):
            for key in ("facet_kind", "body"):
                parts.extend(_strings(facet.get(key)))

    for component in asset.get("components") or []:
        if isinstance(component, Mapping):
            for key in (
                "component_key",
                "component_kind",
                "body",
                "reasoning_functions",
            ):
                parts.extend(_strings(component.get(key)))

    return "\n".join(part for part in parts if part)


def _vector(value: Any) -> tuple[float, ...]:
    if hasattr(value, "tolist"):
        value = value.tolist()
    if not isinstance(value, Sequence) or isinstance(value, (str, bytes, bytearray)):
        raise ValueError("embedding vector must be a numeric sequence")
    result = tuple(float(item) for item in value)
    if len(result) != EXPECTED_DIMENSION:
        raise ValueError(
            f"expected {EXPECTED_DIMENSION}-dimensional embedding, got {len(result)}"
        )
    norm = math.sqrt(sum(item * item for item in result))
    if norm == 0.0:
        raise ValueError("embedding vector must have non-zero norm")
    return tuple(item / norm for item in result)


def _dot(left: Sequence[float], right: Sequence[float]) -> float:
    if len(left) != len(right):
        raise ValueError("embedding dimensions do not match")
    return sum(a * b for a, b in zip(left, right, strict=True))


class FastEmbedDenseRetriever:
    """Frozen exact-cosine dense retrieval over the accepted benchmark universe."""

    def __init__(
        self,
        assets: Sequence[Mapping[str, Any]],
        *,
        model: Any | None = None,
        observed_version: str | None = None,
        model_factory: Callable[..., Any] | None = None,
    ) -> None:
        ordered = sorted(assets, key=lambda item: str(item["stable_key"]))
        if len(ordered) != 28:
            raise ValueError(
                f"Specification 022 dense corpus requires 28 assets, got {len(ordered)}"
            )
        self._stable_keys = tuple(str(item["stable_key"]) for item in ordered)
        if len(self._stable_keys) != len(set(self._stable_keys)):
            raise ValueError("dense corpus stable keys must be unique")
        self._revision_ids = {
            str(item["stable_key"]): str(item["revision_id"]) for item in ordered
        }
        self._titles = {
            str(item["stable_key"]): str(item["title"]) for item in ordered
        }
        passages = [asset_passage(item) for item in ordered]
        if any(not passage for passage in passages):
            raise ValueError("dense corpus passages must be non-empty")

        if model is None:
            installed = self._installed_version()
            if installed != FASTEMBED_VERSION:
                raise RuntimeError(
                    "FastEmbed version does not match frozen Specification 022: "
                    f"expected {FASTEMBED_VERSION}, observed {installed}"
                )
            factory = model_factory or self._load_model_factory()
            model = factory(
                model_name=MODEL_NAME,
                providers=list(PROVIDERS),
                threads=THREADS,
            )
        else:
            if observed_version != FASTEMBED_VERSION:
                raise ValueError(
                    "injected dense model must declare the exact frozen FastEmbed "
                    f"version {FASTEMBED_VERSION}"
                )
        self._model = model
        vectors = list(self._model.passage_embed(passages))
        if len(vectors) != 28:
            raise ValueError(
                f"dense model returned {len(vectors)} document embeddings for 28 assets"
            )
        self._document_vectors = tuple(_vector(item) for item in vectors)

    @property
    def package_version(self) -> str:
        return FASTEMBED_VERSION

    @property
    def model_name(self) -> str:
        return MODEL_NAME

    @staticmethod
    def _installed_version() -> str:
        try:
            return version(FASTEMBED_PACKAGE)
        except PackageNotFoundError as exc:
            raise RuntimeError(
                "fastembed is required only for the frozen Specification 022 "
                f"live-capable dense adapter; expected {FASTEMBED_VERSION}"
            ) from exc

    @staticmethod
    def _load_model_factory() -> Callable[..., Any]:
        try:
            module = import_module("fastembed")
        except ModuleNotFoundError as exc:
            raise RuntimeError(
                "fastembed is not installed; live-capable Specification 022 "
                "execution must install the frozen experiment-only dependency"
            ) from exc
        factory = getattr(module, "TextEmbedding", None)
        if factory is None:
            raise RuntimeError("fastembed.TextEmbedding is unavailable")
        return factory

    def search(
        self,
        query: str,
        *,
        limit: int = 10,
    ) -> tuple[KnowledgeRetrievalHit, ...]:
        if not query.strip():
            return ()
        if limit <= 0:
            return ()
        query_vectors = list(self._model.query_embed(query))
        if len(query_vectors) != 1:
            raise ValueError(
                f"dense query embedding expected one vector, got {len(query_vectors)}"
            )
        query_vector = _vector(query_vectors[0])
        scored = sorted(
            (
                (stable_key, _dot(document, query_vector))
                for stable_key, document in zip(
                    self._stable_keys,
                    self._document_vectors,
                    strict=True,
                )
            ),
            key=lambda item: (-item[1], item[0]),
        )[:limit]
        return tuple(
            KnowledgeRetrievalHit(
                stable_key=stable_key,
                revision_id=self._revision_ids[stable_key],
                title=self._titles[stable_key],
                score=float(score),
                channel="DENSE_FASTEMBED",
            )
            for stable_key, score in scored
        )
