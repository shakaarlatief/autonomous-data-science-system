# Research 647: Actual 719-query relationship paraphrase, authority-scope, and abstention stress

**Date:** 2026-11-12
**Status:** REAL_719_QUERY_PARAPHRASE_STRESS_EXECUTED / ACCEPTED_S1_S2_H1 / H2_DIRECTION_PARSE_FAILURE / UNSUPPORTED_SEMANTIC_SCOPE_GUARDED
**Scope:** Record a real, complete fixed source-derived wording and unsupported-claim query population, distinguish recognized source-relative absence from unparsed intention, and prevent raw path mentions from being treated as dependency, governed authority, or working links.
**Authority:** Checkpoint 909 exact existing 130 query result; immutable 65 historical original Git bytes; pre-execution V01 paraphrase/scope contract and real executed 719 query result; Research 513/559/576 unchanged.
**Checkpoint:** 910. **Specification:** 028 unchanged. **Interaction:** ChatGPT / chatgpt-42.

## 1. Question and source construction

An additional run was actually executed, not proposed. It consumed exactly 65 real historical UTF-8 repository document bodies at Git revision `4b94ffe183ff7af72cef6ee7492b4ba2f30c11ef`, bounded source fingerprint `01206bdb2fdc3517627a94bdf6587efaa2f5d9ed10ad220f5799c496353c5a09`, and all 110 directed raw `docs/...` path mentions. The previous Checkpoint 909 experimental result identity was checked before execution: SHA-256 `99206720df7dfa6deb788f4abd8428137a55f5ee68962e83f08da79a7775c399`. The original prior results and scorer remain unchanged.

The new complete fixed population contains **719 unique queries**, built from every one of the 65 unique first H1 titles:

- **520 explicitly source-scoped path-mention questions** in four 130-query families: S1/S2 examples used to define a generic bounded parser, H1/H2 alternative held-out morphology fixed before score observation. Each family contains 65 forward and 65 reverse requests, **70 positive** and **60 zero-literal-reference** cases. Across four families there are 880 reference opportunities and an aggregate K=10 structural ceiling of 832.
- **195 intentionally unsupported real-world claim questions**, all 65 titles asked separately about operational dependencies, source governance/authority, and working hyperlinks. None of these concepts is proven by literal repository-path mentions.
- **Four unknown/ambiguous title controls**, two absent-name requests and two requests containing two different quoted titles.

The full method was specified before new scores, at:

    experiments/r0_p03_navigation_probe/EXPLORATORY_PARAPHRASE_SCOPE_AND_ABSTENTION_CONTRACT_V01.md

Executed module and exact exclusive-create output:

    experiments/r0_p03_navigation_probe/exploratory_paraphrase_scope_and_abstention_v01.py
    experiments/r0_p03_navigation_probe/exploratory_paraphrase_scope_and_abstention_result_v01.json
    FULL_OUTPUT_BYTES=1276498
    FULL_OUTPUT_SHA256=b1e4291b673d16e45ac96c6785b92884efc327276a9a898f7d83b6b95138a26e

Every requested source title and source file was retained. No question wording, graph edge or parser rule was changed after result inspection.

## 2. Actual implemented methods

**Old exact-template parser:** Immutable `parse_relation_question` from Checkpoint 909. It is a control for dependence on the original rigid template. It recognized zero of the 719 differently worded requests, as expected.

**New guarded relationship parser:** Accepts exactly one quoted first-H1 source title, resolves it from the pinned 65-source title index, distinguishes unknown and ambiguous names, and requires *both* a repository-file-path scope cue and an explicit reference/mention/citation cue. It then recognizes source-relative forward intent from bounded spatial prefixes (in, inside, within) or reverse intent from bounded query-prefix forms. It **rejects** actual dependency, governed authority, real-world relationship and working hyperlink claims before using the graph. Unsupported requests return an explicit `unsupported_scope` state, **not** a false answer asserting no real dependencies or hyperlinks. Successfully parsed source-reference questions use the real 110-edge outgoing or incoming index, with the same BM25/path tie-break and ten-result limit.

**Source-only lexical control:** The same FTS5/BM25 textual retrieval supplies ordinary document candidates, top ten, for each query, including unsupported ones. These are **candidate documents**, not answers asserting any relationship. A lexical candidate hit is not itself a false authority claim. This control returned 7,190 candidate source slots over 719 questions.

**No graph answer labels given to the parser:** `classify_intent(query, titles)` receives only the natural-language query and the historical first-H1 title index. It cannot inspect expected graph neighbors. Accepted index retrieval and scoring do share the same literal path graph, which limits independence of the retrieval score.

## 3. Actual results

| Fixed question family (130 each) | Direction recognized | Required source-mention hits at top ten | K=10 ceiling | Source-relative empty confirmed |
| --- | ---: | ---: | ---: | ---: |
| S1: repository-path references | 130 | 208/220 | 208 | 60/60 |
| S2: docs/-path mentions | 130 | 208/220 | 208 | 60/60 |
| H1: explicit file-path citations | 130 | 208/220 | 208 | 60/60 |
| **H2: outbound/inbound docs/ citations** | **0** | **0/220** | 208 | **0/60** |

The held-out H1 wording happened to satisfy the bounded generic spatial cues. The equally valid H2 wording used `outbound`/`inbound` without those spatial prefixes, and the rule-based intent parser rejected **all 130** as `unparsed_in_scope`. This is a meaningful **semantic coverage failure**, despite the presence of authentic structural witnesses for 70 of the rejected requests.

Across 520 source-scoped paraphrases, 390 were interpreted and 130 were not, or **75% fixed-family intent coverage**. Across 880 source-mention opportunities, 624 were retrieved, **70.9% unconditional positive-instance recall**. Relative to the fixed ten-result ceiling of 832, 624/832, or **75% of achievable structural reference hits**, were obtained. The old exact-template parser recognized **0/719** new questions.

**Do not inflate successful empty-set scores:** When H2's 60 structurally empty tasks were rejected, the predicted relation path list was empty and a naïve set-equality scorer would report 60 exact-set matches. The guarded parser explicitly recorded **0 correctly recognized `no_matching_literal_mentions` states** for H2. These cases are rejected intentions, not successfully answered structural negatives. For S1, S2 and H1, all 180 structurally empty queries were correctly identified as supported-scope, no-edge findings.

**Unsupported-scope controls:** All three non-equivalent question families were explicitly rejected safely: **65/65 dependency, 65/65 governance/authority, and 65/65 working-hyperlink requests**, total **195/195**, with zero asserted structural relationships. Four unknown/ambiguous identity controls were separately rejected **4/4**. This is an implementation correctness result on hand-authored controls, not evidence that the parser never makes an unsafe claim on arbitrary text.

## 4. Interpretation and scientific limits

The result is stronger than simply checking Checkpoint 909's fixed grammar: the same bounded graph retrieval mechanism was exposed to new query surface forms and a purposely non-equivalent semantic scope. It demonstrates an engineering **tradeoff between a conservative evidence boundary and incomplete linguistic coverage**. Silent lexical fallback on a failed relationship interpretation could return apparently relevant source bodies without satisfying the requested relation, while overpermissive acceptance could equate raw text mentions with historical authority. A typed `unparsed_in_scope` outcome makes both limitations visible.

Nevertheless, none of these requests came from an independent unseen human task author. The exact source titles and query-template families were selected by the implementing coordinator, and the H1/H2 forms were known in the pre-scored protocol. The held-out distinction applies only to the parser's initial example morphology, not independent experimental provenance or a natural language distribution. The relation-index and reference oracle use the same path-mention extractor, so 208/220 on accepted questions is expected when the exact graph is correctly traversed. No historical dependency, lifecycle governance, accepted editorial link, actual hyperlink operation or project-wide current authority has been authenticated.

This study does **not** implement true source-owned B2 editorial `CARRIER_LINKS`, B3 selective concerns, B4 learned semantic retrieval, full V03 equalized baselines, independently adjudicated historical answers, maintenance holdout, cost parity, or original 12-primary Research 513 architecture selection. Original C01/C02 question identities/dispositions remain unchanged. No source world admission or physical migration occurred.

## 5. Next bounded research direction

Do **not** adjust the existing guard to recognize `outbound`/`inbound` and then rescore H2 as though it were unseen. H2's 0/130 coverage is now an immutable negative generalization observation. A successor parser may learn to recognize new linguistic cues, but should be evaluated on **genuinely fresh independently authored or otherwise withheld** query language and against source-declared relationship semantics distinct from the answer-extracting raw path graph.

Before choosing a physical architecture, examine how to represent and verify actual source-owned editorial relations or provenance-bearing claims. Where authentic declarations are absent, record that evidence gap and abstain instead of pretending any literal document citation is an endorsed dependency. A focused independent Claude architectural/methodological critique could now assess the accumulated executed Checkpoint 905-910 findings before any major new semantic mechanism is made authoritative, but need not prevent further runnable exploratory engineering tests.

    CHECKPOINT_910=PARAPHRASE_SCOPE_TEST_EXECUTED
    NEW_REQUESTS=719
    NEW_SOURCE_SCOPED_REQUESTS=520
    NEW_UNSUPPORTED_SEMANTIC_REQUESTS=195
    NEW_UNKNOWN_AMBIGUOUS_REQUESTS=4
    IN_SCOPE_INTERPRETED=390
    IN_SCOPE_UNPARSED=130
    SOURCE_INSTANCE_REQUIRED=880
    SOURCE_INSTANCE_FOUND=624
    TOP10_INSTANCE_CEILING=832
    HAND_AUTHORED_UNSUPPORTED_REJECTIONS=195_OF_195
    SOURCE_IDENTITY_CONTROLS_REJECTED=4_OF_4
    H2_REJECTED=130_OF_130
    H2_CORRECT_NO_EDGE_STATE=0
    PREVIOUS_909_HASH_PRESERVED=YES
    R0_P03_FORMAL_SCORING=NONE
    ARCHITECTURE_SELECTED=NO
    NEXT=INDEPENDENT_QUERY_AND_ACTUAL_DECLARED_RELATION_SEMANTICS
