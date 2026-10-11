"""Crash/restart, replay, and concurrency tests for synthetic R0-P01 durability.

The tests run actual independent child Python processes and the historical
Ed25519/ES256 signature verification. All supplied credentials are public
and synthetically generated with fresh in-memory Node keys. The private keys
never enter the SQLite journal or the test runner.

The separately documented missing per-run nonce is an explicit LIMITATION:
passing these tests must never be described as cross-run replay resistance.
"""
from __future__ import annotations

import copy
import json
import os
import shutil
import sqlite3
import subprocess
import sys
from pathlib import Path

import pytest

from experiments.r0_p01_owner_acceptance_v01 import harness as original
from experiments.r0_p01_successor_synthetic.durable_admission import (
    DurableJournalError,
    SyntheticDurableLedger,
)

ROOT = Path(original.HERE).parents[1]
RUN_ID = "SYNTHETIC-DURABLE-RESTART-0001"

WORKER = r"""
import json,os,pathlib,sys
from experiments.r0_p01_owner_acceptance_v01 import harness as h
from experiments.r0_p01_successor_synthetic.durable_admission import SyntheticDurableLedger
config=json.loads(pathlib.Path(sys.argv[1]).read_text(encoding="utf-8"))
record=json.loads(pathlib.Path(sys.argv[2]).read_text(encoding="utf-8"))
action=sys.argv[3]
node=h.NodeBridge()
try:
    store=SyntheticDurableLedger(**config)
    if action=="before_commit_crash":
        store._commit_transaction=lambda _connection: os._exit(38)
    result=store.admit(record,node)
    if action=="after_commit_crash":
        os._exit(39)
    print(json.dumps(result),flush=True)
finally:
    node.close()
"""


@pytest.fixture(scope="module")
def environment():
    if not shutil.which("node") or not shutil.which("ssh-keygen"):
        pytest.skip("Node and OpenSSH required for synthetic durable replay tests")
    fixture=json.loads(
        (Path(original.HERE)/"fixture.json").read_text(encoding="utf-8")
    )
    statement=json.loads(
        (Path(original.HERE)/"clarification_vectors_v02.json").read_text(
            encoding="utf-8"
        )
    )["statement"]
    node=original.NodeBridge()
    try:
        keys={}
        for identity, method in (
            ("A_PRIMARY","synthetic_ssh"),
            ("B_PRIMARY","synthetic_webauthn"),
            ("RECOVERY","synthetic_ssh"),
        ):
            response=node.call(
                method,
                label="SYNTHETIC-NON-OWNER-DURABLE-PUBLIC-"+identity.replace("_","-"),
                statement=statement,
            )
            assert original.verify(
                statement,response["proof"],response["credential"],node
            )
            keys[identity]=(method,response["credential"])
        yield fixture,node,keys
    finally:
        node.close()


def config(environment, tmp_path, arm, run_id=RUN_ID):
    f,_,keys=environment
    return {
        "path":str(tmp_path/"admission.sqlite3"),
        "run_id":run_id,
        "fixture":f,
        "arm":arm,
        "primary":keys[f"{arm}_PRIMARY"][1],
        "recovery":keys["RECOVERY"][1],
        "a_primary":keys["A_PRIMARY"][1],
        "a_recovery":keys["RECOVERY"][1],
        "scenario":"BURDEN",
    }


def sign_record(environment, cfg, item, signer, *, ledger=None):
    fixture,node,keys=environment
    if ledger is None:
        ledger=original.Ledger(
            fixture,cfg["arm"],cfg["primary"],cfg["recovery"],
            cfg["a_primary"],cfg["a_recovery"],cfg["scenario"],
        )
    credential=keys[signer][1]
    record=original.record(
        fixture,cfg["arm"],item,ledger,"ACCEPT",None,credential
    )
    response=node.call(
        keys[signer][0],
        label="SYNTHETIC-NON-OWNER-DURABLE-PUBLIC-"+signer.replace("_","-"),
        statement=record["statement"],
    )
    assert response["credential"]==credential
    assert original.verify(
        record["statement"],response["proof"],credential,node
    )
    record["proof"]=response["proof"]
    record["verifier_result"]="VALID"
    return record


def child(tmp_path, config_data, record, action):
    """Run a separate process with only public config and signed proof bytes."""
    conf=tmp_path/"config.json"
    proof=tmp_path/"signed_record.json"
    conf.write_bytes(original.canonical(config_data))
    proof.write_bytes(original.canonical(record))
    return subprocess.run(
        [sys.executable,"-B","-c",WORKER,str(conf),str(proof),action],
        cwd=ROOT,capture_output=True,text=True,timeout=25,
        env={**os.environ,"PYTHONDONTWRITEBYTECODE":"1"},
    )


@pytest.mark.parametrize("arm",["A","B"])
def test_committed_consumed_id_remains_rejected_after_process_restart(
    environment,tmp_path,arm,
):
    _,node,_=environment
    cfg=config(environment,tmp_path,arm)
    record=sign_record(environment,cfg,"P0",f"{arm}_PRIMARY")
    journal=SyntheticDurableLedger(**cfg,create=True)
    assert journal.admit(record,node)["admitted"]
    before=journal.snapshot(node)
    result=child(tmp_path,cfg,record,"normal")
    assert result.returncode==0,result.stderr
    assert json.loads(result.stdout)=={
        "admitted":False,"reason":"CONSUMED_ACCEPTANCE_ID",
    }
    after=SyntheticDurableLedger(**cfg).snapshot(node)
    assert after==before
    assert after["accepted_count"]==1


@pytest.mark.parametrize("arm",["A","B"])
def test_crash_before_commit_rolls_back_and_acceptance_remains_available(
    environment,tmp_path,arm,
):
    _,node,_=environment
    cfg=config(environment,tmp_path,arm)
    record=sign_record(environment,cfg,"P0",f"{arm}_PRIMARY")
    journal=SyntheticDurableLedger(**cfg,create=True)
    crash=child(tmp_path,cfg,record,"before_commit_crash")
    assert crash.returncode==38,crash.stderr
    restarted=SyntheticDurableLedger(**cfg)
    assert restarted.snapshot(node)["accepted_count"]==0
    assert restarted.admit(record,node)["admitted"]
    assert restarted.snapshot(node)["accepted_count"]==1


@pytest.mark.parametrize("arm",["A","B"])
def test_crash_after_commit_before_response_cannot_double_accept(
    environment,tmp_path,arm,
):
    _,node,_=environment
    cfg=config(environment,tmp_path,arm)
    record=sign_record(environment,cfg,"P0",f"{arm}_PRIMARY")
    SyntheticDurableLedger(**cfg,create=True)
    crash=child(tmp_path,cfg,record,"after_commit_crash")
    assert crash.returncode==39,crash.stderr
    restarted=SyntheticDurableLedger(**cfg)
    assert restarted.snapshot(node)["accepted_count"]==1
    before=restarted.snapshot(node)
    assert restarted.admit(record,node)=={
        "admitted":False,"reason":"CONSUMED_ACCEPTANCE_ID",
    }
    assert restarted.snapshot(node)==before


@pytest.mark.parametrize("arm",["A","B"])
def test_two_concurrent_processes_cannot_admit_one_signed_acceptance_twice(
    environment,tmp_path,arm,
):
    _,node,_=environment
    cfg=config(environment,tmp_path,arm)
    record=sign_record(environment,cfg,"P0",f"{arm}_PRIMARY")
    journal=SyntheticDurableLedger(**cfg,create=True)
    conf=tmp_path/"config.json"
    proof=tmp_path/"signed_record.json"
    conf.write_bytes(original.canonical(cfg))
    proof.write_bytes(original.canonical(record))
    cmd=[sys.executable,"-B","-c",WORKER,str(conf),str(proof),"normal"]
    a=subprocess.Popen(cmd,cwd=ROOT,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True)
    b=subprocess.Popen(cmd,cwd=ROOT,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True)
    results=[]
    for proc in (a,b):
        stdout,stderr=proc.communicate(timeout=25)
        assert proc.returncode==0,stderr
        results.append(json.loads(stdout))
    assert sorted(x["admitted"] for x in results)==[False,True]
    assert journal.snapshot(node)["accepted_count"]==1


def test_restarted_trust_root_restores_current_roles_and_blocks_old_primary(
    environment,tmp_path,
):
    fixture,node,keys=environment
    cfg=config(environment,tmp_path,"A")
    journal=SyntheticDurableLedger(**cfg,create=True)
    memory=original.Ledger(
        fixture,"A",cfg["primary"],cfg["recovery"],
        cfg["a_primary"],cfg["a_recovery"],cfg["scenario"],
    )
    baseline=sign_record(environment,cfg,"P0","A_PRIMARY",ledger=memory)
    assert journal.admit(baseline,node)["admitted"]
    assert memory.admit(baseline,node)["admitted"]
    stale=sign_record(environment,cfg,"S01","A_PRIMARY",ledger=memory)
    rotation=sign_record(environment,cfg,"P5","A_PRIMARY",ledger=memory)
    assert journal.admit(rotation,node)["admitted"]
    assert memory.admit(rotation,node)["admitted"]
    restarted=SyntheticDurableLedger(**cfg)
    current=restarted.snapshot(node)
    assert current["signer_set_version"]==original.V2
    assert current["accepted_count"]==2
    before=restarted.snapshot(node)
    assert restarted.admit(stale,node)["reason"]=="IDENTITY_OR_BASE_MISMATCH"
    assert restarted.snapshot(node)==before
    new_primary=sign_record(environment,cfg,"S01","RECOVERY",ledger=memory)
    assert restarted.admit(new_primary,node)["admitted"]
    assert restarted.snapshot(node)["accepted_count"]==3


def test_unrelated_run_or_initial_public_signer_cannot_reopen_same_journal(
    environment,tmp_path,
):
    cfg=config(environment,tmp_path,"A")
    SyntheticDurableLedger(**cfg,create=True)
    with pytest.raises(DurableJournalError,match="run, fixture, or initial trust identity"):
        SyntheticDurableLedger(**{**cfg,"run_id":"SYNTHETIC-DIFFERENT-RUN-0002"})
    cfg2=copy.deepcopy(cfg)
    cfg2["primary"]=environment[2]["RECOVERY"][1]
    with pytest.raises(DurableJournalError,match="run, fixture, or initial trust identity"):
        SyntheticDurableLedger(**cfg2)


def test_durable_payload_corruption_and_sequence_truncation_fail_closed(
    environment,tmp_path,
):
    _,node,_=environment
    cfg=config(environment,tmp_path,"A")
    record=sign_record(environment,cfg,"P0","A_PRIMARY")
    journal=SyntheticDurableLedger(**cfg,create=True)
    assert journal.admit(record,node)["admitted"]
    with sqlite3.connect(cfg["path"]) as conn:
        conn.execute("UPDATE accepted SET record_blob = ?",(b"{}",))
    with pytest.raises(DurableJournalError,match="byte digest"):
        journal.snapshot(node)
    with sqlite3.connect(cfg["path"]) as conn:
        conn.execute("DELETE FROM accepted")
    with pytest.raises(DurableJournalError,match="anchor mismatch"):
        journal.snapshot(node)


def test_denied_replay_does_not_change_durable_hash_or_entry_count(
    environment,tmp_path,
):
    _,node,_=environment
    cfg=config(environment,tmp_path,"B")
    record=sign_record(environment,cfg,"P0","B_PRIMARY")
    journal=SyntheticDurableLedger(**cfg,create=True)
    assert journal.admit(record,node)["admitted"]
    before=journal.snapshot(node)
    assert journal.admit(record,node)=={
        "admitted":False,"reason":"CONSUMED_ACCEPTANCE_ID",
    }
    assert journal.snapshot(node)==before


def test_old_signed_statement_does_not_contain_unique_run_nonce(
    environment,tmp_path,
):
    """Explicitly expose, not conceal, the historical cross-run replay gap.

    A separate freshly initialized store cannot independently distinguish
    an old signed acceptance from a new one if the signed statement does not
    bind a run nonce. Thus even a fully passing durable-restart test suite
    DOES NOT authorize replacing the fresh nonce requirement in the
    successor signing protocol.
    """
    _,node,_=environment
    cfg=config(environment,tmp_path,"A")
    record=sign_record(environment,cfg,"P0","A_PRIMARY")
    assert "run_id" not in record["statement"]
    assert cfg["run_id"] not in original.canonical(record["statement"]).decode()
    assert SyntheticDurableLedger(**cfg,create=True).admit(record,node)["admitted"]
    another_dir=tmp_path/"other_run"
    another_dir.mkdir()
    separate={**cfg,
              "path":str(another_dir/"admission.sqlite3"),
              "run_id":"SYNTHETIC-OTHER-RUN-0002"}
    # KNOWN HISTORICAL LIMITATION: this succeeds, and must not be called
    # future-proof cross-run security or a qualified successor.
    assert SyntheticDurableLedger(**separate,create=True).admit(record,node)["admitted"]


def test_missing_database_never_silently_recreates_consumption_history(
    environment,tmp_path,
):
    _,node,_=environment
    cfg=config(environment,tmp_path,"A")
    with pytest.raises(DurableJournalError,match="journal missing"):
        SyntheticDurableLedger(**cfg)
    journal=SyntheticDurableLedger(**cfg,create=True)
    proof=sign_record(environment,cfg,"P0","A_PRIMARY")
    assert journal.admit(proof,node)["admitted"]
    assert journal.snapshot(node)["accepted_count"]==1
    with pytest.raises(DurableJournalError,match="already exists"):
        SyntheticDurableLedger(**cfg,create=True)
    # This simulates accidental journal deletion, NOT malicious rollback
    # protection. A reopen cannot silently reset state to zero.
    Path(cfg["path"]).unlink()
    with pytest.raises(DurableJournalError,match="journal missing"):
        SyntheticDurableLedger(**cfg)


def test_existing_empty_database_is_not_initialized_on_restart(
    environment,tmp_path,
):
    cfg=config(environment,tmp_path,"B")
    Path(cfg["path"]).write_bytes(b"")
    with pytest.raises(DurableJournalError,match="reopening journal without genesis"):
        SyntheticDurableLedger(**cfg)
    with pytest.raises(DurableJournalError,match="already exists"):
        SyntheticDurableLedger(**cfg,create=True)
