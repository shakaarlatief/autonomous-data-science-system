"""Independent expected results for measured synthetic R0-P01 cases.

Cryptographic positive/negative checks use actual Windows OpenSSH Ed25519
and Node WebAuthn-shaped ES256 proofs from ephemeral non-owner test keys.
The expected descriptive result labels below are independently authored and
do not derive from the implementation's decision branches.
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

from experiments.r0_p01_owner_acceptance_v01 import harness as old
from experiments.r0_p01_successor_synthetic import run_bound_acceptance as crypto
from experiments.r0_p01_successor_synthetic import synthetic_measurement as measure
from experiments.r0_p01_successor_synthetic.trusted_claim_store import SyntheticClaimStore

ROOT = Path(old.HERE).parents[1]
TEMPLATE = json.loads(
    (Path(old.HERE) / "clarification_vectors_v02.json").read_text(encoding="utf-8")
)["statement"]


@pytest.fixture(scope="module")
def signer():
    if not shutil.which("node") or not shutil.which("ssh-keygen"):
        pytest.skip("Node and OpenSSH required for synthetic integration")
    with crypto.SyntheticRunCrypto() as node:
        yield node


@pytest.fixture(params=["SSH", "ES256"])
def arm(request, signer):
    method = "sign_ssh" if request.param == "SSH" else "sign_es256"
    label = "SYNTHETIC-NON-OWNER-MEASUREMENT-" + request.param
    seed = crypto.new_run_statement(TEMPLATE, claim_nonce="0" * 64)
    credential = signer.call(method, label=label, statement=seed)["credential"]
    return method, label, credential


def approval(ref: str, *, replacement_of=None):
    return {
        "authorization_ref": "SYNTHETIC-AUTH-MEASURE-" + ref,
        "purpose": "REPLACEMENT" if replacement_of else "NEW_RUN",
        "replacement_of": replacement_of,
        "approved": True,
        "source": "SYNTHETIC_TRUSTED_CONTROLLER",
    }


def prepare(tmp_path, arm):
    cfg = {
        "path": str(tmp_path / "measure.sqlite3"),
        "issuer_id": "SYNTHETIC-R0P01-MEASURE-ISSUER-001",
        "legacy_template": TEMPLATE,
        "trusted_credential": arm[2],
        "require_governed_issuance": True,
    }
    return cfg, SyntheticClaimStore(**cfg, create=True)


def execute(store, signer, arm, mode, ref, replacement_of=None):
    method, label, _ = arm
    return measure.run_measured_synthetic_case(
        store, signer, signer_method=method, signer_label=label,
        mode=mode, authorization=approval(ref, replacement_of=replacement_of),
    )


@pytest.mark.parametrize(
    ("mode", "outcome", "admitted", "calls", "kind"),
    [
        ("VALID", "VERIFIED_CRYPTOGRAPHIC_ADMISSION", True, 1, "COMPLETED"),
        ("INVALID_PROOF", "ERROR_WITHOUT_ADMISSION", False, 1, "ERROR"),
        ("INTERRUPTED", "INTERRUPTED_WITHOUT_ADMISSION", False, 0, "INTERRUPTED"),
    ],
)
def test_real_signature_state_drives_descriptive_outcome(
    signer, arm, tmp_path, mode, outcome, admitted, calls, kind,
):
    cfg, store = prepare(tmp_path, arm)
    result = execute(store, signer, arm, mode, "FIRST-RUN-0001")
    assert result["cryptographic_admitted"] is admitted
    assert result["observation_kind"] == kind
    assert result["scripted_signer_calls"] == calls
    assert type(result["measured_elapsed_ms"]) is int
    assert result["measured_elapsed_ms"] >= 0
    report = measure.assess_verified_journal(SyntheticClaimStore(**cfg), signer)
    assert report["claim_count"] == 1
    entry = report["claims"][0]
    assert entry["descriptive_outcome"] == outcome
    assert entry["observed_kinds"] == [kind]
    assert entry["recorded_signer_calls"] == calls
    assert entry["observed_elapsed_ms"] == result["measured_elapsed_ms"]
    assert entry["observation_count"] == 1
    assert entry["observation_coverage"] == "PRESENT"
    assert report["total_recorded_elapsed_ms"] == result["measured_elapsed_ms"]
    assert report["total_recorded_signer_calls"] == calls
    assert report["scope"] == "SYNTHETIC_DESCRIPTIVE_NOT_OWNER_OUTCOME_SCORER"


def test_interrupted_run_effort_survives_successful_replacement(signer, arm, tmp_path):
    cfg, store = prepare(tmp_path, arm)
    first = execute(store, signer, arm, "INTERRUPTED", "INTERRUPT-0001")
    second = execute(
        store, signer, arm, "VALID", "REPLACEMENT-0002",
        replacement_of=first["claim_nonce"],
    )
    report = measure.assess_verified_journal(SyntheticClaimStore(**cfg), signer)
    assert report["claim_count"] == 2
    assert [x["descriptive_outcome"] for x in report["claims"]] == [
        "SUPERSEDED_WITHOUT_ADMISSION",
        "VERIFIED_CRYPTOGRAPHIC_ADMISSION",
    ]
    assert report["claims"][0]["observed_kinds"] == ["INTERRUPTED"]
    assert report["claims"][0]["recorded_signer_calls"] == 0
    assert report["claims"][1]["observed_kinds"] == ["COMPLETED"]
    assert report["total_recorded_elapsed_ms"] == (
        first["measured_elapsed_ms"] + second["measured_elapsed_ms"]
    )


def test_completed_observation_without_signature_never_awards_success(signer, arm, tmp_path):
    _, store = prepare(tmp_path, arm)
    statement = store.issue_governed(signer, approval("NO-SIGNATURE-0001"))
    assert store.record_observation(
        claim_nonce=statement["claim_nonce"], kind="COMPLETED",
        elapsed_ms=99, interactions=1, note="Synthetic script ended", node=signer,
    )["recorded"]
    result = measure.assess_verified_journal(store, signer)["claims"][0]
    assert result["descriptive_outcome"] == "UNRESOLVED_WITHOUT_ADMISSION"
    assert result["admission_status"] == "ISSUED"
    assert result["observed_kinds"] == ["COMPLETED"]


def test_monotonic_latency_includes_actual_signer_delay(signer, arm, tmp_path):
    _, store = prepare(tmp_path, arm)
    class DelayedSigner:
        def call(self, method, **kwargs):
            if method in ("sign_ssh", "sign_es256"):
                time.sleep(0.035)
            return signer.call(method, **kwargs)
    result = execute(store, DelayedSigner(), arm, "VALID", "DELAYED-0001")
    assert result["cryptographic_admitted"] is True
    assert result["measured_elapsed_ms"] >= 30
    assert measure.assess_verified_journal(store, signer)["claims"][0][
        "observed_elapsed_ms"
    ] >= 30


def test_interruption_never_calls_synthetic_signer(signer, arm, tmp_path):
    _, store = prepare(tmp_path, arm)
    class RefuseSigner:
        def call(self, method, **kwargs):
            raise AssertionError("signing should not occur")
    result = execute(store, RefuseSigner(), arm, "INTERRUPTED", "NO-SIGN-0001")
    assert result["scripted_signer_calls"] == 0
    assert measure.assess_verified_journal(store, signer)["claims"][0][
        "descriptive_outcome"
    ] == "INTERRUPTED_WITHOUT_ADMISSION"


def test_signer_error_is_recorded_without_exception_details(signer, arm, tmp_path):
    cfg, store = prepare(tmp_path, arm)
    class FailedSigner:
        def call(self, method, **kwargs):
            raise RuntimeError("private key diagnostic text must not be persisted")
    result = execute(store, FailedSigner(), arm, "VALID", "SIGN-ERROR-0001")
    assert result["observation_kind"] == "ERROR"
    assert result["cryptographic_admitted"] is False
    observed = SyntheticClaimStore(**cfg).snapshot(signer)["observations"]
    assert len(observed) == 1
    assert "private key" not in observed[0]["note"]
    assert measure.assess_verified_journal(store, signer)["claims"][0][
        "descriptive_outcome"
    ] == "ERROR_WITHOUT_ADMISSION"


def test_invalid_rehearsal_requests_do_not_issue_claim(signer, arm, tmp_path):
    _, store = prepare(tmp_path, arm)
    params = {
        "store": store, "node": signer,
        "authorization": approval("BAD-INPUT-0001"),
        "signer_method": arm[0], "signer_label": arm[1], "mode": "VALID",
    }
    for changes in (
        {"mode": "REAL_OWNER"},
        {"signer_method": "owner_ssh"},
        {"signer_label": "OWNER-PRIMARY"},
    ):
        with pytest.raises(ValueError):
            measure.run_measured_synthetic_case(**{**params, **changes})
    assert store.snapshot(signer)["claims"] == []


def test_report_reverifies_admission_before_reporting_success(signer, arm, tmp_path):
    import sqlite3
    cfg, store = prepare(tmp_path, arm)
    result = execute(store, signer, arm, "VALID", "TAMPER-0001")
    assert result["cryptographic_admitted"]
    with sqlite3.connect(cfg["path"]) as conn:
        conn.execute(
            "UPDATE claims SET admission_sha256=? WHERE status='ADMITTED'",
            ("0" * 64,),
        )
    with pytest.raises(Exception, match="accepted record integrity mismatch"):
        measure.assess_verified_journal(store, signer)


def test_report_survives_new_python_process_without_private_signer(signer, arm, tmp_path):
    cfg, store = prepare(tmp_path, arm)
    execute(store, signer, arm, "VALID", "RESTART-0001")
    config_file = tmp_path / "config.json"
    config_file.write_bytes(old.canonical(cfg))
    worker = (
        "import json,sys,pathlib;"
        "from experiments.r0_p01_successor_synthetic.trusted_claim_store "
        "import SyntheticClaimStore;"
        "from experiments.r0_p01_successor_synthetic.run_bound_acceptance "
        "import SyntheticRunCrypto;"
        "from experiments.r0_p01_successor_synthetic.synthetic_measurement "
        "import assess_verified_journal;"
        "cfg=json.loads(pathlib.Path(sys.argv[1]).read_text(encoding='utf-8'));"
        "node=SyntheticRunCrypto();"
        "print(json.dumps(assess_verified_journal(SyntheticClaimStore(**cfg),node),"
        "sort_keys=True),flush=True);node.close()"
    )
    run = subprocess.run(
        [sys.executable, "-B", "-c", worker, str(config_file)],
        cwd=ROOT, capture_output=True, text=True, timeout=25,
        env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"},
    )
    assert run.returncode == 0, run.stderr
    assert json.loads(run.stdout) == measure.assess_verified_journal(store, signer)

def test_cryptographic_acceptance_without_evidence_is_flagged_incomplete(
    signer, arm, tmp_path,
):
    # Simulate a crash window after an atomic signature admission but
    # before the independent measurement observation is persisted.
    _, store = prepare(tmp_path, arm)
    statement = store.issue_governed(signer, approval("NO-MEASUREMENT-0001"))
    material = signer.call(arm[0], label=arm[1], statement=statement)
    assert store.admit(
        node=signer, claim_nonce=statement["claim_nonce"], presented=statement,
        proof=material["proof"], credential=arm[2],
    )["admitted"]
    view = measure.assess_verified_journal(store, signer)["claims"][0]
    assert view["descriptive_outcome"] == "VERIFIED_CRYPTOGRAPHIC_ADMISSION"
    assert view["observation_coverage"] == "MISSING"
    assert view["observation_count"] == 0
    assert view["observed_elapsed_ms"] == 0
    assert view["recorded_signer_calls"] == 0
