# Research 338: Key Author A P0.5 Attempt 002 Pass and P1 Authorization Boundary

**Date:** 2026-09-26
**Status:** P0.5 ATTEMPT 002 PASS / HOST IDE ISOLATION VERIFIED / PRE-P1 HARDENING COMPLETE / NO SEMANTIC MATERIAL / OWNER P1 AUTHORIZATION NEXT
**Parent:** Research 337 / owner-run local Claude Code P0.5 Attempt 002 report
**Scope:** Reconcile P0.5 Attempt 002, independently verify the remaining host-side and private-workspace controls, close the pre-P1 hardening gate, and route to an explicit owner authorization decision before semantic Key Author A work begins.
**Authority:** Operational key-author execution control only. The Research 332 public protocol freeze and Research 334 execution addendum remain unchanged. This record does not itself authorize P1.

## 1. Attempt 002 executor result

The owner-run local Claude Code session returned:

    P0_5_RESULT
        PASS

    session_id
        a59b8c99-1a18-40e3-a5c4-7fbcc9f2bc55

    Claude Code version
        2.1.283

    model
        claude-opus-5-5

    effort
        high

    permission mode
        default

    external terminal
        PASS

    IDE context absent
        PASS

    Chrome disabled
        PASS

    MCP disabled
        PASS

    web denied
        PASS

    local settings absent
        PASS

    project settings SHA-256
        8579fdb498a7d8a80b33025aa13d0a6a200e78881fd4e4fc7979e267a1d61eb6

    Research 330 export
        PASS

    P0 transcript copy
        PASS

    no semantic material
        PASS

    p1_authorized
        false

P1 was not started.

## 2. Independent private-workspace verification

Task-owner postflight independently verified:

    .claude/settings.json SHA-256
        8579fdb498a7d8a80b33025aa13d0a6a200e78881fd4e4fc7979e267a1d61eb6

    .claude/settings.local.json
        ABSENT

    work/PROGRESS.json current_phase
        P0_5_COMPLETE_AWAITING_REVIEW

    work/PROGRESS.json p1_authorized
        false

    work/PROGRESS.json semantic_labels_created
        false

    P0.5 session recorded
        a59b8c99-1a18-40e3-a5c4-7fbcc9f2bc55

    out/ file count
        0

The private P0.5 provenance record also binds:

    model
        claude-opus-5-5

    effort
        high

    permission mode
        default

    launch parent chain
        explorer.exe > powershell.exe > claude.exe

    launch flags
        --model claude-opus-5-5
        --effort high
        --permission-mode default
        --setting-sources project
        --strict-mcp-config
        --no-chrome

No semantic content is recorded in the P0.5 provenance.

## 3. Research 330 exact export verification

Task-owner postflight independently verified exactly one file in the private Research 330 export directory.

The exported raw Git blob has:

    SHA-256
        8e191d81d15da3254466194f874223aebb377306056619f47778565ae286a8fa

    bytes
        28175

The private provenance records Git blob:

    57664148320440dbb7f0c9daf97b8dc5ccc06b08

from frozen source commit:

    c1664b54fada13e05a96b1743000a78b77b41940

using:

    git cat-file blob

This matches the exact Research 335 requirement.

## 4. P0 transcript containment verification

Task-owner postflight independently verified the copied P0 transcript at:

    transcripts/622a692e-b9e9-4565-9e40-a0f3ba561848.jsonl

with:

    SHA-256
        9df21fd17e9dc9278a9600aafbd09e97dbac80af4f7f1c45f054402860982e9b

    bytes
        562437

The P0.5 provenance records exactly one source candidate and byte equality between source and private copy.

This closes the specific P0 transcript containment requirement from Research 335.

The normal Claude client transcript store remains part of the Key A confidentiality boundary. Future Key Author B must still be isolated from all Key A transcript storage, including P0, P0.5 and later semantic-session transcripts.

## 5. Host-side IDE isolation verification

The P0.5 Attempt 002 Claude CLI process started at approximately 09:49 local time from the standalone external PowerShell launch.

Task-owner host postflight observed:

    current Attempt 002 Claude CLI PID
        64212

    active VS Code IDE listener
        localhost port 63596

    Attempt 002 -> IDE listener connection
        NONE

A different older Claude CLI process:

    PID 50008

remained connected to the VS Code IDE listener.

Therefore the active IDE lockfile belongs to other ongoing ADS/Claude activity and does not imply Key A attachment.

Disposition:

    KEY_A_CLAUDE_CODE_IDE_ATTACHED
        false

    IDE_DISCONNECTED
        PASS

    VS_CODE_MAY_REMAIN_RUNNING
        true

    CODEXLESS_MAY_REMAIN_RUNNING
        true

This satisfies Research 336.

## 6. No-semantic-material disposition

The executor reports no semantic material.

Task-owner postflight independently verified the strongest available mechanical indicators:

    out/
        empty

    p1_authorized
        false

    semantic_labels_created
        false

    current phase
        P0_5_COMPLETE_AWAITING_REVIEW

The P0.5 session performed only the two authorized non-semantic remediations and provenance/progress recording.

No evidence indicates creation of:

    STATE expected outputs
    BIRTH labels
    LEGACY labels
    LEGACY witness/control identities
    grouping pairs
    canonical Key A bytes

Disposition:

    P0_5_ATTEMPT_002_SEMANTIC_CONTAMINATION
        NONE

## 7. P0.5 gate disposition

Every Research 335 P0.5 gate is now satisfied:

    Research 330 exact export
        PASS

    P0 transcript copied and hashed
        PASS

    standalone external-terminal launch
        PASS

    IDE disconnected
        PASS

    model claude-opus-5-5
        PASS

    effort high
        PASS

    interactive-approval permission class
        PASS
        exact recorded mode = default

    prior deny configuration effective
        PASS

    no semantic labels created
        PASS

Therefore:

    P0_5
        PASS

    PRE_P1_HARDENING
        COMPLETE

## 8. Authorization boundary

Passing P0.5 makes Key Author A P1 technically eligible under the frozen execution protocol.

It does not itself authorize semantic execution.

The project-owner instruction for this continuation requires explicit authorization before semantic Key Author A work begins.

Therefore:

    P1_READY
        true

    P1_AUTHORIZED
        false

    NEXT_EXPECTED_ACTOR
        human owner

The next legitimate action is an explicit owner decision to authorize or hold P1.

Until that decision:

    do not change work/PROGRESS.json p1_authorized

    do not create STATE expected outputs

    do not create BIRTH or LEGACY semantic labels

    do not create witness/control identities

    do not create grouping pairs

    do not create canonical/private Key A bytes

## 9. Current boundary

    PUBLIC_R2_FREEZE=UNCHANGED
    EXECUTION_ADDENDUM=UNCHANGED

    P0_5_ATTEMPT_001=HOLD_PRESERVED
    P0_5_ATTEMPT_002=PASS
    PRE_P1_HARDENING=COMPLETE

    KEY_A_MODEL=claude-opus-5-5
    KEY_A_EFFORT=HIGH
    KEY_A_PERMISSION_CLASS=INTERACTIVE_APPROVAL
    KEY_A_PERMISSION_MODE_RECORDED=default
    KEY_A_IDE_ATTACHED=false

    KEY_A_LABELS=NONE
    KEY_A_PRIVATE_BYTES=NOT_CREATED

    P1_READY=true
    P1_AUTHORIZED=false
    NEXT=OWNER_P1_AUTHORIZATION_DECISION
