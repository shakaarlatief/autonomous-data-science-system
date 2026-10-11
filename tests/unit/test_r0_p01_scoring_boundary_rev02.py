"""Mutation tests for the source-sensitive REV02 F1 scoring-boundary candidate guard.

The tests protect exact source identities, independent review judgments, all
seven cross-family risks, and open-source finding traceability. They do not
implement or certify an owner authentication experiment or F1 scorer.
"""
from __future__ import annotations

import copy
import hashlib
import json
from collections import Counter

import pytest

from scripts import check_r0_p01_pending_review_register as pending
from scripts import check_r0_p01_scoring_boundary_rev02 as guard


@pytest.fixture
def payload():
    return json.loads(guard.REV02.read_text(encoding="utf-8"))


@pytest.fixture(scope="module")
def inventory():
    return json.loads(guard.INVENTORY.read_text(encoding="utf-8"))


@pytest.fixture(scope="module")
def pending_register():
    return pending.manifest()


def test_24_source_bounded_cases_and_18_pending_gate_refs() -> None:
    result=guard.validate()
    assert result == {
        "scenarios":24,
        "determinations":{"SOURCE_DETERMINED":17,"CANDIDATE_BLOCKED":7},
        "pending_gate_sources":18,
        "cited_gate_sources":18,
    }


def test_critical_ssh_ctrl_c_race_is_required(payload,inventory,pending_register) -> None:
    payload["cases"]=[x for x in payload["cases"] if x["id"]!="X1"]
    with pytest.raises(ValueError,match="identities changed"):
        guard.validate_payload(payload,inventory,pending_register)


def test_ambiguous_rp_abort_case_cannot_be_removed(payload,inventory,pending_register) -> None:
    payload["cases"]=[x for x in payload["cases"] if x["id"]!="S3-03"]
    with pytest.raises(ValueError,match="identities changed"):
        guard.validate_payload(payload,inventory,pending_register)


def test_blocked_case_relabelled_as_determined_is_rejected(payload,inventory,pending_register) -> None:
    next(x for x in payload["cases"] if x["id"]=="S3-03")["determination"]="SOURCE_DETERMINED"
    with pytest.raises(ValueError,match="silently changed"):
        guard.validate_payload(payload,inventory,pending_register)


def test_original_review_055_case_statuses_preserved(payload,inventory,pending_register) -> None:
    next(x for x in payload["cases"] if x["id"]=="S4-01")["review_055_status"]="CONFIRMED_AS_STATED"
    with pytest.raises(ValueError,match="per-case decision"):
        guard.validate_payload(payload,inventory,pending_register)


def test_predecessor_and_notsupported_sources_required(payload,inventory,pending_register) -> None:
    for uid in ("V01_CONTRACT-L0223","V01_CONTRACT-L0231",
                "REV04_POLICY:webauthn_assertion_failure_table.NotSupportedError.outcome",
                "REV04_POLICY:webauthn_assertion_failure_table.NotSupportedError.proof_viability_receipt"):
        assert any(uid in x["source_basis"] for x in payload["cases"])
    row=next(x for x in payload["cases"] if x["id"]=="S1-04")
    row["source_basis"].remove("V01_CONTRACT-L0223")
    row=next(x for x in payload["cases"] if x["id"]=="S1-05")
    row["source_basis"].remove("V01_CONTRACT-L0223")
    target=next(x for x in payload["open_gate_pending_coverage"] if x["unit_id"]=="V01_CONTRACT-L0223")
    target["case_ids"]=[]
    target["resolution"]="DEFERRED_F1_SOURCE_SITE_OR_RECEIPT_DESIGN"
    with pytest.raises(ValueError,match="crucial B05"):
        guard.validate_payload(payload,inventory,pending_register)


def test_pending_unit_can_never_be_automatically_approved(payload,inventory,pending_register) -> None:
    target=payload["open_gate_pending_coverage"][0]
    target["resolution"]="TASK_OWNER_ACCEPTED"
    with pytest.raises(ValueError,match="silently approved"):
        guard.validate_payload(payload,inventory,pending_register)


def test_case_id_cannot_be_hidden_by_altering_pending_coverage(payload,inventory,pending_register) -> None:
    target=payload["open_gate_pending_coverage"][0]
    target["case_ids"]=[]
    with pytest.raises(ValueError,match="not reconciled"):
        guard.validate_payload(payload,inventory,pending_register)


def test_unfounded_non_reviewed_source_reference_rejected(payload,inventory,pending_register) -> None:
    payload["cases"][0]["source_basis"][0]="V01_CONTRACT-L9999"
    with pytest.raises(ValueError,match="unsupported exact source unit"):
        guard.validate_payload(payload,inventory,pending_register)


def test_source_determined_cannot_have_blocked_reason(payload,inventory,pending_register) -> None:
    case=next(x for x in payload["cases"] if x["id"]=="S4-01")
    case["blocked_reason"]="Issue definitively resolved in all combinations of evidence"
    with pytest.raises(ValueError,match="unsupported blocked reason"):
        guard.validate_payload(payload,inventory,pending_register)


def test_blocked_must_have_explicit_reason(payload,inventory,pending_register) -> None:
    case=next(x for x in payload["cases"] if x["id"]=="S3-03")
    case["blocked_reason"]=None
    with pytest.raises(ValueError,match="lacks explicit blocked reason"):
        guard.validate_payload(payload,inventory,pending_register)


def test_sensitive_conditional_attempt_premises_required(payload,inventory,pending_register) -> None:
    case=next(x for x in payload["cases"] if x["id"]=="S3-02")
    case["premises"]["raw_flags"]="NO_SILENT_INFERENCE"
    with pytest.raises(ValueError,match="whole-attempt class has no flag premise"):
        guard.validate_payload(payload,inventory,pending_register)


def test_approved_source_digest_cannot_drift(payload,inventory,pending_register) -> None:
    payload["approved_source_sha256"]["policy"]="0"*64
    with pytest.raises(ValueError,match="source hash altered"):
        guard.validate_payload(payload,inventory,pending_register)


def test_no_owner_policy_modification_can_be_declared(payload,inventory,pending_register) -> None:
    payload["cases"][0]["owner_policy_interpretation"]="OWNER_APPROVED_NEW_RULE"
    with pytest.raises(ValueError,match="unapproved policy interpretation"):
        guard.validate_payload(payload,inventory,pending_register)


def test_committed_blob_hashes_match_repaired_register_on_platform() -> None:
    register=pending.manifest()
    path="docs/model_collaboration/threads/MC-0030/messages/033_claude_r0_p01_clause_audit_batch001.md"
    blob=pending._committed_bytes(pending.ROOT, pending.Path(path))
    exact=hashlib.sha256(blob).hexdigest()
    entry=next(x for x in register["reviewer_message_digests"] if x["message_path"]==path)
    assert entry["message_sha256"]==exact
    assert register["hash_basis"]=="COMMITTED_GIT_BLOB_BYTES_HEAD_RELATIVE_PATH"
    crlf_variant=blob.replace(b"\r\n",b"\n").replace(b"\n",b"\r\n")
    assert hashlib.sha256(crlf_variant).hexdigest()!=exact
    pending.validate()


def test_every_historical_reviewer_pending_row_remains_unresolved(pending_register) -> None:
    assert len(pending_register["pending"])==55
    assert all(x["task_owner_resolution"]=="UNRESOLVED" for x in pending_register["pending"])
