# Research 418: Key Author A P6B Evidence-Query HOLD and Governed Replacement

**Date:** 2026-10-01
**Status:** P6A PASS/FROZEN / P6B ACCEPTED PREFIX 3 / EVIDENCE-QUERY HOLD / ONE FRESH REPLACEMENT AUTHORIZED
**Parent:** Research 417
**Scope:** Reconcile the qualified P6B prompt-separator remediation with the subsequent live P6B execution boundary, diagnose the new bounded HOLD without inspecting hidden semantic output, and freeze the task-owner disposition before any replacement attempt.
**Authority:** P6B execution/recovery disposition only. This record does not alter candidate-gap values, evidence semantics, evidence horizon, thresholds, grouping semantics, canonical Key A assembly, commitment generation, Key Author B, scoring, successor implementation, migration, oracle retirement, or authority switching.

## 1. The Research 417 prompt-launch defect is no longer the active failure

Research 417 froze the P6B-only invocation remediation:

    --add-dir <fixedEvidenceRoot> -- <prompt>

The private local-runtime repository now preserves that implementation at:

    9e215adcd93572b960a4eb603999243478441ee9
    Fix P6B Claude prompt separation

The corresponding release bundle is:

    p6-private-ops-v5

The live purpose-specific P6 control plane subsequently advanced through P6B semantic execution and accepted three source jobs. That live behavior is direct evidence that the original variadic `--add-dir` prompt-consumption failure no longer prevents P6B semantic launch.

P6A remains PASS/FROZEN and must not be rerun.

## 2. New bounded P6B HOLD

The current private runner state reports:

    subphase = P6B
    status = HOLD
    accepted_sources = 3
    failed_source = LSP-816d7caf56ea
    error_code = P6_GIT_QUERY_FAILED

The accepted prefix is exactly the first three frozen P6B sources:

    LSP-157dfb537436
    LSP-4f1bc6ce3068
    LSP-8b58f8ed9f58

All three have accepted private artifacts and transcript hashes recorded by the bounded runner.

No fourth-source artifact is recorded as accepted.

The task owner has not opened the accepted P6B semantic artifacts, the failed semantic output, or the failed Claude transcript. Hidden semantic details remain unexposed to ChatGPT.

## 3. Bounded mechanical diagnosis

The qualified P6 worker verifies the fixed evidence root once before entering the source loop.

Because the same orchestration successfully accepted the first three P6B sources, that evidence-root preflight necessarily completed before the current fourth-source failure.

Within the source loop, `P6_GIT_QUERY_FAILED` is emitted only by the bounded Git-query helper used while mechanically resolving a semantic author's declarative evidence request against the fixed evidence snapshot.

Therefore the current HOLD is classified narrowly as:

    POST_SEMANTIC_REQUEST_MECHANICAL_EVIDENCE_QUERY_HOLD

It is not classified as a recurrence of the Research 417 Claude prompt-launch defect.

The bounded status does not expose which evidence request failed or the request's semantic contents. The task owner does not inspect that hidden material merely to obtain a more specific explanation.

The exact lower-level Git-query cause is therefore intentionally left unclaimed. It may be an unresolvable declarative request or another query-level failure, but the current bounded evidence does not justify selecting between those possibilities.

## 4. Frozen recovery rule already covers this boundary

Research 410 prospectively requires:

    automatic retry-to-green = prohibited
    HOLD -> stop orchestration
    preserve failed attempt
    require governed disposition
    replacement attempt -> fresh Claude Code process

For P6B evidence requests specifically, a malformed or mechanically unresolvable request rejects the current attempt before freeze and does not authorize task-owner editing.

The qualified `resume_after_hold` operation also verifies the accepted prefix and artifact hashes before it archives the held orchestration and starts a new orchestration UUID.

It preserves the accepted prefix and uses a fresh semantic session for the unfinished source.

## 5. Task-owner disposition

The current held fourth-source attempt receives this governed disposition:

    DISPOSITION = FRESH_REPLACEMENT_ALLOWED
    ACCEPTED_PREFIX = PRESERVE_3
    TASK_OWNER_SEMANTIC_EDITING = PROHIBITED
    AUTOMATIC_RETRY_LOOP = PROHIBITED

Exactly one fresh replacement may now be launched through the bounded:

    resume_after_hold

operation.

The replacement must:

    preserve all three accepted P6B source artifacts byte-for-byte
    archive the held orchestration
    create a new orchestration UUID
    create a fresh Claude Code session for the unfinished source
    use no --resume
    use no --continue
    keep the same frozen evidence horizon
    keep the same P6B semantic/evidence contract
    expose no P6A candidate-gap values

If the fresh replacement reaches another `P6_GIT_QUERY_FAILED` HOLD before the failed source is accepted, execution stops again. A repeated query failure is not automatically retried and must instead trigger a new bounded diagnosis of whether the evidence-query contract or implementation needs prospective remediation.

## 6. Current boundary

    P6A=PASS_FROZEN
    P6B=HOLD
    P6B_ACCEPTED_PREFIX=3
    P6B_FAILED_SOURCE=LSP-816d7caf56ea
    P6B_HOLD_ERROR=P6_GIT_QUERY_FAILED
    P6B_HIDDEN_SEMANTIC_DETAILS_EXPOSED=false
    P6B_HELD_ATTEMPT_DISPOSITION=FRESH_REPLACEMENT_ALLOWED
    P6C=NOT_STARTED
    KEY_A_CANONICAL_ASSEMBLY_AUTHORIZED=false
    KEY_A_COMMITMENT_AUTHORIZED=false
    KEY_AUTHOR_B_AUTHORIZED=false
    NEXT=GOVERNED_RESUME_AFTER_HOLD
