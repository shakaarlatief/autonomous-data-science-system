# Checkpoint 266: Repository Information Architecture and Exhaustive Knowledge Routing

**Date:** 2026-08-29  
**Status:** COMPLETE / VALIDATED  
**Checkpoint class:** DEVELOPMENT_METHOD / KNOWLEDGE_ARCHITECTURE / CONTINUITY  
**Project stage:** V1 next-generation Project Cockpit design exploration with repository-scale preservation architecture refinement  
**Scope:** Separates structural, live-state and semantic navigation; introduces exhaustive durable-family topic routing and checkpoint-range coverage; repairs validation ownership and full-gate integrity; and reconciles the global canonical documents without changing the active Cockpit product decision.  
**Authority:** Governing Level-2 development-method checkpoint. Product semantics remain governed by existing accepted specifications/foundations and the still-open Checkpoint 264 human review.  
**Interaction environment:** ChatGPT  
**Project / workspace:** Autonomous Data Science System  
**Interaction session:** `chatgpt-10`  
**Conversation title:** `10 - Project Cockpit Design Exploration`  
**Primary collaborator:** ChatGPT

## 1. Trigger

The repository owner requested a deeper full-architecture review after the v0.6 discoverability repair, with particular concern about three different questions being mixed together:

```text
What is happening right now?
What kinds of files exist and what is each for?
What knowledge do we have about a subject?
```

The audit confirmed that the underlying preservation layers remained strong, but the global navigation surfaces still overlapped enough to create future drift risk.

## 2. Research basis

Research 104 performed the repository-scale follow-up audit across:

```text
canonical global docs
all 24 numbered Foundations
all 24 numbered Specifications
all numbered Research records
checkpoint policy/inventory
specialized indexes
current routing / Knowledge Map validators
current Cockpit verification workflow
```

Result:

```text
substantive preservation    strong
structural discoverability  required clearer ownership
semantic discoverability    required exhaustive durable-family routing
current-state duplication   unnecessary and risky
heavy semantic database     not justified
```

## 3. Development Method v0.7

`docs/DEVELOPMENT_METHOD.md` is promoted to v0.7.

Global responsibilities are now explicit:

```text
README.md              stable landing page
docs/README.md         structural repository/documentation guide
CURRENT_STATE.md       sole human-readable live state
current_routing.json   sole machine-readable live pointer
KNOWLEDGE_MAP.md       evergreen subject library
CONTINUITY.md          reconstruction/recovery procedure
DEVELOPMENT_METHOD.md  operational development method
MAJOR_CHANGES.md       selective structural history
```

The v0.6 V0-V4 risk-scaled verification ladder and micro-checkpoint aggregation remain accepted.

## 4. Structural guide

Added:

```text
docs/README.md
```

It defines the purpose, authority and lifecycle of canonical global docs, foundations, specifications, research, checkpoints, specialized indexes, code, tests, schemas, migrations, scripts, experiments, Git and CI.

This is the canonical answer to “what kinds of files do we have and what are they for?”

## 5. Knowledge Map becomes semantic-only

`docs/KNOWLEDGE_MAP.md` no longer carries a live continuation section or current checkpoint/branch/test metadata.

Its sole job is:

```text
subject
    -> relevant canonical sources
    -> deep foundations
    -> specifications
    -> research/evidence
    -> important checkpoints
    -> specialized indexes/ledgers
```

A source may belong to multiple topics.

## 6. Exhaustive durable-family routing

The Knowledge Map explicitly routes every numbered file in:

```text
docs/foundations/
docs/specifications/
docs/research/
```

Every numbered checkpoint is additionally assigned through validated `KM-CHECKPOINT-RANGE` records, while important checkpoints remain directly linked under relevant subjects.

Specialized indexes remain first-class retrieval surfaces and are routed rather than duplicated.

## 7. Validation architecture

`check_knowledge_map.py` now validates:

```text
stable topic IDs
non-empty topic routing
all routed paths resolve
all numbered Foundations routed
all numbered Specifications routed
all numbered Research records routed
all numbered checkpoint numbers covered by semantic ranges
checkpoint range topic IDs valid
specialized indexes reachable
live current-state markers absent from KNOWLEDGE_MAP
```

`check_current_routing.py` requires live synchronization only between:

```text
current_routing.json
CURRENT_STATE.md
current checkpoint file existence
```

The validator no longer forces live state into root README or Knowledge Map.

## 8. Canonical global-document reconciliation

The closure audit also checked the purpose and currentness of the global canonical files rather than assuming that correct architecture implied current content.

Retained without structural redesign:

```text
DECISIONS.md
    explicit accepted project-level decisions and supersession history

PRINCIPLES.md
    stable cross-project working principles

DEVELOPMENT_METHOD.md
    operational Level-2 method

CONTINUITY.md
    reconstruction/rotation/recovery procedure
```

Reconciled because current canonical content had become stale:

```text
VISION.md
    removed obsolete immediate-next-experiment/current-state material
    restored stable long-term system direction
    incorporated durable Source Universe and collaboration architecture

OPEN_QUESTIONS.md
    updated through Specifications 021/022 and current Knowledge/Source Universe state
    corrected Q-022 from unresolved source persistence to the actual remaining
    source-vault and source-to-accepted-knowledge questions

MAJOR_CHANGES.md
    added Cockpit exact-implementation-provenance recovery
    added Development Method v0.7 information-architecture transition

model_collaboration/README.md
    aligned protocol authority wording with current Development Method v0.7
```

The audit did not justify merging these files. Their distinct jobs remain useful.

## 9. Historical metadata repair

Checkpoints 263 and 264 received metadata-only header repair to satisfy the provider-neutral contract. Their substantive historical content was unchanged.

## 10. Full-gate invocation defect and repair

The first forced-full v0.6 Cockpit workflow was inspected and found to have executed only 16 tests, not the expected complete 78-test family.

Cause:

```text
quoted glob from selector output
    -> passed literally through workflow interpolation
    -> requested V3 narrowed unintentionally
```

That green run is not accepted as V3 evidence.

The workflow was repaired to separate explicit full-mode execution from narrowed-mode execution. Verification tier is now determined by what tests actually executed.

## 11. Final validation evidence

All required closure gates are satisfied.

### Knowledge Map integrity

The first v0.7 run exposed one parser defect only: a Markdown inline-code backtick was retained on a routed path token. The parser was corrected without changing the semantic map.

Final evidence:

```text
fix commit   0791eb1d0569a85aed37fdcb218b0c49835db2e9
workflow     33256989165
job          99112350334
result       SUCCESS
```

### Current routing consistency

```text
workflow     33256097893
Windows job  99109955121   SUCCESS
Ubuntu job   99109955151   SUCCESS
```

### Checkpoint metadata

```text
workflow     33256097922
job          99109955176
result       SUCCESS
```

### Genuine full Cockpit V3

The repaired full-mode command executed the actual complete family:

```text
npx playwright test e2e/cockpit-reintegration*.spec.ts
```

Evidence:

```text
implementation/method target  9182483af4686037ef2fe9341c31fa0e4de31332
workflow                      33256097920
job                           99109955347
browser tests                 78 / 78 PASS
```

The logs explicitly report `Running 78 tests` and `78 passed`.

Checkpoint 266 is therefore closed as `COMPLETE / VALIDATED`.

## 12. Relationship to Checkpoint 265

Checkpoint 265 was a valid intermediate repair: it restored broad topic routing and introduced risk-scaled verification.

Its two-layer Knowledge Map and unfinished validation boundary are refined and superseded by the stronger v0.7 architecture here. No scientific/product conclusion from Checkpoint 265 is rewritten.

## 13. Product boundary unchanged

This is a Level-2 repository/development-method checkpoint.

The active Cockpit product gate remains Checkpoint 264:

```text
General project discussion
    same visible footprint as WorkUnit boxes
    selected frame on visible project box only

WorkUnit conversation
    selected frame on visible WorkUnit surface only

existing spacing
    remains correct
```

If human-confirmed, resume Checkpoint 258 / Research 097 Adaptive Conversation Dock review.

Production `/cockpit` remains untouched.

## 14. Promotion audit

Promoted/current:

```text
Development Method v0.7
docs/README.md structural guide
semantic-only exhaustive KNOWLEDGE_MAP
reconciled VISION / OPEN_QUESTIONS / MAJOR_CHANGES
risk-scaled verification with actual-execution V3 integrity
Research 104
Checkpoint 266
```

Not promoted:

```text
semantic/vector repository database
one monolithic canonical document
per-commit checkpointing
new Cockpit product decision
new scientific conclusion from Specification 022
```

## 15. Exact continuation

The Level-2 architecture review is complete.

The next product action remains the already-open human Checkpoint 264 visual recheck. A second-model architecture review may be opened as a non-blocking collaboration obligation against this frozen v0.7 result; such a review does not reopen Checkpoint 266 unless it produces a substantive finding that warrants revision.
