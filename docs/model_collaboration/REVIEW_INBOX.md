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
exact target           03d3997498192544ce92c97c2a49e839b3a95af4
request                 docs/model_collaboration/threads/MC-0004/messages/003_chatgpt_work_unit_grammar_divergent_ideation_request.md
expected output         docs/model_collaboration/threads/MC-0004/messages/004_claude_work_unit_grammar_divergent_ideation.md
priority                ordinary required before work-unit grammar convergence
```

The human project owner positively reviewed the first W1-W4 work-unit grammar browser experiment but explicitly requested broader Claude ideas and inspiration before selecting or combining the current candidates.

This is not a blind review. Claude may inspect all current candidate material.

The exact target above supersedes the earlier pre-lighting-correction target. Before Claude was triggered, human review identified and ChatGPT corrected:

```text
Project Scene view overlap
accidental suppression of accepted H4 in-box resting light
fixed-left resting light despite top/bottom/right category signature bars
```

The corrected browser target now exposes an intentional secondary comparison:

```text
In-box light
    H4 baseline   restored default control
    Reduced       intentional alternative
```

The outward resting spill and H4 hover behavior remain held. Signature-anchored resting light now follows the visible signature edge.

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
H4 in-box baseline             restored as default control
Reduced in-box light           explicit optional comparison
signature-side lighting        corrected
active slice                   work-unit category / silhouette grammar
current candidates             W1-W4, not a closed menu
current checkpoint             220
next expected actor            human verification, then Claude
```

Primary current evidence:

```text
docs/research/046_work_unit_category_and_silhouette_visual_grammar_experiment.md
docs/research/047_work_unit_grammar_h4_control_correction_and_inbox_light_comparison.md
docs/checkpoints/220_work_unit_grammar_h4_control_corrected_claude_ideation_ready.md
```

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
    H4 grammar-control drift corrected before Claude ideation
```

## Manual trigger

After the project owner verifies the corrected browser rendering, use:

```text
Check v1-cockpit-design-exploration and docs/model_collaboration/REVIEW_INBOX.md, then proceed with the pending MC-0004 Claude task.
```

The repository carries the detailed contract. No transcript relay is required.
