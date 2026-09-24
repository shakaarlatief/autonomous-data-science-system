# Research 293: P-D1 Warrant-Proportionality Result

**Date:** 2026-09-24
**Status:** P-D1 PASS / SELECTIVE WARRANT MODEL SUPPORTED / NO OWNER ASSURANCE DECISION
**Parent protocol:** Research 277
**Claim-set freeze:** Research 291
**Harness freeze:** Research 292
**Frozen harness commit:** 733e55796beed3cd07f4017e4f3718e3a2e2f943
**Frozen source commit:** 1a095044282622f2ce9e2bd38b90d77b8be8a4a2
**Probe:** P-D1
**Candidate:** WARRANT-F V0.2
**Scope:** Record the frozen-harness execution result for warrant proportionality.
**Authority:** Empirical architecture evidence only.

## 1. Result

Observed:

    P-D1
    result                         PASS
    first-class claims             12
    covered suite test functions  160
    invariant warrants             4
    sampled Product mutations      4 / 4 killed

Durable evidence:

    experiments/r8c_assurance_probe_v01/evidence/p_d1_run_001.json

The result self-binds to the exact harness/source commits and Git-blob hashes frozen by Research 292.

## 2. Selective claim grain

The twelve first-class claims remain:

    4 invariant
    4 suite
    4 cross-boundary

The four suite claims cover:

    S1 Product reasoning                 4 test functions
    S2 Product context selection         2
    S3 JW1 semantic family             134
    S4 repository integrity             20

Total:

    160 current test functions
    12 first-class assurance claims

Therefore the candidate does not require one first-class claim per test.

This is evidence that selective semantic assurance claims can aggregate ordinary test families.

## 3. Invariant warrants

All four preregistered invariant claims executed:

    one sensitivity witness
    one specificity / valid-near-miss witness

All eight executions passed.

Claims:

    I1 noncanonical authority exclusion
    I2 duplicate current identity ownership rejection
    I3 stale capture-promotion target rejection
    I4 known-private-value public nonleakage

Each warrant remains scoped narrowly to the property actually witnessed.

No broader semantic family is upgraded to fully warranted merely because one invariant witness passes.

## 4. Suite-warrant mutation adequacy

The Product reasoning suite baseline passed.

The four fixed mutations were all killed:

    M1 expected nonce field removed
    M2 duplicate output-list guard disabled
    M3 unsupported methodological-basis guard disabled
    M4 duplicate knowledge-key guard disabled

Observed:

    kill rate = 4 / 4 = 1.0

This does not prove universal Product-reasoning defect detection.

It demonstrates the architecture discriminator:

> one suite claim can carry bounded executable sensitivity evidence without creating one first-class claim per test.

## 5. Coverage honesty

Warrant status counts:

    FULL_FOR_DECLARED_SCOPE  4
    PARTIALLY_WARRANTED      8

The partial status is intentional for broad suite/cross-boundary claims whose complete scope is not established by P-D1.

This supports the WARRANT-F rule:

    witnessed scope < declared broader scope
        -> PARTIALLY_WARRANTED

rather than overstating assurance.

## 6. Maintenance proportionality

The frozen warrant catalog contains zero triggers requiring re-witnessing on ordinary unrelated test edits.

Re-witness triggers are tied to:

    semantic verifier changes
    declared-input changes
    witness changes
    claim-scope changes
    material suite redesign
    suite-health triggers
    later dependent empirical evidence

This directly addresses Claude's Message 003 concern that the original warrant rule would re-witness an entire suite on almost every edit.

## 7. Scope limits

P-D1 does not establish:

    optimal claim taxonomy for all future ADS assurance
    a universal mutation-testing cadence
    a numeric mutation-score threshold
    final warrant storage representation
    final Project Engineering implementation
    complete warrant coverage of all 160 current tests

Those remain realization/evolution questions.

## 8. Result class

Under Research 277:

    P_D1=PASS
    TARGET_ARCHITECTURE_EVIDENCE=SUPPORTED
    TARGET_ARCHITECTURE_AMENDMENT_REQUIRED=false

WARRANT-F V0.2 requires no amendment from P-D1.

## 9. Current state

    P_H=INCONCLUSIVE
    P_D6=PASS
    P_D3=PASS
    P_D5=PASS
    P_D1=PASS

    COMPLETED_VALID_OR_SCOPED_PROBES=5_OF_8
    UNRESOLVED_AMEND_RESULTS=0
    HARNESS_INVALID_ACTIVE_RESULTS=0

    OWNER_ASSURANCE_DECISION=HELD
    NEXT=P_D2_RATCHET_HISTORY
