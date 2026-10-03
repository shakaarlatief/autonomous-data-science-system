# Research 477: MC-0029 Message 017 final-critique reconciliation

**Date:** 2026-10-03
**Status:** MESSAGE 017 ACCEPTED WITH REFINEMENTS / V0.1 AMENDMENT REQUIRED / NO PRODUCTION SELECTION
**Parent:** Research 476 / MC-0029 Message 017
**Evidence base:** f32305f075c823cb8e642d76dceb385e48731d2a
**Scope:** Reconcile Claude Message 017, disposition its proposed gaps/amendments, and define the smallest remaining pre-owner-decision work.
**Authority:** Development reconciliation only. No production selection, Specification 028 replacement, migration, dependent-DRP resumption, or hidden-R2 exposure.

## 1. Transport provenance

Claude reported that the Runtime Bridge was unavailable and committed Message 017 through the GitHub connector. ChatGPT subsequently fetched and verified:

    commit  f32305f075c823cb8e642d76dceb385e48731d2a
    parent  90b770f14830c3c5d33e04bf05fbea161831b82e
    paths   exactly messages/017_claude_integrated_hybrid_final_critique.md

The content is admitted as collaboration evidence because the exact one-file write and lineage were verified. The transport deviation is recorded:

    COLLABORATOR_WRITE_TRANSPORT_NONCONFORMANCE=RECORDED

It is not precedent for bypassing the Runtime Bridge when available.

## 2. Overall disposition

Message 017:

    ACCEPT_WITH_REFINEMENTS

Routing:

    AMEND_INTEGRATED_CANDIDATE_BEFORE_OWNER_DECISION

is accepted.

No materially better whole architecture was identified. THIN_CENTRED_HYBRID remains the strongest current direction, but V0.1 contains known integration gaps that should be amended before owner decision.

## 3. Gap dispositions

G-1 enforcement accounting outside REQUIRE:

    ACCEPT_WITH_REFINEMENT.

PROHIBIT / GATE / SEQUENCE must bind an enforcing control/predicate or explicit DETECTIVE_ONLY handling. AUTHORIZE is latent permission, so the requirement is that consequential exercise consumes the exact authorization decision/predicate and leaves a governed receipt, not that every authorization is "enforced" at acceptance.

G-2 self-certification through domain contracts:

    ACCEPT.

Completion/domain-contract references are pinned exact revisions by default. Later revisions require governed re-binding. If completion-rule ownership and realization ownership coincide, consequential satisfaction additionally requires independent qualification/admission or another separately governed acceptance boundary.

G-3 cross-plane evaluation cycles:

    ACCEPT.

J3, WARRANT-F and gate evaluation need one shared evidence/freshness predicate source plus an explicit acyclic dependency order and snapshot/revision rules.

G-4 lineage/realization succession:

    ACCEPT.

C7 proved 1:1, 1:N and N:1, not arbitrary crossing N:M repartition. Coverage, completion contracts and deferrals across semantic succession remain undefined. Crossing repartition, reinstatement and realization carry/reset require explicit design and qualification.

G-5 owner acceptance unauthenticated/unmeasured:

    SPLIT.

The authenticity/binding gap is accepted. An acceptance record must bind the exact package shown, exact owner decision, resulting accepted semantics, provenance and effective boundary.

The claim that unmeasured owner-review efficacy is itself a coherence defect is rejected. Research 456 already establishes owner acceptance as a normative responsibility boundary, not a claim of human infallibility. The system should strengthen review and detection, but authority validity does not depend on proving reviewer accuracy.

## 4. Amendment dispositions

AM-1 Domain-contract binding:
    ACCEPT_WITH_REFINEMENT.
    Pin exact revisions by default. No silent follow-latest. Independent qualification is required where the same owner defines and realizes consequential completion.

AM-2 Standing-consequence enforcement accounting:
    ACCEPT_WITH_REFINEMENT.
    PROHIBIT/GATE/SEQUENCE bind enforcement or DETECTIVE_ONLY handling. AUTHORIZE binds consumption/receipt when exercised.

AM-3 Exact acceptance accounting:
    ACCEPT.
    Every accepted machine effect created/changed by the event gets an explicit accounting disposition. Allow explicit event-level CREATES_NO_ACCEPTED_MACHINE_EFFECTS. NO_REALIZATION_REQUIRED uses bounded accepted reason classes, not free text alone.

AM-4 Accepted effect statement/digest:
    ACCEPT.
    Bind owner-visible accepted_effect_statement + typed consequence + exact refs to accepted_effect_id and define semantic_digest over governing semantic content.

AM-5 Completion components:
    ACCEPT_WITH_REFINEMENT.
    Components are acceptance-shaped outcomes/criteria rather than guessed implementation partitions. Artifact/path references remain valid when the governing requirement itself is artifact-specific; lint is advisory, not semantic authority.

AM-6 Temporal satisfaction/regression/conflict:
    ACCEPT.
    Re-derive on relevant revision/freshness changes. Add REGRESSED as derived history-sensitive flag. Define conflict_present over bounded unresolved consequence/source-fact/lineage-control conflicts. Component-level deferral remains unsupported unless separately designed.

AM-7 Orientation:
    ACCEPT.
    Retain REVIEW_REQUIRED/DEFERRED/OPEN/SATISFIED. Add next_gap UNOWNED and DEPENDENCY plus orthogonal REGRESSED. Add a sibling standing-consequence enforcement view rather than overloading realization status.

AM-8 Lineage extension:
    ACCEPT.
    Add REPARTITION with explicit predecessor-successor mapping, per-target effective boundaries, REINSTATE as a new identity, and explicit realization succession. Semantic successors start OPEN by default. Carried realization requires governed mapping, freshness validity and requalification. CARRY_FORWARD may preserve compatible realization because meaning is unchanged.

AM-9 Cross-plane stratification:
    ACCEPT / D-3 REQUIRED.
    Candidate order:
        lineage resolution
        -> natural source facts/shared evidence predicates
        -> WARRANT-F decisions where required
        -> J3 satisfaction
        -> orientation
        -> compiled/consuming control.
    A WARRANT-F claim about J3 binds a frozen J3 snapshot and may not feed back into that same J3 revision.

AM-10 Acceptance authenticity:
    ACCEPT_WITH_IMPLEMENTATION_OPEN.
    Bind exact package digest/revision, exact owner decision payload, accepted semantic output, provenance and temporal authority. No cryptographic/storage mechanism is selected yet.

AM-11 Independent second-model faithfulness review:
    OPTIONAL_DETECTIVE_SAFEGUARD, NOT AUTHORITY CONDITION.
    Useful where available, but not compensation for owner-infallibility evidence and not required for acceptance validity. D-1 may use independent model review/evaluation for interaction-independence purposes.

AM-12 REVIEW_REQUIRED ownership:
    ACCEPT.
    Every review item derives a resolving owner class/reference from its source predicate/domain.

AM-13 Legacy transition:
    AMEND.
    Do not downgrade every legacy IN_FORCE obligation to DETECTIVE_ONLY. Legacy semantics retain existing authority/control. Hybrid completeness/orientation is scoped to reconciled/activated hybrid identities; unreconciled legacy is surfaced explicitly and excluded from hybrid-completeness claims until governed reconciliation.

AM-14 Evidence labels:
    ACCEPT.
    C4-C8 = mechanism plausibility. C9 = development burden evidence. SP-4 = bounded detector mechanism evidence. SP-2 = development owner-faithfulness evidence. Integrated end-to-end production-readiness evidence is absent.

## 5. Required remaining discriminators

D-1 INTEGRATED MICRO-REPLAY:
    required before owner decision.
    Use one real recent governing act, at most two only if necessary.
    Exercise amended J1 -> owner ACCEPT/AMEND/REJECT -> actual natural-owner J2 -> shared-predicate J3 -> orientation -> one lineage transition with realization succession.
    Two evaluator implementations must be authored independently by different models.
    This is not an owner-efficacy test: source meaning and proposed package are visible together.

D-2 LINEAGE EXTENSION:
    required.
    Cover crossing REPARTITION, per-target effective boundaries, REINSTATE, realization carry and default reset-to-OPEN.

D-3 CROSS-PLANE DEPENDENCY PROOF:
    required.
    Freeze the AO/compiler/WARRANT-F/lineage/J3/orientation dependency graph and prove no same-revision cycles or duplicated evidence/freshness semantics.

No separate pre-decision owner-infallibility experiment is required.

## 6. Next candidate

The successor candidate becomes:

    THIN_CENTRED_HYBRID_V02

with status:

    AMENDED_DEVELOPMENT_CANDIDATE
    D1_D2_D3_REQUIRED_BEFORE_OWNER_DECISION
    PRODUCTION_TARGET_SELECTED=false

## 7. Current disposition

    MESSAGE017=ACCEPT_WITH_REFINEMENTS
    MESSAGE017_ROUTING=ACCEPTED
    V01=AMEND_BEFORE_OWNER_DECISION
    NEXT_CANDIDATE=THIN_CENTRED_HYBRID_V02

    D1=REQUIRED
    D2=REQUIRED
    D3=REQUIRED

    OWNER_ARCHITECTURE_DECISION_READY=false
    PRODUCTION_TARGET_SELECTED=false
    HIDDEN_R2_DETAILS=SEALED

    NEXT=FREEZE_THIN_CENTRED_HYBRID_V02
