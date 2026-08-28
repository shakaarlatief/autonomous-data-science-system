# Research 083: A6 Adaptive Anchor and Canonical Box Sidebar Mode

**Date:** 2026-08-28  
**Status:** Active Phase-C design evidence / current working defaults inside Checkpoint 246  
**Scope:** Preserves the project owner's next Conversation Workspace decisions after first review of the scope/anchor browser: A6 Adaptive Anchor is selected as the working opened-box composition, work-unit-scoped conversations should reuse the already accepted Cockpit work-unit component rather than invent a separate mini-card design, and the conversation rail should let the user switch between canonical box view and ordinary text view.  
**Authority:** Research evidence only. A6 is selected "for now" and remains open to challenge by the pending Claude comparative/divergent follow-up. Final persistence semantics, responsive scaling, large-thread navigation and production implementation remain unfrozen.

## 1. Human disposition

The project owner selected:

```text
A6 Adaptive Anchor
    SELECTED WORKING DEFAULT FOR NOW
```

Meaning:

```text
work-unit-scoped conversation
    compact persistent home identity while reading
    + explicit Expand box action
    + richer work-unit inspector on demand
```

A0-A5 remain historical comparison evidence. A6 may still be challenged or improved by Claude before final promotion.

## 2. Canonical work-unit reuse in conversation navigation

The project owner rejected the need for a separately designed "mini work-unit artifact" visual grammar.

The desired principle is:

```text
THE BOX IN THE PROJECT WORLD
    =
THE BOX IN THE CONVERSATION RAIL

same semantic component
same accepted visual grammar
same category / disposition / operational-status / attention channels

only geometric scale / available width changes
```

This is preferable to maintaining a second mini-card design because it preserves immediate recognition and prevents visual-semantic drift between the Project Cockpit and Conversation Workspace.

The rail representation should therefore reuse the accepted work-unit component and its confirmed channels, including when applicable:

```text
scientific category shape and category hue
P7 project disposition
runtime or BLOCKED operational carrier
A3 attention bars
accepted surface/material and resting-light treatment
work-unit title and supporting line
```

SEL2 is **not** shown merely because a conversation belongs to a work unit:

```text
conversation home / ownership
    !=
project-map persistent selection
```

If the underlying work unit is actually selected in a context where selection semantics apply, SEL2 remains the accepted selection treatment. Conversation ownership by itself must not fake that state.

## 3. User-switchable conversation rail

The owner explicitly wants both rail modes available:

```text
BOXES
    canonical work-unit components
    scaled to fit the navigation rail
    strongest visual recognition and project continuity

TEXT
    conventional compact conversation list
    strongest density and familiarity
```

This is not a design-lab-only comparison anymore. It is a prospective user preference because both modes are useful and semantically compatible.

The current browser persists the chosen rail view in local browser storage for the prototype.

The prior `Marker + title` experiment is no longer part of the active two-mode control. It remains historical evidence rather than a current required mode.

## 4. Browser implementation refinement

Current route:

```text
http://localhost:5173/design-lab/conversation-workspace-work-unit-anchor.html
```

New implementation behavior:

```text
A6 remains the default opened-box presence mode.

Conversation sidebar
    Boxes / Text switch appears directly below search.

Boxes mode
    work-unit threads are rendered using the canonical accepted work-unit node markup
    existing accepted work-unit CSS is reused through a lower-priority cascade layer
    component is geometrically scaled for the rail
    no separate miniature semantic design is introduced

Text mode
    ordinary thread title + metadata list

Preference
    prototype persists Boxes/Text choice in localStorage when available
```

Implementation commits:

```text
c0fad7428d76c11397c706f36a00448b05d2abe2
    canonical work-unit renderer + Boxes/Text user switch

1c25b982c4da0d64b18a483057102adc468d9c35
    harden scaled canonical node block layout
```

New stylesheet:

```text
frontend/design-lab/conversation-workspace-work-unit-anchor-canonical-boxes.css
```

It imports the existing accepted work-unit design-lab styles into a named cascade layer. Existing Conversation Workspace styles remain unlayered and therefore continue to own the page-level layout, while the actual `.grammar-node` work-unit component retains its established visual grammar.

Production `/cockpit` remains untouched.

## 5. Why this is architecturally cleaner

The emerging component relationship is:

```text
canonical WorkUnit visual component
    project map instance
    conversation-rail instance
    compact conversation-home instance
    richer inspector instance where useful
```

rather than:

```text
project work-unit design
    + unrelated sidebar mini-card design
    + unrelated conversation-home card design
```

The first model reduces duplicate design logic and makes semantic state changes easier to recognize consistently across surfaces.

The final production implementation should ideally make scale/presentation variants properties of one component system rather than independent copies.

## 6. Current held Conversation Workspace direction

```text
Quiet Graphite
    held visual baseline

conversation scope
    Project general
    Work-unit scoped

conversation home
    separate from per-turn context

work-unit rail identity
    canonical box component, scaled
    OR user-selected text list

opened-box composition
    A6 Adaptive Anchor working default
```

## 7. Still open

```text
whether A6 survives Claude's follow-up unchanged
exact scale and density of canonical boxes in very long conversation lists
how completed/deferred/future visual state should update in old conversations
whether rail boxes show live state, historical state, or both
large-project grouping/search behavior
whether text/box preference is project-scoped or global
how A6 transitions from X5
whether A6 richer inspector should itself use X5 geometry/content
conversation re-homing / multi-home edge cases
final production component API
```

## 8. Collaboration consequence

Claude Message 010 remains the pending next model contribution.

Message 009 remains the original comparative/divergent request. A Message 009A addendum records these newer human decisions so Claude can evaluate them without rewriting the already-frozen request history.
