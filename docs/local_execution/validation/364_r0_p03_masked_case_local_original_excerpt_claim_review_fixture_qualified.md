# Validation 364: Two frozen answers transformed into one exact-byte case-local masked reviewer input

**Date:** 2026-11-14
**Status:** EIGHT_ANSWERS_FOUR_NEEDS_SOURCE_ONLY_REVIEW_FIXTURE_FROZEN / REVIEW_NOT_YET_RUN / NO_GOLD
**Research:** Research 665. **Checkpoint:** 928.
**Scope:** Freeze and mechanically qualify the actual masked source-conditioned evidence packet before independent reviewer invocation, without changing historical sources or original answer outputs.

## Exact source and output identities

- Original user-defined world: historical Git source pin `47ed6344a9153dcf366769e95722840fbf1a8f8b`.
- Original immutable Message 079 SHA-256 `618767905efe5c3f4ff67088a45b579a41b7b420679e20b7ec5870e6cd501b05`; Message 080 `171a000daa1bd569ecac3cc5227c9239d9b513684b5ce35b04edc2db39584905`.
- Frozen original source-only Packet A V02 SHA-256 `3876a30dabc022c67483ea0de5c3ddfcbb75c43ed054f5e4668345df53fe9a37`; Packet B V02 `a7ec96918330aa75b2ead92fcf6ad60b4324abc9d5f90ed1f82d1422fc6499d0`.
- Review contract SHA-256 `0e832f0d1a87f8f119f7d146f918e669f0942d3db5292d7261dd3be1597d7ac1`.
- Actual eight-answer case-local reviewer fixture `four_need_masked_source_excerpt_claim_review_packet_v01.json`: **234,990 bytes**, SHA-256 `e53544ac31eacaf6fd64e74b67c920d9a2b0ec96bafb1a0951c5fdc43c3453a2`.
- Public source-free lineage manifest `four_need_masked_source_excerpt_claim_review_manifest_v01.json`: **1,446 bytes**, SHA-256 `afd02851a2795be8442b1d8e859fbcf7456c3038256ebb67bddd3306f9fbda62`.
- Source-free next model handoff: MC-0030 Message **081**, **8,692 bytes**, SHA-256 `8290563f2dc2188c7586cb5757e837e0fe7087d63d25fae12b851cd586169dce`.

## What the model-free build verified

The generator `four_need_masked_source_excerpt_claim_review_v01.py` rereads and hash-checks only the four frozen **public** input files, never protected original reference gold or historical Git source bodies. It proves both treatment packets have exactly the same four original question texts; makes exactly two candidate response bodies per question, with **four** sources each; removes **eight** original author self-rating lines; replaces **two** explicit treatment-name mentions; and retains all substantive answer claims/citations, including the already-observed B N03 out-of-case source reference. Original source contexts are **32** and excerpt windows **64**, unchanged and never supplemented.

The deterministic P/Q assignment is **balanced 2/2 per original method**, with no original treatment names or input filenames in the reviewer-facing JSON. The mapping is not cryptographically hidden: the generator code is visible elsewhere, so this is partial masking only. There is no original gold, source relevance gold, private reference label, treatment key, or numerical architecture score in the reviewer packet.

Pre-result dry-run exposed one overly broad masking assertion: the English term `self-description` was legitimately used in an answer as a **substantive description of a document's own claimed status**, not as an author grade. The mask guard was narrowed to reject only original **author verdict lines**, preserving that substantive term. This was corrected **before the first immutable fixture write**, not a post-result output edit. The generator's output overwrite guard was also moved to the actual file-creation entrypoint to allow subsequent byte-exact deterministic replay tests without changing the exclusive-create behavior. No source ranking, answer text, evidence corpus or original author output was altered.

The actual generated packet and manifest are exclusive-create, version V01. Original byte replay and synthetic tests verify per-case exact evidence equality, immutable input hashes, balanced assignments and retention of the known out-of-case N03 mention. Any full semantic claim-support verdict is intentionally **not** asserted at this stage.

## Actual focused tests

A pre-output focused regression suite passed **44/44**. After the frozen packet and manifest were written, a test was added for exact original output replay; **45/45** focused tests passed:

```text
.venv\Scripts\python.exe -m pytest -q -s -p no:cacheprovider --basetemp=.venv/.pytest_r0_p03_masked_v01_frozen tests/unit/test_r0_p03_four_need_masked_source_excerpt_claim_review_v01.py tests/unit/test_r0_p03_four_need_source_only_answer_case_boundary_v01.py tests/unit/test_model_collaboration_state.py tests/unit/test_model_collaboration_message_identity.py
.............................................
45 passed in 0.88s
```

The repository-level integrity and Knowledge Map/checkpoint validators are rerun prior to final publication. If any gate fails, this validation must be amended before claiming a clean commit.

## Scientific and operational limitations

Reviewer will receive the **source-limited** exact original evidence excerpts but not original author self-labels or complete historical reference gold. This controls explicit prompt priming but cannot ensure provider/model independence or OS-level source isolation. The subsequent assessment is **retrospective with respect to original answers**, not an independent scored B0-B4 architecture arm. Neither a support statement from a source nor a correct citation establishes executed CI, accepted owner decision or a full historical absence proof.

The source-free response expected next is MC-0030 Message 082, original one-file local commit, after a new reviewer evaluates all eight answers against the masked fixture and retains complete per-claim details in Git-ignored local storage.

    VERIFIED_ORIGINAL_INPUT_SHA_IDENTITIES=4
    ORIGINAL_FIXED_QUESTION_COUNT=4
    FROZEN_ANSWER_BODY_COUNT=8
    CASE_LOCAL_SOURCE_CONTEXTS=32
    EXACT_REPLAY=PASS
    REVIEWER_OUTPUT=NOT_YET_RECEIVED
    FORMAL_EXPERIMENT_SCORE=NONE
