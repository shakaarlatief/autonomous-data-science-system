"""Adversarial tests of the actual co-committed, non-governing J2 event.

A genuine git commit verifies source bytes, path, and parent; it cannot prove
actor credentials, provider API, an accepted governing effect, or a qualified
COVERS relationship. Synthetic mutations below are never published facts.
"""
from copy import deepcopy
from hashlib import sha256
import json
import subprocess

import pytest

from experiments.r0_p03_navigation_probe import (
    v03_forward_j2_at_action_evidence_probe_v01 as probe,
)


@pytest.fixture(scope="module")
def event():
    return probe.original_commit_data()


@pytest.fixture(scope="module")
def projection():
    return probe.build()


def test_real_single_file_git_commit_with_expected_parent_and_source(event):
    raw, observed = event
    assert observed["event_commit"] == probe.ACTION_COMMIT
    assert observed["commit_parent"] == probe.ACTION_PARENT
    assert observed["changed_paths"] == ["A\t" + probe.ACTION_PATH]
    assert observed["git_blob_oid"] == probe.ACTION_BLOB_OID
    assert observed["git_blob_sha256"] == probe.ACTION_BLOB_SHA256
    assert observed["git_blob_size"] == 2990
    assert raw["experimental_action"]["expected_parent_sha"] == observed["commit_parent"]


def test_original_git_source_bytes_worktree_and_event_record_match():
    git_raw = probe.git("show", f"{probe.ACTION_COMMIT}:{probe.ACTION_PATH}")
    work_raw = (probe.ROOT / probe.ACTION_PATH).read_bytes()
    assert git_raw == work_raw
    assert sha256(git_raw).hexdigest() == probe.ACTION_BLOB_SHA256
    assert json.loads(git_raw)["event_id"] == "R0_P03_V2_FORWARD_J2_ACTION_001"


def test_source_written_without_claiming_commit_already_happened(event):
    record, observed = event
    action = record["experimental_action"]
    assert action["commit_occurred_at_time_record_was_written"] is False
    assert action["commit_sha_known_before_action"] is False
    assert action["source_path"] == probe.ACTION_PATH
    assert action["commit_message"] == probe.ACTION_COMMIT_MESSAGE


def test_actor_statement_cocommitted_but_not_proven_actor_identity(event, projection):
    record, observed = event
    assert observed["exact_claim_present_in_same_commit_tree"] is True
    assert record["actor_statement"]["claimant_role"] == (
        "EXPOSED_CHATGPT_ARCHITECTURE_COORDINATOR"
    )
    assert observed["independent_actor_identity"] == "NOT_VERIFIED"
    assert projection["actor_claim"]["independent_owner_identity_proof"] is False


def test_probe_only_relational_statement_has_no_governing_target(event, projection):
    claim = event[0]["actor_statement"]["relational_claim"]
    assert claim["target"] == probe.PROBE_ONLY_TARGET
    assert claim["relation"] == "COVERS"
    assert claim["component_ids"] == probe.EXPECTED_COMPONENTS
    assert claim["source_status"] == "CLAIMED_BY_EXPOSED_ACTOR_NOT_J2_ADMITTED"
    assert projection["actor_claim"]["governing_j1_target_accepted"] is False
    assert projection["new_accepted_j1_effects"] == 0
    assert projection["new_qualified_natural_owner_j2"] == 0


def test_fact_owners_remain_distinct_and_git_observable_no_extra_relation(projection):
    assert projection["observable_git"]["fact_owner"] == "GIT_COMMIT_OBJECT"
    assert projection["observable_git"]["changed_path_exact"] is True
    assert projection["observable_git"]["parent_exact"] is True
    assert projection["observable_git"]["file_blob_exact"] is True
    assert projection["observable_git"]["no_separate_covers_needed_for_direct_git_facts"] is True


def test_requested_executor_not_independently_proved_by_git(projection):
    execution = projection["ephemeral_executor"]
    assert execution["requested_executor_self_report"] == (
        "CODEXLESS_RUNTIME_BRIDGE_CODEX_GIT_COMMIT_PATHS"
    )
    assert execution["provider_execution_report_in_current_conversation"] == (
        "BRIDGE_COMMIT_PATHS_AND_PUSH_FF_SUCCESS_REPORTED"
    )
    assert execution["durable_independent_provider_receipt"] is False
    assert execution["underlying_provider_api_independently_authenticated"] is False


def test_history_remains_cannot_attest_new_record_is_not_old_coverage(projection):
    older = projection["comparison_to_historical"]
    assert older["historical_later_source_owner_response"] == "CANNOT_ATTEST"
    assert older["historical_contemporaneous_covers_of_new_p03_j1"] is False
    assert older["new_event_has_contemporaneously_cocommitted_claim"] is True
    assert older["new_event_claim_is_qualified_j2"] is False
    assert older["new_event_proves_actual_requested_executor"] is False


def test_no_j3_formal_scores_target_or_migration(projection):
    assert projection["historical_j3_completion"] == "HOLD"
    assert projection["new_j3_completion"] == (
        "NOT_APPLICABLE_NO_GOVERNING_PROBE_EFFECT"
    )
    assert projection["formal_r0_p03_scores"] is None
    assert projection["physical_target_selected"] is False
    assert projection["p03_preexisting_experiment_only_accepted_j1"] == 4


@pytest.mark.parametrize("field,replacement", [
    ("governing_authority", "ACCEPTED_J1"),
    ("record_class", "GOVERNING_REALIZATION"),
    ("at_action_source_status", "J3_SATISFIED"),
    ("event_id", "R0_P03_V2_FORWARD_J2_ACTION_002"),
    ("schema_version", 2),
])
def test_falsely_elevating_record_or_changing_event_fails(event, field, replacement):
    altered = deepcopy(event[0])
    altered[field] = replacement
    with pytest.raises(ValueError, match="PROSPECTIVE_|SOURCE_RECORD_FALSELY"):
        probe.verify_event_record(altered)


@pytest.mark.parametrize("field,replacement", [
    ("expected_parent_sha", "0" * 40),
    ("source_path", "different/unauthorized.json"),
    ("requested_executor", "INDEPENDENT_PROVIDER_PROOF"),
    ("commit_occurred_at_time_record_was_written", True),
    ("commit_sha_known_before_action", True),
    ("commit_message", "PRODUCTION_J1_CERTIFIED"),
    ("expected_branch", "main"),
])
def test_false_action_or_postcommit_knowledge_rejected(event, field, replacement):
    altered = deepcopy(event[0])
    altered["experimental_action"][field] = replacement
    with pytest.raises(ValueError, match="ACTION_INTENT_OR_PARENT"):
        probe.verify_event_record(altered)


@pytest.mark.parametrize("field,replacement", [
    ("claimant_role", "QUALIFIED_NATURAL_OWNER_SIGNER"),
    ("claimant_identity_assurance", "CRYPTOGRAPHIC_AUTHENTICATED_OWNER"),
    ("natural_owner_claim_scope", "PRODUCTION_J2_AUTHORITY"),
    ("action_intent", "I certified full production realization"),
])
def test_fake_source_authority_rejected(event, field, replacement):
    altered = deepcopy(event[0])
    altered["actor_statement"][field] = replacement
    with pytest.raises(ValueError, match="RELATIONAL_CLAIM_NOT_EXACTLY_BOUNDED"):
        probe.verify_event_record(altered)


@pytest.mark.parametrize("field,replacement", [
    ("target", "D1-E01-D2-CLAUDE-WRITE-REQUIREMENT"),
    ("source_status", "J2_RELATIONAL_QUALIFIED"),
    ("coverage_extent", "FULL_PRODUCTION"),
    ("relation", "CERTIFIES_J3"),
    ("component_ids", ["TRANSPORT_ATTESTED_GITHUB_CONNECTOR"]),
])
def test_probe_claim_cannot_be_transplanted_into_accepted_effect(event, field, replacement):
    altered = deepcopy(event[0])
    altered["actor_statement"]["relational_claim"][field] = replacement
    with pytest.raises(ValueError, match="RELATIONAL_CLAIM_NOT_EXACTLY_BOUNDED"):
        probe.verify_event_record(altered)


def test_extra_authority_field_is_rejected(event):
    altered = deepcopy(event[0])
    altered["new_j3_status"] = "SATISFIED"
    with pytest.raises(ValueError, match="SCHEMA_OR_AUTHORITY"):
        probe.verify_event_record(altered)


def test_observable_owner_cannot_be_changed_to_actor(event):
    altered = deepcopy(event[0])
    altered["fact_owner_boundaries"]["git_parent_and_changed_path"]["natural_owner"] = (
        "EXPOSED_CHATGPT_ARCHITECTURE_COORDINATOR"
    )
    with pytest.raises(ValueError, match="FACT_CLASS_OR_OWNER"):
        probe.verify_event_record(altered)


def test_provider_ephemeral_claim_cannot_be_falsely_recorded_as_observed(event):
    altered = deepcopy(event[0])
    altered["fact_owner_boundaries"]["actual_bridge_invocation"]["status"] = "PROVIDER_SIGNED"
    with pytest.raises(ValueError, match="FACT_CLASS_OR_OWNER"):
        probe.verify_event_record(altered)


def test_assurance_limits_must_not_be_deleted(event):
    altered = deepcopy(event[0])
    altered["assurance_limits"] = altered["assurance_limits"][:3]
    with pytest.raises(ValueError, match="ASSURANCE_EXCLUSIONS"):
        probe.verify_event_record(altered)


def test_tampered_real_git_parent_cannot_pass(monkeypatch):
    original = probe.git

    def fake(*args):
        if args == ("show", "-s", "--format=%P", probe.ACTION_COMMIT):
            return ("f" * 40 + "\n").encode("ascii")
        return original(*args)

    with monkeypatch.context() as m:
        m.setattr(probe, "git", fake)
        with pytest.raises(ValueError, match="CHANGED_PATH_OR_PARENT"):
            probe.original_commit_data()


def test_extra_real_git_changed_path_cannot_pass(monkeypatch):
    original = probe.git

    def fake(*args):
        if args == ("diff-tree", "--no-commit-id", "--name-status", "-r", probe.ACTION_COMMIT):
            return ("A\t" + probe.ACTION_PATH + "\nA\tmalicious/extra.json\n").encode("utf8")
        return original(*args)

    with monkeypatch.context() as m:
        m.setattr(probe, "git", fake)
        with pytest.raises(ValueError, match="CHANGED_PATH_OR_PARENT"):
            probe.original_commit_data()


def test_substituted_claim_source_blob_cannot_pass(monkeypatch):
    original = probe.git

    def fake(*args):
        if args == ("show", f"{probe.ACTION_COMMIT}:{probe.ACTION_PATH}"):
            return b'{"pretend":"relevant"}\n'
        return original(*args)

    with monkeypatch.context() as m:
        m.setattr(probe, "git", fake)
        with pytest.raises(ValueError, match="EVENT_RECORD_BYTES_CHANGED"):
            probe.original_commit_data()


def test_result_is_immutable_and_regenerates_identically(projection):
    recorded = json.loads(probe.OUTPUT.read_text("utf8"))
    assert recorded == projection
    assert recorded["status"].startswith("REAL_GIT_AT_ACTION")
    assert recorded["candidate_design_discriminators"]["architectural_candidate"] == (
        "OPEN_NO_PHYSICAL_SELECTION"
    )


def test_published_commit_has_exact_single_added_path():
    result = subprocess.check_output(
        ["git", "diff-tree", "--no-commit-id", "--name-status", "-r", probe.ACTION_COMMIT],
        cwd=probe.ROOT, text=True, encoding="utf8",
    ).splitlines()
    assert result == ["A\t" + probe.ACTION_PATH]
