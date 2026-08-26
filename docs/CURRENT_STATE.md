# Current State

**Checkpoint:** 225  
**Date:** 2026-08-26  
**Active development branch:** `v1-cockpit-design-exploration`  
**Active PR:** none  
**Exploration branch base:** `v1-frontend-spike` at Checkpoint 205 head `2480109fadeee1e480ef03b82e335aacdf9adf91`  
**Promoted V1 integration branch:** `v1-frontend-spike` at feature-promotion head `ed5b60bdc882bed0799ce55228ce8187f9c55aa1`  
**Development stage:** MC-0004 Phase C browser-rendered Project Cockpit design evaluation. The configurable work-unit appearance principle is now promoted in Foundation 023 after positive human browser review. The remaining customizable-preview connector attachment defect has been fixed. The active design slice is now generic connector and port visual grammar. The permanent source-vault bootstrap remains deliberately paused.  
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
docs/checkpoints/225_configurable_appearance_promoted_connector_grammar_review_opened.md
docs/research/053_connector_and_port_visual_grammar_experiment.md
docs/research/052_configurable_cockpit_review_connector_geometry_fix_and_foundation_promotion.md
docs/foundations/023_user_configurable_cockpit_appearance_and_semantic_invariants.md
frontend/design-lab/connector-grammar.html
frontend/design-lab/connector-grammar.css
frontend/design-lab/connector-grammar.js
```

Current local URL:

```text
http://localhost:5173/design-lab/connector-grammar.html
```

Exact connector browser implementation target before documentation/routing commits:

```text
e3394447eeae721eab9bd66d347d0d327dbe0485
```

---

# Provisionally settled grid/world direction

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

Decorative ambient behavior remains legitimate only when it stays subordinate and cannot be mistaken for semantic project/runtime state.

---

# Work-unit interaction and semantic grammar

Generic H4 hover/outward-world behavior remains sufficiently settled.

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
    one restrained perimeter sweep on hover entry
    small depth lift
    fast entry + smoother slower release
```

Current semantic category marker mapping:

```text
Question / Blocker        circle
Investigation             square
Validation / Analysis     triangle
Model Work                diamond
Evaluation                plus
```

---

# Foundation 023: configurable appearance

Human review of the configurator was strongly positive. The product direction is now promoted:

```text
ADS owns semantic meaning
+
user controls approved non-semantic appearance dimensions
```

Promoted artifact:

```text
docs/foundations/023_user_configurable_cockpit_appearance_and_semantic_invariants.md
```

Current proven configurable dimensions:

```text
Box shape
    Normal
    Subtle shapes

Micro design
    None
    Micro material
    Micro light
```

Appearance choices must not redefine category, disposition, runtime, importance, evidence, provenance, or methodological meaning.

Plausible future preference hierarchy:

```text
user appearance profile
    global personal default

project appearance override
    optional project-specific choice

semantic project state
    independent from both
```

Production settings persistence and collaboration behavior remain open.

---

# Customizable-preview connector defect: fixed

Human review found one small defect: project-scene lines did not correctly attach to rendered work-unit boxes.

Root cause:

```text
static authored SVG coordinates
instead of rendered node geometry
```

The preview now derives connector endpoints from `.node-surface` bounding boxes and recalculates after initial render, view changes, shape changes, and browser/scene geometry changes.

The Investigation right-edge notch receives a silhouette-aware inset anchor under Subtle shapes.

Exact defect-fix commit:

```text
c1f996f6500672641de8e00780d5a4949c5dcb28
```

Configurator route remains:

```text
http://localhost:5173/design-lab/work-unit-grammar-customizable.html
```

---

# Active Slice 02C: connector and port visual grammar

The next bounded design question is:

> How should generic project relationships visually meet work units and remain legible without turning the Cockpit into graph noise?

This is the dependency-aligned point at which Claude concept C4 Port Grammar becomes active.

Held controls:

```text
G4 world
scientific category markers
Reduced in-box light
accepted H4 hover/world response
Subtle shapes
Micro material
same churn-project fixture
same four generic relationships
```

Current candidates:

```text
K0  Clean Curve
    direct edge-to-edge line, no ports

K1  Micro Dots
    small source and target endpoint dots

K2  Frame Sockets
    small square structural sockets

K3  Target Cue
    restrained target-side directional chevron

K4  Hover Ports
    clean rest state, endpoint dots revealed on related-node hover
```

All candidates use dynamic rendered-edge connector geometry rather than fixed path coordinates.

Human browser review is the active gate.

---

# MC-0004 collaboration state

```text
Phase A  Claude independent proposal  cd2e12f2c79ee3b2f205457c5940eb2022b4631a  BLIND_TO_CANDIDATE
Phase B  Claude comparative review    d94d696214a41d2a3904aa9ce2a42bdab5f2f3ce  COMPARATIVE_ONLY
Phase C  browser-rendered design evaluation
Latest Claude contribution            faf18ed9932d60a24dd80589b0ec0ba71c5940fd
Current                              connector / port grammar human review
```

There is no pending Claude obligation.

---

# Important non-decisions

Still unresolved:

```text
final work-unit taxonomy
final semantic connector vocabulary
relation-type colors and line semantics
dependency / evidence / lineage connector distinctions
runtime-flow connector behavior
selected/focused persistent treatment
runtime / waiting / blocked / approval treatment
final node dimensions and typography
semantic zoom
Internal Layout Grammar
2.5D focus/depth system
production motion implementation/library
Conversation Workspace composition
large-project layout/grouping/command architecture
production appearance persistence
final design system
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
    accepted architecture/runbook unchanged
```

Course 2 remains blocked until the permanent recovery-integrity gate succeeds.

---

## Exact continuation

```text
1. use Checkpoint 225 and v1-cockpit-design-exploration
2. pull the latest branch locally
3. optionally refresh work-unit-grammar-customizable.html and confirm the connector attachment fix
4. open http://localhost:5173/design-lab/connector-grammar.html
5. compare K0 through K4 on the same project scene
6. hover nodes and inspect connector emphasis / K4 hover ports
7. judge resting noise, physical attachment, direction usefulness and large-project plausibility
8. human may prefer, reject or combine connector mechanisms
9. preserve a generic connector baseline before adding semantic relation classes
10. keep production Cockpit untouched
11. keep source-vault deployment paused until explicitly resumed
```
