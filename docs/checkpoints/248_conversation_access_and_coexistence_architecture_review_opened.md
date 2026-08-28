# Checkpoint 248: Conversation Access and Coexistence Architecture Review Opened

**Date:** 2026-08-28  
**Status:** Current product-design checkpoint  
**Checkpoint class:** CONTINUITY / PRODUCT_DESIGN / INTERACTION_ARCHITECTURE  
**Project stage:** V1 next-generation Project Cockpit browser-rendered design exploration  
**Scope:** Corrects the previous entry-only Conversation Workspace framing and opens review of conversation as an orthogonal capability that must be reachable from Project Grid and Deep Dive states, either as full-focus chat or as a co-present work+conversation surface.  
**Authority:** Current Phase-C routing/evidence boundary. This checkpoint holds the previously accepted Conversation Workspace visual decisions and work-depth model while reopening only how conversation is invoked and composed with active work surfaces. Final split/dock geometry, persistence, URL state and production implementation remain unfrozen.  
**Interaction environment:** ChatGPT  
**Project / workspace:** Autonomous Data Science System  
**Interaction session:** chatgpt-08  
**Conversation title:** 08 - Project Cockpit Design Exploration  
**Primary collaborator:** ChatGPT

## 1. Trigger

The project owner clarified that the product must support conversation from every major work depth and that the previous Checkpoint 247 browser incorrectly treated the primary question as X5 -> full-chat replacement.

The corrected requirement is:

```text
Project Grid
    neutral / selected / X5 expanded
    -> conversation available

Deep Dive specialist workspace
    -> conversation available

Conversation
    may take full focus
    OR
    may coexist with the active work surface
```

## 2. Held work-depth architecture

```text
Project Grid
    compact work units
    -> SEL2 selected
    -> X5 expanded
    -> Z7 Deep Dive

Deep Dive
    full specialist workspace
```

None of those held states is replaced by this checkpoint.

## 3. Held conversation architecture

```text
compact native Cockpit composer
    remains available for lightweight Grid interaction

full Conversation Workspace
    Quiet Graphite baseline
    Boxes / Text user-switchable thread rail
    project-general conversations
    work-unit-scoped conversations
    A6 Expand box context action
    no redundant floating work-unit card
```

## 4. New architectural rule

Conversation presentation is orthogonal to underlying work context.

```text
WORK CONTEXT
    Grid neutral
    Grid selected
    Grid X5 expanded
    Deep Dive

x

CONVERSATION PRESENTATION
    compact / work-only
    full chat focus
    co-present right dock
    co-present balanced split
    co-present chat-dominant + work context
```

Conversation scope remains separately modeled:

```text
project-general
work-unit-scoped
```

Invocation origin does not silently change conversation ownership.

## 5. Required access behavior

```text
Global conversation action from Grid
    available regardless of Grid state

Open conversation from a work unit / X5
    can target that work unit's conversation directly

Conversation action from Deep Dive
    available inside specialist workspace

Chat about this work unit from Deep Dive
    can target the Deep Dive work unit's conversation directly

Switching conversation thread
    does not mutate the underlying Grid/Deep Dive work context
```

## 6. State preservation

Opening full or co-present conversation must not destructively reset the source surface.

Return/close should restore the same work context, including selected/X5/Deep Dive identity and relevant local UI state where feasible.

## 7. Recovered earlier evidence

Research 079 is reinterpreted rather than discarded.

```text
CV0 Focus Workspace
    full-chat-focus baseline

CV1 Right Dock
    useful co-present work-primary candidate

CV2 Split Workbench
    useful balanced co-present candidate

CV5 Focus + Context Rail
    useful chat-dominant co-present candidate

CV6 Conversation + Inspector
    useful focused-context evidence
```

The exact final mechanism remains open.

## 8. New factorized browser

Local route:

```text
http://localhost:5173/design-lab/conversation-workspace-access-coexistence.html
```

Files:

```text
frontend/design-lab/conversation-workspace-access-coexistence.html
frontend/design-lab/conversation-workspace-access-coexistence.css
frontend/design-lab/conversation-workspace-access-coexistence.js
```

Research:

```text
docs/research/086_conversation_workspace_orthogonal_access_and_coexistence_architecture.md
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

P3 is the initial browser default only. It is not selected.

## 9. Disposition of Checkpoint 247

```text
E0-E4 entry transitions
    preserved as possible full-focus motion evidence
    no winner selected

Checkpoint 247
    no longer the active boundary
    its problem framing was too narrow
```

Z7 remains the held Deep Dive entry transition and is unaffected.

## 10. Current human review gate

Judge the **system model first**, not pixel polish:

```text
1. can chat be opened from every Grid state without losing that state?
2. can a work-unit-specific chat be opened directly from its box/X5?
3. can chat be opened from Deep Dive?
4. does full-chat focus still make sense as one valid mode?
5. which co-present modes are useful for Grid + chat?
6. which co-present modes are useful for Deep Dive + chat?
7. should Grid and Deep Dive share one presentation grammar or tune proportions independently?
8. does closing chat clearly restore the underlying work context?
```

## 11. Still unfrozen

```text
final co-present composition
resizable split behavior
pane collapse / restore behavior
whether thread rail remains visible in every co-present width
exact conversation transition choreography
keyboard shortcuts
URL / session state
multi-window / detachable chat
conversation persistence and lifecycle schema
specialist-workspace local-state persistence details
final responsive behavior
```

Production `/cockpit` remains untouched.
