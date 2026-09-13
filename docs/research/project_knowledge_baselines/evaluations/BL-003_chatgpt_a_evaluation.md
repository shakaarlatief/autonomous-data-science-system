# BL-003 ChatGPT A Evaluation

**Date evaluated:** 2026-09-13
**Scenario:** BL-003
**Environment:** ChatGPT / GPT-5.6 Sol
**Result commit:** `95c1b2e0ae0014f9f173331a0b5b1fe2d0b64173`
**Frozen evidence snapshot:** `f355994c538e0b9b28b5a3c2a5814252ffea1939`
**Result artifact:** `docs/research/project_knowledge_baselines/results/BL-003_chatgpt_a.md`
**Historical parent:** `KF-RD-01`
**Evaluation status:** VALID / SUBSTANTIVE BASELINE RESULT

## 1. Protocol integrity

BL-003-A satisfies the V0.2 historical-snapshot constraints.

The receipt records:

```text
Codexless Runtime Bridge only
exact frozen snapshot for substantive project evidence
snapshot-bounded local Git object/tree operations
no native GitHub connector
no web/external evidence
no descendant/current project evidence
no other baseline/evaluator/failure-corpus material
```

One initial broad `ls-tree` attempt was blocked before execution and returned no repository content. Several exact-snapshot multi-file reads were truncated and then narrowed. Neither event contaminated the evidence boundary.

The result commit changed only the permitted result artifact.

## 2. Core scenario finding

BL-003-A does **not** reproduce the strong form of historical parent `KF-RD-01`.

The frozen global `KNOWLEDGE_MAP.md` had become disproportionately shaped by the then-active Cockpit continuation, but the fresh ChatGPT did not treat that map as the whole project. It used the frozen repository tree plus multiple deeper authorities to reconstruct a broad project picture spanning at least:

```text
epistemic integrity / project constitution
LLM-system-human boundary
project state / dependency / object model
methodological navigation and reusable knowledge
V1 persistence / retrieval / context / runtime infrastructure
professional product experience / Project Cockpit
Source Universe / artifact integrity / evidence provenance
scientific evaluation / falsification
project-development governance / knowledge preservation / multi-model collaboration
```

The result therefore extends materially beyond the immediate Cockpit route and identifies representative governing/deep sources for each domain.

The answer also explicitly states that the orientation is not exhaustive and that it intentionally did not inspect every specification, checkpoint, research memo or implementation file.

## 3. What the result changes

The result weakens a simple interpretation of `KF-RD-01` such as:

```text
Knowledge Map becomes Cockpit-heavy
    -> fresh collaborator cannot recover broad project orientation
```

Under this trial, a strong fresh ChatGPT with snapshot-bounded repository tree/search access **can** recover broad orientation despite the drifted global map.

The stronger supported interpretation is more nuanced:

> **The drifted global navigation surface reduced direct semantic routing quality, but broad reconstruction remained possible by compensating with repository-wide structural search plus selective deep-source reading.**

That distinction matters for architecture design. The old architecture may have a **cost/efficiency and default-routing problem** rather than an absolute recoverability failure.

## 4. Frozen qualitative scoring

### S1 — task/situation recognition: PASS

The collaborator correctly recognized that the task required broad project orientation rather than immediate-current-task reconstruction.

### S2 — governing-source discovery: PASS

It found multiple high-value governing/deep sources across enduring domains rather than relying only on the global map or current Cockpit material.

### S3 — governing-source consumption: PASS

The final orientation contains detailed concepts traceable to the cited Foundations, Specifications, experiment result, Source Universe material and development-governance sources. This is materially stronger than filename-only discovery.

### S4 — authority/source-strength selection: PASS

The answer privileges Vision, Development Method, Foundations, accepted Specifications and experiment evidence according to their role. It correctly treats `KNOWLEDGE_MAP.md` as a routing aid rather than a substitute for deeper authority.

### S5 — final task correctness / fidelity: PASS

The user asked for a useful broad project orientation, major enduring domains/workstreams and important governing/deep sources without a file dump. The answer directly satisfies that request.

### S6 — uncertainty calibration: PASS

The answer explicitly states its non-exhaustive coverage, names categories it did not inspect, and does not claim an exact operational status reconstruction.

### S7 — broad-vs-narrow context appropriateness: PASS

The response is broad by design and extends well beyond the active Cockpit route while remaining organized around enduring architectural domains rather than chronological history.

### S8 — read/tool cost and irrelevant-context burden: PARTIAL

The result reports about 18 tool/read actions. That is not excessive for the requested breadth and no large irrelevant historical dump appears in the answer, but it is materially more expensive than a compact purpose-built broad-orientation path would ideally require.

The trial therefore shows **recoverability with non-trivial search/read work**, not cheap sublinear reconstruction.

## 5. Failure attribution

```text
snapshot/source absence             NO
navigation/discoverability failure  NO STRONG FAILURE
situation-dispatch failure          NO
authority-resolution failure        NO
source-consumed reasoning failure   NO
uncertainty/calibration failure      NO
context-allocation failure           NO MATERIAL FAILURE
reconstruction cost pressure         YES / MODERATE
protocol contamination               NO
```

## 6. Research 124 implication

BL-003-A supports a distinction between **recoverability** and **navigation efficiency**.

The frozen architecture was capable of supporting broad reconstruction when a fresh ChatGPT:

```text
was explicitly asked for broad orientation
had repository-wide exact-snapshot tree/search access
was willing to inspect a substantial set of deep sources
```

What remains unproven is whether the same breadth is achieved:

```text
with a small bounded cold-start read budget
under a generic continuation prompt
without strong repository-tree/search tooling
or as corpus size grows substantially
```

This aligns with the Research 124 scaling principle: the redesign problem is not simply "can the project ever be reconstructed?" but whether sufficient understanding can be acquired **reliably and cheaply enough** as the project grows.

The historical map-drift incident therefore remains relevant as evidence of routing-surface degradation, while BL-003 prevents that incident from being overstated as total project-orientation failure.

## 7. Replicate decision

No immediate identical repeat is required. The result is protocol-valid and the central finding is clear.

If later architecture work needs a sharper scaling discriminator, a separate fixed-read-budget orientation trial would be more informative than repeating the same unconstrained broad-orientation task.

```text
BL003_CHATGPT_A=VALID
S1=PASS
S2=PASS
S3=PASS
S4=PASS
S5=PASS
S6=PASS
S7=PASS
S8=PARTIAL
BROAD_ORIENTATION_RECOVERABLE=true
GLOBAL_MAP_DRIFT_EQUAL_TOTAL_RECONSTRUCTION_FAILURE=false
RECONSTRUCTION_COST_PRESSURE=observed
IMMEDIATE_IDENTICAL_REPLICATE=NO
POSSIBLE_LATER_FIXED_BUDGET_VARIANT=YES
NEXT=BL-004_CHATGPT_A
```