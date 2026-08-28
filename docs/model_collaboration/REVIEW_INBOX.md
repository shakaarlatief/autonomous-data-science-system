# Model Collaboration Review Inbox

**Date:** 2026-08-28  
**Status:** Current human-readable routing view  
**Authority:** Convenience index only. Per-thread `STATE.json`, `THREAD.md`, frozen requests, exact Git refs and resolution records remain authoritative.  
**Repository:** `shakaarlatief/autonomous-data-science-system`  
**Coordination branch:** `v1-cockpit-design-exploration`

## Routing discipline

The repository and coordination branch above must also be named explicitly in any human-to-Claude trigger prompt.

Claude should not infer or switch the coordination branch. If a trigger names a different branch than this authoritative routing state, Claude should stop and report the mismatch rather than choose a branch heuristically.

## Pending model obligation

```text
none
```

Claude Message 010 is complete at:

```text
8c2c95aec8bf9d53e17500f4a38f9311d19a1e8b
```

## Next actor

```text
human project owner
```

Current checkpoint:

```text
248
```

## Held Conversation Workspace direction

```text
Quiet Graphite
    current visual baseline

Conversation sidebar
    user-switchable Boxes / Text

Boxes mode
    canonical WorkUnit visual component scaled for navigation

A6 Adaptive Anchor
    current opened-box composition

A6 resting state
    no redundant floating work-unit box
```

## Architecture correction from project owner

Conversation must be reachable from every major work depth and may either take full focus or coexist with the active work surface.

```text
WORK CONTEXT
    Grid neutral
    Grid selected
    Grid X5 expanded
    Deep Dive

x

CONVERSATION PRESENTATION
    compact / work only
    full chat focus
    co-present work + chat

x

CONVERSATION SCOPE
    project-general
    work-unit-scoped
```

A global conversation action must be available regardless of Grid state. Work units/X5 and Deep Dive must also support direct opening of the corresponding work-unit conversation. Closing chat should preserve and restore the same underlying work context.

Research 079's earlier split/dock/context-rail ideas are recovered as co-presence evidence. They were not rejected by later Conversation Workspace visual decisions.

## Current active review

Research:

```text
docs/research/086_conversation_workspace_orthogonal_access_and_coexistence_architecture.md
```

Browser:

```text
http://localhost:5173/design-lab/conversation-workspace-access-coexistence.html
```

The browser factorizes:

```text
UNDERLYING WORK SURFACE
    Grid neutral
    Grid selected
    Grid X5 expanded
    Deep Dive

CONVERSATION
    Project general
    Current work-unit chat

PRESENTATION
    P0 Work only / compact chat
    P1 Full chat focus
    P2 Right dock
    P3 Balanced split
    P4 Chat dominant + work context
```

P3 is the initial browser default only, not a selected result.

Checkpoint 247's E0-E4 transition candidates remain preserved as possible full-chat-focus motion evidence. No winner was selected because the entry-only framing was incomplete.

Production `/cockpit` remains untouched. Semantic zoom remains deferred with S0 as provisional working behavior. Z7 specialist deep focus remains held.
