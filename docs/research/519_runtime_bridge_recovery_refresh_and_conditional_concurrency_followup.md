# Research 519: Runtime Bridge recovery, same-chat tool refresh, and conditional concurrency follow-up

**Date:** 2026-10-05
**Status:** COMMIT-INDEX RECOVERY LIVE / SAME-CHAT TOOL REFRESH OBSERVED / CONCURRENCY ROOT CAUSE OPEN / P01 CONTINUES UNDER RECURRENCE TRIGGER
**Parent:** Research 506, Research 518; Validation 034, Validation 206, Validation 212
**Scope:** Preserve the Runtime Bridge reliability knowledge exposed while freezing R0-P01, distinguish resolved behavior from still-open behavior, and define the exact trigger for whether concurrency investigation interrupts the R0-P01 route.
**Authority:** Operational/reliability reconciliation only. This record does not select a physical architecture, alter Specification 028, authorize production migration, or classify R0-P01.

## 1. Why this record exists

The R0-P01 freeze exposed three different mechanisms that must not be conflated:

1. recovery from an interrupted semantic commit that left an exact staged index;
2. ChatGPT refresh of a changed Runtime Bridge tool projection;
3. intermittent `bridge concurrency limit reached (1)` / uncertain-result behavior after some long-running or interrupted Runtime Bridge operations.

Only the first two are presently resolved or operationally characterized. The third remains an open reliability question and is not yet proven systematic.

## 2. Interrupted semantic-commit recovery is now a first-class bounded action

The Runtime Bridge now exposes:

    codex.git_recover_commit_index

The live release is:

    releaseId       commit-index-recovery-v4
    runtime version 0.1.1-preview.75-commit-index-recovery
    tool count      179

The release was activated and post-activation verification returned no release mismatch.

The action accepts only:

    workspaceId
    expectedHead
    exact repository-relative paths

It reuses existing semantic-commit authority and protected-path policy and is not a general reset/checkout/unstage escape hatch.

Its intended semantics are:

    exact current HEAD must equal expectedHead
    exact non-empty staged path set must equal the declared paths
    transient Git states must be absent
    protected paths are rejected
    only the declared index scope is restored to HEAD
    working-tree bytes are preserved
    refs / HEAD are preserved
    uncertain mutation result is reconciled without replay
    postflight must establish an empty index and preserved working-tree state

## 3. First real public-repository use

Before recovery, the public ADS repository was at:

    HEAD / origin
    6dc76da4a0c56901fe39d4dc23a818b1273f988f

with exactly the eleven intended R0-P01 freeze paths stranded in the Git index after an interrupted semantic commit.

The first live recovery invocation did not return a clean client receipt before the caller timed out. It must therefore not be represented as a response-level PASS.

However, authoritative repository postflight after the call established:

    HEAD unchanged
    origin unchanged
    Git index empty
    all eleven P01 changes preserved in the working tree

The recovery effect therefore occurred successfully. This is state-based reconciliation of an uncertain client response, not invention of a missing tool receipt.

The recovered P01 freeze was subsequently committed as:

    5f41625ad3811b6d769a112885ea2afcbd48952f
    Freeze R0-P01 owner-authenticity probe contract

and later reconciliation proved:

    HEAD == origin/v1-source-vault-bootstrap-resume
    5f41625ad3811b6d769a112885ea2afcbd48952f

with a clean tracked working tree and empty index.

## 4. ChatGPT same-chat tool projection refresh

The new recovery action was live on the MCP server before it was callable from the already-open ChatGPT conversation.

The project owner used the ChatGPT UI path:

    Plug-ins
    -> Codexless Runtime Bridge
    -> ...
    -> Beheren
    -> Tools vernieuwen

After that action, the same existing conversation received the refreshed Runtime Bridge projection and `codex.git_recover_commit_index` became callable.

This is stronger and newer evidence than the 2026-09-03 observation in Validation 034 that a new/fresh conversation might be required after a schema-level tool change.

Current bounded conclusion:

    changed Runtime Bridge tool name/schema
        -> existing ChatGPT conversation may retain stale projection
        -> Tools vernieuwen can refresh the projection in-place
        -> a new chat is not automatically required

This is a current-host observation, not a permanent platform guarantee.

## 5. What Tools vernieuwen is for

The refresh control is now classified narrowly:

    Tools vernieuwen = refresh ChatGPT's projection of the plugin's current tool surface

It is appropriate after a Runtime Bridge release adds, removes, or changes callable tool schemas.

It must not be normalized as the recovery mechanism for ordinary Runtime Bridge execution failures, semantic Git uncertainty, or concurrency saturation.

## 6. Open concurrency / uncertain-result observation

During the recovery/release sequence, some semantic operations returned or were followed by:

    bridge concurrency limit reached (1)

while later repository reconciliation sometimes showed that the underlying Git mutation had nevertheless completed.

This family of observations predates the new recovery action and has appeared previously around semantic commit/push work. The current evidence therefore does not support blaming `codex.git_recover_commit_index` for the phenomenon.

The current server uses an in-memory in-flight admission counter around relevant tool handlers. Under an ordinary handler completion path, `finally` should release that counter. The observed behavior is therefore not yet explained by the simple existence of the counter itself.

Plausible classes of cause remain open, including:

    client timeout versus server handler lifetime
    host-process lifetime after caller-visible timeout
    request/session disconnect lifecycle
    worker/runtime-generation transition effects
    a narrower implementation defect in one uncertain-result path

No one of these is selected as root cause by this record.

## 7. What is not concluded

The evidence does not establish that:

    every future semantic Git operation will hit the concurrency limit
    the Runtime Bridge has become generally unusable
    the new recovery action caused the concurrency behavior
    Tools vernieuwen is required before ordinary work
    the concurrency design requires a major durable-operation redesign

The project has a long history of successful Runtime Bridge operations across semantic Git, GitHub, runtime release, browser, document and agent surfaces.

The recent sequence was unusually stressful: interrupted commit recovery, new tool publication, multiple release iterations, runtime restarts, schema refresh and uncertain mutation reconciliation occurred in close succession.

## 8. Exact continuation trigger

The project will not preempt R0-P01 for a speculative Runtime Bridge redesign.

R0-P01 continues normally from the clean pushed freeze at `5f41625ad3811b6d769a112885ea2afcbd48952f`.

The trigger is:

    during an ordinary, non-release/debug semantic Git operation
    if the same concurrency / uncertain-completion pattern recurs
        -> stop further project mutations
        -> reconcile authoritative repository state first
        -> open a bounded Runtime Bridge root-cause investigation
        -> correlate ChatGPT result, recent-call receipts, handler lifecycle,
           in-flight admission state, host-process lifecycle and repository effect
        -> implement only the architecture justified by that evidence
        -> qualify the repair before resuming ordinary mutations
    otherwise
        -> continue R0-P01
        -> retain this issue as deferred reliability evidence

A mutation timeout or uncertain response must never be retried blindly. Existing postflight/reconciliation discipline remains mandatory.

## 9. Architecture consequence

The Runtime Bridge remains reusable external infrastructure under Research 506.

This incident is useful evidence for the eventual professional control-plane design, but it does not by itself authorize:

    generic unrestricted Git mutation
    arbitrary reset / checkout / branch switching
    a durable operation-controller redesign
    Runtime Bridge extraction
    ADS authority switch

Those decisions remain evidence-driven.

## 10. Current boundary

    COMMIT_INDEX_RECOVERY_TOOL=LIVE
    COMMIT_INDEX_RECOVERY_FIRST_PUBLIC_EFFECT=RECONCILED_SUCCESS
    SAME_CHAT_TOOLS_REFRESH=OBSERVED_WORKING
    TOOLS_REFRESH_PURPOSE=SCHEMA_PROJECTION_ONLY

    CONCURRENCY_ROOT_CAUSE=OPEN
    CONCURRENCY_SYSTEMATIC_FAILURE=NOT_ESTABLISHED
    PREEMPTIVE_RUNTIME_REDESIGN=NO

    RECURRENCE_TRIGGER=ORDINARY_SEMANTIC_GIT_SAME_FAILURE_PATTERN
    ON_TRIGGER=STOP_MUTATIONS_AND_DIAGNOSE
    WITHOUT_TRIGGER=CONTINUE_R0_P01

    R0_P01_FREEZE_COMMIT=5f41625ad3811b6d769a112885ea2afcbd48952f
    R0_P01_FREEZE_PUSHED=true
    R0_P01_HARNESS=NOT_IMPLEMENTED
    NEXT=BOUNDED_MANUAL_CODEX_R0_P01_HARNESS_IMPLEMENTATION
