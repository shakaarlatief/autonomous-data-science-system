# Research 086: Conversation Workspace Orthogonal Access and Coexistence Architecture

**Date:** 2026-08-28  
**Status:** Active Phase-C interaction-design evidence  
**Scope:** Corrects the overly narrow Conversation Workspace entry-only framing from Checkpoint 247 and defines the next review around conversation availability across Project Grid and specialist Deep Dive states, including both full-focus chat and simultaneous work+conversation compositions.  
**Authority:** Research evidence only. This memo does not select a final split/dock architecture, conversation persistence schema, URL contract, responsive policy, or production component implementation.  

## 1. Trigger

The project owner clarified that the previous Conversation Workspace entry-transition browser framed the problem too narrowly.

The product is not:

```text
project/work surface
    -> replace it with chat
```

Conversation is a first-class capability that must be reachable from multiple work surfaces and may either take full focus or coexist with the currently active work surface.

The earlier Research 079 split/dock/context-rail candidates therefore remain relevant evidence. They were not invalidated by the later Quiet Graphite/A6 work. They need to be reinterpreted as **conversation presentation modes over an underlying work surface**, rather than mutually exclusive whole-product architectures.

## 2. Held work-surface hierarchy

The Project Cockpit still has the held work-unit depth ladder:

```text
PROJECT GRID
    compact work units

    -> SEL2 selected work unit

    -> X5 contextual expansion

    -> Z7 Pull-Back Then Dive

SPECIALIST WORKSPACE / DEEP DIVE
    full-resolution analytical work surface
```

The Grid and Deep Dive are work surfaces. Conversation should not erase this conceptual distinction.

## 3. Held conversation layers

The product also has distinct conversation layers:

```text
COMPACT COCKPIT COMPOSER
    lightweight interaction while staying in the Grid

FULL CONVERSATION WORKSPACE
    persistent long-form conversation surface
    Quiet Graphite current baseline
    Boxes/Text thread rail
    project-general and work-unit-scoped conversations
    A6 work-unit context expansion
```

The compact composer and full Conversation Workspace are not substitutes for each other.

## 4. Key architectural correction: conversation is orthogonal to work depth

The robust model is factorized:

```text
WORK CONTEXT
    Project Grid
        neutral
        selected work unit
        X5 expanded work unit

    Specialist Workspace / Deep Dive

x

CONVERSATION PRESENTATION
    compact composer
    full-focus Conversation Workspace
    co-present Conversation Workspace

x

CONVERSATION SCOPE
    project-general
    work-unit-scoped
    future pinned/per-turn context as separately modeled context
```

This means entering conversation does **not** inherently mean destroying or abandoning the underlying work context.

## 5. Required access paths

### 5.1 From Project Grid, regardless of Grid state

The user must be able to open the full Conversation Workspace while the Grid is:

```text
neutral
one work unit selected
one work unit expanded as X5
```

A global Conversation action should remain available regardless of those states.

If the user opens a conversation globally, the target may be a project-general conversation or any selected conversation from the conversation list.

If the user explicitly invokes conversation from a work unit, ADS should open that work unit's corresponding conversation when one exists, or create/open the appropriate work-unit-scoped conversation according to future lifecycle rules.

### 5.2 From Deep Dive

The user must be able to invoke conversation from inside a specialist workspace.

Two presentation outcomes must be possible in the product architecture:

```text
FULL CHAT FOCUS
    Conversation Workspace takes the active stage
    specialist workspace is preserved underneath as recoverable state

CO-PRESENT WORK + CHAT
    specialist workspace remains visible and usable
    Conversation Workspace shares the application stage
```

Opening chat from Deep Dive should naturally be able to target that work unit's conversation, while still allowing the user to switch to project-general or other conversations.

## 6. State preservation requirement

Opening conversation must not destructively reset the source work context.

At minimum, return/close should be able to restore:

```text
Grid viewport / zoom as appropriate UI state
selected work unit
X5 expanded state when it was the source
Deep Dive workspace identity
relevant specialist-workspace local UI state where feasible
```

Therefore:

```text
full-focus Conversation Workspace
    is a presentation/focus state
    not a destructive replacement of the underlying project state
```

Exact URL/session persistence remains unfrozen.

## 7. Conversation invocation and conversation scope are separate

Invocation origin should not be conflated with conversation ownership.

Examples:

```text
Global Chat from neutral Grid
    -> project-general or chosen thread

Global Chat while X5 is open
    -> does not silently make the conversation owned by that work unit

Open conversation from X5
    -> work-unit-scoped conversation for that X5 home

Open conversation from Deep Dive
    -> naturally offers/opens the Deep Dive work unit's conversation

Switch thread after opening
    -> changes active conversation
    -> does not mutate the underlying Grid/Deep Dive work context
```

This continues the held distinction between conversation home and temporary context.

## 8. Reinterpretation of Research 079

The following earlier candidates become directly relevant as **co-presence mechanisms**:

```text
CV1 Right Dock
    work surface remains primary
    conversation occupies a bounded right region

CV2 Split Workbench
    work and conversation share the stage more equally

CV5 Focus + Context Rail
    conversation dominates while a narrow live work-context rail remains

CV6 Conversation + Inspector
    conversation paired with focused work-unit context
```

CV0 Focus Workspace remains the full-chat-focus baseline.

CV3 Canvas Lens, CV4 Bottom Workbench, CV7 Progressive Recent-to-Full and CV8 Tabbed Stage remain historical evidence and may be revisited if materially useful, but are not automatically promoted.

## 9. Next browser should factorize instead of bundle

The next executable comparison should let the project owner independently choose:

```text
UNDERLYING WORK SURFACE
    Grid neutral
    Grid selected
    Grid X5 expanded
    Deep Dive

CONVERSATION TARGET
    Project general
    Current work-unit conversation

CONVERSATION PRESENTATION
    Work only / compact composer
    Full chat focus
    Right dock
    Balanced split
    Chat-dominant + live work-context rail
```

This is preferable to separate browsers that accidentally imply only one valid entry path.

## 10. Important non-decisions

Still unfrozen:

```text
final co-present layout
whether Grid and Deep Dive use exactly the same split proportions
whether chat pane carries the full thread rail at every width
resizable split behavior
pane collapse rules
conversation open/close transition choreography
keyboard shortcuts
URL representation
multi-window / detachable conversation possibilities
conversation lifecycle and persistence schema
specialist-workspace local-state persistence details
responsive behavior below desktop/laptop target widths
```

## 11. Disposition of Checkpoint 247 transition browser

The entry-transition experiment remains useful motion evidence, but its framing is incomplete because it assumes X5 -> full-chat replacement as the principal problem.

Therefore:

```text
E0-E4
    preserved as possible FULL-FOCUS transition choreography evidence
    no winner selected

Checkpoint 247
    superseded as the active review boundary by the broader
    conversation access + coexistence architecture question
```

The work-unit deep-focus Z7 decision remains unaffected.

Production `/cockpit` remains untouched.
