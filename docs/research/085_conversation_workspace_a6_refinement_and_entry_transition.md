# Research 085: Conversation Workspace A6 Refinement and Entry Transition

**Date:** 2026-08-28  
**Status:** Active Phase-C design evidence  
**Scope:** Records the project owner's rejection of the Claude-informed composition alternatives as irrelevant to the already chosen Conversation Workspace direction, removes the redundant floating A6 work-unit box, and opens the next bounded question: how an X5-opened work unit should transition into its full Conversation Workspace.  
**Authority:** Research evidence only. Quiet Graphite, Boxes/Text sidebar choice, A6 as the current opened-box composition, and the no-floating-box refinement are held working directions. Entry/return choreography remains under review.

## 1. Human disposition after Claude synthesis

The project owner explicitly clarified that the Claude-informed B1-B4 composition alternatives do not change the already chosen Conversation Workspace look.

Current interpretation:

```text
Quiet Graphite
    HELD

Conversation sidebar
    Boxes / Text user switch
    HELD

Work-unit-scoped conversation identity
    active canonical work-unit box in sidebar
    conversation title / WORK UNIT identity
    Expand box action
    HELD

A6 Adaptive Anchor
    HELD WORKING COMPOSITION

B1 Breadcrumb Thread
B2 Scroll-Responsive Presence
B3 Object-Anchored Gutter
B4 Wrapped Around Object
    NOT RELEVANT TO CURRENT CHOSEN LOOK
    preserved only as research history
```

Claude Message 010 remains useful evidence for later ontology, historical-state, density and edge-case work, but its additional composition candidates are not active alternatives.

## 2. Redundant A6 floating box removed

The project owner identified the small floating work-unit card in the upper-right transcript area as redundant.

The reason is straightforward:

```text
which work unit owns this conversation?

already communicated by
    active canonical box in sidebar
    conversation title
    WORK UNIT scope label
    Expand box action
```

Therefore another persistent floating box adds repetition without new information.

Refinement:

```text
A6 REST
    no floating work-unit card

A4 Floating Instrument
    remains historical experiment behavior only
```

Exact implementation commit:

```text
606e027f281b35c2dfc93d059a1681df23bc2b73
```

The change only removes the adaptive-mode selector from the rule that exposes `.floating-anchor`. It does not alter A4, the sidebar, title, composer, or explicit expanded-box behavior.

## 3. Current Conversation Workspace identity hierarchy

The resulting work-unit-scoped Conversation Workspace is intentionally simpler:

```text
LEFT SIDEBAR
    canonical work-unit object recognition

HEADER
    conversation title
    WORK UNIT scope
    Expand box

READING FIELD
    transcript remains visually clean
    no repeated home-object card

EXPAND BOX
    richer work-unit context only when requested
```

This is the current working balance between project-object continuity and transcript readability.

## 4. Next bounded question: entry and return choreography

With destination composition settled enough to proceed, the next question is:

```text
How should an X5-opened work unit become its full Conversation Workspace,
and how should the user return to project context?
```

This is separate from the destination layout itself.

New browser:

```text
http://localhost:5173/design-lab/conversation-workspace-entry-transition.html
```

Files:

```text
frontend/design-lab/conversation-workspace-entry-transition.html
frontend/design-lab/conversation-workspace-entry-transition.css
frontend/design-lab/conversation-workspace-entry-transition.js
```

Initial implementation target:

```text
43ee0ae0ffc63eba6e99a42e9157568c53cc8806
```

Production `/cockpit` remains untouched.

## 5. Controlled destination

Every transition ends in the same held destination:

```text
Quiet Graphite Conversation Workspace
Boxes/Text sidebar architecture
active canonical work-unit box in sidebar
conversation title + WORK UNIT scope
A6 Expand box action
NO floating A6 work-unit card
full transcript + composer
```

Only entry/return choreography changes.

## 6. Transition candidates

```text
E0 Direct Replace
    baseline
    project world disappears and conversation appears

E1 Anchored Grow
    conversation grows from the actual rendered X5 location
    tests object continuity

E2 World Recede
    project world moves backward in depth
    Conversation Workspace comes forward

E3 Pull-Back Then Dive
    adapts the already liked Z7 spatial family
    small pull-back establishes orientation
    then camera dives through the work-unit locus into conversation

E4 X5 Aperture
    X5 itself becomes an aperture into the Conversation Workspace
    the aperture expands until the conversation owns the stage
```

E3 is the initial browser default only. It is not selected.

## 7. Return modifier

The browser also factorizes return behavior:

```text
Fast direct return
    faster than entry
    tests asymmetric navigation

Symmetric return
    roughly mirrors entry
```

This modifier is not yet selected.

## 8. Still open

```text
final Conversation Workspace entry transition
final return choreography
whether conversation and specialist-workspace entry should share one motion family
exact duration/easing
interruption/cancellation
browser back/forward semantics
reduced-motion final behavior
conversation URL state
final A6 expanded-box internal composition
conversation persistence/lifecycle ontology
```
