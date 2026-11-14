# Validation 362: Four frozen independent needs, two equal-original-source retrieval packets, exact source identity and excerpt provenance

**Date:** 2026-11-14
**Status:** SOURCE_WORLD_2258_BLOBS_ACTUALLY_INDEXED / TWO_SOURCE_PACKETS_CREATED / V02_LINE_CLIPPING_METADATA_CORRECTED / SOURCE_ONLY_ANSWERING_PENDING
**Research:** Research 663. **Checkpoint:** 926.
**Scope:** Record original source-world source identity, actual retrieval method differential, source-only packet integrity, V01/V02 versioned metadata correction and already-run synthetic and original-Git citation tests, with no private answer gold.

## Input and method identity

- Original needs: MC-0030 Message 073 at original commit `881e78d1708a38e4c6cad86336f9eb999ae5dc11`, frozen file SHA-256 `95dec6abdc5ad7ceec435f9cb3b3eb114a4dad8ac75f4865df05ea9509eff5d6`.
- Original Git source pin: `47ed6344a9153dcf366769e95722840fbf1a8f8b`.
- Prospectively authored method: `experiments/r0_p03_navigation_probe/FOUR_NEED_GOLD_FREE_ORIGINAL_SOURCE_NAVIGATION_TRIAL_CONTRACT_V01.md`, SHA-256 `2e7637f174d2b1772737eab896eaefeb306c31eba546785bcb6369b2dba0d09e`.
- Executable V01: `experiments/r0_p03_navigation_probe/four_need_gold_free_original_source_navigation_v01.py`.
- V02 correction executable: `experiments/r0_p03_navigation_probe/four_need_gold_free_packet_clipping_correction_v02.py`.
- Eligible common candidate world: exact `git ls-tree` path/type filter, **2,258 Git source blobs**, **18,106,101** raw original source bytes, blob object digest checks. Original corpus presence does not imply relevance-gold closure.
- Retrieval: `BODY_FTS5_BM25` and `BODY_PLUS_HEADINGS_RRF_DIAGNOSTIC` using same document texts capped 12,000 indexed characters, four documents per question and same excerpt budget. Headings are native source text; diagnostic is **not official subject-based B1**.
- Gold exclusion: no private source report, original expected source/line labels, prior model answer or metadata target mapping entered the input corpus, query, rankers or source-only packet.

## Actual first execution, preserved versions

| Artifact | Original byte length | SHA-256 |
| --- | ---: | --- |
| V01 Packet A | 92,553 | `0c7b39ecba5524c96d96426303e29c362b09c070fa24c14aa2d6c8b4a080be10` |
| V01 Packet B | 91,532 | `60bcdf530b98377f2faa7749ac904f0f1a0f9d00590f32cd1b38a03af0375ac5` |
| V01 aggregate | Exact retained | `6f35585e5b2ba71e6b20c72f6932ac2291c2365b51c3820b9ea1cc74bbae56bb` |
| V02 Packet A | 92,552 | `3876a30dabc022c67483ea0de5c3ddfcbb75c43ed054f5e4668345df53fe9a37` |
| V02 Packet B | 91,531 | `a7ec96918330aa75b2ead92fcf6ad60b4324abc9d5f90ed1f82d1422fc6499d0` |
| V02 correction receipt | Exact retained | `b8f0b7f3a5725fa400334f7b8caa0413b38deb5d4a352c59ac0b6080ec298906` |

Top-four overlap counts **[2, 2, 2, 3]** across N01-N04. All 32 source contexts across 23 unique original Git blobs were checked by exact original `git rev-parse <pin>:<path>` and `git cat-file blob <OID>` source bytes. For all displayed excerpt lines, the recorded 1-based original line was in bounds and the text matched its original line prefix; **two false line clipping flags** in original V01 were found, not hidden. Original V01 exact packets were retained and a separate V02 **only flips one `line_clipped` boolean in each packet**, leaving the rest byte-equivalent after removal of that field. All V02 excerpts' clipping flags were rechecked against full historical Git lines. Both packets still contain no answer truth, relevance-gold selection or treatment label.

## Tests actually executed

The full selected source-evidence/test collection used the repository-managed virtual environment with no pytest cache and a dedicated local basetemp:

```text
.venv\Scripts\python.exe -m pytest -q -s -p no:cacheprovider --basetemp=.venv/.pytest_r0_p03_077_nav_combined tests/unit/test_r0_p03_four_need_gold_free_original_source_navigation_v01.py tests/unit/test_r0_p03_four_need_source_packet_clipping_correction_v02.py tests/unit/test_r0_p03_four_need_gold_free_packet_v02_integrity.py tests/unit/test_r0_p03_fresh_reference_private_citation_audit_v01.py tests/unit/test_r0_p03_fresh_reference_private_citation_audit_v02.py tests/unit/test_r0_p03_fresh_reference_need_index_pilot_v01.py tests/unit/test_model_collaboration_state.py tests/unit/test_model_collaboration_message_identity.py
.............................................................................................
93 passed in 5.11s
```

The two retained V01/V02 citation-audit versions and their public aggregate source-integrity receipts from Checkpoint 925 were not modified by this trial. Neither the prior 84,359-byte local-only original reference report nor the 27,210-byte private literal-attribution review was opened for the retrieval trial.

## Original Message 077 verification

- Claude literal-fidelity Message 077 commit `7e73de03db2b2308cd6366245c35b3ed1ee59196`, parent `a2ea89711ff316f965d234cb9cf483c8fac9c05f`, sole path added.
- Exact public 10,234-byte source-free report SHA-256 `b3eae816f34a6b3a8ebbc3000ba32ba2c12f89c7374914f32d08686e3133ba89`.
- Ignored local-only private review report independent metadata check: file exists, 27,210 bytes, SHA-256 `3a0e867dfd78c9008418a13eaec708a9f2f738a111ddac143f070cc88307c80f`. Exposed coordinator has not read private review content.
- Reviewer outcome: 11 abbreviated/format variants, one misplaced line, zero flagged unsupported/UNRESOLVED, with four secondary cautions and two interpretive claims. Does not prove full report truth or remove original V02 discrepancy counts.

## Scientific limits and remaining work

The actual outputs are **source-only answer contexts**, not natural-language answers, test scores, treatment-grade ranking metrics, original-source relevance closure, blinded gold or formal R0-P03. The next actual work is the two separately sessioned answer authors, Session A then B, following Message 078 and the frozen Packet A/B V02 hashes. Qualification of their claim/line support, source-only accuracy, proper abstention and side-by-side limitations comes **after** both outputs are frozen. Neither source-corpus scope nor the cheap heading diagnostic should be relabelled a fully governed V03/B1 source-owner implementation.

The public aggregate repository-integrity gate must pass before final fast-forward publication.

    PUBLIC_QUESTION_AND_CORPUS_FROZEN=true
    SOURCE_FILE_COUNT=2258
    SOURCE_RAW_BYTES=18106101
    NUMBER_OF_SOURCE_PACKET_CONTEXTS=32
    UNIQUE_HISTORICAL_SOURCE_CONTEXTS=23
    V02_METADATA_ONLY_FLAGS_CORRECTED=2
    ANSWERER_A=NOT_STARTED
    ANSWERER_B=NOT_STARTED
    FORMAL_R0_P03_SCORE=NONE
