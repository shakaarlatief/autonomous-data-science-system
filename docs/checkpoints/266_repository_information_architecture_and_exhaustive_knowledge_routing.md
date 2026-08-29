# Checkpoint 266: Repository Information Architecture and Exhaustive Knowledge Routing

**Date:** 2026-08-29  
**Status:** IMPLEMENTED / FINAL VALIDATION OPEN  
**Checkpoint class:** DEVELOPMENT_METHOD / KNOWLEDGE_ARCHITECTURE / CONTINUITY  
**Project stage:** V1 next-generation Project Cockpit design exploration with repository-scale preservation architecture refinement  
**Scope:** Separates structural, live-state and semantic navigation; introduces exhaustive durable-family topic routing and checkpoint-range coverage; repairs validation ownership; and carries forward the final v0.6 verification closure without changing the active Cockpit product decision.  
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

The audit confirmed that the underlying preservation layers remain strong, but the global navigation surfaces still overlapped enough to create future drift risk.

## 2. Research basis

Research 104 performed the repository-scale follow-up audit across:

```text
canonical global docs
all 24 numbered Foundations
all 24 numbered Specifications
all existing numbered Research records
checkpoint policy/inventory
specialized indexes
current routing / Knowledge Map validators
current Cockpit verification workflow
```

Result:

```text
substantive preservation    strong
structural discoverability  needs clearer ownership
semantic discoverability    needs exhaustive durable-family routing
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

## 4. New structural guide

Added:

```text
docs/README.md
```

It defines the purpose, authority and lifecycle of:

```text
canonical global docs
foundations
specifications
research
checkpoints
specialized domain indexes
src / frontend / schemas / migrations / scripts / tests / experiments
Git and CI roles
```

This is now the canonical answer to “what kinds of files do we have and what are they for?”

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

The Knowledge Map now explicitly routes every numbered file in:

```text
docs/foundations/
docs/specifications/
docs/research/
```

This converts the map from a manually helpful index into a mechanically completeness-guarded semantic library for the project's primary durable knowledge families.

## 7. Scalable checkpoint routing

Every numbered checkpoint is semantically assigned through validated `KM-CHECKPOINT-RANGE` records.

This avoids two bad extremes:

```text
no checkpoint semantic routing
    -> history becomes hard to rediscover by topic

hundreds of visible checkpoint links
    -> Knowledge Map becomes a duplicate chronological directory
```

Important checkpoints remain directly linked under relevant topics; exact chronology remains in `docs/checkpoints/`, specialized ledgers and Git.

## 8. Specialized indexes retained

The global map continues to route into, rather than duplicate:

```text
docs/methodological_knowledge/COVERAGE_MAP.md
docs/cockpit/PHASE_C_DECISION_LEDGER.md
docs/cockpit/ACCEPTED_IMPLEMENTATION_MANIFEST.md
docs/source_universe/PERMANENT_VAULT_BOOTSTRAP.md
docs/model_collaboration/REVIEW_INBOX.md
```

## 9. Validation changes

`check_knowledge_map.py` is strengthened to validate:

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

`check_current_routing.py` is simplified so live synchronization is required only between:

```text
current_routing.json
CURRENT_STATE.md
current checkpoint file existence
```

The validator no longer forces live state into root README or Knowledge Map.

## 10. Historical metadata repair

Checkpoints 263 and 264 receive metadata-only header repair to satisfy the current provider-neutral contract.

Their substantive historical content is unchanged.

## 11. v0.6 full-gate invocation defect

The first forced-full v0.6 Cockpit workflow was inspected and found to have executed only 16 tests, not the expected complete 78-test family.

Cause:

```text
quoted glob from selector output
    -> passed literally through workflow interpolation
    -> requested V3 narrowed unintentionally
```

That green run is not accepted as V3 evidence.

The workflow now has an explicit full-mode command and a separate narrowed-mode command. This method transition carries forward the requirement for one genuine full V3 pass.

## 12. Product boundary unchanged

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

## 13. Relationship to Checkpoint 265

Checkpoint 265 was a valid intermediate repair: it restored broad topic routing and introduced risk-scaled verification.

Its two-layer Knowledge Map and final validation boundary are refined/superseded here before closure. Checkpoint 265's pending validation obligation is therefore rolled forward to this stronger checkpoint rather than paid twice.

No separate Checkpoint 267 should be created merely to fix validation details inside this same Level-2 boundary.

## 14. Final validation gate

Required closure evidence:

```text
Knowledge map integrity           PASS
Current routing consistency       PASS
Checkpoint metadata               PASS
Cockpit reintegration fidelity    genuine full V3 PASS
```

The full Cockpit gate is forced on the implementation commit because the verification workflow itself changes.

After these gates pass, this checkpoint may be marked COMPLETE with a documentation-only V0 closure update. The Cockpit product human-review state remains separate.
