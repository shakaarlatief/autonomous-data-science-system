from __future__ import annotations

import hashlib
import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ART = ROOT / "docs/research/project_knowledge_candidate_01_q1_q2_cross_provider_v01"
FIXTURE = ART / "Q1_Q2_CROSS_PROVIDER_FIXTURE_V01.json"
ORACLE = ART / "Q1_Q2_CROSS_PROVIDER_ORACLE_V01.json"
PACKET = ART / "PORTABLE_PROVIDER_PACKET_V01.md"
REQUEST = ART / "EXTERNAL_PROVIDER_REQUEST_V01.txt"
RESULT = ART / "EXTERNAL_PROVIDER_RESULT_V01.json"
FIRST_RESULT = ART / "FIRST_RUN_EXTERNAL_PROVIDER_RESULT_V01.json"
EVALUATION = ART / "EVALUATION_V01.json"
EVAL_SCRIPT = ROOT / "scripts/research/evaluate_candidate_01_q1_q2_cross_provider_v01.py"

EXPECTED_CANONICAL = {
    "fixture": "ac08b3437e5776dff536aae3566ebd709cfc98a71b0143d270609fc4280d0817",
    "oracle": "891a242cf29dcda66fc389c7ff7d9d41030b922a953156dceb7051493668d64e",
    "packet": "669715d607f3ac4fd71f7e9d653b9721ca1d8bc173cb01197b28ed44176c4799",
    "request": "e0791220868ef12bf3cbd9b32facf87add461c80b38943114776a6214bdaecbf",
}
EXPECTED_RESULT = "d118cc88c6576ef35470fed95e48c7ee13fc295a7ce64dab919c871f15ec8ef8"


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def canonical_text_sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes().replace(b"\r\n", b"\n")).hexdigest()


def test_frozen_artifact_and_first_result_hashes():
    assert canonical_text_sha(FIXTURE) == EXPECTED_CANONICAL["fixture"]
    assert canonical_text_sha(ORACLE) == EXPECTED_CANONICAL["oracle"]
    assert canonical_text_sha(PACKET) == EXPECTED_CANONICAL["packet"]
    assert canonical_text_sha(REQUEST) == EXPECTED_CANONICAL["request"]
    assert hashlib.sha256(RESULT.read_bytes()).hexdigest() == EXPECTED_RESULT
    assert RESULT.read_bytes() == FIRST_RESULT.read_bytes()


def test_external_provider_is_non_openai_and_exact_model_is_recorded():
    result = load(RESULT)
    assert result["provider"] == "Anthropic"
    assert result["model"] == "Claude Opus 5"
    assert result["fresh_session"] is True
    assert result["prior_ads_context"] is False


def test_task_a_scoped_replacement_beats_retrieval_rank():
    result = load(RESULT)["task_a"]
    assert result["resolution_status"] == "RESOLVED"
    assert result["governing_ids"] == ["D-028"]
    assert result["retrieval_used_as_authority"] is False


def test_task_b_missing_scope_remains_fail_visible():
    result = load(RESULT)["task_b"]
    assert result["resolution_status"].startswith("UNRESOLVED")
    assert result["governing_ids"] == []
    assert result["retrieval_used_as_authority"] is False
    assert "scope" in result["missing_scope_or_conflict"].lower()


def test_task_c_partial_supersession_retains_public_git_exclusion():
    result = load(RESULT)["task_c"]
    assert result["resolution_status"].startswith("RESOLVED")
    assert result["governing_architecture_ids"] == ["D-033"]
    assert result["retained_outcomes"] == ["public_git_source_binary_exclusion"]
    assert result["public_git_source_binaries_allowed_merely_because_ads_consumes_them"] is False
    assert result["retrieval_used_as_authority"] is False


def test_authority_receipt_binds_frozen_base_and_non_authoritative_retrieval():
    receipt = load(RESULT)["authority_receipt"]
    assert receipt["source_base_commit"] == "a685ef48c4c4853babff9295f03f198c7b3dcd1d"
    assert receipt["retrieval_is_non_authoritative"] is True
    assert receipt["unresolved_items"]


def test_evaluation_passes_all_semantic_checks():
    evaluation = load(EVALUATION)
    assert evaluation["passed"] == 20
    assert evaluation["failed"] == 0
    assert evaluation["cross_provider_q1_q2_support"] is True
    assert evaluation["supported_mechanism_ids"] == ["KA-R36", "KA-R14", "KA-R24"]


def test_status_variances_are_nonsemantic():
    variances = load(EVALUATION)["status_label_variances"]
    assert variances["task_b_status"]["literal_match"] is False
    assert variances["task_b_status"]["semantic_match"] is True
    assert variances["task_c_status"]["literal_match"] is False
    assert variances["task_c_status"]["semantic_match"] is True


def test_evaluator_recomputes_exactly():
    spec = importlib.util.spec_from_file_location("cross_provider_eval", EVAL_SCRIPT)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    assert module.evaluate() == load(EVALUATION)
