# Research 140: Real ADS Relationship Corpus V0.1 Machine Freeze

**Date:** 2026-09-13
**Status:** UNLABELED REAL-CORPUS V0.1 MACHINE-FROZEN / REVIEWER JUDGMENTS NOT YET STARTED / TARGET ARCHITECTURE NOT SELECTED
**Scope:** Freeze the first real-repository relationship corpus before any ChatGPT or Claude ownership/reification judgment, preserving exact source evidence and a judgment-neutral case boundary for Research 139's behavioral discriminator.
**Authority:** Experiment input only under Research 124/139. Requirements V0.2 remain the frozen candidate-acceptance authority. Corpus inclusion does not imply an expected semantic-ownership label.
**Declared references:** `research:124`, `research:139`, `path:docs/research/PROJECT_KNOWLEDGE_ARCHITECTURE_REQUIREMENTS_V02.md`, `checkpoint:483`

## 1. Exact frozen corpus

```text
path:
    docs/research/project_knowledge_real_corpus_v01/RELATIONSHIP_CORPUS_V01.json
corpus_id:
    PKA-REAL-REL-V01
source repository commit:
    47656a2a6ed98061d987786814a6be39d38b3999
case count:
    15
bytes:
    26,873
SHA-256:
    cc61a9610b2a88b8be6c3af06b661c6ce270e094e380d1d362dc8f10d8f90ed5
```

The corpus was created from the exact source state at `47656a2a6ed98061d987786814a6be39d38b3999` and validated before any reviewer labels existed. Every case records the exact source path, source SHA-256, line range and source excerpt used for judgment.

If a semantic defect is discovered later, V0.1 must not be silently relabeled or edited in place. Create a new corpus version and preserve this one as experiment provenance.

## 2. What is deliberately absent

No case contains any of the answer-bearing fields that made V0.2's admission test circular:

```text
expected_label
natural_owner
independent_lifecycle
should_reify
H1 / H2 / H3 designation
mechanized admission output
reviewer judgment
```

The corpus does include the four allowed judgment classes at the top-level protocol boundary so reviewers know the response taxonomy:

```text
SOURCE_LOCAL
FIRST_CLASS_SEMANTIC_OBJECT
DERIVED_ONLY
UNRESOLVED
```

That is a response vocabulary, not a case label.

## 3. Selection basis

The 15 cases were selected to cover distinct **real project-development relationship categories**, not to balance or predetermine expected labels.

Coverage includes:

```text
authority / scoped supersession
operational supersession
governance
workstream pause/resume and active/paused route state
reopen/evolution triggers
independence-sensitive review-base binding
evidence -> reusable-knowledge derivation
semantic navigation membership
public/private authority delegation
live routing state
collaboration write scope / actor state
review task -> exact target binding
authority transition from current to successor architecture
```

Several cases may ultimately receive the same reviewer class. Diversity of relationship semantics is the selection objective; class balance is not.

## 4. Source-grounding rule

A reviewer must judge from the packet's actual source evidence plus frozen Requirements V0.2. The short case-facts sentence and question exist only to identify the relationship being judged. They do not outrank the excerpt.

A reviewer may request deeper source context if the packet is insufficient, but must then either:

```text
record the additional exact source read in the judgment provenance
or
return UNRESOLVED if the protocol does not authorize enough evidence
```

The reviewer may not silently substitute remembered project context for the packet evidence.

## 5. Independence plan

The first judgment pair is ChatGPT and Claude. The independence target is reviewer-label non-exposure, not blindness to Research 124.

The intended sequence is:

```text
1. this corpus freezes at immutable commit X
2. ChatGPT judges all 15 cases and freezes its complete result as descendant Y
3. Claude is routed to exact X for substantive reads
4. descendant ChatGPT labels/results are explicitly excluded from Claude's evidence boundary
5. Claude freezes all 15 judgments
6. only then are the two judgment sets compared
```

This reproduces the useful independence discipline from MC-0013 without pretending that either model is blind to the architecture problem itself.

## 6. Required reviewer output per case

Each reviewer must return exactly one primary label and:

```text
confidence: HIGH / MEDIUM / LOW
rationale tied to source evidence
proposed_natural_owner_or_null
independent_continuity_basis_or_null
derived_inputs_or_null
missing_evidence_or_null
```

Physical storage technology is out of scope at this stage.

## 7. Corpus validation completed

Before freeze, a deterministic check verified:

```text
15 case ids present
every source file exists in the frozen source state
every recorded source SHA-256 and Git blob SHA match the frozen Git blob bytes
every excerpt exactly matches its recorded line range
no prohibited answer-bearing field occurs at case level
corpus SHA-256 matches cc61a9610b2a88b8be6c3af06b661c6ce270e094e380d1d362dc8f10d8f90ed5
```

## 8. Current disposition

```text
REAL_CORPUS_V01=MACHINE_FROZEN
CORPUS_SHA256=cc61a9610b2a88b8be6c3af06b661c6ce270e094e380d1d362dc8f10d8f90ed5
CHATGPT_JUDGMENT=NOT_STARTED_AT_FREEZE
CLAUDE_JUDGMENT=NOT_STARTED_AT_FREEZE
MECHANIZED_RULE=NOT_STARTED
REQUIREMENTS_V02=UNCHANGED_FROZEN
TARGET_ARCHITECTURE=NOT_SELECTED
NEXT=CHATGPT_INDEPENDENT_JUDGMENT_SET
```
