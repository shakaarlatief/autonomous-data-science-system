# Research 335: DRP-03 R2 Key Author A P0 Preflight Reconciliation

**Date:** 2026-09-26
**Status:** P0 SUBSTANTIVELY PASSED / FOUR PRE-P1 HARDENING ITEMS RESOLVED BY TASK-OWNER DECISION / P0.5 REMEDIATION NEXT / NO SEMANTIC LABELS
**Parent:** Research 334 / local Claude Code P0 report
**Scope:** Reconcile the non-semantic local Claude Code P0 report, independently verify repository-side claims that can be checked from ADS, resolve the four reported blockers before semantic key authoring, and route to a bounded P0.5 hardening step.
**Authority:** Operational key-author execution control only. The Research 332 public protocol freeze and Research 334 execution addendum remain unchanged.

## 1. P0 disposition

The local Claude Code P0 report states PASS for requirements 1 through 13 and explicitly states that no semantic Key A material was created.

Executor-reported P0 facts include:

    Claude Code version
        2.1.283

    model observed
        claude-opus-5-5

    P0 effort
        medium from environment

    P0 session
        622a692e-b9e9-4565-9e40-a0f3ba561848

    P0 permission mode
        auto

    permission-config SHA-256
        8579fdb498a7d8a80b33025aa13d0a6a200e78881fd4e4fc7979e267a1d61eb6

    key-author packet manifest SHA-256
        406c0f70df9cf65f8262b94f6d48c3ce82b523e41e552f2bd5aa990c7dd37448

    semantic labels
        NONE

    private Key A bytes
        NONE

    STATE expected outputs
        NONE

    LEGACY witness/control identities
        NONE

    grouping pairs
        NONE

The executor also reports that the frozen public export, addendum, isolated workspace, read-only LEGACY evidence horizon and no-network/no-connector boundary passed.

Those local-environment claims are accepted as P0 executor evidence, not independently reproduced by ChatGPT.

## 2. Independent repository-side checks

ChatGPT independently verified:

    ADS HEAD
        68a1849c4366412ae1e94ac54d247571f7f84b47

    upstream branch HEAD
        68a1849c4366412ae1e94ac54d247571f7f84b47

    working tree
        clean

    current checkpoint before this reconciliation
        671

    current boundary
        obligation-rerun-private-key-author-a-local-preflight-boundary

The frozen public manifest explicitly binds Research 330:

    path
        docs/research/330_mc0029_message009_reconciliation_v07_and_drp03_r2_protocol_v03_freeze_candidate.md

    SHA-256
        8e191d81d15da3254466194f874223aebb377306056619f47778565ae286a8fa

    bytes
        28175

Therefore exporting that exact bound blob into the private semantic workspace does not introduce post-freeze or non-frozen protocol material.

## 3. Blocker 1: semantic effort level

Decision:

    KEY_A_MODEL
        claude-opus-5-5

    KEY_A_SEMANTIC_EFFORT
        HIGH

The P0 session's medium effort occurred before semantic labels existed and does not contaminate the key.

Before P1, a new plain-terminal Claude Code session must expose and verify:

    model = claude-opus-5-5
    effort = high

Those values become fixed semantic-execution configuration for Key Author A.

If either cannot be positively verified before the first semantic judgment:

    STOP

If either changes after semantic labeling begins:

    STOP
    task-owner review required

## 4. Blocker 2: Research 330 export

Decision:

    EXPORT RESEARCH 330 EXACTLY

Reason:

    it is already an external binding of the frozen Research 332 public manifest

    its exact hash and byte length are frozen

    the execution addendum refers to Research 330 for batching, replacement semantics and allowed evidence forms

The private export must be exact raw Git blob bytes and must verify:

    SHA-256
        8e191d81d15da3254466194f874223aebb377306056619f47778565ae286a8fa

    bytes
        28175

Do not export MC-0029 Messages 006 through 009.

Do not export unrelated repository history.

Research 331 is not required for P1 and is not added merely because it is also an external public-freeze binding.

## 5. Blocker 3: P1 launch environment and permission mode

P1 must start in a NEW Claude Code session from the private workspace root.

Before launch:

    close VS Code and other Claude-Code-capable IDE integrations

    launch from a plain PowerShell terminal

The executor must positively report:

    IDE connector
        DISCONNECTED

    web / MCP / GitHub connectors
        DISABLED / DENIED

For semantic phases, the permission mode is:

    INTERACTIVE_APPROVAL

Meaning:

    do not use auto/bypass-style autonomous permission escalation

    use the product's current manual/default approval mode that requires owner approval for non-preapproved shell/tool actions

    record the exact Claude Code mode string exposed by the installed version

The task owner does not rely on the Windows path-deny rules as a shell sandbox.

P1 STATE needs no shell command for semantic derivation.

The P1 prompt therefore forbids shell use during semantic STATE derivation.

Later phases that require deterministic local Git queries must use separately approved read-only commands and remain inside the frozen LEGACY evidence horizon.

The same model/effort/codebook/addendum/frozen inputs remain fixed across phases.

## 6. Blocker 4: transcript containment

Claude Code transcript material is private key-author material even when stored by the client outside KEYA_WORK.

Before P1:

    locate the exact P0 transcript by P0 session ID

    copy it into a private transcripts/ directory under KEYA_WORK

    hash the exact copied bytes

    record the path/hash in private provenance

The original Claude client transcript may remain in its normal local storage during Key A execution, but that location becomes part of the Key A confidentiality boundary.

Future Key Author B must not run in an environment that can read:

    KEYA_WORK
    its private archive
    Key A Claude Code transcript storage

A separate Windows/OS user profile is the preferred later mechanism for Key Author B because it provides a clearer boundary.

Equivalent isolation may be used only if independently verified before Key B begins.

## 7. Windows shell boundary

P0 correctly reported that Windows provides no shell sandbox equivalent to the file-tool path denies.

Therefore:

    file-tool deny rules
        useful but not sufficient

    shell
        governed by interactive owner approval plus phase-specific prompt prohibition/allowlist

For P1 STATE:

    shell use = PROHIBITED

For later LEGACY evidence work:

    only read-only Git/search commands within the frozen LEGACY_SEARCH repository may be approved

    git commit / push / fetch / pull / clone / remote mutation / hooks bypass for mutation
        PROHIBITED

The fact that local Git hooks can be bypassed with --no-verify is therefore treated as evidence that hooks are defense-in-depth only, never the authority boundary.

## 8. P0.5 remediation gate

Before P1 semantic work, P0.5 must demonstrate:

    Research 330 exact export PASS

    P0 transcript copied and hashed PASS

    plain-terminal launch PASS

    IDE disconnected PASS

    model claude-opus-5-5 verified PASS

    effort high verified PASS

    exact interactive/manual permission mode recorded PASS

    prior deny configuration still effective PASS

    no semantic labels created PASS

P0.5 is non-semantic.

It must not create STATE outputs, BIRTH/LEGACY labels, witness identities, grouping pairs or key bytes.

## 9. Current boundary

    PUBLIC_R2_FREEZE=UNCHANGED
    EXECUTION_ADDENDUM=UNCHANGED

    P0=PASS_WITH_REMEDIATION
    P0_SEMANTIC_CONTAMINATION=NONE

    KEY_A_MODEL=claude-opus-5-5
    KEY_A_EFFORT=HIGH
    KEY_A_PERMISSION_CLASS=INTERACTIVE_APPROVAL

    RESEARCH330_EXPORT=AUTHORIZED_EXACT_FROZEN_BLOB
    KEY_A_TRANSCRIPT_BOUNDARY=EXPANDED_TO_CLIENT_TRANSCRIPT_STORAGE

    KEY_A_LABELS=NONE
    KEY_A_PRIVATE_BYTES=NOT_CREATED

    NEXT=P0.5_HARDENING_AND_CONFIGURATION_VERIFICATION
