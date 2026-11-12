# Research 644: Actual 65-query document-location stress reveals query-family dependence

**Date:** 2026-11-12
**Status:** EXECUTED_MECHANICAL_65_HEADING_QUERIES / B0_64_OF_65_B1_63_OF_65_B2_PROXY_64_OF_65 / NO_ARCHITECTURE_SELECTION
**Scope:** Preserve a real deterministic second query family and the clear difference between authored subject-label legacy retrieval and query-only document-location behavior.
**Authority:** Fixed exploratory 65-first-H1 source-only query method, real executed original historical source comparison and exact trace; Research 642/643, original Research 217/513/559 and Specification 028 remain unchanged.
**Checkpoint:** 907. **Specification:** 028 unchanged. **Interaction:** ChatGPT / chatgpt-42.

## 1. Why a second query family was necessary

The already executed nine W5-T1-V02 original scenarios were authored alongside B1's source-owned subject memberships. B1 was given the correct published subject ID and achieved a familiar 9/9 strict pass on that legacy fixture. Research 559, following the previously delivered Claude independent design critique, had identified the same oracle-bias risk. A second test family must not reuse those subject gold lists or provide the topic ID to the B1 treatment.

To perform an actual broader test without restarting C01/C02 private witness recovery, the source-only sampling rule created one exact-title document-location query from the **first literal nonempty Markdown `# ` heading of every one of 65 real historical Git source documents** at exact historical revision `4b94ffe183ff7af72cef6ee7492b4ba2f30c11ef`. The correct target is exactly the same source file that contained the heading. Preflight confirmed **65/65 files had a first H1**, **65/65 headings distinct**, and maximum heading length 93 characters. All 65 queries were included without manual replacement, success-based rejection or targeted paraphrases.

This is mechanically answerable and orthogonal to the old B1-authored nine scenario relevance sets, but it is **not** a natural independent human information-need sample. Exact source heading matching inherently tends to favor lexical retrieval, and a document target is not an authoritative answer or execution witness.

## 2. What actually ran

Fixed method and real executed code/result:

    experiments/r0_p03_navigation_probe/EXPLORATORY_65_SOURCE_HEADING_QUERY_STRESS_CONTRACT_V01.md
    experiments/r0_p03_navigation_probe/exploratory_65_source_heading_query_stress.py
    experiments/r0_p03_navigation_probe/exploratory_65_source_heading_query_stress_result_v01.json

    EXACT_SOURCE_REVISION=4b94ffe183ff7af72cef6ee7492b4ba2f30c11ef
    SOURCE_DOCUMENTS=65
    H1_HEADING_QUERIES=65
    HISTORICAL_LITERAL_CITATION_EDGES=110
    QUERY_LIMIT=10
    EXECUTED_RESULT_BYTES=195216
    EXECUTED_RESULT_SHA256=497cdfc559f7d2d56c97b12afb33de1210f5f8bf1945ca9978bd7b73b6ad58b4

Compared the actual identical full-text/subject metadata/citation source inputs with one repeated heading query per file:

- **B0-like**: identical SQLite FTS5 unicode61 and BM25 literal OR query strategy, at most ten full-text matching documents.
- **B1-like automatic human-language subject routing**: no old scenario topic IDs, no target/gold path available to ranker. Subject inference uses fixed content-word overlaps of heading against published authored subject label/description and a minimum overlap threshold, then source-owned subject memberships and preferred route, with lexical fallback. This is *not* a sophisticated query understanding model and has preexisting metadata cost.
- **B2-like one-hop literal citation expansion**: no governed editorial link semantics, same 65-document explicit `docs/` mentions and one-hop seeded BM25 traversal as the earlier proxy. Literal path mentions are neither authority nor accepted relations.

Score each ranked result against its mechanically known own-document target at rank one and among top ten; report reciprocal rank@10 and counts returned. This is an exact source **location** score, not historical semantic answer correctness.

## 3. Actual results and contrast

| Metric | B0-like full text | B1-like inferred subject route | B2-like literal-link proxy |
| --- | ---: | ---: | ---: |
| Target source in first result | **45/65** | **33/65** | **45/65** |
| Target source somewhere in top ten | **64/65** | **63/65** | **64/65** |
| Mean reciprocal rank@10 | **0.803590** | **0.653590** | **0.802949** |
| Total returned source slots | 650 | 650 | 650 |

The B1 deterministic catalog term matcher inferred a subject for **54/65** queries and used lexical fallback for **11/65**. The B2 citation proxy added **306** citation candidates behind seed results across all 65 queries. Those counts are diagnostic implementation facts, not learned relevance or authoring-equivalence measurements.

**One query family favors B1's original editorial taxonomy by construction, another heading-based family favors direct lexical matching.** The observed difference does not establish that B0 is globally better or that Research 217's semantic subject arrangement has no value; it shows that **routing the user query to the correct navigation mechanism is a real part of the design** and that an independently selected set of task types matters more than repeating one biased oracle.

Particularly, B1's original 9/9 requires known subject IDs and B1-authored gold; when the query gives only natural-language title terms and a simple subject inference rule, B1 can displace exact document targets. Conversely, this new test bakes target words into the query from the target content, favoring lexical retrieval. A defensible architecture may need a **hybrid query router or fallback** without treating either mechanism as universal. No such architecture is selected here and any new hybrid should be compared prospectively on different queries.

## 4. Constraints, execution risk and next concrete engineering direction

These 65 headings are not human-authored unseen tasks, the original 65 documents and subject annotations were already used in W5, and the source target is an intentional tautological locator for a document title. No true held-out corpus, independent natural query gold, authority/currentness, J2 closure, historical operation proof, B3 governed concern vocabulary or B4 embedding comparator is tested. The B1 topic matcher is one heuristic, not the best possible inference system. No Research 513 threshold has been amended and the formal R0-P03 12-primary plus independently re-adjudicated nine-legacy experiment remains unscored.

**Concrete next choice rather than another archival evidence loop:** evaluate a properly versioned and reproducible retrieval-intent switch between exact-source lookup, topical discovery and cross-cutting obligation discovery, then test it with a new arm-neutral task sample. If only two or three runnable mechanisms are source-backed, disclose missing B3/B4 coverage rather than fabricate and score them. Alternatively the owner can pursue full prospective Research 513 reference qualification separately, without pausing all useful execution-first engineering. Claude's earlier exposed prefreeze critique remains useful design evidence, but no independent Claude model response is falsely claimed for these executed pilot measurements.

    HEADING_TASKS=65_OF_65_ALL_INCLUDED
    QUERY_FROM_H1=EXACT_SOURCE_TEXT
    SUBJECT_ID_SUPPLIED=NO
    B0_TOP_ONE=45_OF_65
    B1_TOP_ONE=33_OF_65
    B2_PROXY_TOP_ONE=45_OF_65
    B0_TOP_TEN=64_OF_65
    B1_TOP_TEN=63_OF_65
    B2_PROXY_TOP_TEN=64_OF_65
    B0_MRR_AT_10=0.803590
    B1_MRR_AT_10=0.653590
    B2_PROXY_MRR_AT_10=0.802949
    C01_C02_PROTECTED_REFERENCE_ACCESSED=NO
    FULL_RESEARCH_513_SCORING=NONE
    ARCHITECTURE_SELECTION=NONE
    NEXT=EXECUTION_FIRST_QUERY_ROUTING_STRESS_AND_PROSPECTIVE_GOLD_DECISION
