"""Atomic synthetic R0-P01 accepted-proof and timing-evidence regression.

This suite exercises actual SQLite commit boundaries with real synthetic
Ed25519 SSHSIG and WebAuthn-shaped ES256 public verification. A precommit
abrupt child exit must leave both admission and its measured observation
absent. A postcommit pre-acknowledgment child exit must leave both present.

The older unmeasured admission remains intentionally possible for backward
synthetic tests, and the assessor must still flag its observation as MISSING.
The new measured-admission path guarantees only one atomic recorded technical
latency for the verified claim, not true owner effort or a scored experiment.
"""
from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
import time
from pathlib import Path

import pytest

from experiments.r0_p01_owner_acceptance_v01 import harness as historical
from experiments.r0_p01_successor_synthetic import run_bound_acceptance as crypto
from experiments.r0_p01_successor_synthetic import synthetic_measurement as measure
from experiments.r0_p01_successor_synthetic.trusted_claim_store import (
    ClaimStoreError,
    SyntheticClaimStore,
)

ROOT = Path(historical.HERE).parents[1]
TEMPLATE = json.loads(
    (Path(historical.HERE) / "clarification_vectors_v02.json").read_text(encoding="utf-8")
)["statement"]

CHILD = r"""
import json,os,pathlib,sys,time
from experiments.r0_p01_successor_synthetic.run_bound_acceptance import SyntheticRunCrypto
from experiments.r0_p01_successor_synthetic.trusted_claim_store import SyntheticClaimStore
cfg=json.loads(pathlib.Path(sys.argv[1]).read_text(encoding="utf-8"))
record=json.loads(pathlib.Path(sys.argv[2]).read_text(encoding="utf-8"))
mode=sys.argv[3]
with SyntheticRunCrypto() as node:
    store=SyntheticClaimStore(**cfg)
    if mode=="before_commit":
        store._commit=lambda connection: os._exit(51)
    elif mode=="after_commit":
        def post_commit(connection):
            connection.commit()
            os._exit(52)
        store._commit=post_commit
    result=store.admit(
        node=node,claim_nonce=record["statement"]["claim_nonce"],
        presented=record["statement"],proof=record["proof"],
        credential=record["credential"],measurement_started_ns=time.perf_counter_ns(),
    )
    print(json.dumps(result),flush=True)
"""


@pytest.fixture(scope="module")
def node():
    if not shutil.which("node") or not shutil.which("ssh-keygen"):
        pytest.skip("real public verification requires Node and OpenSSH")
    with crypto.SyntheticRunCrypto() as client:
        yield client


@pytest.fixture(params=["SSH", "ES256"])
def arm(request, node):
    method = "sign_ssh" if request.param == "SSH" else "sign_es256"
    label = "SYNTHETIC-NON-OWNER-ATOMIC-FINALIZE-" + request.param
    seed = crypto.new_run_statement(TEMPLATE, claim_nonce="0" * 64)
    key = node.call(method, label=label, statement=seed)["credential"]
    return method, label, key


def authorization(ref):
    return {
        "authorization_ref": "SYNTHETIC-AUTH-FINALIZE-" + ref,
        "purpose": "NEW_RUN", "replacement_of": None,
        "approved": True, "source": "SYNTHETIC_TRUSTED_CONTROLLER",
    }


def create(tmp_path, arm, node):
    cfg = {
        "path": str(tmp_path / "atomic.sqlite3"),
        "issuer_id": "SYNTHETIC-ATOMIC-FINALIZE-ISSUER-001",
        "legacy_template": TEMPLATE,
        "trusted_credential": arm[2],
        "require_governed_issuance": True,
    }
    store = SyntheticClaimStore(**cfg, create=True)
    statement = store.issue_governed(node, authorization("ONE-RUN-0001"))
    signed = node.call(arm[0], label=arm[1], statement=statement)
    assert signed["credential"] == arm[2]
    assert crypto.verify_for_run(
        presented=statement, trusted_expected=statement,
        proof=signed["proof"], credential=arm[2], node=node,
    )
    return cfg, store, {"statement": statement, "proof": signed["proof"],
                        "credential": arm[2]}


def admit(store, node, record, *, started_ns=None):
    return store.admit(
        node=node, claim_nonce=record["statement"]["claim_nonce"],
        presented=record["statement"], proof=record["proof"],
        credential=record["credential"],
        measurement_started_ns=(
            time.perf_counter_ns() if started_ns is None else started_ns
        ),
    )


def child(tmp_path, cfg, record, mode):
    config_path = tmp_path / "cfg.json"
    record_path = tmp_path / "record.json"
    config_path.write_bytes(historical.canonical(cfg))
    record_path.write_bytes(historical.canonical(record))
    return subprocess.run(
        [sys.executable, "-B", "-c", CHILD, str(config_path), str(record_path), mode],
        cwd=ROOT, capture_output=True, text=True, timeout=25,
        env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"},
    )


def test_successful_measured_acceptance_commits_one_complete_receipt(node, arm, tmp_path):
    cfg, store, record = create(tmp_path, arm, node)
    started = time.perf_counter_ns()
    time.sleep(0.032)
    result = admit(store, node, record, started_ns=started)
    assert result["admitted"] is True
    assert result["observation_sequence"] == 1
    assert result["measured_elapsed_ms"] >= 30
    snapshot = SyntheticClaimStore(**cfg).snapshot(node)
    assert snapshot["claims"][0]["status"] == "ADMITTED"
    assert snapshot["observations"] == [{
        "claim_nonce": record["statement"]["claim_nonce"],
        "kind": "COMPLETED",
        "elapsed_ms": result["measured_elapsed_ms"],
        "interactions": 1,
        "note": "Synthetic signature and admission operation completed",
    }]
    view = measure.assess_verified_journal(store, node)["claims"][0]
    assert view["observation_coverage"] == "PRESENT"
    assert view["observation_count"] == 1
    assert view["descriptive_outcome"] == "VERIFIED_CRYPTOGRAPHIC_ADMISSION"


def test_crash_before_commit_publishes_neither_proof_nor_duration(node, arm, tmp_path):
    cfg, store, record = create(tmp_path, arm, node)
    before = store.snapshot(node)
    process = child(tmp_path, cfg, record, "before_commit")
    assert process.returncode == 51, process.stderr
    restarted = SyntheticClaimStore(**cfg)
    assert restarted.snapshot(node) == before
    result = admit(restarted, node, record)
    assert result["admitted"] is True
    assert restarted.snapshot(node)["claims"][0]["status"] == "ADMITTED"
    assert len(restarted.snapshot(node)["observations"]) == 1


def test_crash_after_commit_before_ack_persists_both_proof_and_measurement(
    node, arm, tmp_path,
):
    cfg, store, record = create(tmp_path, arm, node)
    process = child(tmp_path, cfg, record, "after_commit")
    assert process.returncode == 52, process.stderr
    restarted = SyntheticClaimStore(**cfg)
    snapshot = restarted.snapshot(node)
    assert snapshot["claims"][0]["status"] == "ADMITTED"
    assert len(snapshot["observations"]) == 1
    assert snapshot["observations"][0]["kind"] == "COMPLETED"
    assert snapshot["observations"][0]["elapsed_ms"] >= 0
    assert admit(restarted, node, record)["reason"] == "CLAIM_NOT_ACTIVE"
    assert restarted.snapshot(node) == snapshot
    assert measure.assess_verified_journal(restarted, node)["claims"][0][
        "observation_coverage"
    ] == "PRESENT"


def test_invalid_signature_cannot_commit_measurement_or_admission(node, arm, tmp_path):
    _, store, record = create(tmp_path, arm, node)
    before = store.snapshot(node)
    modified = dict(record)
    modified["statement"] = {**record["statement"], "decision": "REJECT"}
    result = admit(store, node, modified)
    assert result["admitted"] is False
    assert result["reason"] == "INVALID_RUN_PROOF"
    assert store.snapshot(node) == before


@pytest.mark.parametrize("wrong_start", [0, -1, "100", 1.5, True])
def test_invalid_monotonic_start_rejected_before_any_state_change(
    node, arm, tmp_path, wrong_start,
):
    _, store, record = create(tmp_path, arm, node)
    before = store.snapshot(node)
    with pytest.raises(ValueError, match="invalid synthetic monotonic"):
        admit(store, node, record, started_ns=wrong_start)
    assert store.snapshot(node) == before


def test_future_monotonic_start_rolls_back_admission_and_receipt(node, arm, tmp_path):
    _, store, record = create(tmp_path, arm, node)
    before = store.snapshot(node)
    with pytest.raises(ClaimStoreError, match="invalid synthetic measurement duration"):
        admit(store, node, record, started_ns=time.perf_counter_ns() + 10**13)
    assert store.snapshot(node) == before


def test_old_unmeasured_admission_remains_explicitly_missing_observation(
    node, arm, tmp_path,
):
    _, store, record = create(tmp_path, arm, node)
    result = store.admit(
        claim_nonce=record["statement"]["claim_nonce"],
        presented=record["statement"], proof=record["proof"],
        credential=record["credential"], node=node,
    )
    assert result["admitted"] is True
    report = measure.assess_verified_journal(store, node)["claims"][0]
    assert report["observation_coverage"] == "MISSING"
    assert report["descriptive_outcome"] == "VERIFIED_CRYPTOGRAPHIC_ADMISSION"
