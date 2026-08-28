# Current State

**Checkpoint:** 248  
**Date:** 2026-08-28  
**Active development branch:** `v1-cockpit-design-exploration`  
**Active PR:** none  
**Exploration branch base:** `v1-frontend-spike` at Checkpoint 205 head `2480109fadeee1e480ef03b82e335aacdf9adf91`  
**Promoted V1 integration branch:** `v1-frontend-spike` at `ed5b60bdc882bed0799ce55228ce8187f9c55aa1`  
**Development stage:** MC-0004 Phase C browser-rendered Project Cockpit design evaluation. The work-unit depth ladder and current Conversation Workspace look remain held. Checkpoint 247's X5-to-full-chat entry-only framing was too narrow. The active boundary is now conversation access from every major work state and full-focus versus simultaneous work+conversation composition.  
**Latest specification:** Specification 024 remains accepted. Specification 008 remains the promoted V1 Project Cockpit interaction architecture.  
**Latest scientific experiment:** Specification 022 remains `INCOMPLETE / EXECUTION INTEGRITY FAILED`; no scientific comparison may be inferred from that run.

## Active interaction context

```text
Interaction environment  ChatGPT
Project / workspace      Autonomous Data Science System
Interaction session      chatgpt-08
Conversation title       08 - Project Cockpit Design Exploration
Primary collaborator     ChatGPT
```

Repository artifacts remain authoritative across chats and models.

---

# Current active boundary

Primary route:

```text
docs/checkpoints/248_conversation_access_and_coexistence_architecture_review_opened.md
docs/research/086_conversation_workspace_orthogonal_access_and_coexistence_architecture.md
frontend/design-lab/conversation-workspace-access-coexistence.html
frontend/design-lab/conversation-workspace-access-coexistence.css
frontend/design-lab/conversation-workspace-access-coexistence.js
```

Current local URL:

```text
http://localhost:5173/design-lab/conversation-workspace-access-coexistence.html
```

Production `/cockpit` remains untouched.

---

# Held Cockpit controls and accepted / working Phase-C results

```text
G4 Adaptive Hybrid world
Dark-mode baseline
H4 hover/world response
Reduced in-box resting light
scientific category marker grammar
E5 Hue + Tag relation-class carrier
P7 Neutral Tag + Tone disposition
editable current-process focus set
conditional runtime semantics
one switchable operational carrier
T7 Soft Shade runtime tag
BLOCKER -> BLOCKS -> BLOCKED cause/effect model
BLOCKED sharper compact ring
FAIL smoother circular compact ring
A3 Signal Bars for HIGH attention
SEL2 Corner Brackets for persistent selection
X5 balanced contextual expansion without context recession
L0 Flat Fields provisional working internal-layout default
Z7 Pull-Back Then Dive specialist-workspace entry
fullscreen specialist-workspace end state
compact topology compass retained
S0 Geometric Control provisional zoom working default
Quiet Graphite Conversation Workspace baseline
Boxes/Text user-switchable conversation rail
A6 Adaptive Anchor opened-box composition
A6 resting state without redundant floating home-object card
```

Important targets:

```text
directionality                07d573b6569b9f09a3b7e00936f3eadecee721b3
relation class E5             497e81f06ba1f9901511449237d1bb9f96b2d108
P7 disposition                fac1db37af4225927d6c799e37418a3ad9c42c13
editable focus                da115b74de526fca05ed6f468bef39bdb801355c
T7 Soft Shade                 08534f94c2f272f969159087de2797a23e36b330
switchable runtime            fb847bd65ff6e5e4203a89ee2d4f74b7187c8359
BLOCKED/status carrier        88fd3c3cfe7a1eff4664afde06341b7b654c97f4
A3 attention priority         767c66f76974d3c0a851de0dfa17c502817a4b12
SEL2 selection                e7304fe834d86166d843fda7e1df0f4ddb1f793a
X5 contextual expansion       94bc1100b7388cc56497cafc03051ce326424a80
Z7 specialist deep focus      04616a52df5cceff6c59223bbd6f07448d027510
semantic zoom browser         65ac02326a75b1c9f056676819d2d1b7b23b74c5
A6 no-floating-box refinement 606e027f281b35c2dfc93d059a1681df23bc2b73
```

---

# Conversation architecture

The corrected architecture is factorized:

```text
WORK CONTEXT
    Project Grid
        neutral
        selected box
        X5 expanded

    Deep Dive specialist workspace

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

Required behavior:

```text
Global Conversations action
    available from every Grid state

Open conversation from work unit/X5
    targets corresponding work-unit conversation

Deep Dive
    has global conversation access
    has direct current-work-unit chat access

Full chat focus
    valid presentation mode
    preserves underlying work context

Co-present chat
    valid presentation mode
    Grid or Deep Dive remains visible/usable

Switch conversation thread
    does not mutate underlying work context

Close/collapse conversation
    restores the same Grid selection/X5/Deep Dive state
```

Research 079's CV1/CV2/CV5/CV6 mechanisms are recovered as co-presence evidence. They were not rejected by the later Conversation Workspace visual decisions.

---

# Current browser factorization

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

P3 is the initial browser default only. No co-present composition has been selected.

Checkpoint 247's E0-E4 remain preserved only as potential full-chat-focus motion evidence. No transition winner was selected.

---

# Semantic zoom disposition

```text
S0 Geometric Control
    provisional working default

S1-S8
    preserved for later
    not rejected

semantic zoom
    DEFERRED
```

---

# Repository preservation health

```text
repository preservation architecture   SOUND
structural overhaul                     NOT WARRANTED
new knowledge subsystem                 NOT JUSTIFIED
checkpoint granularity                  HARDENED
checkpoint validation closure           HARDENED
active-branch routing validation        HARDENED
Claude coordination branch routing      EXPLICIT
```

Historical research/checkpoints remain the durable evidence layer. Current routing documents are intentionally compact navigation surfaces.

---

# Source Universe deployment

```text
source-vault bootstrap
    PAUSED
    not cancelled
    not rejected
    not superseded
```

Course 2 remains gated.
