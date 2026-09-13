# Research 141: Real ADS Relationship Corpus V0.1 ChatGPT Independent Judgment

**Date:** 2026-09-13
**Status:** CHATGPT JUDGMENT SET COMPLETE AND FROZEN / CLAUDE INDEPENDENT JUDGMENT NEXT / CROSS-REVIEWER COMPARISON NOT YET ALLOWED / TARGET ARCHITECTURE NOT SELECTED
**Scope:** Preserve ChatGPT's complete independent semantic-ownership/reification judgment set over the machine-frozen 15-case real ADS relationship corpus before any Claude case labels exist or are exposed.
**Authority:** Reviewer evidence only under Research 124/139/140. Requirements V0.2 remain the frozen candidate-acceptance authority. This judgment set does not establish ground truth, select a target architecture or authorize a mechanized admission rule.
**Declared references:** `research:124`, `research:139`, `research:140`, `path:docs/research/PROJECT_KNOWLEDGE_ARCHITECTURE_REQUIREMENTS_V02.md`, `path:docs/research/project_knowledge_real_corpus_v01/RELATIONSHIP_CORPUS_V01.json`, `checkpoint:484`

## 1. Independence and freeze boundary

ChatGPT judged all 15 cases only after Corpus V0.1 was machine-frozen at:

```text
corpus freeze commit: ae87c1facbf7c7d7508414e86a935bc439404c24
corpus SHA-256:       cc61a9610b2a88b8be6c3af06b661c6ce270e094e380d1d362dc8f10d8f90ed5
```

No Claude judgment set existed or was read. The reviewer knew Requirements V0.2, Research 124 and the already-public MC-0014 lessons, which is intentional under Research 139. The independence property being preserved is **case-label non-exposure**, not blindness to the architecture problem.

The complete machine-readable judgment set is:

```text
docs/research/project_knowledge_real_corpus_v01/CHATGPT_JUDGMENTS_V01.json
SHA-256: 73848d51f659fab83c2cd461cad7b8a0973ade569db6d958ad2b024a7d3cd7dd
```

No additional source reads were used beyond the frozen evidence packets. Where a packet did not establish enough authority-class information, the reviewer was required to use `UNRESOLVED` rather than silently consult remembered project context.

## 2. Aggregate result before any cross-reviewer comparison

```text
SOURCE_LOCAL                  10 / 15
FIRST_CLASS_SEMANTIC_OBJECT    2 / 15
DERIVED_ONLY                   2 / 15
UNRESOLVED                     1 / 15

HIGH confidence               12 / 15
MEDIUM confidence              3 / 15
LOW confidence                 0 / 15
```

These counts are **not architecture scores**. They are one reviewer's classifications of a small coverage-stratified real corpus. The empirical value comes later from agreement/disagreement with an independently frozen second judgment set and case-level analysis.

## 3. SOURCE_LOCAL judgments

ChatGPT classifies these ten cases as source-local:

```text
RC-001  D-015 scoped supersession by D-033
RC-002  D-011 multi-successor scoped supersession
RC-004  checkpoint metadata/role governed by checkpoint contract
RC-007  Source Vault reopen/pause triggers
RC-008  MC-0013 review-base and exposure boundary
RC-009  Methodological Knowledge provenance to source evidence
RC-011  public/private authority delegation rule
RC-013  collaboration write-scope / next-actor state
RC-014  review-task coordination branch / immutable target binding
RC-015  current-to-successor architecture authority-transition invariant
```

The common rationale is not that these relations are trivial. It is that one durable semantic owner can state the full relation without forcing another independently maintained authority surface. Examples include an old decision owning its own scoped supersession status, a process contract owning its reopen triggers, and a review thread owning its exact evidence-base constraints.

Two are deliberately only `MEDIUM` confidence:

```text
RC-002
    multi-successor scope maps can become structurally rich even if D-011 remains a
    plausible owner

RC-015
    the packet contains a governance invariant, not a concrete future migration instance;
    an actual successor transition with independent approvals/effective time/state could
    later earn first-class identity
```

## 4. FIRST_CLASS_SEMANTIC_OBJECT judgments

Two real workstream cases are classified first-class with `HIGH` confidence:

```text
RC-005  paused Cockpit workstream + preserved resume anchor while Source Vault proceeds
RC-006  active Research 123 route + paused Research 113/Source Vault + later-return semantics
```

In both cases, the thing requiring continuity is the **workstream/control state itself** rather than any one participant artifact. The state persists across pause/resume boundaries, branches/checkpoints, dependency/return relationships and later continuation. This directly connects to KA-R25..R29 without requiring a decision about whether the future physical representation is a file, row, graph object or another mechanism.

This is the first real-corpus evidence in the current program that ChatGPT independently classifies any relationship/control concept as deserving first-class semantic identity. It is still only one reviewer's judgment.

## 5. DERIVED_ONLY judgments

Two cases are classified derived-only with `HIGH` confidence:

```text
RC-003  obsolete same-branch CI run after newer push
RC-010  Knowledge Map subject-to-artifact routing membership
```

For RC-003, obsolescence can be computed from run branch/head/status, the newer push and the supersession/cancellation policy. Persisting a second authoritative `obsolete_by` truth would create staleness risk.

For RC-010, the source explicitly says topic membership is navigation metadata and not an authority claim. The relationship is therefore naturally a rebuildable organizational view over authoritative knowledge/routing inputs.

These cases are important because the real-corpus discriminator is not merely source-local versus reified object. Some semantic relationships are best treated as governed derivations with no unique authoritative relation fact at all.

## 6. UNRESOLVED judgment

`RC-012`, the compact `current_routing.json` tuple, is `UNRESOLVED / MEDIUM`.

The packet establishes the fields but not their semantic authority classes. From the packet alone, the reviewer cannot tell whether all fields are:

```text
unique canonical live state
a deterministic projection of checkpoint/workstream/branch sources
or a mixture of canonical and projected fields
```

That distinction determines whether the right answer is SOURCE_LOCAL, DERIVED_ONLY or a first-class live-route object. Research 140 explicitly forbids silently using remembered project context to fill the gap, so the correct output is unresolved.

This is a useful protocol result: `UNRESOLVED` can actually fire when a real evidence packet does not support a safe ownership conclusion.

## 7. What this judgment set does and does not support

Before Claude judges the same corpus, this result may support only reviewer-specific observations:

```text
ChatGPT does not reify most sampled relationships
ChatGPT sees two workstream/control cases as independently continuous
ChatGPT sees two relationships as derived-only rather than authoritative
one packet is insufficient for a confident class
```

It does **not** yet establish:

```text
that these labels are correct ground truth
that the 10/2/2/1 distribution generalizes to ADS
that a universal admission rule exists
that workstreams and other first-class objects should share one schema/store
that selective semantic reification is the selected architecture
```

The cross-reviewer comparison is intentionally forbidden until Claude's complete set is frozen independently.

## 8. Next independence gate

Claude's substantive evidence boundary must be exactly the corpus-freeze commit:

```text
ae87c1facbf7c7d7508414e86a935bc439404c24
```

The descendant ChatGPT surfaces must be explicitly excluded, including at least:

```text
docs/research/project_knowledge_real_corpus_v01/CHATGPT_JUDGMENTS_V01.json
docs/research/141_real_ads_relationship_corpus_v01_chatgpt_independent_judgment.md
Checkpoint 485 and later checkpoint bodies
CURRENT_STATE / routing synthesis added after the corpus freeze
```

Claude may use current descendant routing only to discover its obligation. Its case evidence and Requirements V0.2 reads must come from the exact frozen base.

## 9. Current disposition

```text
CHATGPT_JUDGMENT_SET=FROZEN
CHATGPT_SOURCE_LOCAL=10
CHATGPT_FIRST_CLASS=2
CHATGPT_DERIVED_ONLY=2
CHATGPT_UNRESOLVED=1
CLAUDE_JUDGMENT_SET=NOT_YET_PRODUCED
CROSS_REVIEWER_COMPARISON=PROHIBITED_UNTIL_CLAUDE_FREEZE
MECHANIZED_RULE=NOT_STARTED
REQUIREMENTS_V02=UNCHANGED_FROZEN
TARGET_ARCHITECTURE=NOT_SELECTED
NEXT=OPEN_CLAUDE_INDEPENDENT_REAL_CORPUS_JUDGMENT
```
