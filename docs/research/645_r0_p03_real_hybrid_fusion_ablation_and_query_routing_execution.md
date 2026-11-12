# Research 645: Executed hybrid retrieval, ablations, and query-only routing

**Date:** 2026-11-12
**Status:** REAL_EIGHT_STRATEGY_HYBRID_PILOT_EXECUTED / TITLE_FUSION_GAIN_AND_TOPIC_LOSS / NO_FORMAL_ARCHITECTURE_SELECTION
**Scope:** Record a real two-query-family experiment with pure B0/B1/B2-proxy arms, pairwise RRF, three-way RRF, and an exact-title query switch. Preserve all unfavorable and favorable outcomes, retrieval-pool costs, and formal R0-P03 inference limits.
**Authority:** Owner's explicit execution-first direction, frozen `EXPLORATORY_HYBRID_FUSION_AND_QUERY_ROUTING_CONTRACT_V01.md`, actual 642,735-byte executed trace, Research 642-644, prior Claude criticism reconciled in Research 559, unchanged Research 513/576.
**Checkpoint:** 908. **Specification:** 028 unchanged. **Interaction:** ChatGPT / chatgpt-42.

## 1. Executed test, not a proposed comparison

Ran `experiments/r0_p03_navigation_probe/exploratory_hybrid_fusion_and_routing_v01.py --output` on the exact original **65 historical Git UTF-8 documents** at `4b94ffe183ff7af72cef6ee7492b4ba2f30c11ef`, SHA-256 corpus fingerprint `01206bdb2fdc3517627a94bdf6587efaa2f5d9ed10ad220f5799c496353c5a09`. Exact-byte predecessor output hashes from Checkpoints 905/906/907 were reauthenticated; all old nine-task B0 and B2 ranked paths, and all 65 source-heading task B0, B1, B2 ranked paths, matched their original saved traces **before new hybrid evaluation**.

Fixed actual output:

    FILE=experiments/r0_p03_navigation_probe/exploratory_hybrid_fusion_and_routing_result_v01.json
    BYTES=642735
    SHA256=e07bcf10e4f04cbde6cbd08b33fb77c02ca17efa03d1a4dbffb73c7a9439334f

Two distinct task families were evaluated with deliberately **separate metric definitions**:

1. Nine already-known **W5 B1-authored topical scenarios** with the original `must_retrieve` / explicit `must_not_retrieve` source lists, micro recall and strict all-positives/no-explicit-negatives pass.
2. Sixty-five previously executed **mechanical first-H1 source document locator queries**, each self-targeted to the file whose heading supplied its words; score hit@1, hit@10 and MRR@10, not answer correctness.

All methods get the same query text and same source bytes. On both families the standalone B1 treatment must *infer the topic from query text* through the prior fixed, deterministic subject-label/description matcher; **no hidden scenario subject identifier is supplied**. This differs materially from the original B1 9/9 pilot, where the correct subject was supplied and the returned list contained fewer carriers.

Actual mechanisms and combinations:

    B0                           common full-text lexical FTS5 BM25 proxy
    B1                           existing authored subject membership and inferred query topic
    B2                           literal source-path citation expansion proxy, NOT editorial governed B2
    fusion_b0_b1                 unweighted reciprocal rank fusion
    fusion_b0_b2                 same RRF
    fusion_b1_b2                 same RRF
    fusion_all                   same RRF across three sources
    router                       exact first-H1 title => B0; otherwise B0+B1 RRF

RRF strength fixed **K=60** before this run, with at most ten candidates from each participating mechanism, a lexical-rank/path deterministic tie, and at most ten final source outputs. The router only sees normalized query strings and the same 65-document title index. No gold labels or old scenario IDs can enter ranker calls. **Fusion candidates are not cost-equivalent**: up to 20-30 unique upstream candidates may be ranked before producing the same final ten.

## 2. Real separate nine-task topical results

| Actually executed mechanism | Strict complete PASS/9 | Relevant source hits/39 | Micro recall@10 | Known distractor intrusions | Upstream unique candidate slots across queries |
| --- | ---: | ---: | ---: | ---: | ---: |
| B0 lexical | 1 | 28 | 0.717949 | 4 | 90 |
| B1 inferred subject | **6** | **39** | **1.000000** | 3 | 90 |
| B2 literal citation | 2 | 25 | 0.641026 | 6 | 90 |
| B0+B1 RRF | 4 | 37 | 0.948718 | 3 | 109 |
| B0+B2 RRF | 1 | 27 | 0.692308 | 4 | 113 |
| B1+B2 RRF | 4 | 37 | 0.948718 | 4 | 120 |
| B0+B1+B2 RRF | 4 | 36 | 0.923077 | 3 | 131 |
| Exact-title/B0+B1 router | 4 | 37 | 0.948718 | 3 | 109 |

**Important shift from the earlier legacy B1 9/9:** With inferred rather than supplied subjects, all 39 B1-positive source instances still occur within top ten, but the ten-carrier filled list contains **three explicitly labeled distractor intrusions**, reducing strict passes to 6/9. The earlier 9/9 is not overwritten or recast as a current independent score. For the current fixed 6/9 B1-inferred outcome, B0+B1 RRF yields **no new complete scenario passes and loses two**; this is a legitimate negative fusion result, not an implementation defect to tune away.

The baseline original labels were authored by B1's research author and are not arm-neutral evidence. The original nine tasks are *not* Research 559's independently re-adjudicated new legacy gold. No official `>=8/9` gate is therefore applied.

## 3. Real separate 65-title source-location results

| Mechanism | Hit@1/65 | Hit@10/65 | MRR@10 | Upstream unique candidate slots across queries |
| --- | ---: | ---: | ---: | ---: |
| B0 lexical | 45 | 64 | 0.803590 | 650 |
| B1 inferred subject | 33 | 63 | 0.653590 | 650 |
| B2 literal citation | 45 | 64 | 0.802949 | 650 |
| **B0+B1 RRF** | **47** | **64** | **0.834359** | 805 |
| B0+B2 RRF | 45 | 64 | 0.803223 | 875 |
| B1+B2 RRF | 47 | 64 | 0.832198 | 921 |
| B0+B1+B2 RRF | 43 | 64 | 0.797582 | 1016 |
| Exact-title/B0+B1 router | 45 | 64 | 0.803590 | 650 |

The **B0+B1 fusion** improves four individual first-rank correct-source queries relative to B0 but worsens two, giving a net **+2 hit@1** and higher MRR@10; the top-ten hit count remains 64. Relative to B1 alone, it improves fourteen first-place cases and worsens none. Its candidate pool rises from 650 to **805 total per-query unique candidate instances** (+155, ~24%); this is a diagnostic union, *not* measured elapsed time or distinct physical source reads.

Adding B2 to B0+B1 yields **no improved first-rank correct cases and four regressed cases**, dropping hit@1 to 43 and MRR@10 to 0.797582, with **1016** upstream unique-candidate instances (~56% greater than B0 alone). The broad triple combination does **not** outperform the targeted pairwise fusion in this sample.

## 4. Adaptive router is a control, not validated intelligence

The query-only exact-title router took **B0 for all 65** H1-derived document-location queries and **B0+B1 fusion for all nine** old topical-label queries. Its measured outcomes are exactly those branch baselines. It has no demonstrated ability to distinguish authentic open-ended user intents, ambiguous titles or historical evidence requirements. First-H1 normalization comes from a source-derived title index, not the reference answer path; nevertheless, the exact-title stress sample is transparently favorable to this switch. Do not call this a general-purpose learned intent router or recommend it as the governing architecture from these observations.

## 5. Engineering implications and scientific constraints

This is an actual expanded live pilot with **eight** mechanisms/strategies and clear pure-arm ablation controls. Evidence supports **conditional complementarity**, not a single absolute winner:

- A fixed pairwise lexical+subject fusion improves location ranking on content-derived exact-title queries, but can dilute complete topical coverage.
- Naively fusing source-path links into a broader pool is not inherently beneficial and can displace relevant sources.
- Subject taxonomy can be effective for topical exploration yet sensitive to routing, available labels and extra distractors.
- A title/intent decision may be useful, but needs task-independent validation before claims of adaptive generalization.

All inputs were previously examined in the ongoing research and the combined design was authored **after** the old B0/B1/B2 results. Old topical gold remains B1-authored; H1 self-targets favor lexical. This is an **exploratory posthoc follow-up**, not a new prospective blind experiment. B0 lacks the complete common governing V03 substrate, the B2 treatment is a literal path proxy not actual source-owned editorial links, B3 governed selective concerns and B4 semantic/embedding retrieval do not exist here. Equal ten returned slots do not equalize candidate lookups, metadata labor, latency, cost, authority/citation correctness, maintenance burden or answer synthesis. The original full twelve-primary/independently neutralized nine-legacy Research 513/559/576 test remains unscored, with original C01/C02 holds intact.

**Next bounded engineering unit:** test combinations and query routing on genuinely new tasks or a held-out query-generation method with explicit source/authority controls, rather than tuning RRF weights or classifier thresholds on the already exposed 74 queries. Seek authentic governed concern/link source declarations before implementing claimed B2/B3 arms. Do not use these pilot results to choose a physical target.

    EXECUTED_HYBRID_STRATEGIES=8
    TWO_TASK_FAMILIES=9_PREVIOUSLY_KNOWN_AND_65_SOURCE_HEADING
    SOURCE_FILES=65_EXACT_GIT_OBJECTS
    LEXICAL_SUBJECT_RRF_HEADING_HIT1=47_OF_65
    LEXICAL_SUBJECT_RRF_HEADING_MRR=0.834359
    INFERRED_SUBJECT_TOPICAL_STRICT=6_OF_9
    LEXICAL_SUBJECT_RRF_TOPICAL_STRICT=4_OF_9
    ROUTER_EXACT_TITLE_BRANCH_65=65
    ROUTER_FUSION_BRANCH_9=9
    PROSPECTIVE_BLIND_GENERALIZATION=NOT_ESTABLISHED
    FORMAL_B0_B4_SCORING=NOT_EXECUTED
    SOURCE_ADMISSIONS=NONE
    ARCHITECTURE_SELECTION=NONE
    NEXT=FRESH_TASK_GENERALIZATION_AND_SEMANTICALLY_VALID_LINK_CONCERN_MECHANISMS
