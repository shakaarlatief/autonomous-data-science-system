"""Non-scored source-provenance and role-hint checks for the revised P03 frame.

These tests explicitly do not qualify semantic authority, independent legacy gold,
sample representativeness, arm comparison, or fresh-agent scoring.
"""

from __future__ import annotations

import importlib.util
import json
import re
import subprocess
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parents[2]
MODULE = REPO / "experiments/r0_p03_navigation_probe/role_frame_candidate.py"
SPECIMEN = REPO / "experiments/r0_p03_navigation_probe/neutral_substrate_specimen_candidate.json"
_spec = importlib.util.spec_from_file_location("r0_p03_role_frame_candidate", MODULE)
assert _spec is not None and _spec.loader is not None
frame = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(frame)


@pytest.fixture(scope="module")
def census():
    return frame.build_role_census(REPO, frame.SOURCE_REF)


def test_exact_git_ref_and_identical_read_only_census(census):
    assert census == frame.build_role_census(REPO, frame.SOURCE_REF)
    assert census["source_ref"] == frame.SOURCE_REF
    assert census["classification"] == "UNFROZEN_ROLE_FRAME_CENSUS_NONSCORING"
    assert re.fullmatch(r"[a-f0-9]{64}", census["included_path_blob_digest_sha256"])
    with pytest.raises(ValueError):
        frame.committed_paths(REPO, "HEAD")
    with pytest.raises(ValueError):
        frame.committed_paths(REPO, "../branch")


def test_audited_counts_are_exact_ref_file_counts(census):
    assert census["tracked_path_count"] == 3304
    assert census["candidate_text_path_count"] == 2883
    roles = census["path_family_counts"]["REVIEW"]
    assert roles["project_tool_realizer_candidate"] == 54
    assert roles["machine_schema_realization"] == 11
    assert roles["verification_or_test_carrier"] == 116
    assert roles["derived_project_knowledge_view"] == 21
    assert roles["incumbent_project_knowledge_source"] == 10
    assert census["path_family_counts"]["AUXILIARY_NOT_SAMPLED"]["historical_fixture_or_probe"] == 380


def test_experiment_design_leakage_flagged_and_historical_evidence_remains():
    assert frame.leakage_reason("docs/research/557_r0_p03_common_substrate_and_source_census_candidate.md")
    assert frame.leakage_reason("docs/checkpoints/895_r0_p03_owner_option_a_legacy_gold_amendment_and_claude_reconciliation.md")
    assert frame.leakage_reason("docs/model_collaboration/threads/MC-0030/messages/062_claude_r0_p03_prefreeze_comparator_design_critique.md")
    assert frame.leakage_reason("experiments/r0_p03_navigation_probe/role_frame_candidate.py")
    assert frame.leakage_reason("docs/research/217_w5_t1_v02_controlled_subject_architecture_acceptance.md") is None
    assert frame.leakage_reason("docs/checkpoints/192_specification_022_incomplete_result_preservation_promotion_candidate.md") is None


def test_roles_are_review_hints_not_authority_verdicts(census):
    roles = census["path_family_counts"]["REVIEW"]
    for expected in ("governing_decision_carrier", "research_proposal_or_result",
                     "project_tool_realizer_candidate", "verification_or_test_carrier",
                     "machine_schema_realization", "derived_project_knowledge_view",
                     "product_or_cross_plane_realizer", "operational_routing_source"):
        assert expected in roles
    assert frame.proposed_family("docs/project_knowledge/generated/identity_index.json")[2] == "DERIVED_NOT_GOVERNING"
    assert frame.proposed_family("tools/project_knowledge/authority.py")[2] == "NOT_PROVEN_COVERAGE"
    assert frame.proposed_family("docs/research/254_r7b_target_project_information_hierarchy_and_research218_supersession_candidate.md")[2] == "ACCEPTANCE_CURRENTNESS_REVIEW"
    assert census["lifecycle_review_hints_by_role"]["derived_project_knowledge_view"] == {"DERIVED_NOT_GOVERNING": 21}
    assert "No selected build or heldout" in " ".join(census["limitations"])


def test_nontext_and_auxiliary_do_not_silently_become_gold(census):
    assert census["excluded_or_withheld_counts"]["NON_TEXT_OR_UNSUPPORTED"] > 0
    assert census["excluded_or_withheld_counts"]["P03_RESEARCH_DESIGN"] >= 4
    assert census["excluded_or_withheld_counts"]["P03_MODEL_DESIGN_MESSAGE"] >= 3
    assert census["path_family_counts"]["REVIEW_WITH_CONTAMINATION_CONTROL"]["navigation_or_orientation"] == 4
    assert "gold_answers" not in census
    assert "heldout_paths" not in census
    assert "selected_build" not in census


def test_specimen_is_ten_source_bound_records_without_scoring():
    specimen = json.loads(SPECIMEN.read_text("utf-8"))
    assert specimen["source_ref"] == frame.SOURCE_REF
    assert len(specimen["records"]) == 10
    assert specimen["state"].startswith("UNFROZEN_NONSCORING_TASK_OWNER_AUTHORED")
    assert "scoring" not in specimen
    assert "gold_answers" not in specimen
    assert "selected_heldout" not in specimen
    ids = {rec["id"] for rec in specimen["records"]}
    assert {"GOV_D035", "GOV_D036", "INCUMBENT_SPEC028",
            "PROPOSAL_R254", "J2_AUTHORITY_MODULE", "J2_SEMANTIC_SCHEMA",
            "J2_AUTHORITY_TEST", "J3_IDENTITY_INDEX", "J3_STALE_CORE",
            "ROUTING_895"} == ids
    tracked = frame.committed_paths(REPO, frame.SOURCE_REF)
    for rec in specimen["records"]:
        assert tracked[rec["source_path"]] == rec["git_blob_oid"]
        content = subprocess.run(
            ["git", "show", frame.SOURCE_REF + ":" + rec["source_path"]],
            cwd=REPO, capture_output=True, encoding="utf-8", check=True,
        ).stdout.splitlines()
        assert rec["line_start"] == rec["line_end"]
        assert content[rec["line_start"] - 1] == rec["exact_source_line"]


def test_specimen_currentness_and_negative_provenance_witness():
    d = {r["id"]: r for r in json.loads(SPECIMEN.read_text("utf-8"))["records"]}
    assert d["GOV_D036"]["status"] == "SELECTED_SUCCESSOR_NOT_OPERATIONAL"
    assert d["INCUMBENT_SPEC028"]["status"] == "INCUMBENT_OPERATIONAL_CONTEXT_AS_IDENTIFIED_BY_D036"
    assert d["PROPOSAL_R254"]["status"] == "CANDIDATE_NOT_GOVERNING_TARGET"
    assert d["J3_IDENTITY_INDEX"]["status"].startswith("DERIVED_NONAUTHORITATIVE")
    assert d["J3_STALE_CORE"]["status"] == "DERIVED_STALE_RELATIVE_TO_ROUTING_895"
    assert '"checkpoint": 564' in d["J3_STALE_CORE"]["exact_source_line"]
    assert '"current_checkpoint": 895' in d["ROUTING_895"]["exact_source_line"]


def test_synthetic_j2_is_not_deployed_or_authoritative():
    specimen = json.loads(SPECIMEN.read_text("utf-8"))
    assert len(specimen["synthetic_relations"]) == 1
    edge = specimen["synthetic_relations"][0]
    assert edge["status"] == "SYNTHETIC_V03_ANALOGUE_NOT_GOVERNING_J2"
    assert "tools/project_knowledge/" in edge["source_line"]
    assert "No REALIZES/COVERS acceptance" in edge["not_claimed"]
    assert len(specimen["negative_assertions"]) >= 3
    assert "No" not in specimen["source_ref"]
