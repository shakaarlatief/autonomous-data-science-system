# Autonomous Data Science System

## Overview

This repository is the persistent development home of the Autonomous Data Science System (ADS).

ADS is being developed as a rigorous, adaptive, semi-autonomous environment for data-science projects in which a strong LLM is one flexible reasoning component inside a wider system that owns project memory, methodological navigation, provenance, execution coordination, deterministic guarantees where justified, and a professional human interaction surface.

The working purpose is:

> **Create the best defensible data-science process for the particular project, where what "best" means depends on the project's goals, constraints, required outputs, risk, and desired human involvement, while maintaining non-negotiable methodological integrity.**

Explicit machinery must earn its complexity empirically.

---

## Current development stage

Prototype V0 is complete. Bounded V1 is constructing the methodological knowledge universe and the professional substrate needed to use it safely.

Current route:

```text
checkpoint            234
active branch         v1-cockpit-design-exploration
active PR             none
exploration base      2480109fadeee1e480ef03b82e335aacdf9adf91
promoted V1 head      ed5b60bdc882bed0799ce55228ce8187f9c55aa1
latest specification  Specification 024
Cockpit baseline      Specification 008
current boundary      user-curated current-process focus-set human review
source-vault          PAUSED, preserved, Course 2 gate unchanged
```

Specification 022 remains `INCOMPLETE / EXECUTION INTEGRITY FAILED`; no scientific `GENERIC` / `ADS_HORIZON` / `ORACLE_HORIZON` comparison may be inferred from that run.

---

## Current Cockpit design direction

Held controls:

```text
G4 Adaptive Hybrid world                          SELECTED / provisionally settled
H4 generic hover/outward-world response          SELECTED / sufficiently settled
Reduced in-box resting light                      SELECTED preferred working baseline
```

Current scientific category-marker grammar:

```text
Question / Blocker        circle
Investigation             square
Validation / Analysis     triangle
Model Work                diamond
Evaluation                plus
```

Foundation 023 preserves user-configurable non-semantic work-unit appearance while ADS owns semantic meaning. Foundation 024 preserves configurable connector treatment, orthogonal hover/focus behavior and system-owned relation directionality.

Relation-class visual grammar remains sufficiently settled:

```text
E5  Hue + Tag
```

Project-disposition visual direction is accepted for the current Phase-C round:

```text
P7  Neutral Tag + Tone

REST
    category color remains dominant
    disposition tag remains neutral
    Completed / Deferred / Future retain selective tonal recession

HOVER
    disposition tag reveals its state-specific hue
```

The final project-disposition ontology remains unfrozen.

---

## Active Slice 02G: current-process focus lens and editable focus set

The current focus architecture separates:

```text
work-unit existence
project disposition
current-focus membership
view emphasis
```

The browser supports:

```text
Context visible
Focus current process
Edit focus set
Reset example
```

`Focus current process` strongly suppresses work outside the current focus set while keeping it hover-recoverable. `Edit focus set` lets the user explicitly add or remove individual work units from that set with `+ FOCUS` / `- FOCUS` controls. This does not delete the work unit or change its disposition.

Connector suppression updates with focus membership: if either endpoint lies outside the current focus, the connector is treated as contextual for the focus lens.

The design-lab browser preserves the edited focus set in browser `localStorage` only as prototype convenience. Production ownership and persistence semantics remain open.

Browser:

```text
http://localhost:5173/design-lab/work-unit-process-focus.html
```

Exact implementation target:

```text
da115b74de526fca05ed6f468bef39bdb801355c
```

Research and checkpoint:

```text
docs/research/063_user_curated_current_process_focus_membership.md
docs/research/062_current_process_focus_lens_and_context_suppression_experiment.md
docs/checkpoints/234_user_curated_current_process_focus_set_review_opened.md
```

---

## Collaboration state

Claude's latest Phase-C contribution remains:

```text
faf18ed9932d60a24dd80589b0ec0ba71c5940fd
```

No model-collaboration obligation is pending.

C5 Internal Layout Grammar remains deferred to semantic zoom / information-density work.

---

## Production boundary

Current design work remains isolated under `frontend/design-lab/**`.

Production `/cockpit` remains the control baseline.

Not yet authorized:

```text
production Cockpit replacement
final current-focus membership semantics
automatic focus-selection logic
production focus-set ownership / persistence
multiple named focus lenses
final project-disposition ontology
runtime-state / priority visual grammar
final semantic relation taxonomy
production relation colors / codes
semantic assignment of connector stroke rhythm
new graph/canvas dependency
new motion-library adoption
final visual-system freeze
```

Specification 008 remains the promoted interaction architecture.

---

## Source Universe substrate

Specification 023 remains `SOURCE_SUBSTRATE_ACCEPTED`.

Permanent deployment remains preserved but paused. Course 2 remains blocked until the permanent recovery-integrity gate succeeds.

---

## Repository role

This repository is the durable development source of truth.

> **The chat is where we think. The repository is where the system remembers.**

---

## Start here

```text
docs/CURRENT_STATE.md
docs/KNOWLEDGE_MAP.md
docs/current_routing.json

docs/checkpoints/234_user_curated_current_process_focus_set_review_opened.md
docs/research/063_user_curated_current_process_focus_membership.md
docs/research/062_current_process_focus_lens_and_context_suppression_experiment.md
frontend/design-lab/work-unit-process-focus.html

docs/research/061_project_disposition_neutral_tag_tone_convergence_refinement.md
frontend/design-lab/work-unit-disposition-grammar.html

docs/foundations/024_composable_connector_presentation_and_semantic_directionality.md
docs/foundations/023_user_configurable_cockpit_appearance_and_semantic_invariants.md

docs/model_collaboration/threads/MC-0004/THREAD.md
docs/model_collaboration/threads/MC-0004/STATE.json
docs/model_collaboration/REVIEW_INBOX.md
```

## Exact next step

```text
1. pull v1-cockpit-design-exploration
2. open http://localhost:5173/design-lab/work-unit-process-focus.html
3. turn Edit focus set on
4. add and remove several work units with + FOCUS / - FOCUS
5. switch between Context visible and Focus current process
6. inspect node and connector suppression after each membership change
7. verify editing outside-focus nodes remains comfortable
8. verify browser refresh preserves the prototype set and Reset example restores the fixture
9. refine / accept / reject the editable focus-set interaction
10. keep production Cockpit untouched
```
