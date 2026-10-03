# Research 499: D-1 comparison result and bounded interface reconciliation

**Date:** 2026-10-03
**Status:** D1_AMEND / SEMANTIC PATH COHERENT / INITIALIZATION COLLECTION SHAPE AMENDED
**Parent:** Research 490-498
**Probe ID:** HYBRID_D1_REAL_EVENT_REPLAY_V01
**Frozen result commit:** 71488a63e717be144957a03472e013456afb8402
**Result artifact:** experiments/ao10_hybrid_d1_replay_v01/result.json
**Result Git-blob SHA-256:** 6294e97f3716866c68c8e402d84275c8bd1902162a3dc1a59f19d89ac47f4a01
**Scope:** Preserve the single frozen D-1 execution, classify the one material mismatch without post-result normalization, and reconcile the smallest architecture/interface amendment.
**Authority:** Development evidence and architecture reconciliation only. No production activation, migration, Specification 028 replacement, dependent-DRP resumption, or hidden-R2 exposure.

## 1. Raw frozen result

The single authorized D-1 comparison produced:

    material fields                  14
    A -> frozen key exact            yes
    B -> frozen key exact            no
    A <-> B exact                    no
    material mismatch fields         1
    raw outcome                      D1_MISMATCH_REQUIRES_RECONCILIATION

The mismatch is preserved exactly.

No evaluator, key, fixture, runner, or result is edited after observation.

## 2. Exact mismatch

The only differing field is:

    realization_initialization

Frozen key and ChatGPT Evaluator A emitted:

    {
        "effect_id": "D1-E01-D2-CLAUDE-WRITE-REQUIREMENT",
        "mode": "OPEN_RESET"
    }

Claude Evaluator B emitted:

    [
        {
            "effect_id": "D1-E01-D2-CLAUDE-WRITE-REQUIREMENT",
            "mode": "OPEN_RESET"
        }
    ]

The semantic payload is identical:

    effect identity
        D1-E01-D2-CLAUDE-WRITE-REQUIREMENT

    initialization mode
        OPEN_RESET.

The disagreement is container cardinality only.

## 3. Why this is a real D-1 mismatch

Research 497 froze all output fields as material and prohibited post-result normalization.

Therefore the V01 run does not become a pass by treating object and singleton-array as equivalent after the fact.

The raw outcome remains:

    D1_MISMATCH_REQUIRES_RECONCILIATION.

## 4. Root cause

The reviewer-facing D-1 contract froze:

    realization_initialization_fields:
        effect_id
        mode

but did not freeze whether:

    realization_initialization

is:

    one object

or:

    an ordered collection of zero or more initialization objects.

Message 020 independently recorded an adjacent ambiguity before scoring:

    realization_initialization ordering is not stated.

Claude therefore implemented it as a collection.

The hidden key and ChatGPT Evaluator A implemented it as a singleton object.

This is an output-interface under-specification, not disagreement over J1 meaning, J2 facts, J3 truth, lineage relation, currentness, completion, standing enforcement, authorization exercise, review routing, or orientation.

## 5. Cross-probe architecture evidence

D-2 already qualified:

    SPLIT
    MERGE
    crossing N:M REPARTITION
    REINSTATE
    realization succession.

Those semantics permit one lifecycle transition to produce multiple successor initialization records.

D-2 itself uses:

    successor_initialization

as an ordered collection.

A singleton-only D-1 integrated output would therefore be narrower than the already-qualified lineage architecture.

The collection form is the coherent whole-system choice.

## 6. Amendment

The D-1 interface is amended prospectively:

    realization_initialization
        = ordered array of zero or more initialization records

Each record contains exactly:

    effect_id
    mode

Ordering:

    lexical by effect_id.

For the real D-1 replay the canonical value is:

    [
        {
            "effect_id": "D1-E01-D2-CLAUDE-WRITE-REQUIREMENT",
            "mode": "OPEN_RESET"
        }
    ]

The amendment changes representation cardinality only.

It does not alter:

    accepted J1 semantics
    owner ACCEPT decision
    natural-owner J2 facts
    shared predicates
    completion authority
    J3 requirement satisfaction
    current-effect set
    lineage relation
    realization-succession mode
    standing prohibition handling
    authorization exercise
    review ownership.

## 7. D-1 disposition

Under Research 490 outcome classes:

    D1=D1_AMEND

not:

    D1_INTEGRATED_MICROREPLAY_PLAUSIBLE

because exact V01 comparison did not pass.

And not:

    D1_REDESIGN_REQUIRED

because the integrated semantic path did not exhibit duplicate authority, circular ownership, hidden prose adjudication, or inability to represent the real event.

The bounded interface amendment resolves the discovered coherence issue at the candidate-design level.

The evidence statement is therefore:

    integrated semantic replay = coherent on all tested substantive values;
    independent implementations = 13/14 exact fields plus identical semantic payload in the one shape-mismatch field;
    output cardinality contract = under-specified and amended to collection form.

## 8. Pre-owner-decision status

Research 477 required D-1, D-2, and D-3 to be executed before the architecture decision.

That required evidence program is now complete:

    D1 = D1_AMEND
    D2 = D2_LINEAGE_EXTENSION_PLAUSIBLE
    D3 = D3_DEPENDENCY_PROOF_PASSES.

Before owner decision, the candidate itself must now be re-frozen with the D-1 collection amendment included explicitly.

No further semantic experiment is required by the current evidence unless that candidate freeze exposes a new contradiction.

## 9. Current boundary

    D1_RAW_RESULT=D1_MISMATCH_REQUIRES_RECONCILIATION
    D1_RECONCILED_DISPOSITION=D1_AMEND
    D1_AMENDMENT=REALIZATION_INITIALIZATION_IS_ORDERED_COLLECTION
    D2=D2_LINEAGE_EXTENSION_PLAUSIBLE
    D3=D3_DEPENDENCY_PROOF_PASSES

    OWNER_ARCHITECTURE_DECISION_READY=false
    PRODUCTION_TARGET_SELECTED=false
    HIDDEN_R2_DETAILS=SEALED

    NEXT=FREEZE_THIN_CENTRED_HYBRID_V03
