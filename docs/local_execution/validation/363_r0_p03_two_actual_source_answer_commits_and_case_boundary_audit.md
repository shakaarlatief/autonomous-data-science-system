# Validation 363: Two original source-only answer commits, correct duplicate-author HOLD and case-local evidence audit

**Date:** 2026-11-14
**Status:** MESSAGES_079_080_ORIGINAL_ONE_FILE_COMMITS_VERIFIED / ONE_B_N03_CROSS_CASE_SOURCE_REFERENCE / ACTUAL_SOURCE_ANSWER_PILOT_UNSCORED
**Research:** Research 664. **Checkpoint:** 927.
**Scope:** Record exact actual first-published answer provenance, frozen packet identity, model self-outcomes and independently executed structural source-to-case membership checks, without accessing original private reference truth.

## Frozen original answer and packet identity

| Item | Actual identity |
| --- | --- |
| Original A answer Message 079 | `d521fefc53375bbbc29b184b7ab56cef576d90ea`, parent `e403a0cdb5de0747eface94c4b998c53ae66cdc4`, one added file, 24,225 bytes, SHA-256 `618767905efe5c3f4ff67088a45b579a41b7b420679e20b7ec5870e6cd501b05` |
| Original B answer Message 080 | `193cd6d56d24b2facdc8efb11b536e22051f71a7`, parent `d521fefc53375bbbc29b184b7ab56cef576d90ea`, one added file, 24,928 bytes, SHA-256 `171a000daa1bd569ecac3cc5227c9239d9b513684b5ce35b04edc2db39584905` |
| Frozen A original source-only packet V02 | 92,552 bytes, SHA-256 `3876a30dabc022c67483ea0de5c3ddfcbb75c43ed054f5e4668345df53fe9a37` |
| Frozen B original source-only packet V02 | 91,531 bytes, SHA-256 `a7ec96918330aa75b2ead92fcf6ad60b4324abc9d5f90ed1f82d1422fc6499d0` |

Original parent and one-added-file properties were independently read from Git, not inferred solely from model relay. Original B author explicitly reported starting at `d521fefc...` and creating a new Message 080. The later, additional owner-started B session halted at existing HEAD `193cd6d5...` and refused to overwrite Message 080. It produced no new answer or commit. The original Message 080 was retained.

The original answer author self-dispositions were **A: 0 full, 3 partial, 1 abstention (N01)**; **B: 0 full, 4 partial, 0 abstentions**. These are not independent answer-quality scores. Both models used the same provider and family, and their handoff exposed earlier reviewer disposition labels; OS-level access segregation is not verified.

## Mechanically verified case-local evidence boundaries

The new `experiments/r0_p03_navigation_probe/four_need_source_only_answer_case_boundary_audit_v01.py` script reads only the four hash-verified public input files (Messages 079/080 and packets A/B V02). It parses the original four question sections, identifies all fully specified source path@blob IDs, and checks actual question-assigned packet source membership. No private original-source reference report, original Git blob body, hidden need gold or prior answer comparison enters the algorithm.

| Count | A | B |
| --- | ---: | ---: |
| Full source references | 16 | 17 |
| In assigned case | 16 | 16 |
| From another case in assigned packet | 0 | **1 (N03)** |
| Outside entire packet | 0 | 0 |
| `same@blob` shorthand | 27 | 0 |

First execution of the source-free audit produced **4,404 bytes**, SHA-256 `975cba9fddbfcf74925fe33853955264ce358ba62467344af0c9e688d00352ad`. The B N03 cross-case item is an observed violation of the already-frozen per-question source-use restriction, not a claim-false verdict. The source-only answers and packet bytes were not rewritten or regraded.

The initial synthetic-only unit run exposed a *test assertion* that omitted a leading newline in its expected Markdown section slice. The **test-only** expectation was corrected; the audit's source-membership algorithm was not changed. The second focused regression run passed **40/40** with source-boundary negative controls. The larger repository integrity and final regression are independently performed before publication.

## Scientific and custody limits

The audit verifies exact original packet membership of explicit source IDs. It does **not** resolve alias/shorthand references, check each claimed line number, independently judge answer entailment, authenticate owner acts or historical CI execution, or score whole-case completeness. The previous 52 original reference citations and private literal-fidelity review remain separated and unchanged. A cross-case citation is not exposure to the other retrieval treatment; it is an internal case-boundary failure. Both treatments remain cheap unscored diagnostics rather than official fully governed knowledge substrates.

The presence of all four Packet B self-described partial answers does not imply four valid comparable answers; B N03 contains out-of-case evidence and must be qualified. A and B may be compared descriptively where their evidence constraints were respected, especially N01's abstain versus partial distinction, but neither gets a formal Research 513 score.

    ORIGINAL_B_AUTHORED_BEFORE_LATER_HOLD=true
    ORIGINAL_A_MESSAGE_UNCHANGED=true
    ORIGINAL_B_MESSAGE_UNCHANGED=true
    A_FULL_REFERENCES_CASE_LOCAL=16_OF_16
    B_FULL_REFERENCES_CASE_LOCAL=16_OF_17
    B_N03_CROSS_CASE_BREACH=true
    CURRENT_FORMAL_R0_P03_RESULT=INCOMPLETE
