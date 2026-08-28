# Autonomous Data Science System

## Overview

This repository is the persistent development home of the Autonomous Data Science System (ADS).

ADS is being developed as a rigorous, adaptive, semi-autonomous environment for data-science projects in which a strong LLM is one flexible reasoning component inside a wider system that owns project memory, methodological navigation, provenance, execution coordination, deterministic guarantees where justified, and a professional human interaction surface.

> **The chat is where we think. The repository is where the system remembers.**

## Current development stage

```text
checkpoint            248
active branch         v1-cockpit-design-exploration
active PR             none
exploration base      2480109fadeee1e480ef03b82e335aacdf9adf91
promoted V1 head      ed5b60bdc882bed0799ce55228ce8187f9c55aa1
latest specification  Specification 024
Cockpit baseline      Specification 008
current boundary      Conversation access + coexistence architecture review
source-vault          PAUSED, preserved, Course 2 gate unchanged
```

Specification 022 remains `INCOMPLETE / EXECUTION INTEGRITY FAILED`; no scientific `GENERIC` / `ADS_HORIZON` / `ORACLE_HORIZON` comparison may be inferred from that run.

## Held Cockpit design direction

```text
G4 Adaptive Hybrid world
H4 hover/world response
Reduced in-box resting light
scientific category-marker grammar
E5 Hue + Tag relation-class carrier
P7 Neutral Tag + Tone disposition
editable current-process focus set
conditional runtime semantics
switchable runtime carrier with T7 Soft Shade tag
BLOCKER -> BLOCKS -> BLOCKED cause/effect model
BLOCKED sharper compact ring
FAIL smoother circular compact ring
A3 Signal Bars for HIGH attention
SEL2 Corner Brackets for persistent selection
X5 balanced contextual expansion without context recession
L0 Flat Fields provisional expanded-card default
Z7 Pull-Back Then Dive specialist-workspace entry
fullscreen specialist-workspace end state
compact topology compass retained
S0 Geometric Control provisional zoom working default
Quiet Graphite Conversation Workspace baseline
Boxes / Text user-switchable conversation rail
A6 Adaptive Anchor opened-box composition
A6 resting state has no redundant floating work-unit box
```

Semantic zoom remains deliberately deferred. S0 is the working behavior; S1-S8 remain preserved and not rejected.

## Conversation architecture correction

The current product model now treats conversation as orthogonal to work depth.

```text
WORK CONTEXT
    Project Grid
        neutral
        selected work unit
        X5 expanded work unit

    Deep Dive specialist workspace

x

CONVERSATION PRESENTATION
    compact Cockpit composer / work only
    full Conversation Workspace focus
    co-present Conversation Workspace

x

CONVERSATION SCOPE
    project-general
    work-unit-scoped
```

A global conversation action must be available regardless of Grid state. A work unit/X5 can open its corresponding conversation directly. Deep Dive must also expose conversation, both as full chat focus and as a simultaneous work+chat composition.

Opening conversation must not destructively reset the underlying Grid selection/X5 or Deep Dive state. Closing or collapsing conversation should restore the same work context.

Research 079's earlier dock/split/context-rail ideas remain relevant as co-presence mechanisms rather than mutually exclusive whole-product architectures.

## Active Slice: Conversation access + coexistence

Primary browser:

```text
http://localhost:5173/design-lab/conversation-workspace-access-coexistence.html
```

Research and checkpoint:

```text
docs/checkpoints/248_conversation_access_and_coexistence_architecture_review_opened.md
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

P3 is the initial browser default only and is not selected.

Checkpoint 247's E0-E4 transition candidates remain preserved as possible **full-chat-focus** motion evidence, but no winner was selected because the entry-only framing was too narrow.

Production `/cockpit` remains untouched.

## Repository preservation

```text
repository architecture        SOUND
structural overhaul            NOT WARRANTED
new knowledge subsystem        NOT JUSTIFIED
checkpoint granularity         HARDENED
validation closure             HARDENED
active-branch routing guard    HARDENED
Claude branch routing          EXPLICIT
```

Historical checkpoints and research records remain the durable evidence layer. Current routing documents are navigation surfaces, not replacements for those records.

## Start here

```text
docs/CURRENT_STATE.md
docs/KNOWLEDGE_MAP.md
docs/current_routing.json

docs/checkpoints/248_conversation_access_and_coexistence_architecture_review_opened.md
docs/research/086_conversation_workspace_orthogonal_access_and_coexistence_architecture.md
frontend/design-lab/conversation-workspace-access-coexistence.html

docs/research/079_conversation_workspace_presentation_architecture_experiment.md
docs/research/085_conversation_workspace_a6_refinement_and_entry_transition.md
frontend/design-lab/conversation-workspace-entry-transition.html

frontend/design-lab/conversation-workspace-work-unit-anchor.html
docs/research/083_a6_adaptive_anchor_and_canonical_box_sidebar_mode.md

docs/model_collaboration/threads/MC-0004/THREAD.md
docs/model_collaboration/threads/MC-0004/STATE.json
docs/model_collaboration/REVIEW_INBOX.md
```
