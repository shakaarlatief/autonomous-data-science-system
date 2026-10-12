"""Source-grounded synthetic F1 receipt/flag expectations, not a frozen oracle.

These handwritten expected outcomes use the approved B01 terminal-event/G1
rules and selected explicitly described §8.6 source-site flags. Tests do
not treat a caller-supplied receipt as independently authenticated; genuine
RP/browser attestation and capability probe validation remain separate.
"""
from __future__ import annotations

import copy
import hashlib

import pytest

from experiments.r0_p01_successor_synthetic.independent_receipt_reference import (
    derive_arm_evidence, derive_narrow_flags,
)
from experiments.r0_p01_successor_synthetic.independent_b01_oracle import classify_b01

ATTEMPT="SYNTHETIC-P01-RECEIPTS-0001"
EVENTS=("P0","S01","S02","S03")
BASE={
    "verifier_result":"NOT_RUN",
    "unexpected_rp_exit_sequence":None,
    "owner_abort_sequence":None,
    "previous_snapshot_bytes":None,
    "declared_previous_sha256":None,
    "final_head_witness_present":True,
}


def receipt(arm="A",event="P0",outcome="VALID"):
    return {
        "attempt_id":ATTEMPT,
        "arm":arm,
        "event":event,
        "acceptance_id":f"{ATTEMPT}-{arm}-{event}",
        "event_terminal":outcome is not None,
        "terminal_outcome":outcome,
        "verification_result":(
            outcome if outcome in {"VALID","INVALID"} else "NOT_RUN"
        ),
        "assertion":None,
    }


def cancelled(event="P0", *, invoked=True, consumed=True, delivered=True):
    item=receipt("B",event,"WEBAUTHN_ASSERTION_NOT_COMPLETED")
    identity=item["acceptance_id"]
    item["assertion"]={
        "rp_issued":True,
        "rp_delivered":delivered,
        "browser_get_invoked":invoked,
        "rp_consumed":consumed,
        "rp_acceptance_id":identity,
        "browser_acceptance_id":identity,
        "browser_result":"NotAllowedError",
    }
    return item


def derive(arm="A",setup="REALIZABLE",events=None,**kwargs):
    return derive_arm_evidence(
        arm=arm,attempt_id=ATTEMPT,setup=setup,
        event_receipts=[] if events is None else events,**kwargs,
    )


@pytest.mark.parametrize("arm",["A","B"])
def test_four_distinct_verified_terminal_receipts_complete_arm(arm):
    result=derive(arm,events=[receipt(arm,event) for event in EVENTS])
    assert result["evidence_state"]=="COMPLETED"
    assert result["terminal_events"]==list(EVENTS)
    assert result["missing_or_unqualified_events"]==[]


@pytest.mark.parametrize("missing",EVENTS)
def test_missing_one_of_four_required_events_is_incomplete(missing):
    result=derive(events=[receipt("A",event) for event in EVENTS if event!=missing])
    assert result["evidence_state"]=="INCOMPLETE"
    assert result["missing_or_unqualified_events"]==[missing]


@pytest.mark.parametrize("setup",["OWNER_REFUSED","NOT_VISITED","CAPABILITY_CLAIMED"])
def test_owner_refusal_unvisited_or_unproved_capability_never_implies_not_realizable(setup):
    result=derive(setup=setup,events=[])
    assert result["evidence_state"]=="INCOMPLETE"
    if setup=="CAPABILITY_CLAIMED":
        assert result["capability_qualification"]=="PENDING_INDEPENDENT_PRODUCER"


def test_unqualified_claimed_capability_receipt_fails_closed():
    with pytest.raises(ValueError,match="qualification pending"):
        derive(
            setup="CAPABILITY_CLAIMED",
            capability_receipt={"self_declared":"NotSupportedError"},
        )


@pytest.mark.parametrize("outcome",[
    "P0_NON_ACCEPT_DECISION",
    "OWNER_S_EVENT_STOP",
    "SSH_UNLOCK_BUDGET_EXHAUSTED",
    "PARTIAL_OR_INCONSISTENT_OUTPUT",
    "INVALID",
])
def test_terminal_no_proof_or_invalid_verification_is_still_terminal_event(outcome):
    events=[receipt("A","P0",outcome)]
    events += [receipt("A",e) for e in EVENTS[1:]]
    result=derive(events=events)
    assert result["evidence_state"]=="COMPLETED"
    assert result["terminal_events"]==list(EVENTS)


@pytest.mark.parametrize("invoked,consumed,delivered,expected",[
    (True,True,True,"COMPLETED"),
    (False,True,True,"INCOMPLETE"),
    (True,False,True,"INCOMPLETE"),
    (True,True,False,"INCOMPLETE"),
])
def test_rp_client_observation_is_required_for_webauthn_terminal_no_proof(
    invoked,consumed,delivered,expected,
):
    events=[cancelled("P0",invoked=invoked,consumed=consumed,delivered=delivered)]
    events += [receipt("B",e) for e in EVENTS[1:]]
    result=derive("B",events=events)
    assert result["evidence_state"]==expected
    if expected=="INCOMPLETE":
        assert result["missing_or_unqualified_events"]==["P0"]


@pytest.mark.parametrize("browser_result",["NotAllowedError","OWNER_CANCEL","TIMEOUT"])
def test_complete_correlated_webauthn_cancel_receipt_remains_no_proof_terminal(browser_result):
    ev=cancelled()
    ev["assertion"]["browser_result"]=browser_result
    result=derive("B",events=[ev]+[receipt("B",e) for e in EVENTS[1:]])
    assert result["evidence_state"]=="COMPLETED"


def test_webauthn_claimed_notallowed_without_rp_receipt_cannot_claim_completed():
    ev=receipt("B","P0","WEBAUTHN_ASSERTION_NOT_COMPLETED")
    result=derive("B",events=[ev]+[receipt("B",e) for e in EVENTS[1:]])
    assert result["evidence_state"]=="INCOMPLETE"


def test_ctrl_c_mid_event_does_not_create_a_terminal_stop():
    ev=receipt("A","S02",None)
    events=[receipt("A","P0"),receipt("A","S01"),ev]
    result=derive(events=events)
    assert result["evidence_state"]=="INCOMPLETE"
    assert result["missing_or_unqualified_events"]==["S02","S03"]


def test_invalid_verifier_is_terminal_invalid_proof_not_instrument():
    events=[receipt("A",e, "INVALID" if e=="P0" else "VALID") for e in EVENTS]
    assert derive(events=events)["evidence_state"]=="COMPLETED"
    flags=derive_narrow_flags(**{**BASE,"verifier_result":"INVALID"})
    assert not flags["integrity.verifier_error"]
    assert not flags["integrity.instrument_failure"]


def test_verifier_error_is_not_an_invalid_owner_signature():
    events=[receipt("A","P0",None)]
    events[0]["verification_result"]="ERROR"
    assert derive(events=events)["evidence_state"]=="INCOMPLETE"
    flags=derive_narrow_flags(**{**BASE,"verifier_result":"ERROR"})
    assert flags["integrity.verifier_error"]
    assert flags["integrity.instrument_failure"]


@pytest.mark.parametrize("change",[
    {"attempt_id":"SYNTHETIC-OTHER-RUN-0001"},
    {"arm":"B"},
    {"acceptance_id":"SYNTHETIC-OTHER-RUN-0001-A-P0"},
    {"event":"UNKNOWN"},
    {"event_terminal":1},
    {"terminal_outcome":"DOES_NOT_EXIST"},
    {"terminal_outcome":None},
    {"verification_result":"VALIDATOR_CRASHED"},
    {"verification_result":"INVALID"},
])
def test_malformed_or_untrusted_event_identity_cannot_become_completed(change):
    event={**receipt(),**change}
    with pytest.raises(ValueError):
        derive(events=[event]+[receipt("A",x) for x in EVENTS[1:]])


def test_duplicate_event_receipts_are_not_four_distinct_proof_events():
    with pytest.raises(ValueError,match="duplicate"):
        derive(events=[receipt("A","P0")]*4)


@pytest.mark.parametrize("change",[
    {"rp_consumed":"true"},
    {"rp_acceptance_id":"SYNTHETIC-OTHER-RUN-0001-B-P0"},
    {"browser_acceptance_id":"SYNTHETIC-OTHER-RUN-0001-B-P0"},
    {"browser_result":"NotSupportedError"},
])
def test_webauthn_forged_or_malformed_cancel_receipt_fails_closed(change):
    ev=cancelled()
    ev["assertion"].update(change)
    with pytest.raises(ValueError):
        derive("B",events=[ev])


@pytest.mark.parametrize("verify,expected",[
    ("VALID",False),("INVALID",False),("NOT_RUN",False),("ERROR",True),
])
def test_tri_state_verifier_failure_flag_is_exact(verify,expected):
    result=derive_narrow_flags(**{**BASE,"verifier_result":verify})
    assert result["integrity.verifier_error"] is expected


@pytest.mark.parametrize("rp,owner,expected",[
    (3,None,True),(3,5,True),(5,3,False),(None,3,False),
])
def test_node_exit_flag_obeys_causal_order_of_recorded_abort(rp,owner,expected):
    f=derive_narrow_flags(**{
        **BASE,"unexpected_rp_exit_sequence":rp,
        "owner_abort_sequence":owner,
    })
    assert f["integrity.node_rp_failure"] is expected
    assert f["integrity.instrument_failure"] is expected


def test_same_sequence_order_is_not_guessed():
    with pytest.raises(ValueError,match="ambiguous"):
        derive_narrow_flags(**{
            **BASE,"unexpected_rp_exit_sequence":3,
            "owner_abort_sequence":3,
        })


def test_actual_previous_snapshot_bytes_are_hashed_not_self_asserted():
    previous=b"SYNTHETIC-NON-OWNER-PREVIOUS-FINAL-SNAPSHOT"
    truth=hashlib.sha256(previous).hexdigest()
    good=derive_narrow_flags(**{
        **BASE,"previous_snapshot_bytes":previous,
        "declared_previous_sha256":truth,
    })
    assert not good["integrity.evidence_chain_break"]
    changed=derive_narrow_flags(**{
        **BASE,"previous_snapshot_bytes":previous+b"x",
        "declared_previous_sha256":truth,
    })
    assert changed["integrity.evidence_chain_break"]


def test_missing_final_head_witness_is_only_a_disclosure():
    flags=derive_narrow_flags(**{**BASE,"final_head_witness_present":False})
    assert flags["evidence.final_head_witness_absent"]
    assert not flags["integrity.evidence_chain_break"]
    assert not flags["integrity.instrument_failure"]
    a={"evidence_state":"INCOMPLETE","proof_viable":False,"selection_eligible":False}
    score=classify_b01(
        A=a,B=a,integrity_flag=flags["integrity.evidence_chain_break"],
        instrument_flag=flags["integrity.instrument_failure"],
        volume_gate_pass=False,
    )
    assert score["class"]=="INVALID" and score["reason"]=="INVALID_INCOMPLETE"


def test_actual_hash_link_break_dominates_verifier_error_at_scoring_boundary():
    f=derive_narrow_flags(**{
        **BASE,"verifier_result":"ERROR",
        "previous_snapshot_bytes":b"actual",
        "declared_previous_sha256":hashlib.sha256(b"expected").hexdigest(),
    })
    a={"evidence_state":"INCOMPLETE","proof_viable":False,"selection_eligible":False}
    score=classify_b01(
        A=a,B=a,integrity_flag=f["integrity.evidence_chain_break"],
        instrument_flag=f["integrity.instrument_failure"],
        volume_gate_pass=False,
    )
    assert score["reason"]=="INVALID_INTEGRITY"


@pytest.mark.parametrize("change",[
    {"unexpected_rp_exit_sequence":True},
    {"owner_abort_sequence":0},
    {"verifier_result":"verifier error"},
    {"final_head_witness_present":None},
    {"previous_snapshot_bytes":b"orphan"},
    {"declared_previous_sha256":"0"*64},
    {"previous_snapshot_bytes":b"data","declared_previous_sha256":"bad"},
])
def test_invalid_flag_evidence_fails_closed_instead_of_defaulting_false(change):
    with pytest.raises(ValueError):
        derive_narrow_flags(**{**BASE,**change})


def test_g1_false_reopen_blocked_by_uncorroborated_browser_cancellation():
    ssh=derive(events=[
        receipt("A",event,"OWNER_S_EVENT_STOP") for event in EVENTS
    ])
    web=derive("B",events=[
        cancelled("P0",consumed=False),
        *[receipt("B",event,"INVALID") for event in EVENTS[1:]],
    ])
    assert ssh["evidence_state"]=="COMPLETED"
    assert web["evidence_state"]=="INCOMPLETE"
    left={"evidence_state":ssh["evidence_state"],"proof_viable":False,
          "selection_eligible":False}
    right={"evidence_state":web["evidence_state"],"proof_viable":False,
           "selection_eligible":False}
    verdict=classify_b01(
        A=left,B=right,integrity_flag=False,instrument_flag=False,
        volume_gate_pass=False,
    )
    assert verdict["class"]=="INVALID"
    assert verdict["reason"]=="INVALID_INCOMPLETE"


def test_g1_reopen_only_after_both_four_event_terminal_sets_resolved():
    ssh=derive(events=[
        receipt("A",event,"SSH_UNLOCK_BUDGET_EXHAUSTED") for event in EVENTS
    ])
    web=derive("B",events=[
        cancelled(event) for event in EVENTS
    ])
    assert ssh["evidence_state"]=="COMPLETED"
    assert web["evidence_state"]=="COMPLETED"
    left={"evidence_state":ssh["evidence_state"],"proof_viable":False,
          "selection_eligible":False}
    right={"evidence_state":web["evidence_state"],"proof_viable":False,
           "selection_eligible":False}
    verdict=classify_b01(
        A=left,B=right,integrity_flag=False,instrument_flag=False,
        volume_gate_pass=False,
    )
    assert verdict["class"]=="REOPEN"
    assert verdict["reason"]=="NO_VIABLE_CRYPTOGRAPHIC_ARM_AFTER_COMPLETE_EVIDENCE"

@pytest.mark.parametrize("outcome",["OWNER_S_EVENT_STOP","SSH_UNLOCK_BUDGET_EXHAUSTED"])
def test_native_ssh_event_terminals_do_not_complete_webauthn_arm(outcome):
    ev=receipt("B","P0",outcome)
    with pytest.raises(ValueError,match="native SSH"):
        derive("B",events=[ev])
