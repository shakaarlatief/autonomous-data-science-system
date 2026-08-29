# Checkpoint 265: Development Method v0.6 Knowledge Routing and Verification Reconciliation

**Date:** 2026-08-29  
**Status:** IMPLEMENTED / FINAL VALIDATION OPEN  
**Checkpoint class:** DEVELOPMENT_METHOD / KNOWLEDGE_ARCHITECTURE / VERIFICATION  
**Project stage:** V1 next-generation Project Cockpit design exploration with repository-scale preservation-method reconciliation  
**Scope:** Promotes Development Method v0.6, restores the project-wide evergreen Knowledge Map, introduces structural map validation and risk-scaled Cockpit verification, and reduces micro-checkpoint/CI churn without changing the active Cockpit product decision.  
**Authority:** Governing development-method checkpoint. Product semantics remain governed by their existing accepted specifications/foundations and the still-open Checkpoint 264 human review.  
**Interaction environment:** ChatGPT  
**Project / workspace:** Autonomous Data Science System  
**Interaction session:** `chatgpt-10`  
**Conversation title:** `10 - Project Cockpit Design Exploration`  
**Primary collaborator:** ChatGPT

## 1. Audit result

Research 103 establishes that substantive ADS knowledge remains strongly preserved, but two scaling problems had become real:

```text
Knowledge discoverability
    global KNOWLEDGE_MAP drifted from an evergreen project library
    into a Cockpit-current-state document

Development verification
    complete 78-test Cockpit gate was being paid repeatedly
    during tiny local visual iterations
```

A third process drift was also confirmed: recent frontend micro-adjustments were producing more numbered checkpoints than the existing checkpoint policy intended.

## 2. Development Method v0.6

`docs/DEVELOPMENT_METHOD.md` is promoted to v0.6.

New governing additions:

```text
V0-V4 risk-scaled verification ladder
conservative full-gate fallback for unknown blast radius
human visual review before expensive full closure gates for low-risk tuning
[full-cockpit] explicit full-gate marker
subsystem/targeted verification while iterating
full integrated verification at meaningful acceptance/promotion boundaries
checkpoint aggregation for micro-iterations within one review question
coherent multi-file state transitions where practical
evergreen topic-library obligation for KNOWLEDGE_MAP
```

No existing fidelity/provenance guarantee is removed.

## 3. Knowledge Map restoration

`docs/KNOWLEDGE_MAP.md` again has two separate layers:

```text
Current continuation route
Evergreen topic library
```

The evergreen library covers seventeen stable topic families across the entire ADS project and routes each topic to relevant canonical, foundational, specification, research, checkpoint and specialized-index evidence.

This restores the library behavior remembered by the project owner while retaining a small current continuation route at the top.

## 4. Structural map guard

Added:

```text
scripts/check_knowledge_map.py
.github/workflows/knowledge-map-integrity.yml
```

The validator protects the existence and path integrity of the topic library without pretending to automate semantic authority resolution.

## 5. Adaptive Cockpit verification

Added:

```text
scripts/select_cockpit_verification.py
```

Updated:

```text
.github/workflows/cockpit-reintegration-fidelity.yml
```

The selector uses safe path-based narrowing for high-confidence local surfaces and defaults to full V3 verification for shared, mixed or unknown changes.

The workflow also cancels obsolete in-progress runs for the same branch/ref.

This method change itself explicitly forces one complete Cockpit run through the `[full-cockpit]` commit marker because the verification architecture is being changed.

## 6. Checkpoint aggregation rule

Small fixes within one already-open review question should normally be recorded as iterations inside that boundary rather than creating a new checkpoint number after each commit.

A new checkpoint is warranted when something material changes, for example:

```text
human acceptance/rejection changes current truth
review scope changes
risk/verification boundary changes
new reusable technical finding deserves preservation
stage/branch/promotion state changes
continuation point materially changes
```

Git remains the exact low-level implementation history.

## 7. Continuity alignment

`docs/CONTINUITY.md` is aligned to the current provider-neutral interaction identity:

```text
chatgpt-10
10 - Project Cockpit Design Exploration
```

New-session reconstruction now explicitly uses the evergreen topic library after reading current routing, so future sessions can discover related knowledge by topic rather than by remembered document number.

## 8. Product boundary unchanged

This checkpoint is a Level-2 development-method transition, not a Cockpit product decision.

The active product gate remains:

```text
Checkpoint 264
General project discussion footprint / selected-surface human recheck
```

If that visual result is confirmed, the next product action remains resuming Checkpoint 258 / Research 097 Adaptive Conversation Dock review.

Production `/cockpit` remains untouched.

## 9. Promotion audit

Promoted:

```text
docs/DEVELOPMENT_METHOD.md            -> v0.6
docs/CONTINUITY.md                    -> v0.6-aligned reconstruction
docs/KNOWLEDGE_MAP.md                 -> current route + evergreen library
Research 103                          -> durable audit/rationale
Checkpoint 265                        -> current method transition
adaptive Cockpit selector/workflow    -> operational verification implementation
knowledge-map validator/workflow      -> operational discoverability guard
```

Not promoted:

```text
new Foundation                         not required; Foundation 014 remains valid
new product Specification              not a product contract change
semantic/vector knowledge database     not justified
per-micro-change checkpointing         explicitly not selected
```

## 10. Final validation gate

Because the verification architecture itself changed, this method transition requires one full V3 Cockpit gate plus the relevant lightweight repository validators.

Expected final evidence:

```text
Cockpit reintegration fidelity    full V3 pass
Knowledge map integrity           pass
Current routing consistency       pass
Checkpoint metadata               pass
```

After those gates pass, Checkpoint 265 may be marked COMPLETE without another full Cockpit run.
