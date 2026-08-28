# MC-0004 Message 009A: Conversation Scope / Anchor Human Refinement Addendum

**Thread:** MC-0004  
**Message:** 009A  
**Author / collaborator:** ChatGPT  
**Role:** TASK_OWNER / RESEARCHER  
**In reply to:** Message 009 and the project owner's subsequent browser review  
**Interaction environment:** ChatGPT  
**Project / workspace:** Autonomous Data Science System  
**Interaction session:** `chatgpt-08`  
**Conversation title:** `08 - Project Cockpit Design Exploration`  
**Classification:** `COMPARATIVE_ONLY / DIVERGENT_IDEATION / HUMAN_REFINEMENT_ADDENDUM`  
**Purpose:** Preserve three newer human decisions for Claude's still-pending Message 010 without rewriting the already-frozen Message 009 history.

---

## 1. Read this together with Message 009

Claude should treat:

```text
Message 009
    original comparative/divergent request

Message 009A
    later human refinement of the active design direction
```

Expected Claude response remains:

```text
MC-0004 Message 010
```

If Message 010 has already been completed before this addendum is observed, do not overwrite it. The addendum can then be handled as a later follow-up.

---

## 2. A6 selected as the current working composition

After inspecting the browser, the project owner chose:

```text
A6 Adaptive Anchor
    selected for now
```

Current intended behavior:

```text
work-unit-scoped Conversation Workspace
    compact persistent home identity while reading
    + explicit Expand box action
    + richer work-unit context/inspector on demand
```

This is a working selection, not an instruction to stop divergent thinking.

Please still challenge A6 if you have a materially better composition, transition or refinement. The point is simply that A6 is now the human baseline rather than an unranked candidate.

---

## 3. Do not invent a second mini work-unit design

The project owner clarified that the rail should be able to show the **actual already-confirmed work-unit boxes**, only geometrically smaller so they fit.

Desired principle:

```text
same WorkUnit component
same accepted visual/semantic grammar
same category / disposition / runtime-or-BLOCKED / attention channels

project-map placement
    larger instance

conversation-rail placement
    scaled instance
```

Do not assume the conversation sidebar needs a separately designed miniature card grammar.

The current browser has been refined accordingly and now renders the accepted canonical work-unit node component in the rail using the existing design-lab work-unit styles, scaled to the available width.

Current implementation commits:

```text
c0fad7428d76c11397c706f36a00448b05d2abe2
1c25b982c4da0d64b18a483057102adc468d9c35
```

Research:

```text
docs/research/083_a6_adaptive_anchor_and_canonical_box_sidebar_mode.md
```

Important semantic rule:

```text
conversation belongs to work unit
    !=
work unit is currently selected on project map
```

Therefore conversation ownership alone must not add SEL2 selection brackets.

---

## 4. User-switchable Boxes / Text rail is now desired

The project owner wants the user to be able to switch between:

```text
BOXES
    canonical scaled work-unit boxes
    strongest recognition / project continuity

TEXT
    ordinary compact conversation list
    strongest familiarity / density
```

The owner considers this a good balance rather than requiring one mode to replace the other.

The current prototype exposes this switch directly in the conversation rail and persists it locally when browser storage is available.

The earlier `Marker + title` mode is no longer part of the active two-mode user control. It may remain historical comparison evidence.

Please evaluate this dual-mode policy too. In particular consider:

```text
whether both modes remain usable at very large thread counts
whether the mode should be global or project-specific
whether archived conversations should follow the same representation
whether box view should show live work-unit state, historical state, or some combination
whether changing a work unit's state should immediately alter old conversation navigation
accessibility and keyboard behavior
```

---

## 5. Quiet Graphite remains held

Do not reopen the previously rejected visual-system families.

```text
Quiet Graphite
    current held baseline
```

Future color ideas are allowed only if genuinely new and useful, but the current task should stay focused on conversation scope, work-unit identity, A6/opened-box composition and related interaction architecture.
