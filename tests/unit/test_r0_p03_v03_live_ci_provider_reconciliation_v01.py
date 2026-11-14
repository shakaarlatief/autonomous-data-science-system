"""Adversarial tests for real GitHub check/job/workflow source disagreement.

These assertions are strictly about source status reconciliation. The live
GitHub reads were performed through the connected provider API in the owning
conversation; this local JSON relay is not provider-authenticated proof.
"""
from __future__ import annotations

from copy import deepcopy
from hashlib import sha256
import subprocess

import pytest

from experiments.r0_p03_navigation_probe import (
    v03_live_ci_provider_reconciliation_v01 as probe,
)


@pytest.fixture(scope="module")
def original():
    return probe.source_relay()


@pytest.fixture(scope="module")
def derived():
    return probe.build()


def clone(original):
    return deepcopy(original)


def selected(source):
    return next(c for c in source["ref_check_runs"] if c["id"] == probe.CHECK_ID)


def selected_job(source):
    return next(j for j in source["workflow_jobs"] if j["id"] == probe.CHECK_ID)


def become_complete(source):
    """Hypothetical provider correction, not an authenticated update."""
    source = clone(source)
    source["check_run"]["status"] = "completed"
    selected(source)["status"] = "completed"
    selected_job(source)["status"] = "completed"
    return source


def test_actual_git_943_ancestry_rechecked_not_ci_issuer():
    assert probe.recheck_real_git() == {"commit": probe.COMMIT, "parent": probe.PARENT}


def test_original_relay_has_fixed_untrusted_role_and_no_governing_class(original):
    assert original["source_role"] == probe.SOURCE_ROLE
    assert original["source_authentication_from_copied_file"] is False
    assert original["record_is_governing"] is False
    assert original["source_credential_server_owned"] is True
    assert original["repository_full_name"] == probe.REPOSITORY
    assert original["target_git_sha"] == probe.COMMIT


def test_actual_source_check_workflow_job_and_steps_disagree(original):
    check = original["check_run"]
    job = selected_job(original)
    run = original["workflow_run"]
    assert (check["status"], check["conclusion"]) == ("in_progress", "success")
    assert (job["status"], job["conclusion"]) == ("in_progress", "success")
    assert check["completed_at"] and job["completed_at"]
    assert (run["status"], run["conclusion"]) == ("completed", "success")
    assert len(original["steps"]) == 5
    assert all(s["status"] == "completed" and s["conclusion"] == "success"
               for s in original["steps"])


def test_actual_live_943_anomaly_retains_seven_completed_success_one_conflict(original):
    x = probe.assess(original, probe.COMMIT)
    assert x.coherence == probe.Coherence.SOURCE_REPORTED_CONTRADICTION
    assert x.checked_ref_count == 8
    assert x.completed_success_count == 7
    assert x.completed_failure_count == 0
    assert x.conflicting_check_ids == (probe.CHECK_ID,)
    assert "NONTERMINAL_CHECK_WITH_TERMINAL_CONCLUSION" in x.reasons
    assert "NONTERMINAL_JOB_HAS_COMPLETED_AT" in x.reasons
    assert "COMPLETED_WORKFLOW_CONFLICTS_WITH_NONTERMINAL_JOB" in x.reasons


def test_actual_source_identity_coherence_distinct_from_status_consistency(original):
    assert original["check_run"]["id"] == probe.CHECK_ID
    assert original["workflow_run"]["id"] == probe.RUN_ID
    assert original["check_run"]["check_suite_id"] == original["workflow_run"]["check_suite_id"]
    assert selected_job(original)["run_id"] == probe.RUN_ID
    assert selected(original)["head_sha"] == probe.COMMIT
    assert selected(original)["app_slug"] == "github-actions"


def test_hypothetical_corrected_check_status_is_coherent_but_untrusted(original):
    modified = become_complete(original)
    x = probe.assess(modified, probe.COMMIT)
    assert x.coherence == probe.Coherence.SOURCE_REPORTED_COMPLETE_SUCCESS
    assert x.completed_success_count == 8
    assert x.independent_provider_authentication is False
    assert x.model_or_connector_identity_authenticated is False
    assert x.governing_j2_relational_qualified is False
    assert x.governing_j3_complete is False


def test_tampered_false_green_copy_does_not_create_authenticity(original):
    modified = become_complete(original)
    assert probe.assess(modified, probe.COMMIT).independent_provider_authentication is False
    assert probe.assess(original, probe.COMMIT).coherence == probe.Coherence.SOURCE_REPORTED_CONTRADICTION


def test_old_green_942_not_admitted_for_target_943(original):
    assert probe.assess(original, "e29329b3097b593a917a386d33f900a3cf97b193").coherence == probe.Coherence.REJECT_WRONG_SHA


@pytest.mark.parametrize("source_override", [None, "", "a" * 40, "0" * 40])
def test_wrong_or_absent_presented_commit_rejected(original, source_override):
    changed = clone(original)
    changed["target_git_sha"] = source_override
    assert probe.assess(changed, probe.COMMIT).coherence == probe.Coherence.REJECT_WRONG_SHA


@pytest.mark.parametrize("field,value", [
    ("head_sha", "1" * 40),
    ("check_suite_id", 123),
    ("id", 123),
    ("app_id", 123),
    ("app_slug", "malicious-issuer"),
])
def test_wrong_github_check_source_binding_rejected(original, field, value):
    altered = clone(original)
    altered["check_run"][field] = value
    assert probe.assess(altered, probe.COMMIT).coherence == probe.Coherence.REJECT_UNTRUSTED_SOURCE_SHAPE


@pytest.mark.parametrize("field,value", [
    ("head_sha", "1" * 40),
    ("id", 345),
    ("run_attempt", 2),
    ("event", "workflow_dispatch"),
    ("actor_login", ""),
])
def test_wrong_workflow_source_binding_rejected(original, field, value):
    altered = clone(original)
    altered["workflow_run"][field] = value
    assert probe.assess(altered, probe.COMMIT).coherence == probe.Coherence.REJECT_UNTRUSTED_SOURCE_SHAPE


@pytest.mark.parametrize("field,value", [
    ("head_sha", "1" * 40),
    ("app_id", 234),
    ("app_slug", "fake-issuer"),
])
def test_wrong_check_in_complete_ref_list_rejected(original, field, value):
    altered = clone(original)
    altered["ref_check_runs"][0][field] = value
    assert probe.assess(altered, probe.COMMIT).coherence == probe.Coherence.HOLD_MISSING


@pytest.mark.parametrize("field,value", [
    ("run_id", 123),
    ("run_attempt", 2),
])
def test_wrong_job_run_association_rejected(original, field, value):
    altered = clone(original)
    selected_job(altered)[field] = value
    assert probe.assess(altered, probe.COMMIT).coherence == probe.Coherence.HOLD_MISSING


def test_missing_ref_checks_not_mislabeled_pass(original):
    altered = clone(original)
    altered["ref_check_runs"].pop()
    assert probe.assess(altered, probe.COMMIT).coherence == probe.Coherence.HOLD_MISSING


def test_duplicate_check_id_and_name_not_counted_twice(original):
    for field in ("id", "name"):
        altered = clone(original)
        altered["ref_check_runs"][0][field] = altered["ref_check_runs"][1][field]
        assert probe.assess(altered, probe.COMMIT).coherence == probe.Coherence.HOLD_MISSING


def test_duplicate_workflow_job_not_falsely_counted(original):
    altered = clone(original)
    altered["workflow_jobs"][1]["id"] = altered["workflow_jobs"][0]["id"]
    assert probe.assess(altered, probe.COMMIT).coherence == probe.Coherence.HOLD_MISSING


def test_missing_selected_check_or_job_is_not_success(original):
    x = clone(original)
    x["ref_check_runs"][0]["id"] = 555555
    assert probe.assess(x, probe.COMMIT).coherence == probe.Coherence.HOLD_MISSING
    x = clone(original)
    selected_job(x)["id"] = 555555
    assert probe.assess(x, probe.COMMIT).coherence == probe.Coherence.HOLD_MISSING


def test_list_and_specific_check_status_disagreement_is_explicit_conflict(original):
    altered = clone(original)
    selected(altered)["status"] = "completed"
    x = probe.assess(altered, probe.COMMIT)
    assert x.coherence == probe.Coherence.SOURCE_REPORTED_CONTRADICTION
    assert x.conflicting_check_ids == (probe.CHECK_ID,)
    assert "SAME_CHECK_ID_CONTRADICTORY_ENDPOINT_FIELDS" in x.reasons


def test_job_endpoint_disagrees_with_check_not_majority_voted(original):
    altered = clone(original)
    selected_job(altered)["status"] = "completed"
    assert probe.assess(altered, probe.COMMIT).coherence == probe.Coherence.SOURCE_REPORTED_CONTRADICTION


def test_completed_workflow_can_not_override_in_progress_child_job(original):
    altered = clone(original)
    altered["check_run"]["conclusion"] = None
    selected(altered)["conclusion"] = None
    selected_job(altered)["conclusion"] = None
    altered["check_run"]["completed_at"] = None
    selected_job(altered)["completed_at"] = None
    x = probe.assess(altered, probe.COMMIT)
    assert x.coherence == probe.Coherence.SOURCE_REPORTED_CONTRADICTION
    assert "COMPLETED_WORKFLOW_CONFLICTS_WITH_NONTERMINAL_JOB" in x.reasons


def test_source_in_progress_without_success_fields_and_parent_pending_stays_hold(original):
    altered = clone(original)
    altered["workflow_run"]["status"] = "in_progress"
    altered["workflow_run"]["conclusion"] = None
    altered["check_run"]["conclusion"] = None
    altered["check_run"]["completed_at"] = None
    selected(altered)["conclusion"] = None
    selected_job(altered)["conclusion"] = None
    selected_job(altered)["completed_at"] = None
    assert probe.assess(altered, probe.COMMIT).coherence == probe.Coherence.HOLD_INCOMPLETE


def test_repaired_complete_source_one_failed_job_does_not_pass(original):
    altered = become_complete(original)
    altered["check_run"]["conclusion"] = "failure"
    selected(altered)["conclusion"] = "failure"
    selected_job(altered)["conclusion"] = "failure"
    altered["workflow_run"]["conclusion"] = "failure"
    x = probe.assess(altered, probe.COMMIT)
    assert x.coherence == probe.Coherence.SOURCE_REPORTED_FAILURE
    assert x.completed_failure_count == 1


def test_unrelated_workflow_failure_not_conflated_with_selected_run(original):
    altered = become_complete(original)
    another = next(v for v in altered["ref_check_runs"] if v["id"] != probe.CHECK_ID
                   and not v["name"].startswith("validate-current-routing"))
    another["conclusion"] = "failure"
    x = probe.assess(altered, probe.COMMIT)
    assert x.coherence == probe.Coherence.SOURCE_REPORTED_FAILURE
    assert x.completed_failure_count == 1


def test_steps_failure_contradicts_reported_success(original):
    altered = become_complete(original)
    altered["steps"][0]["conclusion"] = "failure"
    x = probe.assess(altered, probe.COMMIT)
    assert x.coherence == probe.Coherence.SOURCE_REPORTED_CONTRADICTION
    assert "SUCCESSFUL_JOB_HAS_FAILED_STEP" in x.reasons


def test_steps_still_running_cannot_be_overridden_by_workflow_success(original):
    altered = become_complete(original)
    altered["steps"][0]["status"] = "in_progress"
    altered["steps"][0]["conclusion"] = None
    assert probe.assess(altered, probe.COMMIT).coherence == probe.Coherence.HOLD_INCOMPLETE


@pytest.mark.parametrize("key,value", [
    ("record_is_governing", True),
    ("source_authentication_from_copied_file", True),
    ("source_role", "GITHUB_SIGNED_PROOF"),
    ("source_credential_server_owned", False),
    ("provider_auth_mode_reported", "unknown"),
    ("repository_full_name", "foreign/repo"),
])
def test_metadata_can_never_elevate_relay_authority(original, key, value):
    altered = clone(original)
    altered[key] = value
    assert probe.assess(altered, probe.COMMIT).coherence == probe.Coherence.REJECT_UNTRUSTED_SOURCE_SHAPE


def test_proof_field_injection_fails_closed(original):
    altered = clone(original)
    altered["model_identity_authenticated"] = True
    assert probe.assess(altered, probe.COMMIT).coherence == probe.Coherence.REJECT_UNTRUSTED_SOURCE_SHAPE


def test_any_embedded_provider_signature_field_is_not_accepted(original):
    altered = clone(original)
    altered["check_run"]["signed_by_github"] = True
    assert probe.assess(altered, probe.COMMIT).coherence == probe.Coherence.REJECT_UNTRUSTED_SOURCE_SHAPE


def test_not_even_a_tampered_copy_becomes_governing_j2_j3(original):
    for specimen in (original, become_complete(original)):
        outcome = probe.assess(specimen, probe.COMMIT)
        assert outcome.independent_provider_authentication is False
        assert outcome.model_or_connector_identity_authenticated is False
        assert outcome.governing_j2_relational_qualified is False
        assert outcome.governing_j3_complete is False


def test_non_mapping_source_does_not_throw_or_gain_admission():
    assessment = probe.assess(None, probe.COMMIT)
    assert assessment.coherence == probe.Coherence.REJECT_UNTRUSTED_SOURCE_SHAPE


def test_pinned_source_bytes_and_git_platform_neutral_attributes():
    assert sha256(probe.SOURCE.read_bytes()).hexdigest() == probe.SOURCE_SHA256
    for path in (probe.SOURCE, probe.RESULT):
        rel = path.relative_to(probe.ROOT).as_posix()
        attr = subprocess.check_output(
            ["git", "check-attr", "text", "--", rel],
            cwd=probe.ROOT, text=True, encoding="utf8",
        ).strip()
        assert attr == f"{rel}: text: unset"
        assert b"\r\n" not in path.read_bytes()


def test_derived_result_preserves_exact_status_and_formal_gates(derived):
    assert derived["source_status"] == probe.Coherence.SOURCE_REPORTED_CONTRADICTION
    assert derived["source_reported_completed_success_count"] == 7
    assert derived["source_reported_completed_failure_count"] == 0
    assert derived["source_reported_total_checks"] == 8
    assert derived["all_five_steps_source_reported_complete_success"] is True
    assert derived["parent_workflow_source_reported_completed_success"] is True
    assert derived["offline_copy_is_provider_signed"] is False
    assert derived["independent_model_session_identity_authenticated"] is False
    assert derived["governing_j2_relational_admissions_added"] == 0
    assert derived["historical_e01_j3"] == "HOLD"
    assert derived["formal_r0_p03_score"] is None
    assert derived["physical_target_selected"] is False


def test_observation_scope_has_finite_stop_not_more_mock_auth(derived):
    assert derived["suggested_next_step"].startswith("FINITELY_STOP_COPY_PROBES")
    assert derived["self_authenticating_trust_root_created"] is False


def test_result_is_immutable_derived_source_only(derived):
    assert __import__("json").loads(probe.RESULT.read_text("utf8")) == derived
