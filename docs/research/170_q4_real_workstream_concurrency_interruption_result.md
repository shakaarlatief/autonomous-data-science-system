# Research 170: Q4 Real Workstream / Concurrency / Interruption Result

**Date:** 2026-09-14
**Status:** Q4 REAL-SOURCE STRESS SUPPORT PASSED / NON-SEMANTIC STATUS-LABEL VARIANCE PRESERVED / WHOLE-ARCHITECTURE EVIDENCE RECONCILIATION V0.3 NEXT / TARGET ARCHITECTURE NOT SELECTED
**Candidate:** `PKA-CANDIDATE-01`
**Qualification cluster:** Q4 workstream continuation / concurrency
**Fixture freeze commit:** `e1ab545f536e32c580fe7960496242f7f300db1e`
**Exact real base:** `eece72a16d9664387a67e38998ec715f8efe927e`
**Implementation collaborator:** fresh manual implementation thread using GPT-6 Astra, High reasoning
**Scope:** Preserve and evaluate the oracle-blind first Q4 implementation against the separately frozen oracle, qualify real-source multi-dependency/interruption/stale-write behavior, and route the program back to whole-architecture evidence reconciliation.
**Authority:** Shadow subsystem evidence only. Current continuity remains operational authority and no live workstream source was mutated.
**Declared references:** `research:169`, `research:168`, `research:166`, `research:144`, `checkpoint:514`

## 1. First-run preservation

The implementation collaborator created exactly two files before orchestration resumed:

```text
scripts/research/probe_candidate_01_q4_real_v01.py
RESULTS_V01.json
```

The result was preserved byte-for-byte before the oracle was evaluated:

```text
RESULTS_V01.json
FIRST_RUN_RESULTS_V01.json
SHA-256  85e9bf340c62ee9eeea860e53f4b40d3f753a5e0c83bb6c115678aa95532ac44
byte-identical  yes
implementation repairs after first run  0
oracle reads recorded by implementation  0
```

The implementation itself records execution head `e1ab545f536e32c580fe7960496242f7f300db1e`, run ordinal 1 and exclusive-create output policy.

## 2. Source and revision verification

All ten declared inputs were verified exactly:

```text
9 real sources     exact Git blobs at frozen real base
1 shadow DAG       exact frozen raw bytes
all verified       10 / 10
```

Every real tracked source is reported with:

```text
source_commit = eece72a16d9664387a67e38998ec715f8efe927e
hash_basis    = GIT_BLOB_BYTES_AT_COMMIT
```

The concurrency target uses the Research 168 explicit revision descriptor rather than an ambiguous working-tree hash.

## 3. Multi-dependency DAG result

The implementation reconstructs an acyclic workstream DAG with seven dependency edges and two genuine multi-dependency nodes.

`WS-Q4-STRESS` resolves:

```text
depends_on
    WS-Q125-INTEGRATED  COMPLETED
    WS-Q9-MIGRATION     COMPLETED

runnable  true
```

`WS-Q10-FINAL` resolves:

```text
depends_on
    WS-Q4-STRESS        ACTIVE
    WS-Q1-PORTABILITY   BLOCKED
    WS-Q2-HARD-CASES    BLOCKED

runnable  false
```

The dependency closure remains a DAG rather than being flattened into a single route or parent tree.

## 4. Interruption recovery result

The durable transition receipts reconstruct exactly:

```text
completed  S1 S2
pending    S3 S4 S5
next       S3
blind replay required  false
recovery replay count  0
```

The unrelated Cockpit diagnostic reads the real paused Cockpit resume anchor and leaves both the Q4 transition and DAG unchanged:

```text
transition_mutated  false
dag_mutated         false
anchor_matches      true
```

This is real-source interruption-recovery evidence without relying on previous-chat plan state.

## 5. Stale concurrent update result

All update attempts operate only on the exact frozen Cockpit Git blob in memory.

```text
WRITER-B-FRESH
    expected BASE
    status APPLIED
    mutation true

WRITER-A-STALE
    still expects BASE after Writer B advanced state
    status REJECTED_STALE_REVISION
    mutation false
    before hash == after hash
    stale marker absent

WRITER-C-FRESH
    expects AFTER_WRITER_B
    status APPLIED
    mutation true
```

The live tracked Cockpit file is independently hashed before and after:

```text
live worktree SHA before  59de209560fc4d49d41c5652bef7d2cfc06abf9ef9f817ae8c82bd3e49e2a89c
live worktree SHA after   59de209560fc4d49d41c5652bef7d2cfc06abf9ef9f817ae8c82bd3e49e2a89c
unchanged                 true
```

No real conflicting update was created merely for qualification.

## 6. Oracle comparison

`EVALUATION_V01.json` at SHA-256 `f29a13fd1246aaa85714932b7b2faba0d97796b54cdf13b59ebdd27b6b707cff` records:

```text
semantic checks  20 / 20 PASS
failed checks     0
Q4 support        true
```

One literal enum variance is preserved rather than repaired away:

```text
oracle label    STALE_REVISION
observed label  REJECTED_STALE_REVISION
literal match   false
semantic match  true
```

The fixture did not prescribe a result-schema enum name. The observed value is strictly more explicit while preserving the required stale-revision semantics and zero-mutation behavior. The evaluator therefore records `NON_SEMANTIC_LABEL_VARIANCE`; the first-run result is unchanged.

## 7. Verification

```text
focused Q4 tests                  9 / 9 PASS
exhaustive partitioned unit suite 291 / 291 PASS
Python compile checks             PASS
```

During the full-suite run, one older Q1/Q2/Q5 regression test proved phase-brittle after the Q4 fixture-freeze checkpoint had already been committed: it expected `current_authority_unchanged=false` merely because current-state publication had once been uncommitted. The regression was corrected to test the durable invariant instead: current authority remains unchanged relative to the clean committed HEAD, while only the capture auto-promotion check is expected to change after promotion. This is test-maintenance evidence, not a Q4 implementation repair.

The Q4 evaluator script also required one syntax-only repair before its first successful evaluation invocation. No Q4 result value or implementation behavior was changed after oracle inspection.

## 8. Evidence disposition

The Q4 result adds real-source evidence for:

```text
KA-R27  multiple dependencies
KA-R28  interruption recovery
KA-R29  concurrent collaborator safety
```

Combined with prior real support for active-route reconstruction, workstream identity/state, pause/return semantics and KA-I09, Q4 now has real subsystem evidence on every cluster item.

Updated descriptive coverage:

```text
real-evidence items                61 / 67
synthetic-or-better items          63 / 67
full-real subsystem clusters       Q3 Q4 Q5 Q6 Q7 Q8 Q9
mixed-gap clusters                 Q1 Q2
final governing cluster            Q10
final qualified passes              0 / 67
```

## 9. What remains after Q4

Only six frozen items lack real Candidate 01 evidence:

```text
Q1   KA-R36  provider and tool portability
Q2   KA-R14  supersession/supplementation/conflict visibility
Q2   KA-R24  probabilistic retrieval is not sole governing authority
Q10  KA-R30  bounded qualification budgets
Q10  KA-R40  structural + behavioral qualification
Q10  KA-R41  multidimensional reconstruction qualification
```

The exact implementation model is now preserved for this Q4 run, but it remains another OpenAI-family execution. That does not by itself establish provider portability and no KA-R36 credit is claimed here.

Because the evidence field has changed substantially again, the next step is a fresh whole-architecture reconciliation before choosing whether Q1/Q2 should be closed in one integrated pre-Q10 challenge or separately.

```text
RESEARCH170=Q4_REAL_SOURCE_STRESS_SUPPORT_PASS
FIRST_RUN_PRESERVED=true
SEMANTIC_ORACLE_CHECKS=20_OF_20
NON_SEMANTIC_LABEL_VARIANCE=1
Q4_FULL_REAL_SUBSYSTEM_SUPPORT=true
REAL_EVIDENCE_ITEMS=61_OF_67
FINAL_QUALIFIED_PASSES=0
TARGET_ARCHITECTURE=NOT_SELECTED
NEXT=WHOLE_ARCHITECTURE_EVIDENCE_RECONCILIATION_V03
```
