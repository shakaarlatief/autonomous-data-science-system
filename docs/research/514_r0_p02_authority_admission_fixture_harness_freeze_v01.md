# Research 514: R0-P02 exact authority-admission fixture and harness freeze V0.1

**Date:** 2026-10-04
**Status:** R0-P02 EXACT FIXTURE / ORACLE / CANDIDATE CONTRACT / SCORER FROZEN / NO CANDIDATE RESULT OBSERVED / BOUNDED IMPLEMENTATION NEXT
**Parent:** Research 512-513
**Candidate under test:** GOVERNED_LEDGER_KERNEL_V02
**Probe:** R0-P02
**Scope:** Freeze the exact deterministic fixture, expected-result oracle, implementation contract, scorer, live-host transport leg and implementation blindness boundary before candidate implementation or result observation.
**Authority:** Probe-fixture preregistration only. No R0-P02 result, physical target selection, production implementation, migration, Specification 028 amendment, Runtime Bridge extraction, or authority switch is authorized.

## 1. Frozen files

The deterministic R0-P02 probe surface is frozen under:

    experiments/r0_p02_authority_admission_v01/

Exact frozen inputs:

    fixture.json
        SHA-256 dda68b1f4368dc982edffa2718330032f69842e7ac490dd84cbaaadcd4740d23
        bytes 3156

    oracle.json
        SHA-256 ea059f0482298b21e290aa2b87823122d2ff1c583728bacbaa0c0568a17fdba4
        bytes 2352

    candidate_contract.md
        SHA-256 bad3e5f0adb74c9887d0cb68d290e1a2534af5b836ad4a036bb0f4838106fa52
        bytes 1966

    score.py
        SHA-256 616bbce9571b69cbefd7419fb0ab64de4919309122fc5719fcec68fab4fa07d8
        bytes 5107

The scorer has been syntax-compiled only.

No candidate.py exists at freeze time.

No probe score has been produced.

## 2. Probe-only representation disclaimer

The deterministic core uses:

    PROBE_JSON_V01_SORTED_KEYS_COMPACT_UTF8_TEST_ONLY
    TEST_HMAC_SHA256_NOT_PRODUCTION

These are intentionally synthetic probe mechanisms.

They do not select:

    production canonicalization
    production owner cryptography
    production key storage
    production serialization

R0-P01 owns real owner-exclusive cryptography and UX.

R1 later owns canonicalization conformance qualification.

R0-P02 uses synthetic signing only to isolate admission/order/staleness/tamper semantics from credential-product choice.

## 3. Exact deterministic case set

The frozen fixture contains exactly 20 cases:

    C01 GENESIS_VALID
    C02 BASE_ACCEPTANCE_VALID
    C03 UNRELATED_NON_GOVERNING_DOES_NOT_STALE
    C04 UNRELATED_GOVERNING_DOES_NOT_STALE
    C05 CONFLICT_A_ADMITS
    C06 CONFLICT_B_STALE_AFTER_A
    C07 FORGED_SIGNATURE_REJECT
    C08 CHANGED_ENVELOPE_REJECT
    C09 DECISION_SUBSTITUTION_REJECT
    C10 CROSS_PROJECT_REPLAY_REJECT
    C11 ACCEPTANCE_ID_REPLAY_REJECT
    C12 DUPLICATE_SEQUENCE_REJECT
    C13 BROKEN_PREV_DIGEST_REJECT
    C14 MIDDLE_CHAIN_REWRITE_DETECT
    C15 HOST_TRANSFORM_INVARIANT
    C16 RECOVER_NOT_STARTED
    C17 RECOVER_DONE_NO_DUPLICATE
    C18 PRIOR_WITNESS_TRUNCATION_DETECT
    C19 FRESH_VERIFIER_TRUNCATION_LIMIT
    C20 EXTERNAL_HEAD_WITNESS_TRUNCATION_DETECT

The expected primary outcomes and latestness classes are frozen in oracle.json.

## 4. Fresh-verifier limitation is part of the oracle

C19 is not a defect case.

Its required output is:

    outcome       CHAIN_VALID
    latestness    LATESTNESS_UNPROVEN

That is deliberate.

A fresh verifier with only:

    configured genesis trust
    one presented repository snapshot

can verify the authenticity and internal continuity of the chain presented.

It cannot prove the non-existence of a later valid checkpoint that an adversarial carrier has suppressed.

The candidate must not overclaim.

C18 and C20 prove that rollback becomes detectable when a trusted prior/out-of-band head witness is supplied.

## 5. Candidate implementation boundary

The only candidate implementation file is:

    experiments/r0_p02_authority_admission_v01/candidate.py

It must expose:

    evaluate_fixture(fixture: dict) -> dict

and satisfy candidate_contract.md.

The implementation is experimental architecture-probe code only.

It is not a production Project-system implementation.

## 6. Implementation blindness

The bounded implementer may read:

    Research 512
    Research 513
    Research 514
    experiments/r0_p02_authority_admission_v01/fixture.json
    experiments/r0_p02_authority_admission_v01/candidate_contract.md

The implementer must not inspect before candidate.py is frozen:

    experiments/r0_p02_authority_admission_v01/oracle.json
    experiments/r0_p02_authority_admission_v01/score.py
    any score/result file
    any later repair/result artifact

The implementer may:

    syntax-check candidate.py
    run its own non-oracle smoke checks
    inspect fixture.json

The implementer may not:

    call score.py
    derive expected outcomes from oracle.json
    modify fixture.json
    modify candidate_contract.md
    modify Research 513/514
    modify production Project-system code

If accidental oracle/scorer exposure occurs, stop and report it before scoring. The task owner decides attempt validity.

## 7. Scorer controls

score.py prospectively freezes:

    exact output schema validation
    exact fixture-order requirement
    exact outcome/latestness comparison
    64-lowercase-hex-or-null digest validation
    identical-run determinism check
    renamed-case metamorphic check
    alternate-project/secret metamorphic check

The renamed-case metamorphic check prevents a candidate that maps literal case IDs directly to oracle outputs from passing.

The alternate-context metamorphic check requires the mechanism to survive different synthetic project IDs and synthetic secret material.

A deterministic-core PASS requires zero scorer errors.

## 8. Candidate authorship and repair rule

One bounded candidate implementation attempt is authorized after this freeze.

If candidate.py has a syntax/runtime defect before score.py is run:

    repair is permitted
    repair must be frozen before first score observation

Once score.py is run:

    result is observed
    candidate.py is frozen for that attempt
    no result-guided repair to the same attempt is permitted

A failure may trigger a prospectively frozen Attempt 002 only if the failure is classified as:

    harness/implementation defect
    rather than evidence against the architecture mechanism

and the repair rule is frozen before Attempt 002 scoring.

There is no retry-to-green.

## 9. Deterministic-core PASS condition

The deterministic core passes only if:

    score.py exits 0
    deterministic_core = PASS
    error_count = 0
    20/20 frozen cases match
    both metamorphic checks pass

The score output is insufficient by itself to classify full R0-P02.

The live-host leg remains required.

## 10. Live-host transport leg

After deterministic-core PASS, run exactly one bounded real-host transport qualification through Runtime Bridge GitHub surfaces.

It must not modify the coordination branch.

Temporary refs:

    base branch
        r0-p02-host-v01-base

    work branch
        r0-p02-host-v01-work

Both are created from the exact coordination-branch head that contains the frozen passing candidate result boundary.

### 10.1 Payload

The work branch receives exactly one new probe payload path:

    experiments/r0_p02_authority_admission_v01/host_probe_payload.json

The payload contains:

    protocol = R0-P02-V01
    project_id = ADS-R0-P02-SYNTHETIC
    acceptance_id = HOST-PROBE-001
    envelope_digest
    shown_digest
    semantic_base_digest
    decision = ACCEPT
    signer_set_version = SIGNERS-V1
    detached_test_proof

The proof remains TEST_HMAC_SHA256 probe-only material.

No production credential is used.

### 10.2 Host operation

Through Runtime Bridge GitHub connector capability:

    create base branch
    create work branch
    create host_probe_payload.json on work branch
    open PR work -> base
    verify PR head
    squash-merge PR into base
    fetch merged payload bytes
    verify semantic/proof bytes and digests remain exact despite commit transformation
    verify coordination branch head is unchanged
    delete work branch if still present
    delete base branch

If cleanup is interrupted, the exact temporary refs are fail-visible and must be cleaned before probe closure.

### 10.3 Live-host PASS gates

The live-host leg passes only if:

    payload content survives squash merge exactly
    work commit identity changes or is not relied upon
    detached proof validity is unchanged
    coordination branch is unchanged
    no production authority surface changes
    connector-only transport succeeds
    cleanup succeeds or leaves an exact recoverable cleanup obligation

A GitHub/host outage is infrastructure failure, not architecture failure.

An inability to preserve/verify the detached semantic proof through normal host transformation is architecture evidence.

## 11. Host serialization interpretation

The live-host leg does not claim that GitHub branch protection or merge queues are semantic authority.

It tests only:

    provider transport
    connector-only contribution
    commit transformation independence
    exact payload preservation

Serialized semantic admission remains the Project-system rule from Research 512.

A future R1 workflow may realize serialization through:

    merge queue
    bounded promotion controller
    another qualified exact-result mechanism

without changing J1 authority.

## 12. Full R0-P02 classification

After deterministic and live-host legs:

    PASS
        deterministic core passes
        live-host leg passes
        Research-512 same-repository chain/checkpoint threat model is sufficient without an additional selected witness

    PASS_WITH_SELECTION
        deterministic and live-host legs pass
        one bounded external/remembered witness variant is selected for required rollback freshness

    AMEND
        Git family survives but witness/checkpoint/promotion mechanics require a bounded architecture amendment

    REOPEN
        deterministic authority/order/tamper semantics cannot be realized over Git proportionately or require a second semantic authority/correctness-critical service

    INVALID
        blindness, fixture, oracle, scorer, repair or attempt-integrity contract is violated

No full classification may be issued before both legs are complete.

## 13. Exact next action

Use a bounded implementation agent to author only:

    experiments/r0_p02_authority_admission_v01/candidate.py

under the blindness boundary in Section 6.

After the candidate is frozen, task owner independently verifies:

    only candidate.py changed
    oracle/scorer blindness attestation
    syntax/runtime readiness without scoring

Only then may score.py be run once for Attempt 001.

## 14. Current boundary

    R0_P02_PROTOCOL=RESEARCH_513
    R0_P02_FIXTURE=FROZEN_V01
    R0_P02_CANDIDATE=NOT_IMPLEMENTED
    R0_P02_RESULT=NOT_OBSERVED

    FIXTURE_SHA256=dda68b1f4368dc982edffa2718330032f69842e7ac490dd84cbaaadcd4740d23
    ORACLE_SHA256=ea059f0482298b21e290aa2b87823122d2ff1c583728bacbaa0c0568a17fdba4
    CONTRACT_SHA256=bad3e5f0adb74c9887d0cb68d290e1a2534af5b836ad4a036bb0f4838106fa52
    SCORER_SHA256=616bbce9571b69cbefd7419fb0ab64de4919309122fc5719fcec68fab4fa07d8

    PHYSICAL_ARCHITECTURE_SELECTED=false
    IMPLEMENTATION_STARTED=false
    MIGRATION_AUTHORIZED=false
    SPECIFICATION_028_AUTHORITY=UNCHANGED

    NEXT=BOUNDED_CODEX_R0_P02_CANDIDATE_IMPLEMENTATION
