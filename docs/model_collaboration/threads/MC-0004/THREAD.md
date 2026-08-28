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
    Research 083
    ChatGPT Message 009A human refinement addendum
    Claude Message 010 completed at 8c2c95aec8bf9d53e17500f4a38f9311d19a1e8b
    Research 084 synthesis browser opened
    project owner reaffirmed prior design and rejected B1-B4 as irrelevant to chosen look
    redundant A6 floating work-unit card removed

Phase C Conversation Workspace entry / return transition
    Checkpoint 247
    Research 085
    transition browser target 43ee0ae0ffc63eba6e99a42e9157568c53cc8806
    no transition selected
    later determined to be too narrowly framed around X5 -> full-chat replacement

Phase C Conversation access + coexistence
    Checkpoint 248
    Research 086
    conversation access/coexistence browser target db31970d6885ce785609f9c3300f22123130d821
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
Z7 Pull-Back Then Dive specialist-workspace entry
fullscreen specialist-workspace end state
compact topology compass retained
S0 Geometric Control provisional zoom working default
Quiet Graphite current Conversation Workspace visual baseline
A6 Adaptive Anchor current Conversation Workspace opened-box composition
canonical WorkUnit box / Text user-switchable conversation rail
A6 resting state without redundant floating home-object card
```

Semantic zoom S1-S8 remains preserved and deferred, not rejected.

## Conversation Workspace visual disposition

The independent dual-design round is complete and preserved in Research 081.

The project owner selected:

```text
Quiet Graphite
    current baseline
```

Currently rendered alternatives remain rejected:

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

## Conversation Scope + Work-Unit Anchor result

Held product model:

```text
PROJECT-GENERAL CONVERSATION
    legitimate project-level conversation
    no single box owns it

WORK-UNIT-SCOPED CONVERSATION
    belongs to one work unit
    remains immediately recognizable as belonging to that box

PER-TURN CONTEXT
    separate temporary project context
```

Held presentation:

```text
conversation rail
    user-switchable Boxes / Text

Boxes mode
    canonical work-unit visual identity

opened-box composition
    A6 Adaptive Anchor

A6 rest-state identity
    active box in sidebar
    title + WORK UNIT scope in header
    Expand box action
    no extra floating box in transcript
```

Conversation ownership does not imply project-map selection, so SEL2 is not added merely because a chat belongs to a work unit.

Exact A6 floating-box removal:

```text
606e027f281b35c2dfc93d059a1681df23bc2b73
```

## Claude Message 010 disposition

Claude's code-grounded findings and later ontology/density ideas remain preserved. Its B1-B4 additional composition treatments were explicitly judged irrelevant to the already chosen Conversation Workspace look and remain historical evidence rather than active alternatives.

## Checkpoint 247 disposition

Research 085 and E0-E4 remain useful **full-chat-focus transition choreography** evidence only.

```text
E0 Direct Replace
E1 Anchored Grow
E2 World Recede
E3 Pull-Back Then Dive
E4 X5 Aperture
```

No winner was selected because the project owner clarified that the architecture must first support conversation across every work state and simultaneous work+chat compositions.

## Current Slice: Conversation access + coexistence

Checkpoint:

```text
248
```

Research:

```text
docs/research/086_conversation_workspace_orthogonal_access_and_coexistence_architecture.md
```

Browser:

```text
http://localhost:5173/design-lab/conversation-workspace-access-coexistence.html
```

Factorized product model:

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

Required access paths:

```text
Global Conversations from any Grid state
Open this conversation from work unit/X5
Global Conversations from Deep Dive
Chat about this work unit from Deep Dive
thread switching without mutating work context
close/collapse chat restores underlying work context
```

Research 079 is recovered as co-presence evidence:

```text
CV0 Focus Workspace        -> full chat focus baseline
CV1 Right Dock             -> work-primary co-present candidate
CV2 Split Workbench        -> balanced co-present candidate
CV5 Focus + Context Rail   -> chat-dominant co-present candidate
CV6 Conversation + Inspector -> focused-context evidence
```

Current browser presentation modes:

```text
P0 Work only / compact chat
P1 Full chat focus
P2 Right dock
P3 Balanced split
P4 Chat dominant + work context
```

P3 is only the initial browser default. No co-present composition is selected.

## Current collaboration gate

```text
next actor: human project owner
mode: conversation access + coexistence browser review
pending Claude obligation: none
```

## Production boundary

Production `/cockpit` remains untouched.

Still unfrozen includes final co-present Conversation Workspace composition, split proportions/resizing, thread-rail behavior under constrained widths, full-chat-focus transition choreography, conversation URL/session state, persistence/lifecycle, pinned context promotion, historical-state semantics, semantic zoom, large-project virtualization, compass semantics, specialist-workspace composition and final production visual system.
