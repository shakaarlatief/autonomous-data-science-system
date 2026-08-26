# Model Collaboration Review Inbox

**Date:** 2026-08-26  
**Status:** Current human-readable routing view  
**Authority:** Convenience index only. Per-thread `STATE.json`, `THREAD.md`, frozen requests, exact Git refs, and resolution records remain authoritative.  
**Purpose:** Let a returning collaborator discover pending review/catch-up obligations without relying on private chat memory.

## Current pending obligation

```text
thread                 MC-0004
phase                  PHASE_C_BROWSER_DESIGN_EVALUATION
kind                   COMPARATIVE_ONLY / DIVERGENT_IDEATION
requested collaborator Claude
active branch          v1-cockpit-design-exploration
exact target           88a507d42744917be1e84b29177dd0465f24cd82
request                 docs/model_collaboration/threads/MC-0004/messages/003_chatgpt_work_unit_grammar_divergent_ideation_request.md
expected output         docs/model_collaboration/threads/MC-0004/messages/004_claude_work_unit_grammar_divergent_ideation.md
priority                ordinary required before work-unit grammar convergence
```

The human project owner positively reviewed the first W1-W4 work-unit grammar browser experiment but explicitly requested broader Claude ideas and inspiration before selecting or combining the current candidates.

This is not a blind review. Claude may inspect all current candidate material.

Important human clarification:

```text
NO artificial candidate-count cap
NO requirement to narrow to 3-5 directions
preserve all genuinely distinct and worthwhile candidates
browser testing may use multiple batches if useful
batching != rejection
narrow only for redundancy, domination, boundary violation, or weak value
```

Claude should write only under:

```text
docs/model_collaboration/threads/MC-0004/messages/**
```

ChatGPT retains target-state write ownership.

## Current design context

```text
G4 world                       provisionally settled
H4 generic rest/hover lighting sufficiently settled
active slice                   work-unit category / silhouette grammar
current candidates             W1-W4, not a closed menu
current checkpoint             219
next expected actor            Claude
```

The Project Scene view-switching defect found during preliminary human review was corrected before the exact target above was frozen.

## Recently completed collaboration evidence

```text
MC-0004 Phase A
    Claude proposal commit  cd2e12f2c79ee3b2f205457c5940eb2022b4631a
    classification          BLIND_TO_CANDIDATE

MC-0004 Phase B
    Claude review commit    d94d696214a41d2a3904aa9ce2a42bdab5f2f3ce
    classification          COMPARATIVE_ONLY

MC-0004 Phase C
    G4 selected and provisionally settled
    H4 selected and generic rest/hover lighting sufficiently settled
    first W1-W4 work-unit grammar experiment implemented and preliminarily reviewed
```

## Manual trigger

Because this work lives on an active unpromoted branch, the manual Claude trigger should name that branch explicitly:

```text
Check v1-cockpit-design-exploration and docs/model_collaboration/REVIEW_INBOX.md, then proceed with the pending MC-0004 Claude task.
```

The repository carries the detailed contract. No transcript relay is required.
