# Research 082: Conversation Scope, Work-Unit Anchor, and Quiet Graphite Baseline

**Date:** 2026-08-28  
**Status:** Active Phase-C interaction-design evidence  
**Scope:** Preserves the project owner's first disposition after reviewing the independent Conversation Workspace families, holds Quiet Graphite as the current visual baseline, rejects the previously rendered alternative visual systems, and opens a more advanced browser study for conversation ownership and persistent work-unit identity inside the full Conversation Workspace.  
**Authority:** Research evidence only. Quiet Graphite is the current working visual baseline, not a permanent ban on future visual exploration. Final conversation ontology, work-unit anchoring semantics, multi-object conversation semantics, full workspace composition, persistence model and production implementation remain unfrozen.

## 1. Human disposition of the independent visual-system round

After reviewing the new Conversation Workspace designs, the project owner stated:

```text
Quiet Graphite
    best of the currently rendered systems
    use for now

Deep Navy
Warm Slate
Monochrome Signal
Violet Ink
Editorial Dark
Claude Technical Manuscript
Claude Studio Console
Claude Hybrid
    rejected as currently rendered visual systems
```

Important interpretation:

```text
Quiet Graphite
    CURRENT VISUAL BASELINE

other currently rendered color / full-system families
    REJECTED

future color exploration
    allowed only through genuinely new proposals
    not by silently reviving the rejected variants
```

This is stronger than the previous pre-synthesis state, but it does not freeze the final production palette forever.

## 2. New human requirement: conversation ownership must be explicit

The project owner clarified that the Conversation Workspace must support both:

```text
PROJECT-GENERAL CONVERSATION
    not attached to one box
    may discuss the project broadly

WORK-UNIT-SCOPED CONVERSATION
    explicitly belongs to one work unit / box
    should remain visually and cognitively connected to that box
```

This creates a critical distinction:

```text
conversation home / ownership
    which project object, if any, this conversation belongs to

per-turn context
    which objects are temporarily in scope for one message or discussion
```

These must not be conflated.

A project-general conversation may reference many work units without automatically becoming owned by one.

A work-unit-scoped conversation may reference neighboring objects without silently changing its home work unit.

This distinction is conceptually valuable for persistence, navigation, provenance and user orientation even though the final data model remains unfrozen.

## 3. Human proposal: preserve the box as a recognizable identity artifact

The project owner specifically proposed that work-unit-scoped conversations should be immediately recognizable from their associated box rather than requiring the user to remember conversation titles.

The intended direction is not:

```text
restore the entire project grid
keep a giant full work-unit card permanently visible
```

Instead:

```text
canonical work-unit identity
    survives inside Conversation Workspace
    as a compact artifact / specimen / instrument
    analogous in spirit to the compact topology compass
```

Potential benefits:

```text
visual recognition without title recall
semantic continuity between project map and conversation
clear distinction between general and work-unit conversations
stronger provenance of where a conversation belongs
faster return from long conversation history to project structure
```

Primary risk:

```text
copying full work-unit cards too literally into every thread entry
    -> clutter
    -> weak transcript hierarchy
    -> left rail becomes another miniature project map
```

Therefore the study uses compact identity artifacts rather than full map replicas.

## 4. New browser

Local route:

```text
http://localhost:5173/design-lab/conversation-workspace-work-unit-anchor.html
```

Files:

```text
frontend/design-lab/conversation-workspace-work-unit-anchor.html
frontend/design-lab/conversation-workspace-work-unit-anchor.css
frontend/design-lab/conversation-workspace-work-unit-anchor.js
```

Initial implementation target:

```text
56e32bc0a682bdb0a5bf54d5d9db7b3b987fdb7e
```

Current repaired browser implementation target:

```text
9a5443f3fb248d38768c4fedf48a025a6eda6016
```

The later commit `145e96a502b23c513e14ca3520412d7acf0aa625` only removes an unused, unreferenced CSS override file and does not change rendered browser behavior.

Two semantic/interaction repairs were made after the initial target:

```text
thread active state
    only the actual active conversation is highlighted
    not every work-unit-scoped conversation simultaneously

conversation home artifact
    does NOT reuse SEL2 corner brackets
    because home/ownership != persistent selection
```

That second correction is important. A conversation being owned by a work unit must not visually imply that the same work unit is currently selected on the project map.

Production `/cockpit` remains untouched.

## 5. Factorized controls

The browser deliberately separates three questions.

### 5.1 Conversation scope

```text
Work-unit scoped
Project general
```

When Project general is active, work-unit anchoring disappears rather than inventing a fake box.

### 5.2 Thread-list identity

```text
Text control
Marker + title
Mini work-unit artifact
```

The mini-artifact direction tests the project owner's proposal most directly.

Work-unit artifacts reuse project semantics in compact form:

```text
category shape
category hue
project disposition cue
runtime / BLOCKED cue where useful
attention bars where useful
work-unit title
```

A project-general conversation uses a separate neutral project-level identity artifact.

### 5.3 Opened-box presence inside the full Conversation Workspace

```text
A0  Chat-only control
A1  Header specimen
A2  Context shelf
A3  Inner sidecar
A4  Floating instrument
A5  Box inspector
A6  Adaptive anchor
```

All use Quiet Graphite and the same transcript.

## 6. Candidate meanings

```text
A0 Chat-only control
    no persistent home-box artifact after entry
    baseline only

A1 Header specimen
    tiny canonical work-unit specimen beside conversation title
    strongest title-level ownership signal

A2 Context shelf
    compact horizontal work-unit artifact between header and transcript
    more legible context without a side rail

A3 Inner sidecar
    narrow work-unit specimen column inside the conversation workspace
    persistent but deliberately smaller than a full project map region

A4 Floating instrument
    small compass-like work-unit identity instrument floating over the transcript
    maximum spatial lightness

A5 Box inspector
    dedicated right-side work-unit inspector
    most explicit simultaneous conversation + opened-box composition

A6 Adaptive anchor
    compact header/floating identity at rest
    explicit Expand box action opens the richer right-side inspector
    tests whether persistent recognition and on-demand detail can coexist
```

A6 is an experimental synthesis, not a preselected winner.

## 7. Held visual baseline

This browser intentionally does not reopen palette selection.

Held:

```text
Quiet Graphite
neutral graphite surfaces
restrained mint interface signal
technical sans
ADS responses document-like
user turns compact bounded prompts
project references semantic objects
structured project changes separate from prose
tool / activity detail secondary and collapsed
```

Future visual-system work must introduce genuinely new candidates if the palette is reopened.

## 8. New semantic hypothesis

A useful prospective model is:

```text
Conversation
    home_scope
        PROJECT_GENERAL
        or WORK_UNIT

    home_object_id
        null for project-general
        one work-unit id for work-unit scoped

Message / composer context
    contextual_object_ids
        zero or more project objects
```

This is only a conceptual hypothesis for interface reasoning.

It is not a frozen persistence schema.

Multi-home conversations, conversations anchored to non-work-unit objects, and conversation branching remain unfrozen.

## 9. Human review questions

```text
Does the mini work-unit artifact make thread ownership instantly recognizable?
Is a full miniature box too visually heavy in the left rail?
Should general project conversations have an explicitly different identity artifact?
Which A0-A6 treatment best combines the opened work unit with long-form chat?
Does A4 feel elegantly instrument-like or too detached from the conversation?
Does A5 become too much like a permanent inspector/sidebar?
Does A6 preserve identity while keeping detail optional?
Should the work-unit artifact expand back toward X5 contextual detail on demand?
```

## 10. Claude follow-up

The independent round is complete, so the next Claude contribution does not need to remain blind.

Claude request:

```text
docs/model_collaboration/threads/MC-0004/messages/009_chatgpt_conversation_scope_work_unit_anchor_ideation_request.md
```

Expected output:

```text
MC-0004 Message 010
```

Claude is asked to inspect the new requirement and browser, challenge the proposed semantic distinction and anchor mechanisms, and add any materially different ideas for:

```text
conversation ownership / home semantics
work-unit identity in the thread rail
conversation + opened-box composition
project-general conversation treatment
transition between X5 opened box and work-unit-scoped conversation
```

No artificial candidate-count limit applies.

## 11. Checkpoint disposition

The prior whole-system visual comparison materially changed state:

```text
Quiet Graphite selected as current baseline
other rendered visual systems rejected
new active question = conversation scope + work-unit anchoring
```

Checkpoint 246 therefore opens the current product-design boundary.