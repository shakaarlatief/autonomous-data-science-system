# Research 648: Real source-reference context audit, V02 correction, and source-declared metadata boundary

**Date:** 2026-11-12
**Status:** EXECUTED_EXACT_HISTORICAL_SOURCE_PROVENANCE_V01_PLUS_CORRECTED_SOURCE_DECLARATIONS_V02 / NO_AUTHORITY_ADMISSION
**Checkpoint:** 911. **Specification:** 028 unchanged. **Interaction:** ChatGPT / chatgpt-42.
**Scope:** Identify evidence lost when historical text references are materialized as unqualified graph edges; preserve an actual extractor defect separately rather than retroactively rewriting observed results; distinguish source-authored reference metadata from governed, normative or operational relations.

## 1. Why this work was necessary

The execution-first experiments 905–910 measured several real full-text, subject, literal path-link and hybrid navigation mechanisms. The 909 relationship index retrieved 208/220 structurally expected mentions at K=10, and the 910 wording experiment exposed 130/130 H2 parser misses. Those are valid executed engineering observations. However, both their structural reference oracle and relation index rely on the **same original literal path-extractor output**. They do **not** demonstrate that a repository path mention is a true source-owned editorial relationship, natural-owner J2, governing fact, cross-cutting concern, operational dependency or valid hyperlink.

The next concrete source audit therefore returned to the underlying **original historical Git text bytes** instead of running another test on the same unqualified edge oracle. It preserved exact provenance at source, target, line, column, source Git blob SHA-1, line SHA-256, full source SHA-256 and actual occurrence text. The historical corpus has **65** unique originals at `4b94ffe183ff7af72cef6ee7492b4ba2f30c11ef` with previously verified aggregate fingerprint `01206bdb2fdc3517627a94bdf6587efaa2f5d9ed10ad220f5799c496353c5a09`. No C01/C02 private file, restricted question, old answer gold or source release was accessed.

## 2. Fixed V01 original-provenance audit

The source-context contract was authored before the complete first V01 output. It runs the exact historical path matcher over the original body lines and records **every raw token occurrence**, without treating any syntax as semantic truth. Each occurrence is classified into FENCED_CODE, INLINE_CODE or OTHER_TEXT, with separate lexical cues for potential governance/navigation wording and path selectors. The same directed path may have multiple witnesses in different contexts.

    CONTRACT=experiments/r0_p03_navigation_probe/EXPLORATORY_REFERENCE_PROVENANCE_AUDIT_CONTRACT_V01.md
    EXECUTABLE=experiments/r0_p03_navigation_probe/exploratory_reference_provenance_audit_v01.py
    OUTPUT=experiments/r0_p03_navigation_probe/exploratory_reference_provenance_audit_result_v01.json
    OUTPUT_BYTES=177638
    OUTPUT_SHA256=e935edf01c6298b2c55950236c18eab6a9d4f712cfeca1ce3c7c48f69376d299

**Actual individual path references: 146**, collapsing to the exact previously scored **110** unique directed source/target pairs. Occurrence contexts: **93 fenced-code**, **46 inline-code**, **7 other-text**. Contexts can overlap per pair; **11 pairs** have multiple context types, while **70 pairs** occur exclusively in fenced code, **26 exclusively in inline code**, and **3 exclusively in other text.**

| Syntactic extraction policy (no semantic truth) | Directed pairs retained | Distinct sources with outgoing pairs | Distinct incoming targets |
| --- | ---: | ---: | ---: |
| ALL original literal path mentions | 110 | 31 | 39 |
| At least one occurrence outside fenced code | 40 | 23 | 16 |
| At least one occurrence outside both fenced and inline code | 7 | 6 | 5 |
| Actual conventional Markdown inline hyperlinks in these originals | 0 | 0 | 0 |

**70** of 110 original pairs vanish if only fenced code is excluded; an additional **33** pairs vanish if inline-code references are excluded. The final seven other-text paths are mostly typed selector-like strings. No conventional Markdown inline links from one historical 65-member source to another were detected by this exact bounded syntax parser. This cannot establish that there are no meaningful relationships, because inline-code source paths appear inside authored prose. Example source-grounded statement: the old `docs/CONTINUITY.md` explicitly says risk-scaled verification is governed by the path presented in inline-code syntax to `docs/DEVELOPMENT_METHOD.md`. A filter that discards that solely because of inline backticks would lose a plausible normative claim. A fenced path list can likewise carry historical context even when not a governing link.

V01's separate lexical indicators counted **14** line occurrences with bounded governance wording, **23** with bounded navigation wording and **zero** Markdown-link occurrences. These are flags for later semantic review, not author/adjudicator verdicts.

## 3. Observed V01 defect and V02 separately executed correction

A synthetic regression exposed an error **in V01 PATH_SELECTOR indicator only**. The V01 code searched for complete `path:docs/` text in a prefix ending at the first character of the *current* `docs/...` token. It consequently marked only **7** occurrences instead of all actual current-token-adjacent path selectors. This bug did not change the 146 raw occurrences, 110 source pairs or syntax-context projections. The original exact V01 JSON and its implementation are preserved and not overwritten.

The V02 contract fixes this **prospectively as a separate derivation**, fully bound to the original immutable V01 SHA. For each exact original occurrence, `PATH_SELECTOR` is recomputed only when the five immediately preceding characters say `path:`, and a new narrower `DECLARED_REFERENCES_FIELD` flag is set only where that adjacent selector occurs on a real Markdown `**Declared references:**` metadata line. Every other exact occurrence identity, source byte digest, position, line and earlier syntactic context must remain identical.

    CONTRACT=experiments/r0_p03_navigation_probe/EXPLORATORY_REFERENCE_DECLARATION_CORRECTION_CONTRACT_V02.md
    EXECUTABLE=experiments/r0_p03_navigation_probe/exploratory_reference_declaration_correction_v02.py
    OUTPUT=experiments/r0_p03_navigation_probe/exploratory_reference_declaration_correction_result_v02.json
    OUTPUT_BYTES=175032
    OUTPUT_SHA256=25b26e66e3bb03232d4ee7931e66aceb6bd6eaf28d2f5ae0ff207713c333831d

**Actually measured V02 source-authored subsets:**
- **18** adjacent `path:` occurrence/pairs, written in **12** historical source documents, pointing at ten distinct targets.
- Of those, **11** appear in explicit **Declared references** metadata fields across **six** source documents and seven distinct targets.
- V02 modified **18 occurrence-flag records** relative to V01, not the original paths, source lines, graph edges, source bytes or case-scoring material.
- The same four context-projection pair counts remained **110 / 40 / 7 / 0**, and all 65 real original documents remain included.

These source-owned fields are an actual author's declaration that other sources are **referenced**. They are not evidence of semantic governance, normative `about`/J2 coverage, accepted implementation, production deployment, target validity or historical event correctness. An explicit `path:` field without the `Declared references` label is still merely a typed path selector until its source-owner meaning is established.

## 4. Independent exact-target-match challenge and known parser limitation

The synthetic test also found a separate legacy matcher limitation: in a new sentence `See docs/b.md.`, the old regex can reject the valid `docs/b.md` token because a trailing period belongs to its exclusion class. Instead of silently changing old source interpretation, V02 ran an **independent eligible-path enumeration** by matching escaped exact paths from the original 65-source roster and using alternative terminal boundaries. That scanner independently returned **146 occurrence instances and 110 directed source pairs** in this exact old corpus, with **zero additional entries**. Therefore the counted old pinned corpus is not materially affected by that newly identified boundary bug, though it would be unsafe to reuse the old regex as an exhaustive extractor over an arbitrary new corpus.

The independent challenger is still a bounded syntax scanner, not a separate semantic annotator or proof of completeness for every path grammar.

## 5. Consequences for architecture and the experimental program

1. **Distinguish occurrence, reference, declaration, and authority.** The correct representation is not one undifferentiated `edge`. Source path occurrences have witnesses and context; some are explicitly source-authored declarations; none automatically proves a governing obligation or real dependency.
2. **Do not apply naive code-exclusion as a semantic filter.** Inline-code formatting can mark an exact file name within an authoritative prose assertion. Require typed source relation semantics and provenance, not an aesthetic Markdown heuristic.
3. **Do not promote the old literal graph's self-consistency scores.** The impressive 208/220 K=10 structural coverage is a valid parser/index capability result, but cannot decide B0–B4 or validate J2 without independently qualified semantic relation targets.
4. **A useful next engineering probe** would distinguish the eleven authored Declared references from actual source-owned governing relations, carry line-level evidence through any navigation service, and test whether the system refuses unsupported dependency/authority claims. The 11 fields are an accessible real source-backed seed, not sufficient blind semantic gold.
5. **Invite a bounded exposed Claude critique** of the accumulated empirical findings and the V01/V02 evidence boundary. Claude's MC-0030 history means it is a comparative technical critic, not an independent blind original-task/gold evaluator. Any owner relay must use the exact public branch and frozen artifact hashes.

No original twelve-primary/independently neutralized nine-legacy Research 513/559/576 scored test has completed. Specification 028 and original C01/C02 source custody and dispositions remain unchanged. No source admission, target selection, production architecture switch or migration is authorized.

    REAL_SOURCE_PROVENANCE_AUDIT=EXECUTED
    HISTORICAL_SOURCES=65
    PATH_OCCURRENCES=146
    RAW_DIRECTED_PAIRS=110
    OUTSIDE_FENCE_PAIRS=40
    OUTSIDE_ALL_CODE_PAIRS=7
    MARKDOWN_INLINE_LINK_PAIRS=0
    V01_SELECTOR_BUG=OBSERVED_AND_IMMUTABLY_RETAINED
    V02_ADJACENT_PATH_SELECTOR=18
    V02_SOURCE_AUTHORED_DECLARED_REFERENCE=11
    ALTERNATE_MATCHER_EXTRA_PAIRS=0
    SOURCE_OWNED_DECLARATION_IS_GOVERNING_RELATION=NOT_ESTABLISHED
    ORIGINAL_R0_P03_SCORED_ARCHITECTURE=NONE
    NEXT=BOUNDED_EXPOSED_CLAUDE_CHALLENGE_AND_SOURCE_DECLARATION_SEMANTICS
