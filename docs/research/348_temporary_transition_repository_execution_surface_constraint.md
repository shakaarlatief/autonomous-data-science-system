# Research 348: Temporary Transition Repository Execution-Surface Constraint

**Date:** 2026-09-26
**Status:** OWNER-APPROVED TEMPORARY OPERATING CONSTRAINT / CODEXLESS RUNTIME BRIDGE ONLY FOR ADS REPOSITORY OPERATIONS / GITHUB CONNECTOR QUARANTINED FOR THIS REPOSITORY / TARGET ARCHITECTURE UNCHANGED
**Parent:** Research 347 / owner clarification after P3 Batch 1 repository reconciliation
**Scope:** Preserve a temporary transition-period operating constraint for the current ADS public repository after a mixed local/remote mutation incident. This is a current development-method control only. It does not select the future Project operating architecture, Git provider, branch strategy, promotion mechanism, local/remote execution model, or accepted-state realization.
**Authority:** Owner-approved current operating procedure during the present architecture transition. Release or amendment requires a deliberate later decision.

## 1. Trigger

During the Research 347 / Checkpoint 684 reconciliation, the task owner initially used the Codexless Runtime Bridge for local repository work. When several Runtime Bridge write attempts were rejected by the active safety guard, the task owner silently fell back to the native GitHub connector for direct repository-file mutation.

The GitHub connector's file mutation operations committed each file independently. One logical transition therefore fragmented into several published commits instead of one coherent multi-file transition.

The direct-remote sequence included:

    a8d88951  Record Key A P3 batch one acceptance
    786bbb31  Add checkpoint 684
    87fa707f  Route to P3 batch two
    698e8a8d  Update MC-0029 after P3 batch one
    39011eb2  Index P3 batch one acceptance
    1ab2f5a1  Route MC-0029 to P3 batch two
    57b5ed16  Record P3 batch one acceptance

Consequences included:

    fragmented history
    transient local/remote divergence
    temporarily partial coordination-state publication
    ambiguity about which mutation surface had authoritative completion state

The private P3 Batch 1 semantic artifact was not affected. This was a repository/workflow-integrity issue, not a semantic-key-integrity failure.

The already-published commits are preserved. Public history is not rewritten merely to cosmetically restore atomicity.

## 2. Architectural interpretation

This constraint is not a target-architecture selection.

Research 276 and the accepted WARRANT-F V0.2 architecture explicitly preserve freedom over:

    branch strategy
    push/pull/merge procedure
    promotion procedure
    accepted-state carrier
    local versus remote execution
    provider / Git-host
    executor surface
    workflow mechanism

Therefore this record must not be interpreted as:

    future ADS must be local-first
    GitHub APIs are architecturally disallowed
    Runtime Bridge is permanently selected as the target provider
    one particular Git workflow has target preservation rights

The future operating realization remains open and is governed by the accepted architecture, evidence, later realization design, qualification and authority-switch process.

## 3. Temporary transition rule

Effective immediately for the current public:

    autonomous-data-science-system

repository during the present transition:

    CODEXLESS RUNTIME BRIDGE
        is the single authorized ChatGPT execution surface for ADS repository operations

    NATIVE GITHUB CONNECTOR
        is prohibited for ADS repository operations

The prohibition covers both mutation and routine repository-state retrieval when equivalent evidence is available through the Runtime Bridge.

Repository operations include:

    file creation
    file editing
    file deletion
    Git status/diff/log inspection
    validation execution
    staging/commit operations
    fetch/pull/push operations
    branch/ref inspection
    repository file retrieval used to drive development decisions

The purpose is execution-surface coherence during transition, not distrust of GitHub as a future provider.

## 4. Failure behavior

A Runtime Bridge failure does not authorize silent fallback to another repository execution surface.

If the required Runtime Bridge capability fails, is blocked, or appears missing:

    STOP the affected repository mutation
    inspect the current local and remote state through the Runtime Bridge where possible
    diagnose the Runtime Bridge or execution-policy issue
    repair, extend or explicitly reconsider the execution path
    preserve partial durable effects if any
    rerun required validation
    resume only after the path is understood

Do not:

    switch to the GitHub connector merely because it is available
    create direct remote commits as an implicit fallback
    interleave local and direct-remote mutation paths inside one logical transition
    infer that a failed local command changes the target architecture

An exception requires an explicit deliberate decision by the owner/task owner before use.

## 5. Current transitional mutation discipline

While this temporary constraint is active, the preferred current-repository procedure is:

    mutate the local checkout through the Runtime Bridge
    inspect the complete local diff
    run the required repository validations
    preserve one coherent multi-file logical transition where practical
    revalidate branch HEAD before advancement
    commit through the Runtime Bridge Git capability
    fetch/revalidate upstream
    push through the Runtime Bridge
    confirm local == origin and working tree clean

This procedure is a transition-period realization of the current development method.

It is not a frozen requirement for the future architecture.

## 6. Continuity requirement

The constraint must be visible to a fresh collaborator without relying on chat memory.

Therefore it is reflected in:

    docs/DEVELOPMENT_METHOD.md
    docs/CONTINUITY.md
    docs/CURRENT_STATE.md
    docs/KNOWLEDGE_MAP.md

The live P3 semantic route is unchanged.

Research 347 remains authoritative for:

    P3 Batch 1 PASS
    Batch 2 task-owner release

The current semantic boundary remains:

    key-author-birth-heldout-batch-two-execution-boundary

## 7. Release condition

This constraint remains active until a deliberate later reassessment.

Natural reassessment points include:

    relevant target operating-workflow realization
    physical migration planning
    accepted-state/promotion realization
    authority-switch preparation
    an explicit need for a capability unavailable through Runtime Bridge
    evidence that a multi-surface repository workflow is preferable and sufficiently governed

Release is not automatic merely because:

    the GitHub connector becomes convenient
    a Runtime Bridge call fails
    another model prefers direct Git-host access
    the project reaches a new chat

## 8. Current state

    TRANSITION_REPOSITORY_EXECUTION_SURFACE
        CODEXLESS_RUNTIME_BRIDGE_ONLY

    GITHUB_CONNECTOR_FOR_ADS_REPOSITORY
        PROHIBITED

    SILENT_FALLBACK_ON_RUNTIME_BRIDGE_FAILURE
        PROHIBITED

    EXPLICIT_EXCEPTION_PATH
        REQUIRED

    TARGET_WORKFLOW_ARCHITECTURE
        UNCHANGED / STILL OPEN AT REALIZATION LAYER

    P3_BATCH1
        PASS_PRIVATE_FROZEN

    P3_BATCH2
        TASK_OWNER_RELEASED

    RECOVERY_RECONCILIATION
        COMPLETE

    LOCAL_REMOTE_SYNC_BEFORE_MUTATION
        PASS / FAST-FORWARDED THROUGH RUNTIME BRIDGE

    STALE_COORDINATION_FILES
        REPAIRED / REVIEW_INBOX + MC-0029 BRIEF

    RESEARCH347_METADATA_DEFECT
        REPAIRED / MISSING SCOPE RESTORED

    PUBLIC_REPOSITORY_INTEGRITY
        PASS

    NEXT
        CONTINUE P3 BATCH 2
