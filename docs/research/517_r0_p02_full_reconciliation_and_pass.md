# Research 517: R0-P02 full reconciliation and PASS classification

**Date:** 2026-10-04
**Status:** R0-P02 PASS / GOVERNED_LEDGER_KERNEL_V02 GIT SUBSTRATE SURVIVES / R0-P01 NEXT
**Parent:** Research 512-516
**Probe:** R0-P02
**Candidate under test:** GOVERNED_LEDGER_KERNEL_V02
**Deterministic candidate commit:** `83f9fad87e910b75299a3f478cf2b294d9d4ff7a`
**Deterministic result commit:** `3cc196f12903725ee703ac2c12ce2e6f2cbd06a9`
**Live-host evidence commit:** `9a291c9d1065d109fcd519ec6b6cf706e787a1dd`
**Scope:** Reconcile the complete R0-P02 evidence after both preregistered legs and issue the full probe classification.
**Authority:** R0-P02 architecture-decision evidence only. This record does not select the full physical target, start production implementation, authorize migration, amend Specification 028, extract Runtime Bridge, or switch Project-system authority.

## 1. Attempt history

Attempt 001 remains preserved as:

    HARNESS_INVALID
    ARCHITECTURE_INFERENCE=NONE

Its raw FAIL was not rewritten or normalized after observation.

Research 515 prospectively repaired only the missing public result-classification contract and refroze Attempt 002 without changing:

    fixture
    oracle
    scorer
    thresholds
    negative controls
    architecture candidate
    semantic mechanism

Attempt 002 then ran under the corrected blindness boundary.

## 2. Deterministic-core result

Attempt 002 candidate:

    83f9fad87e910b75299a3f478cf2b294d9d4ff7a

The frozen scorer executed exactly once and returned:

    deterministic_core = PASS
    case_count         = 20
    error_count        = 0
    metamorphic_checks = 2
    exit               = 0

This proves the frozen deterministic surface satisfies the Research 514 hard gate.

The successful surface includes:

    deterministic canonical envelope and semantic-base digests
    exact detached synthetic proof verification
    project / acceptance / decision binding
    semantic rather than repository-global staleness
    unrelated governing and non-governing changes do not falsely stale proposals
    deterministic in-ledger sequence / previous-entry continuity
    duplicate acceptance rejection
    duplicate sequence rejection
    middle-chain rewrite detection
    semantic conflict rejection without double-current result
    full rebuild equals incremental fold
    interrupted admission recovery without duplicate admission
    prior/out-of-band witness rollback detection
    explicit fresh-verifier latestness limitation
    host-transform invariance at the semantic packet level

The renamed-case and alternate-context metamorphic checks both passed, showing that the implementation does not depend on literal case IDs or one fixed synthetic project/secret context.

## 3. Live-host result

The Research 514 live-host leg used only Runtime Bridge GitHub connector capability.

Temporary branches:

    r0-p02-host-v01-base
    r0-p02-host-v01-work

were both created from:

    15428acfc9a8ca8ac0cfa3ce9c05e4110f922dec

The work branch received exactly one payload path.

Work commit:

    44ade93f30cd6fc2eb0c8e08ec9028a22dacdfc6

PR:

    #86

Squash result:

    4bd7d3971f09683613c4374d14ed98fc69e2c462

The commit identity therefore changed across host transformation.

Before and after squash, the exact payload remained:

    Git blob SHA
        3fbf6af8e6b116c787786c064d0ff3c2f3ba70c4

    UTF-8 payload SHA-256
        b4f5561dd0e129658ad28ee9178e264118198a8eeef269300f1971a84fbc00f5

Post-squash detached synthetic proof verification returned:

    DETACHED_PROOF_VALID=True
    PROFILE_OK=True
    SIGNER_OK=True

The coordination branch remained exactly:

    15428acfc9a8ca8ac0cfa3ce9c05e4110f922dec

through the host operation.

Both temporary branches were deleted under expected-head guards, and post-cleanup search found neither branch.

Therefore all Research 514 live-host PASS gates are satisfied:

    exact payload preservation
    transformed commit identity
    unchanged detached-proof validity
    unchanged coordination branch
    no production authority-surface mutation
    connector-only host transport
    successful cleanup

## 4. Anti-rollback witness decision

Research 512 and Research 513 deliberately separate:

    integrity of the history presented

from:

    proof that no newer valid history has been suppressed

The deterministic probe confirms the theoretical boundary:

    prior/out-of-band trusted checkpoint
        rollback is detectable

    completely fresh verifier with only one presented repository snapshot
        chain can be valid as presented
        latestness remains unproven

The current ADS Project threat model does not require a totally fresh verifier, with no retained or out-of-band evidence at all, to defeat a carrier that suppresses a newer otherwise-valid history.

The required target properties are satisfied by:

    authenticated semantic records
    deterministic in-ledger chain integrity
    explicit high-consequence owner checkpoints
    prior-checkpoint comparison when such a checkpoint exists
    fail-visible LATESTNESS_UNPROVEN for a truly fresh verifier

An additional permanently authoritative freshness service or second semantic ledger is neither required nor justified by current evidence.

Therefore R0-P02 selects:

    INDEPENDENT_EXTERNAL_WITNESS_REQUIRED=false

and retains the V0.2 checkpoint policy:

    required at genesis
    required at authority switch / rollback boundary
    required at trust-root rotation
    required at other high-consequence boundaries defined by accepted policy

No additional ordinary frequency/size checkpoint mandate is selected by R0-P02.

A remembered or independently persisted checkpoint may later be used as bounded defense-in-depth without becoming semantic authority, but it is not a prerequisite for target viability.

## 5. Full classification

Research 514 defines PASS as:

    deterministic core passes
    live-host leg passes
    same-repository chain/checkpoint threat model is sufficient
    no additional selected witness is required

All four conditions are satisfied.

Therefore:

    R0_P02=PASS

This is not PASS_WITH_SELECTION because no additional witness variant is selected.

This is not AMEND because no checkpoint/witness/promotion architecture amendment is required.

This is not REOPEN because trustworthy deterministic admission/order/tamper behavior was realized over Git without a second semantic authority or correctness-critical service.

This is not INVALID because the valid Attempt 002 obeyed the prospectively repaired attempt-integrity contract.

## 6. Architecture consequence

The evidence supports retaining the GOVERNED_LEDGER_KERNEL_V02 Git-based governing substrate into the remaining R0 evaluation.

Specifically retained:

    Git as leading durable carrier
    Git not semantic authority
    detached owner proof independent of host commit identity
    semantic_base_digest rather than whole-repository stale binding
    in-ledger sequence / previous-entry digest order
    owner checkpoints at consequence-triggered boundaries
    natural host serialization as replaceable transport/control
    explicit fresh-verifier latestness limitation
    no required external transparency service
    no second semantic ledger

Production cryptography and owner-signing usability remain R0-P01.

Semantic navigation remains R0-P03.

## 7. Next action

Research 513 freezes the preferred order:

    R0-P02
    R0-P01
    R0-P03

R0-P02 is now complete.

The next bounded stage is:

    R0-P01 owner authenticity / acceptance burden
    exact fixture / harness freeze before result observation

No P01 owner trial may begin until that boundary is prospectively frozen.

## 8. Current state

    R0_P02=PASS
    DETERMINISTIC_CORE=PASS
    LIVE_HOST_LEG=PASS
    INDEPENDENT_EXTERNAL_WITNESS_REQUIRED=false

    GOVERNED_LEDGER_KERNEL_V02=RETAINED
    PHYSICAL_ARCHITECTURE_SELECTED=false

    R0_P01=NEXT
    R0_P03=PENDING

    SPECIFICATION_028_AUTHORITY=UNCHANGED
    PRODUCTION_IMPLEMENTATION_STARTED=false
    MIGRATION_AUTHORIZED=false
    AUTHORITY_SWITCH_AUTHORIZED=false

    NEXT=FREEZE_R0_P01_EXACT_FIXTURE_AND_HARNESS
