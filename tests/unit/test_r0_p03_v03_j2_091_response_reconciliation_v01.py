"""Source-anchored tests of the irreversible retrospective J2 testimony limit.

The new Claude source-owner response is CANNOT_ATTEST, not a COVERS claim.
These cases protect direct Git OBSERVABLE facts from a mistaken blanket
RELATIONAL coverage gate and forbid treating two same-event transport
statements as independent provider proof. None is a scored P03 benchmark.
"""
from copy import deepcopy
from hashlib import sha256
import json
from pathlib import Path
import subprocess

import pytest

from experiments.r0_p03_navigation_probe import (
    v03_j2_091_response_reconciliation_v01 as study,
)


@pytest.fixture(scope="module")
def evidence():
    return study.build()


def test_exact_published_message091_identity():
    body, prov = study.published_reply()
    assert prov["commit"] == study.REPLY_COMMIT
    assert prov["parent"] == study.REPLY_PARENT
    assert prov["changed_paths"] == ["A\t" + study.REPLY_PATH]
    assert prov["git_blob_oid"] == study.REPLY_GIT_BLOB
    assert prov["source_git_blob_sha256"] == study.REPLY_GIT_SHA256
    assert prov["source_git_blob_bytes"] == 11784
    assert sha256(body.encode("utf8")).hexdigest() == study.REPLY_GIT_SHA256


def test_worktree_crlf_representation_not_confused_with_git_blob():
    original = study.git("show", f"{study.REPLY_COMMIT}:{study.REPLY_PATH}")
    working = (study.ROOT / study.REPLY_PATH).read_bytes()
    assert working.replace(b"\r\n", b"\n") == original
    assert sha256(original).hexdigest() == study.REPLY_GIT_SHA256


def test_claude_cannot_attest_and_has_no_covers_candidate():
    body, _ = study.published_reply()
    summary = study.parse_disposition(body)
    assert summary["DISPOSITION"] == "CANNOT_ATTEST"
    assert summary["COVERED_COMPONENTS"] == "NONE"
    assert summary["JSON_DECLARATION"] == "NOT_PROVIDED"
    assert summary["J2_QUALIFIED"] == "0"
    assert summary["J3_CERTIFIED"] == "false"
    assert summary["CONTRADICTION_FOUND"] == "false"


@pytest.mark.parametrize("field,new", [
    ("DISPOSITION", "EXPLICIT_COVERS_CLAIM"),
    ("COVERED_COMPONENTS", "AUTHORIZED_PATH_ONLY"),
    ("JSON_DECLARATION", "PROVIDED"),
    ("PROVIDER_TRANSPORT", "PROVEN_BY_GIT"),
    ("J2_QUALIFIED", "3"),
    ("J3_CERTIFIED", "true"),
    ("AUTHORIAL_CONTINUITY", "VERIFIED"),
    ("ACCEPTED_PACKET_SHA256", "f" * 64),
])
def test_false_reinterpretation_of_claude_response_fails_closed(field, new):
    body, _ = study.published_reply()
    changed = body.replace(field + "=" + study.EXPECTED_SUMMARY[field], field + "=" + new)
    with pytest.raises(ValueError, match="MESSAGE091_DISPOSITION_OR_SCOPE_DRIFT"):
        study.parse_disposition(changed)


def test_no_implicit_json_claim_allowed():
    body, _ = study.published_reply()
    fake = body + "\n" + chr(96) * 3 + "json\n{}\n" + chr(96) * 3 + "\n"
    with pytest.raises(ValueError, match="MESSAGE091_UNEXPECTED_COVERS_JSON"):
        study.parse_disposition(fake)


def test_summary_missing_or_duplicated_fails():
    body, _ = study.published_reply()
    with pytest.raises(ValueError, match="MESSAGE091_SUMMARY_NOT_UNIQUE"):
        study.parse_disposition(body + "\nMESSAGE=MC0030_091")
    with pytest.raises(ValueError, match="MESSAGE091_FINAL_DISPOSITION_MISSING"):
        study.parse_disposition(body.replace(chr(96) * 3 + "text\nMESSAGE=MC0030_091", chr(96) * 3 + "txt\nMESSAGE=MC0030_091"))


def test_original_commit_message_is_second_attestation_not_provider_proof(evidence):
    rows = evidence["ephemeral_transport"]["attestation_sources"]
    assert rows["number_of_textual_attestation_carriers"] == 2
    assert rows["number_of_independent_provider_records"] == 0
    assert rows["number_of_independent_first_hand_owner_witnesses"] == 0
    assert rows["duplicated_admitted_natural_owner_j2_fact"] is False
    assert rows["single_authoritative_provider_event_carrier_selected"] is False
    assert rows["underlying_transport"] == "UNKNOWN"


def test_tampered_original_commit_attestation_detected(monkeypatch):
    native_git = study.git

    def forged(*args):
        if args == ("show", "-s", "--format=%B", study.j2.ACTION):
            return b"Commit with no source-attested connector transport"
        return native_git(*args)

    with monkeypatch.context() as ctx:
        ctx.setattr(study, "git", forged)
        with pytest.raises(ValueError, match="ORIGINAL_COMMIT_TRANSPORT_ATTESTATION_DRIFT"):
            study.check_repeated_transport_claim()


def test_tampered_original_message_attestation_detected(monkeypatch):
    native_git = study.j2.git

    def forged(*args):
        data = native_git(*args)
        if args == ("show", f"{study.j2.ORIGINAL_PIN}:{study.j2.CLAUDE_MESSAGE}"):
            return data.replace(
                study.ORIGINAL_TRANSPORT_LINE.encode("utf8"),
                b"Transport                       unsupported claim",
            )
        return data

    with monkeypatch.context() as ctx:
        ctx.setattr(study.j2, "git", forged)
        with pytest.raises(ValueError, match="ORIGINAL_MESSAGE_TRANSPORT_ATTESTATION_DRIFT"):
            study.check_repeated_transport_claim()


def test_direct_git_observables_do_not_require_extra_relational_claim(evidence):
    fields = evidence["observable_git"]
    assert fields["verified_component_ids"] == [
        "AUTHORIZED_PATH_ONLY", "COMMIT_RECEIPT_BOUND_TO_CORRECTION_HEAD"
    ]
    assert fields["natural_owner"] == "GIT_COMMIT_OBJECT"
    assert fields["additional_relational_covers_required_for_direct_observable_fact_itself"] is False
    assert fields["j3_satisfied_from_git_alone"] is False


def test_separate_genuine_relational_coverage_remains_unqualified(evidence):
    relation = evidence["natural_owner_relational"]
    assert relation["reply"] == "CANNOT_ATTEST"
    assert relation["new_covers_claim_present"] is False
    assert relation["covered_components"] == []
    assert relation["qualified_relational_facts"] == 0
    assert relation["first_hand_context_retained"] is False


def test_source_attestation_does_not_rewrite_governing_requirement(evidence):
    state = evidence["ephemeral_transport"]
    assert state["component"] == "TRANSPORT_ATTESTED_GITHUB_CONNECTOR"
    assert state["attestation_exists_as_original_source_text"] is True
    assert state["actual_connector_action_proven"] is False
    assert state["assurance_and_completion_rule_interpretation"] == (
        "UNRESOLVED_DO_NOT_SILENTLY_AMEND_E01"
    )
    assert evidence["accepted_j1_original_statement_unchanged"] is True


def test_no_j3_certification_no_formal_p03_or_physical_target(evidence):
    assert evidence["accepted_experiment_only_j1"] == 4
    assert evidence["qualified_j2_relational_count"] == 0
    assert evidence["new_j3_completion_certified"] is False
    assert evidence["historical_d1_result"] == "D1_AMEND_UNCHANGED"
    assert evidence["formal_p03_scores"] is None
    assert evidence["physical_architecture_selected"] is False


def test_finite_historical_reask_stop_and_new_contemporaneous_path(evidence):
    assert evidence["natural_owner_relational"][
        "reask_same_historical_action_from_other_claude_sessions"
    ] is False
    assert evidence["future_physical_design_trigger"]["status"] == (
        "OPEN_J2_TYPED_FACT_AND_ASSURANCE_CONTRACT"
    )
    assert evidence["next"].startswith("NON_RETROSPECTIVE")


def test_source_reply_author_trailer_not_independent_original_action_proof(evidence):
    assert evidence["publication"]["provenance_class"] == (
        "SHARED_GIT_CONTENT_WITH_CLAUDE_COLLABORATION_TRAILER"
    )
    assert evidence["publication"]["original_action_first_hand_continuity"] == (
        "NOT_ESTABLISHED"
    )


def test_published_reply_wrong_parent_or_path_rejected(monkeypatch):
    native_git = study.git

    def forged(*args):
        if args == ("show", "-s", "--format=%P", study.REPLY_COMMIT):
            return ("f" * 40 + "\n").encode("ascii")
        return native_git(*args)

    with monkeypatch.context() as ctx:
        ctx.setattr(study, "git", forged)
        with pytest.raises(ValueError, match="PUBLICATION_PARENT_OR_PATH_CHANGED"):
            study.published_reply()


def test_current_git_publication_matches_only_one_added_file():
    changed = subprocess.check_output(
        ["git", "diff-tree", "--no-commit-id", "--name-status", "-r", study.REPLY_COMMIT],
        cwd=study.ROOT, text=True, encoding="utf8",
    ).splitlines()
    assert changed == ["A\t" + study.REPLY_PATH]


def test_immutable_receipt_reproducible_and_no_unqualified_promotion():
    raw = study.RESULT.read_bytes()
    assert json.loads(raw) == study.build()
    assert sha256(raw).hexdigest() == (
        "772badb8775a345e8d29cae55d057ffc47deb83aa91aebcc1a2fa6766bc29760"
    )
