# BL-002 ChatGPT B Evaluation

**Date evaluated:** 2026-09-13
**Scenario:** BL-002B replacement for BL-002-A
**Environment:** ChatGPT / GPT-5.6 Sol
**Result commit:** `0cea423431d9528f9c163f02e357d420e3c239a0`
**Frozen evidence snapshot:** `1a422c79dc67384426ad10e28c2fc6845147f9e0`
**Result artifact:** `docs/research/project_knowledge_baselines/results/BL-002_chatgpt_b.md`
**Historical parent:** `KF-SD-03`
**Evaluation status:** VALID / SUBSTANTIVE BASELINE RESULT

## 1. Protocol integrity

BL-002-B satisfies the V0.2 replacement constraints.

The result receipt records:

```text
Codexless Runtime Bridge only
exact frozen SHA used for all substantive repository evidence
snapshot-bounded local Git object/tree operations only
no native GitHub connector
no web/external evidence
no descendant/current Research 124 evidence
no other baseline/evaluator material
```

One combined exact-snapshot read was truncated, but the truncation did not expose descendant/current content and the relevant collaboration facts were available through other permitted snapshot reads. This is an ordinary read limitation rather than contamination.

The result commit changed only the permitted result path.

## 2. Core scenario finding

BL-002-B does **not** reproduce the historical generic-manual-relay behavior from `KF-SD-03`.

The fresh ChatGPT identified the request as governed by the repository-native model-collaboration system and materially reconstructed:

```text
MC-* thread identity
BRIEF / THREAD / STATE contract
REVIEW_INBOX routing
coordination branch vs immutable substantive evidence target
explicit role/write-scope separation
secondary collaborator message-only write surface
fresh persistent Claude interaction provenance
short standardized repository/branch relay
numbered durable Claude message before later comparison
final reconciliation before resolution
```

It also noticed that `MC-0010` already existed as a distinct pending obligation and did not silently overwrite/reuse it.

This is strong evidence that, **when the task explicitly cues the collaborator to use the way the project already handles multi-model collaboration**, the frozen architecture makes that process discoverable and reconstructable without a giant human-carried prompt.

## 3. Construct-validity limitation

The result must not be overinterpreted as proof that the historical situation-dispatch failure has been solved.

The BL-002 request itself says:

> "Tell me exactly how you would set that up using the way this project already handles multi-model collaboration."

That phrase explicitly tells the tested collaborator that a project-specific collaboration process exists and should govern the task. The historical `KF-SD-03` failure was stronger: ChatGPT was asked to involve/talk with Claude and failed to activate the already-preserved process until the owner reminded it how the process works.

Therefore BL-002-B tests primarily:

```text
once project-specific process existence is cued,
can a fresh collaborator discover/reconstruct/use that process?
```

It does **not** cleanly test:

```text
without that cue,
does the collaborator spontaneously classify "bring Claude in" as a governed project situation?
```

This is a scenario-design limitation, not a failure of the model or repository.

If Research 124 later needs evidence specifically about spontaneous dispatch, it should add one adjacent constructed variant with neutral wording such as "I want Claude involved before we continue; what should we do?" while keeping the evaluator mechanism hidden. That variant should be decided after the initial four-scenario pilot rather than expanding the pilot immediately.

## 4. Frozen qualitative scoring

### S1 — task/situation recognition: PASS WITH PROMPT-CUE LIMITATION

The collaborator correctly treated the task as governed multi-model collaboration, but the user prompt explicitly cued that project-specific process category.

### S2 — governing-source discovery: PASS

It discovered and used the canonical collaboration README, provenance/naming rules, inbox, deferred-review protocol, MC-0008 contract/state/resolution, and the frozen thread tree.

### S3 — governing-source consumption: PASS

The final answer reflects multiple detailed rules from those sources rather than filename-only discovery.

### S4 — authority/source-strength selection: PASS

It distinguishes coordination branch from immutable substantive evidence, thread contract from convenience routing, collaboration evidence from project authority, and role from write scope.

Its use of MC-0008 as the strongest analogous precedent is traceable to the permitted snapshot. The exact future review mode is not pre-scored by the baseline protocol because later owner routing is absent from the frozen evidence.

### S5 — final task correctness / fidelity: PASS

The answer directly supplies a governed setup process and immediate next steps, preserves the no-mutation boundary, and avoids the giant manual prompt pattern.

### S6 — uncertainty calibration: PASS

It explicitly marks the Claude session number as provisional, acknowledges that it did not inspect current Research 124, and avoids claiming later owner decisions unavailable at the snapshot.

### S7 — broad-vs-narrow context appropriateness: PASS

The context read is concentrated on the model-collaboration subsystem and one relevant precedent rather than reconstructing unrelated project history.

### S8 — read/tool cost and irrelevant-context burden: PASS

The receipt reports approximately seven pre-write tool calls with targeted reads. No broad current-state reconstruction was required.

## 5. Failure attribution

```text
snapshot/source absence             NO
navigation/discoverability failure  NO
process reconstruction failure      NO
authority-resolution failure        NO
source-consumed reasoning failure   NO
uncertainty/calibration failure      NO
context-allocation inefficiency      NO MATERIAL FAILURE
protocol contamination               NO
scenario construct limitation        YES
```

## 6. Research 124 implication

BL-002-B supports a narrower and more useful claim than "the dispatch problem is solved":

> **The frozen repository-native collaboration architecture is sufficiently discoverable and reconstructable for a fresh ChatGPT to recover the intended governed workflow efficiently once the task is explicitly framed as using the project's existing multi-model collaboration process.**

The unresolved question is upstream situation recognition: whether the same process activates when the user merely asks to involve Claude without reminding the model that a governed project-specific process exists.

This reinforces the MC-0011 distinction between:

```text
situation dispatch / classification
    -> process/source discovery
    -> process/source consumption
    -> task execution fidelity
```

BL-002-B provides strong evidence for the middle stages, not clean evidence for uncued dispatch.

## 7. Replicate decision

No second identical BL-002-B replicate is required. The result is clear and protocol-valid.

A later **adjacent uncued variant** may be warranted specifically for spontaneous dispatch, but it should be considered after BL-003 and BL-004 rather than interrupting the bounded pilot now.

```text
BL002_CHATGPT_B=VALID
S1=PASS_WITH_PROMPT_CUE_LIMITATION
S2=PASS
S3=PASS
S4=PASS
S5=PASS
S6=PASS
S7=PASS
S8=PASS
HISTORICAL_GENERIC_MANUAL_RELAY_REPRODUCED=false
UNCUED_SITUATION_DISPATCH_TESTED=false
IMMEDIATE_IDENTICAL_REPLICATE=NO
POSSIBLE_LATER_ADJACENT_VARIANT=YES
NEXT=BL-003_CHATGPT_A
```