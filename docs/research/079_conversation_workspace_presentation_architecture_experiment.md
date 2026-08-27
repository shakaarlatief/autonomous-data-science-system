# Research 079: Conversation Workspace Presentation Architecture Experiment

**Date:** 2026-08-27  
**Status:** Active Phase-C interaction-design evidence  
**Scope:** Opens the first browser-rendered comparison for the full persistent Conversation Workspace after the project owner deferred semantic zoom with S0 Geometric Control as the working default.  
**Authority:** Research evidence only. No final conversation persistence model, session ontology, transcript schema, presentation architecture, conversation/project linking semantics, storage model or production component architecture is frozen by this memo.

## 1. Trigger

Research 078 is now deferred with:

```text
S0 Geometric Control
    provisional working default

S1-S8
    preserved for later
    not rejected
```

This makes the next high-value unresolved problem the Conversation Workspace already identified as first-class in Research 037 and required by the project owner.

The governing product requirement is:

```text
compact Cockpit composer
    must coexist with
serious persistent long-form project conversation
```

A permanent giant chat sidebar is not assumed.

## 2. Governing conversation distinction

Research 037 distinguishes:

```text
Composer
    lightweight Cockpit entry point

Conversational response
    user-visible answer in current context

Conversation history
    durable visible multi-turn dialogue

Conversation Workspace
    full surface for reading, searching and continuing long discussions
```

The browser tests only presentation architecture for the fourth layer.

The transcript remains user-visible dialogue. It is not raw chain-of-thought or unrestricted orchestration trace.

Consequential project truth remains in structured project state rather than existing only in conversation prose.

## 3. New browser

Local route:

```text
http://localhost:5173/design-lab/conversation-workspace-architecture.html
```

Files:

```text
frontend/design-lab/conversation-workspace-architecture.html
frontend/design-lab/conversation-workspace-architecture.css
frontend/design-lab/conversation-workspace-architecture.js
```

Exact initial implementation target:

```text
42cfe87a0531206187741488f35785fc87f10f1e
```

Production `/cockpit` remains untouched.

## 4. Held controls

```text
compact native Cockpit composer remains
S0 geometric zoom is the current working default
SEL2 selection remains accepted
X5 contextual expansion remains accepted
Z7 deep-focus transition remains accepted
fullscreen specialist-workspace direction remains accepted
structured project state remains canonical for consequential outcomes
```

The project map fixture is schematic and exists only to test conversation/context composition.

## 5. Controlled candidates

```text
CV0  Focus Workspace
    conversation replaces the project map
    strongest long-form reading surface

CV1  Right Dock
    conversation opens as a right region
    project map contracts into remaining safe area

CV2  Split Workbench
    project and conversation share the stage equally

CV3  Canvas Lens
    large floating transcript remains spatially inside the Cockpit
    project recedes behind it

CV4  Bottom Workbench
    conversation grows upward from the compact composer
    project remains visible above

CV5  Focus + Context Rail
    conversation owns most of the stage
    narrow project-context rail preserves orientation

CV6  Conversation + Inspector
    long-form transcript paired with selected-work contextual inspector

CV7  Progressive Recent-to-Full
    compact composer -> recent-turn surface -> full Conversation Workspace

CV8  Tabbed Stage
    Project and Conversation behave as route-like peer stages
```

The candidate count is evidence-driven rather than arbitrarily capped.

## 6. Same conversation, different surfaces

Every candidate uses the same underlying conceptual conversation.

The fixture deliberately includes:

```text
user messages
ADS messages
project-object references
blocking relationship reference
system-visible structured project change
continuing composer
```

This tests whether conversation can be a navigational/explanatory view over real project state instead of a parallel chat universe.

The actual persistence model remains unfrozen.

## 7. Interaction behavior

Most candidates toggle directly between project and full Conversation Workspace.

CV7 deliberately tests a progressive-depth hypothesis:

```text
compact composer
    -> recent turns
    -> full Conversation Workspace
```

This is the only candidate with an explicit intermediate layer because the existence of a recent-context layer is itself part of that architecture.

## 8. Human review gate

Review questions:

```text
which architecture is best for genuinely long discussions?
when should the project map remain simultaneously visible?
does a right dock become a permanent giant sidebar?
does full Conversation Focus fit the same product-depth metaphor as analytical work?
is a compact context rail enough orientation?
is a selected-work inspector useful or distracting?
does recent-context expansion earn an intermediate interaction layer?
should Project and Conversation be peer routes/tabs?
```

The human may prefer, reject, combine or refine mechanisms.

## 9. Still unfrozen

```text
one conversation versus multiple project conversations
named conversations / sub-conversations
fork / branch / archive / resume lifecycle
search and filtering
message-to-project linking semantics
project-object-to-conversation linking
conversation compaction / summaries
conversation URL state
conversation workspace relation to specialist analytical workspaces
split-state persistence
responsive/mobile behavior
conversation data model and storage
production rendering / virtualization
```

## 10. Checkpoint disposition

The semantic-zoom gate has materially changed state from active comparison to deferred working default, so a new checkpoint is warranted before this first-class conversation problem is reviewed.
