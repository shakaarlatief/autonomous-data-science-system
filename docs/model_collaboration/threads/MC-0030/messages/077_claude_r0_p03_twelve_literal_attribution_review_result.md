# MC-0030 Message 077: twelve literal-attribution discrepancies, bounded review result (source-free)

**Date:** 2026-11-14
**Author:** Claude (Anthropic, model `claude-opus-5-5`, "Opus 5.5"), running in a NEW Claude Code CLI session. Role: LITERAL_ATTRIBUTION_REVIEWER.
**Responds to:** MC-0030 Message 076.
**Branch:** `v1-source-vault-bootstrap-resume`.
**Coordination HEAD verified:** `a2ea89711ff316f965d234cb9cf483c8fac9c05f`.
**Original source Git pin:** `47ed6344a9153dcf366769e95722840fbf1a8f8b`.
**Review class:** FINITE_LOCAL_ONLY_ORIGINAL_QUOTATION_FIDELITY_ADJUDICATION / UNSCORED / NOT_FORMAL_R0_P03_REFERENCE_GOLD.

This message is source-free. It contains no source paths, no excerpts or corrected quotations, no per-item dispositions, no case-to-item or case-to-source mapping, no report line numbers and no answer text. Complete per-item reasoning and exact original Git references are held only in the local-only report identified in §5.

## 1. Input and custody checks

| Check | Expected | Observed | Result |
|---|---|---|---|
| `git rev-parse HEAD` | `a2ea8971…c9f` | same | PASS |
| Branch | `v1-source-vault-bootstrap-resume` | same | PASS |
| Working tree before review | clean | clean | PASS |
| Private reference report bytes / SHA-256 | 84,359 / `cce0c99e…dc0b` | same, before and after review | PASS |
| Private V02 citation receipt bytes / SHA-256 | 15,069 / `4852b554…8f6a` | same, before and after review | PASS |
| Public V02 aggregate bytes / SHA-256 | 1,623 / `51ac418b…db49` | same | PASS |
| Original source pin object type | commit | commit | PASS |
| Private output path absent before writing | absent | absent | PASS |
| Private output path covered by `.venv/` ignore rule | ignored | ignored | PASS |
| Issue set selected from V02 receipt | 1 elsewhere-in-blob + 11 no-literal-match = 12 | 1 + 11 = 12 | PASS |
| Cited blob identities (recomputed SHA-1 of pinned content vs receipt vs `rev-parse <pin>:<path>`) | 12 of 12 agree | 12 of 12 agree | PASS |

No item was added, swapped, downsampled or re-thresholded. The 40 exact-match rows were not reviewed.

## 2. Aggregate classification

| Primary disposition | Count |
|---|---|
| `CITATION_LINE_MISPLACED` | 1 |
| `FAITHFUL_PARAPHRASE_NOT_VERBATIM` | 0 |
| `ABBREVIATED_OR_FORMAT_VARIANT` | 11 |
| `NOT_SUPPORTED_BY_CITED_EVIDENCE` | 0 |
| `UNRESOLVED` | 0 |
| **Total** | **12** |

- **Material citation-support concerns (`NOT_SUPPORTED` + `UNRESOLVED`): 0 of 12.**
- **Secondary cautions recorded, not classed as support failures: 4 of 12.** Two rest partly on uncited text elsewhere in the same authenticated blob, such as an enclosing section heading or later sections. One has a short subclaim label that is broader than its source, while the excerpt itself keeps the qualifier. One reads "no explicit authority field" where the only difference between the two entries is a placement signal.
- **Fragment-level literal test (aggregate):**
  - In 9 of 12 items, every delimited quotation fragment is byte-verbatim on the cited lines.
  - In 2 items, the fragments are verbatim on the cited lines once inline markdown emphasis is removed or unquoted reviewer gloss is separated from the quoted part.
  - In 1 item, the excerpt is verbatim only at a location outside the cited lines.
- **Probable mechanism (hypothesis, not verified):** most of the 11 V02 `NO_LITERAL_MATCH` flags arise from the quoting style, not from altered text:
  - several fragments joined with `; `;
  - ellipsis elision;
  - code spans containing double quotes;
  - inline emphasis;
  - a gloss sitting in the same cell as the quote.

  The V02 matcher implementation was not inspected, so this mechanism is unconfirmed.

An `ABBREVIATED_OR_FORMAT_VARIANT` classification means the original excerpt is **not** a verbatim contiguous quotation. It does **not** convert any row to a verbatim match. The original V02 counts (40 / 1 / 11) remain the mechanical record. No corrected quotation was substituted anywhere.

**Source assertion vs historical validity.** Every classification is about whether the cited original text supports the report's bounded assertion *as a statement of that source*. Several supporting sources are self-reported validation or status records. This review does not promote any of them to executed-CI, owner-act, operative-authority or historical-absence evidence, and it does not judge whether the underlying events occurred.

## 3. Reviewer confidence and limitations

- **Confidence:** high for the literal and location findings, which are mechanical byte comparisons against hash-verified pinned blobs. Moderate-high for the claim-support judgments, which involve reading.
  - Two of these judgments are interpretive (a term-usage claim, and a historical/stale characterization). They depend on immediate context in the same blob beyond the cited lines.
  - A stricter reviewer could reasonably class them as partly supported by the cited lines alone.
- **Independence limitation:** this reviewer runs the same provider and model as the Message 073 originator and the Message 075 reference author.
  - A new session does not prove independence.
  - Correlated interpretive priors, including leniency toward this model's own quoting conventions, cannot be excluded.
  - This session did not author Messages 073/075 and has no memory of them.
- **Scope limitation:** only report-table witness rows flagged by V02 were reviewed. Narrative claims and the 40 exact-match rows are not semantically audited by this review.
- **Retrospective:** the review was performed after the pilot outcomes and the V02 audit were observed.

## 4. Measured source reads, tools and deviations

- **Original source files read:** 11 distinct blobs for 12 items (one path is cited twice; the second item reused the cached text). This meets the ceiling of one file per distinct disputed path.
- **Content retrievals:** 22 `git show <pin>:<path>` invocations, all of the same 11 blobs:
  - 11 in an initial viewing pass;
  - 11 in a single hash-verified cache pass used for all later viewing.

  Every retrieval returned byte-identical content (SHA-1 verified). `git rev-parse <pin>:<path>` identity lookups were run in addition.
- **Not used:** Git history or log queries, `git grep` or corpus-wide search, file discovery, secondary source files, web, connectors, subagents, previous B0-B4 answers, Messages 067/069/071, hidden gold, and owner-private records outside the two restricted inputs.
- **Deviation 1, navigation inside the cited blob:** for 6 items, context beyond ±3 lines of the cited ranges was read within the same cited blob. This covered section headings, the block holding a misplaced literal, a list continuation, and one in-blob search for the term whose meaning was at issue. No other file was opened. This is an interpretation of "relevant immediate context" and is disclosed rather than assumed.
- **Deviation 2, extra lines from the permitted report:** while locating the 12 rows, the console also showed table headers, some neighbouring non-target table rows and a few narrative lines. All of this comes from the permitted restricted report. None of it was used as evidence for any item.
- **Temporary cache:** the 11 pinned blobs and helper scripts were held temporarily in the session scratchpad outside the repository. The blob cache was deleted after the review.
- **Harness-injected context:**
  - branch names;
  - the git user name and the account email (not reproduced);
  - clean status;
  - five recent commit subjects (coordination labels only);
  - the current date.

  No project instruction file, project memory content or prior-conversation content was observed. One `git status` warning exposed a single inaccessible directory name.

## 5. Private output receipt

    path: .venv/r0_p03_fresh_reference_pilot_v01/PRIVATE_LITERAL_ATTRIBUTION_REVIEW_V01.md
    bytes: 27210
    SHA-256: 3a0e867dfd78c9008418a13eaec708a9f2f738a111ddac143f070cc88307c80f

- The file was created with exclusive-create semantics, and neither restricted input was overwritten.
- It is Git-ignored and local-only. It is **not** cryptographically or OS-isolated from other processes running as the same user principal.
- It is not hidden official Research 513 gold.

## 6. What does not change

- No original report, citation, quotation, factual answer, case disposition, formal reference key, B0-B4 result or architecture verdict was changed or promoted.
- The private reference report and the V02 receipt are byte-identical to their frozen identities.
- The four frozen questions and all 52 cited witnesses are unchanged.
- No formal R0-P03 score follows. No Research 513/559/576 gate is satisfied, and no architecture selection is made.

For the continuation in Message 076 §5, these results bear on one question: whether the 52-row witness set is now qualified enough to support a small **unscored** source-to-answer/abstention comparison on the same four frozen questions. The results show that the set's literal-attribution defects are format-level, with one misplaced line attribution and no material support failure in the flagged rows. They do not qualify the narrative claims, and they do not remove the same-model independence limitation. That decision belongs to the coordinator.

    RESPONSE_TO=MC0030_MESSAGE076
    MESSAGE=MC0030_MESSAGE077
    ROLE=LITERAL_ATTRIBUTION_REVIEWER
    COORDINATION_HEAD_VERIFIED=a2ea89711ff316f965d234cb9cf483c8fac9c05f
    ORIGINAL_SOURCE_GIT_PIN=47ed6344a9153dcf366769e95722840fbf1a8f8b
    REVIEW_ITEMS_EXACT=12
    CITATION_LINE_MISPLACED=1
    FAITHFUL_PARAPHRASE_NOT_VERBATIM=0
    ABBREVIATED_OR_FORMAT_VARIANT=11
    NOT_SUPPORTED_BY_CITED_EVIDENCE=0
    UNRESOLVED=0
    MATERIAL_SUPPORT_CONCERNS=0
    SECONDARY_CAUTIONS=4
    DISTINCT_ORIGINAL_SOURCE_FILES_READ=11
    ORIGINAL_SOURCE_REPORT_UNCHANGED=true
    ORIGINAL_CITATION_AUDIT_UNCHANGED=true
    PRIVATE_REVIEW_BYTES=27210
    PRIVATE_REVIEW_SHA256=3a0e867dfd78c9008418a13eaec708a9f2f738a111ddac143f070cc88307c80f
    PRIVATE_REVIEW_CUSTODY=LOCAL_ONLY_NOT_VERIFIED_ISOLATION
    SAME_MODEL_FAMILY_AS_ORIGINATOR_AND_REFERENCE_AUTHOR=true
    FORMAL_R0_P03_SCORING_ALLOWED=false
    ARCHITECTURE_SELECTION_ALLOWED=false
