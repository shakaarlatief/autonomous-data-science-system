# BL-004 ChatGPT A Evaluation

**Date evaluated:** 2026-09-13
**Scenario:** BL-004
**Environment:** ChatGPT / GPT-5.6 Sol
**Frozen evidence snapshot:** `2d425c76c385961cdd7f986c17ed83437a3d3806`
**Result artifact:** `docs/research/project_knowledge_baselines/results/BL-004_chatgpt_a.md`
**Result SHA-256:** `16813efc6c41733884da790738adabd2d066b8c1393c93ae38a2ee35c7839f61`
**Historical parents:** `KF-AS-01`, `KF-CS-01`
**Evaluation status:** VALID / SUBSTANTIVE BASELINE RESULT

## 1. Protocol integrity

BL-004-A satisfies the V0.2 access constraints according to its receipt and the locally preserved result bytes.

The receipt records:

```text
Codexless Runtime Bridge only
exact frozen snapshot for substantive project evidence
snapshot-bounded git ls-tree / show / grep reads
no descendant/current project content as substantive evidence
no implementation mutation
```

The result file was created locally by the trial but fell under the repository's global `**/results/` ignore rule, so it was not automatically visible to ordinary Git status/push behavior. Its local SHA-256 exactly matches the project-owner completion report. The evaluator will preserve those exact bytes durably without modifying the trial answer.

This is a result-preservation harness issue, not a substantive trial defect.

## 2. Core scenario finding

BL-004-A strongly **does not reproduce** the historical exact-source fidelity failure represented by `KF-AS-01` / `KF-CS-01`.

The fresh ChatGPT explicitly distinguishes multiple authority/source-strength layers:

```text
Specification 008                   promoted interaction-architecture floor
Foundations 021/023/024             product/semantic invariants
latest explicit Phase-C selections  current held design decisions
isolated accepted design-lab targets fidelity oracles for exact mechanisms
existing production Cockpit         integration substrate, not visual authority
```

Most importantly, it states that where a research record names an exact accepted browser target or implementation file, integration should **port geometry, timing, layer ordering, proportions and interaction behavior from that implementation rather than recreate the effect from memory or prose**.

That is the precise distinction the historical integration failed to preserve.

The answer also refuses two opposite mistakes:

```text
prose-summary-only reconstruction      rejected
blind copying of prototype-only state  rejected
```

It treats exact design-lab implementation as fidelity evidence for the accepted mechanism while keeping prototype persistence, fixture ontology and experiment controls subordinate unless separately promoted.

## 3. Exact-source depth limitation

The trial read a large set of decision/provenance records, the design-lab tree and the current production Cockpit source. It did **not** exhaustively inspect every accepted design-lab CSS/JS implementation file line-by-line.

That does not invalidate the scenario because the task is planning-only and asks whether the collaborator recognizes the need to consume exact accepted implementations/provenance before integration. It clearly does.

Still, the evidence supports a slightly narrower claim than "all exact visual source implementations were fully consumed":

> **The collaborator correctly identifies exact implementation artifacts as stronger fidelity sources than prose summaries, locates their role through the frozen provenance records, and designs the integration around source-level reuse/comparison rather than free reimplementation.**

Actual implementation would still require consuming the exact source files for each mechanism before porting it.

## 4. Frozen qualitative scoring

### S1 — task/situation recognition: PASS

The collaborator recognizes that this is an integration-fidelity/source-selection problem, not merely a UI implementation task.

### S2 — governing-source discovery: PASS

It identifies promoted specifications/foundations, latest held Phase-C decision records, design-lab implementation targets and the production integration substrate.

### S3 — governing-source consumption: PASS WITH DEPTH LIMIT

The final answer reflects detailed Phase-C decisions and production constraints from many frozen sources. Exact implementation artifacts are correctly elevated as fidelity oracles, but not every underlying CSS/JS source was exhaustively read during this planning-only trial.

### S4 — authority/source-strength selection: PASS

This is the strongest part of the result. It explicitly orders semantic/promoted authority, current design-selection evidence, exact implementation fidelity sources and production substrate rather than flattening them into peers.

### S5 — final task correctness / fidelity: PASS

The answer directly supplies both the source-selection hierarchy and an integration strategy designed to preserve accepted visual/interaction decisions. It proposes reuse/port/composition, source-level comparison, representative mixed-state fixtures, side-by-side human review and interaction validation instead of prose-driven reimplementation.

### S6 — uncertainty calibration: PASS

The result preserves open questions such as conversation co-presence geometry, light mode, semantic zoom, X5 internals, persistence, Z7 timing/return semantics, URL/session contracts and production graph/canvas technology instead of freezing them implicitly.

### S7 — broad-vs-narrow context appropriateness: PASS

The task legitimately spans many Phase-C channels. The answer remains focused on source authority and integration fidelity rather than drifting into unrelated ADS domains.

### S8 — read/tool cost and irrelevant-context burden: PARTIAL

The receipt reports roughly 16 snapshot-bounded Git reads plus request/workspace access. This is reasonable for a broad multi-channel integration plan, but again demonstrates that recovering exact accepted state across many independent Phase-C decisions is not cheap.

## 5. Failure attribution

```text
snapshot/source absence                   NO
navigation/discoverability failure        NO MATERIAL FAILURE
governing-source activation failure       NO
authority/source-strength failure          NO
prose-over-exact-source fidelity failure   NO
source-consumed reasoning failure          NO
uncertainty/calibration failure            NO
context-allocation failure                 NO MATERIAL FAILURE
reconstruction/source-assembly cost        YES / MODERATE
protocol contamination                     NO
result-preservation harness issue          YES / NON-SUBSTANTIVE
```

## 6. Research 124 implication

BL-004-A shows that the historical Cockpit fidelity failure is **not inevitable under the frozen project-development knowledge architecture**.

A fresh ChatGPT can recover the crucial rule that:

```text
semantic decision record
    tells us what was accepted and why

exact accepted implementation/provenance
    tells us how the accepted interaction/visual mechanism actually behaves

production integration
    should preserve both without treating either prototype scaffolding or prose alone
    as the whole authority
```

This sharpens Research 124's source-strength problem. The architecture needs to preserve and activate not only "the relevant document" but the **appropriate evidence depth for the requested task**.

For high-fidelity implementation tasks, a prose synthesis may be excellent for orientation yet still be too weak as the final implementation source. The reconstruction path must be able to descend from synthesis into exact executable provenance when fidelity requires it.

This is directly compatible with the emerging Tier A/B/C and progressive-disclosure framing:

```text
orientation / current decision
    -> exact governing design selection
    -> exact implementation/provenance evidence when task demands fidelity
```

## 7. Initial four-scenario pilot synthesis

With BL-004-A complete, the original four-scenario ChatGPT pilot has produced four usable substantive scenario outcomes plus one invalid/replaced BL-002 attempt.

The main findings are:

```text
BL-001
    right operational authority can activate
    but exact task contract can still be lost after activation

BL-002-B
    collaboration process is discoverable/reconstructable when explicitly cued
    but uncued spontaneous situation dispatch was not cleanly tested

BL-003
    broad project orientation remains recoverable despite global-map drift
    but requires non-trivial compensating search/read work

BL-004
    exact-source fidelity hierarchy can be reconstructed correctly
    but assembling many accepted mechanism sources is again non-trivial in cost
```

This pilot therefore does **not** support the simplistic thesis that the current architecture is generally unable to preserve/reconstruct project understanding. It supports a more precise set of weaknesses:

```text
activation can fail before retrieval begins
activation success does not guarantee exact answer/task fidelity
broad/exact reconstruction often depends on compensating search effort
source strength/depth must vary with task fidelity requirements
```

## 8. Follow-up decision

One central empirical question from MC-0011 remains insufficiently tested: **uncued situation dispatch**.

Because BL-002 explicitly told the collaborator to use the project's existing multi-model collaboration process, it cannot establish whether a generic "bring Claude in" request spontaneously triggers that process.

A single constructed adjacent variant is therefore justified before external research begins. It should keep the same frozen snapshot but remove the process-existence cue.

No additional repeat of BL-001, BL-003 or BL-004 is required at this boundary.

```text
BL004_CHATGPT_A=VALID
S1=PASS
S2=PASS
S3=PASS_WITH_DEPTH_LIMIT
S4=PASS
S5=PASS
S6=PASS
S7=PASS
S8=PARTIAL
HISTORICAL_EXACT_SOURCE_FIDELITY_FAILURE_REPRODUCED=false
INITIAL_FOUR_SCENARIO_PILOT=COMPLETE
UNCUED_SITUATION_DISPATCH=STILL_UNRESOLVED
NEXT=ONE_TARGETED_UNCUED_DISPATCH_VARIANT
```