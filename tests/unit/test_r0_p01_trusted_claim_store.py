"""End-to-end synthetic trusted claim issuance and run-bound admission tests.

Each run has a fresh random nonce, persisted before the signer is called.
No caller-provided signed statement is trusted as a run selector. The stored
expected statement is deterministically reconstructed from immutable genesis
and the issued nonce, then actual Ed25519 OpenSSH or ES256 Node verification
checks the synthetic proof. A new claim supersedes an unfinished old one.

Subprocesses are used for genuine restart, precommit and postcommit crashes,
and races. All keys are ephemeral Node synthetic KeyObjects; all on-disk
records contain only public signer identity, challenge and signature bytes.
This does not authorize a real owner trial or establish malicious disk
rollback resilience, hardware WebAuthn or the whole R0-P01 scorer.
"""
from __future__ import annotations

import copy
import hashlib
import json
import os
import shutil
import sqlite3
import subprocess
import sys
from pathlib import Path

import pytest

from experiments.r0_p01_owner_acceptance_v01 import harness as old
from experiments.r0_p01_successor_synthetic import run_bound_acceptance as rb
from experiments.r0_p01_successor_synthetic.trusted_claim_store import (
    ClaimStoreError, SyntheticClaimStore,
)

ROOT=Path(old.HERE).parents[1]
TEMPLATE=json.loads(
    (Path(old.HERE)/"clarification_vectors_v02.json").read_text(encoding="utf-8")
)["statement"]

WORKER=r"""
import json,os,pathlib,sys
from experiments.r0_p01_successor_synthetic.run_bound_acceptance import SyntheticRunCrypto
from experiments.r0_p01_successor_synthetic.trusted_claim_store import SyntheticClaimStore
config=json.loads(pathlib.Path(sys.argv[1]).read_text(encoding='utf-8'))
request=json.loads(pathlib.Path(sys.argv[2]).read_text(encoding='utf-8'))
action=sys.argv[3]
with SyntheticRunCrypto() as node:
    store=SyntheticClaimStore(**config)
    if action in ('issue_before_commit_crash','admit_before_commit_crash'):
        store._commit=lambda _conn: os._exit(41)
    if action.startswith('issue_'):
        result=store.issue(node)
    elif action.startswith('admit_'):
        result=store.admit(node=node,**request)
    elif action=='snapshot':
        result=store.snapshot(node)
    else:raise RuntimeError('unsupported worker operation')
    if action in ('issue_after_commit_crash','admit_after_commit_crash'):
        os._exit(42)
    print(json.dumps(result,sort_keys=True),flush=True)
"""


@pytest.fixture(scope="module")
def node():
    if not shutil.which("node") or not shutil.which("ssh-keygen"):
        pytest.skip("Node and OpenSSH required for non-owner integration tests")
    with rb.SyntheticRunCrypto() as signer:
        yield signer


@pytest.fixture(params=["SSH","ES256"])
def arm(request,node):
    kind,method=(
        ("SSH_ED25519","sign_ssh") if request.param=="SSH"
        else ("WEBAUTHN_ES256","sign_es256")
    )
    # The first synthetic run is signed only to obtain the enrolled public
    # signer identity. It cannot admit an owner operation or test claim.
    probe=rb.new_run_statement(TEMPLATE,claim_nonce="0"*64)
    label="SYNTHETIC-NON-OWNER-DURABLE-CLAIM-"+request.param
    credentials=node.call(method,label=label,statement=probe)
    assert credentials["credential"]["kind"]==kind
    return request.param,method,label,credentials["credential"]


def setup(tmp_path,arm):
    _,_,_,credential=arm
    return {
        "path":str(tmp_path/"claims.sqlite3"),
        "issuer_id":"SYNTHETIC-R0P01-CLAIM-ISSUER-001",
        "legacy_template":TEMPLATE,
        "trusted_credential":credential,
    }


def sign(node,arm,statement):
    _,method,label,credential=arm
    result=node.call(method,label=label,statement=statement)
    assert result["credential"]==credential
    assert rb.verify_for_run(
        presented=statement,trusted_expected=statement,
        credential=credential,proof=result["proof"],node=node
    )
    return result["proof"]


def request(statement,proof,credential,*,selector=None):
    return {
        "claim_nonce":selector if selector is not None else statement["claim_nonce"],
        "presented":statement,"proof":proof,"credential":credential,
    }


def process(tmp_path,config,action,req=None):
    cfg=tmp_path/"worker-config.json"
    record=tmp_path/"worker-request.json"
    cfg.write_bytes(old.canonical(config))
    record.write_bytes(old.canonical(req or {}))
    return subprocess.run(
        [sys.executable,"-B","-c",WORKER,str(cfg),str(record),action],
        cwd=ROOT,env={**os.environ,"PYTHONDONTWRITEBYTECODE":"1"},
        capture_output=True,text=True,timeout=24,
    )


def test_new_issued_claim_roundtrip_and_restart_admission(node,arm,tmp_path):
    cfg=setup(tmp_path,arm)
    store=SyntheticClaimStore(**cfg,create=True)
    statement=store.issue(node)
    assert statement["claim_nonce"]!="0"*64
    assert statement["protocol"]==rb.PROTOCOL
    assert store.snapshot(node)["claims"][0]["status"]=="ISSUED"
    proof=sign(node,arm,statement)
    before=SyntheticClaimStore(**cfg).snapshot(node)
    assert store.admit(node=node,**request(statement,proof,cfg["trusted_credential"]))["admitted"]
    fresh=SyntheticClaimStore(**cfg)
    after=fresh.snapshot(node)
    assert len(after["claims"])==1 and after["claims"][0]["status"]=="ADMITTED"
    assert after["claims"][0]["statement_sha256"]==old.digest(statement)
    assert after!=before
    assert not fresh.admit(node=node,**request(statement,proof,cfg["trusted_credential"]))["admitted"]
    assert fresh.snapshot(node)==after
    result=process(tmp_path,cfg,"snapshot")
    assert result.returncode==0,result.stderr
    assert json.loads(result.stdout)==after


def test_prior_unfinished_claim_is_superseded_before_fresh_replacement(node,arm,tmp_path):
    cfg=setup(tmp_path,arm)
    store=SyntheticClaimStore(**cfg,create=True)
    old_statement=store.issue(node)
    old_proof=sign(node,arm,old_statement)
    fresh_statement=store.issue(node)
    assert old_statement["claim_nonce"]!=fresh_statement["claim_nonce"]
    before=store.snapshot(node)
    assert [x["status"] for x in before["claims"]]==["SUPERSEDED","ISSUED"]
    # Even selecting the old claim by its actual nonce must fail; submitting
    # the older proof to the new claim must fail with unchanged store.
    a=store.admit(node=node,**request(old_statement,old_proof,cfg["trusted_credential"]))
    b=store.admit(node=node,**request(old_statement,old_proof,cfg["trusted_credential"],selector=fresh_statement["claim_nonce"]))
    c=store.admit(node=node,**request(fresh_statement,old_proof,cfg["trusted_credential"]))
    assert a["reason"]=="CLAIM_NOT_ACTIVE"
    assert b["reason"]==c["reason"]=="INVALID_RUN_PROOF"
    assert store.snapshot(node)==before
    new_proof=sign(node,arm,fresh_statement)
    assert store.admit(node=node,**request(fresh_statement,new_proof,cfg["trusted_credential"]))["admitted"]


def test_wrong_public_signer_even_with_valid_signature_is_not_trusted(node,arm,tmp_path):
    cfg=setup(tmp_path,arm)
    store=SyntheticClaimStore(**cfg,create=True)
    statement=store.issue(node)
    method=arm[1]
    outsider=node.call(
        method,label="SYNTHETIC-NON-OWNER-DURABLE-CLAIM-OUTSIDER-"+arm[0],
        statement=statement,
    )
    assert rb.verify_for_run(
        presented=statement,trusted_expected=statement,
        proof=outsider["proof"],credential=outsider["credential"],node=node
    )
    before=store.snapshot(node)
    result=store.admit(node=node,**request(statement,outsider["proof"],outsider["credential"]))
    assert result["reason"]=="UNTRUSTED_SIGNER"
    assert before==store.snapshot(node)


def test_forged_semantic_or_claim_context_refused_without_side_effects(node,arm,tmp_path):
    cfg=setup(tmp_path,arm)
    store=SyntheticClaimStore(**cfg,create=True)
    statement=store.issue(node)
    proof=sign(node,arm,statement)
    before=store.snapshot(node)
    for mutated in [
        {**statement,"semantic_base_digest":"b"*64},
        {**statement,"decision":"REJECT"},
        {**statement,"claim_nonce":"c"*64},
    ]:
        result=store.admit(
            node=node,**request(mutated,proof,cfg["trusted_credential"],selector=statement["claim_nonce"])
        )
        assert result["reason"]=="INVALID_RUN_PROOF"
        assert store.snapshot(node)==before


def test_crash_before_and_after_issuance_commit_preserve_correct_claim_state(node,arm,tmp_path):
    cfg=setup(tmp_path,arm)
    store=SyntheticClaimStore(**cfg,create=True)
    before=store.snapshot(node)
    aborted=process(tmp_path,cfg,"issue_before_commit_crash")
    assert aborted.returncode==41,aborted.stderr
    assert SyntheticClaimStore(**cfg).snapshot(node)==before
    committed=process(tmp_path,cfg,"issue_after_commit_crash")
    assert committed.returncode==42,committed.stderr
    restarted=SyntheticClaimStore(**cfg)
    after=restarted.snapshot(node)
    assert after["issued_count"]==1 and after["claims"][0]["status"]=="ISSUED"
    # Issuance response was lost, but exact expected claim survives restart.
    assert after["claims"][0]["nonce"]!= "0"*64


def test_crash_before_and_after_admission_commit_preserve_single_use(node,arm,tmp_path):
    cfg=setup(tmp_path,arm)
    store=SyntheticClaimStore(**cfg,create=True)
    statement=store.issue(node)
    signed=sign(node,arm,statement)
    req=request(statement,signed,cfg["trusted_credential"])
    initial=store.snapshot(node)
    aborted=process(tmp_path,cfg,"admit_before_commit_crash",req)
    assert aborted.returncode==41,aborted.stderr
    assert SyntheticClaimStore(**cfg).snapshot(node)==initial
    committed=process(tmp_path,cfg,"admit_after_commit_crash",req)
    assert committed.returncode==42,committed.stderr
    reopened=SyntheticClaimStore(**cfg)
    before=reopened.snapshot(node)
    assert before["claims"][0]["status"]=="ADMITTED"
    assert reopened.admit(node=node,**req)["reason"]=="CLAIM_NOT_ACTIVE"
    assert reopened.snapshot(node)==before


def test_concurrent_child_processes_admit_the_same_claim_once(node,arm,tmp_path):
    cfg=setup(tmp_path,arm)
    store=SyntheticClaimStore(**cfg,create=True)
    statement=store.issue(node)
    proof=sign(node,arm,statement)
    conf=tmp_path/"worker-config.json"
    record=tmp_path/"worker-request.json"
    conf.write_bytes(old.canonical(cfg))
    record.write_bytes(old.canonical(request(statement,proof,cfg["trusted_credential"])))
    cmd=[sys.executable,"-B","-c",WORKER,str(conf),str(record),"admit_normal"]
    a=subprocess.Popen(cmd,cwd=ROOT,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True)
    b=subprocess.Popen(cmd,cwd=ROOT,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True)
    results=[]
    for proc in (a,b):
        out,err=proc.communicate(timeout=24)
        assert proc.returncode==0,err
        results.append(json.loads(out))
    assert sorted(x["admitted"] for x in results)==[False,True]
    assert store.snapshot(node)["claims"][0]["status"]=="ADMITTED"


def test_expected_statement_tampering_cannot_rewrite_trusted_run(node,arm,tmp_path):
    cfg=setup(tmp_path,arm)
    store=SyntheticClaimStore(**cfg,create=True)
    statement=store.issue(node)
    forged={**statement,"decision":"REJECT"}
    blob=old.canonical(forged)
    # Tampering with both the statement AND its unkeyed hash must fail
    # because expected statement is independently reconstructed from genesis.
    with sqlite3.connect(cfg["path"]) as conn:
        conn.execute(
            "UPDATE claims SET expected_blob=?,expected_sha256=?",
            (blob,hashlib.sha256(blob).hexdigest()),
        )
    with pytest.raises(ClaimStoreError,match="expected statement was modified"):
        SyntheticClaimStore(**cfg).snapshot(node)


def test_changed_genesis_or_missing_db_cannot_be_reopened_as_empty(node,arm,tmp_path):
    cfg=setup(tmp_path,arm)
    store=SyntheticClaimStore(**cfg,create=True)
    store.issue(node)
    other={**cfg,"issuer_id":"SYNTHETIC-R0P01-CLAIM-ISSUER-OTHER"}
    with pytest.raises(ClaimStoreError,match="wrong issuer genesis"):
        SyntheticClaimStore(**other)
    with pytest.raises(ClaimStoreError,match="already exists"):
        SyntheticClaimStore(**cfg,create=True)
    Path(cfg["path"]).unlink()
    with pytest.raises(ClaimStoreError,match="missing issuer database"):
        SyntheticClaimStore(**cfg)


def test_random_nonce_collision_never_reissues_claim(node,arm,tmp_path,monkeypatch):
    cfg=setup(tmp_path,arm)
    store=SyntheticClaimStore(**cfg,create=True)
    first=store.issue(node)
    monkeypatch.setattr(rb,"fresh_claim_nonce",lambda:first["claim_nonce"])
    before=store.snapshot(node)
    with pytest.raises(ClaimStoreError,match="nonce collision"):
        store.issue(node)
    assert store.snapshot(node)==before


def test_externally_supplied_claim_nonce_is_not_an_authority_to_issue(node,arm,tmp_path):
    cfg=setup(tmp_path,arm)
    store=SyntheticClaimStore(**cfg,create=True)
    assert store.admit(
        claim_nonce="a"*64,presented=rb.new_run_statement(
            TEMPLATE,claim_nonce="a"*64
        ),proof={},credential=cfg["trusted_credential"],node=node,
    )["reason"]=="UNKNOWN_CLAIM"
    assert store.snapshot(node)["issued_count"]==0


def test_two_concurrent_issuers_preserve_both_claims_but_only_one_active(
    node,arm,tmp_path,
):
    cfg=setup(tmp_path,arm)
    store=SyntheticClaimStore(**cfg,create=True)
    conf=tmp_path/"worker-config.json"
    record=tmp_path/"worker-request.json"
    conf.write_bytes(old.canonical(cfg))
    record.write_bytes(old.canonical({}))
    cmd=[sys.executable,"-B","-c",WORKER,str(conf),str(record),"issue_normal"]
    a=subprocess.Popen(cmd,cwd=ROOT,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True)
    b=subprocess.Popen(cmd,cwd=ROOT,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True)
    issued=[]
    for proc in (a,b):
        out,err=proc.communicate(timeout=24)
        assert proc.returncode==0,err
        issued.append(json.loads(out))
    assert issued[0]["claim_nonce"]!=issued[1]["claim_nonce"]
    state=store.snapshot(node)
    assert state["issued_count"]==2
    assert [c["status"] for c in state["claims"]]==["SUPERSEDED","ISSUED"]


def test_corrupt_admitted_proof_cannot_be_recovered_even_if_hash_recomputed(
    node,arm,tmp_path,
):
    cfg=setup(tmp_path,arm)
    store=SyntheticClaimStore(**cfg,create=True)
    statement=store.issue(node)
    proof=sign(node,arm,statement)
    assert store.admit(node=node,**request(statement,proof,cfg["trusted_credential"]))["admitted"]
    with sqlite3.connect(cfg["path"]) as conn:
        row=conn.execute("SELECT admission_blob FROM claims WHERE status='ADMITTED'").fetchone()
        record=old.strict_json(row[0])
        record["presented"]["claim_nonce"]="e"*64
        tampered=old.canonical(record)
        conn.execute(
            "UPDATE claims SET admission_blob=?,admission_sha256=? WHERE status='ADMITTED'",
            (tampered,hashlib.sha256(tampered).hexdigest()),
        )
    with pytest.raises(ClaimStoreError,match="admitted run identity not authoritative"):
        SyntheticClaimStore(**cfg).snapshot(node)
