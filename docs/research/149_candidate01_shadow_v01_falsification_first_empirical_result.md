# Research 149: Candidate 01 Shadow V0.1 Falsification-First Empirical Result

**Date:** 2026-09-14
**Status:** FIRST SHADOW SLICE PASSED FROZEN ORACLE ON FIRST RUN / FOUNDATIONAL MECHANISMS SUPPORTED / BROADER QUALIFICATION STILL PENDING / TARGET ARCHITECTURE NOT SELECTED
**Candidate:** `PKA-CANDIDATE-01`
**Scope:** Implement and execute the exact Research 148 frozen fixture without changing fixture/oracle bytes, preserve the first raw run, compare behavior against the separate oracle, and decide whether Candidate 01 survives the first stop/reopen gate.
**Authority:** Narrow synthetic prototype evidence only. This does not select Candidate 01, migrate authority, or qualify all Requirements V0.2 statements.
**Declared references:** `research:147`, `research:148`, `research:144`, `path:docs/research/project_knowledge_candidate_01_shadow_v01/SHADOW_FIXTURE_V01.json`, `path:docs/research/project_knowledge_candidate_01_shadow_v01/SHADOW_ORACLE_V01.json`, `checkpoint:493`

## 1. Anti-treatment-bias provenance

The exact fixture and oracle were committed and pushed before prototype code existed.

```text
freeze commit       8ccefd17e229ee5a484c4481ed005290efc0282e
fixture SHA-256     77ffecc278995ef03130d962f863d46ccebac41d446de7099cc666750e8b66f7
oracle SHA-256      3ced74eb18f4d792c9a43eaf2b3d6956c497bc7b85c71bfc6b5e226f840fc38b
```

The implementation hard-codes only the fixture hash. It contains no `SHADOW_ORACLE`/`ORACLE_V01` reference and does not read the oracle. Tests read the oracle separately.

The first executable run was preserved at:

```text
docs/research/project_knowledge_candidate_01_shadow_v01/FIRST_RUN_RESULTS_V01.json
```

The later canonical raw result is:

```text
docs/research/project_knowledge_candidate_01_shadow_v01/RESULTS_V01.json
```

Both are byte-identical:

```text
bytes       5715
SHA-256     b4498e20d2f4984d938e6e6e32e9a34d7e4706ad17daf010d0ab6f7eb162ebd1
first-run repair before pass    none
```

This matters because no semantic failure was hidden by changing the implementation after seeing a failing first run.

## 2. Implementation boundary

Prototype code:

```text
scripts/research/project_knowledge_candidate01_shadow_v01.py
```

Focused tests:

```text
tests/unit/test_project_knowledge_candidate01_shadow_v01.py
```

The implementation uses only four candidate profile concepts:

```text
GOVERNING_PROCEDURE
JOINT_AUTHORITY_DECLARATION
IDENTITY_TRANSITION
DERIVED_VIEW_MANIFEST
```

It does not implement workstreams, capture/promotion, private delegation, migration, full current-state narrative, semantic retrieval or production storage syntax.

## 3. F1 result: one normative action-contract home + drift review

Baseline P1 has no findings.

Frozen mutation 1 introduces prose assertion `C07` without a corresponding structured normative constraint. The validator returns:

```text
PROSE_CONTRACT_MISSING_NORMATIVE_CONSTRAINT / C07
```

Frozen mutation 2 changes the prose-side semantic assertion for `C03` while leaving the structured contract unchanged. The validator returns:

```text
PROSE_CONTRACT_SEMANTIC_MISMATCH / C03
```

The prototype therefore demonstrates the intended architecture behavior:

```text
structured contract remains the normative home
prose drift becomes a review finding
validator does not rewrite the normative contract from prose
```

### Limitation

The fixture provides deterministic `prose_assertions` as a stand-in for semantic extraction from natural language. This is **not** evidence that production natural-language drift detection is solved. It isolates the governance mechanism after a semantic discrepancy has been detected.

## 4. F2 result: natural direction versus irreducible joint authority

### Ordinary supplement

```text
P1 + P2
natural relation       P2 SUPPLEMENT -> P1
joint objects created  0
natural owner          P2
```

### Directional near-miss

```text
N1 + N2
natural relation       N2 SPECIALIZE -> N1
admission               SOURCE_OWNED_DERIVED_CLOSURE
joint objects created  0
```

The near-miss has a completed review receipt, so the result cannot be explained by absence of a review event. J2 fails because a natural semantic direction already exists.

### Symmetric positive case

```text
X1 + X2 + X3
semantic roles          peer / peer / peer
directional edges       none
non-redundant content   yes
irreducible set facts   all-members-required + set-level effective/conflict facts
review receipt          present
J1..J6                  all true
admission               JOINT_AUTHORITY_ADMITTED
joint objects created  1
```

The implementation reads semantic facts and relations, not an expected class flag.

### Interpretation

This is the first executable support for the final MC-0016 J2/J3 rule: **natural directional ownership stays source-local; irreducible symmetric set-level authority may earn first-class representation.**

### Limitation

The positive case is synthetic. The prototype uses an explicit bounded vocabulary of irreducible set-level fact types and deterministic symmetry evidence. It demonstrates that the rule can be implemented without reading its own expected label; it does not prove that every real repository case can be classified automatically or without review.

## 5. F3 result: BL-001-style action-contract fidelity

The authority resolver activates six constraints from P1 + P2 in this order:

```text
C01 C02 C03 C06 C04 C05
```

`BL1-GOOD` passes.

`BL1-BAD` emits:

```text
C02 C01 C03 C06 C05
```

The checker fails visibly with:

```text
omitted           C04
order violations  C01, C02
status            FAIL_VISIBLE
```

This is narrow but important evidence that source activation plus stable constraint IDs can prevent the exact class of "source was read but mandatory contract was lost" failure exposed by BL-001.

### Limitation

The attempted output is already represented as emitted constraint IDs. This proves deterministic contract-plan fidelity, not free-form natural-language semantic equivalence. The later high-consequence free-form verifier remains unqualified.

## 6. F4 result: dependency-local refresh versus full rebuild

Frozen change:

```text
CHANGE-P2-CONTRACT
changed authoritative source   P2
```

Incremental result:

```text
authoritative source scans     1
refreshed generated views      AUTHORITY_CURRENT, CONTRACT_CURRENT
IDENTITY_CURRENT refreshed     no
```

Full rebuild source-record scans under passive identity history growth:

```text
20 records   -> 31 total source/event records scanned
100 records  -> 111
200 records  -> 211
```

The current-view digest is identical at all three scales:

```text
3e7d482d673d6f600d46c25b5dceb892e2c2987e459124f49d7e70cdf886fe48
```

Interpretation:

```text
routine local refresh can remain dependency-local
periodic clean rebuild remains history-proportional
passive historical growth does not change current semantic view output
```

This directly supports the Research 146 calibration that KA-R31/KA-I12 concern required reconstruction rather than requiring globally sublinear repair/rebuild.

### Limitation

One change topology and three small view manifests are not enough to establish repository-wide marginal maintenance economics. The dependency graph itself is still synthetic and compact.

## 7. F5 result: identity history versus bounded current lookup

Identity event records processed during clean rebuild:

```text
1x   24
5x  104
10x 204
```

Normal lookup of historical semantic identity `S-M` uses the precomputed current-target index and takes exactly one index lookup at all scales. The current targets are:

```text
S-M -> S-A, S-B1, S-B2
```

Other frozen current resolutions include:

```text
S-A -> S-A
S-B -> S-B1, S-B2
S-C -> S-C
```

The generated current identity index has six entries and the final current carrier set remains four carriers at every scale.

Interpretation:

> Complete transition history may grow while ordinary semantic-identity resolution stays on a bounded current index rather than replaying history.

### Limitation

This does not yet qualify very large merge/split graphs, concurrent identity transitions, migration of real repository references or corruption recovery.

## 8. Stop/reopen condition audit

Research 147 defined seven reasons to stop before broader prototype work. None fired in V0.1:

```text
ordinary base/supplement forced into joint authority                 no
hidden expected-label dependency                                   no
contract drift mechanism unable to surface frozen discrepancies     no
BL-001-style omitted activated constraint passed                    no
normal lookup required whole-history replay                         no
ordinary local change forced all generated views to rebuild         no
profile/special-object machinery expanded beyond bounded slice      no
```

The first slice therefore does **not** justify reopening H3.

## 9. Verification

```text
frozen fixture hash guard                         PASS
first raw run                                     PASS against later oracle comparison
first-run bytes equal final result bytes          PASS
focused Candidate 01 tests                        10 passed
all repository unit tests                         197 passed in 3.18s
Python source compile via in-memory compile()      PASS
fixture forbidden expected-label scan             PASS
implementation oracle-name/reference scan         PASS
```

A direct `py_compile` command was blocked because the read-only sandbox would not permit writing `__pycache__`; an equivalent in-memory `compile()` check passed for both implementation and test source. This is an execution-environment write restriction, not a code failure.

## 10. Requirement-evidence interpretation

This experiment adds **narrow synthetic support**, not final qualification, for mechanisms associated with:

```text
KA-R09  authority activation / action-contract fidelity
KA-R14  supplementation/conflict/set semantics
KA-R15  directional versus rich relationship representation
KA-R21  derived-state rebuildability
KA-R31  bounded required current reconstruction under passive history
KA-R33  dependency-local marginal refresh
KA-R46  representation-independent identity continuity + current-target lookup
KA-I05  governing contract survives into structured action plan
KA-I12  required current lookup/reconstruction does not replay history
KA-I17  semantic identity persists across carrier/merge/split transitions
```

None is marked finally qualified yet because the candidate has not been exercised on a sufficiently integrated and realistic repository slice.

## 11. What the first slice changes

Before this run, Candidate 01 was only architecture design plus separate mechanism evidence. After this run, five of its most architecture-sensitive integration assumptions have one common executable implementation and frozen-oracle evidence.

That is enough to continue the shadow program, but not enough to select the candidate.

The next prototype slice should broaden from structural foundations into the still-untested system behaviors that most strongly determine whether Candidate 01 is useful in real ADS development:

```text
workstream DAG / pause / resume / interruption recovery
capture -> consolidate -> promote with must-preserve fidelity
deterministic current-state core + generated routing/navigation parity
public/private degraded-mode and non-leakage behavior
consequence-sensitive source availability / ambiguity
```

Migration/rollback should remain later than these ordinary-operation behaviors unless the broader slice exposes a migration-specific blocker.

```text
RESEARCH149=SHADOW_V01_FIRST_SLICE_PASS
FIRST_RUN_REPAIR=NONE
FROZEN_ORACLE=PASS
FOUNDATIONAL_STOP_CONDITIONS=NONE_TRIGGERED
H3_REOPEN=NO
FINAL_QUALIFIED_PASSES=0
TARGET_ARCHITECTURE=NOT_SELECTED
NEXT=BROADER_SHADOW_OPERATIONAL_BEHAVIOR_SLICE
```
