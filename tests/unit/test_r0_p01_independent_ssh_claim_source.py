"""Bounded source-vs-claim verification using a read-only SQLite consumer.

Expected classifications are authored here rather than copied from the
claim-store's output labels. Signing occurs only in the synthetic ephemeral
Node worker during fixture setup. The reader never starts a signer or accepts
a submitted verdict or event-terminal flag. Source trust is explicitly limited
to the configured local issuer journal as presented, not authenticated origin,
a proof of human presence, or externally witnessed anti-rollback.
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
from dataclasses import asdict
from pathlib import Path

import pytest

from experiments.r0_p01_owner_acceptance_v01 import harness as legacy
from experiments.r0_p01_successor_synthetic import run_bound_acceptance as rb
from experiments.r0_p01_successor_synthetic import independent_ssh_claim_source as source
from experiments.r0_p01_successor_synthetic.trusted_claim_store import SyntheticClaimStore

ROOT=Path(legacy.HERE).parents[1]
TEMPLATE=json.loads(
    (Path(legacy.HERE)/"clarification_vectors_v02.json").read_text(encoding="utf-8")
)["statement"]

@pytest.fixture(scope="module")
def signer():
    if not shutil.which("node") or not shutil.which("ssh-keygen"):
        pytest.skip("real Node and OpenSSH needed for non-owner source binding")
    with rb.SyntheticRunCrypto() as worker:
        probe=rb.new_run_statement(TEMPLATE,claim_nonce="0"*64)
        identity=worker.call(
            "sign_ssh",label="SYNTHETIC-NON-OWNER-READER-PRIMARY-001",statement=probe,
        )["credential"]
        outsider=worker.call(
            "sign_ssh",label="SYNTHETIC-NON-OWNER-READER-FOREIGN-001",statement=probe,
        )["credential"]
        assert identity != outsider
        yield worker,identity,outsider


def config(tmp_path,signer,*,governed=False):
    return {
        "path":str(tmp_path/"issuer.sqlite3"),
        "issuer_id":"SYNTHETIC-READONLY-CLAIM-ISSUER-001",
        "legacy_template":TEMPLATE,
        "trusted_credential":signer[1],
        "require_governed_issuance":governed,
    }


def authorization(*,number=1,replacement=None):
    return {
        "authorization_ref":f"SYNTHETIC-AUTH-READONLY-TEST-{number:04d}",
        "purpose":"REPLACEMENT" if replacement else "NEW_RUN",
        "replacement_of":replacement,
        "approved":True,
        "source":"SYNTHETIC_TRUSTED_CONTROLLER",
    }


def issue(store, signer, *, number=1, replacement=None):
    node=signer[0]
    if store.require_governed_issuance:
        return store.issue_governed(
            node, authorization(number=number,replacement=replacement)
        )
    return store.issue(node)


def sign(signer,statement, *, foreign=False):
    name="FOREIGN" if foreign else "PRIMARY"
    response=signer[0].call(
        "sign_ssh",
        label=f"SYNTHETIC-NON-OWNER-READER-{name}-001",
        statement=statement,
    )
    return response["proof"]


def admit(store,signer,statement, *, proof=None):
    return store.admit(
        claim_nonce=statement["claim_nonce"],presented=statement,
        credential=signer[1],
        proof=proof if proof is not None else sign(signer,statement),
        node=signer[0],
    )


def assess(tmp_path,cfg,statement,**changes):
    args={
        "journal_path":cfg["path"],
        "issuer_id":cfg["issuer_id"],
        "legacy_template":cfg["legacy_template"],
        "enrolled_credential":cfg["trusted_credential"],
        "require_governed_issuance":cfg["require_governed_issuance"],
        "trusted_claim_nonce":statement["claim_nonce"],
        "trusted_acceptance_id":statement["acceptance_id"],
        "scratch_root":tmp_path,
    }
    args.update(changes)
    return source.assess_ssh_claim(**args)


def mutate(db, statement, mutation):
    with sqlite3.connect(db) as conn:
        row=conn.execute(
            "SELECT admission_blob FROM claims WHERE nonce=?",
            (statement["claim_nonce"],),
        ).fetchone()
        assert row and row[0] is not None
        record=legacy.strict_json(row[0])
        mutation(record)
        changed=legacy.canonical(record)
        conn.execute(
            "UPDATE claims SET admission_blob=?,admission_sha256=? WHERE nonce=?",
            (changed,hashlib.sha256(changed).hexdigest(),statement["claim_nonce"]),
        )


def test_issued_only_cannot_be_relabelled_as_verified_proof(signer,tmp_path):
    cfg=config(tmp_path,signer)
    store=SyntheticClaimStore(**cfg,create=True)
    statement=issue(store,signer)
    out=assess(tmp_path,cfg,statement)
    assert (out.journal_status,out.proof_verification,out.admitted_proof_sha256)==(
        "ISSUED","NOT_RUN",None
    )
    assert out.source_origin_authenticated is False
    assert out.expected_statement_sha256==legacy.digest(statement)


def test_admitted_source_is_reverified_with_real_openssh(signer,tmp_path):
    cfg=config(tmp_path,signer)
    store=SyntheticClaimStore(**cfg,create=True)
    statement=issue(store,signer)
    proof=sign(signer,statement)
    assert admit(store,signer,statement,proof=proof)["admitted"] is True
    out=assess(tmp_path,cfg,statement)
    assert (out.journal_status,out.proof_verification)==("ADMITTED","VALID")
    assert out.claim_sequence==1
    assert len(out.admitted_proof_sha256)==64
    assert out.source_origin_authenticated is False
    assert not hasattr(out,"event_terminal")
    assert not hasattr(out,"evidence_state")


def test_fresh_process_reverifies_source_without_any_signer_invocation(
    signer,tmp_path,
):
    cfg=config(tmp_path,signer)
    store=SyntheticClaimStore(**cfg,create=True)
    statement=issue(store,signer)
    assert admit(store,signer,statement)["admitted"]
    public={
        "journal_path":cfg["path"],"issuer_id":cfg["issuer_id"],
        "legacy_template":TEMPLATE,"enrolled_credential":signer[1],
        "require_governed_issuance":False,
        "trusted_claim_nonce":statement["claim_nonce"],
        "trusted_acceptance_id":statement["acceptance_id"],
        "scratch_root":str(tmp_path),
    }
    input_path=tmp_path/"public-config.json"
    input_path.write_bytes(legacy.canonical(public))
    child="""
import json,sys
from dataclasses import asdict
from pathlib import Path
from experiments.r0_p01_successor_synthetic.independent_ssh_claim_source import assess_ssh_claim
inputs=json.loads(Path(sys.argv[1]).read_text(encoding='utf-8'))
print(json.dumps(asdict(assess_ssh_claim(**inputs)),sort_keys=True))
"""
    result=subprocess.run(
        [sys.executable,"-B","-c",child,str(input_path)],
        cwd=ROOT,capture_output=True,text=True,
        env={**os.environ,"PYTHONDONTWRITEBYTECODE":"1"},timeout=20,
    )
    assert result.returncode==0,result.stderr
    out=json.loads(result.stdout)
    assert out["proof_verification"]=="VALID"
    assert not out["source_origin_authenticated"]


@pytest.mark.parametrize("variant",["issuer","signer","acceptance","claim"])
def test_external_trust_inputs_not_overridden_by_db(signer,tmp_path,variant):
    cfg=config(tmp_path,signer)
    store=SyntheticClaimStore(**cfg,create=True)
    statement=issue(store,signer)
    assert admit(store,signer,statement)["admitted"]
    other={
        "issuer":{"issuer_id":"SYNTHETIC-READONLY-DIFFERENT-ISSUER"},
        "signer":{"enrolled_credential":signer[2]},
        "acceptance":{"trusted_acceptance_id":"R0-P01-UNKNOWN"},
        "claim":{"trusted_claim_nonce":"f"*64},
    }[variant]
    with pytest.raises(source.UnqualifiedSourceError):
        assess(tmp_path,cfg,statement,**other)


def test_missing_source_is_never_reinitialized(signer,tmp_path):
    cfg=config(tmp_path,signer)
    statement=rb.new_run_statement(TEMPLATE,claim_nonce="1"*64)
    with pytest.raises(source.UnqualifiedSourceError,match="missing journal"):
        assess(tmp_path,cfg,statement)
    assert not Path(cfg["path"]).exists()


def test_admission_status_without_any_proof_is_not_cryptographic_evidence(
    signer,tmp_path,
):
    cfg=config(tmp_path,signer)
    store=SyntheticClaimStore(**cfg,create=True)
    statement=issue(store,signer)
    with sqlite3.connect(cfg["path"]) as conn:
        conn.execute("UPDATE claims SET status='ADMITTED'")
    with pytest.raises(source.UnqualifiedSourceError,match="admitted proof"):
        assess(tmp_path,cfg,statement)


@pytest.mark.parametrize("change",["decision","nonce","signer","signature"])
def test_tampered_admission_fails_despite_recomputed_local_hash(
    signer,tmp_path,change,
):
    cfg=config(tmp_path,signer)
    store=SyntheticClaimStore(**cfg,create=True)
    statement=issue(store,signer)
    assert admit(store,signer,statement)["admitted"]
    def alter(record):
        if change=="decision":
            record["presented"]["decision"]="REJECT"
        elif change=="nonce":
            record["presented"]["claim_nonce"]="a"*64
        elif change=="signer":
            record["credential"]=signer[2]
        else:
            record["proof"]["sshsig"]=sign(signer,rb.new_run_statement(
                TEMPLATE,claim_nonce="f"*64
            ))["sshsig"]
    mutate(cfg["path"],statement,alter)
    with pytest.raises(source.UnqualifiedSourceError):
        assess(tmp_path,cfg,statement)


def test_expected_statement_plus_digest_rewrite_is_detected(signer,tmp_path):
    cfg=config(tmp_path,signer)
    store=SyntheticClaimStore(**cfg,create=True)
    statement=issue(store,signer)
    assert admit(store,signer,statement)["admitted"]
    changed=legacy.canonical({**statement,"decision":"REJECT"})
    with sqlite3.connect(cfg["path"]) as conn:
        conn.execute(
            "UPDATE claims SET expected_blob=?,expected_sha256=?",
            (changed,hashlib.sha256(changed).hexdigest()),
        )
    with pytest.raises(source.UnqualifiedSourceError,match="stored expected"):
        assess(tmp_path,cfg,statement)


def test_corrupt_unrelated_earlier_proof_invalidates_selected_clean_claim(
    signer,tmp_path,
):
    cfg=config(tmp_path,signer)
    store=SyntheticClaimStore(**cfg,create=True)
    first=issue(store,signer)
    assert admit(store,signer,first)["admitted"]
    second=issue(store,signer)
    assert admit(store,signer,second)["admitted"]
    assert assess(tmp_path,cfg,second).proof_verification=="VALID"
    mutate(cfg["path"],first,lambda record:record["presented"].update(
        {"decision":"REJECT"}
    ))
    with pytest.raises(source.UnqualifiedSourceError):
        assess(tmp_path,cfg,second)


def test_superseded_unadmitted_claim_stays_not_run(signer,tmp_path):
    cfg=config(tmp_path,signer)
    store=SyntheticClaimStore(**cfg,create=True)
    first=issue(store,signer)
    second=issue(store,signer)
    assert first["claim_nonce"]!=second["claim_nonce"]
    a=assess(tmp_path,cfg,first)
    b=assess(tmp_path,cfg,second)
    assert (a.journal_status,a.proof_verification)==("SUPERSEDED","NOT_RUN")
    assert (b.journal_status,b.proof_verification)==("ISSUED","NOT_RUN")


def test_real_governed_synthetic_approval_remains_unattested_owner_consent(
    signer,tmp_path,
):
    cfg=config(tmp_path,signer,governed=True)
    store=SyntheticClaimStore(**cfg,create=True)
    statement=issue(store,signer)
    assert admit(store,signer,statement)["admitted"]
    observed=assess(tmp_path,cfg,statement)
    assert observed.proof_verification=="VALID"
    assert observed.source_origin_authenticated is False


def test_substituted_invalid_authorization_fails_even_with_new_hash(
    signer,tmp_path,
):
    cfg=config(tmp_path,signer,governed=True)
    store=SyntheticClaimStore(**cfg,create=True)
    statement=issue(store,signer)
    assert admit(store,signer,statement)["admitted"]
    with sqlite3.connect(cfg["path"]) as conn:
        a=conn.execute("SELECT authorization_blob FROM run_authorizations").fetchone()[0]
        obj=legacy.strict_json(a)
        obj["approved"]=False
        data=legacy.canonical(obj)
        conn.execute("UPDATE run_authorizations SET authorization_blob=?,authorization_sha256=?",
                     (data,hashlib.sha256(data).hexdigest()))
    with pytest.raises(source.UnqualifiedSourceError,match="authorization"):
        assess(tmp_path,cfg,statement)


def test_corrupt_observation_rejected_without_claiming_event_truth(signer,tmp_path):
    cfg=config(tmp_path,signer)
    store=SyntheticClaimStore(**cfg,create=True)
    statement=issue(store,signer)
    assert admit(store,signer,statement)["admitted"]
    assert store.record_observation(
        claim_nonce=statement["claim_nonce"],kind="INTERRUPTED",
        elapsed_ms=8,interactions=1,note="SYNTHETIC_INTERRUPTED",node=signer[0],
    )["recorded"]
    with sqlite3.connect(cfg["path"]) as conn:
        a=conn.execute("SELECT observation_blob FROM observations").fetchone()[0]
        obj=legacy.strict_json(a)
        obj["elapsed_ms"]=-1
        data=legacy.canonical(obj)
        conn.execute(
            "UPDATE observations SET observation_blob=?,observation_sha256=?",
            (data,hashlib.sha256(data).hexdigest()),
        )
    with pytest.raises(source.UnqualifiedSourceError,match="observation"):
        assess(tmp_path,cfg,statement)


def test_native_verifier_outage_never_becomes_invalid_owner_proof(
    signer,tmp_path,monkeypatch,
):
    cfg=config(tmp_path,signer)
    store=SyntheticClaimStore(**cfg,create=True)
    statement=issue(store,signer)
    assert admit(store,signer,statement)["admitted"]
    observer=source.observe_ssh_verification
    def broken(**kwargs):
        from experiments.r0_p01_successor_synthetic.trusted_ssh_observation import SSHVerificationObservation
        return SSHVerificationObservation(
            "ERROR","VERIFIER_FAILURE","0"*64,None,signer[1]["public_id"],None,
        )
    monkeypatch.setattr(source,"observe_ssh_verification",broken)
    with pytest.raises(source.UnqualifiedSourceError,match="presently valid"):
        assess(tmp_path,cfg,statement)
    monkeypatch.setattr(source,"observe_ssh_verification",observer)
    assert assess(tmp_path,cfg,statement).proof_verification=="VALID"


def test_reading_source_does_not_change_issuer_records(signer,tmp_path):
    cfg=config(tmp_path,signer)
    store=SyntheticClaimStore(**cfg,create=True)
    statement=issue(store,signer)
    assert admit(store,signer,statement)["admitted"]
    def dump():
        with sqlite3.connect(cfg["path"]) as conn:
            return (
                conn.execute("SELECT * FROM identity").fetchall(),
                conn.execute("SELECT * FROM claims").fetchall(),
                conn.execute("SELECT * FROM observations").fetchall(),
            )
    before=dump()
    out=assess(tmp_path,cfg,statement)
    assert out.proof_verification=="VALID"
    assert dump()==before


def test_valid_signature_cannot_prove_journal_writer_or_actual_admission(
    signer,tmp_path,
):
    """Demonstrate the remaining provenance gap with a real valid proof.

    A hostile local journal writer can insert an already valid SSH signature
    and forge the unkeyed admission status/hash without using the issuer's
    admit() method. The consumer can cryptographically reverify that signature
    as presented, but it cannot establish who wrote the journal record or
    when/why it was admitted. This is a limitation witness, not success of
    genuine source-origin authentication.
    """
    cfg=config(tmp_path,signer)
    store=SyntheticClaimStore(**cfg,create=True)
    statement=issue(store,signer)
    proof=sign(signer,statement)
    assert store.snapshot(signer[0])["claims"][0]["status"]=="ISSUED"
    # Deliberately bypass trusted store.admit(): status/proof material is
    # written directly into the synthetic local store by the test adversary.
    injected=legacy.canonical({
        "presented":statement,"proof":proof,"credential":signer[1],
    })
    with sqlite3.connect(cfg["path"]) as conn:
        conn.execute(
            "UPDATE claims SET status='ADMITTED',admission_blob=?,admission_sha256=? "
            "WHERE nonce=? AND status='ISSUED'",
            (injected,hashlib.sha256(injected).hexdigest(),statement["claim_nonce"]),
        )
    observed=assess(tmp_path,cfg,statement)
    assert observed.proof_verification=="VALID"
    assert observed.journal_status=="ADMITTED"
    assert observed.source_origin_authenticated is False
    assert not hasattr(observed,"event_terminal")
    assert not hasattr(observed,"owner_authorized")
