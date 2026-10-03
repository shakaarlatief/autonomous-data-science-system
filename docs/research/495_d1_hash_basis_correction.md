# Research 495: D-1 freeze digest hash-basis correction

**Date:** 2026-10-03
**Status:** HASH-BASIS CORRECTION / D-1 CONTENT FREEZE UNCHANGED
**Parent:** Research 492 / MC-0029 Message 020
**Probe ID:** HYBRID_D1_REAL_EVENT_REPLAY_V01
**Scope:** Correct the byte-basis description of the D-1 frozen artifact digests before ChatGPT materializes or executes Claude Evaluator B.
**Authority:** Development-integrity correction only. No semantic content, fixture, key, evaluator, threshold, or scoring rule is changed.

## 1. Finding

Claude independently observed before D-1 scoring that the SHA-256 values recorded in Research 492 Section 1 were computed over the Windows working-tree representation with CRLF line endings rather than the repository's committed Git-blob bytes.

The file contents are semantically and textually unchanged.

The defect is the hash basis, not content drift.

## 2. Correct committed-byte digests

For the frozen commit containing the D-1 replay specification, the authoritative reproducibility basis is:

    GIT_BLOB_BYTES_AT_COMMIT

The corrected SHA-256 values are:

    accepted_j1.json
        cffbeffc45e0adeda0adbb6b240b4b9968f461f3af4ce3f89af716776742ebe4

    source_facts.json
        3b5ceaa50765297c34d8d1cfa2f6230ba1d3263f457aa3f6f71dd51f39b6ded3

    definitions.json
        b1852c008fe9f61026cc44b24e5f936c8ec22d129989cb09019ae004805d98ac

    evaluator_contract.json
        01acbd0a3d4e9f497cf27bba6472a4265e1fe585aa9ca04122da8a38efa5cccf

    evaluator_key.json
        f555dbc603294f3a618a38cb2f6c1f5e11f0cd6f2406c688e620888028cc23a8

## 3. Research 492 interpretation

Research 492 remains the semantic/specification freeze.

Its Section 1 digest strings are superseded only as byte-basis identifiers.

They must not be used as committed-artifact checksums.

All semantic statements, source facts, definitions, output contract, and evaluator key remain exactly the same committed blobs.

## 4. Prospective integrity rule

For repository-tracked artifact freezes, SHA-256 must henceforth state its basis explicitly.

Default basis:

    GIT_BLOB_BYTES_AT_COMMIT

Working-tree-byte hashes may be recorded only when explicitly labeled:

    WORKTREE_BYTES

and must not be used interchangeably with Git-blob hashes.

This prevents line-ending normalization from appearing as false content drift.

## 5. Scoring integrity

At this correction point:

    ChatGPT Evaluator A remains frozen and unexecuted;
    Claude Evaluator B source exists only in Message 020 and has not been materialized/executed by ChatGPT;
    no D-1 comparison result exists;
    the hidden key is unchanged;
    no semantic expectation is changed.

Therefore the correction is prospective with respect to D-1 execution and scoring.

## 6. Current boundary

    HASH_BASIS=GIT_BLOB_BYTES_AT_COMMIT
    D1_SPEC_CONTENT=UNCHANGED
    D1_KEY=UNCHANGED
    EVALUATOR_A=FROZEN_UNEXECUTED
    EVALUATOR_B=CLAUDE_AUTHORED_NOT_YET_MATERIALIZED_BY_CHATGPT
    D1_RESULT_EXISTS=false

    NEXT=MATERIALIZE_AND_FREEZE_D1_CLAUDE_EVALUATOR_B
