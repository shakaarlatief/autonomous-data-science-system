# R0-P02 Attempt 002 Output Classification Contract

**Status:** PROSPECTIVELY FROZEN ATTEMPT 002 REPAIR CONTRACT
**Parent:** Research 515
**Scope:** Publish the canonical result vocabulary and semantic normalization rules that were missing from the blinded Attempt 001 candidate contract. This contract does not change the fixture, oracle, scorer, thresholds, negative controls, or authority-admission mechanism.

## 1. Canonical outcome vocabulary

Attempt 002 must report outcomes using only these scorer-facing classes when applicable:

    ADMITTED
    STALE_SEMANTIC_BASE
    INVALID_SIGNATURE
    WRONG_PROJECT
    DUPLICATE_ACCEPTANCE
    INVALID_SEQUENCE
    CHAIN_BREAK
    PROOF_UNCHANGED
    NOT_STARTED
    DONE_NO_DUPLICATE
    ROLLBACK_DETECTED
    CHAIN_VALID

Internal implementation exceptions/reasons may be more specific. The returned `outcome` is the canonical external classification.

## 2. Canonical latestness vocabulary

Attempt 002 must report latestness using only:

    VALID_AS_PRESENTED
    NOT_APPLICABLE
    STALE
    LATESTNESS_UNPROVEN

Latestness is a separate dimension from the primary outcome.

## 3. General normalization rules

These rules apply by semantic condition, never by literal case_id.

### 3.1 Successful presented/admitted state

When the tested operation successfully establishes or verifies the intended presented state and no freshness limitation or rollback witness changes that interpretation:

    latestness = VALID_AS_PRESENTED

Successful ordinary governing admission reports:

    outcome = ADMITTED

### 3.2 Signed semantic content or decision changed under an old proof

If the detached proof no longer authenticates the semantic object/decision that is being presented, including a changed envelope or substituted decision:

    outcome = INVALID_SIGNATURE
    latestness = NOT_APPLICABLE

An implementation may internally detect an envelope-digest mismatch, shown-digest mismatch, or decision-binding mismatch. Those are internal reasons under the canonical external INVALID_SIGNATURE class.

### 3.3 Wrong project

If an otherwise signed packet is bound to another project identity:

    outcome = WRONG_PROJECT
    latestness = NOT_APPLICABLE

### 3.4 Semantic stale base

If a validly authenticated acceptance was prepared against a semantic dependency state that is no longer current:

    outcome = STALE_SEMANTIC_BASE

When this occurs as the expected conflict result after another valid admission, the presented ledger/state itself remains:

    latestness = VALID_AS_PRESENTED

### 3.5 Duplicate acceptance

If an already-folded acceptance identity is presented again:

    outcome = DUPLICATE_ACCEPTANCE
    latestness = VALID_AS_PRESENTED

The existing presented ledger remains valid; the duplicate operation is rejected.

### 3.6 Ledger ordering and chain integrity

A duplicate/non-contiguous ledger sequence reports:

    outcome = INVALID_SEQUENCE
    latestness = NOT_APPLICABLE

A broken previous-entry binding, rewritten middle history, or equivalent chain-binding/history-integrity failure reports:

    outcome = CHAIN_BREAK
    latestness = NOT_APPLICABLE

Internal reasons such as BROKEN_PREV_DIGEST, ENTRY_DIGEST_MISMATCH, or ENVELOPE_DIGEST_MISMATCH during chain replay may remain diagnostic only.

### 3.7 Host transform independence

If carrier commit topology/identity changes while the detached semantic packet and proof bytes remain exact and valid:

    outcome = PROOF_UNCHANGED
    latestness = VALID_AS_PRESENTED

The mechanism may internally admit/verify the packet; the external probe result describes the property tested.

### 3.8 Recovery

If interruption observation proves the operation never started:

    outcome = NOT_STARTED
    latestness = VALID_AS_PRESENTED

If observation proves the exact acceptance is already durably present and recovery performs no duplicate admission:

    outcome = DONE_NO_DUPLICATE
    latestness = VALID_AS_PRESENTED

The implementation must mechanically preserve the no-duplicate property rather than merely renaming DONE.

### 3.9 Witnessed rollback/truncation

If a trusted prior or out-of-band newer head witness proves the presented chain is behind:

    outcome = ROLLBACK_DETECTED
    latestness = STALE

### 3.10 Fresh verifier limitation

If a fresh verifier receives a valid internally continuous presented chain but no independent freshness witness:

    outcome = CHAIN_VALID
    latestness = LATESTNESS_UNPROVEN

This is an intentional theoretical limitation, not a failure.

## 4. Repair restriction

Attempt 002 may change only the candidate's result classification/reporting needed to satisfy this contract.

It must not:

    inspect oracle.json
    inspect score.py
    inspect attempt_001_result.md
    hard-code case_id -> expected result
    alter fixture.json
    weaken signature, staleness, chain, duplicate, recovery, witness, or rebuild checks
    remove or bypass any negative control
    add repository/file/network/model/Git subprocess I/O
    represent synthetic HMAC or probe JSON as production choices

The existing architecture-probe mechanics are not being redesigned by this repair.

## 5. Allowed validation before freeze

Before Attempt 002 scoring, the implementer may perform:

    syntax validation
    deterministic repeated-call smoke checks
    fixture immutability checks
    output-shape checks
    canonical-vocabulary membership checks
    mechanism-focused non-oracle smoke checks

It may not run the scorer or derive hidden per-case expected outputs.

## 6. Attempt boundary

After candidate.py is revised under this contract:

    task owner reviews the diff
    only candidate.py may have changed for the implementation commit
    candidate is committed and pushed
    tracked tree is verified clean
    scorer runs exactly once for Attempt 002

No result-guided repair is allowed within Attempt 002.
