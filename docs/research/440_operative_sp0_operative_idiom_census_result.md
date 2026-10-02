# Research 440: OPERATIVE SP-0 operative-idiom census result

**Date:** 2026-10-02
**Status:** SP-0 COMPLETE / MIXED_EXISTING_IDIOM / SP-1 FROZEN AND NEXT
**Protocol:** Research 439
**Fixed evidence base:** 8e8aed19cf3e1c159f74fdef787070688634a221
**Result artifact:** docs/research/project_knowledge_activation_orchestration/ao10/OPERATIVE_SP0_RESULT_V01.json
**Scope:** Record the first frozen small development probe for OPERATIVE V0.1.
**Authority:** Development evidence only. This result does not select OPERATIVE, amend Specification 028, authorize implementation, expose hidden R2 material, resume dependent DRPs, migrate repository state, or switch authority.

## 1. Mechanical census

Research 439 froze Research 300-437 as the census universe.

Observed:

    records                                   138
    trailing assignment block                 123
    prevalence                                0.891304347826
    assignment lines                          1570
    unique assignment keys                    695
    lines per detected block
        minimum                               1
        median                                13
        mean                                  12.764227642276
        maximum                               33

The prevalence gate therefore passes comfortably:

    0.8913 >= 2/3

This independently confirms the narrow Claude/Research-438 claim that an assignment-style closing idiom is already common in recent Project research records.

It does not establish that those blocks are complete operative contracts.

## 2. Descriptive key/effect distribution

A conservative deterministic keyword classifier was applied to the 1570 terminal assignments. Ambiguous cases default to OTHER.

    OTHER                         687
    AUTHORIZATION_PERMISSION      307
    RESULT_STATUS                 285
    ROUTING_NEXT_ACTION           110
    EVIDENCE_PROVENANCE            68
    IMPLEMENTATION_MIGRATION       58
    HOLD_PROHIBITION               44
    ASSURANCE_QUALIFICATION         9
    AUTHORITY_LIFECYCLE             2

This classification is descriptive only.

The high OTHER count is itself informative: the current key vocabulary is broad and ad hoc, so the existing idiom must not simply be promoted into a future grammar.

## 3. Prospectively selected eight-record omission review

Research 439 froze eight hash-selected records across numeric strata before body review.

Coding granularity is unique consequential semantic effect groups; repeated header/body/tail restatements count once.

Observed:

    block represented effects     70
    prose-only effects             39
    ambiguous effects               0

    prose_only_share
        39 / (70 + 39)
        = 0.357798165138

Per-record counts:

    Research 315     19 represented /  8 prose-only
    Research 321      9 represented /  4 prose-only
    Research 346      7 represented /  7 prose-only
    Research 366      9 represented /  2 prose-only
    Research 376      8 represented /  0 prose-only
    Research 395      6 represented /  1 prose-only
    Research 412      6 represented /  5 prose-only
    Research 433      6 represented / 12 prose-only

The exact effect descriptions are frozen in OPERATIVE_SP0_RESULT_V01.json.

## 4. Result class

Research 439 defines:

    MIXED_EXISTING_IDIOM
        trailing-block prevalence >= 2/3
        AND 0.25 < prose_only_share <= 0.50

Observed:

    prevalence       0.8913
    prose_only_share 0.3578

Therefore:

    SP0 = MIXED_EXISTING_IDIOM

## 5. Interpretation

Two statements are now simultaneously supported.

First:

    the project already has a strong habit of ending governing/research records
    with compact assignment-style state/action summaries

Second:

    those summaries are not generally exhaustive of consequential machine semantics

In the sample, detailed controls frequently remain prose-only, especially:

    tool/source/exposure restrictions
    exact sequencing and gating rules
    fail-closed behavior
    qualification thresholds
    immutable/frozen-input rules
    recovery/rollback prerequisites
    write-once and no-retry constraints

Therefore OPERATIVE cannot claim that the target grammar is merely a zero-cost formalization of current closing blocks.

The stronger and more accurate hypothesis becomes:

    the project already has the cultural shape of an operative summary,
    but a true machine-operative contract would require selective additional
    authoring or generation of consequential details that current summaries omit

This is not a rejection of OPERATIVE.

It is a development amendment to its adoption-cost hypothesis.

## 6. Architectural consequence

Do not design the future grammar by copying the 695 existing keys.

SP-1 remains necessary to determine:

    which of the omitted details machines actually need
    which questions are consequential
    which information can be generated from already-authoritative facts
    which details should remain human-governing prose
    what minimum bounded clause/slot surface is justified

Because SP-0 is MIXED rather than CULTURAL_CHANGE_REQUIRED, the candidate family comparison is not reopened yet.

But under Research 439 combined routing, SP-2 must not be frozen until SP-1 determines whether OPERATIVE needs redesign.

## 7. Evidence hygiene

No hidden R2 item-level material was accessed.

All eight sampled records and the full census are public repository evidence.

The SP-1 protocol remains exactly as frozen by Research 439 and is not changed using this result.

    SP0=COMPLETE
    SP0_RESULT=MIXED_EXISTING_IDIOM
    TRAILING_BLOCK_PREVALENCE=0.891304347826
    PROSE_ONLY_SHARE=0.357798165138
    OPERATIVE_EXISTING_IDIOM_CLAIM=PARTIALLY_SUPPORTED
    OPERATIVE_ZERO_MARGINAL_AUTHORING_COST_CLAIM=NOT_SUPPORTED
    HIDDEN_R2_DETAILS=SEALED
    SP1_PROTOCOL=UNCHANGED_FROZEN
    NEXT=EXECUTE_SP1
