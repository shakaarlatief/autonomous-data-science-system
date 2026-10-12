"""Synthetic trusted claim issuer with durable, run-bound admission.

This is a deliberately bounded successor integration experiment. It binds a
fresh random claim nonce, the precise expected signed statement, trusted
public signer identity and one-time acceptance in ONE SQLite database.

Security properties in scope:
- Explicit create vs reopen (missing/blank stores never silently reset).
- Immutable trusted genesis: historical statement template and signer.
- Issuance is a transactional operation: never infer expected context from a
  submitted signature. Exactly one currently ISSUED claim at a time.
- A newly issued claim supersedes any unfinished prior claim.
- Only a proof of the exact independently stored expected statement, under
  the originally trusted public credential, can be admitted.
- Rejections publish no changes. Once committed, replay is denied even after
  process death, including death before successful caller acknowledgement.
- Each stored accepted record is cryptographically reverified on restart.
- All nonces and signer keys are synthetic; no owner operation is available.

Not a production credential controller or ADS architecture decision:
- Caller-provided genesis trust is not yet backed by a hardware/owner root.
- No independent anti-rollback/anti-deletion anchor exists. File ownership,
  complete malicious rollback and power-failure behavior are outside tests.
- One acceptance per claim is a deliberately scoped experiment, not the full
  P0/S01... trial event workflow, scorer, burden measurement or recovery.
- SQLite and the historical nine-field template are replaceable choices.
"""
from __future__ import annotations

import copy
import hashlib
import re
import sqlite3
import time
from contextlib import closing
from pathlib import Path

from experiments.r0_p01_owner_acceptance_v01 import harness as legacy
from experiments.r0_p01_successor_synthetic import run_bound_acceptance as crypto


class ClaimStoreError(RuntimeError):
    """Durable trusted state is lost, inconsistent or unverifiable."""


class SyntheticClaimStore:
    VERSION = 2
    DOMAIN = b"ADS-R0-P01-SYNTHETIC-CLAIM-ISSUER-V01\0"

    def __init__(
        self, path: str | Path, *,
        issuer_id: str, legacy_template: dict, trusted_credential: dict,
        create: bool = False, require_governed_issuance: bool = False,
    ) -> None:
        if not isinstance(issuer_id,str) or re.fullmatch(
            r"SYNTHETIC-[A-Za-z0-9_-]{8,100}", issuer_id
        ) is None:
            raise ValueError("synthetic issuer identity required")
        if not legacy.valid_credential(trusted_credential):
            raise ValueError("invalid public signer identity")
        # Validate a synthetic example without creating or consuming a claim.
        crypto.new_run_statement(legacy_template, claim_nonce="0" * 64)
        if type(require_governed_issuance) is not bool:
            raise ValueError("governed issuance setting must be boolean")
        self.require_governed_issuance = require_governed_issuance
        self.path = Path(path)
        self.context = copy.deepcopy({
            "issuer_id": issuer_id,
            "template": legacy_template,
            "trusted_credential": trusted_credential,
            "protocol": crypto.PROTOCOL,
            "require_governed_issuance": require_governed_issuance,
        })
        self.context_blob = legacy.canonical(self.context)
        self.genesis = hashlib.sha256(self.DOMAIN + self.context_blob).hexdigest()
        if not self.path.parent.is_dir():
            raise ClaimStoreError("issuer directory missing")
        if create:
            try:
                self.path.touch(exist_ok=False)
            except FileExistsError as exc:
                raise ClaimStoreError("issuer database already exists") from exc
        elif not self.path.is_file():
            raise ClaimStoreError("missing issuer database; refusing to reset")
        self._initialize(create=create)

    def _connection(self):
        conn=sqlite3.connect(str(self.path),timeout=15,isolation_level=None)
        conn.execute("PRAGMA busy_timeout=15000")
        conn.execute("PRAGMA synchronous=FULL")
        conn.execute("PRAGMA foreign_keys=ON")
        return conn

    def _initialize(self, *, create: bool):
        with closing(self._connection()) as conn:
            try:
                conn.execute("PRAGMA journal_mode=WAL")
                conn.execute("BEGIN IMMEDIATE")
                conn.execute(
                    """CREATE TABLE IF NOT EXISTS identity(
                        id INTEGER PRIMARY KEY CHECK(id=1),
                        version INTEGER NOT NULL,
                        context_blob BLOB NOT NULL,
                        sequence INTEGER NOT NULL
                    )"""
                )
                conn.execute(
                    """CREATE TABLE IF NOT EXISTS claims(
                        seq INTEGER PRIMARY KEY CHECK(seq>0),
                        nonce TEXT UNIQUE NOT NULL,
                        expected_blob BLOB NOT NULL,
                        expected_sha256 TEXT NOT NULL,
                        status TEXT NOT NULL CHECK(status IN
                          ('ISSUED','SUPERSEDED','ADMITTED')),
                        admission_blob BLOB,
                        admission_sha256 TEXT
                    )"""
                )
                conn.execute(
                    """CREATE TABLE IF NOT EXISTS run_authorizations(
                        claim_seq INTEGER PRIMARY KEY
                          REFERENCES claims(seq),
                        authorization_blob BLOB NOT NULL,
                        authorization_sha256 TEXT NOT NULL
                    )"""
                )
                conn.execute(
                    """CREATE TABLE IF NOT EXISTS observations(
                        seq INTEGER PRIMARY KEY CHECK(seq>0),
                        claim_nonce TEXT NOT NULL REFERENCES claims(nonce),
                        kind TEXT NOT NULL CHECK(kind IN
                          ('INTERRUPTED','ERROR','COMPLETED')),
                        observation_blob BLOB NOT NULL,
                        observation_sha256 TEXT NOT NULL
                    )"""
                )
                row=conn.execute(
                    "SELECT version,context_blob,sequence FROM identity WHERE id=1"
                ).fetchone()
                if row is None:
                    if not create:
                        raise ClaimStoreError("no genesis on existing issuer database")
                    if conn.execute("SELECT 1 FROM claims LIMIT 1").fetchone():
                        raise ClaimStoreError("missing genesis with existing claims")
                    conn.execute(
                        "INSERT INTO identity VALUES(1,?,?,0)",
                        (self.VERSION,self.context_blob),
                    )
                else:
                    self._check_genesis(row)
                conn.commit()
            except Exception:
                conn.rollback()
                raise

    def _check_genesis(self,row):
        if (
            row[0] != self.VERSION or bytes(row[1]) != self.context_blob
            or type(row[2]) is not int or row[2] < 0
        ):
            raise ClaimStoreError("wrong issuer genesis or invalid sequence")

    def _checked(self,conn,node):
        """Rebuild the authoritative claim roster and verify admitted proofs.

        The claim expected message is reconstructed from immutable genesis
        and the stored nonce, so altering a saved expected document and its
        local SHA-256 together cannot make a different statement authoritative.
        """
        genesis=conn.execute(
            "SELECT version,context_blob,sequence FROM identity WHERE id=1"
        ).fetchone()
        if genesis is None:
            raise ClaimStoreError("issuer genesis missing")
        self._check_genesis(genesis)
        result=[]
        issued=0
        for seq,nonce,expected,expected_hash,status,admitted,admitted_hash in conn.execute(
            "SELECT seq,nonce,expected_blob,expected_sha256,status,"
            "admission_blob,admission_sha256 FROM claims ORDER BY seq"
        ):
            if seq!=len(result)+1 or not isinstance(nonce,str) or re.fullmatch(
                r"[0-9a-f]{64}",nonce
            ) is None or not isinstance(expected,bytes):
                raise ClaimStoreError("invalid durable claim identity/sequence")
            statement=crypto.new_run_statement(self.context["template"],claim_nonce=nonce)
            if expected!=legacy.canonical(statement):
                raise ClaimStoreError("trusted expected statement was modified")
            if hashlib.sha256(expected).hexdigest()!=expected_hash:
                raise ClaimStoreError("expected statement digest mismatch")
            if status not in {"ISSUED","SUPERSEDED","ADMITTED"}:
                raise ClaimStoreError("invalid persisted claim status")
            if status=="ISSUED":
                issued+=1
                if admitted is not None or admitted_hash is not None:
                    raise ClaimStoreError("unadmitted claim has proof data")
            elif status=="SUPERSEDED":
                if admitted is not None or admitted_hash is not None:
                    raise ClaimStoreError("superseded claim has accepted proof")
            else:
                if not isinstance(admitted,bytes) or not isinstance(admitted_hash,str):
                    raise ClaimStoreError("missing accepted proof")
                if hashlib.sha256(admitted).hexdigest()!=admitted_hash:
                    raise ClaimStoreError("accepted record integrity mismatch")
                try:
                    record=legacy.strict_json(admitted)
                    if legacy.canonical(record)!=admitted:
                        raise ClaimStoreError("noncanonical accepted proof")
                    if record["presented"]!=statement:
                        raise ClaimStoreError("admitted run identity not authoritative")
                    if record["credential"]!=self.context["trusted_credential"]:
                        raise ClaimStoreError("accepted signer not the trusted signer")
                    if not crypto.verify_for_run(
                        presented=record["presented"],trusted_expected=statement,
                        proof=record["proof"],credential=record["credential"],node=node,
                    ):
                        raise ClaimStoreError("persisted cryptographic proof invalid")
                except (ValueError,TypeError,KeyError,UnicodeError,legacy.IntegrityError) as exc:
                    raise ClaimStoreError("malformed persisted signed proof") from exc
            result.append({"seq":seq,"nonce":nonce,"statement":statement,"status":status})
        approvals={}
        for claim_seq,blob,proof_hash in conn.execute(
            "SELECT claim_seq,authorization_blob,authorization_sha256 "
            "FROM run_authorizations ORDER BY claim_seq"
        ):
            if (
                type(claim_seq) is not int or claim_seq < 1
                or claim_seq > len(result) or type(blob) is not bytes
                or hashlib.sha256(blob).hexdigest()!=proof_hash
            ):
                raise ClaimStoreError("invalid authorization evidence")
            try:
                auth=legacy.strict_json(blob)
            except (ValueError,UnicodeError,TypeError) as exc:
                raise ClaimStoreError("malformed authorization evidence") from exc
            if legacy.canonical(auth)!=blob or not self._valid_authorization(auth):
                raise ClaimStoreError("invalid authorization record")
            approvals[claim_seq]=auth
        if self.require_governed_issuance and len(approvals)!=len(result):
            raise ClaimStoreError("governed claim missing procedural authorization")
        if not self.require_governed_issuance and approvals:
            raise ClaimStoreError("ungoverned issuer cannot accept owner authorization evidence")
        for claim in result:
            claim["authorization_ref"]=(
                approvals[claim["seq"]]["authorization_ref"]
                if claim["seq"] in approvals else None
            )
        evidence=[]
        for seq,nonce,kind,blob,digest in conn.execute(
            "SELECT seq,claim_nonce,kind,observation_blob,"
            "observation_sha256 FROM observations ORDER BY seq"
        ):
            if (
                seq!=len(evidence)+1 or nonce not in {x["nonce"] for x in result}
                or kind not in {"INTERRUPTED","ERROR","COMPLETED"}
                or type(blob) is not bytes or
                hashlib.sha256(blob).hexdigest()!=digest
            ):
                raise ClaimStoreError("invalid durable observation")
            try:
                entry=legacy.strict_json(blob)
            except (ValueError,UnicodeError,TypeError) as exc:
                raise ClaimStoreError("malformed observation evidence") from exc
            if (
                legacy.canonical(entry)!=blob
                or not self._valid_observation(entry)
                or entry["kind"]!=kind or entry["claim_nonce"]!=nonce
            ):
                raise ClaimStoreError("observation record mismatch")
            evidence.append(entry)
        self._observations_cache=evidence
        if len(result)!=genesis[2] or issued>1:
            raise ClaimStoreError("issuer sequence or active claim invariant violated")
        if issued and result[-1]["status"]!="ISSUED":
            raise ClaimStoreError("active claim must be latest issued")
        if len({row["nonce"] for row in result})!=len(result):
            raise ClaimStoreError("duplicate claim identity")
        return result

    @staticmethod
    def _valid_authorization(auth):
        """Validate a caller-supplied synthetic procedural permission record.

        This is deliberately NOT an authenticity proof of a real human:
        production owner consent must come from the authenticated interaction
        or owner-controlled session, not an arbitrary JSON field.
        """
        return (
            type(auth) is dict
            and set(auth)=={"authorization_ref","purpose","replacement_of",
                           "approved","source"}
            and type(auth["authorization_ref"]) is str
            and re.fullmatch(
                r"SYNTHETIC-AUTH-[A-Z0-9-]{8,90}",
                auth["authorization_ref"],
            ) is not None
            and type(auth["purpose"]) is str
            and auth["purpose"] in {"NEW_RUN","REPLACEMENT"}
            and type(auth["source"]) is str
            and auth["source"]=="SYNTHETIC_TRUSTED_CONTROLLER"
            and auth["approved"] is True
            and (
                (auth["purpose"]=="NEW_RUN" and auth["replacement_of"] is None)
                or (auth["purpose"]=="REPLACEMENT" and
                    type(auth["replacement_of"]) is str and
                    re.fullmatch(r"[0-9a-f]{64}",auth["replacement_of"]) is not None)
            )
        )

    @staticmethod
    def _valid_observation(event):
        """Permit nonsecret synthetic factual records, not status overrides."""
        return (
            type(event) is dict
            and set(event)=={"claim_nonce","kind","elapsed_ms","interactions","note"}
            and type(event["claim_nonce"]) is str
            and re.fullmatch(r"[0-9a-f]{64}",event["claim_nonce"]) is not None
            and type(event["kind"]) is str
            and event["kind"] in {"INTERRUPTED","ERROR","COMPLETED"}
            and type(event["elapsed_ms"]) is int
            and 0 <= event["elapsed_ms"] <= 86_400_000
            and type(event["interactions"]) is int
            and 0 <= event["interactions"] <= 1_000_000
            and type(event["note"]) is str
            and 0 < len(event["note"]) <= 300
            and not any(x in event["note"].lower() for x in
                        ("passphrase","private key","password","secret key"))
        )

    @staticmethod
    def _commit(conn):
        """Deterministic crash injection seam for synthetic tests only."""
        conn.commit()

    def issue(self,node):
        """Atomically persist a fresh, trusted run before returning to signer.

        A second issuance invalidates an unfinished prior claim. This only
        models the *test* research controller, never real owner consent.
        """
        if self.require_governed_issuance:
            raise ClaimStoreError("governed issuer requires explicit authorization")
        return self._issue(node,authorization=None)

    def issue_governed(self,node,authorization:dict):
        """Issue only from a structurally valid trusted-controller decision.

        Caller authentication is deliberately outside this synthetic module.
        The record is not independently verified as a real owner identity.
        """
        if not self.require_governed_issuance:
            raise ClaimStoreError("governed issuance not enabled at genesis")
        if not self._valid_authorization(authorization):
            raise ClaimStoreError("explicit synthetic owner approval missing")
        return self._issue(node,authorization=authorization)

    def _issue(self,node,authorization):
        with closing(self._connection()) as conn:
            try:
                conn.execute("BEGIN IMMEDIATE")
                roster=self._checked(conn,node)
                if authorization is not None:
                    if authorization["purpose"]=="REPLACEMENT":
                        existing=next((r for r in roster if
                                       r["nonce"]==authorization["replacement_of"]),None)
                        if existing is None:
                            raise ClaimStoreError("replacement must reference prior claim")
                    if any(r["authorization_ref"]==authorization["authorization_ref"]
                           for r in roster):
                        raise ClaimStoreError("authorization reference already consumed")
                nonce=crypto.fresh_claim_nonce()
                if any(x["nonce"]==nonce for x in roster):
                    raise ClaimStoreError("random nonce collision; issuance refused")
                statement=crypto.new_run_statement(
                    self.context["template"],claim_nonce=nonce
                )
                blob=legacy.canonical(statement)
                conn.execute("UPDATE claims SET status='SUPERSEDED' WHERE status='ISSUED'")
                seq=len(roster)+1
                conn.execute(
                    "INSERT INTO claims VALUES(?,?,?,?,?,?,?)",
                    (seq,nonce,blob,hashlib.sha256(blob).hexdigest(),"ISSUED",None,None),
                )
                conn.execute("UPDATE identity SET sequence=? WHERE id=1",(seq,))
                if authorization is not None:
                    approval_blob=legacy.canonical(authorization)
                    conn.execute(
                        "INSERT INTO run_authorizations VALUES(?,?,?)",
                        (seq,approval_blob,hashlib.sha256(approval_blob).hexdigest())
                    )
                self._commit(conn)
                return copy.deepcopy(statement)
            except Exception:
                conn.rollback()
                raise

    def admit(
        self, *, claim_nonce: str, presented: dict, proof: dict,
        credential: dict, node, measurement_started_ns: int | None = None,
    ):
        """Admit only the trusted active claim exactly once, atomically.

        The claim_nonce is selected by the caller's trusted run controller,
        not recovered from the proof. The persisted expected statement is
        independently reconstructed from genesis and journal nonce.

        For the bounded synthetic measured-admission path, the controller
        passes a monotonic start time captured just before signing. The
        verified proof and elapsed time are committed together, removing the
        admission-then-observation gap. The duration ends before commit,
        therefore it does NOT measure SQLite fsync or the complete human
        ceremony. A caller-supplied start time is not an authenticated metric.
        """
        if measurement_started_ns is not None:
            if not self.require_governed_issuance:
                raise ValueError("measured admission requires governed synthetic issuer")
            if type(measurement_started_ns) is not int or measurement_started_ns <= 0:
                raise ValueError("invalid synthetic monotonic measurement start")
        with closing(self._connection()) as conn:
            try:
                conn.execute("BEGIN IMMEDIATE")
                roster=self._checked(conn,node)
                selected=next((x for x in roster if x["nonce"]==claim_nonce),None)
                if selected is None:
                    conn.rollback()
                    return {"admitted":False,"reason":"UNKNOWN_CLAIM"}
                if selected["status"]!="ISSUED":
                    conn.rollback()
                    return {"admitted":False,"reason":"CLAIM_NOT_ACTIVE"}
                if credential != self.context["trusted_credential"]:
                    conn.rollback()
                    return {"admitted":False,"reason":"UNTRUSTED_SIGNER"}
                if not crypto.verify_for_run(
                    presented=presented,trusted_expected=selected["statement"],
                    proof=proof,credential=credential,node=node,
                ):
                    conn.rollback()
                    return {"admitted":False,"reason":"INVALID_RUN_PROOF"}
                payload=legacy.canonical({
                    "presented":presented,"proof":proof,"credential":credential
                })
                conn.execute(
                    "UPDATE claims SET status='ADMITTED',"
                    "admission_blob=?,admission_sha256=? WHERE seq=? AND status='ISSUED'",
                    (payload,hashlib.sha256(payload).hexdigest(),selected["seq"]),
                )
                if conn.execute("SELECT changes()").fetchone()[0]!=1:
                    raise ClaimStoreError("admission compare-and-set failed")
                result={"admitted":True,"claim_nonce":claim_nonce}
                if measurement_started_ns is not None:
                    elapsed_ns=time.perf_counter_ns()-measurement_started_ns
                    if elapsed_ns < 0 or elapsed_ns//1_000_000 > 86_400_000:
                        raise ClaimStoreError("invalid synthetic measurement duration")
                    elapsed_ms=elapsed_ns//1_000_000
                    observation={
                        "claim_nonce":claim_nonce, "kind":"COMPLETED",
                        "elapsed_ms":elapsed_ms, "interactions":1,
                        "note":"Synthetic signature and admission operation completed",
                    }
                    if not self._valid_observation(observation):
                        raise ClaimStoreError("invalid synthetic completion observation")
                    observation_blob=legacy.canonical(observation)
                    observation_seq=len(self._observations_cache)+1
                    conn.execute(
                        "INSERT INTO observations VALUES(?,?,?,?,?)",
                        (observation_seq,claim_nonce,"COMPLETED",observation_blob,
                         hashlib.sha256(observation_blob).hexdigest()),
                    )
                    result["measured_elapsed_ms"]=elapsed_ms
                    result["observation_sequence"]=observation_seq
                self._commit(conn)
                return result
            except Exception:
                conn.rollback()
                raise

    def record_observation(self,*,claim_nonce:str,kind:str,elapsed_ms:int,
                           interactions:int,note:str,node):
        """Append a synthetic nonsecret observation without changing admission.

        Interrupted/error observations remain in history across replacement,
        and do not impersonate a valid cryptographic governing decision.
        """
        event={"claim_nonce":claim_nonce,"kind":kind,"elapsed_ms":elapsed_ms,
               "interactions":interactions,"note":note}
        if not self._valid_observation(event):
            raise ValueError("invalid or potentially sensitive observation")
        with closing(self._connection()) as conn:
            try:
                conn.execute("BEGIN IMMEDIATE")
                roster=self._checked(conn,node)
                if not any(r["nonce"]==claim_nonce for r in roster):
                    conn.rollback()
                    return {"recorded":False,"reason":"UNKNOWN_CLAIM"}
                seq=len(self._observations_cache)+1
                blob=legacy.canonical(event)
                conn.execute(
                    "INSERT INTO observations VALUES(?,?,?,?,?)",
                    (seq,claim_nonce,kind,blob,hashlib.sha256(blob).hexdigest())
                )
                self._commit(conn)
                return {"recorded":True,"observation_sequence":seq}
            except Exception:
                conn.rollback()
                raise

    def snapshot(self,node):
        """Return validated nonsecret issuer state after checking all proofs."""
        with closing(self._connection()) as conn:
            try:
                conn.execute("BEGIN")
                roster=self._checked(conn,node)
                view={
                    "issuer_id":self.context["issuer_id"],
                    "issued_count":len(roster),
                    "claims":[
                        {"nonce":x["nonce"],"status":x["status"],
                         "statement_sha256":legacy.digest(x["statement"]),
                         "authorization_ref":x["authorization_ref"]}
                        for x in roster
                    ],
                    "observations":copy.deepcopy(self._observations_cache),
                    "genesis_sha256":self.genesis,
                }
                conn.commit()
                return view
            except Exception:
                conn.rollback()
                raise
