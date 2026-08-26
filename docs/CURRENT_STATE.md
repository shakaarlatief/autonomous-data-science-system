# Current State

**Checkpoint:** 224  
**Date:** 2026-08-26  
**Active development branch:** `v1-cockpit-design-exploration`  
**Active PR:** none  
**Exploration branch base:** `v1-frontend-spike` at Checkpoint 205 head `2480109fadeee1e480ef03b82e335aacdf9adf91`  
**Promoted V1 integration branch:** `v1-frontend-spike` at feature-promotion head `ed5b60bdc882bed0799ce55228ce8187f9c55aa1`  
**Development stage:** MC-0004 Phase C browser-rendered Project Cockpit design evaluation. Scientific category markers are selected for the current work-unit grammar direction. Reduced in-box light is the preferred working baseline. Refined M1 micro-materials and subtle true-shape boxes remain positive. The newest product decision is that compatible visual treatments should coexist as user-configurable Cockpit appearance choices rather than being forced into one universal visual winner. A live configurator is open for human browser review. The permanent source-vault bootstrap remains deliberately paused.  
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
docs/checkpoints/224_user_configurable_cockpit_visual_grammar_prototype_opened.md
docs/research/051_user_configurable_cockpit_visual_grammar_and_semantic_invariants.md
docs/research/050_scientific_marker_selection_and_micro_material_shape_refinement.md
frontend/design-lab/work-unit-grammar-customizable.html
frontend/design-lab/work-unit-grammar-customizable.css
frontend/design-lab/work-unit-grammar-customizable.js
```

Local URL:

```text
http://localhost:5173/design-lab/work-unit-grammar-customizable.html
```

Exact configurable browser implementation target before documentation/routing commits:

```text
ac16df1bbcd456b63c042c28e52516679139bf32
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

# Work-unit interaction lighting

Generic H4 hover/outward-spill behavior remains sufficiently settled.

Current preferred resting-light baseline:

```text
Reduced in-box resting light  SELECTED PREFERRED WORKING CONTROL
```

Historical H4-baseline evidence remains preserved.

Signature-coupled resting light remains governed by:

```text
signature edge
+
signature position along that edge
-> resting-light origin
```

---

# Selected work-unit category-mark direction

```text
Scientific marker family
    Question        circle
    Investigation   square
    Validation      triangle
    Model           diamond
    Evaluation      plus
```

Rejected/retired directions remain preserved historically:

```text
bare Q / I / V / M / E letters
G2 Compact Marker Rail
S3 Inner Instrument Architecture
G1 Instrument Glyph Family retired from active focused comparison
```

The scientific marker mapping is now treated as a semantic visual invariant in the configurable prototype.

---

# Positive optional visual mechanisms

## Refined M1 micro-material

```text
Question / yellow diagonal       retained
Investigation / green dots       strengthened
Validation / blue lines          strengthened
Model / red grid                 strengthened
Evaluation / luminous diagonal   retained
```

## Subtle true-shape family

```text
Question        upper-right diagonal cut
Investigation   right-edge inward notch
Validation      subtle right-side top step
Model           stepped bottom-right geometry
Evaluation      right-side beveled termination
```

The full upper-left reading entry remains protected. The earlier aggressive Validation raised-tab form is rejected.

---

# New product direction: configurable Cockpit appearance

The project owner decided that the positive visual mechanisms do not need to compete for one mandatory global style.

The new architecture distinguishes:

```text
SEMANTIC PROJECT MODEL
    category
    project disposition
    runtime state
    importance / recommendation strength
    dependencies / evidence

PRESENTATION PROFILE
    safe user-selectable appearance preferences
```

Current configurable dimensions in the browser proof:

```text
Box shape
    Normal
    Subtle shapes

Micro design
    None
    Micro material
    Micro light
```

Current convenience presets:

```text
Clean
    normal + none

Structured
    subtle shapes + none

Rich
    subtle shapes + micro material
```

These settings change presentation only. They do not change project semantics.

## Semantic invariants held beneath customization

```text
scientific category-marker mapping remains fixed
Reduced in-box light remains the preferred baseline
project category/state/runtime/importance data remain unchanged
accessibility constraints remain authoritative
appearance must not masquerade as semantic state
```

## Persistence proof

The design-lab page uses browser-local persistence:

```text
localStorage
    ads-design-lab-cockpit-appearance-v1
```

This is not a production storage decision.

A plausible later production hierarchy is:

```text
user appearance profile
    global personal default

optional project appearance override
    per-project preference

semantic project state
    independent from both
```

Production persistence, synchronization and team/shared-project behavior remain open.

---

# MC-0004 collaboration state

```text
Phase A  Claude independent proposal  cd2e12f2c79ee3b2f205457c5940eb2022b4631a  BLIND_TO_CANDIDATE
Phase B  Claude comparative review    d94d696214a41d2a3904aa9ce2a42bdab5f2f3ce  COMPARATIVE_ONLY
Phase C  browser-rendered design evaluation
Latest Claude contribution            faf18ed9932d60a24dd80589b0ec0ba71c5940fd
Current                              user-configurable appearance human review
```

No Claude action is pending.

Dependency-bound candidates remain preserved:

```text
C4 Port Grammar
    connector-semantics slice

C5 Internal Layout Grammar
    semantic zoom / information-density slice
```

---

# Promotion boundary

The user-configurable appearance principle is now preserved as an active product direction with executable evidence, but it is not yet promoted into a new foundation/specification because the configurator itself still needs human browser review.

Still unresolved:

```text
production settings storage
account synchronization
per-project override precedence
team/shared-project appearance behavior
which additional dimensions become safely configurable
whether category marker style itself should ever vary
light/dark theme relation to appearance profiles
settings import/export
final work-unit taxonomy
final semantic colors/status palette
connector vocabulary
semantic zoom
Conversation Workspace
large-project layout/grouping
final production design system
```

Production `/cockpit` remains untouched.

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
1. use Checkpoint 224 and v1-cockpit-design-exploration
2. pull the latest branch locally
3. open http://localhost:5173/design-lab/work-unit-grammar-customizable.html
4. switch Normal <-> Subtle shapes
5. switch None <-> Micro material <-> Micro light
6. try Clean / Structured / Rich presets
7. verify scientific markers and semantic meaning remain stable across appearance changes
8. verify the combinations feel coherent rather than like unrelated themes
9. verify Project scene and Category strip both remain readable
10. if human review confirms the model, run promotion audit for a durable user-configurable Cockpit appearance principle
11. only then design production persistence/settings ownership
12. keep production Cockpit untouched
13. keep source-vault deployment paused until explicitly resumed
```
