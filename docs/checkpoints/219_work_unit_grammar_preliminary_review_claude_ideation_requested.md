# Checkpoint 219: Work-Unit Grammar Preliminary Review, Claude Ideation Requested

**Date:** 2026-08-26  
**Status:** Current product-design checkpoint  
**Checkpoint class:** CONTINUITY / PRODUCT_DESIGN / COLLABORATION  
**Project stage:** V1 next-generation Project Cockpit browser-rendered design exploration  
**Scope:** Records the human project's positive preliminary review of the first W1-W4 work-unit category/silhouette experiment, correction of the Project Scene view-switching defect, and a new bounded Claude divergent-ideation request before the work-unit grammar is selected or refined.  
**Authority:** Current Phase-C routing/evidence boundary only. Specification 008 remains the promoted Cockpit interaction architecture.  
**Interaction environment:** ChatGPT  
**Project / workspace:** Autonomous Data Science System  
**Interaction session:** chatgpt-08  
**Conversation title:** 08 - Project Cockpit Design Exploration  
**Primary collaborator:** ChatGPT

## 1. Preliminary human disposition

The project owner reviewed the first W1-W4 work-unit grammar experiment in the browser and gave a strongly positive preliminary reaction to the quality of the implementation.

No W1-W4 selection is frozen yet.

The project owner explicitly observed that the current four variants likely cover only part of the plausible visual-design space and requested additional ideas and inspiration from Claude before deciding whether to select, combine or expand the current directions.

This creates a legitimate divergent-design gate rather than a routine second-opinion ceremony.

## 2. Browser defect found and corrected

When switching to `Project scene`, both the category-strip nodes and project-scene nodes were visible simultaneously, producing the overlap seen in the human browser review.

Cause:

```text
view switching relied on the HTML hidden attribute
+
author CSS continued to provide display/layout rules for the hidden panel
->
the inactive panel remained rendered in the browser composition
```

Correction:

```text
frontend/design-lab/work-unit-grammar.js
```

The view controller now applies both:

```text
panel.hidden
+
explicit inline display suppression for the inactive panel
```

and initializes the correct panel state on page load.

The corrected exact browser-experiment target for the Claude ideation request is:

```text
88a507d42744917be1e84b29177dd0465f24cd82
```

This is a bounded design-lab defect correction only. No production Cockpit file changed.

## 3. Current W1-W4 status

The existing candidates remain useful evidence rather than a closed menu:

```text
W1  Unified Precision Frame
W2  Edge-Signature Grammar
W3  Structural Silhouette Family
W4  Hybrid Semantic Instrument
```

The human project owner has not selected one.

The active question has widened slightly from:

```text
Which of W1-W4 is best?
```

to:

```text
What professional, distinctive and learnable work-unit category grammar should ADS test before converging?
```

This remains bounded to category identity. Project disposition, runtime state, importance, connector semantics and semantic zoom remain separate design axes.

## 4. Claude request

The collaboration request is preserved as:

```text
docs/model_collaboration/threads/MC-0004/messages/003_chatgpt_work_unit_grammar_divergent_ideation_request.md
```

Claude is asked to:

```text
audit which visual-design dimensions W1-W4 underexplore
propose materially different concept families
identify promising combinations
use external design inspiration where useful
recommend a small next browser round
state risks and reversal evidence
```

This pass is explicitly classified:

```text
COMPARATIVE_ONLY / DIVERGENT_IDEATION
```

It is not a new blind-independent phase. Claude may inspect the complete current candidate state.

Claude's write boundary remains:

```text
docs/model_collaboration/threads/MC-0004/messages/**
```

ChatGPT retains target-state write ownership.

## 5. Preserved controls

The following remain unchanged:

```text
G4 Adaptive Hybrid world                 provisionally settled
H4 generic rest/hover interaction light  sufficiently settled
dark mode                                current design baseline
decorative polish                        legitimate when semantically non-misleading
production /cockpit                      untouched
source-vault deployment                  paused
```

## 6. Promotion audit

No new visual grammar is mature enough for canonical or specification promotion.

The collaboration-routing state does need updating because the next expected actor changes from human review to a bounded Claude contribution.

The existing Research 046 experiment remains the governing browser-design protocol for this slice. Message 003 adds the temporary divergent-ideation request rather than replacing that research.

## 7. Exact continuation

```text
1. use v1-cockpit-design-exploration
2. preserve G4 and H4 as controls
3. preserve W1-W4 as current candidates, not a closed menu
4. Claude reads Message 003 and reviews exact target 88a507d42744917be1e84b29177dd0465f24cd82
5. Claude writes only a new MC-0004 numbered message with divergent work-unit grammar ideas
6. ChatGPT inspects and synthesizes Claude's proposal against Research 046 and the existing browser evidence
7. build only the strongest additional/combined browser variants that appear worth testing
8. return to human visual comparison before selecting the work-unit category grammar
9. keep production Cockpit untouched
```
