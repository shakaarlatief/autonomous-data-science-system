"""Source-bound checks for the executed Route B corpus-trained LSA model.

An unsupervised truncated word co-occurrence factor space is a genuine
classical semantic embedding, but is not a pretrained language model and
does not repair exposed tasks or the original formal P03 protocol gates.
"""
from __future__ import annotations

from hashlib import sha256
import json
import math

import pytest

from experiments.r0_p03_navigation_probe.route_b_b4_local_lsa_embedding_comparison_v01 import (
    ARMS, BASELINE, BASELINE_SHA256, BASELINE_SIZE, DIMENSIONS, K, PIN,
    RESULT, ROOT, STEPS, STRUCTURED, STRUCTURED_SHA256, STRUCTURED_SIZE,
    dense_rank, dot, fit_sparse_idf_matrix, frozen,
    gram_from_sparse, latent_project, leading_eigenvectors,
    matrix_times_vector, normalise, original_contents, original_query_vector,
    orthogonalize, rrf, run,
)

OUTPUT_SIZE = 154662
OUTPUT_SHA = "59fd12cc78892bf6f97cde88e44fc692729582560011bf81a55f1fc62af0b00f"


def result() -> dict:
    raw = RESULT.read_bytes()
    assert len(raw) == OUTPUT_SIZE
    assert sha256(raw).hexdigest() == OUTPUT_SHA
    assert raw.endswith(b"\n") and b"\r\n" not in raw
    return json.loads(raw)


def test_original_B0_and_B123_exact_frozen_parent_sha_before_LSA() -> None:
    b0 = frozen(BASELINE, BASELINE_SIZE, BASELINE_SHA256)
    prior = frozen(STRUCTURED, STRUCTURED_SIZE, STRUCTURED_SHA256)
    actual = result()
    assert actual["original_B0_result_sha256"] == BASELINE_SHA256
    assert actual["original_B123_result_sha256"] == STRUCTURED_SHA256
    assert actual["original_git_pin"] == b0["source_git_pin"] == PIN
    assert prior["build_carriers"] == b0["build_sources"]
    assert actual["training_source_paths"] == b0["build_sources"]
    assert not (set(actual["training_source_paths"]) & set(b0["heldout_sources"]))
    assert len(b0["heldout_sources"]) == 20
    assert len(actual["training_source_paths"]) == 60


def test_true_word_factor_model_not_a_char_ngram_or_fake_neural_embedding() -> None:
    d = result()
    assert d["model_type"] == "UNSUPERVISED_CORPUS_TRAINED_CLASSICAL_LSA_NOT_PRETRAINED_NEURAL"
    assert d["trained_only_on_original_60_source_bodies"]
    assert d["heldout_original_files_excluded_from_fit"]
    assert not d["fit_labels_or_reference_answers_used"]
    assert d["rank_16_requested"] == d["rank_actual"] == DIMENSIONS == 16
    assert d["fixed_power_iteration_steps_per_component"] == STEPS == 160
    assert d["source_character_cap"] == 12000
    cost = d["model_cost"]
    assert cost["source_text_count"] == 60
    assert cost["source_original_character_cap"] == 12000
    assert cost["vocabulary_size"] == 5084
    assert cost["nonzero_source_term_features"] == 20098
    assert cost["symmetric_gram_matrix_float_entries"] == 3600
    assert cost["stored_document_latent_float_values"] == 960
    assert cost["stored_eigenvector_float_values"] == 960
    assert cost["query_embeddings_float_values"] == 192
    assert cost["neural_model_and_weights_download"] is False
    assert d["token_policy"].startswith("V04 unique fixed")
    assert not cost["fitted_on_reference_answers"]
    assert not cost["fitted_on_question_texts"]
    assert d["model_fitted_word_idf_sha256"]


def test_all_original_doc_sha256_bind_to_git_and_vectors_are_dense_nonzero() -> None:
    d = result()
    prior = frozen(BASELINE, BASELINE_SIZE, BASELINE_SHA256)
    blobs = original_contents(prior["build_sources"])
    assert len(blobs) == 60
    sha_by_path = {r["path"]: r["original_source_sha256"] for r in prior["source_roster"]}
    assert len(d["document_dense_vectors"]) == 60
    for embedding in d["document_dense_vectors"]:
        path = embedding["path"]
        assert sha256(blobs[path]).hexdigest() == sha_by_path[path]
        assert embedding["original_sha256"] == sha_by_path[path]
        assert len(embedding["embedding"]) == 16
        assert all(math.isfinite(v) for v in embedding["embedding"])
        assert math.sqrt(dot(embedding["embedding"], embedding["embedding"])) > 0


def test_latent_eigenspace_has_positive_factors_and_measured_residuals() -> None:
    d = result()
    lambdas = d["Gram_eigenvalues"]
    diagnostics = d["Gram_eigenpair_actual_residuals"]
    assert len(lambdas) == len(diagnostics) == 16
    assert all(eigenvalue > 0 for eigenvalue in lambdas)
    assert all(row["fixed_power_steps"] == 160 for row in diagnostics)
    assert max(row["relative_residual_to_rayleigh"] for row in diagnostics) < 0.01
    assert all(math.isfinite(x) for x in lambdas)
    assert lambdas[0] > lambdas[-1]


def test_synthetic_source_low_rank_spectral_math_without_any_external_package() -> None:
    # Independent validation of the eigensolver on a known positive
    # semidefinite matrix. Eigenvectors must be normalized and orthogonal.
    g = [[4.0, 0.0, 0.0], [0.0, 2.0, 0.0], [0.0, 0.0, 1.0]]
    vectors, eigenvalues, diag = leading_eigenvectors(g)
    assert len(vectors) == len(eigenvalues) == 3
    assert sorted(eigenvalues, reverse=True) == pytest.approx([4.0, 2.0, 1.0], rel=1e-7)
    for i, vector in enumerate(vectors):
        assert dot(vector, vector) == pytest.approx(1.0, abs=1e-7)
        assert matrix_times_vector(g, vector) == pytest.approx(
            [eigenvalues[i] * v for v in vector], abs=1e-5
        )
        for prev in vectors[:i]:
            assert abs(dot(vector, prev)) < 1e-7
        assert diag[i]["relative_residual_to_rayleigh"] < 1e-5
    assert normalise([3, 4]) == pytest.approx([0.6, 0.8])
    assert orthogonalize([1, 1], [[1, 0]]) == pytest.approx([0, 1])


def test_query_projection_known_word_and_out_of_vocabulary_abstention() -> None:
    # 60 fictional documents are used only for a unit-level feature
    # computation, never as an extension to the original source roster.
    dummy = ["apples oranges lemons" if i % 2 == 0
             else "physics gravitation relativity" for i in range(60)]
    sparse, vocab, stats = fit_sparse_idf_matrix(dummy)
    assert stats["vocabulary_size"] == 6
    assert stats["source_text_count"] == 60
    gram, changes = gram_from_sparse(sparse)
    assert len(gram) == 60 and changes > 0
    q, metadata = original_query_vector("apples gravitation foreignword", vocab)
    assert set(q) == {"apples", "gravitation"}
    assert metadata["query_oov_token_count"] == 1
    assert dot(list(q.values()), list(q.values())) == pytest.approx(1.0)
    unknown, reason = original_query_vector("totallyoutofvocabulary", vocab)
    assert unknown == {} and not reason["query_projection_has_known_terms"]
    assert dense_rank(["a", "b"], [[1.0, 0], [0, 1.0]], [0, 0]) == ([], [])


def test_latent_embedding_recomputes_query_projection_without_gold_shortcut() -> None:
    # Synthetic factor-space projection proves query coordinates derive
    # from source-term overlap, not the source label, path or status fields.
    dummy = [f"apples oranges distinctterm{i}" if i % 2 == 0
             else f"physics gravitation distinctterm{i}" for i in range(60)]
    sparse, vocab, _ = fit_sparse_idf_matrix(dummy)
    gram, _ = gram_from_sparse(sparse)
    components, lambdas, _ = leading_eigenvectors(gram)
    original_vectors, qvec, meta = latent_project(
        sparse, vocab, components, lambdas, "apples oranges"
    )
    assert len(original_vectors) == 60
    assert len(qvec) == len(components)
    assert meta["query_projection_has_known_terms"]
    assert all(math.isfinite(v) for v in qvec)
    assert dense_rank(["a", "b"], [[1, 0], [0, 1]], [1, 0])[0] == ["a", "b"]
    assert rrf(["a", "b"], ["b", "a"]) == ["a", "b"]


def test_real_original_12_question_B4_outputs_and_failures_not_repaired() -> None:
    d = result()
    metrics = d["metrics"]
    assert set(metrics) == set(ARMS)
    assert metrics["B0_ORIGINAL"]["required_source_at_1"] == 8
    assert metrics["B0_ORIGINAL"]["required_source_at_10"] == 11
    assert metrics["B4_LSA16_DENSE_ONLY_EXPLORATORY"]["required_source_at_1"] == 3
    assert metrics["B4_LSA16_DENSE_ONLY_EXPLORATORY"]["required_source_at_10"] == 10
    assert metrics["B4_LSA16_B0_RRF_EXPLORATORY"]["required_source_at_1"] == 5
    assert metrics["B4_LSA16_B0_RRF_EXPLORATORY"]["required_source_at_10"] == 11
    assert metrics["B4_LSA16_B2_RRF_EXPLORATORY"]["required_source_at_1"] == 5
    assert metrics["B4_LSA16_B2_RRF_EXPLORATORY"]["required_source_at_10"] == 11
    assert metrics["B4_LSA16_DENSE_ONLY_EXPLORATORY"]["missing_source_at_top_10"] == ["P01", "P02"]
    assert metrics["B4_LSA16_B0_RRF_EXPLORATORY"]["missing_source_at_top_10"] == ["P01"]
    cases = d["cases"]
    assert len(cases) == 12
    original = frozen(BASELINE, BASELINE_SIZE, BASELINE_SHA256)
    assert [c["question_id"] for c in cases] == [
        c["id"] for c in original["comparative_retrieval_trace"]
    ]
    for before, case in zip(original["comparative_retrieval_trace"], cases):
        assert case["original_question"] == before["question"]
        assert case["rankings_before_exposed_source_lookup"]["B0_ORIGINAL"] == (
            before["common_source_candidate_rankings"]["B0_SUBSTRATE_LEXICAL_BASELINE"]
        )
        assert case["source_authority_or_operative_effect_asserted"] is False
        expected = case["original_Git_required_source_for_exposed_evaluation_only"]
        for name, ranked in case["rankings_before_exposed_source_lookup"].items():
            assert len(ranked) <= K == 10
            assert len(set(ranked)) == len(ranked)
            assert set(ranked) <= set(d["training_source_paths"])
            got = ranked.index(expected) + 1 if expected in ranked else None
            assert case["exposed_required_source_rank_after_retrieval"][name] == got
        for hit in case["dense_scored_top10_original_git_paths"]:
            assert -1.0 - 1e-9 <= hit["cosine_similarity"] <= 1.0 + 1e-9


def test_full_original_model_reexecution_yields_identical_154662_bytes() -> None:
    assert run() == result()


def test_formal_science_and_pretrained_model_claims_stay_unqualified() -> None:
    d = result()
    assert not d["formal_R0_P03_scored"]
    assert not d["physical_target_selected"]
    assert any("not a pretrained" in text.lower() for text in d["scientific_limits"])
    assert any("nine-case" in text for text in d["scientific_limits"])
    assert any("independent" in text for text in d["scientific_limits"])
    assert any("no formal" in text.lower() for text in d["scientific_limits"])
