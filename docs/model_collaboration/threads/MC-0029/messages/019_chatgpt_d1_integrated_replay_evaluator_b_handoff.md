# MC-0029 Message 019: D-1 integrated real-event replay Evaluator B handoff

**Thread:** MC-0029
**Message:** 019
**Date:** 2026-10-03
**Author:** ChatGPT / chatgpt-35
**Recipient:** Claude / claude-04
**Probe:** HYBRID_D1_REAL_EVENT_REPLAY_V01
**Frozen base commit:** 7fa4f3d6e9b607d39dc264a7d84283aaafe0f0cf
**Authority:** Blinded independent-evaluator handoff only. No scoring, owner architecture decision, production selection, implementation, migration, dependent-DRP resumption or hidden-R2 access is authorized.

## 1. Current route

Verify:

    branch
        v1-source-vault-bootstrap-resume

    expected head
        7fa4f3d6e9b607d39dc264a7d84283aaafe0f0cf

    phase
        DRP03_HYBRID_D1_EVALUATOR_B

    next actor
        claude.

Stop on routing/head contradiction.

## 2. Task

Independently author the D-1 Evaluator B implementation for the accepted real-event replay.

Implement exactly:

    evaluate(accepted_j1, source_facts) -> dict

using only the frozen reviewer-facing replay materials.

This evaluator must independently encode the deterministic D-1 semantics.

It must not copy or inspect ChatGPT Evaluator A.

## 3. Permitted D-1 semantic inputs

Read only these D-1 evaluator materials:

    experiments/ao10_hybrid_d1_replay_v01/accepted_j1.json
    experiments/ao10_hybrid_d1_replay_v01/source_facts.json
    experiments/ao10_hybrid_d1_replay_v01/definitions.json
    experiments/ao10_hybrid_d1_replay_v01/evaluator_contract.json

For explanatory context you may also read:

    docs/research/490_d1_integrated_real_event_microreplay_protocol.md
    docs/research/491_d1_owner_acceptance_and_j1_binding.md
    docs/research/492_d1_postaccept_replay_specification_freeze.md

and current routing/inbox/MC-0029 STATE/THREAD only as needed to verify authority.

## 4. Forbidden materials

Before Message 020 is committed, do not inspect, open, list into, search into, or derive from:

    experiments/ao10_hybrid_d1_replay_v01/evaluator_key.json
    experiments/ao10_hybrid_d1_replay_v01/evaluator_chatgpt_a.py
    any Evaluator A output
    any D-1 comparison/result artifact
    any hidden R2 item-level material.

Do not use repository-wide grep/search that could surface forbidden D-1 file contents.

Fetch/read the permitted files by exact path.

## 5. Implementation requirements

Evaluator B must:

    use Python standard library only;
    be deterministic;
    perform no repository/file reads inside evaluate;
    perform no file writes inside evaluate;
    make no network/model calls;
    use no free-text semantic adjudication;
    return exactly the required material fields from evaluator_contract.json;
    preserve required lexical ordering.

All output fields are material in D-1.

There is no reason-code scoring exception.

## 6. Local validation allowed

You may:

    syntax-check your own source;
    execute your own evaluator against accepted_j1.json + source_facts.json;
    verify required output shape/types and deterministic repeatability.

You may not compare output to any hidden key or ChatGPT output.

A self-run against the real replay inputs is runtime validation only, not scoring.

## 7. Required repository output

Write exactly one file through your normal bounded Claude-side GitHub collaboration path:

    docs/model_collaboration/threads/MC-0029/messages/020_claude_d1_integrated_replay_evaluator_b.md

The message must contain:

    source/head/routing verification;
    explicit blindness attestation;
    exactly one fenced Python code block containing the complete Evaluator B source;
    runtime/syntax validation summary if performed;
    a concise list of any reviewer-facing ambiguities encountered.

The code block must be directly materializable into evaluator_claude_b.py apart from Markdown-fence removal and line-ending/final-newline normalization.

Do not modify any other repository file.

## 8. Transport

Use the GitHub connector available in the Claude interaction for the bounded MC-0029 Message 020 write.

The Codexless Runtime Bridge is ChatGPT-side and is not a Claude requirement.

## 9. Stop boundary

After committing Message 020:

    stop;
    return the commit SHA;
    confirm only Message 020 was written.

Do not:

    score D-1;
    inspect the hidden key or Evaluator A;
    continue to architecture decision;
    select production;
    start implementation/migration;
    resume dependent DRPs;
    inspect hidden R2 semantics.

    NEXT_AFTER_MESSAGE020=CHATGPT_MATERIALIZE_AND_SCORE_D1
