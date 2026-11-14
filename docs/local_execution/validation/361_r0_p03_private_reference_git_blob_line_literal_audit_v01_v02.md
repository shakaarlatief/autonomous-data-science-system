# Validation 361: Frozen private report identity, original Git blob and line replay, transparent V01/V02 correction

**Date:** 2026-11-14
**Status:** HISTORICAL_BLOB_IDS_52_OF_52_MATCH / LINE_RANGES_52_OF_52_VALID / EXACT_QUOTE_MATCHES_40_OF_52 / TWELVE_LITERAL_GAPS / FORMAL_R0_P03_UNSCORED
**Research:** Research 662. **Checkpoint:** 925.
**Scope:** Record actual original-source mechanical citation audit runs, immutable outputs, source-content non-disclosure, synthetic regressions and explicit limits. This is **not** independent semantic answer truth verification.

## Evidence input and read boundary

- Frozen local-only reviewer report: **84,359 bytes**, SHA-256 `cce0c99e2c6b019b3e8f67ea960e92c2108b8ff673b685b2865de6977d06dc0b`, hash recomputed by isolated model-free Python process before analysis. Original report bytes never edited.
- Original historical source tree: `47ed6344a9153dcf366769e95722840fbf1a8f8b` (confirmed original commit); each explicit witness's path and SHA-1 checked with `git rev-parse <PIN>:path`; source content loaded by `git show <PIN>:path`, never current branch-head content.
- Public audit runner V01: `experiments/r0_p03_navigation_probe/fresh_reference_private_citation_audit_v01.py`.
- Public audit runner V02: `experiments/r0_p03_navigation_probe/fresh_reference_private_citation_audit_v02.py`.
- The exposed coordinator's tool responses were **aggregate-only**. Case-to-source mappings, 52 explicit witness paths, excerpts, source lines and individual failure locations are not in public results or model-visible tool output.

## Distinct outcomes

| Metric | First frozen V01 | Corrected V02 |
| --- | ---: | ---: |
| Explicit original reference rows | 52 | 52 |
| Original Git blob identity valid | 48 | **52** |
| Source-line range valid | 48 | **52** |
| Source read blocked by audit's excessive prefix filter | 4 | 0 |
| Exact cited-line quote | 36 | **40** |
| Literal quote found elsewhere in same Git blob | 1 | **1** |
| No verbatim match anywhere in source blob | 11 | **11** |
| Incidental non-citation cell classified unparsed | 1 | **0** |
| Distinct original source paths opened | 42 | **46** |

The V01 directory restriction was discovered from actual V01 output, preserved as a first-run implementation defect, and removed only in a separately versioned V02. The V02 algorithm remains deliberately conservative on quotation, not a fuzzy quote-repairer.

Immutable output identity:

- V01 public **1,664 bytes**, SHA-256 `916103b959810258a663390a77ab020a13ba2868efcda8e6bd92812b83f758ab`; V01 private detailed **15,101 bytes**, SHA-256 `9310b16ca62fdaed688bd2fd8d63897a7b7c96cc0d85ab5f97dc5edd8d68933b`.
- V02 public **1,623 bytes**, SHA-256 `51ac418bca0c895a861dd4724810ed86e933fd2328bf2db10a4dfec1c674db49`; V02 private detailed **15,069 bytes**, SHA-256 `4852b554d3f9c2389d2eef2242bde32f1999b52cac80dca47a260b1e51ac8f6a`.
- Both versions' exact public AND private outputs were recomputed by model-free Python builder calls and byte-for-byte matched previously saved first-run results. No actual original Git witness paths or source-blob identities appeared in the V02 public aggregate; that was tested programmatically without serializing those values.

## Public synthetic test executions

The actual focused suite:

```text
.venv\Scripts\python.exe -m pytest -q -s -p no:cacheprovider --basetemp=.venv/.pytest_r0_p03_citation_v02 tests/unit/test_r0_p03_fresh_reference_private_citation_audit_v01.py tests/unit/test_r0_p03_fresh_reference_private_citation_audit_v02.py tests/unit/test_r0_p03_fresh_reference_need_index_pilot_v01.py tests/unit/test_model_collaboration_state.py tests/unit/test_model_collaboration_message_identity.py
................................................................................
80 passed in 1.02s
```

The first V01 synthetic run exposed a **test-only Windows path-separator assumption** (66 passing, one failing); the test alone was corrected to assert path components, and the same first V01 audit algorithm was left unchanged. The subsequently executed suite above includes the V02 correction's synthetic negative controls. No personal or case-specific data was embedded in tests.

## Explicit scientific boundary

- 52/52 historical source identity matches do not establish that assertions in those sources are true or operative.
- 52/52 valid line pointers do not establish that cited passages support the associated claims.
- 40/52 literal quote matches do **not** validate all quotations: the remaining twelve require separate review.
- Excerpts that appear elsewhere in the same blob may be mispositioned; excerpts absent verbatim may be paraphrases or real attribution errors. None is automatically repaired or scored as false.
- The audit checks explicit table witnesses only; uncited narrative, reviewer whole-answer judgments and historical owner/CI execution are not independently audited.
- Git-ignored local-only storage and independent deterministic replay do not establish secret-scored-gold custody or genuine OS/principal separation.
- Original Research 513/559/576 and C01/C02 holds unchanged; no B0-B4 model score, physical architecture selection or authority switch.

    PRIVATE_INPUT_SHA256_VERIFIED=true
    ORIGINAL_GIT_BLOB_ID_VERIFIED=52_OF_52
    ORIGINAL_LINE_RANGE_VALID=52_OF_52
    EXACT_LITERAL_CITED_LINE_MATCH=40_OF_52
    OUTSTANDING_LITERAL_QUOTE_REVIEW=12
    EXACT_PUBLIC_REPLAY=PASS
    EXACT_PRIVATE_REPLAY=PASS
    PUBLIC_LEAK_TEST=PASS
    INDEPENDENT_SEMANTIC_REFERENCE_GOLD=false
    FORMAL_R0_P03_RESULT=INCOMPLETE
