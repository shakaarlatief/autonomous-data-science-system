# BL-002U ChatGPT A Evaluation

**Date evaluated:** 2026-09-13
**Scenario:** BL-002U / constructed adjacent uncued-dispatch variant
**Environment:** ChatGPT / GPT-5.6 Sol
**Result commit:** `881c01a2d29b9c6e9403b41f7d427b0939aa91a3`
**Frozen evidence snapshot:** `1a422c79dc67384426ad10e28c2fc6845147f9e0`
**Result artifact:** `docs/research/project_knowledge_baselines/results/BL-002U_chatgpt_a.md`
**Historical parent:** `KF-SD-03`
**Evaluation status:** VALID / SUBSTANTIVE RESULT WITH SCENARIO-METADATA CUE LIMITATION

## 1. Protocol integrity

BL-002U-A is protocol-valid under the V0.2 historical-snapshot access rules.

The receipt records:

```text
Codexless Runtime Bridge only
exact frozen SHA for substantive project evidence
snapshot-bounded git show / grep / ls-tree reads only
no native GitHub connector
no web/external sources
no descendant/current Research 124 evidence
no baseline/evaluator/failure-corpus reads
```

The result commit changed exactly one permitted result path.

One broad exact-snapshot grep was truncated, but targeted frozen reads succeeded afterward and no descendant/current content entered the trial context.

## 2. Core scenario finding

The substantive user task was deliberately neutral:

> "Before we continue the current project-development knowledge-architecture work, I want Claude involved so we can get its perspective too. What should we do next?"

Unlike BL-002-B, it did **not** tell the model to use "the way this project already handles multi-model collaboration."

The fresh ChatGPT nevertheless discovered and reconstructed the repository-native collaboration process. It selected a new `MC-0011` thread, separated it from existing `MC-0010`, recovered the independent-first `INDEPENDENT_THEN_COMPARATIVE` pattern from MC-0008, preserved branch-versus-frozen-evidence distinctions, bounded Claude's write scope, proposed a neutral brief and deterministic routing, and explicitly rejected an informal manual relay as the primary collaboration mechanism.

The historical generic-manual-relay behavior from `KF-SD-03` therefore does **not** reproduce under this adjacent task wording.

## 3. Scenario-metadata cue limitation

BL-002U materially improves the construct validity of BL-002-B, but it is not perfectly cue-free.

The request artifact itself contains evaluator-oriented metadata:

```text
BL-002U Request: Bring Claude In / Uncued Dispatch Variant
Scenario type: CONSTRUCTED ADJACENT VARIANT of historical KF-SD-03
```

The tested collaborator did not know the contents of `KF-SD-03`, but the phrase `Uncued Dispatch Variant` can still prime it to treat the task as a dispatch-classification problem rather than an ordinary ad hoc request.

Therefore the strongest justified claim is not:

```text
purely unprimed spontaneous dispatch proven
```

It is:

> **With the explicit "use the project's collaboration process" cue removed from the substantive task, a fresh ChatGPT still discovers and reconstructs the governed collaboration workflow efficiently from the frozen repository. The remaining evaluator-facing scenario label prevents treating this as a perfectly unprimed behavioral experiment.**

This residual limitation is not large enough to justify another pre-external-research replicate. A truly opaque harness could remove all evaluator labels from the trial-visible request, but the present evidence is already sufficient to distinguish the current architecture from the historical generic-relay failure without expanding the pilot indefinitely.

## 4. Frozen qualitative scoring

### S1 — task/situation recognition: PASS WITH SCENARIO-METADATA CUE LIMITATION

The collaborator correctly classified "bring Claude in" as a governed project-collaboration situation without the substantive prompt telling it that a project-specific process exists. The request title/metadata still contained the words `Uncued Dispatch Variant`, so the result is not fully unprimed.

### S2 — governing-source discovery: PASS

It found the canonical collaboration README plus the most relevant prior independent/comparative thread and live thread tree.

### S3 — governing-source consumption: PASS

The final answer reflects detailed thread lifecycle, independence, provenance, role/write-scope and resolution semantics from those sources.

### S4 — authority/source-strength selection: PASS

The answer separates coordination routing from the immutable substantive evidence base, distinguishes collaboration evidence from canonization authority, and does not collapse the unrelated MC-0010 obligation into the new task.

### S5 — final task correctness / fidelity: PASS

It directly answers what should happen next, avoids mutation as requested, and recommends the repository-native collaboration process rather than an informal relay.

### S6 — uncertainty calibration: PASS

It explicitly states what was not inspected and does not claim descendant/current decisions unavailable at the frozen snapshot.

### S7 — broad-vs-narrow context appropriateness: PASS

The reads remain concentrated on the collaboration subsystem and one strong precedent.

### S8 — read/tool cost and irrelevant-context burden: PASS

The receipt reports six exact-snapshot Git commands after the request read. That is a relatively small bounded reconstruction cost for this process-level task.

## 5. Failure attribution

```text
snapshot/source absence                  NO
navigation/discoverability failure       NO
process reconstruction failure           NO
authority-resolution failure             NO
generic-manual-relay behavior            NO
uncertainty/calibration failure           NO
context-allocation inefficiency           NO MATERIAL FAILURE
protocol contamination                    NO
scenario/evaluator metadata priming       YES / LIMITATION
```

## 6. Research 124 implication

Taken with BL-002-B, the evidence now supports a stronger but still calibrated conclusion:

```text
explicit process cue present      -> governed collaboration process reconstructs successfully
substantive process cue removed   -> governed collaboration process still reconstructs successfully
```

The historical KF-SD-03 failure therefore appears less like a simple repository discoverability defect and more like a **model/task-state activation failure that is possible but not deterministic**.

The frozen repository already contained enough structure for a fresh ChatGPT to recover the correct process with modest search effort. A successor architecture should still reduce dependence on stochastic situation recognition, but it should not be justified by claiming that the existing process is generally undiscoverable.

This supports the MC-0011 reasoning-control-plane hypothesis while sharpening its purpose:

> **The value of an explicit dispatch/control mechanism is reliability and repeatability at the decision point, not making an otherwise unrecoverable process discoverable for the first time.**

## 7. Baseline closure decision

No further pre-external-research baseline trial is required.

The remaining metadata-priming imperfection could be repaired with a more opaque harness, but another run would provide diminishing value relative to the next planned evidence source: broad external research across human factors, information retrieval, memory/consolidation, configuration management and preservation/governance disciplines.

The historical baseline program should now be synthesized as complete for this Research 124 phase.

```text
BL002U_CHATGPT_A=VALID
S1=PASS_WITH_SCENARIO_METADATA_CUE_LIMITATION
S2=PASS
S3=PASS
S4=PASS
S5=PASS
S6=PASS
S7=PASS
S8=PASS
GENERIC_MANUAL_RELAY_REPRODUCED=false
UNCUED_DISPATCH_EVIDENCE=SUPPORTIVE_BUT_NOT_PERFECTLY_UNPRIMED
MORE_BASELINE_TRIALS_BEFORE_EXTERNAL_RESEARCH=NO
NEXT=BROAD_QUESTION_DRIVEN_EXTERNAL_RESEARCH
```