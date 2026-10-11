"""Real synthetic Ed25519 and ES256 claim-nonce signature sensitivity tests.

Unlike the historical V02 signed acceptance (where an external database
run_id was not signed), the successor statement includes a fresh 256-bit
claim_nonce and explicit protocol marker in the cryptographic message.

Both a wrong run and modification of the nonce inside signed bytes must be
rejected. Positive controls use real Windows OpenSSH verification or Node
P-256 verification. All signers are ephemeral, synthetic and never owner
credentials or physical Windows Hello authenticators.
"""
from __future__ import annotations

import copy
import json
import shutil
from pathlib import Path

import pytest

from experiments.r0_p01_owner_acceptance_v01 import harness as old
from experiments.r0_p01_successor_synthetic import run_bound_acceptance as rb

TEMPLATE_PATH=Path(old.HERE)/"clarification_vectors_v02.json"


@pytest.fixture(scope="module")
def template():
    return json.loads(TEMPLATE_PATH.read_text(encoding="utf-8"))["statement"]


@pytest.fixture(scope="module")
def signed_material(template):
    if not shutil.which("node") or not shutil.which("ssh-keygen"):
        pytest.skip("Node and OpenSSH required for real synthetic signature checks")
    one=rb.new_run_statement(template,claim_nonce=rb.fresh_claim_nonce())
    two=rb.new_run_statement(template,claim_nonce=rb.fresh_claim_nonce())
    assert one["claim_nonce"] != two["claim_nonce"]
    assert one["acceptance_id"] == two["acceptance_id"]
    node=rb.SyntheticRunCrypto()
    try:
        proofs={}
        for arm,method in [("SSH","sign_ssh"),("ES256","sign_es256")]:
            label="SYNTHETIC-NON-OWNER-CLAIM-BOUND-"+arm
            a=node.call(method,label=label,statement=one)
            b=node.call(method,label=label,statement=two)
            assert a["synthetic_non_owner"] and b["synthetic_non_owner"]
            assert a["credential"]==b["credential"]
            assert a["proof"] != b["proof"]
            proofs[arm]=(a,b)
        yield node,one,two,proofs
    finally:
        node.close()


def accepted(node,statement,expected,signed):
    return rb.verify_for_run(
        presented=statement, trusted_expected=expected,
        proof=signed["proof"],credential=signed["credential"],node=node,
    )


@pytest.mark.parametrize("arm",["SSH","ES256"])
def test_new_run_signed_message_has_valid_cryptographic_positive_controls(
    signed_material,arm,
):
    node,one,two,proofs=signed_material
    first,second=proofs[arm]
    assert accepted(node,one,one,first)
    assert accepted(node,two,two,second)


@pytest.mark.parametrize("arm",["SSH","ES256"])
def test_valid_old_run_signature_cannot_authorize_a_different_run(
    signed_material,arm,
):
    node,one,two,proofs=signed_material
    first,second=proofs[arm]
    assert one["acceptance_id"] == two["acceptance_id"]
    assert accepted(node,one,one,first)
    assert accepted(node,two,two,second)
    # First reject from trusted-run mismatch even though old proof is valid.
    assert not accepted(node,one,two,first)
    # Then require actual cryptographic failure when the attacker replaces
    # the presented signed nonce while retaining run-one signature bytes.
    assert not accepted(node,two,two,first)
    assert not accepted(node,one,one,second)


@pytest.mark.parametrize("arm",["SSH","ES256"])
def test_signed_nonce_change_invalidates_signature_without_changing_signer(
    signed_material,arm,
):
    node,one,two,proofs=signed_material
    first,_=proofs[arm]
    altered=copy.deepcopy(one)
    altered["claim_nonce"]=two["claim_nonce"]
    assert set(altered)==set(one)
    assert altered["acceptance_id"]==one["acceptance_id"]
    assert not accepted(node,altered,altered,first)
    assert accepted(node,one,one,first)


@pytest.mark.parametrize("arm",["SSH","ES256"])
def test_signed_decision_or_semantic_digest_change_cannot_reuse_signature(
    signed_material,arm,
):
    node,one,_,proofs=signed_material
    proof,_=proofs[arm]
    for change in [
        {"decision":"REJECT"},
        {"semantic_base_digest":"f"*64},
        {"shown_digest":"e"*64},
    ]:
        altered={**one,**change}
        assert rb.valid_shape(altered)
        assert not accepted(node,altered,altered,proof)
    assert accepted(node,one,one,proof)


@pytest.mark.parametrize("arm",["SSH","ES256"])
def test_signed_protocol_and_claim_shape_are_fail_closed(
    signed_material,arm,
):
    node,one,_,proofs=signed_material
    proof,_=proofs[arm]
    for changed in [
        {**one,"protocol":"HISTORICAL-V02"},
        {**one,"claim_nonce":"a"*63},
        {**one,"claim_nonce":"A"*64},
        {k:v for k,v in one.items() if k!="claim_nonce"},
        {**one,"untrusted_extra":"owner"},
    ]:
        assert not rb.valid_shape(changed)
        assert not accepted(node,changed,changed,proof)


def test_random_claim_nonce_is_high_entropy_and_not_predictable_from_event():
    generated=[rb.fresh_claim_nonce() for _ in range(32)]
    assert len(set(generated))==32
    assert all(len(n)==64 and n==n.lower() for n in generated)
    assert all(bytes.fromhex(n) and len(bytes.fromhex(n))==32 for n in generated)


@pytest.mark.parametrize("nonce",["","0"*63,"0"*65,"G"*64,"0"*64+"suffix"])
def test_new_statement_requires_valid_run_nonce(template,nonce):
    with pytest.raises(ValueError,match="claim_nonce"):
        rb.new_run_statement(template,claim_nonce=nonce)


def test_historical_v02_signature_verifier_cannot_accept_new_protocol_statement(
    signed_material,
):
    node,one,_,proofs=signed_material
    ssh,_=proofs["SSH"]
    p256,_=proofs["ES256"]
    # Extra signed fields are not in the exact historical V02 statement
    # grammar. Do not accidentally reinterpret V02 proofs as V03 authority.
    assert not old.verify(one,ssh["proof"],ssh["credential"],node)
    assert not old.verify(one,p256["proof"],p256["credential"],node)


@pytest.mark.parametrize("arm",["SSH","ES256"])
def test_wrong_public_signer_key_is_not_authorized(
    signed_material,arm,template,
):
    node,one,_,proofs=signed_material
    first,_=proofs[arm]
    other=node.call(
        "sign_ssh" if arm=="SSH" else "sign_es256",
        label="SYNTHETIC-NON-OWNER-CLAIM-BOUND-OTHER-"+arm,
        statement=one,
    )
    assert accepted(node,one,one,first)
    assert accepted(node,one,one,other)
    # Proof from the first key may not be attributed to the other key.
    assert not rb.verify_for_run(
        presented=one,trusted_expected=one,
        proof=first["proof"],credential=other["credential"],node=node,
    )


def test_signed_run_identity_is_explicit_and_materially_changes_message(
    signed_material,
):
    _,one,two,_=signed_material
    assert one["protocol"]==rb.PROTOCOL and two["protocol"]==rb.PROTOCOL
    assert one["claim_nonce"]!=two["claim_nonce"]
    assert set(one)==rb.FIELDS
    assert old.canonical(one)!=old.canonical(two)
    assert old.sha(old.canonical(one))!=old.sha(old.canonical(two))


def test_synthetic_worker_rejects_unlabelled_or_owner_signer_request(
    signed_material,
):
    node,one,_,_=signed_material
    with pytest.raises(ValueError,match="input validation"):
        node.call("sign_ssh",label="OWNER-PRIMARY",statement=one)
    with pytest.raises(ValueError,match="input validation"):
        node.call("sign_es256",label="OWNER-WINDOWS-HELLO",statement=one)
