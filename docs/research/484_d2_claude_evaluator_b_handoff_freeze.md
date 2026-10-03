# Research 484: D-2 Claude evaluator B blinded handoff freeze

**Date:** 2026-10-03
**Status:** BLINDED HANDOFF FROZEN / CLAUDE NEXT
**Parent:** Research 482-483
**Fixed evidence base:** 03ce1624024477095fdb862db9b762b67870d39d
**Probe ID:** HYBRID_D2_LINEAGE_EXTENSION_V01
**Scope:** Freeze the exact independent-author handoff for Claude Evaluator B after ChatGPT Evaluator A is immutable and unexecuted.
**Authority:** Collaboration handoff only. No evaluator comparison, D-2 result, production selection, migration, dependent-DRP resumption, or hidden-R2 exposure is authorized.

## 1. Reviewer-facing inputs

Claude may read only the following D-2 semantic/evaluator materials:

    docs/research/482_d2_extended_lineage_realization_succession_protocol.md
    experiments/ao10_hybrid_d2_lineage_v01/reviewer_fixtures.json
    experiments/ao10_hybrid_d2_lineage_v01/evaluator_contract.json

Claude may also read:

    docs/current_routing.json
    docs/model_collaboration/REVIEW_INBOX.md
    docs/model_collaboration/threads/MC-0029/STATE.json
    docs/model_collaboration/threads/MC-0029/THREAD.md

only as needed to verify routing and collaboration authority.

## 2. Blinded materials

Before Message 018 is committed, Claude must not read or derive from:

    experiments/ao10_hybrid_d2_lineage_v01/evaluator_key.json
    experiments/ao10_hybrid_d2_lineage_v01/evaluator_chatgpt_a.py
    any evaluator-A output
    any future D-2 comparison/result artifact
    any hidden R2 item-level material.

The existence/hash of Evaluator A is routing provenance only and conveys no implementation semantics.

## 3. Required task

Independently author a Python evaluator implementing exactly:

    evaluate_fixture(fixture) -> dict

under Research 482 and evaluator_contract.json.

Requirements:

    Python standard library only;
    no repository/file reads inside evaluate_fixture;
    no file writes;
    no network;
    no model calls;
    deterministic output;
    no free-text semantic adjudication;
    output fields and ordering exactly match evaluator_contract.json.

Claude may syntax-check and may execute its own evaluator against reviewer_fixtures.json to catch runtime errors.

Claude may not compare its output to any hidden key or ChatGPT output.

## 4. Required output

Write exactly:

    docs/model_collaboration/threads/MC-0029/messages/018_claude_d2_lineage_evaluator_b.md

The message must include:

    source/head verification;
    explicit attestation that blinded materials were not inspected;
    one and only one fenced Python code block containing the complete Evaluator B source;
    a short note on any ambiguity encountered in the reviewer-facing specification.

The code block must be directly materializable byte-for-byte into:

    evaluator_claude_b.py

apart from line-ending normalization and removal of the Markdown fence itself.

Do not write any other repository file.

## 5. Transport rule

Use the purpose-specific Codexless Runtime Bridge governed write/commit path.

If that path is unavailable in the Claude interaction:

    do not substitute a generic GitHub connector;
    do not mutate the repository;
    report the unavailable governed path and stop.

## 6. Stop boundary

Do not:

    inspect Evaluator A;
    inspect the evaluator key;
    score D-2;
    continue to D-1;
    make an owner architecture decision;
    select production;
    start implementation/migration;
    inspect hidden R2 semantics.

After committing Message 018:

    stop
    return the commit SHA.

## 7. Current disposition

    EVALUATOR_A=FROZEN_UNEXECUTED
    EVALUATOR_B=CLAUDE_NEXT
    D2_RESULT_EXISTS=false
    CLAUDE_BLIND_TO_KEY_AND_A=true
    HIDDEN_R2_DETAILS=SEALED

    NEXT=CLAUDE_MESSAGE018_D2_EVALUATOR_B
