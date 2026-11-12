# Research 643: Actual execution-first source citation traversal comparison and B2 boundary

**Date:** 2026-11-12
**Status:** EXECUTED_POSTHOC_B2_LIKE_SOURCE_LINK_PROXY / LOWER_OVERALL_RECALL_THAN_B0 / LEGACY_PILOT_ONLY
**Scope:** Preserve a real source-derived third retrieval mechanism executed against the exact nine-scenario/65-carrier historical fixture, clarify nonuniform outcomes and isolate from authentic B2 editorial-link semantics.
**Authority:** Explicit owner direction to continue executable experiments, fixed exploratory source-link contract, actual live result JSON, prior Research 642 and Research 559/513. No original protocol/architecture amendment.
**Checkpoint:** 906. **Specification:** 028 unchanged. **Interaction:** ChatGPT / chatgpt-42.

## Real implemented expansion

The previously executed 65-source corpus and nine scenarios remain frozen in Git at `4b94ffe183ff7af72cef6ee7492b4ba2f30c11ef`, with the same human-readable subject-label queries and per-scenario top-ten retrieval budget. The new V02 incremental executable validates that its B0 ranking **exactly matches** the already committed B0 trace before applying any link expansion. It also reuses the exact previously measured B1 trace without changing author metadata.

    experiments/r0_p03_navigation_probe/EXPLORATORY_LEGACY_B2_SOURCE_LINK_PROXY_CONTRACT_V01.md
    experiments/r0_p03_navigation_probe/exploratory_legacy_b2_source_link_proxy.py
    experiments/r0_p03_navigation_probe/exploratory_legacy_b2_source_link_proxy_result_v01.json

The new fixed **B2-like explicit citation traversal proxy** scans historical Markdown source text for literal `docs/...` path mentions of exact members of the same 65-carrier population, yielding **110 directed references from 31 of 65 sources**. This literal mention graph is not interpreted as governed, accepted, status-correct, semantically relevant or editorially curated. The retrieval rule retains the first **five** B0 lexical/BM25 source results as seeds, follows directed references **one hop**, selects eligible unique targets by descending number of citing seeds then prior BM25 position then stable path, and fills any unoccupied results back from B0 until ten. The original private C01/C02 question/answer/source-mapping files are never touched.

The source-link retrieval algorithm does **not** inspect the known `must_retrieve` or `must_not_retrieve` targets when ranking. Those are used only in the later mechanical evaluation function, and the same published nine-scenario research oracle is used across all three mechanisms.

## Actual reproducible findings

    RESULT_BYTES=27987
    RESULT_SHA256=136b7037515f97ea253abee6b1d9394a4f7770edddbc108a8174f29b48aae404
    SOURCE_CORPUS=65_HISTORICAL_ORIGINALS
    SCENARIOS=9_PUBLISHED_LEGACY
    CITATION_EDGES=110
    CITATION_SOURCE_CARRIERS=31
    B2_LINK_TARGET_SLOTS_ADDED_TO_SEEDS=33
    PER_SCENARIO_RETRIEVAL_LIMIT=10

| Measure | B0-like lexical | B1-like authored subjects | B2-like literal source-link proxy |
| --- | ---: | ---: | ---: |
| Strict complete scenario PASS | 1/9 | 9/9 | 2/9 |
| Gold positive source instances @10 | 28/39 | 39/39 | 25/39 |
| Micro recall@10 | 0.717949 | 1.000000 | 0.641026 |
| Macro recall@10 | 0.738889 | 1.000000 | 0.672222 |
| Explicit negative example intrusions | 4 | 0 | 6 |
| Total returned carrier slots | 90 | 51 | 90 |

The link expansion both improves one scenario's strict pass relative to B0 and **reduces total recall** by three positive instances while adding two more explicit distractor intrusions. These outcomes are not contradictory because full-scenario pass is an all-or-nothing event on different scenarios. They illustrate a concrete failure mode of **unqualified graph expansion**: a mention graph can displace relevant initial lexical results with unrelated or only tangentially linked documents.

The literal citation proxy is **not** authentic `B2 CARRIER_LINKS` as defined in Research 513. A true B2 augmentation requires *source-owned, intentionally editorial carrier-to-governing navigation* in addition to the common V03 substrate, which is not represented by arbitrary text mentions. Conversely, these results do not establish that such authored links would be beneficial, harmful, proportionate, or even materially different from common relation/lineage edges. The named B0-like and B1-like arms also lack the full shared normative relation substrate.

## Honest limits and next bounded execution decision

This incremental pilot was designed **after** observing the earlier B0/B1 results, though the new B2 proxy's extraction/ranking rule was committed to a source-neutral method file before the first B2 score. It is consequently posthoc exploratory and cannot be retrospectively described as independent prospective arm tuning or final architectural comparison. The known legacy nine scenarios, preferred B1 subject IDs, subject memberships, explicit gold-positive/distractor sets and prior 9/9 B1 score are already exposed. No fresh blind score, J1/J2 governing truth, currentness, maintenance holdout, human-evaluator result, implementation-cost parity or B3/B4 measurement is established.

The conclusion is **NOT** “B1 is the architecture winner,” “B2 editorial links fail” or “further graph navigation is inherently worse.” The conclusion is the narrow executed fact: exact-document citation-expansion of a lexical baseline under this chosen fixed algorithm showed mixed strict pass effects and worse overall retrieval metrics on one known B1-oriented historical research fixture.

A meaningful next test should resist doubling down on the same known gold. Prefer one **new fixed arm-neutral mechanically generated query/target family** or separately qualified independent retrieval/authority benchmark, with no post-result tuning, and then test actual governed B2/B3 semantics only if valid independent source-owned metadata exists. If source-authored governed concern obligations are absent, do **not** invent a B3 “win” from heuristic topical tags. A bounded, real independent query test can run without starting another C01/C02 full historical answer-closure campaign. Preserve the original Research 513 experiment and Research 559's approved prospective nine-legacy neutrality procedure.

    INCREMENTAL_B2_PROXY=EXECUTED_AND_REPRODUCIBLE
    REAL_CITATION_EDGES=110
    B0_STRICT=1_OF_9
    B1_STRICT=9_OF_9
    B2_PROXY_STRICT=2_OF_9
    B0_MICRO_RECALL=0.717949
    B2_PROXY_MICRO_RECALL=0.641026
    B2_REAL_EDITORIAL_LINK_ARM=NOT_IMPLEMENTED
    B3_REAL_SELECTIVE_CONCERN_ARM=NOT_IMPLEMENTED
    RESEARCH_513_SCORED_B0_B4=NOT_EXECUTED
    ARCHITECTURE_SELECTION=NONE
    NEXT=BOUNDED_FRESH_QUERY_GENERALIZATION_TEST_OR_GROUNDED_METADATA_PILOT
