from __future__ import annotations

import hashlib
import importlib.util
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ARTIFACT = ROOT / "docs/research/project_knowledge_candidate_01_q1_q2_q5_integrated_v01"
FIXTURE = ARTIFACT / "Q1_Q2_Q5_FIXTURE_V01.json"
ORACLE = ARTIFACT / "Q1_Q2_Q5_ORACLE_V01.json"
REQUEST = ARTIFACT / "FRESH_COLLABORATOR_REQUEST_V01.md"
RESULT = ARTIFACT / "FRESH_COLLABORATOR_RESULT_V01.json"
FIRST_RESULT = ARTIFACT / "FIRST_RUN_FRESH_COLLABORATOR_RESULT_V01.json"
EVALUATION = ARTIFACT / "FRESH_COLLABORATOR_EVALUATION_V01.json"
FIRST_EVAL = ARTIFACT / "FIRST_RUN_EVALUATION_V01.json"
SECOND_EVAL = ARTIFACT / "SECOND_RUN_EVALUATION_V01.json"
REVIEW = ARTIFACT / "PROMOTION_REVIEW_V01.json"
PROMOTED = ARTIFACT / "SHADOW_PROMOTED_KNOWLEDGE_V01.md"
FINAL = ARTIFACT / "FINAL_INTEGRATED_RESULT_V01.json"
EVAL_SCRIPT = ROOT / "scripts/research/project_knowledge_candidate01_q1_q2_q5_integrated_v01.py"
FINAL_SCRIPT = ROOT / "scripts/research/project_knowledge_candidate01_q1_q2_q5_integrated_final_v01.py"
EXPECTED_FIXTURE_SHA = "9b88f3e8b8b807451e5073cb803115307e4f272d150fddf25fddb431829d0991"
EXPECTED_ORACLE_SHA = "01f9077b9af9b428f746d9063919a829793212a4f580aeb65222f578aedbbfde"
EXPECTED_REQUEST_SHA = "c279b638b8214349eca1528d7f558b8b3b118c02063e9ef8d9da518166bee0fc"
EXPECTED_RESULT_SHA = "ccbaa542d3c522d0a6460eb20ba5784ba9fde419a7764043671370a9ec80d448"
DECL_RE = re.compile(
    r"<!-- PKA-STRUCTURED-DECLARATION-BEGIN -->\r?\n(.*?)\r?\n<!-- PKA-STRUCTURED-DECLARATION-END -->",
    re.DOTALL,
)


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def promoted_declaration():
    match = DECL_RE.search(PROMOTED.read_text(encoding="utf-8"))
    assert match
    return json.loads(match.group(1))


def test_frozen_fixture_oracle_request_and_first_result_hashes():
    assert hashlib.sha256(FIXTURE.read_bytes()).hexdigest() == EXPECTED_FIXTURE_SHA
    assert hashlib.sha256(ORACLE.read_bytes()).hexdigest() == EXPECTED_ORACLE_SHA
    assert hashlib.sha256(REQUEST.read_bytes()).hexdigest() == EXPECTED_REQUEST_SHA
    assert hashlib.sha256(RESULT.read_bytes()).hexdigest() == EXPECTED_RESULT_SHA
    assert RESULT.read_bytes() == FIRST_RESULT.read_bytes()


def test_fresh_collaborator_used_exact_bounded_read_set():
    fixture = load(FIXTURE)
    result = load(RESULT)
    assert len(result["reads"]) == 9
    assert len(set(result["reads"])) == 9
    assert set(result["reads"]) == set(fixture["allowed_collaborator_reads"])
    assert set(result["reads"]).isdisjoint(set(fixture["protocol"]["forbidden_legacy_bootstrap_paths"]))


def test_consequential_authority_decision_matches_frozen_expectations():
    result = load(RESULT)
    oracle = load(ORACLE)["expectations"]
    assert "BLOCKED" in result["task_a"]["decision"]
    assert oracle["task_a"]["required_governing_source"] in result["task_a"]["governing_sources"]
    assert set(oracle["task_a"]["required_evidence_sources"]).issubset(set(result["task_a"]["evidence_sources"]))
    assert oracle["task_a"]["required_distractor_rejection"] in result["task_a"]["distractors_rejected"]
    assert set(result["task_a"]["activated_risks"]) == set(oracle["task_a"]["required_risk_ids"])
    assert result["authority_receipt"]["workstream"] == oracle["task_a"]["required_workstream"]


def test_stale_authority_view_fails_visibly():
    result = load(RESULT)
    assert result["task_b"]["stale_view_id"] == "STALE-VIEW-COURSE2-01"
    assert "FAIL" in result["task_b"]["decision"]
    assert "SOURCE_BINDING_MISMATCH" in result["task_b"]["reason"]


def test_pre_promotion_evaluation_passes_and_budget_is_bounded():
    evaluation = load(EVALUATION)
    assert evaluation["oracle_result"] == "PASS"
    assert evaluation["passed"] == 25
    assert evaluation["failed"] == 0
    assert evaluation["budget"]["evidence_read_count"] == 9
    assert evaluation["budget"]["evidence_read_bytes_from_frozen_manifest"] == 35438
    assert evaluation["budget"]["legacy_bootstrap_read_count"] == 0


def test_evaluator_failures_are_preserved_as_evaluator_only_defects():
    first = load(FIRST_EVAL)
    second = load(SECOND_EVAL)
    final = load(EVALUATION)
    assert first["failed_checks"] == ["current_authority_unchanged"]
    assert second["failed_checks"] == ["current_authority_unchanged"]
    assert final["failed_checks"] == []
    assert load(FINAL)["collaborator_repairs"] == 0
    assert load(FINAL)["evaluator_repairs"] == 2


def test_source_revision_basis_ambiguity_is_preserved_not_hidden():
    finding = load(EVALUATION)["source_revision_diagnostic"]
    assert finding["finding"] == "SOURCE_REVISION_BASIS_AMBIGUOUS"
    assert finding["indexed_matches_git_blob"] is True
    assert finding["indexed_matches_working_tree_raw"] is False
    assert finding["indexed_matches_working_tree_lf_normalized"] is True
    assert finding["receipt_follows_frozen_index"] is True


def test_capture_requires_explicit_review_and_promotes_only_inside_shadow():
    result = load(RESULT)
    review = load(REVIEW)
    promoted = promoted_declaration()
    assert result["capture_candidate"]["state"] == "CAPTURED_NON_AUTHORITATIVE"
    assert result["capture_candidate"]["promotion_recommendation"] == "REVIEW_FOR_PROMOTION"
    assert all(review["checks"].values())
    assert review["decision"] == "ACCEPT_FOR_SHADOW_PROMOTION"
    assert promoted["statement"] == result["capture_candidate"]["statement"]
    assert promoted["source_basis"] == result["capture_candidate"]["source_basis"]
    assert promoted["shadow_only"] is True
    assert promoted["current_project_authority"] is False


def test_final_integrated_result_passes_without_selection_or_final_qualification():
    final = load(FINAL)
    assert final["passed"] == 11
    assert final["failed"] == 0
    assert final["integrated_q1_q2_q5_shadow_support"] is True
    assert final["architecture_amendment_required"] == "EXPLICIT_SOURCE_REVISION_BASIS_DESCRIPTOR"
    assert final["final_qualification_claimed"] is False
    assert final["target_architecture_selected"] is False


def test_exact_engine_provenance_is_not_overclaimed():
    final = load(FINAL)
    assert final["collaborator_exact_engine_provenance_recorded"] is False
    assert "not for a provider/engine-portability claim" in final["collaborator_provenance_limitation"]


def test_post_promotion_and_later_publication_state_do_not_rewrite_preserved_evidence():
    evaluator = load_module(EVAL_SCRIPT, "candidate01_q125_eval")
    fixture = evaluator.load(FIXTURE)
    oracle = evaluator.load(ORACLE)
    collaborator = evaluator.load(RESULT)
    preserved = load(EVALUATION)
    recomputed_eval = evaluator.evaluate(fixture, oracle, collaborator)
    phase_dependent = {"capture_not_auto_promoted", "current_authority_unchanged"}
    for key, value in preserved["checks"].items():
        if key not in phase_dependent:
            assert recomputed_eval["checks"][key] == value
    assert preserved["checks"]["capture_not_auto_promoted"] is True
    assert preserved["checks"]["current_authority_unchanged"] is True
    assert recomputed_eval["checks"]["capture_not_auto_promoted"] is False
    assert recomputed_eval["checks"]["current_authority_unchanged"] in {True, False}
    assert set(recomputed_eval["failed_checks"]).issubset(phase_dependent)
    final = load(FINAL)
    assert final["integrated_q1_q2_q5_shadow_support"] is True
    assert final["checks"]["current_authority_unchanged"] is True
