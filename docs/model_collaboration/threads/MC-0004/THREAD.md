# MC-0004: Next-Generation Project Cockpit Design Exploration

**Thread:** MC-0004  
**Status:** ACTIVE / PHASE C BROWSER DESIGN EVALUATION  
**Review mode:** `INDEPENDENT_THEN_COMPARATIVE`  
**Task owner:** ChatGPT  
**Target-state write owner:** ChatGPT  
**Claude role:** independent reviewer / counter-designer / researcher  
**Human project owner:** final arbiter of product-intent choices  
**Opened:** 2026-08-26

## Purpose

Run a broad next-generation Project Cockpit design exploration while preserving Specification 008 unless new evidence justifies revision. Phase C uses browser-rendered experiments, continuous human review, selective external references and selective cross-model contributions before production visual replacement is authorized.

## Collaboration history

```text
Phase A
    Claude independent proposal
    message 001
    commit cd2e12f2c79ee3b2f205457c5940eb2022b4631a
    BLIND_TO_CANDIDATE

Phase B
    Claude comparative review
    message 002
    commit d94d696214a41d2a3904aa9ce2a42bdab5f2f3ce
    COMPARATIVE_ONLY

Phase C divergent work-unit ideation
    ChatGPT request message 003
    Claude response message 004
    commit faf18ed9932d60a24dd80589b0ec0ba71c5940fd
    COMPARATIVE_ONLY / DIVERGENT_IDEATION
```

No Claude action is currently pending.

## Held controls

```text
G4 Adaptive Hybrid
    SELECTED / provisionally settled

H4 generic hover/outward-world response
    SELECTED / sufficiently settled

Reduced in-box resting light
    SELECTED preferred working baseline
```

Current scientific category-marker mapping:

```text
Question / Blocker        circle
Investigation             square
Validation / Analysis     triangle
Model Work                diamond
Evaluation                plus
```

Foundation 023 promotes the durable split between semantic work-unit meaning and approved user-configurable appearance.

Foundation 024 preserves connector treatment, hover/focus and semantic directionality as separate dimensions.

## Connector and relation results

Current connector treatments:

```text
Clean
Micro dots
Frame sockets
Direction arrows
```

Accepted directionality:

```text
D0  Undirected      no arrow
D1  Forward         arrow at B
D2  Reverse         same arrow at A
D3  Bidirectional   same arrow at both endpoints
```

Exact accepted directionality target:

```text
07d573b6569b9f09a3b7e00936f3eadecee721b3
```

Relation-class visual encoding remains sufficiently settled:

```text
E5  Hue + Tag
```

Latest accepted relation-class target:

```text
497e81f06ba1f9901511449237d1bb9f96b2d108
```

Stroke rhythm remains preserved for a different future line-level semantic dimension and currently has no assigned meaning.

## Project-disposition result

Research 059 through 061 explored disposition hue, tags, tone, rhythm and mixed-category interaction.

The project owner accepted:

```text
P7  Neutral Tag + Tone

REST
    category hue remains the dominant persistent color
    explicit disposition tag remains neutral
    selective tonal recession remains for Completed / Deferred / Future
    no disposition perimeter hue
    no rhythm

HOVER
    tag border/text reveal the state-specific hue
```

Latest accepted P7 implementation before the next slice:

```text
fac1db37af4225927d6c799e37418a3ad9c42c13
```

The final disposition ontology remains unfrozen.

P4 State Rhythm and the earlier colored alternatives remain preserved as experiment/history evidence.

## Current-process focus-lens result

After accepting P7, the project owner requested a stronger suppression mode for work that should remain in the Cockpit as context but is not currently part of the active process.

Research 062 separated:

```text
PROJECT DISPOSITION
    semantic state of the work unit

CURRENT-PROCESS MEMBERSHIP
    whether it belongs to the emphasized process set

VIEW EMPHASIS
    how strongly work outside that set is suppressed
```

The browser exposed:

```text
Context visible
    accepted P7 presentation remains readable

Focus current process
    current-process work remains full salience
    contextual work is strongly suppressed
    contextual connector segments recede
    contextual nodes partially recover on hover
```

The project owner reviewed this result and said:

```text
Perfect. This is exactly what I meant.
```

The focus-lens mechanism is therefore accepted in principle for the current design round, while final current-process membership semantics remain open.

## New human requirement: user-curated focus membership

The project owner immediately added that the focus mode should be flexible:

```text
user can add work units to the current focus
user can remove work units from the current focus
```

This is interpreted as editing a focus set, not deleting work units or rewriting disposition.

Binding separation is now:

```text
WORK-UNIT EXISTENCE
    whether the work unit exists in the project

PROJECT DISPOSITION
    where the work unit stands in the project

CURRENT-FOCUS MEMBERSHIP
    whether the work unit belongs to the emphasized process set

VIEW EMPHASIS
    how strongly outside-focus work is suppressed
```

## Active Slice 02G refinement: editable focus set

Research:

```text
docs/research/063_user_curated_current_process_focus_membership.md
```

Checkpoint:

```text
docs/checkpoints/234_user_curated_current_process_focus_set_review_opened.md
```

Browser route:

```text
frontend/design-lab/work-unit-process-focus.html
frontend/design-lab/work-unit-process-focus.css
frontend/design-lab/work-unit-process-focus.js
```

Local URL:

```text
http://localhost:5173/design-lab/work-unit-process-focus.html
```

Exact browser implementation target:

```text
da115b74de526fca05ed6f468bef39bdb801355c
```

The browser now exposes:

```text
Context visible
Focus current process
Edit focus set
Reset example
```

When edit mode is active, each work unit exposes:

```text
+ FOCUS
    add work unit to current focus

- FOCUS
    remove work unit from current focus
```

Membership changes immediately update:

```text
node data-process-scope
membership summary count
strong focus suppression
connector current/context classification
```

A connector is contextual whenever either endpoint lies outside the current focus.

While editing, strongly suppressed context is temporarily raised to a more operable salience. Leaving edit mode restores the full suppression hierarchy.

The browser stores the edited focus set in `localStorage` only as design-lab convenience. This does not select production ownership or persistence semantics.

## Dependency-bound ideas

```text
C4 Port Grammar
    matured into connector-treatment / hover / directionality architecture

C5 Internal Layout Grammar
    remains deferred to semantic zoom / information-density slice
```

## Current gate

```text
human verifies Edit focus set is clear and unobtrusive
human verifies + FOCUS / - FOCUS do not imply project deletion
human adds and removes several nodes
human verifies Focus current process updates immediately
human verifies connector suppression follows edited membership
human verifies edit-mode recovery keeps outside-focus nodes operable
human verifies refresh persistence and Reset example behavior
-> refine / accept / reject editable focus membership
-> do not freeze production focus ownership or persistence yet
```

Runtime-state and priority/importance visual grammars remain separate future slices.

## Production boundary

Production `/cockpit` remains untouched. No graph/canvas dependency, automatic focus-selection algorithm, final focus-set ownership/persistence model, final project-disposition ontology, runtime-state grammar, importance grammar, production appearance persistence, motion library or final visual-system freeze is authorized by this thread.
