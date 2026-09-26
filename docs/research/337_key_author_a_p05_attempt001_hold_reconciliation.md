# Research 337: Key Author A P0.5 Attempt 001 Hold Reconciliation

**Date:** 2026-09-26
**Status:** P0.5 ATTEMPT 001 HOLD / MANUAL-DEFAULT MODE SATISFIED / CURRENT SESSION IDE-DISCONNECTED / LOCAL STANDING-APPROVAL DRIFT REQUIRES RESET / NO SEMANTIC CONTAMINATION
**Parent:** Research 335 / Research 336 / owner-run local Claude Code P0.5 Attempt 001 report
**Scope:** Reconcile the first P0.5 execution report, correct the permission-mode interpretation against the frozen task-owner decision and current Claude Code behavior, independently verify the current session's IDE attachment state where host evidence is available, preserve the session-created local permission drift, and route a clean P0.5 rerun before any semantic work.
**Authority:** Operational key-author execution control only. The Research 332 public protocol freeze, Research 334 execution addendum, Research 335 semantic configuration, and Research 336 external-terminal isolation invariant remain unchanged.

## 1. Attempt 001 disposition

P0.5 Attempt 001 stopped before either authorized remediation and returned:

    P0_5_RESULT
        HOLD

    session_id
        030cfe65-3077-4d74-8632-a2b0860e241c

    Claude Code version
        2.1.283

    model
        claude-opus-5-5

    effort
        high

    permissionMode recorded in transcript
        default

    external terminal
        PASS

    Research 330 export
        NOT ATTEMPTED

    P0 transcript copy/hash
        NOT ATTEMPTED

The executor stopped before semantic work.

The attempt remains HOLD, but the task-owner review narrows the reason. The reported permission-mode string and the mere existence of a live VS Code IDE lockfile are not blockers by themselves. The remaining blocker is session-created standing permission drift that must be removed before the clean rerun.

## 2. Permission-mode reconciliation

Research 335 did not require the literal internal string `manual`.

It fixed the semantic permission class as:

    INTERACTIVE_APPROVAL

and defined that class as:

    do not use auto/bypass-style autonomous permission escalation

    use the product's current manual/default approval mode

    record the exact Claude Code mode string exposed by the installed version

Current Claude Code 2.1.283 documentation states that the UI mode named Manual has config/internal value:

    default

and that:

    manual

is an accepted CLI alias for that same mode.

Therefore:

    launch flag
        --permission-mode manual

    session transcript permissionMode
        default

are consistent rather than contradictory.

The previous ChatGPT P0.5 launch prompt overconstrained the report to the literal string `manual`. That overconstraint is corrected prospectively.

For the clean rerun, use the canonical config value directly:

    --permission-mode default

Expected recorded session value:

    default

This still satisfies Research 335's INTERACTIVE_APPROVAL decision.

Current external reference consulted:

    https://code.claude.com/docs/en/permission-modes

## 3. Session-created local permission drift

Before P0.5 Attempt 001, task-owner inspection of KEYA_WORK showed:

    .claude/settings.json

and no:

    .claude/settings.local.json

During Attempt 001, Claude Code created:

    .claude/settings.local.json

after standing "don't ask again" approvals.

The executor's intermediate report observed an earlier version of this file. Task-owner postflight inspection found the final on-disk file had expanded to four allow rules and had:

    SHA-256
        8dd70c5b407a61b8abd286d16326c7aaefbd6faf4691abfa871deb01bd3810cb

    bytes
        1396

The rules include broad standing approvals for:

    PowerShell(claude *)
    PowerShell(Get-ChildItem *)
    PowerShell(Get-Content *)

plus bounded environment/config inspection commands.

The broad `PowerShell(claude *)` rule is incompatible with the intended P0.5/P1 interactive-approval boundary because later Claude CLI mutation/configuration commands could execute without a fresh owner prompt.

Current Claude Code settings documentation confirms that "Yes, and don't ask again" creates project-local `permissions.allow` rules in `.claude/settings.local.json`, and those local allow rules apply as standing approvals.

Current external reference consulted:

    https://code.claude.com/docs/en/settings

Disposition:

    .claude/settings.local.json
        MUST BE REMOVED before P0.5 Attempt 002

    standing "don't ask again" approvals
        PROHIBITED for Key A P0.5/P1

    owner approvals
        ONE-TIME ONLY where an action genuinely requires approval

The failed-attempt transcript and this reconciliation preserve the evidence. The accidental permission file itself has no preservation requirement and should not remain active.

## 4. IDE isolation reconciliation

Research 336 requires:

    KEY_A_CLAUDE_CODE_IDE_ATTACHED=false

It does not require:

    VS_CODE_PROCESS_CLOSED=true

Attempt 001 reported a standalone external terminal, process ancestry outside VS Code, no IDE-provided context, no IDE tool exposure, and no Claude IDE environment variable, but conservatively marked IDE_DISCONNECTED=FAIL because a live VS Code IDE lockfile existed.

Task-owner postflight inspected the host network state.

The P0.5 Claude CLI process corresponding to the Attempt 001 launch had no TCP connection to the active VS Code IDE MCP listener.

A different older Claude CLI process did have a loopback connection to that listener.

Therefore the live lockfile represented an active IDE server for other Claude/ADS activity, not attachment of the P0.5 Attempt 001 process.

Disposition:

    P0.5 Attempt 001 current-session IDE attachment
        DISCONNECTED / PASS

    VS Code
        MAY REMAIN RUNNING

    Codexless
        MAY REMAIN RUNNING

    live IDE lockfile alone
        NOT EVIDENCE THAT KEY A SESSION IS ATTACHED

Current Claude Code IDE documentation confirms that the VS Code extension exposes a loopback IDE MCP server and that an external-terminal CLI uses `/ide` to connect to VS Code.

Therefore the Key A session must not invoke `/ide`.

Current external reference consulted:

    https://code.claude.com/docs/en/ide-integrations

## 5. No-semantic-material reconciliation

The executor reported:

    NO_SEMANTIC_MATERIAL=FAIL

only because the post-remediation verification phase was not reached.

That field is not evidence that semantic material exists.

Task-owner postflight independently verified after Attempt 001:

    out/ file count
        0

    work/PROGRESS.json p1_authorized
        false

    work/PROGRESS.json semantic_labels_created
        false

    work/PROGRESS.json current_phase
        P0_COMPLETE_AWAITING_REVIEW

    recorded semantic session count
        unchanged at 1 P0 session

The owner-run report also states that no Research 330 export, P0 transcript copy, semantic label, or workspace semantic artifact was created.

Disposition:

    P0.5 ATTEMPT 001 SEMANTIC CONTAMINATION
        NONE

    KEY_A_LABELS
        NONE

    KEY_A_PRIVATE_BYTES
        NOT CREATED

    P1
        NOT AUTHORIZED

## 6. Clean P0.5 Attempt 002

Before Attempt 002:

    stop/exit Attempt 001

    remove the session-created:
        .claude/settings.local.json

    verify the original:
        .claude/settings.json
        SHA-256 8579fdb498a7d8a80b33025aa13d0a6a200e78881fd4e4fc7979e267a1d61eb6

Relaunch from standalone Windows Terminal / PowerShell with:

    model
        claude-opus-5-5

    effort
        high

    permission mode
        default

    Chrome
        disabled

    MCP
        strict / no configured servers

The clean session must use one-time approvals only.

The clean session must not invoke `/ide`.

P0.5 Attempt 002 must then complete the two still-pending non-semantic remediations:

    exact Research 330 raw Git-blob export

    exact P0 transcript copy/hash

and re-run the complete P0.5 postflight.

P1 remains unauthorized until Attempt 002 is returned and reviewed.

## 7. Current boundary

    PUBLIC_R2_FREEZE=UNCHANGED
    EXECUTION_ADDENDUM=UNCHANGED

    P0=PASS_WITH_REMEDIATION
    P0_5_ATTEMPT_001=HOLD

    P0_5_ATTEMPT_001_PERMISSION_MODE=PASS_DEFAULT_IS_MANUAL_CONFIG_VALUE
    P0_5_ATTEMPT_001_EXTERNAL_TERMINAL=PASS
    P0_5_ATTEMPT_001_IDE_DISCONNECTED=PASS_TASK_OWNER_HOST_VERIFIED

    P0_5_ATTEMPT_001_LOCAL_PERMISSION_DRIFT=BLOCKING
    P0_5_ATTEMPT_001_RESEARCH330_EXPORT=NOT_ATTEMPTED
    P0_5_ATTEMPT_001_P0_TRANSCRIPT_COPY=NOT_ATTEMPTED

    P0_5_ATTEMPT_001_SEMANTIC_CONTAMINATION=NONE
    KEY_A_LABELS=NONE
    KEY_A_PRIVATE_BYTES=NOT_CREATED

    P1=NOT_AUTHORIZED
    NEXT=P0_5_ATTEMPT_002_CLEAN_PERMISSION_RERUN
