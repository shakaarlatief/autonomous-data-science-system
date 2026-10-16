"""Actual pinned source relations and synthetic negatives; no gold or scorer."""

import copy
import json
from pathlib import Path

import pytest

from experiments.r0_p03_navigation_probe import eligibility_mapping_candidate as mapping
from experiments.r0_p03_navigation_probe import role_frame_candidate as frame

REPO = Path(__file__).resolve().parents[2]


@pytest.fixture(scope="module")
def report():
    return mapping.build_assessment(REPO)


@pytest.fixture(scope="module")
def contract():
    return json.loads((REPO / "experiments/r0_p03_navigation_probe/common_substrate_contract_candidate.json").read_text("utf-8"))


def test_saved_report_reproducible_without_mutable_source_reads(report):
    path = REPO / "experiments/r0_p03_navigation_probe/eligibility_mapping_assessment_candidate.json"
    assert json.loads(path.read_text("utf-8")) == report == mapping.build_assessment(REPO)
    assert report["source_ref"] == frame.SOURCE_REF
    assert report["design_ref"] == "213e6db7d02debfbde37f8e45b4297849bc6089a"
    assert len(report["event_assessments"]) == 36
    assert {x["event_id"] for x in report["event_assessments"]} == {f"D-{i:03}" for i in range(1, 37)}
    assert len(report["code_population"]) == 89
    assert sum(x["source_path"].startswith("src/ads_system/") for x in report["code_population"]) == 35
    assert report["code_reference_relation_count"] == 22
    assert not {"tasks", "answers", "gold", "selected_twelve", "build_paths", "heldout_paths", "scores"}.intersection(report)


@pytest.mark.parametrize("ref", ["HEAD", mapping.DESIGN_REF, "0" * 40])
def test_changed_content_pin_rejected(ref):
    with pytest.raises(ValueError, match="exact content pin"):
        mapping.build_assessment(REPO, ref)


def test_owner_events_not_promoted_to_independent_information_needs(report):
    events = report["event_assessments"]
    assert all(x["independent_information_need"] == mapping.UNKNOWN for x in events)
    assert all(x["task_admission"].startswith("DEFER") for x in events)
    attested = [x for x in events if x["owner_origin_evidence"]]
    assert {x["event_id"] for x in attested} == {"D-035", "D-036"}
    assert all(x["owner_event_origin"].endswith("NOT_ORIGINAL_INFORMATION_NEED") for x in attested)
    assert all(v["independently_eligible_need_count"] is None for v in report["category_evidence"].values())


def test_category_witnesses_gaps_and_non_exhaustiveness_not_lexical_quotas(report):
    expected = {"cold_start_current_orientation": (6, 0), "impact_analysis_evolution": (4, 1),
                "exact_source_authority_recovery": (8, 1)}
    for category, (count, gaps) in expected.items():
        assert report["category_evidence"][category]["event_predicate_count"] == count
        assert report["category_evidence"][category]["explicit_gap_count"] == gaps
    gaps = [x for x in report["event_predicate_witnesses"] if x["status"] == "EXPLICIT_EVIDENCE_GAP"]
    assert all(x["event_id"] == "D-003" for x in gaps)
    assert "not preserved" in gaps[0]["closure"]["obligations"]["source_assertion"][0]["text"]
    assert report["known_gaps"]["whole_repository_impossibility"] == "NOT_DEMONSTRATED"


def test_cross_plane_links_are_typed_and_build_toolchain_not_relabelled(report):
    cross = report["category_evidence"]["cross_plane_discovery"]
    assert (cross["source_declared_product_links"], cross["distinct_contracts"], cross["distinct_components"]) == (14, 6, 13)
    relations = report["relation_audit"]
    assert sum(x["semantic_relation_family"] == "REFERENCE_ONLY_NOT_IMPLEMENTATION_EVIDENCE" for x in relations) == 5
    for relation in relations:
        if relation["semantic_relation_family"] == "REFERENCE_ONLY_NOT_IMPLEMENTATION_EVIDENCE":
            assert relation["cross_plane_relevance"] == "NOT_ESTABLISHED_OR_WITHIN_PROJECT"
        if relation["target_reference"].startswith("docs/specifications/003_"):
            assert relation["contract_scope_review"]["role"] == "PROJECT_BUILD_ENVIRONMENT"
            assert relation["cross_plane_relevance"] == "NOT_ESTABLISHED_OR_WITHIN_PROJECT"
        if relation["source_reference"].startswith("tools/project_knowledge/"):
            assert relation["cross_plane_relevance"] == "NOT_ESTABLISHED_OR_WITHIN_PROJECT"
    assert report["known_gaps"]["Research500_cross_plane_stratification"].startswith("J1_J2_J3_PROJECT_CONTROL")


def test_docstring_intent_dependency_reference_and_non_docstring_separated():
    lines = ['"""This module implements Specification 004.',
             'An example in Specification 012.', '"""',
             '# Implements Specification 023. Product cross-plane.',
             'unrelated = "This module implements Specification 028"',
             'raise RuntimeError("AST inspection must not execute this")',
             'def run():', '    """Operations required by Specification 004 services."""']
    refs = mapping.docstring_references(lines)
    assert [(r["line"], r["kind"]) for r in refs] == [
        (1, "DECLARED_IMPLEMENTATION_INTENT"), (2, "REFERENCE_ONLY_NOT_IMPLEMENTATION_EVIDENCE"),
        (8, "DECLARED_CONTRACT_DEPENDENCY")]
    assert mapping.docstring_references(['"""Product cross-plane discovery."""']) == []


def test_negation_hypothesis_and_example_cannot_be_implementation_intent():
    for clause in ["does not implement", "might implement", "Example: implements"]:
        ref, = mapping.docstring_references([f'"""This module {clause} Specification 004."""'])
        assert ref["kind"] == "REFERENCE_ONLY_NOT_IMPLEMENTATION_EVIDENCE"


def test_source_owned_implementation_of_is_not_lost_as_generic_reference():
    ref, = mapping.docstring_references(['"""Filesystem implementation of Specification 023."""'])
    assert ref["kind"] == "DECLARED_IMPLEMENTATION_INTENT"


def test_explicit_range_is_one_declaration_not_three_independent_needs(report):
    refs = mapping.docstring_references(['"""Adapters implementing Specifications 001-003."""'])
    assert len(refs) == 1 and refs[0]["targets"] == [("specification", i) for i in (1, 2, 3)]
    assert mapping.numbered_references("Foundations 017-020 and Specification 004") == [
        ("foundation", i) for i in (17, 18, 19, 20)] + [("specification", 4)]
    with pytest.raises(ValueError):
        mapping.numbered_references("Specifications 001-999")
    assert report["category_evidence"]["cross_plane_discovery"]["independently_eligible_need_count"] is None


def test_typed_supersession_endpoint_closure_not_arbitrary_graph_expansion(report):
    relations = report["relation_audit"]
    lifecycle = [x for x in relations if x["semantic_relation_family"] == "SOURCE_DECLARED_SCOPED_SUPERSESSION"]
    assert len(lifecycle) == 8
    assert {x["target_reference"] for x in lifecycle if x["source_reference"] == "D-011"} == {
        "D-028", "D-029", "D-030", "D-031", "D-032", "D-033", "D-035"}
    assert all(x["closure"]["local_witnesses_present"] for x in lifecycle)
    assert all(x["closure"]["distinct_witness_path_count"] == 1 for x in lifecycle)
    assert all(x["closure"]["minimum_task_closure"] is None for x in lifecycle)
    assert not any(x["source_reference"] == "D-035" and x["target_reference"] == "D-036" for x in lifecycle)


def test_local_witness_bundles_do_not_certify_full_normative_closure(report):
    relations = report["relation_audit"]
    code = [x for x in relations if x["source_reference"].startswith(("src/", "tools/"))]
    assert all(x["closure"]["local_witnesses_present"] for x in code)
    assert all(x["full_normative_or_task_closure"] == mapping.UNKNOWN for x in code)
    assert all(2 <= x["closure"]["distinct_witness_path_count"] <= 3 for x in code)
    interchange = next(x for x in code if x["source_reference"].startswith("src/ads_system/infrastructure/interchange/knowledge_bundle.py"))
    assert len(interchange["normative_header_dependencies"]) == 5
    assert all(x["status"] == "EXISTS_APPLICABILITY_NOT_ADJUDICATED" for x in interchange["normative_header_dependencies"])
    assert not mapping.closure_bundle({})["local_witnesses_present"]
    missing = mapping.closure_bundle({"assertion": [code[0]["source_provenance"][0]], "authority": []})
    assert not missing["local_witnesses_present"] and missing["missing_obligations"] == ["authority"]


def test_source_identity_subject_scope_and_currentness_not_v03_acceptance(report):
    common = report["neutral_common_mapping"]
    effects = {x["effect_reference"]["source_record"]: x for x in common["governing_effects"]}
    assert effects["D-035"]["exact_subject_reference"]["literal_selected_target"] == "PKA-CANDIDATE-01"
    assert effects["D-036"]["exact_subject_reference"]["literal_selected_target"] == "THIN_CENTRED_HYBRID_V03"
    assert effects["D-036"]["lineage_reference"]["relation"].endswith("NOT_AUTOMATIC_SUPERSESSION")
    assert all(x["effect_reference"]["accepted_v03_effect_id"] == mapping.UNKNOWN for x in effects.values())
    stale = common["derived_orientation"]["staleness_visible"]
    assert (stale["legacy_checkpoint"], stale["pinned_routing_checkpoint"]) == (564, 895)
    assert stale["legacy_core"] == "STALE_CHECKPOINT_MISMATCH"


def test_incumbent_structured_identity_and_derived_class_preserved_as_source_facts(report):
    records = {r["id"]: r for r in report["neutral_common_mapping"]["records"]}
    old = records["D-035"]["source_declared_identity_and_authority_class"]
    assert old["literal_declaration"]["semantic_id"] == "D-035"
    assert old["literal_declaration"]["profile"] == "semantic_source.v1"
    assert old["literal_declaration"]["authority_class"] == "canonical"
    assert not old["accepted_v03_effect"]
    assert records["D-036"]["source_declared_identity_and_authority_class"]["literal_declaration"] == mapping.UNKNOWN
    assert records["J3_IDENTITY_INDEX"]["source_declared_identity_and_authority_class"]["literal_declaration"]["authority_class"] == "derived"


def test_full_common_shape_has_unknowns_and_equal_views_not_runtime_parity(report, contract):
    common = report["neutral_common_mapping"]
    assert len(common["records"]) == 75
    assert mapping.common_mapping_issues(common, contract) == []
    assert report["common_mapping_issues"] == report["equal_view_issues"] == []
    assert report["runtime_arm_parity"] == "NOT_EXECUTED_OR_QUALIFIED"
    assert common["completion"]["state"] == common["j2_coverage"]["accepted_coverage"] == mapping.UNKNOWN
    assert common["evidence_receipts"]["verified_execution_result"] == mapping.UNKNOWN
    for rec in common["records"]:
        assert rec["natural_owner"]["canonical_fact_owner"] == mapping.UNKNOWN
        assert rec["source_eligibility"]["status"].startswith("PENDING")
        assert not rec["governing"] and not rec["accepted_j2_coverage"]


def test_audit_mentions_and_category_labels_do_not_become_shared_navigation(report, contract):
    common = report["neutral_common_mapping"]
    assert len(report["relation_audit"]) == 30
    assert len(common["shared_relations"]) == 8
    assert report["audit_only_relation_count"] == 22
    assert report["common_relation_admission"].endswith("CODE_TO_CONTRACT_B0_VS_B2_UNQUALIFIED")
    assert all(r["semantic_relation_family"] == "SOURCE_DECLARED_SCOPED_SUPERSESSION"
               for r in common["shared_relations"])
    assert all(set(r) == set(contract["exact_record_contract"]["shared_relation"]["required"])
               for r in common["shared_relations"])
    mention = next(r for r in report["relation_audit"] if r["semantic_relation_family"] == "REFERENCE_ONLY_NOT_IMPLEMENTATION_EVIDENCE")
    declared = next(r for r in report["relation_audit"] if r["semantic_relation_family"] == "DECLARED_IMPLEMENTATION_INTENT")
    for candidate in (mention, declared):
        view = copy.deepcopy(common)
        view["shared_relations"].append({k: candidate[k] for k in contract["exact_record_contract"]["shared_relation"]["required"]})
        assert "UNQUALIFIED_RELATION_IN_B0_COMMON_GRAPH" in mapping.common_mapping_issues(view, contract)
        if candidate is mention:
            assert "REFERENCE_ONLY_AUDIT_LINK_IN_COMMON_RELATIONS" in mapping.common_mapping_issues(view, contract)
    view = copy.deepcopy(common)
    view["category_evidence"] = report["category_evidence"]
    assert "ARM_NAVIGATION_IN_SHARED_VIEW" in mapping.common_mapping_issues(view, contract)


@pytest.mark.parametrize("section", ["shared_relations", "lexical_full_text", "j2_coverage", "derived_orientation"])
def test_full_b0_sections_cannot_disappear(report, contract, section):
    view = copy.deepcopy(report["neutral_common_mapping"])
    del view[section]
    assert "MISSING_COMMON_SECTION:" + section in mapping.common_mapping_issues(view, contract)


def test_false_acceptance_and_mismatched_carrier_provenance_rejected(report, contract):
    view = copy.deepcopy(report["neutral_common_mapping"])
    rec = view["records"][0]
    rec.update(governing=True, status="SOURCE_REVIEWED_ACCEPTED_GOVERNING", accepted_effect_reference="fake")
    assert "ENGINEERING_MAPPING_CANNOT_CREATE_ACCEPTANCE" in mapping.common_mapping_issues(view, contract)
    rec["governing"] = False
    rec["accepted_j2_coverage"] = True
    rec.update(status="SOURCE_REVIEWED_ACCEPTED_J2", source_owned_coverage_reference="fake")
    assert "ENGINEERING_MAPPING_CANNOT_CREATE_ACCEPTANCE" in mapping.common_mapping_issues(view, contract)
    rec["git_blob_oid"] = "0" * 40
    assert "CARRIER_PROVENANCE_MISMATCH" in mapping.common_mapping_issues(view, contract)


def test_forged_effect_identity_and_status_rejected(report, contract):
    view = copy.deepcopy(report["neutral_common_mapping"])
    view["governing_effects"][0]["effect_reference"]["accepted_v03_effect_id"] = "fake"
    view["governing_effects"][0]["governing_status"] = "CURRENT_OPERATIONAL"
    issues = mapping.common_mapping_issues(view, contract)
    assert "UNSUPPORTED_V03_ACCEPTANCE_ID" in issues
    assert "GOVERNING_STATUS_SOURCE_MISMATCH" in issues


def test_all_contract_arm_additions_blocked_by_reused_guard(report, contract):
    forbidden = {key for arm in contract["comparison_augmentations"].values() for key in arm["additional_signals"]}
    assert forbidden.issubset(frame.NAVIGATION_KEYS)
    for key in forbidden:
        view = copy.deepcopy(report["neutral_common_mapping"])
        view["records"][0][key] = ["synthetic"]
        assert "ARM_NAVIGATION_IN_SHARED_VIEW" in mapping.common_mapping_issues(view, contract)


@pytest.mark.parametrize("damage", ["quote", "blob", "pin", "range"])
def test_actual_source_witness_verification_rejects_tampering(report, damage):
    view = copy.deepcopy(report["neutral_common_mapping"])
    roster = frame.committed_paths(REPO, frame.SOURCE_REF, ())
    paths = set(view["lexical_full_text"]["source_manifest"])
    texts = frame.pinned_texts(REPO, roster, paths)
    assert mapping.provenance_issues(view, roster, texts) == []
    span = view["records"][0]["source_provenance"][0]
    if damage == "quote":
        span["text"] += " unsupported"
    elif damage == "blob":
        span["git_blob_oid"] = "0" * 40
    elif damage == "pin":
        span["git_commit"] = mapping.DESIGN_REF
    else:
        span["line_end"] = 999999
    assert mapping.provenance_issues(view, roster, texts) == ["SOURCE_WITNESS_MISMATCH"]
