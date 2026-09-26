# Research 340: Key Author A P1 STATE Pass and Return-Boundary Exposure Reconciliation

**Date:** 2026-09-26
**Status:** P1 STATE PASS / MECHANICAL POSTFLIGHT PASS / SEMANTIC OUTPUT FROZEN PRIVATE / BOUNDED TASK-OWNER EXPOSURE RECORDED / NEXT PHASE NOT AUTHORIZED
**Parent:** Research 339 / owner-run local Claude Code P1 report
**Scope:** Reconcile the first semantic Key Author A phase without inspecting or publishing fixture-level truth, mechanically validate the private STATE output and execution transcript, record the bounded return-boundary exposure created by the owner-pasted Claude Code tool preview, and route to a separate owner decision before any later semantic phase.
**Authority:** Key Author A P1 disposition only. This record does not authorize any later semantic phase, Key Author B, scoring, reviewer execution, production implementation, migration, oracle retirement, or authority switching.

## 1. P1 executor result

The owner-run local Claude Code P1 session returned:

    P1_RESULT
        PASS

    session_id
        efc4ef77-b89d-4121-a906-fca81741bc16

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

    MCP disabled
        PASS

    web denied
        PASS

    local settings absent
        PASS

    STATE fixtures expected
        24

    STATE fixtures completed
        24

    private rule trace
        created

    precedents added
        0

    errata added
        0

    semantic material created
        true

    next phase started
        false

The executor intentionally reported Claude Code version as NOT_EXPOSED because retrieving it from inside P1 would have required a shell command, which Research 339 prohibited.

That is not a P1 failure because the exact installed version was already established during P0/P0.5 and P1's transcript/environment remained configuration-consistent.

## 2. Private-workspace postflight

Task-owner postflight independently verified, without publishing fixture-level semantic content:

    work/PROGRESS.json current_phase
        P1_STATE_COMPLETE_AWAITING_REVIEW

    p1_authorized
        true

    semantic_labels_created
        true

    P1 session count
        1

    P1 session ID
        efc4ef77-b89d-4121-a906-fca81741bc16

    .claude/settings.local.json
        absent

    out/ file count
        1

    private P1 STATE output
        present

    private P1 rule trace
        present

    PRECEDENTS.md
        unchanged from P0 seed size

    ERRATA.jsonl
        still empty

No BIRTH or LEGACY semantic artifact is present in out/.

## 3. Mechanical STATE-output validation

The task owner mechanically validated the private P1 STATE file without surfacing semantic values.

Checks passed:

    output object count
        24

    fixture-ID set
        exactly matches the 24 frozen STATE fixtures

    duplicate fixture IDs
        none

    required fields
        exact match for every object:
            fixture_id
            valid_fact_ids
            invalid_fact_ids
            expected_state
            reason

    expected_state
        every value belongs to the frozen public state_enum

    valid/invalid fact arrays
        structurally valid

    duplicate fact IDs within an output
        none

    valid/invalid overlap
        none

    reason
        nonblank for every fixture

    source fact coverage
        every declared fact ID belongs to its frozen fixture

    source fact completeness
        every frozen fixture fact is classified exactly into valid or invalid

Therefore:

    P1_STATE_MECHANICAL_VALIDATION
        PASS

This is a shape/coverage/integrity check only.

The task owner did not semantically re-derive the 24 fixture answers and did not compare them against another key.

## 4. Transcript-level execution verification

The exact P1 Claude Code transcript was located uniquely by session ID.

Mechanical transcript parsing found exactly these actual tool-use types:

    Read
        9

    Edit
        4

    Write
        2

    Glob
        1

No actual tool-use block invoked:

    Bash
    PowerShell
    shell/terminal execution
    WebSearch
    WebFetch
    Agent
    MCP
    IDE tools

The actual Read targets were exactly the P1-authorized files:

    work/PROGRESS.json
    work/CODEBOOK.md
    work/PRECEDENTS.md
    inputs/r2_v03/KEY_AUTHOR_INSTRUCTIONS.md
    inputs/r2_v03/key_author_schema.json
    inputs/addendum/DRP03_R2_KEY_AUTHOR_EXECUTION_ADDENDUM_V01.md
    inputs/r2_v03/public_fixtures/state_rules.json
    inputs/r2_v03/packets/state.json
    inputs/r2_v03/packets/state_provenance.json

The only semantic write target was the authorized private P1 STATE output.

The other write target was the authorized private P1 rule trace.

Edits were limited to work/PROGRESS.json.

The final Glob operation checked the private workspace for the local-settings condition.

Transcript metadata independently records:

    permissionMode
        default

    model
        claude-opus-5-5

    effort
        high

    cwd
        KEYA_WORK

Therefore:

    P1_SHELL_PROHIBITION
        PASS

    P1_EVIDENCE_BOUNDARY
        PASS

## 5. Host-side IDE isolation

Task-owner host postflight observed the P1 Claude CLI process started at approximately 10:14 local time.

The P1 process had no connection to the active VS Code IDE listener.

A separate older Claude CLI process remained connected to VS Code.

This is permitted by Research 336.

Therefore:

    KEY_A_P1_IDE_ATTACHED
        false

    P1_IDE_ISOLATION
        PASS

## 6. Semantic freeze status

P1 is the first phase that intentionally creates hidden Key Author A semantic material.

The STATE output is now treated as:

    PRIVATE
    FROZEN_PENDING_LATER_KEY_ASSEMBLY
    NOT_REPOSITORY_MATERIAL
    NOT_KEY_B_VISIBLE
    NOT_DECISION_REVIEWER_VISIBLE

The task owner has mechanically observed an opaque digest and byte length for change-detection purposes, but this public record intentionally does not publish the phase digest or semantic values.

Before any later Key A phase consumes the P1 output, task-owner postflight must verify that the private P1 bytes remain unchanged from the reviewed P1 boundary.

## 7. Return-boundary exposure incident

The owner's pasted Claude Code console transcript included a tool-preview excerpt from the private P1 STATE output before the bounded final P1 report.

That excerpt exposed a limited fragment of Key A STATE semantic truth to:

    the human project owner
    the ChatGPT task-owner interaction chatgpt-31

It was not written to:

    the ADS public repository
    GitHub
    MC-0029 collaboration messages
    Key Author B storage
    a decision-reviewer environment

The exposure occurred after the P1 semantic file had been written and frozen, so it did not influence Key Author A's P1 derivation.

Disposition:

    P1_OUTPUT_VALIDITY
        UNAFFECTED

    KEY_A_AUTHOR_INDEPENDENCE
        UNAFFECTED

    PUBLIC_KEY_LEAK
        NO

    FUTURE_KEY_B_BLINDNESS
        STILL ACHIEVABLE, BUT THIS CHAT MUST BE EXCLUDED FROM KEY B

    FUTURE_FRESH_DECISION_REVIEWER_USE_OF_CHATGPT_31
        PROHIBITED

The confidentiality boundary is therefore expanded prospectively:

    chatgpt-31 and the human-owner copy/paste surface are treated as exposed-to-Key-A-semantic-fragment

Future owner handoffs must paste only bounded phase reports, not Claude Code tool previews or semantic file excerpts.

This incident is preserved rather than hidden because independence accounting is part of the experiment.

## 8. P1 disposition

All P1 execution and mechanical acceptance gates passed.

Therefore:

    P1_STATE
        PASS

    P1_SEMANTIC_MATERIAL
        CREATED_AND_PRIVATE

    P1_RETURN_BOUNDARY_DEVIATION
        RECORDED / NON-INVALIDATING

    P2_OR_LATER_PHASE
        NOT AUTHORIZED

No later semantic phase begins automatically from this PASS.

The next step is task-owner design/review of the exact next phase boundary followed by an explicit owner authorization decision.

## 9. Current boundary

    PUBLIC_R2_FREEZE=UNCHANGED
    EXECUTION_ADDENDUM=UNCHANGED

    P0_5=PASS
    P1_STATE=PASS

    KEY_A_STATE_OUTPUT=PRIVATE_FROZEN
    KEY_A_SEMANTIC_MATERIAL_CREATED=true

    KEY_A_BIRTH_LABELS=NONE
    KEY_A_LEGACY_LABELS=NONE
    KEY_A_GROUPING_PAIRS=NONE
    COMPLETE_KEY_A_BYTES=NOT_CREATED

    CHATGPT31_KEY_A_FRAGMENT_EXPOSURE=true
    KEY_B_ACCESS_TO_CHATGPT31=PROHIBITED

    LATER_SEMANTIC_PHASE_AUTHORIZED=false
    NEXT=TASK_OWNER_DEFINE_NEXT_KEY_A_PHASE_AND_OWNER_AUTHORIZATION_BOUNDARY
