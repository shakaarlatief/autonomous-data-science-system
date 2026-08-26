# Current State

**Checkpoint:** 219  
**Date:** 2026-08-26  
**Active development branch:** `v1-cockpit-design-exploration`  
**Active PR:** none  
**Exploration branch base:** `v1-frontend-spike` at Checkpoint 205 head `2480109fadeee1e480ef03b82e335aacdf9adf91`  
**Promoted V1 integration branch:** `v1-frontend-spike` at feature-promotion head `ed5b60bdc882bed0799ce55228ce8187f9c55aa1`  
**Development stage:** MC-0004 Phase C browser-rendered Project Cockpit design evaluation. G4 is provisionally settled. H4 generic rest/hover interaction lighting is sufficiently settled. The first W1-W4 work-unit category/silhouette experiment received a positive preliminary human review, its Project Scene view-switching defect was corrected, and a bounded Claude divergent-ideation request is now pending before work-unit grammar convergence. The permanent source-vault bootstrap remains deliberately paused.  
**Latest specification:** Specification 024 remains accepted. Specification 008 remains the promoted V1 Project Cockpit interaction architecture.  
**Latest scientific experiment:** Specification 022 remains `INCOMPLETE / EXECUTION INTEGRITY FAILED`; no scientific comparison may be inferred from that run.

## Active interaction context

```text
Interaction environment  ChatGPT
Project / workspace      Autonomous Data Science System
Interaction session      chatgpt-08
Conversation title       08 - Project Cockpit Design Exploration
Primary collaborator     ChatGPT
```

Previous ChatGPT conversation is `chatgpt-07 / 07 - Project Cockpit Design Exploration` and ended unexpectedly at the product context limit. Repository-only reconstruction succeeded because the substantive H4 correction had already been preserved.

Current Claude collaboration session remains `claude-01 / 01 - ADS Development Review & Collaboration`.
Repository artifacts remain authoritative across chats and models.

---

# Current active boundary

Primary route:

```text
docs/checkpoints/219_work_unit_grammar_preliminary_review_claude_ideation_requested.md
docs/model_collaboration/threads/MC-0004/messages/003_chatgpt_work_unit_grammar_divergent_ideation_request.md
docs/research/046_work_unit_category_and_silhouette_visual_grammar_experiment.md
frontend/design-lab/work-unit-grammar.html
frontend/design-lab/work-unit-grammar.css
frontend/design-lab/work-unit-grammar.js
```

Expected local URL:

```text
http://localhost:5173/design-lab/work-unit-grammar.html
```

Corrected exact browser-experiment target for Claude:

```text
88a507d42744917be1e84b29177dd0465f24cd82
```

## Provisionally settled grid/world direction

```text
G4 Adaptive Hybrid                  SELECTED
Dark mode                           CURRENT design baseline
Light mode                          DEFERRED
Travelling grid currents            KEEP
Current distribution                RANDOMIZED across visible 20 px grid lines
Current cadence                     LIVELY preferred
Intersection glints                 KEEP
Glint location                      100 px MAJOR-GRID INTERSECTIONS ONLY
Glint cadence                       APPROXIMATELY QUIET / INDEPENDENT
Slow ambient light drift            KEEP
Localized semantic activity         KEEP
Fixed authored ambient coordinates  REJECTED
```

This layer is provisionally settled, not permanently frozen. Later integrated evidence may still justify adjustment.

Decorative/ambient visual behavior remains explicitly legitimate when it improves polish, atmosphere and product character while staying visually subordinate enough that it cannot be mistaken for semantic project/runtime state.

## Work-unit interaction lighting: sufficiently settled

Human review selected:

```text
H4 Integrated Response  SELECTED
```

Current retained treatment:

```text
REST
    accepted clean localized/asymmetric in-box illumination
    accepted narrow asymmetric outward world spill through the accent/left side
    no broad circular halo

HOVER
    full node-colored halo
    pointer-following hotspot
    local grid/world illumination
    immediate connector emphasis
    one restrained perimeter sweep on hover entry
    small depth lift
    fast entry + smoother slower release
```

Final human disposition:

```text
resting in-box illumination        ACCEPTED
outward left-side resting spill   ACCEPTED
broad circular resting halo       REJECTED
hover-entry timing                ACCEPTED
hover-release timing              ACCEPTED
```

No further generic lighting-only variant is currently justified.

Later selected/focused, running/waiting, blocked/approval and other semantic states may reuse or modify lighting, but those belong to their own integrated design slices.

---

# Active slice: work-unit category / silhouette visual grammar

Research 037 and Research 038 identified a shared current weakness: most meaningful work units still collapse into one generic rounded-card grammar, with category identity carried too heavily by text, icon and color.

Research 046 isolates:

```text
WHAT IS THIS?
    category / work-unit kind
```

from:

```text
project disposition
runtime state
importance / methodological priority
```

The first browser comparison contains:

```text
W1  Unified Precision Frame
W2  Edge-Signature Grammar
W3  Structural Silhouette Family
W4  Hybrid Semantic Instrument
```

Two comparison modes are available:

```text
Category strip
    isolates category recognition in a neutral comparison context

Project scene
    tests the same grammar inside realistic G4/H4 composition with connectors
```

Representative design-fixture categories:

```text
Question / Blocker
Investigation
Validation / Analysis
Model Work
Evaluation
```

These are not a frozen production taxonomy.

## Preliminary human review

The project owner judged the first implementation positively but did not select W1-W4.

The important new product judgment is:

```text
the current four candidates likely cover too little of the plausible work-unit grammar design space
```

The project owner therefore requested Claude ideas and inspiration before convergence.

This is not a request for Claude to merely rank W1-W4. The desired value is divergent design-space expansion and identification of additional mechanisms or combinations worth browser testing.

## Project Scene defect correction

Human review exposed that switching to `Project scene` left the Category strip visible, causing overlapping duplicate work units.

The design-lab view controller was corrected so inactive panels are explicitly suppressed as well as marked hidden. The exact corrected experiment target is the SHA above.

No production file changed.

---

# Current MC-0004 collaboration gate

```text
Phase A  Claude independent proposal  cd2e12f2c79ee3b2f205457c5940eb2022b4631a  BLIND_TO_CANDIDATE
Phase B  Claude comparative review    d94d696214a41d2a3904aa9ce2a42bdab5f2f3ce  COMPARATIVE_ONLY
Phase C  browser-rendered design evaluation
Current  Claude divergent work-unit grammar ideation requested
```

Pending Claude request:

```text
docs/model_collaboration/threads/MC-0004/messages/003_chatgpt_work_unit_grammar_divergent_ideation_request.md
```

Classification:

```text
COMPARATIVE_ONLY / DIVERGENT_IDEATION
```

Expected Claude response:

```text
docs/model_collaboration/threads/MC-0004/messages/004_claude_work_unit_grammar_divergent_ideation.md
```

Claude may inspect all current candidate material. This is intentionally not a new blind-independent phase.

Claude's write scope remains only:

```text
docs/model_collaboration/threads/MC-0004/messages/**
```

ChatGPT retains target-state write ownership.

Generated-image UI concepts are not part of the preferred Cockpit evaluation workflow. Real browser-rendered experiments and real external references are preferred.

---

# Important non-decisions

Still unresolved:

```text
final work-unit taxonomy
final work-unit silhouette/category grammar
final semantic colors and status palette
multi-axis project-disposition treatment
selected/focused persistent treatment
runtime / waiting / blocked / approval treatment
final node dimensions and typography
final semantic connector vocabulary
semantic zoom
2.5D focus/depth system
production motion implementation/library
Conversation Workspace composition
large-project layout/grouping/command architecture
final design system
```

Only isolated `frontend/design-lab/**` artifacts are authorized for the current experiment. The production `/cockpit` remains the control baseline.

---

# Source Universe deployment

```text
source-vault bootstrap
    PAUSED
    not cancelled
    not rejected
    not superseded
    accepted architecture/runbook unchanged
```

Course 2 remains blocked until the permanent recovery-integrity gate succeeds.

---

## Exact continuation

```text
1. use Checkpoint 219 and v1-cockpit-design-exploration
2. pull the latest branch locally when reviewing the Project Scene defect correction
3. Claude reads Message 003 and exact target 88a507d42744917be1e84b29177dd0465f24cd82
4. Claude writes only Message 004 with divergent work-unit grammar ideas
5. ChatGPT reconstructs Claude's response from the repository
6. synthesize the strongest additional/combined candidates against Research 046 and current browser evidence
7. build a bounded second work-unit grammar browser round
8. return to human comparison before selecting the category grammar
9. keep production Cockpit untouched
10. keep source-vault deployment paused until explicitly resumed
```
