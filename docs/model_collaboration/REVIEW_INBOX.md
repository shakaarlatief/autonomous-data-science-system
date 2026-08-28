# Model Collaboration Review Inbox

**Date:** 2026-08-28  
**Status:** Current human-readable routing view  
**Authority:** Convenience index only. Per-thread `STATE.json`, `THREAD.md`, frozen requests, exact Git refs and resolution records remain authoritative.  
**Repository:** `shakaarlatief/autonomous-data-science-system`  
**Coordination branch:** `v1-cockpit-design-exploration`

## Routing discipline

The repository and coordination branch above must also be named explicitly in any human-to-Claude trigger prompt.

```text
coordination branch
    where Claude reads current routing, this inbox, thread state and request files

exact target ref / SHA
    immutable evidence or artifact a specific request may direct Claude to inspect
```

Claude should not infer or switch the coordination branch. If a trigger names a different branch than this authoritative routing state, Claude should stop and report the mismatch rather than choose a branch heuristically.

## Pending model obligation

```text
MC-0004 Message 010
Claude comparative/divergent Conversation Scope + Work-Unit Anchor ideation
```

Read both request records:

```text
docs/model_collaboration/threads/MC-0004/messages/009_chatgpt_conversation_scope_work_unit_anchor_ideation_request.md
docs/model_collaboration/threads/MC-0004/messages/009a_chatgpt_conversation_scope_anchor_human_refinement_addendum.md
```

Current checkpoint:

```text
246
```

## Next actor

```text
Claude
```

## Current held / working human direction

```text
Quiet Graphite
    current Conversation Workspace visual baseline

A6 Adaptive Anchor
    selected working opened-box composition for now

Conversation sidebar
    user-switchable Boxes / Text

Boxes mode
    reuse the canonical accepted WorkUnit component
    scale it geometrically for the rail
    do not invent a separate mini-card semantic design

Text mode
    ordinary compact conversation list
```

The currently rendered visual-system alternatives from the previous independent round remain rejected. Future palette exploration requires genuinely new candidates rather than reviving those variants.

## Active product model under review

The Conversation Workspace distinguishes:

```text
PROJECT-GENERAL CONVERSATION
    not owned by one work unit

WORK-UNIT-SCOPED CONVERSATION
    belongs to one work unit
    remains visually recognizable as belonging to that box

PER-TURN CONTEXT
    temporary referenced project objects
    separate from conversation home
```

Current browser:

```text
http://localhost:5173/design-lab/conversation-workspace-work-unit-anchor.html
```

Latest browser refinement commits:

```text
c0fad7428d76c11397c706f36a00448b05d2abe2
    canonical work-unit boxes + Boxes/Text user switch

1c25b982c4da0d64b18a483057102adc468d9c35
    canonical scaled-node layout hardening
```

Current research:

```text
docs/research/082_conversation_scope_work_unit_anchor_and_quiet_graphite_baseline.md
docs/research/083_a6_adaptive_anchor_and_canonical_box_sidebar_mode.md
```

## Claude requested contribution

Claude should inspect Message 009 and Message 009A and challenge/broaden:

```text
conversation-home versus per-turn-context mental model
A6 Adaptive Anchor and materially better alternatives if any
canonical WorkUnit reuse in conversation navigation
Boxes/Text dual-mode sidebar policy
project-general conversation identity
X5 -> work-unit conversation entry and return
re-homing / multi-object / completed-or-deferred-home edge cases
live versus historical state in old conversation navigation
large-thread-count behavior and accessibility
```

This follow-up is intentionally comparative rather than blind. Claude may inspect the current browser and proposal.

Production `/cockpit` remains untouched. Semantic zoom remains deferred with S0 as provisional working behavior. Z7 deep-focus remains held.
