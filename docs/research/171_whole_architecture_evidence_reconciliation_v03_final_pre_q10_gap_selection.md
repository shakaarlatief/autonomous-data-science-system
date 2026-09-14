# Research 171: Whole-Architecture Evidence Reconciliation V0.3 and Final Pre-Q10 Gap Selection

**Date:** 2026-09-14
**Status:** WHOLE-ARCHITECTURE EVIDENCE RECONCILED AFTER Q4 / THREE PRE-Q10 REAL-EVIDENCE GAPS REMAIN / CROSS-PROVIDER Q1+Q2 CHALLENGE NEXT / TARGET ARCHITECTURE NOT SELECTED
**Candidate:** `PKA-CANDIDATE-01`
**Scope:** Recompute all 67 frozen requirements/invariants after Research 170 and select the smallest remaining pre-Q10 falsification before the final governing qualification program.
**Authority:** Qualification-planning evidence only. No final KA-R/KA-I pass or architecture selection is granted by this audit.
**Machine audit:** `docs/research/project_knowledge_candidate_01/WHOLE_ARCHITECTURE_EVIDENCE_RECONCILIATION_V03.json` at SHA-256 `3e8df6195ab0082cc0a3e355361ec6fb4fe7d885b29115037214adc41c367b64`
**Source matrix SHA-256:** `a087b2724aa90eed06813cd2372f6e3988d797bd6a5415b0cdd0f2dfd0963bd1`
**Declared references:** `research:170`, `research:168`, `research:166`, `research:145`, `checkpoint:515`

## 1. Updated evidence distribution

```text
REAL          61 / 67
SYNTHETIC      2 / 67
DESIGN_ONLY    4 / 67
-------------------
TOTAL         67 / 67

synthetic-or-better  63 / 67
final qualified       0 / 67
```

This remains an evidence-strength audit, not a requirement-pass ledger.

## 2. Cluster maturity

Seven clusters now have real Candidate 01 subsystem evidence on every item:

```text
Q3 identity / relationship / temporal semantics
Q4 workstream continuation / concurrency
Q5 capture / promotion / consolidation
Q6 derived views / freshness / multi-axis projection
Q7 public/private boundary / degraded mode
Q8 scaling / maintenance economics
Q9 migration / authority switch / self-hosting
```

The only pre-Q10 gaps are now concentrated in Q1 and Q2.

### Q1

```text
10 real
1 design-only
missing real evidence: KA-R36 provider and tool portability
```

The recent manual fresh collaborator runs demonstrate conversation independence and cross-tool execution, but they remain OpenAI-family runs. They are not promoted into provider-portability evidence.

### Q2

```text
7 real
2 synthetic-only
missing real evidence:
    KA-R14 supersession / supplementation / conflict visibility
    KA-R24 probabilistic retrieval is not sole governing authority
```

These two gaps interact naturally: the hard case is not merely retrieving a plausible source, but refusing to let retrieval silently choose authority when source relationships conflict, supplement or supersede one another.

### Q10

```text
0 real
3 design-only
KA-R30 bounded qualification budgets
KA-R40 structural and behavioral qualification
KA-R41 multidimensional reconstruction qualification
```

Q10 remains the final governing program and should run only after the three pre-Q10 gaps above receive real evidence.

## 3. Next experiment

The smallest useful next challenge combines KA-R36, KA-R14 and KA-R24 in one controlled external-provider run.

A capable non-OpenAI collaborator should receive only project-controlled Candidate 01 successor surfaces plus a bounded evidence corpus. The task should contain:

```text
1. one probabilistic/search-style nomination that points to a plausible but non-governing source;
2. one explicit REPLACE/SUPPLEMENT/SPECIALIZE/CORRECT relationship;
3. one conflict or ambiguity that must remain fail-visible unless authority is actually resolvable;
4. exact source revisions and a deterministic authority receipt;
5. no prior ADS conversation context;
6. a fixed read/context budget measured for later Q10 use.
```

The collaborator must reconstruct the same governing result from repository-controlled semantics, not from provider-specific memory or hidden tooling.

## 4. Why this is the final pre-Q10 falsification

If a controlled external-provider run passes, every non-Q10 item will have some real Candidate 01 evidence. At that point Q10 can become a true final governing program rather than a wrapper around known untested mechanisms.

If it fails because Candidate 01 semantics are provider-fragile, retrieval-dependent, or unable to resolve/contain authority conflict, that is architecture-level evidence and selection must remain blocked.

## 5. Architecture-family disposition

Nothing in Q4 changes the H3/Object-Primary conclusion. Candidate 01 continues to handle real identity, migration, public/private, workstream/concurrency and capture/promotion cases without a general central object registry.

```text
H3_REOPEN=NO
TARGET_ARCHITECTURE=NOT_SELECTED
FINAL_QUALIFIED_PASSES=0
```

## 6. Updated sequence

```text
NOW
    Q1 + Q2 controlled non-OpenAI provider authority-hard-case challenge

THEN
    Q10 final multidimensional qualification program

ONLY AFTER Q10
    architecture selection / owner acceptance / authority-switch decision
```

```text
RESEARCH171=WHOLE_ARCH_EVIDENCE_V03_RECONCILED
REAL_EVIDENCE_ITEMS=61_OF_67
PRE_Q10_REAL_GAPS=3
PRE_Q10_GAPS=KA-R36,KA-R14,KA-R24
FINAL_GOVERNING_CLUSTER=Q10
TARGET_ARCHITECTURE=NOT_SELECTED
NEXT=Q1_Q2_CROSS_PROVIDER_AUTHORITY_HARD_CASE_CHALLENGE
```
