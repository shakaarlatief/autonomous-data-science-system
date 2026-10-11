"""Governed synthetic research-run initiation and factual evidence preservation.

A procedural approval record comes from a synthetic trusted-controller fixture
and is NOT a cryptographic proof that a real human provided consent. The
governed store requires that record *before* issuing the test run's fresh
cryptographic claim nonce. Actual real-run consent must be provided by the
human owner separately and is not available to this module.

A declared accident can be recorded as nonsecret observation. A new,
separately approved run may replace the interrupted one while the
interrupted claim, measurements, reason and trust status remain preserved.
Neither a stored approval nor an observation acts as a signature.

Both synthetically generated Ed25519 and WebAuthn-shaped ES256 credentials
are in-memory Node test keys; no owner keys or Windows Hello are invoked.
"""
from __future__ import annotations

import copy
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

import pytest

from experiments.r0_p01_owner_acceptance_v01 import harness as historical
from experiments.r0_p01_successor_synthetic import run_bound_acceptance as crypto
from experiments.r0_p01_successor_synthetic.trusted_claim_store import (
    ClaimStoreError,
    SyntheticClaimStore,
)

ROOT = Path(historical.HERE).parents[1]
TEMPLATE = json.loads(
    (Path(historical.HERE) / "clarification_vectors_v02.json").read_text(encoding="utf-8")
)["statement"]

WORKER = r"""
import json,pathlib,sys
from experiments.r0_p01_successor_synthetic.trusted_claim_store import SyntheticClaimStore
from experiments.r0_p01_successor_synthetic.run_bound_acceptance import SyntheticRunCrypto
cfg=json.loads(pathlib.Path(sys.argv[1]).read_text(encoding="utf-8"))
with SyntheticRunCrypto() as node:
    print(json.dumps(SyntheticClaimStore(**cfg).snapshot(node),sort_keys=True),flush=True)
"""


@pytest.fixture(scope="module")
def node():
    if not shutil.which("node") or not shutil.which("ssh-keygen"):
        pytest.skip("Node and OpenSSH required for non-owner security integration")
    with crypto.SyntheticRunCrypto() as signer:
        yield signer


@pytest.fixture(params=["SSH", "ES256"])
def arm(request,node):
    method = "sign_ssh" if request.param == "SSH" else "sign_es256"
    label = "SYNTHETIC-NON-OWNER-GOVERNED-RUN-" + request.param
    seed = crypto.new_run_statement(TEMPLATE,claim_nonce="0"*64)
    material = node.call(method,label=label,statement=seed)
    assert material["synthetic_non_owner"]
    return method,label,material["credential"]


def config(tmp_path, arm):
    return {
        "path":str(tmp_path / "governed-claim.sqlite3"),
        "issuer_id":"SYNTHETIC-GOVERNED-R0P01-ISSUER-001",
        "legacy_template":TEMPLATE,
        "trusted_credential":arm[2],
        "require_governed_issuance":True,
    }


def authorization(ref: str, *, replacement_of=None, approved=True):
    return {
        "authorization_ref":"SYNTHETIC-AUTH-"+ref,
        "purpose":"REPLACEMENT" if replacement_of is not None else "NEW_RUN",
        "replacement_of":replacement_of,
        "approved":approved,
        "source":"SYNTHETIC_TRUSTED_CONTROLLER",
    }


def signature(node,arm,statement):
    result=node.call(arm[0],label=arm[1],statement=statement)
    assert result["credential"]==arm[2]
    assert crypto.verify_for_run(
        presented=statement,trusted_expected=statement,
        proof=result["proof"],credential=arm[2],node=node,
    )
    return result["proof"]


def open_store(config,node):
    s=SyntheticClaimStore(**config,create=True)
    assert s.snapshot(node)["issued_count"]==0
    return s


@pytest.mark.parametrize("approved", [False, None, "yes", 0])
def test_refused_approval_never_issues_a_claim(node,arm,tmp_path,approved):
    cfg=config(tmp_path,arm)
    store=open_store(cfg,node)
    before=store.snapshot(node)
    with pytest.raises(ClaimStoreError,match="explicit synthetic owner approval"):
        store.issue_governed(node,authorization("REFUSED-0001",approved=approved))
    assert store.snapshot(node)==before


def test_governed_issuer_rejects_unapproved_legacy_issue_api(node,arm,tmp_path):
    cfg=config(tmp_path,arm)
    store=open_store(cfg,node)
    with pytest.raises(ClaimStoreError,match="requires explicit authorization"):
        store.issue(node)
    assert store.snapshot(node)["claims"]==[]
    # The issuance enforcement is bound into genesis and survives restart.
    without_governance={k:v for k,v in cfg.items() if k!="require_governed_issuance"}
    with pytest.raises(ClaimStoreError,match="wrong issuer genesis"):
        SyntheticClaimStore(**without_governance)


def test_explicit_approval_is_persisted_and_linked_to_issued_run(node,arm,tmp_path):
    cfg=config(tmp_path,arm)
    store=open_store(cfg,node)
    claim=store.issue_governed(node,authorization("FIRST-RUN-0001"))
    state=store.snapshot(node)
    assert state["issued_count"]==1
    assert state["claims"][0]["nonce"]==claim["claim_nonce"]
    assert state["claims"][0]["authorization_ref"]=="SYNTHETIC-AUTH-FIRST-RUN-0001"
    assert state["observations"]==[]
    assert SyntheticClaimStore(**cfg).snapshot(node)==state


def test_interrupted_owner_declared_run_is_retained_after_replacement(
    node,arm,tmp_path,
):
    cfg=config(tmp_path,arm)
    store=open_store(cfg,node)
    first=store.issue_governed(node,authorization("ACCIDENT-INITIAL-0001"))
    prior_signature=signature(node,arm,first)
    original_status=store.snapshot(node)
    assert original_status["claims"][0]["status"]=="ISSUED"
    interruption=store.record_observation(
        claim_nonce=first["claim_nonce"],kind="INTERRUPTED",
        elapsed_ms=3200,interactions=3,
        note="Accidentally pressed Ctrl+C during the test",node=node,
    )
    assert interruption["recorded"] and interruption["observation_sequence"]==1

    second=store.issue_governed(
        node,authorization("ACCIDENT-REPLACE-0002",
                           replacement_of=first["claim_nonce"]),
    )
    after_replace=store.snapshot(node)
    assert [r["status"] for r in after_replace["claims"]]==["SUPERSEDED","ISSUED"]
    assert [r["authorization_ref"] for r in after_replace["claims"]]==[
        "SYNTHETIC-AUTH-ACCIDENT-INITIAL-0001",
        "SYNTHETIC-AUTH-ACCIDENT-REPLACE-0002",
    ]
    assert after_replace["observations"]==[{
        "claim_nonce":first["claim_nonce"],"kind":"INTERRUPTED",
        "elapsed_ms":3200,"interactions":3,
        "note":"Accidentally pressed Ctrl+C during the test",
    }]
    assert not store.admit(
        claim_nonce=first["claim_nonce"],presented=first,
        proof=prior_signature,credential=arm[2],node=node,
    )["admitted"]
    assert store.admit(
        claim_nonce=second["claim_nonce"],presented=second,
        proof=prior_signature,credential=arm[2],node=node,
    )["reason"]=="INVALID_RUN_PROOF"
    assert store.snapshot(node)==after_replace
    new_signature=signature(node,arm,second)
    assert store.admit(
        claim_nonce=second["claim_nonce"],presented=second,
        proof=new_signature,credential=arm[2],node=node,
    )["admitted"]
    accepted=store.snapshot(node)
    assert [r["status"] for r in accepted["claims"]]==["SUPERSEDED","ADMITTED"]
    assert accepted["observations"]==after_replace["observations"]
    assert SyntheticClaimStore(**cfg).snapshot(node)==accepted


def test_unrecorded_or_reused_authorization_cannot_produce_new_claim(
    node,arm,tmp_path,
):
    cfg=config(tmp_path,arm)
    store=open_store(cfg,node)
    first=store.issue_governed(node,authorization("ONCE-ONLY-0001"))
    before=store.snapshot(node)
    with pytest.raises(ClaimStoreError,match="already consumed"):
        store.issue_governed(node,authorization("ONCE-ONLY-0001"))
    with pytest.raises(ClaimStoreError,match="reference prior claim"):
        store.issue_governed(node,authorization("UNKNOWN-PRIOR-0002",replacement_of="e"*64))
    assert store.snapshot(node)==before
    assert first["claim_nonce"]==before["claims"][0]["nonce"]


def test_nonsecret_observation_does_not_change_acceptance_classification(
    node,arm,tmp_path,
):
    cfg=config(tmp_path,arm)
    store=open_store(cfg,node)
    statement=store.issue_governed(node,authorization("ERROR-CASE-0001"))
    before=store.snapshot(node)
    assert store.record_observation(
        claim_nonce=statement["claim_nonce"],kind="ERROR",
        elapsed_ms=150,interactions=1,note="Synthetic tool error",node=node,
    )["recorded"]
    assert store.record_observation(
        claim_nonce=statement["claim_nonce"],kind="COMPLETED",
        elapsed_ms=760,interactions=3,note="Synthetic operation ended",node=node,
    )["recorded"]
    after=store.snapshot(node)
    assert after["claims"]==before["claims"]
    assert after["claims"][0]["status"]=="ISSUED"
    assert len(after["observations"])==2
    # An event marked COMPLETED is not authority or a cryptographic PASS.
    forged={**statement,"decision":"AMEND"}
    bad=node.call(arm[0],label=arm[1],statement=forged)["proof"]
    assert store.admit(
        claim_nonce=statement["claim_nonce"],presented=forged,
        proof=bad,credential=arm[2],node=node,
    )["reason"]=="INVALID_RUN_PROOF"
    assert store.snapshot(node)==after


@pytest.mark.parametrize("bad",[
    {"kind":"COMPLETED","elapsed_ms":-1,"interactions":2,"note":"Test"},
    {"kind":"ERROR","elapsed_ms":100,"interactions":-1,"note":"Test"},
    {"kind":"INTERRUPTED","elapsed_ms":10,"interactions":2,"note":"passphrase leaked"},
    {"kind":"INVALID","elapsed_ms":20,"interactions":2,"note":"Test"},
])
def test_bad_or_sensitive_observation_is_rejected_without_state_change(
    node,arm,tmp_path,bad,
):
    cfg=config(tmp_path,arm)
    store=open_store(cfg,node)
    issued=store.issue_governed(node,authorization("NO-SECRET-0001"))
    before=store.snapshot(node)
    with pytest.raises(ValueError,match="invalid or potentially sensitive"):
        store.record_observation(
            node=node,claim_nonce=issued["claim_nonce"],**bad
        )
    assert store.snapshot(node)==before


def test_unknown_claim_observation_is_not_persisted(node,arm,tmp_path):
    cfg=config(tmp_path,arm)
    store=open_store(cfg,node)
    before=store.snapshot(node)
    outcome=store.record_observation(
        claim_nonce="d"*64,kind="ERROR",elapsed_ms=100,interactions=1,
        note="Unknown synthetic event",node=node,
    )
    assert outcome=={"recorded":False,"reason":"UNKNOWN_CLAIM"}
    assert store.snapshot(node)==before


def test_observation_survives_separate_python_process_restart(node,arm,tmp_path):
    cfg=config(tmp_path,arm)
    store=open_store(cfg,node)
    statement=store.issue_governed(node,authorization("RESTART-NOTE-0001"))
    assert store.record_observation(
        claim_nonce=statement["claim_nonce"],kind="INTERRUPTED",
        elapsed_ms=1300,interactions=4,note="Synthetic Ctrl+C",node=node,
    )["recorded"]
    file=tmp_path/"config.json"
    file.write_bytes(historical.canonical(cfg))
    result=subprocess.run(
        [sys.executable,"-B","-c",WORKER,str(file)],
        cwd=ROOT,capture_output=True,text=True,timeout=25,
        env={**os.environ,"PYTHONDONTWRITEBYTECODE":"1"},
    )
    assert result.returncode==0,result.stderr
    assert json.loads(result.stdout)==store.snapshot(node)


def test_corrupted_authorization_and_observation_fail_closed(node,arm,tmp_path):
    import sqlite3
    cfg=config(tmp_path,arm)
    store=open_store(cfg,node)
    statement=store.issue_governed(node,authorization("AUDIT-TAMPER-0001"))
    store.record_observation(
        claim_nonce=statement["claim_nonce"],kind="ERROR",
        elapsed_ms=700,interactions=1,note="Synthetic observation",node=node,
    )
    with sqlite3.connect(cfg["path"]) as conn:
        conn.execute("UPDATE run_authorizations SET authorization_blob = ?",
                     (b"{}",))
    with pytest.raises(ClaimStoreError,match="invalid authorization evidence"):
        SyntheticClaimStore(**cfg).snapshot(node)
    # Restore only the known synthetic receipt, then test observation tamper.
    import hashlib
    valid=historical.canonical(authorization("AUDIT-TAMPER-0001"))
    with sqlite3.connect(cfg["path"]) as conn:
        conn.execute("UPDATE run_authorizations SET authorization_blob=?",
                     (valid,))
        conn.execute("UPDATE observations SET observation_blob=?",
                     (b"{}",))
    with pytest.raises(ClaimStoreError,match="invalid durable observation"):
        SyntheticClaimStore(**cfg).snapshot(node)

@pytest.mark.parametrize("changed",[
    {"purpose":["REPLACEMENT"]},
    {"source":["SYNTHETIC_TRUSTED_CONTROLLER"]},
    {"authorization_ref":123},
    {"replacement_of":["a"]},
    {"approved":1},
])
def test_malformed_authorization_fields_fail_closed(node,arm,tmp_path,changed):
    cfg=config(tmp_path,arm)
    store=open_store(cfg,node)
    record={**authorization("BAD-TYPE-0001"),**changed}
    before=store.snapshot(node)
    with pytest.raises(ClaimStoreError,match="explicit synthetic owner approval"):
        store.issue_governed(node,record)
    assert store.snapshot(node)==before


def test_malformed_observation_kind_fails_closed(node,arm,tmp_path):
    cfg=config(tmp_path,arm)
    store=open_store(cfg,node)
    statement=store.issue_governed(node,authorization("NOTE-TYPE-0001"))
    before=store.snapshot(node)
    with pytest.raises(ValueError,match="invalid or potentially sensitive"):
        store.record_observation(
            claim_nonce=statement["claim_nonce"],kind=["INTERRUPTED"],
            elapsed_ms=0,interactions=0,note="Synthetic observation",node=node,
        )
    assert store.snapshot(node)==before
