# MC-0015 Brief: Independent Claude Judgment of Real ADS Relationship Corpus V0.1

**Thread:** MC-0015
**Date opened:** 2026-09-13
**Review mode:** INDEPENDENT_THEN_COMPARATIVE
**Coordination branch:** `v1-source-vault-bootstrap-resume`
**Independent substantive base:** `ae87c1facbf7c7d7508414e86a935bc439404c24`
**Corpus:** `PKA-REAL-REL-V01`
**Corpus SHA-256:** `cc61a9610b2a88b8be6c3af06b661c6ce270e094e380d1d362dc8f10d8f90ed5`
**Corpus source snapshot:** `47656a2a6ed98061d987786814a6be39d38b3999`
**Claude interaction:** `claude-03`
**Claude conversation title:** `03 - Project Knowledge Architecture Foundations and Design Method`
**Authority:** Collaboration evidence only. Requirements V0.2 remain the frozen candidate-acceptance authority. This thread cannot select a target architecture, alter the corpus, inspect ChatGPT labels during the independent phase, or authorize a mechanized admission rule.
**Purpose:** Obtain Claude's complete independent semantic-ownership/reification judgments for all 15 real ADS relationship cases before any exposure to ChatGPT's already-frozen labels.

## 1. Independence target

This is **reviewer-label independence**, not architecture-problem blindness. Claude already knows the Research 124 evidence program and participated in MC-0011 through MC-0014. That is allowed.

The information that must remain hidden until Claude's complete judgment set is durably frozen is **ChatGPT's case-by-case labels, confidence values and rationales**.

The corpus itself was frozen before either reviewer judgment began at exact commit:

```text
ae87c1facbf7c7d7508414e86a935bc439404c24
```

Use that commit as the substantive evidence boundary.

## 2. Current-branch routing boundary

From the current coordination branch, Claude may read only the routing surfaces required to locate and execute this obligation:

```text
docs/current_routing.json
docs/model_collaboration/REVIEW_INBOX.md
docs/model_collaboration/threads/MC-0015/BRIEF.md
docs/model_collaboration/threads/MC-0015/THREAD.md
docs/model_collaboration/threads/MC-0015/STATE.json
```

Do **not** read current `CURRENT_STATE.md`, current Research 124 additions, current Knowledge Map summaries, later checkpoints or other descendant synthesis before Message 001 is frozen.

For substantive judgment reads, use exact commit `ae87c1facbf7c7d7508414e86a935bc439404c24`.

## 3. Explicit descendant exclusions

The following content exists only after the independent base and is prohibited during Message 001:

```text
docs/research/project_knowledge_real_corpus_v01/CHATGPT_JUDGMENTS_V01.json
docs/research/141_real_ads_relationship_corpus_v01_chatgpt_independent_judgment.md
Checkpoint 485 and later checkpoint bodies
any descendant synthesis that reveals ChatGPT's case labels/counts/confidences/rationales
```

Do not inspect Git diffs/log content after `ae87c1facbf7c7d7508414e86a935bc439404c24` in a way that exposes these files.

If ChatGPT case-label content is exposed unexpectedly, stop and report:

```text
INDEPENDENT_JUDGMENT_CONTAMINATED
```

rather than continuing as though exposure had not happened.

## 4. Governing substantive sources at the exact base

At exact commit `ae87c1facbf7c7d7508414e86a935bc439404c24`, read at minimum:

```text
docs/research/PROJECT_KNOWLEDGE_ARCHITECTURE_REQUIREMENTS_V02.md
docs/research/139_cross_model_probe_reconciliation_and_real_corpus_discriminator_protocol.md
docs/research/140_real_ads_relationship_corpus_v01_machine_freeze.md
docs/research/project_knowledge_real_corpus_v01/RELATIONSHIP_CORPUS_V01.json
```

The corpus packets are the primary case evidence. Each packet is tied to source snapshot `47656a2a6ed98061d987786814a6be39d38b3999` with exact path, Git blob SHA, SHA-256, line range and excerpt.

If a packet is insufficient and deeper source context is materially necessary, you may read the named source at exact source snapshot `47656a2a6ed98061d987786814a6be39d38b3999` and must list that additional read in your response provenance. Do not use a descendant version of the source. If you cannot establish enough evidence within that boundary, use `UNRESOLVED`.

Do not silently fill a packet gap from memory of prior chats.

## 5. Judgment task

Judge **all 15 cases** independently. For each case, choose exactly one primary class:

```text
SOURCE_LOCAL
    one source-like semantic owner can state the authoritative fact fully without
    independently maintained competing truth

FIRST_CLASS_SEMANTIC_OBJECT
    the relationship/activity/identity itself appears to require durable addressable
    continuity distinct from any one participant/source

DERIVED_ONLY
    the queried relationship is best treated as deterministic/rebuildable closure or
    view over authoritative inputs rather than unique authoritative truth

UNRESOLVED
    packet evidence is insufficient or materially different ownership classes remain
    plausible
```

For every case also provide exactly:

```text
confidence: HIGH / MEDIUM / LOW
rationale
proposed_natural_owner_or_null
independent_continuity_basis_or_null
derived_inputs_or_null
missing_evidence_or_null
```

Judge semantic ownership/reification only. Do not choose files versus SQL versus graph storage. Do not attempt to optimize agreement with what you think ChatGPT might have chosen.

## 6. Required output format

Write exactly one message at:

```text
docs/model_collaboration/threads/MC-0015/messages/001_claude_independent_real_corpus_judgment.md
```

Include normal collaboration provenance plus an independence/contamination statement.

Inside the message, include one fenced JSON object with this shape so the result can be compared mechanically later:

```text
{
  "judgment_set_id": "PKA-REAL-REL-V01-CLAUDE-A",
  "corpus_id": "PKA-REAL-REL-V01",
  "corpus_freeze_commit": "ae87c1facbf7c7d7508414e86a935bc439404c24",
  "corpus_sha256": "cc61a9610b2a88b8be6c3af06b661c6ce270e094e380d1d362dc8f10d8f90ed5",
  "additional_source_reads": [],
  "judgments": [
    {
      "case_id": "RC-001",
      "label": "SOURCE_LOCAL | FIRST_CLASS_SEMANTIC_OBJECT | DERIVED_ONLY | UNRESOLVED",
      "confidence": "HIGH | MEDIUM | LOW",
      "rationale": "...",
      "proposed_natural_owner_or_null": null,
      "independent_continuity_basis_or_null": null,
      "derived_inputs_or_null": null,
      "missing_evidence_or_null": null
    }
  ]
}
```

The `judgments` array must contain each `RC-001` through `RC-015` exactly once. Do not include ChatGPT guesses or comparison commentary.

After the JSON block, you may add a short reviewer-level note about which cases were hardest to classify and why, as long as it does not speculate about ChatGPT's labels.

## 7. Write scope

Claude may write only:

```text
docs/model_collaboration/threads/MC-0015/messages/**
```

Do not modify the corpus, Requirements V0.2, Research 139/140, routing, checkpoints, current state, implementation or canonical governance.

## 8. Phase transition

After Message 001 is committed and pushed, ChatGPT will validate the independence boundary and normalize Claude's JSON result. Only then may the two frozen judgment sets be compared case by case.

```text
MC0015=OPEN
MODE=INDEPENDENT_THEN_COMPARATIVE
PHASE=INDEPENDENT_REAL_CORPUS_JUDGMENT
INDEPENDENT_BASE=ae87c1facbf7c7d7508414e86a935bc439404c24
CHATGPT_LABELS=DESCENDANT_ONLY_AND_PROHIBITED
CLAUDE_MESSAGE_001=NEXT
MECHANIZED_RULE=NOT_STARTED
TARGET_ARCHITECTURE=NOT_SELECTED
```
