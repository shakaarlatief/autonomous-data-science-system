"""Non-scored integrity tests for prospective R0-P03 independent task/reference intake.

No test here judges source relevance, authors a new question, certifies independent
reviewer exposure, retrieves a correct answer, selects a heldout sample, or
computes a navigation score. The historical W5 source corpus and fixture
remain immutable experimental evidence.
"""

from __future__ import annotations

import importlib.util
import json
import re
import subprocess
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / "experiments/r0_p03_navigation_probe/independent_reference_intake_candidate.py"
INTAKE = ROOT / "experiments/r0_p03_navigation_probe/legacy_blinded_intake_candidate.json"
METHOD = ROOT / "experiments/r0_p03_navigation_probe/independent_reference_method_candidate.json"

_spec = importlib.util.spec_from_file_location("r0_p03_independent_reference_intake", SOURCE)
assert _spec is not None and _spec.loader is not None
module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(module)


@pytest.fixture(scope="module")
def intake():
    return module.build_intake(ROOT)


def test_intake_reproducibility_and_immutable_refs(intake):
    assert intake == module.build_intake(ROOT)
    assert intake == json.loads(INTAKE.read_text("utf-8"))
    assert intake["input_ref"] == module.INPUT_REF
    assert intake["historical_source_ref"] == module.HISTORICAL_REF
    assert intake["state"] == "PREFREEZE_SCRUBBED_INTAKE_CANDIDATE_NOT_AN_INDEPENDENT_REFERENCE"
    assert re.fullmatch(r"[0-9a-f]{64}", intake["corpus_manifest_sha256"])


def test_exact_legacy_65_sources_and_nine_themes(intake):
    assert intake["historical_source_count"] == len(intake["corpus"]) == 65
    assert intake["theme_count"] == len(intake["themes"]) == 9
    paths = [x["source_path"] for x in intake["corpus"]]
    assert paths == sorted(paths)
    assert len(paths) == len(set(paths))
    tokens = [x["case_id"] for x in intake["themes"]]
    assert len(tokens) == len(set(tokens))
    assert all(item["question_status"] == "NOT_YET_AUTHORED_BY_FRESH_NEUTRALIZER" for item in intake["themes"])


def test_manifest_contains_all_historical_carrier_blob_ids(intake):
    blobs = module.git_blobs(ROOT, module.HISTORICAL_REF)
    for record in intake["corpus"]:
        assert blobs[record["source_path"]] == record["source_blob_oid"]
        assert re.fullmatch(r"[0-9a-f]{40}", record["source_blob_oid"])
    assert "docs/project_knowledge/architecture/whole_architecture.md" in {
        item["source_path"] for item in intake["corpus"]
    }


def test_scrubbed_intake_has_no_B1_memberships_or_gold(intake):
    text = json.dumps(intake)
    for forbidden in ('"candidate_subjects"', '"legacy_topics"', '"must_retrieve"',
                      '"must_not_retrieve"', '"subjects"', '"preferred_subject"',
                      '"scoring_answers"', '"gold_answers"', '"heldout_paths"'):
        assert forbidden not in text
    assert {tuple(sorted(r)) for r in intake["corpus"]} == {("source_blob_oid", "source_path")}
    assert {tuple(sorted(r)) for r in intake["themes"]} == {
        ("case_id", "neutral_theme_hint", "question_status")
    }
    assert all("source_path" not in t for t in intake["themes"])


def test_theme_ids_are_lineage_hints_not_stated_questions(intake):
    assert "theme hint words originate in B1 subject names" in intake["limitations"][0]
    assert [t["case_id"] for t in intake["themes"]] == [f"legacy-{i:02d}" for i in range(1, 10)]
    assert all(t["neutral_theme_hint"] and "-" not in t["neutral_theme_hint"] for t in intake["themes"])
    assert not any("question_text" in t or "required_sources" in t for t in intake["themes"])


def test_input_legacy_fixtures_are_exact_git_bound_not_mutated(intake):
    for alias, expected_sha256 in intake["historical_input_blob_sha256"].items():
        path = {"original_scenarios_input": module.SCENARIO_PATH,
                "original_corpus_input": module.ANNOTATIONS_PATH}[alias]
        data = module.git_file(ROOT, module.INPUT_REF, path)
        import hashlib
        assert hashlib.sha256(data).hexdigest() == expected_sha256
    with pytest.raises(ValueError):
        module.git_file(ROOT, "HEAD", module.SCENARIO_PATH)
    with pytest.raises(ValueError):
        module.git_file(ROOT, module.INPUT_REF, "../untrusted")


def test_method_preserves_all_original_scientific_gates_and_owner_option_a():
    method = json.loads(METHOD.read_text("utf-8"))
    gates = method["original_gate"]
    assert gates["primary_total"] == 12
    assert len(gates["primary_categories"]) == 4
    assert set(gates["primary_categories"].values()) == {3}
    assert (gates["legacy_total"], gates["primary_pass_min"], gates["legacy_pass_min"]) == (9, 10, 8)
    assert (gates["build_target"], gates["heldout_target"]) == (60, 20)
    assert gates["false_authority_tolerance"] == 0
    assert method["legacy_world"]["fixed_sources"] == 65
    assert method["legacy_world"]["topics"] == 9
    assert method["status"].startswith("PREFREEZE_METHOD_ONLY")
    assert "owner_option_a" in method["source_anchors"]


def test_independence_is_explicitly_unfulfilled_and_fail_closed():
    method = json.loads(METHOD.read_text("utf-8"))
    assert method["primary_world"]["author_selection"] == "UNRESOLVED"
    assert method["primary_world"]["gold_answers"] == "NOT_AUTHORED"
    assert method["primary_world"]["task_questions"] == "NOT_AUTHORED"
    assert "cannot_demonstrate_fresh_neutral_annotator_or_evaluator" in method["failure_halts"]
    assert "cannot_isolate_original_B1_gold_from_neutralizer" in method["failure_halts"]
    assert "public_answer_keys_leak_before_arm_freeze" in method["failure_halts"]
    assert "no_access_to_private_gold" in method["roles"]["arm_authors"]["requires"]
    assert method["roles"]["scored_evaluators"]["count_min"] >= 2


def test_analyst_does_not_author_answer_key_or_select_cohort(intake):
    method = json.loads(METHOD.read_text("utf-8"))
    forbidden = {"task_prompts", "scored_results", "gold_answers", "heldout_paths",
                 "selected_build", "required_source_sets", "scenario_relevance_gold"}
    assert not (forbidden & set(intake))
    assert not (forbidden & set(method))
    assert "new_P03_answer_key" in method["explicitly_not_authorized"]
    assert "task_prompt_selection" in method["explicitly_not_authorized"]
    assert "hidden_heldout_selection" in method["explicitly_not_authorized"]
    assert "scored_run" in method["explicitly_not_authorized"]


def test_old_W5_history_remains_experimental_not_replaced():
    method = json.loads(METHOD.read_text("utf-8"))
    assert method["legacy_world"]["immutable_ref"] == module.HISTORICAL_REF
    assert method["legacy_world"]["positive_action"] == "fresh_neutralizer_must_resolve_meaning_and_intended_scope"
    assert "historical B1" in " ".join(method["roles"]["historical_theme_neutralizer"]["requires"]).lower() or any(
        "B1" in x for x in method["roles"]["historical_theme_neutralizer"]["requires"]
    )
