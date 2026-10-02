# Research 439: OPERATIVE SP-0 and SP-1 development-probe preregistration

**Date:** 2026-10-02
**Status:** DEVELOPMENT PROBES FROZEN / PUBLIC EVIDENCE ONLY / NO OWNER PARTICIPATION REQUIRED / EXECUTION NEXT
**Parent:** Research 438 / MC-0029 Message 012
**Fixed evidence base:** 8e8aed19cf3e1c159f74fdef787070688634a221
**Scope:** Prospectively freeze the first two small development probes for OPERATIVE V0.1 before either probe is executed: SP-0 operative-idiom census and SP-1 competency-question inventory.
**Authority:** Development evidence only. These probes cannot select the production architecture, amend Specification 028, expose hidden R2 material, retry R2, authorize implementation, resume dependent DRPs, migrate repository state, or switch authority.

## 1. Purpose

Research 438 makes OPERATIVE V0.1 the leading development candidate but deliberately withholds target selection.

The first questions are intentionally cheap:

    SP-0
        Does current ADS Project practice already exhibit an operative-decision idiom,
        and how much consequential meaning remains outside that idiom?

    SP-1
        What bounded questions do actual Project-system consumers need machines to answer,
        and what is the smallest structured semantic surface required to answer them?

These probes test whether OPERATIVE is plausibly formalizing existing practice and whether a bounded grammar can serve real consumers before any owner-facing drafting replay.

## 2. Evidence discipline

Both probes use only public repository evidence at:

    8e8aed19cf3e1c159f74fdef787070688634a221

Hidden R2 material remains sealed.

No R2 hidden labels, hidden grouping pairs, hidden STATE answers, private precedents or private comparison details may be opened.

SP-0/SP-1 are development evidence. Their material may be used to change the architecture and therefore is not future untouched confirmation.

## 3. SP-0 corpus

Primary census universe:

    docs/research/300_*.md
        through
    docs/research/437_*.md

at the fixed evidence base.

Expected file count from filename enumeration:

    138

Research 438 itself is excluded because it is the reconciliation record that ordered this probe.

## 4. SP-0 mechanical trailing-block detector

For each corpus file:

1. read UTF-8 text at the fixed base;
2. remove only trailing whitespace at end of file;
3. scan upward from the final non-empty line;
4. accept lines matching:

       ^[A-Z][A-Z0-9_]*\s*=

5. permit blank lines while scanning the terminal assignment region;
6. stop at the first non-blank line that does not match;
7. count the record as containing a trailing assignment block iff at least one matching assignment line is found.

This deliberately measures the existing idiom, not a future grammar.

Mechanical outputs:

    corpus size
    records with trailing assignment block
    prevalence
    assignment-line count distribution
    key-name frequency
    raw key/value inventory

## 5. SP-0 effect-type coding

Each trailing assignment is coded into exactly one development category based on the assignment's explicit operational role, with surrounding record text consulted only when the key/value pair is not self-explanatory:

    AUTHORIZATION_PERMISSION
    HOLD_PROHIBITION
    ROUTING_NEXT_ACTION
    RESULT_STATUS
    AUTHORITY_LIFECYCLE
    ASSURANCE_QUALIFICATION
    IMPLEMENTATION_MIGRATION
    EVIDENCE_PROVENANCE
    OTHER

This taxonomy is an analysis device only and does not become OPERATIVE grammar.

Ambiguous cases are coded OTHER rather than forced.

## 6. SP-0 sampled omission review

Eight records are selected prospectively from records with detected trailing blocks.

To prevent phase clustering, use eight numeric strata:

    300-317
    318-335
    336-353
    354-371
    372-389
    390-407
    408-425
    426-437

Within each stratum choose the eligible file whose hexadecimal SHA-256 is lexicographically smallest for:

    "<fixed-base>:<repo-relative-path>:SP0:<lo>-<hi>"

The resulting frozen sample is:

    315_mc0029_message003_reconciliation_integrated_project_system_v03.md
    321_drp01_shared_semantic_substrate_review_harness_freeze.md
    346_key_author_a_p3_explicit_owner_authorization.md
    366_key_author_a_p4_d01_attempt002_hold_eligibility_interface_reopened.md
    376_key_author_a_p4_h04_accepted_h05_released.md
    395_key_author_a_p5_l08_accepted_l09_released.md
    412_key_author_a_p6_owner_acceptance_and_p6a_automation_start.md
    433_drp03_r2_construct_comparison_control_plane_design.md

For each sampled record, identify explicit consequential effects in the body under this bounded definition:

    a statement that explicitly changes or declares
        authorization / permission
        prohibition / hold
        next actor / next action / routing
        project or experiment result/status
        authority / lifecycle / supersession
        admission / qualification requirement or result
        implementation / migration / cutover requirement
        durable evidence/provenance binding

Exclude:

    rationale
    explanatory claims
    examples
    historical narration that does not itself change current/project state
    descriptive architecture discussion with no declared consequence

Each consequential effect is marked:

    BLOCK_REPRESENTED
    PROSE_ONLY
    AMBIGUOUS

A block assignment counts as representing an effect when it captures the same operational consequence without requiring another semantic inference from unrelated prose.

## 7. SP-0 interpretation classes

Let:

    prose_only_share =
        PROSE_ONLY /
        (BLOCK_REPRESENTED + PROSE_ONLY)

excluding AMBIGUOUS from the denominator.

Interpretation:

    FORMALIZATION_PLAUSIBLE
        trailing-block prevalence >= 2/3
        AND prose_only_share <= 0.25

    MIXED_EXISTING_IDIOM
        trailing-block prevalence >= 2/3
        AND 0.25 < prose_only_share <= 0.50

    CULTURAL_CHANGE_REQUIRED
        trailing-block prevalence < 2/3
        OR prose_only_share > 0.50

These are development-routing classes, not scientific truth thresholds.

If CULTURAL_CHANGE_REQUIRED, OPERATIVE is not automatically abandoned, but its "formalizes existing practice" cost claim is rejected and must be redesigned/re-costed before owner-facing SP-2.

## 8. SP-1 primary source universe

At the same fixed base, use these primary sources:

    docs/research/222_ao3_progressive_control_closure_architecture.md
    docs/research/223_ao4_architecture_evolution_and_frozen_contract_governance.md
    docs/research/224_ao5_anchored_interaction_continuity_and_independent_recovery.md
    docs/research/225_ao6_purpose_bound_git_lifecycle_and_workstream_orchestration.md
    docs/research/226_ao7_authority_preserving_successor_orchestration_bridge.md
    docs/research/257_r8a_exact_target_repository_realization_and_project_system_residency_candidate.md
    docs/research/258_mc0025_r8a_adversarial_reconciliation_and_amended_exact_target_candidate.md
    docs/research/276_owner_total_architecture_freedom_and_warrant_f_v02_reconciliation.md
    docs/research/315_mc0029_message003_reconciliation_integrated_project_system_v03.md
    docs/research/318_drp09_assurance_request_claim_integrity_pass.md
    docs/specifications/028_v1_project_knowledge_architecture_implementation_and_migration_contract.md
        section 42, plus only directly referenced definitions needed to interpret section 42

Support sources may be opened only when a primary source points to an identifier whose meaning cannot be reconstructed locally. Every support-source use must be named in the result.

## 9. SP-1 competency-question definition

A competency question is admitted when a named Project-system consumer must answer it to perform one of these consequences:

    route work
    admit/refuse/review a consequential transition
    preserve authority
    maintain continuity/recover
    determine applicable governance
    determine realization/coverage
    determine current operational condition
    qualify cutover/migration
    surface a control miss
    trigger architecture evolution

Questions that are merely useful for explanation or general retrieval are excluded from the machine-operative inventory unless a source explicitly makes them consequential.

## 10. SP-1 extraction schema

For each admitted competency question record:

    cq_id
    normalized_question
    named_consumer
    source_refs
    consequence_class
    answer_shape
    minimum_authoritative_inputs
    requires_machine_determinism
    current_source_of_truth
    candidate_structured_need
    candidate_clause_form
    candidate_slots
    unresolved_interpretation

Allowed consequence classes:

    ROUTING
    ADMISSION
    AUTHORITY
    CONTINUITY_RECOVERY
    EVOLUTION
    REALIZATION_COVERAGE
    OPERATIONAL_PREDICATE
    CUTOVER_MIGRATION
    OBSERVABILITY

Allowed answer shapes:

    BOOLEAN
    ENUM
    REFERENCE
    REFERENCE_SET
    ORDERED_ACTIONS
    STRUCTURED_DECISION
    OTHER_BOUNDED

No free-form prose answer is admitted as a successful machine-operative answer shape.

## 11. SP-1 deduplication

Two extracted questions merge only when all are true:

    same named consumer responsibility
    same decision consequence
    same minimum authoritative inputs
    same answer shape

If any differs, retain separate questions.

The goal is minimal operational sufficiency, not maximum ontology reuse.

## 12. SP-1 candidate grammar derivation

Only after the question inventory is frozen:

1. group questions by required structured semantic function;
2. attempt to satisfy them with the smallest set of clause forms/slots;
3. start from no assumed form;
4. compare the result with, but do not privilege, Claude's illustrative forms:

       REQUIRE
       PROHIBIT
       GATE
       INVARIANT
       SUPERSEDE
       AMEND
       RETIRE
       DEFER
       ASSIGN

5. remove any form or slot with no admitted competency-question consumer.

## 13. SP-1 interpretation classes

    OPERATIVE_GRAMMAR_PLAUSIBLE
        every machine-critical competency question can be answered
        from explicit bounded inputs
        AND <= 10 clause forms are required
        AND no required slot value fundamentally requires
        unconstrained prose interpretation at decision time

    OPERATIVE_GRAMMAR_NEEDS_REDESIGN
        questions appear bounded in principle
        BUT > 10 forms are required
        OR important slots remain semantically overloaded/ambiguous

    EXPRESSIVENESS_BOUNDARY_REOPEN
        at least one machine-critical competency question
        fundamentally requires unconstrained prose interpretation
        or cannot be represented without recreating a general semantic interpreter

The count threshold is a development complexity guard inherited from Message 011, not a universal architectural law.

## 14. Combined routing

After both probes:

    if SP-0 = FORMALIZATION_PLAUSIBLE
       and SP-1 = OPERATIVE_GRAMMAR_PLAUSIBLE
        -> freeze SP-2/SP-3 micro-development protocols

    if either probe is MIXED / NEEDS_REDESIGN
        -> revise OPERATIVE before owner-facing work

    if SP-0 = CULTURAL_CHANGE_REQUIRED
       or SP-1 = EXPRESSIVENESS_BOUNDARY_REOPEN
        -> reopen the candidate family comparison before SP-2

No result from SP-0 or SP-1 can select OPERATIVE for production.

## 15. Execution order

    freeze this record
    validate/push
    execute SP-0 at fixed evidence base
    freeze SP-0 result
    execute SP-1 at fixed evidence base
    freeze SP-1 result
    reconcile combined route

SP-0 result must not be used to change the SP-1 extraction rules already frozen here.

## 16. Current boundary

    RESEARCH439=SP0_SP1_PREREGISTRATION_FROZEN
    FIXED_EVIDENCE_BASE=8e8aed19cf3e1c159f74fdef787070688634a221
    HIDDEN_R2_DETAILS=SEALED
    OWNER_PARTICIPATION_REQUIRED=false
    SP0_EXECUTED=false
    SP1_EXECUTED=false
    NEXT=EXECUTE_SP0
