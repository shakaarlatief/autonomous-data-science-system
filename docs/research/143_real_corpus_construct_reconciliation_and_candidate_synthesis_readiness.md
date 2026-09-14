# Research 143: Real-Corpus Construct Reconciliation and Candidate-Synthesis Readiness

**Date:** 2026-09-14
**Status:** MC-0015 RESOLVED / REAL-CORPUS CONSTRUCT CORRECTED / WHOLE-ARCHITECTURE CANDIDATE SYNTHESIS READY / TARGET ARCHITECTURE NOT SELECTED
**Scope:** Reconcile Claude Message 003 with the first real ADS corpus, retire the construct-invalid four-way label taxonomy, freeze the corrected semantic-unit plus two-axis model for subsequent architecture reasoning, and determine whether further admission-classifier work is warranted before whole-architecture synthesis.
**Authority:** Supporting Research 124 architecture evidence and experiment-method correction. Requirements V0.2 remain the frozen candidate-acceptance authority. No target architecture or physical storage technology is selected here.
**Declared references:** `research:124`, `research:139`, `research:140`, `research:141`, `research:142`, `path:docs/model_collaboration/threads/MC-0015/messages/001_claude_independent_real_corpus_judgment.md`, `path:docs/model_collaboration/threads/MC-0015/messages/003_claude_comparative_construct_validity_review.md`, `path:docs/model_collaboration/threads/MC-0015/messages/004_chatgpt_construct_reconciliation_and_thread_close.md`, `path:docs/research/PROJECT_KNOWLEDGE_ARCHITECTURE_REQUIREMENTS_V02.md`, `checkpoint:487`

## 1. Why MC-0015 changes the conceptual model

The first real-corpus exercise removed the answer-bearing synthetic flags that invalidated V0.2's admission-selectivity claim. That stronger protocol then exposed a different construct defect.

The original response taxonomy treated these as mutually exclusive:

```text
SOURCE_LOCAL
FIRST_CLASS_SEMANTIC_OBJECT
DERIVED_ONLY
UNRESOLVED
```

Claude Message 003 confirms that this mixes at least two questions:

```text
does the semantic thing itself need durable continuity?
where does authoritative state about that thing live?
```

RC-005 proves the overlap concretely. A workstream can have durable semantic identity while one repository artifact remains its natural authoritative source.

RC-006 exposes a second problem: one case can silently combine the semantic object and a view over several objects. The individual workstreams may be durable objects, while the aggregate active/paused/next answer is derived.

Therefore the project must define the semantic unit before applying any ownership/reification classification.

## 2. Corrected semantic judgment model

### Step 0: singular semantic unit

Every architecture-ownership judgment must first identify exactly one semantic unit or queried proposition.

Do not combine:

```text
an object's own state
and
a projection/view over several objects
```

inside one label.

If a packet contains both, split it before judging.

### Axis I: semantic continuity / identity

```text
DURABLE_IDENTITY
    the semantic unit must remain recognizable across material state changes,
    carrier replacement, pause/resume, merge/split or other representation changes

NO_SEPARATE_IDENTITY
    the unit does not need continuity distinct from the authoritative facts that state it

UNRESOLVED
    available evidence does not support a safe continuity decision
```

This is semantic identity, not physical file identity.

### Axis A: authority mode / home

```text
SINGLE_SOURCE
    one canonical semantic source can honestly state the authoritative fact completely

JOINT_AUTHORITY
    a jointly governing source set is intentionally required and reducing the fact to one
    source would lose semantics or create false ownership

DERIVED_ONLY
    the queried state/relation is deterministically rebuildable from authoritative inputs
    and should not become another unique authoritative truth surface

UNRESOLVED
    evidence does not safely establish the authority mode
```

`SINGLE_SOURCE` is intentionally representation-neutral. A first-class relation or workstream may itself have one canonical source. That does not make it less first-class.

`JOINT_AUTHORITY` is also representation-neutral. It does not imply a central database, graph or semantic spine.

## 3. RC-005 corrected result

```text
semantic unit    Cockpit workstream
Axis I           DURABLE_IDENTITY
Axis A           SINGLE_SOURCE
source           docs/cockpit/README.md
```

This is the central construct lesson:

> **First-class semantic identity and single-source authority are compatible.**

The old taxonomy forced a false choice between them.

## 4. RC-006 corrected result

The packet must be decomposed.

For each individual project-development workstream/initiative:

```text
Axis I           plausibly DURABLE_IDENTITY
Axis A           plausibly SINGLE_SOURCE
```

For the aggregate current route answer:

```text
semantic unit    active/paused/next continuation projection
Axis I           NO_SEPARATE_IDENTITY for the projected current answer
Axis A           DERIVED_ONLY
```

The global route can therefore be rebuilt from explicit workstream state without becoming another authority surface.

## 5. RC-012 correction of record

Claude explicitly audits its own independent RC-012 `SOURCE_LOCAL / HIGH` judgment as protocol-nonconforming.

The frozen packet did not state whether `current_routing.json` is canonical, derived or mixed. Claude's rationale relied on accumulated project familiarity while declaring no extra source reads.

The original independent artifact remains immutable evidence of what happened. The packet-only disposition is:

```text
Axis I           UNRESOLVED
Axis A           UNRESOLVED
```

A later enriched packet may answer the question, but it cannot retroactively repair the independent experiment.

## 6. Real-corpus result after construct correction

The original 12/15 exact label agreement remains useful provenance but is not the final semantic model because the label space itself was flawed.

The stronger surviving evidence is case-level:

```text
source-local/single-source patterns independently supported
    scoped supersession
    multi-successor scoped supersession
    governing contract relations
    reopen triggers
    review-base / exposure bookkeeping
    provenance to evidence
    public/private authority policy
    collaboration write/actor state
    review target binding
    sampled architecture-transition policy

derived-only patterns independently supported
    same-branch CI obsolescence
    Knowledge Map subject membership

first-class identity with one natural source
    Cockpit workstream
    plausibly the individual workstreams inside RC-006
```

No clearly grounded real case in Corpus V0.1 requires `JOINT_AUTHORITY` or a new cross-object authority substrate.

## 7. What this means for the earlier H1/H2 question

The evidence no longer supports treating H1 and H2 as the right top-level split.

The useful distinctions are now:

```text
semantic continuity / identity
single-source versus joint authority
unique authority versus derived projection
physical representation
```

These are not the same axis.

A repository-native first-class workstream or relation can still be single-source. Conversely, a fact may involve several objects yet remain derived-only. A joint-authority case, if it appears, can be represented without assuming one global central spine.

The original H2 insight survives only as a bounded possibility:

> some semantic units may need their own identity or a jointly governing authority structure.

The broad “cross-object facts belong in a spine” formulation does not survive the full evidence sequence.

## 8. Architecture family now favored for serious synthesis

The evidence field now favors a representation-neutral family with the following shape:

```text
rich repository-native semantic sources remain primary
stable semantic identity is selective
semantic identity does not imply centralization
ordinary directional facts live with one natural source
first-class workstreams/relations may still have one canonical source
joint-authority support exists as an exception for cases that genuinely require it
derived routing/search/current-state/closure views are rebuildable
capture remains non-authoritative until promotion
current versus historical surfaces remain separated
```

This is best understood as a **repository-native semantic object + derived-view architecture**, not a global registry architecture.

It is still an architecture hypothesis, not the selected target.

## 9. Why another admission classifier is not the next step

The project now knows enough to avoid an immediate mechanized “should this be reified?” classifier.

The main remaining uncertainty is not whether a small rule can imitate a label set. It is whether the whole proposed architecture satisfies all 50 KA-R and 17 KA-I requirements economically, including:

```text
bootstrap/reconstruction
capture/promotion
identity continuity
workstream DAG/resume
joint authority/conflict handling
temporal/supersession semantics
public/private delegation
freshness and derived-view rebuildability
active-surface consolidation
concurrency and migration
```

The next high-value task is therefore whole-architecture synthesis followed by systematic requirement qualification and targeted falsification of weak areas.

A later real hard-case corpus can still be valuable if candidate qualification exposes a specific uncertainty around `DURABLE_IDENTITY + JOINT_AUTHORITY`.

## 10. Research program disposition

```text
MC0015=RESOLVED
FOUR_WAY_REAL_CORPUS_TAXONOMY=RETIRED
SEMANTIC_UNIT_RULE=FROZEN_FOR_FUTURE_REASONING
AXIS_I_SEMANTIC_IDENTITY=FROZEN_FOR_FUTURE_REASONING
AXIS_A_AUTHORITY_MODE=FROZEN_FOR_FUTURE_REASONING
REAL_CORPUS_SOURCE_LOCAL_DEFAULT=SUPPORTED
REAL_CORPUS_DERIVED_VIEW_PATTERN=SUPPORTED
REAL_DURABLE_IDENTITY_PLUS_SINGLE_SOURCE=SUPPORTED_BY_WORKSTREAM_CASE
REAL_DURABLE_IDENTITY_PLUS_JOINT_AUTHORITY=NOT_DEMONSTRATED
MECHANIZED_ADMISSION_CLASSIFIER=DEFERRED
REQUIREMENTS_V02=UNCHANGED_FROZEN
TARGET_ARCHITECTURE=NOT_SELECTED
NEXT=WHOLE_ARCHITECTURE_CANDIDATE_SYNTHESIS_AND_REQUIREMENT_QUALIFICATION
```
