"""Classical corpus-trained LSA embeddings on frozen Route B source bodies.

Creates an actual low-rank distributional semantic vector space using a
standard-library-only Gram eigendecomposition. This is NOT a pretrained
transformer or an independently scored formal Research513 B4 arm.

Mathematical construction:
    X: 60 x |vocabulary| L2-normalized binary-IDF source-word matrix
    G = X X^T: 60 x 60 source Gram matrix
    G U_k ~= U_k Lambda_k,  Lambda_k > 0
    document latent: U_k sqrt(Lambda_k)
    question latent: question X^T U_k / sqrt(Lambda_k)
Cosine on those real-valued dense latent vectors drives retrieval.
"""
from __future__ import annotations

from collections import Counter, defaultdict
from hashlib import sha256
import json
import math
import random
from pathlib import Path
from typing import Any

from experiments.r0_p03_navigation_probe.exploratory_t2_no_id_retrieval_and_selective_evidence_v04 import tokens
from experiments.r0_p03_navigation_probe.route_b_primary_b0_baseline_execution_v01 import (
    ROOT, PIN, original_contents,
)

BASE = ROOT / "experiments/r0_p03_navigation_probe"
BASELINE = BASE / "route_b_primary_b0_baseline_result_v01.json"
BASELINE_SHA256 = "59ab36aef96046f71e2ccacbcc2105918ab19ed4bbc1f013e9bb78539a9bd4ab"
BASELINE_SIZE = 122682
STRUCTURED = BASE / "route_b_distinct_b1_b2_b3_navigation_comparison_result_v01.json"
STRUCTURED_SHA256 = "6a2b656432a5b8fbb963b0e8c14220411ed57bbad6127b8a550c05cf93ee0fa2"
STRUCTURED_SIZE = 92547
RESULT = BASE / "route_b_b4_local_lsa_embedding_comparison_result_v01.json"
CONTRACT = "ROUTE_B_B4_LOCAL_LSA_EMBEDDING_CONTRACT_V01.md"
DIMENSIONS = 16
STEPS = 160
RANDOM_SEED = 20261113
CHAR_CAP = 12000
K = 10
RRF_DAMPING = 60
ARMS = (
    "B0_ORIGINAL",
    "B4_LSA16_DENSE_ONLY_EXPLORATORY",
    "B4_LSA16_B0_RRF_EXPLORATORY",
    "B4_LSA16_B2_RRF_EXPLORATORY",
)


def frozen(path: Path, required_bytes: int, required_sha256: str) -> dict[str, Any]:
    b = path.read_bytes()
    if len(b) != required_bytes or sha256(b).hexdigest() != required_sha256:
        raise ValueError("Frozen original input was changed: " + path.name)
    return json.loads(b)


def dot(x: list[float], y: list[float]) -> float:
    return sum(a * b for a, b in zip(x, y))


def normalise(x: list[float]) -> list[float]:
    length = math.sqrt(dot(x, x))
    return [v / length for v in x] if length > 0 else [0.0 for _ in x]


def orthogonalize(v: list[float], predecessors: list[list[float]]) -> list[float]:
    """Double modified Gram-Schmidt avoids duplicate eigenvector components."""
    a = v[:]
    for _ in range(2):
        for q in predecessors:
            component = dot(a, q)
            a = [x - component * y for x, y in zip(a, q)]
    return normalise(a)


def matrix_times_vector(g: list[list[float]], v: list[float]) -> list[float]:
    return [dot(row, v) for row in g]


def fit_sparse_idf_matrix(
    texts: list[str],
) -> tuple[list[dict[str, float]], dict[str, float], dict[str, Any]]:
    """Learn word vocabulary/IDF from ONLY original 60 build source texts.

    Every source row has unique fixed non-stopword tokens, no labels, task
    words, document titles added separately, or gold-derived placements.
    """
    n = len(texts)
    if n != 60:
        raise ValueError("Must fit on exactly 60 original build sources")
    document_terms = [sorted(set(tokens(text[:CHAR_CAP]))) for text in texts]
    df = Counter(w for doc in document_terms for w in doc)
    if not df:
        raise ValueError("Original build corpus has no usable word features")
    idf = {w: 1.0 + math.log((n + 1) / (count + 1)) for w, count in sorted(df.items())}
    x = []
    for terms in document_terms:
        raw = [idf[w] for w in terms]
        denom = math.sqrt(sum(weight * weight for weight in raw))
        x.append({w: idf[w] / denom for w in terms} if denom > 0 else {})
    return x, idf, {
        "source_text_count": n,
        "vocabulary_size": len(idf),
        "nonzero_source_term_features": sum(map(len, x)),
        "source_feature_policy": "unique_fixed_word_tokens_IDF_L2",
        "source_original_character_cap": CHAR_CAP,
        "fitted_on_reference_answers": False,
        "fitted_on_question_texts": False,
    }


def gram_from_sparse(x: list[dict[str, float]]) -> tuple[list[list[float]], int]:
    """Compute XX^T from original source-token postings, no NumPy/SciPy."""
    n = len(x)
    postings: dict[str, list[tuple[int, float]]] = defaultdict(list)
    for i, row in enumerate(x):
        for word, weight in row.items():
            postings[word].append((i, weight))
    g = [[0.0] * n for _ in range(n)]
    pair_updates = 0
    for word in sorted(postings):
        observed = postings[word]
        for offset, (i, v) in enumerate(observed):
            for j, w in observed[offset:]:
                g[i][j] += v * w
                if i != j:
                    g[j][i] += v * w
                pair_updates += 1
    if any(abs(g[i][i] - 1.0) > 1e-7 for i, row in enumerate(x) if row):
        raise ValueError("Failed source TF-IDF unit-normalization invariant")
    return g, pair_updates


def leading_eigenvectors(g: list[list[float]]) -> tuple[list[list[float]], list[float], list[dict]]:
    """Deterministic orthogonal power iteration on a symmetric PSD Gram.

    The output contains actual residuals; approximation is not disguised
    as a converged exact SVD. No query-dependent fitting or dimension
    sweep is performed.
    """
    n = len(g)
    rng = random.Random(RANDOM_SEED)
    basis: list[list[float]] = []
    eigenvalues: list[float] = []
    diagnostics: list[dict] = []
    for component in range(min(DIMENSIONS, n)):
        v = orthogonalize([rng.uniform(-1.0, 1.0) for _ in range(n)], basis)
        if dot(v, v) < 0.5:
            raise ValueError("Unexpected degenerate eigenvector initializer")
        for _ in range(STEPS):
            v = orthogonalize(matrix_times_vector(g, v), basis)
            if dot(v, v) < 0.5:
                raise ValueError("Rank below requested LSA space or numerical breakdown")
        gv = matrix_times_vector(g, v)
        eigenvalue = dot(v, gv)
        if eigenvalue <= 1e-10:
            break
        residual = math.sqrt(sum((actual - eigenvalue * ui) ** 2
                                 for actual, ui in zip(gv, v)))
        basis.append(v)
        eigenvalues.append(eigenvalue)
        diagnostics.append({
            "component_index": component + 1,
            "rayleigh_eigenvalue": eigenvalue,
            "normalised_eigenvector_residual_l2": residual,
            "relative_residual_to_rayleigh": residual / eigenvalue,
            "fixed_power_steps": STEPS,
        })
    if not basis:
        raise ValueError("No original-source latent semantic factors were learned")
    return basis, eigenvalues, diagnostics


def original_query_vector(
    query: str, idf: dict[str, float],
) -> tuple[dict[str, float], dict]:
    unique = sorted(set(tokens(query)))
    known = [w for w in unique if w in idf]
    q_weights = [idf[w] for w in known]
    norm = math.sqrt(sum(w * w for w in q_weights))
    q = {w: idf[w] / norm for w in known} if norm > 0 else {}
    return q, {
        "unique_nonstopword_query_tokens": len(unique),
        "query_tokens_in_fitted_word_vocabulary": len(known),
        "query_oov_token_count": len(unique) - len(known),
        "query_projection_has_known_terms": bool(q),
    }


def latent_project(
    sparse_docs: list[dict[str, float]],
    idf: dict[str, float],
    basis: list[list[float]],
    eigenvalues: list[float],
    query: str,
) -> tuple[list[list[float]], list[float], dict]:
    """Project question into a true rank-reduced distributional term space."""
    doc_latent = [
        [math.sqrt(lam) * u[i] for u, lam in zip(basis, eigenvalues)]
        for i in range(len(sparse_docs))
    ]
    q, metadata = original_query_vector(query, idf)
    document_overlaps = [sum(w * row.get(t, 0.0) for t, w in q.items())
                         for row in sparse_docs]
    query_latent = [
        sum(overlap * u[i] for i, overlap in enumerate(document_overlaps))
        / math.sqrt(lam)
        for u, lam in zip(basis, eigenvalues)
    ]
    metadata["query_latent_norm"] = math.sqrt(dot(query_latent, query_latent))
    return doc_latent, query_latent, metadata


def dense_rank(
    build: list[str], docs: list[list[float]], query: list[float],
) -> tuple[list[str], list[dict]]:
    """Top-ten cosine over 16 learned LSA coordinates; zero projection abstains."""
    q_norm = math.sqrt(dot(query, query))
    if q_norm <= 1e-14:
        return [], []
    values = []
    for path, d in zip(build, docs):
        d_norm = math.sqrt(dot(d, d))
        score = dot(query, d) / (q_norm * d_norm) if d_norm > 1e-14 else 0.0
        values.append((path, score))
    values.sort(key=lambda x: (-x[1], x[0]))
    winners = values[:K]
    return [p for p, _ in winners], [
        {"path": p, "cosine_similarity": score} for p, score in winners
    ]


def rrf(left: list[str], right: list[str]) -> list[str]:
    scores = defaultdict(float)
    for ranker in (left, right):
        for index, path in enumerate(ranker[:K], 1):
            scores[path] += 1.0 / (RRF_DAMPING + index)
    return [p for p, _ in sorted(scores.items(), key=lambda x: (-x[1], x[0]))[:K]]


def run() -> dict[str, Any]:
    base = frozen(BASELINE, BASELINE_SIZE, BASELINE_SHA256)
    struct = frozen(STRUCTURED, STRUCTURED_SIZE, STRUCTURED_SHA256)
    build = base["build_sources"]
    if len(build) != 60 or len(base["heldout_sources"]) != 20:
        raise ValueError("Frozen original corpus 60+20 requirement violated")
    if struct["build_carriers"] != build or base["source_git_pin"] != PIN:
        raise ValueError("Original B0 and structured source worlds diverge")
    if len(base["comparative_retrieval_trace"]) != 12 or len(struct["retrieval_trace"]) != 12:
        raise ValueError("Source task count drift")
    original = original_contents(build)
    indexed_sha = {row["path"]: row["original_source_sha256"]
                   for row in base["source_roster"]}
    for p, content in original.items():
        if indexed_sha[p] != sha256(content).hexdigest():
            raise ValueError("Original source record drift: " + p)
    text = [original[path].decode("utf8")[:CHAR_CAP] for path in build]
    sparse_docs, idf, vocabulary_cost = fit_sparse_idf_matrix(text)
    gram, gram_updates = gram_from_sparse(sparse_docs)
    basis, eigenvalues, diagnostics = leading_eigenvectors(gram)
    doc_vectors = [
        [math.sqrt(lam) * vector[index] for vector, lam in zip(basis, eigenvalues)]
        for index in range(len(build))
    ]

    cases = []
    for b0case, structured_case in zip(
        base["comparative_retrieval_trace"], struct["retrieval_trace"]
    ):
        if (b0case["id"] != structured_case["id"]
                or b0case["question"] != structured_case["question"]):
            raise ValueError("Original 12 case identities/questions not identical")
        question = b0case["question"]
        sparse_q, q_meta = original_query_vector(question, idf)
        overlaps = [
            sum(w * source_doc.get(term, 0.0) for term, w in sparse_q.items())
            for source_doc in sparse_docs
        ]
        q_vector = [
            sum(overlap * component[i] for i, overlap in enumerate(overlaps))
            / math.sqrt(eigenvalue)
            for component, eigenvalue in zip(basis, eigenvalues)
        ]
        q_meta["query_latent_norm"] = math.sqrt(dot(q_vector, q_vector))
        dense, scored_dense = dense_rank(build, doc_vectors, q_vector)
        baseline = b0case["common_source_candidate_rankings"]["B0_SUBSTRATE_LEXICAL_BASELINE"]
        b2 = structured_case["arm_rankings_before_expected_source_lookup"][
            "B2_EDITORIAL_LINK_NAVIGATION"
        ]
        if baseline != structured_case["arm_rankings_before_expected_source_lookup"][
            "B0_SOURCE_LEXICAL_UNCHANGED"
        ]:
            raise ValueError("Source B0 lexical baseline changed after Checkpoint919")
        rankings = {
            "B0_ORIGINAL": list(baseline),
            "B4_LSA16_DENSE_ONLY_EXPLORATORY": dense,
            "B4_LSA16_B0_RRF_EXPLORATORY": rrf(baseline, dense),
            "B4_LSA16_B2_RRF_EXPLORATORY": rrf(b2, dense),
        }

        # Only now look up evaluation-only source identity for exposed hit@k.
        expected = b0case["intended_source_for_evaluation_only"]
        ranks = {
            label: (result.index(expected) + 1 if expected in result else None)
            for label, result in rankings.items()
        }
        cases.append({
            "question_id": b0case["id"],
            "original_question": question,
            "original_primary_category": b0case["category"],
            "fit_question_token_witness": q_meta,
            "query_latent_16_dimension_coordinates": q_vector,
            "original_Git_required_source_for_exposed_evaluation_only": expected,
            "expected_source_sha256": indexed_sha[expected],
            "rankings_before_exposed_source_lookup": rankings,
            "dense_scored_top10_original_git_paths": [
                {**score, "original_source_sha256": indexed_sha[score["path"]]}
                for score in scored_dense
            ],
            "exposed_required_source_rank_after_retrieval": ranks,
            "source_authority_or_operative_effect_asserted": False,
        })

    metrics = {}
    for name in ARMS:
        ranks = [row["exposed_required_source_rank_after_retrieval"][name]
                 for row in cases]
        metrics[name] = {
            f"required_source_at_{n}": sum(r is not None and r <= n for r in ranks)
            for n in (1, 3, 5, 10)
        } | {
            "mrr_at_10": sum((1 / r) if r else 0.0 for r in ranks) / len(ranks),
            "missing_source_at_top_10": [
                case["question_id"] for case in cases
                if case["exposed_required_source_rank_after_retrieval"][name] is None
            ],
        }

    return {
        "id": "R0_P03_ROUTE_B_CLASSICAL_DISTRIBUTIONAL_LSA_B4_EXPLORATORY_V01",
        "contract": CONTRACT,
        "original_git_pin": PIN,
        "original_B0_result_sha256": BASELINE_SHA256,
        "original_B123_result_sha256": STRUCTURED_SHA256,
        "training_source_paths": build,
        "model_type": "UNSUPERVISED_CORPUS_TRAINED_CLASSICAL_LSA_NOT_PRETRAINED_NEURAL",
        "trained_only_on_original_60_source_bodies": True,
        "heldout_original_files_excluded_from_fit": True,
        "fit_labels_or_reference_answers_used": False,
        "rank_16_requested": DIMENSIONS,
        "rank_actual": len(basis),
        "random_seed": RANDOM_SEED,
        "fixed_power_iteration_steps_per_component": STEPS,
        "token_policy": "V04 unique fixed non-stopword tokens",
        "source_character_cap": CHAR_CAP,
        "model_cost": {
            **vocabulary_cost,
            "symmetric_gram_matrix_float_entries": len(build) ** 2,
            "nonzero_gram_off_diagonals": sum(
                abs(gram[i][j]) > 0 for i in range(len(build))
                for j in range(len(build)) if i != j
            ),
            "original_word_posting_pair_updates": gram_updates,
            "fit_power_matrix_vector_multiplications": len(basis) * STEPS,
            "stored_document_latent_float_values": len(build) * len(basis),
            "stored_eigenvector_float_values": len(build) * len(basis),
            "query_embeddings_float_values": 12 * len(basis),
            "wall_clock_latency_not_measured": True,
            "neural_model_and_weights_download": False,
        },
        "model_fitted_word_idf_sha256": sha256(
            json.dumps(idf, sort_keys=True, separators=(",", ":")).encode()
        ).hexdigest(),
        "Gram_eigenvalues": eigenvalues,
        "Gram_eigenpair_actual_residuals": diagnostics,
        "document_dense_vectors": [
            {
                "path": path,
                "original_sha256": indexed_sha[path],
                "embedding": doc_vectors[i],
            }
            for i, path in enumerate(build)
        ],
        "cases": cases,
        "metrics": metrics,
        "scientific_limits": [
            "LSA is a genuine corpus-trained latent word-semantic embedding but not a pretrained language/sentence model or a transformer.",
            "The B4 formal arm is best justified structured architecture plus a fair pretrained/semantic embedding; this is a deliberately labelled exploratory semantic index and two bounded hybrids.",
            "The model is fit on the same exact 60 original source bodies with no supervised answers; the experimenter nevertheless saw all B0 and B1/B2/B3 retrieval results and designed this method afterward.",
            "Single coordinator-designated source per query is not independent, exhaustive relevance gold or evidence of a correct full answer.",
            "The common V03-native relation/effect/lineage substrate is not fully represented in the B0 original source-text diagnostic.",
            "No genuine externally pretrained neural embeddings were executable under authorized project access at this attempt; uv PyPI fetch was socket denied.",
            "No original nine-case independent legacy score, fresh blinded answer review, heldout subject assignment F1, independently source-owned B1/B3 concern metadata or complete B2 governed links.",
            "Original Git Status text and semantic vectors do not prove operative authority, deployment or acceptance.",
            "No formal R0-P03 architecture selection score, threshold acceptance, owner physical target or migration change is supported.",
        ],
        "formal_R0_P03_scored": False,
        "physical_target_selected": False,
    }


def main() -> None:
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", action="store_true")
    args = parser.parse_args()
    result = run()
    raw = (json.dumps(result, sort_keys=True, indent=2, ensure_ascii=True) + "\n").encode()
    if args.output:
        with RESULT.open("xb") as f:
            f.write(raw)
    print(json.dumps({
        "model": result["model_type"],
        "rank_actual": result["rank_actual"],
        "vocab": result["model_cost"]["vocabulary_size"],
        "source_nonzeros": result["model_cost"]["nonzero_source_term_features"],
        "max_relative_eigen_residual": max(
            item["relative_residual_to_rayleigh"]
            for item in result["Gram_eigenpair_actual_residuals"]
        ),
        "metrics": result["metrics"],
        "output_bytes": len(raw),
        "output_sha256": sha256(raw).hexdigest(),
        "saved": args.output,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
