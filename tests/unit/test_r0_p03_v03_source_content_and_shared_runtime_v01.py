"""Non-scored source-content evidence and runnable common-source API controls.

No test builds a formal cohort, originates a primary information need,
decides historical authority, creates neutral legacy gold, scores B0-B4,
or supplies arm-specific navigation metadata.
"""
from __future__ import annotations

from copy import deepcopy
from hashlib import sha256
import json

import pytest

from experiments.r0_p03_navigation_probe import (
    v03_r0_p03_source_content_role_preflight_v01 as audit,
    v03_r0_p03_shared_core_runtime_v01 as core,
    v03_r0_p03_unscored_mixed_source_cohort_readiness_v01 as pilot,
)


@pytest.fixture(scope="module")
def content():
    return audit.build()


@pytest.fixture(scope="module")
def content_by_path(content):
    return {row["source_path"]: row for row in content["content_role_evidence"]}


@pytest.fixture(scope="module")
def live():
    return core.SharedCoreRuntime("B0")


@pytest.fixture(scope="module")
def runtime_output():
    return core.build()


@pytest.fixture(scope="module")
def witnesses():
    return pilot.witness_records(pilot.load_seed())


def test_24_pinned_original_sources_content_actually_inspected(content):
    assert content["source_count"] == 24
    assert content["source_git_revision"] == pilot.REF
    assert content["source_seed_sha256"] == pilot.SEED_SHA256
    assert content["verified_original_git_content_and_claim_locations"] is True
    assert content["source_modality_counts"] == {
        "JSON_SCHEMA": 1, "MARKDOWN": 11, "PYTHON": 9,
        "TYPESCRIPT": 2, "WORKFLOW_YAML": 1,
    }


def test_no_source_claim_qualifies_formal_semantic_eligibility(content):
    assert content["unreviewed_semantic_eligibility_count"] == 24
    assert content["independent_eligibility_referee_qualified"] is False
    assert content["formal_60_20_source_set_selected"] is False
    assert content["gold_or_task_answers_generated"] is False
    assert content["navigation_arm_scores"] is None
    assert content["production_authority_changed"] is False
    assert all(
        x["semantic_eligibility"] == "NOT_ADJUDICATED"
        and x["accepted_authority"] == "NOT_INFERRED_FROM_SOURCE_CONTENT_OR_ROLE"
        and x["independent_source_referee"] == "NOT_ASSIGNED"
        for x in content["content_role_evidence"]
    )


def test_decisions_collection_has_per_decision_mixed_status_not_whole_file_currentness(content_by_path):
    v = content_by_path["docs/DECISIONS.md"]["source_observation"]
    assert v["structural_claim_type"] == "MULTI_DECISION_COLLECTION_NOT_ONE_STATUS"
    assert v["per_entry_decision_count"] >= 30
    assert len(v["distinct_reported_statuses"]) >= 2
    assert v["whole_document_current_authority_from_this_parser"] is False
    assert any(x["decision_id"] == "D-035" for x in v["decision_witnesses"])
    assert any(x["decision_id"] == "D-036" for x in v["decision_witnesses"])


def test_old_w5_accepted_status_is_distinct_from_production_j1(content_by_path):
    v = content_by_path[
        "docs/research/217_w5_t1_v02_controlled_subject_architecture_acceptance.md"
    ]["source_observation"]
    header = {row["field"]: row["source"]["raw_text"] for row in v["reported_metadata"]}
    assert "T1 ACCEPTED" in header["Status"]
    assert "W5 design result only" in header["Authority"]
    assert v["metadata_is_not_admitted_j1_or_currentness"] is True


def test_research_254_not_current_physical_selection(content_by_path):
    v = content_by_path[
        "docs/research/254_r7b_target_project_information_hierarchy_and_research218_supersession_candidate.md"
    ]["source_observation"]
    headers = {r["field"]: r["source"]["raw_text"] for r in v["reported_metadata"]}
    assert "OWNER DECISION REQUIRED" in headers["Status"]
    assert "NO PHYSICAL MIGRATION" in headers["Status"]


def test_architecture_overview_explicitly_not_governing(content_by_path):
    v = content_by_path["docs/ARCHITECTURE_PROGRAM_OVERVIEW.md"]["source_observation"]
    headers = {r["field"]: r["source"]["raw_text"] for r in v["reported_metadata"]}
    assert "NON-GOVERNING" in headers["Status"]
    assert v["metadata_is_not_admitted_j1_or_currentness"] is True


def test_specification_028_reports_subordinate_authority(content_by_path):
    v = content_by_path[
        "docs/specifications/028_v1_project_knowledge_architecture_implementation_and_migration_contract.md"
    ]["source_observation"]
    headers = {r["field"]: r["source"]["raw_text"] for r in v["reported_metadata"]}
    assert "IMPLEMENTATION PENDING" in headers["Status"]
    assert "It does not switch operational authority" in headers["Authority"]


@pytest.mark.parametrize("path", [
    "tools/project_knowledge/identity.py",
    "tools/project_knowledge/authority.py",
    "tools/project_knowledge/services/refresh.py",
    "tools/project_knowledge/services/generation.py",
    "src/ads_system/application/source_universe.py",
    "src/ads_system/infrastructure/retrieval/sqlite_fts.py",
    "tests/unit/test_project_knowledge_identity.py",
    "tests/unit/test_project_knowledge_refresh.py",
    "scripts/check_repository_integrity.py",
])
def test_python_content_parsed_as_code_without_conferring_coverage(content_by_path, path):
    v = content_by_path[path]["source_observation"]
    assert v["source_format"] == "PYTHON"
    assert v["source_parses"] is True
    assert v["top_level_declaration_count"] > 0
    assert v["realization_of_accepted_effect_proven_by_source"] is False
    assert v["test_result_proven_by_source"] is False
    if path.startswith("tests/"):
        assert v["structural_claim_type"] == "TEST_DECLARATIONS_NOT_EXECUTION"


@pytest.mark.parametrize("path", [
    "frontend/src/components/CockpitProjectMap.tsx",
    "frontend/src/components/MissingnessWorkspace.tsx",
])
def test_tsx_exports_not_claimed_as_executed_ui(content_by_path, path):
    v = content_by_path[path]["source_observation"]
    assert v["source_format"] == "TYPESCRIPT"
    assert v["exports"]
    assert v["running_ui_proven_by_source"] is False


def test_json_schema_declarations_not_accepted_effect(content_by_path):
    v = content_by_path[
        "schemas/project_knowledge/semantic_source.v1.schema.json"
    ]["source_observation"]
    assert v["schema_dialect"].endswith("2020-12/schema")
    assert "semantic_id" in v["property_names"]
    assert v["schema_is_accepted_governing_effect"] is False


def test_ci_workflow_definition_not_success_receipt(content_by_path):
    v = content_by_path[
        ".github/workflows/repository-integrity.yml"
    ]["source_observation"]
    assert v["source_format"] == "WORKFLOW_YAML"
    assert v["actual_provider_ci_run_proven_by_source"] is False
    assert any(x["raw_text"] == "jobs:" for x in v["definition_witnesses"])


def test_every_source_role_claim_has_exact_original_git_witness_line(content_by_path):
    roster = pilot.source_roster()
    for path, record in content_by_path.items():
        lines = pilot.git_blob(path, roster[path]).decode("utf8").splitlines()
        observation = record["source_observation"]
        points = []
        def walk(item):
            if isinstance(item, dict):
                if set(("line", "raw_text", "line_sha256")) <= set(item):
                    points.append(item)
                else:
                    for val in item.values():
                        walk(val)
            elif isinstance(item, list):
                for val in item:
                    walk(val)
        walk(observation)
        assert points, path
        for item in points:
            assert item["raw_text"] == lines[item["line"]-1]
            assert sha256(item["raw_text"].encode("utf8")).hexdigest() == item["line_sha256"]


def test_fake_source_sha_rejected_before_content_review(witnesses):
    row = deepcopy(witnesses[0])
    row["source_sha256"] = "0"*64
    raw = pilot.git_blob(row["source_path"], pilot.source_roster()[row["source_path"]])
    with pytest.raises(ValueError, match="EXACT_BLOB_SHA_MISMATCH"):
        audit.inspect_record(row, raw)


def test_invalid_python_syntax_rejected_as_source_definition(witnesses):
    row = deepcopy(next(w for w in witnesses if w["source_path"] ==
                        "tools/project_knowledge/identity.py"))
    raw = b"def broken(:\n"
    row["source_sha256"] = sha256(raw).hexdigest()
    row["line_count"] = 1
    with pytest.raises(ValueError, match="PYTHON_SYNTAX_INVALID"):
        audit.inspect_record(row, raw)


def test_runtime_has_only_bounded_public_source_core(live):
    assert live.common_contract_sha256 == (
        "33d3ab8fef047f55313ebdab0fb097389859953b8fed0eee5027e288e4e51bdb"
    )
    s = live.experimental_semantics()
    assert s["qualifying_j2_count"] == 1
    assert s["production_j2_j3_qualified"] is False
    assert s["independent_model_actor_authentication"] is False


@pytest.mark.parametrize("arm", ["B0", "B1", "B2", "B3", "B4"])
def test_each_label_exposes_same_actual_common_methods(arm):
    instance = core.SharedCoreRuntime(arm)
    sample = instance.read_source(
        "docs/research/217_w5_t1_v02_controlled_subject_architecture_acceptance.md",
        1, 4,
    )
    assert sample["line_data"][0]["text"].startswith("# Research 217")
    assert instance.literal_search("source", limit=3)
    assert instance.experimental_semantics()["qualifying_j2_count"] == 1
    assert instance.derived_orientation()["governing_truth_is_not_in_cache"] is True


@pytest.mark.parametrize("path", [
    "../../.git/config",
    "docs/DECISIONS.md/../../docs/CONTINUITY.md",
    "docs/nonexistent.md",
    "experiments/r0_p03_navigation_probe/v03_real_pk_delegated_s1_j3_lifecycle_result_v01.json",
])
def test_read_source_does_not_broaden_to_nonseed_or_private_files(live, path):
    with pytest.raises(ValueError, match="UNKNOWN_OR_FORBIDDEN_SOURCE_PATH"):
        live.read_source(path, 1, 1)


@pytest.mark.parametrize("start,end", [
    (0, 1), (2, 1), (1, 41), (-1, -1), (True, 2), (1, True),
    (1.0, 2), (1, 10000),
])
def test_bounded_source_excerpt_budget_rejects_invalid_ranges(live, start, end):
    with pytest.raises(ValueError, match="LINE_BUDGET_VIOLATION"):
        live.read_source("docs/DECISIONS.md", start, end)


def test_read_source_exact_bytes_and_line_provenance(live):
    result = live.read_source("docs/DECISIONS.md", 1, 4)
    assert result["source_ref"] == pilot.REF
    assert result["source_line_is_not_governing_acceptance"] is True
    raw = pilot.git_blob("docs/DECISIONS.md", pilot.source_roster()["docs/DECISIONS.md"])
    assert result["source_sha256"] == sha256(raw).hexdigest()
    for item in result["line_data"]:
        line = raw.decode("utf8").splitlines()[item["line"]-1]
        assert item["text"] == line
        assert item["line_sha256"] == sha256(line.encode("utf8")).hexdigest()


def test_read_outside_original_line_count_rejected(live):
    p = "schemas/project_knowledge/semantic_source.v1.schema.json"
    n = live.source_role_observation(p)
    # An enormous end is over the budget; use one line past the actual count.
    actual = next(row["line_count"] for row in live._sources if row["source_path"] == p)
    with pytest.raises(ValueError, match="LINE_OUTSIDE_ORIGINAL_SOURCE"):
        live.read_source(p, actual+1, actual+1)
    assert n["semantic_eligibility"] == "NOT_ADJUDICATED"


@pytest.mark.parametrize("limit", [0, 21, True, -4, 1.5])
def test_runtime_search_enforces_uniform_max_hits(live, limit):
    with pytest.raises(ValueError, match="LEXICAL_BUDGET_VIOLATION"):
        live.literal_search("source", limit=limit)


def test_actual_shared_api_requests_are_equal_but_not_distinct_arm_implementations(runtime_output):
    assert runtime_output["same_common_api_results_for_all_arm_labels"] is True
    assert runtime_output["same_common_request_counts_for_all_arm_labels"] is True
    assert runtime_output["production_or_actual_arm_runtime_parity_qualified"] is False
    assert runtime_output["b1_b2_b3_b4_additions_implemented"] is False
    hashes = {v["common_api_observation_sha256"]
              for v in runtime_output["per_arm_equal_common_api_probes"].values()}
    assert len(hashes) == 1


def test_delete_rebuild_ephemeral_derived_does_not_touch_source_or_j3(live):
    before = live.derived_orientation()
    source = live.read_source("docs/DECISIONS.md", 1, 1)
    semantic = live.experimental_semantics()
    live.drop_derived()
    assert live.derived_orientation() == before
    assert live.read_source("docs/DECISIONS.md", 1, 1) == source
    assert live.experimental_semantics() == semantic


def test_returned_sources_and_semantics_are_defensive_copies(live):
    path = "docs/research/217_w5_t1_v02_controlled_subject_architecture_acceptance.md"
    source = live.source_role_observation(path)
    source["semantic_eligibility"] = "FORGED_PASS"
    assert live.source_role_observation(path)["semantic_eligibility"] == "NOT_ADJUDICATED"
    s = live.experimental_semantics()
    s["production_j2_j3_qualified"] = True
    assert live.experimental_semantics()["production_j2_j3_qualified"] is False
    orientation = live.derived_orientation()
    orientation["authority_class"] = "GOVERNING"
    assert live.derived_orientation()["authority_class"].startswith("DERIVED_")


def test_invalid_arm_rejected():
    with pytest.raises(ValueError, match="UNKNOWN_ARM"):
        core.SharedCoreRuntime("B5")


def test_immutable_evidence_replay(content, runtime_output):
    assert json.loads(audit.OUTPUT.read_text("utf8")) == content
    assert json.loads(core.OUTPUT.read_text("utf8")) == runtime_output
