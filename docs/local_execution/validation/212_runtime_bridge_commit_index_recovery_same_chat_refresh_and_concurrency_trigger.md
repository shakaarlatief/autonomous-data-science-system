# Validation 212: Runtime Bridge Commit-Index Recovery, Same-Chat Refresh, and Concurrency Trigger

**Date:** 2026-10-05
**Status:** RECOVERY EFFECT PASS BY REPOSITORY RECONCILIATION / SAME-CHAT TOOL REFRESH PASS / CONCURRENCY ROOT CAUSE OPEN
**Scope:** Preserve the live qualification evidence for the new bounded commit-index recovery action, the ChatGPT `Tools vernieuwen` behavior, and the deliberately conditional follow-up policy for intermittent Runtime Bridge concurrency/uncertain-result observations.
**Authority:** Operational validation evidence only. This record does not redefine R0-P01 semantics, select the physical architecture, change Specification 028, or authorize migration.

## 1. Starting incident

An earlier interrupted `codex.git_commit_paths` attempt against the public ADS repository left exactly the eleven R0-P01 freeze paths staged while:

    HEAD
    6dc76da4a0c56901fe39d4dc23a818b1273f988f

remained unchanged.

The generic command lane was intentionally unable to mutate `.git`, so ordinary arbitrary `git restore --staged` was not available to ChatGPT through that lane.

This exposed a real purpose-specific control-plane gap.

## 2. Qualified release

The private local-runtime line produced and activated:

    releaseId       commit-index-recovery-v4
    runtime version 0.1.1-preview.75-commit-index-recovery
    surface          codexless-public-preview-v2
    tool count       179

Post-activation release verification returned zero mismatches.

The added public action is:

    codex.git_recover_commit_index

and its public schema contains only:

    workspaceId
    expectedHead
    paths

## 3. Live public-repository recovery effect

The first real invocation targeted the exact eleven staged P01 paths and expected HEAD `6dc76da4a0c56901fe39d4dc23a818b1273f988f`.

The client-facing call did not produce a final success receipt before timeout. No stronger receipt claim is made.

Subsequent authoritative repository reads established:

    HEAD unchanged
    origin unchanged
    index empty
    all eleven changes preserved as working-tree changes

Therefore:

    RECOVERY_EFFECT=PASS_BY_POSTFLIGHT_RECONCILIATION
    RESPONSE_LEVEL_RECEIPT=UNAVAILABLE

The distinction is intentional.

## 4. P01 durability after recovery

The recovered changes were committed exactly once as:

    5f41625ad3811b6d769a112885ea2afcbd48952f
    Freeze R0-P01 owner-authenticity probe contract

The commit contains exactly the intended eleven files.

Later reconciliation established:

    HEAD
    5f41625ad3811b6d769a112885ea2afcbd48952f

    origin/v1-source-vault-bootstrap-resume
    5f41625ad3811b6d769a112885ea2afcbd48952f

The public tracked working tree and index were clean.

## 5. Same-chat ChatGPT tool refresh

Before UI refresh:

    live MCP server tool count 179
    new recovery tool present on server
    existing ChatGPT chat projection did not expose the new callable action

The owner selected:

    Plug-ins
    -> Codexless Runtime Bridge
    -> ...
    -> Beheren
    -> Tools vernieuwen

After returning to the same conversation:

    codex.git_recover_commit_index became visible and callable

Result:

    SAME_CHAT_TOOL_SCHEMA_REFRESH=PASS

This amends the operational interpretation of Validation 034. A fresh conversation is not automatically required for a new developer-MCP tool projection in the currently observed ChatGPT host.

## 6. Scope of the refresh procedure

Qualified purpose:

    refresh ChatGPT's plugin tool projection after a tool-surface change

Not qualified as:

    semantic-operation recovery
    concurrency reset
    Git reconciliation mechanism
    ordinary per-turn prerequisite

If the plugin schema has not changed, routine use of `Tools vernieuwen` is not prescribed.

## 7. Concurrency / uncertain-result evidence

During the surrounding runtime/recovery sequence, later semantic operations sometimes encountered:

    bridge concurrency limit reached (1)

and some caller-visible failures/timeouts were later found, by repository reconciliation, to have corresponding successful Git effects.

The current evidence is insufficient to determine whether this is:

    a caller timeout while the handler legitimately remains active
    a host-process lifetime issue
    a disconnect/session-lifecycle issue
    a worker-generation interaction
    or another bounded implementation defect

It is also insufficient to establish that ordinary future semantic Git operations will fail systematically.

## 8. Decision rule

Do not interrupt R0-P01 for a speculative reliability redesign now.

Use this trigger:

    next ordinary semantic Git work
        if normal -> continue project work
        if same concurrency / uncertain-completion pattern recurs
            -> stop further mutations
            -> reconcile state
            -> diagnose Runtime Bridge lifecycle before continuing

The diagnosis must include available recent-call evidence, handler admission/release behavior, host-process lifetime, client-visible response, and final repository state.

Blind mutation replay remains prohibited.

## 9. Validation result

    COMMIT_INDEX_RECOVERY_TOOL_LIVE=true
    RECOVERY_EFFECT_PASS_BY_RECONCILIATION=true
    SAME_CHAT_TOOLS_REFRESH_PASS=true
    FRESH_CHAT_REQUIRED=false_current_observation
    TOOLS_REFRESH_IS_CONCURRENCY_FIX=false

    CONCURRENCY_ROOT_CAUSE=OPEN
    CONCURRENCY_SYSTEMATIC=false_not_established
    CONDITIONAL_DIAGNOSIS_TRIGGER=ARMED

    P01_FREEZE_PUSHED=true
    P01_CONTINUATION_UNBLOCKED=true
