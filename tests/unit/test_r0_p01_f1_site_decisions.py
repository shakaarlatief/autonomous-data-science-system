"""Synthetic mutation regression for independently reviewed case pins and F1 decisions.

Validates source/provenance and mandatory cross-case coverage only. No outcome
is an executable scorer oracle; real credential or owner evidence is absent.
"""
from __future__ import annotations

import copy
import json

import pytest

from scripts import check_r0_p01_f1_site_decisions as guard


@pytest.fixture(scope="module")
def inventory():
    return json.loads(guard.INVENTORY.read_text(encoding="utf-8"))


@pytest.fixture(scope="module")
def reviewed_blob():
    pins=json.loads(guard.PINS.read_text(encoding="utf-8"))
    return guard.historical_blob(guard.ROOT,guard.COMMIT,pins["source_path"])


@pytest.fixture
def state():
    return (
        json.loads(guard.PINS.read_text(encoding="utf-8")),
        json.loads(guard.REV02.read_text(encoding="utf-8")),
        json.loads(guard.SITE.read_text(encoding="utf-8")),
    )


def check(state,inventory,reviewed_blob):
    return guard.validate_payload(*state,inventory,reviewed_blob)


def test_full_coverage_with_reviewed_pin_basis():
    r=guard.validate()
    assert r["source_pins"]==24 and r["candidate_site_rows"]==15
    assert r["qualifications"]==7 and r["blocked_scenarios"]==7


def test_reviewed_s3_01_semantic_instrument_inversion_fails(state,inventory,reviewed_blob):
    pins,rev,table=state
    next(x for x in rev["cases"] if x["id"]=="S3-01")["source_grounded_conclusion"]="Every owner abort is an instrument fault with favorable B02 exception."
    with pytest.raises(ValueError,match="source meaning changed"):
        check(state,inventory,reviewed_blob)


def test_x1_ssh_budget_completion_inversion_fails(state,inventory,reviewed_blob):
    next(x for x in state[1]["cases"] if x["id"]=="X1")["source_grounded_conclusion"]="Ctrl+C at third signing call means completed budget exhaustion."
    with pytest.raises(ValueError,match="source meaning changed"):
        check(state,inventory,reviewed_blob)


def test_s1_02_evidenced_client_invocation_dropped_fails(state,inventory,reviewed_blob):
    next(x for x in state[1]["cases"] if x["id"]=="S1-02")["conditions"]="RP only timeout without any evidence of browser invocation"
    with pytest.raises(ValueError,match="source meaning changed"):
        check(state,inventory,reviewed_blob)


def test_premise_change_fails_even_if_local_hash_pin_tampered(state,inventory,reviewed_blob):
    pins,rev,_=state
    row=next(x for x in rev["cases"] if x["id"]=="S3-02")
    row["premises"]["process_isolation"]="NOT_CLAIMED"
    pins["case_premises_exact"]["S3-02"]["process_isolation"]="NOT_CLAIMED"
    pins["pinned_case_sha256"]["S3-02"]=__import__("hashlib").sha256(
        guard.canonical_case_bytes(row,guard.REVIEWED_FIELDS)).hexdigest()
    with pytest.raises(ValueError,match="stored semantic hash not grounded"):
        check(state,inventory,reviewed_blob)


def test_dropping_q1_native_windows_case_fails(state,inventory,reviewed_blob):
    state[2]["rows"]=[x for x in state[2]["rows"] if x["id"]!="D01"]
    with pytest.raises(ValueError,match="row set"):
        check(state,inventory,reviewed_blob)


def test_owner_conditional_policy_not_automatically_adopted(state,inventory,reviewed_blob):
    state[2]["owner_policy_interpretation"]="OWNER_APPROVED_Q1b"
    with pytest.raises(ValueError,match="unapproved owner interpretation"):
        check(state,inventory,reviewed_blob)


def test_malformed_q3_predecessor_source_rejected(state,inventory,reviewed_blob):
    next(x for x in state[2]["rows"] if x["id"]=="D04")["source_basis"][0]="V01_CONTRACT-L9999"
    with pytest.raises(ValueError,match="unsupported frozen"):
        check(state,inventory,reviewed_blob)


def test_no_unconditional_reopen_from_pending_win_test(state,inventory,reviewed_blob):
    next(x for x in state[2]["rows"] if x["id"]=="D01")["expected_class"]="REOPEN"
    with pytest.raises(ValueError,match="unconditional"):
        check(state,inventory,reviewed_blob)


def test_omitting_blocked_cases_fails(state,inventory,reviewed_blob):
    state[2]["blocked_rev02_cases"].remove("X1")
    with pytest.raises(ValueError,match="seven blocked"):
        check(state,inventory,reviewed_blob)


def test_unreviewed_global_scorer_status_fails(state,inventory,reviewed_blob):
    state[2]["F1_frozen"]=True
    with pytest.raises(ValueError,match="unauthorized owner trial"):
        check(state,inventory,reviewed_blob)


def test_table_requires_explicit_evidence_per_site(state,inventory,reviewed_blob):
    next(x for x in state[2]["rows"] if x["id"]=="D02")["evidence_required"]=[]
    with pytest.raises(ValueError,match="missing Q"):
        check(state,inventory,reviewed_blob)
