# Research 339: Key Author A P1 Explicit Owner Authorization

**Date:** 2026-09-26
**Status:** P1 EXPLICITLY AUTHORIZED / STATE SEMANTIC PHASE ONLY / OWNER LAUNCH NEXT / P2-P8 NOT AUTHORIZED
**Parent:** Research 338 / project-owner explicit authorization
**Scope:** Preserve the owner's explicit authorization for Key Author A P1 after the passing P0.5 gate, bind the exact semantic-phase boundary, and route execution to the first STATE derivation session.
**Authority:** Key Author A execution authorization for P1 only. This record does not authorize P2-P8, Key Author B, scoring, reviewer execution, production implementation, migration, oracle retirement, or authority switching.

## 1. Owner decision

The project owner explicitly stated:

    I authorize P1.

This satisfies the owner-authorization boundary established by Research 338 / Checkpoint 675.

Disposition:

    P1_READY
        true

    P1_AUTHORIZED
        true

    P2_THROUGH_P8_AUTHORIZED
        false

The authorization is deliberately narrow. It authorizes only the first semantic Key Author A phase.

## 2. P1 semantic scope

Research 335 already fixes P1 as:

    STATE semantic derivation

P1 therefore derives all 24 STATE expected outputs independently from the frozen inputs authorized by the Research 334 execution addendum.

Allowed semantic sources are limited to the private frozen copies of:

    inputs/r2_v03/packets/state.json
    inputs/r2_v03/packets/state_provenance.json
    inputs/r2_v03/public_fixtures/state_rules.json
    inputs/r2_v03/KEY_AUTHOR_INSTRUCTIONS.md
    inputs/r2_v03/key_author_schema.json
    inputs/addendum/DRP03_R2_KEY_AUTHOR_EXECUTION_ADDENDUM_V01.md
    work/CODEBOOK.md
    work/PRECEDENTS.md

The author may use the bounded STATE provenance because the frozen addendum explicitly authorizes it for key authors.

The other key author's outputs remain unseen.

## 3. Fixed execution configuration

The P1 semantic session must preserve the configuration qualified by Research 338:

    executor
        local Claude Code

    exact model
        claude-opus-5-5

    effort
        high

    permission class
        INTERACTIVE_APPROVAL

    recorded Claude Code mode
        default

    launch surface
        standalone external Windows Terminal / PowerShell

    IDE attachment
        prohibited

    Chrome integration
        disabled

    MCP / web / GitHub connectors
        disabled / denied

    standing local permission overrides
        absent

A model or material configuration change after semantic work begins requires STOP and task-owner review.

No subagent or parallel worker may make semantic judgments.

## 4. Shell boundary

Research 335 explicitly freezes:

    P1 STATE shell use = PROHIBITED

Therefore P1 performs semantic STATE derivation only through the local Claude Code file-reading/writing surface within the private Key A workspace.

P1 must not execute:

    PowerShell
    Bash
    Git
    Python
    external commands
    repository queries
    web/network operations

No shell approval should be required in P1.

If Claude determines that a shell command is necessary to complete STATE derivation:

    STOP
    report HOLD
    do not improvise

## 5. P1 output boundary

P1 creates private semantic Key A material for the first time.

Required semantic output:

    all 24 canonical STATE expected-output objects

with exactly the fields frozen by key_author_schema.json:

    fixture_id
    valid_fact_ids
    invalid_fact_ids
    expected_state
    reason

The output is private and must remain outside all Git repositories and reviewer-accessible storage.

A private rule trace may be retained as allowed by the addendum.

P1 may append semantic precedents only when a genuinely reusable interpretation is needed. PRECEDENTS.md is append-only.

P1 must not create:

    BIRTH labels
    LEGACY labels
    LEGACY witness/control identities
    BIRTH or LEGACY grouping pairs
    complete canonical Key A bytes
    public commitment material

## 6. Progress semantics

At launch:

    p1_authorized
        true

During P1:

    semantic_labels_created
        becomes true when the first STATE expected output is authored

After successful completion:

    current_phase
        P1_STATE_COMPLETE_AWAITING_REVIEW

P2 must not begin automatically.

The task owner must review P1 before any later semantic phase is authorized.

## 7. Transcript and confidentiality boundary

The P1 Claude Code transcript is Key A private material.

It may remain in normal Claude client storage during Key A execution, but that storage remains within the Key A confidentiality boundary.

Future Key Author B must have no read access to:

    KEYA_WORK
    Key A private archive
    P0 transcript
    P0.5 transcripts
    P1 and later Key A semantic transcripts

## 8. Required return

The P1 executor returns only a bounded phase report to the owner/task owner.

The report may include:

    session ID
    Claude Code version
    model
    effort
    permission mode
    external-terminal / IDE-context status
    number of STATE fixtures completed
    private output path
    whether all schema-required fields are present
    whether a private rule trace exists
    precedent count added
    errata count
    semantic material created = true/false
    P2 started = false

The report must not include:

    fixture-level expected states
    valid/invalid fact IDs
    semantic reasons
    semantic precedents
    excerpts sufficient to reconstruct STATE truth

## 9. Current boundary

    PUBLIC_R2_FREEZE=UNCHANGED
    EXECUTION_ADDENDUM=UNCHANGED

    P0_5=PASS
    PRE_P1_HARDENING=COMPLETE

    P1_READY=true
    P1_AUTHORIZED=true
    P1_SCOPE=STATE_ONLY

    P2_THROUGH_P8_AUTHORIZED=false

    KEY_A_LABELS=NONE_AT_AUTHORIZATION
    KEY_A_PRIVATE_BYTES=NOT_CREATED_AT_AUTHORIZATION

    NEXT=OWNER_LAUNCH_KEY_A_P1_STATE
