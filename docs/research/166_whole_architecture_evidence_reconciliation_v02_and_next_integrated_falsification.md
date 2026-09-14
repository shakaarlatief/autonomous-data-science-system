# Research 166: Whole-Architecture Evidence Reconciliation V0.2 and Next Integrated Falsification

**Date:** 2026-09-14
**Status:** WHOLE-ARCHITECTURE EVIDENCE RECONCILED AFTER Q3/Q7/Q9 / NEXT INTEGRATED Q1+Q2+Q5 CHALLENGE SELECTED / TARGET ARCHITECTURE NOT SELECTED
**Candidate:** `PKA-CANDIDATE-01`
**Scope:** Reconcile all Candidate 01 evidence through Research 165 across all 67 frozen requirements/invariants, update cluster maturity after the Q3/Q7/Q9 real/shadow programs, and select the next architecture-level falsification by remaining uncertainty rather than legacy-file sequence.
**Authority:** Qualification-planning evidence only. Requirements V0.2 remain frozen; no final KA-R/KA-I pass or architecture selection is granted by this audit.
**Machine audit:** `docs/research/project_knowledge_candidate_01/WHOLE_ARCHITECTURE_EVIDENCE_RECONCILIATION_V02.json` at SHA-256 `ce1fe5f6f4dd630b2820a05ae961a8df6035d2283f7af8ca25c68169cd099c60`
**Source matrix SHA-256:** `fbc81876d5be589ea97caebae3565e23b078cd9b82b2a30376925e01edec90c7`
**Declared references:** `research:159`, `research:161`, `research:163`, `research:165`, `research:145`, `path:docs/research/PROJECT_KNOWLEDGE_ARCHITECTURE_REQUIREMENTS_V02.md`, `path:docs/research/project_knowledge_candidate_01/QUALIFICATION_MATRIX_V01.json`, `checkpoint:510`

## 1. Why V0.2 is necessary

Research 159 was the correct whole-architecture audit at its boundary, but three of its four immediate P0 architecture falsification targets have now been executed:

```text
Q3 real identity / relationship / temporal semantics   PASS at subsystem level
Q7 real public/private boundary                        PASS at subsystem level
Q9 migration / rollback shadow                         PASS at subsystem level
Q10 final governing qualification program              not yet executed
```

Continuing to follow Research 159's old priority ordering without recomputation would therefore be stale.

## 2. Updated evidence distribution

The V0.2 machine audit derives evidence directly from the current qualification matrix and normalizes each item to its strongest descriptive tier:

```text
DESIGN_ONLY     9
SYNTHETIC       9
REAL           49
---------------
TOTAL          67

synthetic-or-better   58 / 67
real evidence         49 / 67
final qualified        0 / 67
```

These remain evidence-strength descriptors, not requirement-pass states.

## 3. Cluster maturity after Q3/Q7/Q9

### Q1 bootstrap / reconstruction / discovery

```text
8 real
0 synthetic-only
3 design-only
```

Remaining gaps are concentrated rather than broad: real high-recall governing/risk discovery, provider/model/tool portability and integrated proof that durable repository authority outranks transient conversation memory. A bounded cold-start budget must also be established as part of the eventual Q10 gate.

### Q2 authority resolution / action-contract fidelity

```text
3 real
5 synthetic-only
1 design-only
```

This is the highest-consequence mixed cluster. Real evidence exists for a seeded authority/action path, but known-risk/reopen-trigger activation remains design-only and missing/conflicting authority plus several fail-closed behaviors remain synthetic.

### Q3 identity / relationship / temporal semantics

```text
5 real / 5 total
```

Every Q3 cluster item now has real Candidate 01 subsystem evidence. This does not erase the explicit residual limitation: real `MERGE`, `SPLIT` and `TOMBSTONE` transition cases are still absent. Q3 is therefore strong subsystem evidence, not a final cluster pass. H3/Object-Primary remains not reopened.

### Q4 workstream continuation / concurrency

```text
4 real
3 synthetic-only
0 design-only
```

The remaining three gaps are cleanly defined: real multi-dependency DAG behavior, interruption recovery and stale concurrent authoritative-update rejection.

### Q5 capture / promotion / consolidation fidelity

```text
7 real
1 synthetic-only
2 design-only
```

The major remaining gap is no longer consolidation mechanics. It is the lifecycle from fresh reasoning to durable accepted knowledge: persistent project understanding, conversation/model independence and a real capture -> consolidation -> explicit promotion path.

### Q6 derived views / freshness / multi-axis projection

```text
4 real / 4 total
```

Strong real subsystem support. Remaining work is integrated confirmation, especially deletion/rebuild and concurrent freshness.

### Q7 public/private boundary / degraded mode

```text
6 real / 6 total
```

Research 163 converts the entire cluster from synthetic-only to real cross-repository subsystem support, including a genuine stale-private `FAIL` and zero private-value/path leakage.

### Q8 scaling / maintenance economics

```text
6 real / 6 total
```

Strong real subsystem support remains. Sustained-use consolidation economics still need integrated confirmation.

### Q9 migration / authority switch / self-hosting evolution

```text
6 real / 6 total
```

Research 165 converts the full cluster to real-base shadow support: migration parity, compatibility-path preservation, rollback export, fail-closed switch gating and self-hosted migration all pass. An actual authority switch cannot and should not be attempted before full qualification, target selection and owner acceptance.

### Q10 qualification methodology / budgets

```text
0 real
0 synthetic
3 design-only
```

Q10 remains the final governing program. It should not be executed prematurely as a ceremonial wrapper around known Q1/Q2/Q4/Q5 gaps. Those gaps should first be reduced with the highest-value integrated experiments.

## 4. What the evidence now says about Candidate 01

The evidence is no longer consistent with describing Candidate 01 as merely a promising document-oriented design. Five full clusters now have real evidence on every item:

```text
Q3 identity / relationship / temporal
Q6 derived views
Q7 public/private boundary
Q8 scaling / maintenance
Q9 migration / rollback / self-hosting
```

The successful Q3 and Q9 probes are especially important for the architecture-family question. Candidate 01 handled real identity/temporal cases and a real-base migration slice without forcing a general object registry, a central relation spine or dual authority. Nothing in the new evidence justifies reopening H3/Object-Primary now.

At the same time, target selection remains premature because the weak areas are precisely those that determine whether the architecture works **as a cognitive/operational system**, not merely as a representation:

```text
fresh collaborator reconstruction
relevant governing/risk discovery
consequential authority activation
fail-visible missing/conflicting authority
capture -> promotion into durable accepted understanding
real multi-workstream/concurrency recovery
final bounded qualification budgets
```

## 5. Next falsification: integrate Q1 + Q2 + Q5

The next experiment should not test one more metadata mechanism in isolation. It should combine the three mutually dependent capabilities that define successful knowledge use:

```text
Q1
    fresh successor-native reconstruction / discovery

Q2
    consequential authority resolution / known-risk activation / action contract

Q5
    capture of new reasoning -> candidate consolidation -> explicit promotion boundary
```

The key question becomes:

> Can a fresh collaborator start from bounded successor-native surfaces, discover and activate the right governing/risk knowledge for a consequential task, produce a traceable decision/receipt, and preserve genuinely new accepted understanding through an explicit promotion step without relying on the previous conversation or on legacy global current-state truth?

This single integrated challenge is higher-value than separately probing R01, R03, R07, R10 and R22 because those properties interact in actual use.

## 6. Required qualities of the next challenge

The fixture should be frozen before implementation and should include at least:

```text
1. a bounded successor-native bootstrap/current-state packet;
2. a real consequential ADS authority task with a known-risk/reopen trigger;
3. at least one plausible but non-governing distractor;
4. an explicit missing/conflict or stale-authority condition that must fail visibly;
5. a capture artifact containing new reasoning that begins non-authoritative;
6. a promotion gate that can create accepted durable knowledge only after explicit checks;
7. a reconstruction/authority receipt binding exact source revisions and activated constraints;
8. no dependence on the previous chat;
9. measured read/context budget and source-touch count for later Q10 use;
10. no silent promotion merely because information was captured, summarized or repeatedly retrieved.
```

Provider/model portability should be designed into the representation and later exercised with an independent capable collaborator when that adds genuine evidence; it should not be faked by a single-model label.

## 7. Updated priority order

```text
P0 NOW
    Q1 + Q2 + Q5 integrated cold continuation / authority / capture-promotion

P1
    Q4 real multi-dependency / interruption / stale-write stress

P0 FINAL GOVERNING PROGRAM
    Q10 integrated budgets + structural/behavioral multidimensional qualification

P2 INTEGRATED CONFIRMATION
    Q3 Q6 Q7 Q8 Q9 residual/integration checks
```

If the integrated Q1/Q2/Q5 challenge exposes a representation defect that Candidate 01 can only solve through proliferating central machinery or unbounded special cases, architecture-family reopening remains allowed.

## 8. Selection disposition

```text
TARGET_ARCHITECTURE=NOT_SELECTED
FINAL_QUALIFIED_PASSES=0
H3_REOPEN=NO
STRONG_REAL_SUBSYSTEM_CLUSTERS=Q3,Q6,Q7,Q8,Q9
MIXED_GAP_CLUSTERS=Q1,Q2,Q4,Q5
FINAL_GOVERNING_CLUSTER=Q10
NEXT=Q1_Q2_Q5_INTEGRATED_COLD_CONTINUATION_AUTHORITY_CAPTURE_PROMOTION
```
