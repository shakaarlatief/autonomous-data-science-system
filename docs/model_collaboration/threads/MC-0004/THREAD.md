# MC-0004: Next-Generation Project Cockpit Design Exploration

**Thread:** MC-0004  
**Status:** ACTIVE / PHASE C BROWSER DESIGN EVALUATION  
**Review mode:** `INDEPENDENT_THEN_COMPARATIVE`  
**Task owner:** ChatGPT  
**Target-state write owner:** ChatGPT  
**Claude role:** independent reviewer / counter-designer / researcher  
**Human project owner:** final arbiter of product-intent choices  
**Opened:** 2026-08-26

## Collaboration history

```text
Phase A
    Claude independent proposal
    cd2e12f2c79ee3b2f205457c5940eb2022b4631a
    BLIND_TO_CANDIDATE

Phase B
    Claude comparative review
    d94d696214a41d2a3904aa9ce2a42bdab5f2f3ce
    COMPARATIVE_ONLY

Phase C divergent work-unit ideation
    ChatGPT Message 003
    Claude Message 004

Phase C divergent deep-focus ideation
    ChatGPT Message 005
    Claude Message 006
    204664ae1e732dd504174bbc62545e9a93adc85f

Phase C Conversation Workspace independent dual design
    ChatGPT Message 007 blind request
    frozen base c190420c6d77d3191ca9efb9ffc1e401bbb7fda8
    ChatGPT isolated browser frozen at c66f72a74e681f89fd52ba591a1387ea50f0e959
    Claude Message 008 completed at cab2e464d81b48edadd1b6ae51bb7dd620d7e892
    blind gate COMPLETE

Phase C Conversation Scope + Work-Unit Anchor
    Quiet Graphite selected current baseline
    Checkpoint 246
    Research 082
    ChatGPT Message 009
    Claude Message 010 pending
```

## Preserved accepted / working Phase-C results

```text
G4 Adaptive Hybrid world
H4 hover/world response
Reduced in-box resting light
scientific marker category grammar
P7 Neutral Tag + Tone disposition
editable current-process focus set
conditional runtime semantics
one switchable runtime carrier
T7 Soft Shade runtime tag
BLOCKER -> BLOCKS -> BLOCKED cause/effect model
BLOCKED sharper compact ring
FAIL smoother circular compact ring
A3 Signal Bars for elevated attention
SEL2 Corner Brackets for persistent selection
X5 balanced contextual expansion without context recession
L0 Flat Fields provisional working default
Z7 Pull-Back Then Dive deep-focus entry
fullscreen specialist-workspace end state
compact topology compass retained
S0 Geometric Control provisional zoom working default
Quiet Graphite current Conversation Workspace visual baseline
```

Semantic zoom S1-S8 remains preserved and deferred, not rejected.

## Conversation Workspace visual disposition

The independent dual-design round is complete and preserved in Research 081.

The project owner selected:

```text
Quiet Graphite
    current baseline
```

Currently rendered alternatives are rejected:

```text
Deep Navy
Warm Slate
Monochrome Signal
Violet Ink
Editorial Dark
Claude Technical Manuscript
Claude Studio Console
Claude Hybrid
```

Future visual exploration may introduce genuinely new candidates. Rejected systems should not be silently revived as active options.

## Current Slice 02Q: Conversation Scope + Work-Unit Anchor

Checkpoint:

```text
246
```

Research/browser:

```text
docs/research/082_conversation_scope_work_unit_anchor_and_quiet_graphite_baseline.md
http://localhost:5173/design-lab/conversation-workspace-work-unit-anchor.html
```

Initial implementation target:

```text
56e32bc0a682bdb0a5bf54d5d9db7b3b987fdb7e
```

The current human requirement is:

```text
PROJECT-GENERAL CONVERSATION
    legitimate project-level conversation
    no single box owns it

WORK-UNIT-SCOPED CONVERSATION
    belongs to one work unit
    should remain immediately recognizable as belonging to that box

PER-TURN CONTEXT
    temporary referenced project objects
    separate from conversation home
```

The new browser tests three orthogonal dimensions:

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

The project grid is deliberately absent. Work-unit identity is represented as a compact canonical artifact instead of restoring the map.

## Current conceptual hypothesis

```text
conversation home
    !=
per-turn context
```

Possible interface-level representation:

```text
Conversation.home_scope
    PROJECT_GENERAL
    WORK_UNIT

Conversation.home_object_id
    null or one work-unit id

Message.contextual_object_ids
    zero or more project objects
```

This is not a frozen persistence schema. Multi-home, re-homing, non-work-unit anchors and conversation branching remain open.

## Current collaboration gate

Message 009 asks Claude to inspect and broaden the new question.

```text
next actor: Claude
expected output: MC-0004 Message 010
mode: COMPARATIVE_ONLY / DIVERGENT_IDEATION
```

Claude is asked to challenge and expand:

```text
conversation-home mental model
work-unit identity in the thread rail
project-general conversation identity
conversation + opened-box composition
X5 -> work-unit conversation entry / return
edge cases such as re-homing and multi-object discussion
```

Claude may inspect the current browser. Blindness is no longer required because both independent visual proposals are already frozen.

## Production boundary

Production `/cockpit` remains untouched.

Still unfrozen includes final Conversation Workspace composition, conversation persistence/session model, home/anchor schema, multi-object semantics, search/archive/fork lifecycle, message-to-project linking semantics, conversation URL state, semantic zoom, large-project virtualization, deep-focus return choreography, compass semantics, specialist-workspace composition and final production visual system.