# Execution-first historical B2-like source-citation traversal proxy, frozen pilot V01

**Date:** 2026-11-12
**Status:** SOURCE-LINK-RANKING_AND_NO_TUNING_RULE_FROZEN_PRE_EXECUTION / EXPLORATORY_ONLY
**Purpose:** Add an actual executable **source-link mechanism** to the already executed B0-like/B1-like retrieval comparison instead of preparing hypothetical architectural arms indefinitely.

## Inputs and mechanism

Read exactly the same nine old W5-T1-V02 scenarios, 65 historical source document bytes, and historical `4b94ffe183ff7af72cef6ee7492b4ba2f30c11ef` Git revision as the real V01 comparison. Use exactly the prior published subject-label natural-language query for each scenario, SQLite FTS5 unicode61 OR tokenization and deterministic BM25 ranking. Verify the first ten baseline paths match V01 output byte-for-byte for every scenario.

**B2-like source-citation traversal proxy**, additional to B0:

1. The only additional source signal is a literal `docs/.../*.md` or `docs/.../*.json` path reference found in a historical 65-document source body and pointing to another member of the same 65-document corpus. A path mention is a navigation edge, NOT proof of editorial curation, truth, adoption, authority, accepted dependency, source release or a declared semantic relation.
2. Start with the **first five** baseline BM25 results as fixed seeds.
3. Follow outgoing directed reference edges one hop from each seed. Rank unique candidate targets by **descending number of seed documents citing the target**, then by the original full-corpus BM25 position (nonmatching targets after matching targets), then by stable path.
4. Append candidates until ten results in total. Fill any remaining slots with unchanged subsequent B0 BM25 candidates. Never duplicate a source; no recursive graph walk.
5. Do not use `must_retrieve`, `must_not_retrieve`, B1 membership, C01/C02 protected questions, Research 217 answers or result feedback to author the link edges, their ranking, or the stopping rule.

Compare B2-like proxy against the previous frozen B0-like baseline and B1-like existing authored subject-index treatment on the same nine fixed **already-known** research gold sets. Record strict all-required/no-known-distractor pass, micro and macro recall@10, explicit negative intrusions, total returned document slots, graph edge count and per-scenario paths. Run once; no parameter tuning after any result. Recompute one additional complete pass for deterministic exactness.

## Strict scientific boundaries

This is a **post-B0/B1 pilot incremental exploratory arm**, so it has known baseline outcomes and cannot be considered independently preregistered or blind. The nine original scenarios are B1-authored and strongly favor B1 by construction; prior research explicitly identified this. No observed B0/B1 or new B2 proxy result may be promoted to Research 513 formal P03 12-primary and independently re-adjudicated nine-legacy scoring.

The proxy uses literal source mentions, NOT the **B2 CARRIER_LINKS** actual source-owned carrier-to-governing editorial navigation semantics. Do not call it a validated B2 arm. The V03-native shared governing relation substrate, semantic source authority, historical execution evidence, corpus admission, independent gold and equal implementation/metadata authoring costs remain unqualified. No B3 governed selective concerns and no B4 semantic retrieval are implemented or claimed in this unit.

Any improvement, regression, or tie is retained as observed. If executable issues arise, correct only mechanical defects without changing the frozen graph expansion policy, and document actual changes. Do not modify the older 18,712-byte executed pilot result, subject fixture, original current protocol, or protected private reports.

    INPUT=OLD_W5_V02_65_CARRIERS_NINE_SCENARIOS
    B0_FROZEN_RESULT_SHA256=498bb12d906639642da943e8366194ec8b0c7f6817d20ae5b8fa89a43f8a2acb
    FIRST_SEEDS=5
    LINK_HOPS=1
    RETURN_LIMIT=10
    B2_ACTUAL_GOVERNING_CARRIER_LINKS=NOT_IMPLEMENTED
    B3_ACTUAL_SELECTIVE_CONCERNS=NOT_IMPLEMENTED
    SCORING=EXPLORATORY_NAVIGATION_ONLY
