# Current State

**Checkpoint:** 220  
**Date:** 2026-08-26  
**Active development branch:** `v1-cockpit-design-exploration`  
**Active PR:** none  
**Exploration branch base:** `v1-frontend-spike` at Checkpoint 205 head `2480109fadeee1e480ef03b82e335aacdf9adf91`  
**Promoted V1 integration branch:** `v1-frontend-spike` at feature-promotion head `ed5b60bdc882bed0799ce55228ce8187f9c55aa1`  
**Development stage:** MC-0004 Phase C browser-rendered Project Cockpit design evaluation. G4 is provisionally settled. H4 generic rest/hover interaction lighting is sufficiently settled. The W1-W4 work-unit category/silhouette experiment remains open. Human review corrected Project Scene switching, accidental H4 in-box-light suppression, fixed-left lighting despite moved signature bars, and then centered edge lighting despite partial top/bottom signatures being left-biased. The browser exposes an explicit H4-baseline versus Reduced in-box-light comparison. Human verification of this corrected target precedes Claude divergent ideation. The permanent source-vault bootstrap remains deliberately paused.  
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
docs/checkpoints/220_work_unit_grammar_h4_control_corrected_claude_ideation_ready.md
docs/research/047_work_unit_grammar_h4_control_correction_and_inbox_light_comparison.md
docs/research/046_work_unit_category_and_silhouette_visual_grammar_experiment.md
docs/model_collaboration/threads/MC-0004/messages/003_chatgpt_work_unit_grammar_divergent_ideation_request.md
frontend/design-lab/work-unit-grammar.html
frontend/design-lab/work-unit-grammar.css
frontend/design-lab/work-unit-grammar-lighting-controls.css
frontend/design-lab/work-unit-grammar.js
```

Expected local URL:

```text
http://localhost:5173/design-lab/work-unit-grammar.html
```

Corrected exact browser-experiment target for Claude after human verification:

```text
304db34d6482320b317db97277148bc129d07372
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

Current retained generic treatment:

```text
REST
    accepted clean localized/asymmetric in-box illumination
    accepted narrow asymmetric outward world spill through the accent side
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

Final prior human disposition:

```text
resting in-box illumination        ACCEPTED
outward resting spill              ACCEPTED
broad circular resting halo        REJECTED
hover-entry timing                 ACCEPTED
hover-release timing               ACCEPTED
```

No further generic hover/outward-spill tuning is currently justified.

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

Two comparison modes remain:

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

## Preliminary human review and defect corrections

The project owner judged the first implementation positively but did not select W1-W4.

The project owner also judged the current four candidates likely to cover too little of the plausible work-unit grammar design space and requested broader Claude ideas before convergence.

Before Claude should inspect the design, human browser review exposed four control/implementation defects or refinements:

```text
1. Project Scene could remain overlaid with Category strip
2. accepted H4 in-box resting light was accidentally much weaker in the grammar DOM
3. resting light/spill remained left-biased even when category signature bars moved to top/bottom/right
4. after side-awareness was added, partial top/bottom signatures still produced edge-centered light instead of light aligned to the actual bar position
```

All four are now corrected in the design lab.

### Cause of the in-box-light drift

The grammar experiment introduced a separate `.node-surface` above the copied H4 rest-light layer. That visually suppressed most of the color previously visible inside the work unit.

Therefore the previous implementation had preserved nominal CSS values but not the accepted rendered H4 control.

Research 047 records the correction.

## Explicit in-box-light comparison

The accidentally quieter appearance is now preserved intentionally rather than silently discarded.

The browser control exposes:

```text
In-box light
    H4 baseline   DEFAULT
        restored accepted in-box resting illumination

    Reduced
        intentional near-dark / low-colour in-box alternative
```

This changes **in-box resting-light intensity only**.

It does not intentionally change:

```text
outward resting spill
hover halo
pointer hotspot
hover world light
connector hover emphasis
perimeter sweep
hover timing
```

No H4-baseline-versus-Reduced preference exists yet.

## Signature-edge-and-position-aware resting light

The project owner established the rule:

```text
if the visible category signature/accent moves,
signature-anchored resting light follows both:
    the edge
    and the position along that edge
```

Current edge mapping:

```text
W1
    all categories left

W2 / W4
    Question        left
    Investigation   left
    Validation      top
    Model           bottom
    Evaluation      right

W3
    no explicit signature bar
    retain accepted left-biased H4 baseline
```

For W2/W4 Validation and Model, the signature bars occupy the left part of the top/bottom edge. The resting light is therefore left-biased on that horizontal edge rather than centered.

Current authored anchor expressions mirror the frame-signature geometry:

```text
W2 Validation   top     calc(14px + 23%)
W2 Model        bottom  calc(14px + 25%)
W4 Validation   top     calc(12px + 21%)
W4 Model        bottom  calc(12px + 23%)
```

The in-box surface light, near-node rest light and outward spill move together.

---

# Current MC-0004 collaboration gate

```text
Phase A  Claude independent proposal  cd2e12f2c79ee3b2f205457c5940eb2022b4631a  BLIND_TO_CANDIDATE
Phase B  Claude comparative review    d94d696214a41d2a3904aa9ce2a42bdab5f2f3ce  COMPARATIVE_ONLY
Phase C  browser-rendered design evaluation
Current  human verification of corrected grammar target, then Claude divergent ideation
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

The Claude request explicitly preserves:

```text
no artificial candidate-count cap
all genuinely distinct worthwhile candidates may be tested
batching is allowed for clarity but does not imply rejection
H4 baseline vs Reduced is a secondary explicit comparison
signature-anchored lighting follows edge + along-edge position
```

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
H4 baseline vs Reduced in-box resting-light preference
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
1. use Checkpoint 220 and v1-cockpit-design-exploration
2. pull the latest branch locally
3. refresh http://localhost:5173/design-lab/work-unit-grammar.html
4. verify Project Scene still switches cleanly
5. compare H4 baseline vs Reduced in-box resting light
6. inspect W2/W4 Validation and Model especially
7. verify their top/bottom resting light is biased toward the actual left-biased signature bar rather than centered on the edge
8. verify left/right signature treatments and accepted H4 hover still behave correctly
9. if correct, trigger Claude using docs/model_collaboration/REVIEW_INBOX.md
10. Claude reviews exact target 304db34d6482320b317db97277148bc129d07372 and writes only Message 004
11. ChatGPT synthesizes all genuinely worthwhile additional/combined candidates and builds as many browser variants as evidence justifies
12. keep production Cockpit untouched
13. keep source-vault deployment paused until explicitly resumed
```
