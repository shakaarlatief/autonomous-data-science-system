# Current State

**Checkpoint:** 266  
**Date:** 2026-08-29  
**Active development branch:** `v1-cockpit-design-exploration`  
**Active PR:** none  
**Promoted V1 integration branch:** `v1-frontend-spike` at `ed5b60bdc882bed0799ce55228ce8187f9c55aa1`  
**Latest specification:** Specification 024 remains accepted. Specification 008 remains the promoted V1 Project Cockpit interaction architecture.  
**Latest scientific experiment:** Specification 022 remains `INCOMPLETE / EXECUTION INTEGRITY FAILED`; no GENERIC / ADS_HORIZON / ORACLE_HORIZON comparison may be inferred from that run.

## Active interaction context

```text
Interaction environment  ChatGPT
Project / workspace      Autonomous Data Science System
Interaction session      chatgpt-10
Conversation title       10 - Project Cockpit Design Exploration
Primary collaborator     ChatGPT
Product collaboration    MC-0004
Pending model review     MC-0005
```

Repository artifacts remain authoritative across chats and models.

## Development-method boundary

Checkpoint 266 is `COMPLETE / VALIDATED`.

Development Method v0.7 gives the global repository surfaces distinct owners:

```text
README.md              stable repository landing page
docs/README.md         repository/documentation structure and artifact roles
CURRENT_STATE.md       human-readable live project state
current_routing.json   machine-readable live routing pointer
KNOWLEDGE_MAP.md       evergreen semantic subject -> knowledge library
CONTINUITY.md          reconstruction / rotation / recovery procedure
DEVELOPMENT_METHOD.md  method used to build, verify and preserve ADS
MAJOR_CHANGES.md       selective structural history
```

The semantic Knowledge Map is exhaustively guarded for numbered Foundations, Specifications and Research records, with semantic checkpoint-range coverage and specialized-index reachability.

The canonical global-document reconciliation also completed:

```text
VISION.md
    stable high-level direction; obsolete immediate-next-step content removed

PRINCIPLES.md
    retained as stable working principles

DECISIONS.md
    retained as explicit decision/supersession ledger

OPEN_QUESTIONS.md
    reconciled through current V1 evidence, including Specification 022
    and the accepted Source Universe boundary

MAJOR_CHANGES.md
    updated with Cockpit implementation-provenance recovery and v0.7

model collaboration protocol
    retained and aligned to current Development Method v0.7
```

No monolithic documentation file or heavier semantic repository database was justified.

## Checkpoint 266 validation evidence

### Knowledge Map integrity

Initial parser-fix evidence:

```text
fix commit   0791eb1d0569a85aed37fdcb218b0c49835db2e9
workflow     33256989165
job          99112350334
result       SUCCESS
```

Final closure commit revalidation:

```text
closure commit  c834d8298b86a0185ffcc0ffa62d0e9c178cc2ad
workflow        33257341284
job             99113261829
result          SUCCESS
```

The initial failure was a Markdown inline-code parser defect, not missing semantic routing.

### Current routing consistency

Final closure revalidation:

```text
workflow     33257341243
Ubuntu job   99113261741   SUCCESS
Windows job  99113261861   SUCCESS
```

### Checkpoint metadata

Final closure revalidation:

```text
workflow     33257341238
job          99113261672
result       SUCCESS
```

### Genuine full Cockpit V3

```text
implementation/method target  9182483af4686037ef2fe9341c31fa0e4de31332
workflow                      33256097920
job                           99109955347
browser tests                 78 / 78 PASS
```

The actual command was:

```text
npx playwright test e2e/cockpit-reintegration*.spec.ts
```

and the logs explicitly report `Running 78 tests` and `78 passed`.

The later Checkpoint 266 closure commit was correctly classified as documentation-only by the Cockpit selector:

```text
workflow  33257341234
job       99113261838
result    SUCCESS / browser execution skipped
```

The earlier v0.6 run that executed only 16 tests is not accepted as V3 evidence.

## Non-blocking second-model architecture review

The finalized v0.7 architecture is now frozen for a direct Claude adversarial review at:

```text
c834d8298b86a0185ffcc0ffa62d0e9c178cc2ad
```

Collaboration thread:

```text
MC-0005
```

Purpose:

```text
challenge global-file role separation
challenge semantic Knowledge Map design and exhaustive routing
challenge checkpoint-range routing
challenge authority/supersession clarity
challenge validator maintenance cost
challenge order-of-magnitude scaling behavior
propose the strongest simpler alternative if one exists
```

This review is optional/non-blocking for product continuation. Checkpoint 266 remains complete unless a later Claude finding is substantively accepted and warrants revision.

Claude can only write to the declared MC-0005 message surface. ChatGPT remains task owner for later disposition.

## Current Cockpit product boundary remains Checkpoint 264

The repository/development-method reconciliation did not reopen or change the Cockpit product design.

Latest human-confirmed state:

```text
Conversation WorkUnit spacing
    correct

General project discussion containment
    correct

current-process Focus
    working as far as tested
```

Still awaiting human visual confirmation:

```text
General project discussion visible footprint
    matches WorkUnit box footprint

Boxes selected-state frame
    frames the actual visible selected project/WorkUnit object
    no oversized structural row frame
```

Governing product evidence:

```text
docs/checkpoints/264_project_general_footprint_and_selection_frame_human_recheck_opened.md
docs/research/102_project_general_box_footprint_and_selection_frame_alignment.md
```

Normal review route:

```text
http://localhost:4173/design-lab/cockpit-reintegration.html
```

If Checkpoint 264 is visually confirmed, close the Conversation presentation-integrity interruption and resume the Adaptive Conversation Dock review from:

```text
docs/checkpoints/258_adaptive_conversation_dock_human_review_opened.md
docs/research/097_professional_conversation_copresence_and_adaptive_dock_study.md
```

Adaptive route:

```text
http://localhost:4173/design-lab/cockpit-reintegration.html?conversation=adaptive-dock
```

## Held product/scientific decisions

No Cockpit semantic/product decision is reopened by Checkpoint 266 or by the pending MC-0005 review. The held source-faithful Phase-C mechanism set, Quiet Graphite Conversation model, Boxes/Text navigation, A6, current-process Focus, Grid/X5/Deep Dive access, state preservation, L0 provisional status, semantic-zoom deferral and exact implementation-provenance architecture remain unchanged.

Implementation provenance remains governed by:

```text
docs/cockpit/ACCEPTED_IMPLEMENTATION_MANIFEST.md
docs/cockpit/accepted_implementation_manifest.json
```

The failed holistic browser at `8e554d847bb3b6318db432abcb5dff742f0fa523` remains diagnostic evidence only.

Source-vault bootstrap remains PAUSED, not cancelled. The Course 2 source-universe gate is unchanged.

Production `/cockpit` remains untouched.

## Exact next steps

Two independent continuations are now legitimate:

```text
PRODUCT
    human performs the already-open Checkpoint 264 visual recheck
    if correct, resume Adaptive Conversation Dock review

LEVEL-2 REVIEW
    Claude reviews frozen v0.7 target c834d829...
    review is non-blocking and may be processed when convenient
```

The product continuation does not need to wait for Claude.
