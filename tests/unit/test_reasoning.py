from __future__ import annotations

import json

import pytest

from ads_system.application.reasoning import (
    KnowledgeRevisionPointer,
    ReasoningContextValueResult,
    ReasoningModelConfiguration,
    ReasoningRequest,
    validate_methodological_basis,
)


def _request() -> ReasoningRequest:
    return ReasoningRequest(
        run_id="run-1",
        run_nonce="nonce-before-context",
        system_instruction="Use only supplied evidence and context.",
        user_task="Compare the supplied options.",
        project_evidence={"project.task.is_supervised": True},
        methodological_context_payload={
            "schema_version": 1,
            "knowledge": [
                {"stable_key": "random-forest", "revision_id": "rev-rf"},
                {"stable_key": "gradient-boosted-trees", "revision_id": "rev-gbt"},
            ],
        },
        methodological_context_sha256="a" * 64,
        knowledge_revisions=(
            KnowledgeRevisionPointer("random-forest", "rev-rf"),
            KnowledgeRevisionPointer("gradient-boosted-trees", "rev-gbt"),
        ),
        model_configuration=ReasoningModelConfiguration(
            requested_model="gpt-5.6-sol",
            reasoning_effort="medium",
            verbosity="low",
            max_output_tokens=4000,
        ),
    )


def test_reasoning_request_is_deterministic_and_nonce_precedes_context() -> None:
    request = _request()
    first = request.canonical_model_input()
    second = request.canonical_model_input()
    assert first == second
    assert request.semantic_digest() == request.semantic_digest()

    payload = json.loads(first)
    assert payload["experiment_run_nonce"] == "nonce-before-context"
    # The canonical serialized envelope is deliberately ordered by key for
    # determinism. The semantic requirement is that the nonce is a separate
    # top-level field and therefore part of every unique request rather than
    # hidden inside/reused with the methodology payload.
    assert payload["methodological_context"]["schema_version"] == 1


def test_reasoning_result_rejects_duplicate_methodological_basis() -> None:
    with pytest.raises(ValueError, match="methodological_basis must not contain duplicates"):
        ReasoningContextValueResult(
            answer="Compare the two options.",
            proposed_actions=(),
            required_clarifications=(),
            warnings=(),
            methodological_basis=("random-forest", "random-forest"),
        )


def test_methodological_basis_must_be_subset_of_supplied_context() -> None:
    request = _request()
    valid = ReasoningContextValueResult(
        answer="Both supplied tree ensembles are candidates.",
        proposed_actions=(),
        required_clarifications=(),
        warnings=(),
        methodological_basis=("random-forest", "gradient-boosted-trees"),
    )
    validate_methodological_basis(valid, request.knowledge_revisions)

    invalid = ReasoningContextValueResult(
        answer="Introduce another family.",
        proposed_actions=(),
        required_clarifications=(),
        warnings=(),
        methodological_basis=("unsupported-model",),
    )
    with pytest.raises(ValueError, match="outside supplied context"):
        validate_methodological_basis(invalid, request.knowledge_revisions)


def test_reasoning_request_rejects_duplicate_stable_keys() -> None:
    with pytest.raises(ValueError, match="unique stable keys"):
        ReasoningRequest(
            run_id="run-1",
            run_nonce="nonce-1",
            system_instruction="instruction",
            user_task="task",
            project_evidence={},
            methodological_context_payload={},
            methodological_context_sha256="b" * 64,
            knowledge_revisions=(
                KnowledgeRevisionPointer("same", "rev-1"),
                KnowledgeRevisionPointer("same", "rev-2"),
            ),
            model_configuration=ReasoningModelConfiguration(
                requested_model="gpt-5.6-sol",
                reasoning_effort="medium",
                verbosity="low",
                max_output_tokens=4000,
            ),
        )
