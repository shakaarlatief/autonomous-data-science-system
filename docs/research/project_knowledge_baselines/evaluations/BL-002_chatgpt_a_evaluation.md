# BL-002 ChatGPT A Evaluation

**Date evaluated:** 2026-09-13
**Scenario:** BL-002
**Environment:** ChatGPT / GPT-5.6 Sol
**Result commit:** `fdea9b6d39ca58a79fe1e3760b9de690091eb90d`
**Frozen evidence snapshot:** `1a422c79dc67384426ad10e28c2fc6845147f9e0`
**Result artifact:** `docs/research/project_knowledge_baselines/results/BL-002_chatgpt_a.md`
**Historical parent:** `KF-SD-03`
**Evaluation status:** INVALID / SNAPSHOT-CONTAMINATED BY TOOL RESPONSE

## 1. Protocol-integrity decision

BL-002-A cannot be counted as a valid blind-baseline result.

The result receipt explicitly records that one frozen-commit metadata call unexpectedly returned patch content containing an excerpt from **prohibited current Research 124**. The tested collaborator states that it excluded that content from its substantive answer and thereafter used only permitted frozen-snapshot collaboration sources.

That is good fail-visible behavior, but the baseline protocol intentionally treats the historical snapshot as the sole project-evidence environment and forbids inspection of current Research 124 / later diagnosis material. Once later diagnosis content has entered the model context, its influence cannot be proven absent merely because the model says it did not use it.

Therefore the correct experimental classification is:

```text
substantive answer quality        potentially informative
blind-baseline validity           INVALID
reason                            descendant/current diagnosis exposure
attribution                       TOOL/HARNESS CONTAMINATION, not project-knowledge failure
result mutation isolation         PASS
fresh-session intent              PASS as reported
```

The invalidation is methodological rather than punitive. The result remains durable evidence about the harness and may be inspected after the replacement replicate is frozen.

## 2. Non-scored diagnostic observation

Although no S1-S8 baseline score is assigned, the answer is diagnostically notable.

It independently reconstructed the repository-native collaboration machinery and proposed:

```text
new MC-* thread
BRIEF.md / THREAD.md / STATE.json
REVIEW_INBOX routing
explicit coordination branch
bounded Claude write surface
repository-carried task context
short standardized human-to-Claude trigger
Claude message preservation before later comparison
```

It therefore does **not** exhibit the obvious generic-manual-relay behavior seen in historical parent `KF-SD-03`.

However, because current Research 124 content was accidentally exposed before the answer was frozen, this observation cannot be used as evidence that the frozen architecture alone caused that success.

The answer also anchored strongly on MC-0008's `INDEPENDENT_THEN_COMPARATIVE` precedent and proposed an independent architecture-design thread. That may be a reasonable inference from the permitted snapshot, but it cannot be fairly compared with the later owner-approved Research 124 collaboration method because that later method lies outside the frozen evidence boundary.

## 3. Harness lesson

BL-002-A reveals a baseline-harness risk distinct from the knowledge architecture under study:

> A tool advertised/used for frozen-commit metadata can return broader patch/context content than the trial intended to admit.

For subsequent trials, the access surface must be narrowed so that the model can traverse the exact Git tree without broad metadata/search responses that may include descendant or current patches.

The safe controlled lane for the replacement replicate and later trials should be:

```text
Codexless Runtime Bridge only
native GitHub plugin/connector disabled for the trial
exact local Git object/tree reads through read-only Codexless command execution
    git show <SNAPSHOT>:<path>
    git ls-tree ... <SNAPSHOT>
    git grep ... <SNAPSHOT> -- <paths>
no generic commit metadata/search/fetch action that can return unrelated patches
stop immediately as CONTAMINATED if any tool response exposes descendant/current project content
```

This constrains **transport**, not which project files the collaborator chooses to discover inside the frozen tree.

## 4. Replacement-replicate decision

A fresh BL-002 replacement replicate is required because the first trial is invalid.

The substantive task should remain unchanged. Only the snapshot-access harness is hardened.

Reserved replacement result path:

```text
docs/research/project_knowledge_baselines/results/BL-002_chatgpt_b.md
```

The replacement must run in a completely fresh ChatGPT conversation and must not see BL-002-A, this evaluation, Research 124, the failure corpus or any other baseline result/evaluator material.

```text
BL002_CHATGPT_A=INVALID_CONTAMINATED
CONTAMINATION_SOURCE=TOOL_RESPONSE
SUBSTANTIVE_SCORE=NOT_ASSIGNED
HISTORICAL_DISPATCH_FAILURE_REPRODUCTION=UNRESOLVED
HARNESS_HARDENING=REQUIRED
NEXT=BL-002_CHATGPT_B
```