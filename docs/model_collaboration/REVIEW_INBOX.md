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

Request:

```text
docs/model_collaboration/threads/MC-0004/messages/009_chatgpt_conversation_scope_work_unit_anchor_ideation_request.md
```

Current checkpoint:

```text
246
```

## Next actor

```text
Claude
```

## Current visual baseline

The project owner selected:

```text
Quiet Graphite
    current Conversation Workspace baseline
```

The currently rendered alternatives from the previous independent round are rejected. Future palette exploration requires genuinely new candidates rather than reviving those variants.

## Active product question

The Conversation Workspace must distinguish:

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

Initial implementation target:

```text
56e32bc0a682bdb0a5bf54d5d9db7b3b987fdb7e
```

Research:

```text
docs/research/082_conversation_scope_work_unit_anchor_and_quiet_graphite_baseline.md
```

The browser factorizes:

```text
conversation scope
    Work-unit scoped / Project general

thread identity
    Text / Marker + title / Mini work-unit artifact

opened-box presence
    A0 Chat-only control
    A1 Header specimen
    A2 Context shelf
    A3 Inner sidecar
    A4 Floating instrument
    A5 Box inspector
    A6 Adaptive anchor
```

## Claude requested contribution

Claude should inspect Message 009 and broaden/challenge:

```text
conversation-home versus per-turn-context mental model
work-unit identity in the conversation rail
project-general conversation identity
conversation + opened-box composition
X5 -> work-unit conversation entry and return
edge cases such as re-homing, multi-object discussions and completed/deferred work units
```

This follow-up is intentionally comparative rather than blind. Claude may inspect the current browser and proposal.

Production `/cockpit` remains untouched. Semantic zoom remains deferred with S0 as provisional working behavior. Z7 deep-focus remains held.