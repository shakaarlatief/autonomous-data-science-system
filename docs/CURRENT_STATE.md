# Current State

**Checkpoint:** 232  
**Date:** 2026-08-27  
**Active development branch:** `v1-cockpit-design-exploration`  
**Active PR:** none  
**Exploration branch base:** `v1-frontend-spike` at Checkpoint 205 head `2480109fadeee1e480ef03b82e335aacdf9adf91`  
**Promoted V1 integration branch:** `v1-frontend-spike` at feature-promotion head `ed5b60bdc882bed0799ce55228ce8187f9c55aa1`  
**Development stage:** MC-0004 Phase C browser-rendered Project Cockpit design evaluation. Relation-class Hue + Tag is sufficiently settled. Mixed-category review showed that persistent disposition color competes with category identity, so the current project-disposition convergence candidate is P7 Neutral Tag + Tone with disposition color revealed only on hover.  
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

Repository artifacts remain authoritative across chats and models.

---

# Current active boundary

Primary route:

```text
docs/checkpoints/232_disposition_neutral_tag_tone_refinement_review_opened.md
docs/research/061_project_disposition_neutral_tag_tone_convergence_refinement.md
docs/research/060_disposition_hybrid_refinement_and_mixed_category_practical_comparison.md
frontend/design-lab/work-unit-disposition-grammar.html
frontend/design-lab/work-unit-disposition-grammar.css
frontend/design-lab/work-unit-disposition-grammar.js
```

Current local URL:

```text
http://localhost:5173/design-lab/work-unit-disposition-grammar.html
```

Exact current browser implementation target:

```text
fac1db37af4225927d6c799e37418a3ad9c42c13
```

---

# Held Cockpit controls

```text
G4 Adaptive Hybrid                  SELECTED / provisionally settled
Dark mode                           CURRENT design baseline
H4 generic hover/world response     SELECTED / sufficiently settled
Reduced in-box resting light        SELECTED preferred working baseline
```

Current work-unit category marker mapping:

```text
Question / Blocker        circle
Investigation             square
Validation / Analysis     triangle
Model Work                diamond
Evaluation                plus
```

Foundation 023 preserves the boundary:

```text
ADS owns semantic meaning
+
user controls approved non-semantic work-unit appearance dimensions
```

Current proven appearance dimensions:

```text
Box shape       Normal / Subtle shapes
Micro design    None / Micro material / Micro light
```

---

# Connector and relation results

Foundation 024 preserves one connector terminal treatment at a time, with hover/focus as an orthogonal reveal or emphasis mechanism.

Current connector treatments:

```text
Clean
Micro dots
Frame sockets
Direction arrows
```

Accepted direction grammar:

```text
D0  Undirected      no arrow
D1  Forward         arrow at B
D2  Reverse         same arrow at A
D3  Bidirectional   same arrow at both endpoints
```

Accepted directionality implementation:

```text
07d573b6569b9f09a3b7e00936f3eadecee721b3
```

Relation-class visual carrier:

```text
E5  Hue + Tag
    SELECTED / sufficiently settled for current Phase C
```

Latest accepted relation-class implementation:

```text
497e81f06ba1f9901511449237d1bb9f96b2d108
```

Stroke rhythm from the relation-class experiment remains preserved for a different future line-level semantic dimension. No semantic meaning is assigned to it yet.

---

# Active Slice 02F: project disposition

Semantic separation remains binding:

```text
WHAT IS THIS?
    category / work-unit kind

WHAT IS ITS PROJECT DISPOSITION?
    current slice

WHAT IS HAPPENING NOW?
    runtime state, held out

HOW IMPORTANT IS IT NOW?
    priority / relevance, held out
```

Representative disposition fixtures remain provisional:

```text
S0  Active / Current
S1  Recommended / Next
S2  Deferred
S3  Completed
S4  Blocked
S5  Future / Not yet active
```

Earlier browser families remain inspectable as evidence:

```text
P0  Neutral Control
P1  Disposition Hue
P2  Explicit Tag
P3  Tonal Hierarchy
P4  State Rhythm
P5  Hue + Tag
P6  Hue + Colored Tag + Tone
```

Human review of the mixed-category P6/P7 scenes found both persistent-color treatments somewhat confusing. The convergence candidate is therefore now:

```text
P7  Neutral Tag + Tone

REST
    category color remains the dominant persistent color
    disposition tag remains neutral
    Completed / Deferred / Future retain selective tonal recession
    no disposition-colored outer perimeter
    no state rhythm

HOVER
    disposition tag border/text reveal the state-specific hue
    H4 node hover remains otherwise unchanged
```

The page now opens directly in P7.

P4 rhythm and the previous colored P6/P7 variants remain preserved in browser controls / repository history rather than being silently discarded.

## Practical mixed-category verification

The practical scene still contains Question, Investigation, Validation, Model and Evaluation work units across Blocked, Active, Recommended, Completed, Deferred and Future fixtures.

The right P7 scene now tests whether keeping the resting tag neutral materially reduces category/disposition color competition while still providing explicit text and tonal hierarchy. Hovering a P7 node reveals the state hue only in the tag.

Current human gate:

```text
verify P7 resting tag is neutral
verify hover reveals the correct state hue
verify category identity remains visually dominant at rest
verify tonal recession does not imply low importance / disabled state
verify mixed-category scene is materially less confusing
-> if accepted, treat project-disposition visual carrier as sufficiently converged for current Phase C
```

---

# MC-0004 collaboration state

```text
Phase A  Claude independent proposal  cd2e12f2c79ee3b2f205457c5940eb2022b4631a  BLIND_TO_CANDIDATE
Phase B  Claude comparative review    d94d696214a41d2a3904aa9ce2a42bdab5f2f3ce  COMPARATIVE_ONLY
Phase C  browser-rendered design evaluation
Latest Claude contribution            faf18ed9932d60a24dd80589b0ec0ba71c5940fd
Current                               P7 Neutral Tag + Tone human verification
```

There is no pending Claude obligation.

C5 Internal Layout Grammar remains deferred to semantic zoom / information-density work.

---

# Important non-decisions

Still unresolved:

```text
final project-disposition ontology
runtime / queued / waiting / failed / waiting-for-human visual grammar
importance / priority / relevance visual grammar
final semantic relation taxonomy
production relation colors / labels
semantic zoom behavior for relation tags
large-project label-density management
semantic assignment of connector stroke rhythm
runtime-flow connector behavior
selected/focused persistent treatment
production appearance persistence
final work-unit taxonomy
final node dimensions and typography
semantic zoom
C5 Internal Layout Grammar
2.5D focus/depth system
Conversation Workspace composition
large-project layout/grouping/command architecture
final production design system
```

Only isolated `frontend/design-lab/**` artifacts are authorized for the current experiment. Production `/cockpit` remains the control baseline.

---

# Source Universe deployment

```text
source-vault bootstrap
    PAUSED
    not cancelled
    not rejected
    not superseded
```

Course 2 remains blocked until the permanent recovery-integrity gate succeeds.

---

## Exact continuation

```text
1. use Checkpoint 232 and v1-cockpit-design-exploration
2. pull the latest branch locally
3. open http://localhost:5173/design-lab/work-unit-disposition-grammar.html
4. verify P7 opens by default
5. verify P7 tags are neutral at rest
6. hover P7 nodes and verify tag state hue appears only on hover
7. inspect mixed-category P7 scene for reduced semantic/color confusion
8. judge tonal recession separately from importance
9. if accepted, close disposition carrier for current Phase C and move to the next bounded Cockpit question
10. keep production Cockpit untouched
```
