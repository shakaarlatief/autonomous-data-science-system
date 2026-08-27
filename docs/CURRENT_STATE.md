# Current State

**Checkpoint:** 227  
**Date:** 2026-08-27  
**Active development branch:** `v1-cockpit-design-exploration`  
**Active PR:** none  
**Exploration branch base:** `v1-frontend-spike` at Checkpoint 205 head `2480109fadeee1e480ef03b82e335aacdf9adf91`  
**Promoted V1 integration branch:** `v1-frontend-spike` at feature-promotion head `ed5b60bdc882bed0799ce55228ce8187f9c55aa1`  
**Development stage:** MC-0004 Phase C browser-rendered Project Cockpit design evaluation. Work-unit appearance configurability is promoted in Foundation 023. Connector treatment / hover separation and semantic directionality are promoted in refined Foundation 024. The active gate is human verification of the simplified edge-connected arrow directionality grammar. The permanent source-vault bootstrap remains deliberately paused.  
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
docs/checkpoints/227_directionality_arrow_grammar_simplified_human_review_opened.md
docs/research/056_directionality_arrow_grammar_and_hover_separation_refinement.md
docs/foundations/024_composable_connector_presentation_and_semantic_directionality.md
frontend/design-lab/connector-directionality.html
frontend/design-lab/connector-directionality.css
frontend/design-lab/connector-directionality.js
```

Current local URL:

```text
http://localhost:5173/design-lab/connector-directionality.html
```

Exact current browser implementation target:

```text
07d573b6569b9f09a3b7e00936f3eadecee721b3
```

---

# Provisionally settled world / interaction controls

```text
G4 Adaptive Hybrid                  SELECTED / provisionally settled
Dark mode                           CURRENT design baseline
Travelling grid currents            KEEP
Randomized visible-grid currents    KEEP
100 px major-grid glints            KEEP
Slow ambient light drift            KEEP
Localized semantic activity         KEEP
```

Generic H4 hover/world behavior remains sufficiently settled.

Current work-unit rest/hover baseline:

```text
REST
    Reduced in-box resting light
    narrow asymmetric outward world spill
    no broad circular resting halo

HOVER
    full node-colored halo
    pointer-following hotspot
    local grid/world illumination
    immediate connector emphasis
    one restrained perimeter sweep
    2 px depth lift
    fast entry + smoother slower release
```

---

# Work-unit semantic grammar

Current semantic category-marker mapping:

```text
Question / Blocker        circle
Investigation             square
Validation / Analysis     triangle
Model Work                diamond
Evaluation                plus
```

Foundation 023 preserves:

```text
ADS owns semantic meaning
+
user controls approved non-semantic work-unit appearance dimensions
```

Current proven work-unit appearance dimensions:

```text
Box shape       Normal / Subtle shapes
Micro design    None / Micro material / Micro light
```

---

# Connector presentation result

The useful connector mechanisms remain available, but human review clarified that they should not be unnecessarily stacked.

Current connector-treatment vocabulary:

```text
Clean
Micro dots
Frame sockets
Direction arrows
```

Current interaction model:

```text
connector treatment
    one active terminal treatment at a time

hover / focus
    separate mechanism
    may reveal or intensify whichever treatment is active
```

Rejected as a default presentation pattern:

```text
arrow + dot
arrow + socket
socket + dot
other unnecessary terminal stacks
```

Latest retained refinements:

```text
42ec63d17095753dc4ab97628cd859473cbdf5e8
    Micro-dot / hover-port circles moved mostly outside the work-unit perimeter

183264bdd07783eaa2354894592f2cf4a076b6ec
    Frame sockets keep dark interiors and adopt active relation color / restrained glow when highlighted
```

Held geometry/interaction invariants:

```text
curve remains below work-unit bodies
rendered-edge geometry is authoritative
connector follows H4 hover lift / release
Micro dots sit mostly outside the card
Frame sockets remain frame-integrated
```

---

# Foundation 024: connector treatment, hover behavior and semantic directionality

Refined durable principle:

```text
semantic relation model
    system-owned

connector treatment
    configurable within approved bounds
    normally one active terminal treatment at a time

hover behavior
    orthogonal interaction mechanism
```

Direction remains semantic:

```text
undirected
A -> B
A <- B
A <-> B
```

If direction arrows are used, endpoint placement follows semantic direction exactly:

```text
undirected       no arrow
A -> B           arrow at B
A <- B           arrow at A
A <-> B          arrows at both ends
```

---

# Active Slice 02D: simplified arrow directionality

Human review of the first directionality page concluded that dots, sockets and arrows did not need to be shown together merely to test direction.

The refined browser therefore isolates the already-liked K3-style arrow:

```text
D0  Undirected      A - B
    no arrow

D1  Forward         A -> B
    arrow tip docked directly to B

D2  Reverse         A <- B
    exact same arrow tip docked directly to A

D3  Bidirectional   A <-> B
    same arrow at both endpoints
```

The arrow tip is placed on the exact rendered work-unit perimeter, with the arrow arms outside the card. The relation curve uses the same rendered-edge geometry and remains synchronized through H4 hover lift / release.

Current human verification questions:

```text
Does D1 look like the earlier preferred arrow treatment?
Does D2 look like the exact mirrored mechanism?
Does D3 read cleanly as bidirectional rather than duplicated noise?
Does D0 remain clearly undirected?
```

If accepted, directionality is sufficiently converged to proceed to semantic relation classes.

---

# MC-0004 collaboration state

```text
Phase A  Claude independent proposal  cd2e12f2c79ee3b2f205457c5940eb2022b4631a  BLIND_TO_CANDIDATE
Phase B  Claude comparative review    d94d696214a41d2a3904aa9ce2a42bdab5f2f3ce  COMPARATIVE_ONLY
Phase C  browser-rendered design evaluation
Latest Claude contribution            faf18ed9932d60a24dd80589b0ec0ba71c5940fd
Current                               simplified arrow directionality human review
```

There is no pending Claude obligation.

C4 Port Grammar has matured into connector-treatment and directionality architecture.

C5 Internal Layout Grammar remains deferred to semantic zoom / information-density work.

---

# Important non-decisions

Still unresolved:

```text
final semantic relation taxonomy
chronology / causality / dependency / evidence / lineage connector semantics
relation colors / dashed-solid semantics
runtime-flow connector behavior
production connector preference persistence
selected/focused persistent treatment
runtime / waiting / blocked / approval treatment
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
1. use Checkpoint 227 and v1-cockpit-design-exploration
2. pull the latest branch locally
3. open http://localhost:5173/design-lab/connector-directionality.html
4. verify D0-D3 use only the simple edge-connected arrow grammar
5. verify forward, reverse and bidirectional arrows touch the correct work-unit edge
6. verify no dots / sockets are mixed into arrow directionality
7. if accepted, preserve directionality as sufficiently settled
8. open semantic relation-class exploration next
9. keep production Cockpit untouched
10. keep source-vault deployment paused until explicitly resumed
```
