# Research 662: R0-P03 local reference citation replay, original Git identity and unresolved literal attribution

**Date:** 2026-11-14
**Status:** BOUNDED_MECHANICAL_CITATION_AUDIT_COMPLETE / ALL_EXPLICIT_BLOB_AND_LINE_REFERENCES_VALID / TWELVE_LITERAL_ATTRIBUTION_GAPS / INDEPENDENT_CLAIM_TRUTH_NOT_ESTABLISHED
**Scope:** Independently reproduce source and citation coordinates from the local-only original-source feasibility report without exposing its private case-to-source mappings or answer bodies to the coordinating session; preserve V01 audit defects transparently and retain non-scored scientific limits.
**Authority:** Research 661, Checkpoint 924, MC-0030 Messages 073-075, original historical Git horizon `47ed6344a9153dcf366769e95722840fbf1a8f8b`, exact existing private report identity, Validation 361 and Checkpoint 925. This is local deterministic evidence verification, not reference-gold adjudication or a new architecture evaluation.

## 1. Why this bounded audit was required

The independent Claude Opus 5.5 source reviewer reported N01 SUPPORTED and N02-N04 PARTIAL on four frozen information needs. It wrote a complete **84,359-byte** original-source report in a Git-ignored local folder. Its report SHA-256 was independently checked as `cce0c99e2c6b019b3e8f67ea960e92c2108b8ff673b685b2865de6977d06dc0b` before opening the file in the local-only audit process. The exposed ChatGPT coordinating model has **not** read the report's source-specific answers, quoted evidence or case-to-source mappings.

The current question was whether the report's explicit cited Git blob identities, source-line positions and purported literal excerpts are reproducible against the exact historical source snapshot. Source identity and quotation accuracy are separate from evidence entailment, historical event execution, governing owner acceptance and overall answer completeness. Therefore the audit never converts a valid Git reference into independently certified truth.

## 2. Exact executable approach and disclosure boundary

Two committed-source audit versions were created in the public repository. Both read only the fixed ignored report inside a local Python process, resolve its explicit `path@Git-blob-SHA1` table witnesses against `git rev-parse 47ed6344...:path`, open original contents through `git show` at the same pin, verify 1-based source-line bounds and classify literal quote containment. Both produce **only aggregate public JSON**, with original case-to-source mappings and detailed per-citation failure receipts kept under ignored local storage. No source text, original Git source-path lists, case answer, external website or independent hidden gold is printed to the coordinating model.

The strict comparison classes are:

- `EXACT_CITED_LINE_MATCH`: reported excerpt literally occurs within the selected original Git line(s).
- `WHITESPACE_ONLY_CITED_LINE_MATCH`: literal phrase differs only by whitespace normalization.
- `LITERAL_MATCH_ELSEWHERE_IN_SAME_BLOB`: quoted text occurs within the correct historical source but **not** at the reported lines.
- `NO_LITERAL_MATCH`: excerpt is **not found verbatim** in that historical source using the frozen conservative comparison.

This deliberately does not use fuzzy scoring, semantic similarity, rewriting, document-title inference, substitute sources, or post-hoc shifting to more convenient citations. A `NO_LITERAL_MATCH` can reflect paraphrasing, editorial shortening, quotation formatting or an incorrect attribution. It cannot alone establish that the underlying factual assertion is false.

## 3. V01 first run and transparent V02 correction

The first diagnostic already exposed 52 explicit citation rows and found 52 of 52 original Git object identities and valid line positions, but quoted text mismatches. The subsequent source audit V01 added a source-path prefix allowlist **not required by the original reference handoff**. That implementation bug wrongly excluded four historically tracked sources from the original admissible tree. It also classified one incidental non-source `@` field as a malformed citation. The **first saved V01 outcome has been preserved unchanged**, not deleted, rewritten or retroactively described as passing:

| Mechanical V01 count | Result |
| --- | ---: |
| Explicit cited rows | 52 |
| Verified historical blob identity | 48 |
| Valid line ranges | 48 |
| Rejected by checker source-path admission | 4 |
| Exact literal cited-line matches | 36 |
| Literal matches elsewhere in same blob | 1 |
| No literal match in source | 11 |
| Incidental non-source `@` mistakenly counted as malformed | 1 |

V01 public result **1,664 bytes**, SHA-256 `916103b959810258a663390a77ab020a13ba2868efcda8e6bd92812b83f758ab`. Detailed local-only V01 result **15,101 bytes**, SHA-256 `9310b16ca62fdaed688bd2fd8d63897a7b7c96cc0d85ab5f97dc5edd8d68933b`.

V02 was created and its **synthetic correction tests passed before running its historical-data audit**. It fixes only (i) an accidental source-directory restriction by admitting any safe relative original Git path whose blob is actually present at the pin; and (ii) incidental non-citation `@` text, while still detecting syntactically malformed file-extension citation candidates. The original private input bytes, Git pin, line parser, literal excerpt algorithm, quote mismatch categories, source budgets and scored boundaries were not changed. V02 is **a transparently corrected audit after V01 observations**, not a new prospective scientific experiment, not result-guided question/gold editing and not a repair to the private report.

## 4. Corrected actual V02 result

| Mechanically verified property | V02 outcome |
| --- | ---: |
| Original source pin exists and is a Git commit | PASS |
| Explicit original source witness rows | **52** |
| Distinct historical source paths actually opened | **46** |
| Original Git path/blob identity matches | **52/52** |
| Line syntax and 1-based position bounds | **52/52** |
| Verbatim quotes on the cited line(s) | **40/52** |
| Quotes found verbatim elsewhere in the same original blob | **1/52** |
| Quotes without literal match anywhere in that original blob | **11/52** |
| Unparsed candidate source citation cells | **0** |
| All literal excerpts verified at cited lines | **NO** |

The 12 nonmatching literal excerpts are **unresolved attribution observations**, not automatically twelve false answers or twelve unsupported claims. Some are in otherwise partially answerable cases; no case-level distribution is disclosed publicly. Original line citation fidelity therefore does **not** have a complete PASS even though source identity and line bounds do.

V02 public sanitized JSON **1,623 bytes**, SHA-256 `51ac418bca0c895a861dd4724810ed86e933fd2328bf2db10a4dfec1c674db49`. V02 private detailed audit **15,069 bytes**, SHA-256 `4852b554d3f9c2389d2eef2242bde32f1999b52cac80dca47a260b1e51ac8f6a`. Both the V01 and V02 complete public and private output bytes were reproduced by independent reruns of their deterministic builders and exactly matched their stored originals. A separate check confirmed no actual original Git source path or cited blob identity was serialized into the V02 public aggregate.

## 5. Verification strength and retained gaps

A real **80/80 focused synthetic and collaboration regression suite** passed, including corrupt Git blob IDs, invalid line spans, fabricated quotations, quotes at wrong source positions, malformed citation candidates, unsafe paths, source-root parity repair, report version/custody, prior metadata-only pilot tests and collaboration state. Public aggregate repository integrity is separately required at publication.

The audit covers **52 explicit reference-table citations**. It does not prove that all narrative and uncited assertions in the 84,359-byte report were grounded. It does not prove the correctness or provenance of documents' internal self-reports, the historical meaning of accepted design, actual execution or owner acts, or the semantic entailment of all answer claims. It does not independently certify the reviewer-reported N01 full-scope judgment. In particular, a syntactically valid Git blob and line can point to a passage that does not support the associated claim. The excerpt mismatches are retained as genuine review targets.

The private original-source report remains stored on the owner's local machine under ignored `.venv/`, as do both detailed citation-audit manifests. This **same-user local storage is not qualified formal hidden-gold custody**, and private output reproducibility does not create cryptographic separation from future arm authors.

## 6. Next narrow decision-relevant work

Use the **twelve original mismatch dispositions**, not another arbitrary fresh-question cohort, for a **separate bounded adjudication of literal source quotation fidelity**. Give an appropriately unexposed reviewer the immutable original private report, the V02 private mismatch receipt and original historical Git view under a formally scoped local-only read/write boundary; preserve original case text and original report unchanged. Classify each of 12 items as faithfully attributed paraphrase/formatting, line-reference defect, unsupported quote, or source-evidence insufficiency, with exact primary evidence. Keep the detailed correction/attribution assessment private and publish only safe aggregate counts. The reviewer must not simply replace the offending excerpts to obtain an artificial 52/52 success.

After that, if the report's source evidence is sufficiently qualified for an **unscored** comparison, proceed to a small true source-to-answer/abstention demonstration on the unchanged four needs with equal original source context and budgets. None of this supersedes the official Research 513/559/576 thresholds or resolves the prior C01/C02 holds. Do not silently turn the exposed locally retained report into an official scored answer key.

The project's freedom to redesign any knowledge or development level when evidence justifies it remains intact. Neither this audit nor the earlier 1/4 full-scope pilot selects a physical knowledge architecture, changes operative authority, or authorizes migration.

    R0_P03_PRIVATE_REFERENCE_BLOB_IDENTITY=52_OF_52_VERIFIED
    R0_P03_PRIVATE_REFERENCE_LINE_RANGES=52_OF_52_VALID
    R0_P03_PRIVATE_REFERENCE_CITED_LINE_LITERAL_MATCH=40_OF_52
    R0_P03_PRIVATE_REFERENCE_LITERAL_ATTRIBUTION_GAPS=12
    R0_P03_PRIVATE_REFERENCE_CLAIM_ENTAILMENT=NOT_VERIFIED
    R0_P03_PRIVATE_GOLD_QUALIFIED=false
    ORIGINAL_R0_P03_RESULT=INCOMPLETE
    PHYSICAL_ARCHITECTURE_SELECTED=false
