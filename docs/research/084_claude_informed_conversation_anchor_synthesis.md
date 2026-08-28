# Research 084: Claude-Informed Conversation Anchor Synthesis

**Date:** 2026-08-28  
**Status:** Active Phase-C design evidence  
**Scope:** Synthesizes Claude Message 010 with the project owner's held Conversation Workspace decisions and opens a browser comparison of materially different work-unit-home composition mechanisms while keeping Quiet Graphite and the Boxes/Text sidebar choice fixed.  
**Authority:** Research evidence only. A6 remains the project owner's current working default. The new B1-B4 alternatives are challenge candidates, not replacements unless explicitly selected. Conversation persistence/schema, historical-state semantics, pinned context, final transition choreography, and production implementation remain unfrozen.

## 1. Claude response received

Claude completed:

```text
docs/model_collaboration/threads/MC-0004/messages/010_claude_conversation_scope_work_unit_anchor_ideation.md
```

Response commit:

```text
8c2c95aec8bf9d53e17500f4a38f9311d19a1e8b
```

Claude inspected the actual browser source at the exact target requested rather than reasoning from research prose alone.

## 2. Important implementation findings from Claude

Claude found four real asymmetries in the prior browser:

```text
1. only Model selection strategy / RUN could actually be opened
   BLOCKED and DEFER sidebar fixtures were visible but not selectable

2. A6 Expand box only revealed the same content as A5
   so A6's richer-detail claim had not actually been validated

3. very compact canonical representations hid much of the very grammar
   canonical reuse was intended to preserve

4. archived threads fell back to text even in Boxes mode
```

These findings are treated as implementation/design evidence rather than cosmetic observations.

## 3. Conversation-home model: Claude extension

Claude agrees with the held distinction:

```text
conversation home
    !=
per-turn context
```

and proposes a useful third tier:

```text
HOME
    zero or one owning project object

PINNED CONTEXT
    persistent whole-conversation context
    does not imply ownership

PER-TURN CONTEXT
    temporary objects relevant to one message/discussion
```

This resolves a case such as a conversation substantially concerning two work units without forcing artificial multi-home ownership.

Claude also recommends generalizing `home_object_id` beyond WorkUnit so a Decision, Dataset, Evidence object, or other addressable project object can eventually be a natural conversation home.

Current interpretation:

```text
home / pinned / per-turn
    PROMISING INTERFACE MENTAL MODEL
    not frozen persistence schema
```

The synthesis browser shows a small experimental pinned-context cue only to make the distinction tangible. This does not promote it.

## 4. Edge-case handling proposed by Claude

Preserved for later ontology/persistence work:

```text
general -> one work unit
    explicit Adopt as home
    never silent

work-unit scoped -> broader project discussion
    explicit Detach from work unit

conversation equally concerns two work units
    project-general + both pinned

home work unit completed/deferred/deleted/superseded
    preserve historical reference
    render historical-state treatment

conversation fork
    inherit home + pinned state at fork time
    diverge independently afterward

conversation re-home
    explicit operation
    visible transcript marker
```

No schema is frozen by this research note.

## 5. Sidebar consequences

The project owner's held product direction remains:

```text
Boxes
    canonical work-unit visual identity

Text
    conventional compact conversation list

user can switch
```

Claude's `Signature Rail` is preserved as an additional high-thread-count idea but is not added to the active user preference because the owner already selected the Boxes/Text balance and there is no real density evidence yet requiring a third mode.

The synthesis browser does incorporate Claude's historical-state critique:

```text
archived Boxes-mode entries
    remain box-shaped
    use a subdued HISTORICAL treatment
```

This is a browser hypothesis, not a final historical-state grammar.

## 6. A6 refinement

The project owner previously selected:

```text
A6 Adaptive Anchor
    current working default
```

Claude's strongest A6-specific recommendation is accepted for browser testing:

```text
A6 compact home identity
    -> Expand box
    -> X5-derived richer contextual panel
```

The prior implementation only toggled the old A5 inspector. The synthesis browser now gives the expanded state a materially richer X5-style field layout:

```text
Purpose
Constraint
Evidence
Next action
Recent activity
```

This remains a schematic X5 derivative. It does not reopen the deferred final C5 internal-layout grammar.

## 7. New composition candidates

New browser:

```text
http://localhost:5173/design-lab/conversation-workspace-anchor-synthesis.html
```

Files:

```text
frontend/design-lab/conversation-workspace-anchor-synthesis.html
frontend/design-lab/conversation-workspace-anchor-synthesis.css
frontend/design-lab/conversation-workspace-anchor-synthesis.js
frontend/design-lab/conversation-workspace-anchor-synthesis-fixes.js
```

Exact clean browser implementation target:

```text
93dba4688a0e78f5b1d60277761c59c65e79c98d
```

Candidate set:

```text
A6  Refined Adaptive Anchor
    current human-selected working default
    compact home identity at rest
    explicit expansion to richer X5-derived panel

B1  Breadcrumb Thread
    lightest persistent object-home cue
    project -> category -> work unit path above transcript

B2  Scroll-Responsive Presence
    fuller orientation object on arrival
    compressed object identity deeper in reading
    controlled by Arrival / Deep in transcript toggle for reliable comparison

B3  Object-Anchored Gutter
    thin category-owned edge treatment
    object-shaped content removed from primary reading field
    gutter control can recover richer context

B4  Wrapped Around Object
    high-risk structural alternative
    work-unit identity becomes outer conversation-frame chrome
    tests whether conversation can visually feel grown from the object
```

Claude's `Signature Rail` is orthogonal to opened-box composition and therefore not mixed into A6/B1-B4.

## 8. Browser repair and coverage improvements

The synthesis browser deliberately fixes the prior inability to exercise different home states:

```text
General project discussion
Model selection strategy     CURRENT + RUN + HIGH
Production missingness       CURRENT + BLOCKED
Threshold policy             DEFER + NONE
```

All four are selectable.

This lets the same composition be tested against project-general, live-running, blocked and deferred homes.

Archived Boxes-mode entries are also represented using subdued historical work-unit cards rather than silently changing to ordinary text.

## 9. Project-general treatment

Claude challenged the generic `P` fallback as looking like a fake category marker.

The synthesis browser instead uses project identity:

```text
Autonomous Data Science
Telco churn project
```

Project-general conversations have no work-unit home artifact and do not invent one.

## 10. Transition ideas preserved, not mixed into composition selection yet

Claude recommends reusing two mechanisms already explored in deep-focus work:

```text
ENTRY
    anchored to actual X5 object position

RETURN
    asymmetric / faster than entry
```

These are treated as transition modifiers, not competing composition architectures.

They should be tested after the Conversation Workspace composition is sufficiently settled, mirroring the earlier factorized deep-focus process.

## 11. Current review gate

Human review should compare A6/B1-B4 while holding the already selected fundamentals constant:

```text
Quiet Graphite
Boxes/Text user switch
project-general conversations exist
work-unit-scoped conversations exist
conversation home != per-turn context
canonical work-unit identity remains the preferred Boxes-mode principle
```

Useful review sequence:

```text
1. compare A6 against B1-B4 on Model selection strategy
2. click Production missingness and verify BLOCKED identity remains legible
3. click Threshold policy and verify DEFER still reads correctly
4. click General project discussion and verify no fake work-unit identity remains
5. switch Boxes/Text and verify composition choice is independent of rail preference
6. for B2 compare Arrival versus Deep in transcript
7. for A6 expand/collapse the X5-derived panel
8. reject mechanisms that compete with long-form reading rather than supporting orientation
```

## 12. Still open

```text
whether A6 remains winner after B1-B4 comparison
whether pinned context should be promoted
historical-state visual grammar
live-state vs state-at-conversation-time representation
very large thread-count behavior
whether Signature Rail is ever needed
exact X5-derived conversation panel content
entry/return choreography
conversation re-home interaction
non-work-unit homes
final persistence model
production component architecture
```

## 13. Checkpoint disposition

No new checkpoint is created.

Reason:

```text
Checkpoint 246 question
    Conversation Scope + Work-Unit Anchor

Claude response and synthesis browser
    broaden the same active design question
    do not yet change its semantic/promotion boundary
```

Checkpoint 246 therefore remains the correct current checkpoint until human review causes a genuine boundary transition.
