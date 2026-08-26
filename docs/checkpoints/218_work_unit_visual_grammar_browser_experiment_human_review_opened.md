# Checkpoint 218: Work-Unit Visual-Grammar Browser Experiment, Human Review Opened

**Date:** 2026-08-26  
**Status:** Current product-design checkpoint  
**Checkpoint class:** CONTINUITY / PRODUCT_DESIGN / HUMAN_REVIEW  
**Project stage:** V1 next-generation Project Cockpit browser-rendered design exploration  
**Scope:** Records implementation of the first W1-W4 work-unit category/silhouette grammar comparison under the provisionally settled G4 world and H4 interaction-lighting controls, and opens direct browser human review.  
**Authority:** Current Phase-C product-design routing/evidence boundary only. Specification 008 remains the promoted Cockpit interaction architecture.  
**Interaction environment:** ChatGPT  
**Project / workspace:** Autonomous Data Science System  
**Interaction session:** chatgpt-08  
**Conversation title:** 08 - Project Cockpit Design Exploration  
**Primary collaborator:** ChatGPT

## 1. Prior boundary

Checkpoint 217 closed generic rest/hover lighting as the active design question after final human approval of:

```text
H4 resting in-box illumination
H4 outward left-side resting spill
H4 hover-entry timing
H4 hover-release timing
```

No additional generic lighting-only experiment was justified. Later selected/focused/runtime/blocked/approval states remain separate future semantic slices.

The next active question became category/silhouette visual grammar under Research 046.

## 2. Browser experiment implemented

New isolated design-lab surface:

```text
frontend/design-lab/work-unit-grammar.html
frontend/design-lab/work-unit-grammar.css
frontend/design-lab/work-unit-grammar.js
```

Expected local URL:

```text
http://localhost:5173/design-lab/work-unit-grammar.html
```

No production `/cockpit` file was changed.

No new frontend dependency was introduced.

## 3. Held control variables

The comparison deliberately retains the current visual direction rather than redesigning unrelated layers:

```text
G4-style dark world substrate
major/minor technical grid
restrained ambient drift
travelling ambient grid currents
major-grid intersection glints
accepted H4 resting illumination
accepted H4 outward resting spill
accepted H4 hover halo
pointer-following hotspot
hover world illumination
connector emphasis
one-time perimeter sweep
accepted fast-entry / slower-release timing
```

The ambient behavior is decorative/atmospheric and remains lower-salience than semantic interaction response.

## 4. Comparison views

The browser experiment provides two switchable views.

### Category strip

```text
same neutral comparison context
five representative work-unit categories
focus on category recognition and visual grammar
```

### Project scene

```text
same representative churn-project content
connectors visible
G4 world visible
H4 hover behavior visible
focus on whether category grammar survives realistic composition
```

The view switch is part of the design lab only and is not a proposed production feature.

## 5. Representative fixture categories

```text
Question / Blocker
Investigation
Validation / Analysis
Model Work
Evaluation
```

These are visual-fixture categories only. They do not freeze the future production taxonomy.

## 6. W1-W4 variants

### W1 Unified Precision Frame

```text
stable rectangular frame
small category glyph
left/accent signature rail
lowest structural differentiation
```

Purpose: establish the minimum-complexity control.

### W2 Edge-Signature Grammar

```text
stable body geometry
category-specific edge rail / top rail / split rail / bottom rail / terminal rail
```

Purpose: test whether frame rhythm can add category recognition without changing the outer body substantially.

### W3 Structural Silhouette Family

```text
shared typography, material and dimensions
stronger category-specific corner cuts / stepped edges / silhouette changes
```

Purpose: test whether more pre-attentive category recognition earns the stronger geometry.

### W4 Hybrid Semantic Instrument

```text
mostly consistent instrument body
subtle category-specific silhouette cue
semantic glyph
category-specific frame signature
```

Purpose: test whether several restrained cues combine into the strongest professional treatment.

## 7. Important implementation discipline

The experiment continues to preserve:

```text
category
    != project disposition
    != runtime state
    != methodological importance
```

The visual categories should therefore not be interpreted as active/completed/blocked/running semantics.

Those axes remain for later dedicated treatment.

## 8. Review controls

The design lab exposes:

```text
Category strip / Project scene switch
Reduced motion toggle
```

Reduced motion removes ambient current/glint animation and the H4 perimeter sweep while preserving static category and hover meaning.

## 9. Current evidence status

```text
RESEARCH BRIEF
    complete for first round

BROWSER IMPLEMENTATION
    complete for first round

HUMAN BROWSER REVIEW
    OPEN

PRODUCTION PROMOTION
    not authorized
```

The implementation has not yet been judged visually by the project owner. No W1-W4 preference should be inferred before that review.

## 10. Human review questions

```text
Can work-unit kinds be distinguished before reading every title?
Which variant simply looks best?
Which feels most premium and professional?
Does any silhouette treatment look arbitrary or gimmicky?
Which still feels like one coherent ADS product language?
Does stronger silhouette differentiation improve understanding enough to justify its complexity?
Does H4 lighting still look correct across the category treatments?
Is the category strip useful for isolating category identity?
Does the same judgment hold in the realistic project scene?
Would a hybrid between variants be better than selecting one literally?
```

## 11. Production boundary

Still not authorized:

```text
production Cockpit component replacement
production work-unit taxonomy
final semantic palette
production graph/canvas adoption
production motion-library adoption
final status/runtime visual system
```

The current files remain throwaway/rewrite-friendly design evidence.

## 12. Promotion audit

```text
NEW CANONICAL PRINCIPLE / DECISION
    none

NEW ACCEPTED SPECIFICATION
    none

NEW BROWSER DESIGN EVIDENCE
    yes: W1-W4 implementation

CURRENT ROUTING / STATE UPDATE
    warranted

PRODUCTION PROMOTION
    no
```

## 13. Exact continuation

```text
1. use v1-cockpit-design-exploration and Checkpoint 218
2. pull the latest branch locally
3. keep the existing Vite dev server running
4. open http://localhost:5173/design-lab/work-unit-grammar.html
5. compare W1-W4 first in Category strip view
6. compare W1-W4 again in Project scene view
7. hover representative nodes to ensure the accepted H4 treatment still works visually
8. use Reduced motion only as a secondary accessibility check
9. report prefer/reject/combine/refine judgment
10. do not promote anything to production yet
11. keep source-vault deployment paused until explicitly resumed
```
