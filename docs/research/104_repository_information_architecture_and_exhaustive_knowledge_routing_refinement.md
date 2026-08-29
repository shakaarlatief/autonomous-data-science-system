# Research 104: Repository Information Architecture and Exhaustive Knowledge Routing Refinement

**Date:** 2026-08-29  
**Status:** ACCEPTED LEVEL-2 ARCHITECTURE REFINEMENT  
**Scope:** Repository-scale knowledge preservation, discoverability, navigation ownership and validation  
**Primary evidence:** Current repository tree, Foundation 014, Development Method v0.6, current navigation/canonical files, numbered Foundation/Specification/Research inventories, checkpoint metadata/routing validators and the v0.6 validation failure

## 1. Question

As ADS grows, is the current preservation architecture merely storing knowledge, or is it also organized so that a future collaborator can reliably discover the right knowledge without already remembering document numbers, recent conversations or repository history?

The follow-up question is whether the global files have sufficiently distinct jobs:

```text
What is happening now?
What kinds of artifacts exist and what do they mean?
What do we know about a particular subject?
How do I reconstruct the project after context loss?
How is ADS itself developed and preserved?
```

Research 103 established that substantive knowledge durability was strong but global discoverability had drifted. Development Method v0.6 restored a broad topic library and risk-scaled verification. The deeper audit here tests whether that repair itself is structurally clean enough for continued scale.

## 2. Repository-wide audit method

The audit inspected the current branch's repository/documentation architecture rather than relying on chat memory. It reviewed:

```text
root repository tree
root README
docs root
docs/CURRENT_STATE.md
docs/current_routing.json
docs/KNOWLEDGE_MAP.md
docs/CONTINUITY.md
docs/DEVELOPMENT_METHOD.md
docs/MAJOR_CHANGES.md
docs/checkpoints/README.md
Foundation 014
all 24 numbered Foundations
all 24 numbered Specifications
all 103 existing numbered Research records
current checkpoint inventory and metadata validator
specialized Cockpit / Methodological Knowledge / Source Universe /
model-collaboration indexes
current routing and Knowledge Map validators/workflows
current Cockpit verification workflow
```

The goal was not to maximize file count. The goal was to minimize ambiguity about where a future collaborator should look.

## 3. Finding: the repository had good layers but overlapping global navigation responsibilities

The core preservation layers are sound:

```text
canonical current truth
foundational rationale
bounded research evidence
explicit specifications
historical checkpoints
specialized domain indexes
code/tests
Git chronology
```

Foundation 014 already describes this separation well.

The problem was at the global navigation layer. After v0.6, `KNOWLEDGE_MAP.md` had two jobs:

```text
CURRENT CONTINUATION ROUTE
EVERGREEN TOPIC LIBRARY
```

That was a useful emergency correction to the previous Cockpit-heavy drift, but it still duplicated the responsibilities of `CURRENT_STATE.md` and `current_routing.json`.

At the same time, there was no dedicated structural document that answered the repository owner's recurring question:

> What kinds of files do we have, what is each family for, and which one should I trust for which purpose?

`DEVELOPMENT_METHOD.md` partially answered this, but its primary job is how work is performed, not serving as the repository's structural table of contents.

## 4. Finding: current-state duplication is a scaling risk

Before this refinement, live information appeared across several global files:

```text
README.md
CURRENT_STATE.md
current_routing.json
KNOWLEDGE_MAP.md
CONTINUITY.md
```

Examples included current checkpoint, active branch, review gate, promoted SHA and verification details.

This duplication creates two failure modes:

1. **drift risk**: one file advances while another remains stale;
2. **retrieval ambiguity**: a future collaborator cannot know which copy is the intended source of live truth.

The correct answer is not more synchronization logic. The simpler architecture is to give live state one human owner and one machine owner.

Selected ownership:

```text
CURRENT_STATE.md       sole human-readable live state
current_routing.json   sole machine-readable live routing pointer
```

Other global files point to those surfaces rather than copying volatile state.

## 5. Finding: structural navigation and semantic navigation are different problems

Two distinct questions had been mixed:

```text
STRUCTURAL
    What is a Foundation?
    What is a Research record?
    Where are tests?
    What does CURRENT_STATE own?

SEMANTIC
    Where is everything about missing data?
    What documents govern Cockpit selection?
    What evidence relates to provenance?
```

They should not share one giant table.

Selected architecture:

```text
docs/README.md
    repository/documentation structure
    artifact family -> purpose / authority / lifecycle

docs/KNOWLEDGE_MAP.md
    semantic library
    subject -> relevant repository knowledge
```

This matches the original intent of Foundation 014 more closely than the v0.6 two-layer map.

## 6. Finding: topic routing must be exhaustive enough to be trusted

A subject library is not a reliable gate to repository knowledge if major numbered knowledge records can silently exist outside it.

Therefore the global Knowledge Map now has a mechanical completeness contract for the three primary numbered durable-knowledge families:

```text
every docs/foundations/NNN_*.md      -> >=1 topic
every docs/specifications/NNN_*.md   -> >=1 topic
every docs/research/NNN_*.md         -> >=1 topic
```

A file may be assigned to multiple topics. This is intentionally supported because repository knowledge is not a strict tree. For example:

```text
Research 028
    system identity
    project state
    methodological knowledge universe
    recommendation/navigation context

Foundation 019
    reusable methodological knowledge
    retrieval / MethodologicalHorizon
    methodological knowledge universe
```

Multiple membership improves retrieval without duplicating source contents.

## 7. Checkpoints require a different scaling strategy

There are more than 260 numbered checkpoints. Listing every checkpoint path visibly under subjects would make the Knowledge Map difficult to use and would duplicate a directory whose purpose is chronological history.

But leaving checkpoints completely outside semantic routing would make a large part of preserved knowledge harder to rediscover.

Selected compromise:

```text
all checkpoint numbers
    assigned through compact KM-CHECKPOINT-RANGE topic records

important checkpoints
    additionally linked directly inside subject sections

exact chronology
    docs/checkpoints/ + specialized ledgers + Git
```

The validator checks that every numbered checkpoint currently present is covered by at least one semantic range. A range may assign multiple topic IDs.

This provides exhaustive topic ownership without turning `KNOWLEDGE_MAP.md` into a 267-entry chronological duplicate.

## 8. Specialized indexes remain first-class

The global map should not absorb domain indexes that already solve a narrower navigation problem well.

Examples:

```text
docs/methodological_knowledge/COVERAGE_MAP.md
docs/cockpit/PHASE_C_DECISION_LEDGER.md
docs/cockpit/ACCEPTED_IMPLEMENTATION_MANIFEST.md
docs/source_universe/PERMANENT_VAULT_BOOTSTRAP.md
docs/model_collaboration/REVIEW_INBOX.md
```

The global map guarantees that these specialized surfaces are reachable from relevant subjects. Their internal detail remains local to their domain.

## 9. Selected global information architecture

The refined architecture is:

```text
README.md
    stable entry point

docs/README.md
    structural repository/documentation guide

docs/CURRENT_STATE.md
    human-readable current state and exact continuation

docs/current_routing.json
    machine-readable current pointer

docs/KNOWLEDGE_MAP.md
    evergreen semantic subject library

docs/CONTINUITY.md
    reconstruction/rotation/recovery procedure

docs/DEVELOPMENT_METHOD.md
    operational method used to build/preserve ADS

docs/MAJOR_CHANGES.md
    selective structural history
```

This is not cosmetic renaming. It removes overlapping responsibilities that become dangerous as the project grows.

## 10. Validation architecture

`check_knowledge_map.py` is strengthened from a path/topic presence check into a coverage guard.

It now validates:

```text
required stable topic IDs exist
no duplicate topic IDs
each topic routes at least one repository path
all routed paths resolve
all numbered Foundations are routed
all numbered Specifications are routed
all numbered Research records are routed
all numbered checkpoints are covered by semantic checkpoint ranges
checkpoint ranges reference valid topic IDs
required specialized indexes remain reachable
live current-state headers/section do not reappear in KNOWLEDGE_MAP
```

The validator deliberately does **not** decide which source is semantically authoritative. Authority resolution still uses status, scope, chronology and accepted contracts.

## 11. Current-routing validation is simplified rather than expanded

The old current-routing validator required matching live fragments in:

```text
README.md
CURRENT_STATE.md
KNOWLEDGE_MAP.md
```

That requirement itself forced volatile duplication.

The refined validator checks:

```text
current_routing.json schema
current checkpoint file existence
CURRENT_STATE.md agreement with the manifest
```

The stable root README and semantic Knowledge Map no longer need to repeat live branch/checkpoint state.

This is a reduction in accidental coupling.

## 12. Verification-workflow integrity finding

The v0.6 architecture forced a full Cockpit V3 gate after changing verification selection. The workflow was green, but inspection showed that the supposed full invocation executed only 16 tests rather than the expected 78.

Cause:

```text
selector output contained a quoted glob
workflow interpolated it into a shell command
quoted pattern was passed literally instead of expanding as intended
```

Therefore:

```text
workflow says full
    !=
full suite actually executed
```

The v0.7 refinement treats verification tier as a property of the tests that actually ran. The workflow is changed so full mode has an explicit full-suite command, while narrowed modes use selector output.

One genuine post-fix V3 run is required before the Level-2 transition closes.

## 13. Checkpoint metadata repair

The audit also found that Checkpoints 263 and 264 predated the current provider-neutral metadata contract in their headers even though their substantive content remains valid.

They require metadata-only repair:

```text
add missing authority/provenance fields
preserve original substantive chronology and claims
```

This is exactly the kind of correction allowed by the checkpoint policy. It is not a reason to rewrite history.

## 14. Why no semantic/vector knowledge database is introduced

A repository-scale semantic index, vector database or generated dependency graph could eventually become useful. The current evidence does not justify it yet.

Observed problem:

```text
knowledge existed
manual/repository retrieval remained possible
navigation responsibilities drifted
important records were not exhaustively topic-routed
```

The smallest architecture that directly addresses that problem is:

```text
clear ownership
explicit subject routing
exhaustive durable-family coverage
lightweight deterministic validation
```

A heavier knowledge system should be introduced only when concrete retrieval failures remain after this architecture is used in practice.

## 15. Classification

```text
REPOSITORY_INFORMATION_ARCHITECTURE_REFINEMENT_SUPPORTED
```

Development Method v0.7 is justified as a Level-2 refinement.

The product/scientific state of ADS is unchanged by this research. In particular, the current Cockpit product human-review boundary remains the one already preserved at Checkpoint 264.

## 16. Promotion targets

Promote:

```text
new docs/README.md structural guide
DEVELOPMENT_METHOD.md -> v0.7
CONTINUITY.md -> single-responsibility reconstruction procedure
KNOWLEDGE_MAP.md -> evergreen semantic library only
CURRENT_STATE/current_routing -> exclusive live-state owners
check_knowledge_map.py -> exhaustive coverage validator
current-routing validator -> CURRENT_STATE-only live agreement
Cockpit workflow -> explicit full-suite invocation
Checkpoint 266 -> Level-2 transition and validation boundary
```

Do not promote:

```text
new Foundation
    Foundation 014 remains valid and is clarified operationally

new product Specification
    no target-product contract changed

semantic/vector knowledge database
    no observed need yet

hundreds of visible checkpoint links
    semantic checkpoint ranges provide the scalable route
```
