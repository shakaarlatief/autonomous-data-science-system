# Research 239: PKIA-E01 G1 Historical Lifecycle-Independence Measurement

**Date:** 2026-09-22
**Status:** G1 PASS / PSMF LIFECYCLE-INDEPENDENCE JUSTIFICATION SUPPORTED / OWNER DISPOSITION STILL PENDING
**Evolution case:** PKIA-E01
**Preregistered protocol:** Research 238
**Protocol freeze commit:** 2aee0f899e8bbcda5e2387eb0cec4288b8bdb1be
**History window:** Checkpoint 523 through Checkpoint 566
**Exact history start:** 1f09fc812e8d7b1f31771a8b545864b76ea61db0
**Exact history end:** 6c1a51c490c863c34486a1bcb186939675b25071
**Scope:** Execute the frozen Research 238 lifecycle-independence test against the complete bounded Candidate 01 implementation-through-AO9 checkpoint history and determine whether PSMF's separate-upstream lifecycle rationale is supported, rejected or inconclusive.

## 1. Result

G1 passes all preregistered conditions.

The complete 523-566 checkpoint window yields:

    FRAMEWORK_ONLY   22
    PROJECT_ONLY      9
    SPANS_LAYERS      5
    EVIDENCE_ONLY     6
    OUT_OF_SCOPE      2
    total episodes   44

Main denominator:

    N = F + P + S = 36

Rates:

    F / N = 22 / 36 = 61.1%
    P / N =  9 / 36 = 25.0%
    S / N =  5 / 36 = 13.9%

Preregistered PASS thresholds were:

    F / N >= 30%
    S / N < 50%
    PRE_AO has at least 3 FRAMEWORK_ONLY episodes
    AO has at least 3 FRAMEWORK_ONLY episodes

Observed recurrence:

    PRE_AO Checkpoints 523-555
        FRAMEWORK_ONLY = 15
        PROJECT_ONLY   = 9
        SPANS_LAYERS   = 4
        EVIDENCE_ONLY  = 3
        OUT_OF_SCOPE   = 2

        substantive N = 28
        F / N = 53.6%
        S / N = 14.3%

    AO Checkpoints 556-566
        FRAMEWORK_ONLY = 7
        PROJECT_ONLY   = 0
        SPANS_LAYERS   = 1
        EVIDENCE_ONLY  = 3

        substantive N = 8
        F / N = 87.5%
        S / N = 12.5%

The result is not near any PASS/FAIL boundary, and no single disputed episode can change the categorical result. Research 238 therefore does not require an additional second-model coding pass.

## 2. Classification table

| Checkpoint | Class | Evidence-based rationale |
|---|---|---|
| 523 | SPANS_LAYERS | Specification 028 freezes generic implementation/provenance contracts together with Candidate 01 repository-local physical and migration assumptions. |
| 524 | FRAMEWORK_ONLY | Opens independent W0 implementation architecture design; no project-specific semantic owner changes. |
| 525 | EVIDENCE_ONLY | Comparative design evidence only; no new accepted implementation or project semantic delta. |
| 526 | FRAMEWORK_ONLY | Freezes reconciled W0 implementation architecture before coding. |
| 527 | FRAMEWORK_ONLY | Implements the core substrate, schemas, repository snapshots, discovery/validation and declaration machinery. |
| 528 | FRAMEWORK_ONLY | Identity-transition/current-index mechanism. |
| 529 | FRAMEWORK_ONLY | Deterministic authority resolver. |
| 530 | FRAMEWORK_ONLY | Workstream DAG and resume/dependency engine. |
| 531 | OUT_OF_SCOPE | Browser plugin compatibility qualification explicitly preserves the PKA route unchanged. |
| 532 | OUT_OF_SCOPE | Browser turn-end lifecycle investigation explicitly preserves the PKA route unchanged. |
| 533 | FRAMEWORK_ONLY | Deterministic derived-view framework and execution/provenance machinery. |
| 534 | FRAMEWORK_ONLY | Refines the generic current-state-core input contract after a fail-visible implementation stop. |
| 535 | FRAMEWORK_ONLY | Current-state-core generator and supporting generic view machinery. |
| 536 | FRAMEWORK_ONLY | Capture non-authority, validation and promotion-planning mechanism. |
| 537 | FRAMEWORK_ONLY | Public/private validation and degraded-mode mechanism. |
| 538 | FRAMEWORK_ONLY | Full/incremental rebuild-equivalence mechanism. |
| 539 | FRAMEWORK_ONLY | Deterministic CLI, persistent-view and semantic-validation surfaces. |
| 540 | FRAMEWORK_ONLY | Freezes/accepts reusable architecture documentation for the substrate itself. |
| 541 | FRAMEWORK_ONLY | Integrates project-knowledge validation into generic repository-integrity gating. |
| 542 | EVIDENCE_ONLY | Final W0 acceptance boundary; no new semantic mechanism beyond preceding gates. |
| 543 | PROJECT_ONLY | Migrates the selected architecture workstream into a concrete live project semantic owner. |
| 544 | PROJECT_ONLY | Creates the concrete Project Integration Boundary semantic owner. |
| 545 | PROJECT_ONLY | Migrates Source Vault paused/resume semantics and action contract. |
| 546 | PROJECT_ONLY | Migrates Cockpit pause/resume semantics. |
| 547 | PROJECT_ONLY | Migrates the project-specific D-035 selection semantics. |
| 548 | SPANS_LAYERS | Live W1 instance semantics expose and require view-mechanism changes, including workstream execution-anchor alignment and generic view code. |
| 549 | PROJECT_ONLY | ADS-specific compatibility non-overwrite and migration protection. |
| 550 | PROJECT_ONLY | ADS current-continuity authority boundary after live semantic migration. |
| 551 | EVIDENCE_ONLY | Final W1 integrity/acceptance boundary; no new semantic layer change. |
| 552 | SPANS_LAYERS | W2 project migration/materialization requires generic checkout/materialization mechanism repair in the same accepted wave. |
| 553 | PROJECT_ONLY | W3 compatibility shadow is a predecessor-architecture migration adapter, even though implemented in Python. |
| 554 | PROJECT_ONLY | W4 applies capture/promotion to a concrete ADS project boundary and archives the project capture; no generic mechanism change required. |
| 555 | SPANS_LAYERS | W5 simultaneously contains generic implementation-closure work and ADS-specific information architecture, subject vocabulary and placement policy. |
| 556 | FRAMEWORK_ONLY | Opens activation/orchestration control-plane architecture while holding W5 project migration; the project pause is execution state, not a new instance-policy semantic. |
| 557 | EVIDENCE_ONLY | AO-1 is a retrospective completeness/gap audit. |
| 558 | FRAMEWORK_ONLY | Defines architecture-neutral control responsibilities and failure taxonomy. |
| 559 | FRAMEWORK_ONLY | Selects Progressive Control Closure as generic control architecture. |
| 560 | FRAMEWORK_ONLY | Selects Governed Evolution Cases. |
| 561 | FRAMEWORK_ONLY | Selects Anchored Interaction Continuity and Independent Recovery. |
| 562 | SPANS_LAYERS | Selects generic Purpose-Bound Git Lifecycle and simultaneously makes the concrete ADS branch-rotation decision/records its realization gap. |
| 563 | FRAMEWORK_ONLY | Selects the Authority-Preserving Successor Bridge. |
| 564 | EVIDENCE_ONLY | Independent architecture review/reconciliation; amendment remains a candidate rather than an accepted semantic change. |
| 565 | EVIDENCE_ONLY | Historical-regression evidence and owner-decision preparation; no owner semantic decision yet. |
| 566 | FRAMEWORK_ONLY | Owner decisions prospectively amend generic AO-3 behavior and add project-knowledge architecture requirements R51/R52; project sequencing changes are control state. |

## 3. Why routine preservation did not create false spans

Raw Git intervals often contain:

    CURRENT_STATE / routing updates
    checkpoint creation
    Knowledge Map changes
    generated-view refreshes
    compatibility-shadow refreshes
    review-thread bookkeeping
    acceptance/evidence records

Research 238 preregistered these as non-coupling unless they carried a distinct semantic change.

That matters because otherwise every framework implementation episode would appear to touch project state simply because the project professionally records and validates every accepted change.

The classification instead asks whether the **same semantic delta** required framework-level and project-specific semantic change.

## 4. Qualitative falsifier check

Research 238 required a downgrade if nominal FRAMEWORK_ONLY episodes were systematically delayed implementation of project-specific changes from immediately preceding episodes.

That pattern is not observed.

Two pieces of evidence are especially strong.

### 4.1 W0 before live project migration

W0 contains a long run of framework-only mechanism construction:

    identity
    authority
    workstreams
    derived views
    current-state generation
    capture
    privacy
    rebuild equivalence
    CLI
    architecture documentation
    repository integrity

Only after W0 acceptance does W1 begin the concrete Source Vault/Cockpit/D-035/live-owner migration.

This is direct historical evidence that mechanism implementation had an independent lifecycle phase rather than being only a textual side effect of each project-specific semantic migration.

### 4.2 AO while project migration is held

During AO, W5-F0 is explicitly paused.

Nevertheless, the project develops several framework-level control architectures:

    AO-2 control boundary / failure taxonomy
    AO-3 Progressive Control Closure
    AO-4 Governed Evolution Cases
    AO-5 Interaction Continuity / Recovery
    AO-7 Successor Bridge
    AO-9 accepted generic control/requirements amendments

This is unusually strong evidence for lifecycle independence: the project-specific migration lifecycle was deliberately held while framework/control semantics continued to evolve.

AO-6 is correctly classified SPANS_LAYERS because it combines generic Git lifecycle design with a concrete branch rotation decision. The existence of such spans is expected under PSMF and does not undermine the distinct lifecycle demonstrated by the broader distribution.

## 5. Sensitivity

The PASS is not dependent on borderline classifications.

Several conservative recodings are plausible, for example treating architecture-documentation or design-freeze checkpoints as EVIDENCE_ONLY rather than FRAMEWORK_ONLY, or treating additional live-view episodes as SPANS_LAYERS.

The observed margins are large:

    F / N observed 61.1% versus 30% PASS floor
    S / N observed 13.9% versus 50% FAIL boundary
    PRE_AO F = 15 versus minimum 3
    AO F = 7 versus minimum 3

No reasonable reclassification of the small set of arguable episodes approaches a categorical reversal.

Therefore the protocol's independent-review trigger is not activated.

## 6. Interpretation

G1 supports the specific claim it was designed to test:

> ADS history contains a substantial and recurring class of framework-level changes that evolve without requiring simultaneous project-specific semantic changes.

This materially strengthens PSMF's lifecycle rationale.

It does **not** prove:

    that every current PKA mechanism is generic
    that a generic upstream should be created immediately
    that the current tools/project_knowledge tree can be extracted unchanged
    that a second project will fit the current policy/profile set
    that framework upgrades will be cheap
    that Research 218 should gain a framework directory now

Those remain separate qualification/realization questions.

## 7. Consequence for PKIA-E01

Research 238 defined:

    G1 PASS
        -> lifecycle independence supports PSMF as leading topology
        -> proceed to instance-policy-home decision and Research 218 reconciliation

That consequence now applies.

The topology evidence is now substantially stronger than before G1:

    project self-containment         supported
    no external runtime authority    supported
    materialization satisfies V1
                                  provenance
    transferability                  plausible, not yet fully qualified
    lifecycle independence           empirically supported by ADS history
    extraction timing                still NOT NOW

The next architectural question is therefore narrow:

> What is the natural project-local home and ownership boundary for instance policy under PSMF?

That decision should be made before final Research 218 hierarchy disposition.

## 8. Current state

    PKIA_E01=OPEN
    PSMF=LEADING_TARGET_HYPOTHESIS
    G1=PASS
    LIFECYCLE_INDEPENDENCE=SUPPORTED
    OWNER_ACCEPTED_TARGET=NO
    MECHANISM_EXTRACTION_JUSTIFIED_NOW=NO
    INSTANCE_POLICY_HOME=UNRESOLVED
    RESEARCH218=FROZEN_BASELINE_RETAINED
    RESEARCH177=UNCHANGED
    SPECIFICATION028=UNCHANGED
    W5_F0=PAUSED
    AO10=HELD
    AUTHORITY_SWITCH_ALLOWED=false
    NEXT=INSTANCE_POLICY_HOME_AND_RESEARCH218_RECONCILIATION
