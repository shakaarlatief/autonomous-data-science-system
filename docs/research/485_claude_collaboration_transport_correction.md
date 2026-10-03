# Research 485: Claude collaboration transport correction and D-2 handoff supersession

**Date:** 2026-10-03
**Status:** TRANSPORT CORRECTION / RESEARCH 484 SECTION 5 SUPERSEDED / CLAUDE REMAINS NEXT
**Parent:** Research 348, Research 477, Research 484
**Fixed evidence base:** cd00b8277bd867fbc1331e762dfb7eb05e81d81f
**Scope:** Correct a task-owner routing mistake that incorrectly required the ChatGPT-only Codexless Runtime Bridge inside Claude's separate interaction, and preserve the D-2 blinded evaluator handoff with the correct Claude collaboration write path.
**Authority:** Development-method correction only. This record does not alter D-2 semantics, fixtures, Evaluator A, hidden keys, production selection, migration, Specification 028 authority, or hidden R2 material.

## 1. Correction

Research 484 Section 5 incorrectly stated that Claude must use the Codexless Runtime Bridge.

That is false.

The Codexless Runtime Bridge is a custom ChatGPT-side execution surface built and used in the ChatGPT environment.

Claude has never had that custom Runtime Bridge tool in the separate Claude interaction.

Research 348 itself defines the transition rule as:

    CODEXLESS RUNTIME BRIDGE
        is the single authorized ChatGPT execution surface for ADS repository operations.

The word ChatGPT is material.

Research 348 therefore does not imply that a separate Claude interaction must possess or use the ChatGPT custom Runtime Bridge.

## 2. Claude's collaboration write surface

MC-0029 has long carried an explicit bounded secondary write surface for Claude:

    docs/model_collaboration/threads/MC-0029/messages/**

Claude has used its available GitHub connector to commit those bounded collaboration-message artifacts.

That is the relevant Claude-side transport for this collaboration role.

The transport does not grant Claude generic repository mutation authority.

For D-2, Claude remains limited to exactly:

    docs/model_collaboration/threads/MC-0029/messages/018_claude_d2_lineage_evaluator_b.md

and must not write any other repository file.

## 3. Research 477 correction

Research 477 classified Claude's Message 017 GitHub-connector commit as:

    COLLABORATOR_WRITE_TRANSPORT_NONCONFORMANCE=RECORDED

That classification resulted from the same mistaken assumption that Claude should have used the ChatGPT Runtime Bridge.

That transport-nonconformance classification is now:

    WITHDRAWN_AS_FACTUAL_ERROR

Message 017's one-file GitHub-connector write was consistent with Claude's bounded MC-0029 collaboration write surface.

Research 477's substantive architecture reconciliation remains unchanged.

## 4. Research 484 supersession

Research 484 remains historical evidence of the frozen blinded D-2 handoff, but its Section 5 transport rule is superseded.

Correct transport rule:

    Claude uses the GitHub connector available in the Claude interaction
    only for the explicitly authorized MC-0029 message path.

Claude must still:

    verify routing/head;
    remain blind to evaluator_key.json;
    remain blind to evaluator_chatgpt_a.py;
    remain blind to all D-2 outputs/results;
    write exactly one Message 018 file;
    stop after committing Message 018.

No other D-2 boundary changes.

## 5. Independence remains intact

This correction changes only transport instructions.

It does not expose:

    evaluator_key.json
    evaluator_chatgpt_a.py
    evaluator-A output
    any D-2 result
    hidden R2 item-level material.

Evaluator A remains frozen and unexecuted.

Claude Evaluator B remains independently authored.

## 6. Corrected Claude task

Claude may read:

    docs/current_routing.json
    docs/model_collaboration/REVIEW_INBOX.md
    docs/model_collaboration/threads/MC-0029/STATE.json
    docs/model_collaboration/threads/MC-0029/THREAD.md

and the D-2 reviewer-facing materials:

    docs/research/482_d2_extended_lineage_realization_succession_protocol.md
    experiments/ao10_hybrid_d2_lineage_v01/reviewer_fixtures.json
    experiments/ao10_hybrid_d2_lineage_v01/evaluator_contract.json

Claude may write only:

    docs/model_collaboration/threads/MC-0029/messages/018_claude_d2_lineage_evaluator_b.md

using the GitHub connector available in Claude.

## 7. Current disposition

    RESEARCH484_TRANSPORT_RULE=SUPERSEDED
    RESEARCH477_TRANSPORT_NONCONFORMANCE=WITHDRAWN
    D2_PROTOCOL=UNCHANGED
    EVALUATOR_A=FROZEN_UNEXECUTED
    EVALUATOR_B=CLAUDE_NEXT
    CLAUDE_BLIND_TO_KEY_AND_A=true
    HIDDEN_R2_DETAILS=SEALED

    NEXT=CLAUDE_MESSAGE018_D2_EVALUATOR_B
