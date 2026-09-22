# Research 238: PKIA-E01 PSMF Reconciliation and Preregistered Lifecycle-Independence Gate

**Date:** 2026-09-22
**Status:** PSMF LEADING TARGET HYPOTHESIS / OWNER DISPOSITION NOT YET MADE / G1 PREREGISTERED / MEASUREMENT NEXT
**Evolution case:** PKIA-E01
**Collaboration evidence:** MC-0022 Messages 001-004
**Frozen baseline:** Research 218
**Related physical-boundary baseline:** Research 177
**Governing implementation contract:** Specification 028
**Measurement history window:** Checkpoint 523 through Checkpoint 566
**Exact history start:** 1f09fc812e8d7b1f31771a8b545864b76ea61db0
**Exact history end:** 6c1a51c490c863c34486a1bcb186939675b25071
**Scope:** Reconcile MC-0022 into a bounded PSMF target hypothesis and freeze a falsifiable historical lifecycle-independence test before any owner disposition, framework extraction or final internal-hierarchy decision.

## 1. Reconciled topology hypothesis

PKIA-E01 now has one jointly supported leading target hypothesis:

    PROJECT-SOVEREIGN MATERIALIZED FRAMEWORK (PSMF)

PSMF separates generic source authorship from project authority.

A reusable generic source may exist outside a concrete project, but the complete implementation needed to operate that project is materialized and committed inside the project. The concrete project remains self-contained and authoritative even if the generic source disappears.

This is a target hypothesis, not an accepted owner disposition and not an instruction to extract the current ADS implementation now.

## 2. Why another gate is required

PSMF has at least two independent justifications:

    TRANSFERABILITY
        some mechanisms may serve unrelated projects

    LIFECYCLE INDEPENDENCE
        generic mechanism may change for reasons distinct from one
        project's policy, knowledge and migration history

A second unrelated project is strong evidence for transferability.

It does not directly test lifecycle independence.

Claude Message 003 therefore proposed measuring ADS's own history before extraction. This research freezes that test before looking at its result.

## 3. G1 question

> Does the observed ADS development history contain a substantial and recurring class of framework-level changes that can evolve without requiring simultaneous project-specific semantic changes?

The competing failure hypothesis is:

> Framework mechanism and project-specific semantics co-evolve so frequently that a separate canonical upstream would mostly create synchronization cost rather than a meaningful lifecycle boundary.

## 4. Measurement unit

The measurement uses numbered checkpoint transitions from Checkpoint 523 through Checkpoint 566.

A checkpoint transition is used as the semantic episode unit because raw commits contain many routine preservation, generated-view, review-thread and evidence-recording changes that would make file-count or commit-count coupling misleading.

The complete bounded checkpoint range is selected in advance. No favorable episodes may be added and no unfavorable in-scope episodes may be removed after classification begins.

Checkpoint 523 begins the frozen Specification 028 implementation program. Checkpoint 566 closes AO-9 and is the exact pre-PKIA-E01 boundary.

## 5. Layer classes

Each checkpoint episode receives exactly one primary class:

    FRAMEWORK_ONLY
        The accepted semantic/implementation delta changes a mechanism,
        reusable contract or control architecture without requiring a
        project-specific policy/knowledge/migration semantic change.

    PROJECT_ONLY
        The accepted delta changes project-specific instance policy,
        project knowledge/semantic owners, project information architecture,
        migration/compatibility state or ADS-specific realization without
        changing generic mechanism semantics.

    SPANS_LAYERS
        The same accepted semantic delta materially requires both a
        framework-level change and a project-specific semantic/policy change.
        Mere documentation, tests, generated refresh or preservation does
        not qualify as spanning.

    EVIDENCE_ONLY
        The checkpoint records qualification/review/acceptance evidence
        without a new material framework or project semantic delta.

    OUT_OF_SCOPE
        The checkpoint's primary subject is not project-knowledge/
        activation-orchestration architecture or its migration.

Only FRAMEWORK_ONLY, PROJECT_ONLY and SPANS_LAYERS enter the main denominator.

## 6. Mechanical changes excluded from layer coupling

The following do not make an episode SPANS_LAYERS by themselves:

    docs/CURRENT_STATE.md preservation
    docs/current_routing.json updates
    docs/KNOWLEDGE_MAP.md updates
    checkpoint creation itself
    generated project-knowledge view refreshes
    generated manifests
    compatibility-shadow refreshes that merely follow another accepted delta
    collaboration thread bookkeeping
    experiment/replay result recording
    tests that only verify the same primary layer delta

Tests and research documents are not ignored. They inherit the semantic layer of the mechanism/policy they define or qualify.

## 7. Evidence used for classification

For every checkpoint episode, classification must inspect:

    checkpoint scope/status
    linked primary Research/Specification when material
    changed-path set between checkpoint boundaries
    commit subjects inside the interval
    implementation/schema changes when present

Path location alone cannot decide semantic class.

A generic mechanism described under docs/research remains FRAMEWORK-level.

An ADS-specific policy encoded in Python remains PROJECT-level.

## 8. Preregistered subwindows

Recurrence is tested across two materially different development regimes:

    PRE_AO
        Checkpoint 523 through Checkpoint 555
        implementation, migration and W5 information architecture

    AO
        Checkpoint 556 through Checkpoint 566
        activation/orchestration architecture and empirical closure

OUT_OF_SCOPE and EVIDENCE_ONLY episodes do not count toward recurrence.

## 9. Preregistered thresholds

Let:

    N = F + P + S

where F = FRAMEWORK_ONLY, P = PROJECT_ONLY and S = SPANS_LAYERS.

### PASS

G1 passes only if all are true:

    F / N >= 0.30
    S / N < 0.50
    PRE_AO contains at least 3 FRAMEWORK_ONLY episodes
    AO contains at least 3 FRAMEWORK_ONLY episodes

Interpretation: framework-level lifecycle pressure is both substantial and recurring, while coupled changes do not dominate.

### FAIL

G1 fails if any are true:

    F / N < 0.20
    S / N >= 0.50
    either PRE_AO or AO contains zero FRAMEWORK_ONLY episodes

Interpretation: independent framework lifecycle is too weak or coupled evolution dominates.

### INCONCLUSIVE

Any result between PASS and FAIL bands is INCONCLUSIVE.

No threshold may be changed after the first episode is classified.

## 10. Qualitative falsifier

A numeric PASS is not sufficient if review reveals that apparently FRAMEWORK_ONLY episodes are merely delayed implementation of project-specific changes from the immediately preceding episode.

If that dependency pattern is systematic, the result must be downgraded to INCONCLUSIVE and the dependency chains reported.

## 11. Audit discipline

The first pass will produce an evidence table for every checkpoint in the bounded range.

Any ambiguous classification must be marked AMBIGUOUS before final adjudication.

Independent second-model coding is required only when:

    more than 20 percent of substantive episodes are initially ambiguous
    OR
    the final result lies within 10 percentage points of a PASS/FAIL boundary
    OR
    one disputed episode can change the categorical outcome

Otherwise a repository-evidence audit is sufficient and avoids unnecessary collaboration overhead.

## 12. Consequences

G1 PASS:
    lifecycle independence supports PSMF as the leading topology;
    proceed to the instance-policy-home decision and Research 218 reconciliation.

G1 INCONCLUSIVE:
    retain PSMF as candidate, but do not make a residency owner disposition;
    obtain stronger evidence before final hierarchy freeze if residency affects it.

G1 FAIL:
    reopen the PSMF target hypothesis against PROJECT_NATIVE_ONLY;
    do not create/extract a generic upstream merely on transferability grounds.

No result authorizes mechanism extraction.

## 13. Current state

    PKIA_E01=OPEN
    PSMF=LEADING_TARGET_HYPOTHESIS
    OWNER_ACCEPTED_TARGET=NO
    G1_PROTOCOL=FROZEN
    G1_RESULT=NOT_RUN
    RESEARCH218=FROZEN_BASELINE_RETAINED
    RESEARCH177=UNCHANGED
    SPECIFICATION028=UNCHANGED
    W5_F0=PAUSED
    AO10=HELD
    AUTHORITY_SWITCH_ALLOWED=false
    NEXT=EXECUTE_G1_LIFECYCLE_INDEPENDENCE_MEASUREMENT
