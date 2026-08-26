# Research 046: Work-Unit Category and Silhouette Visual-Grammar Experiment

**Date:** 2026-08-26  
**Status:** Active Phase-C product-design research  
**Scope:** Opens the next bounded Project Cockpit browser-design slice after H4 interaction lighting was judged sufficiently settled. Tests how different kinds of meaningful project work should become visually distinguishable without collapsing category, project disposition, runtime state and importance into one overloaded visual channel.  
**Authority:** Research/design protocol only. Specification 008 remains the promoted V1 Cockpit interaction architecture. No production visual system is promoted here.  
**Interaction environment:** ChatGPT  
**Project / workspace:** Autonomous Data Science System  
**Interaction session:** chatgpt-08  
**Conversation title:** 08 - Project Cockpit Design Exploration  
**Primary collaborator:** ChatGPT  
**Companion collaboration thread:** MC-0004

---

## 1. Trigger

The grid/world direction is provisionally settled around G4 Adaptive Hybrid and the work-unit rest/hover interaction-lighting slice is now sufficiently settled around H4 Integrated Response.

The final H4 review established:

```text
accepted clean in-box resting illumination
accepted narrow asymmetric outward resting spill
rejected broad circular resting halo
accepted immediate hover entry
accepted smoother hover release
```

Further generic lighting-only tuning would now have low expected value. Lighting may be revisited later when selected/focused, runtime, blocked or approval states are tested, but those are distinct semantic-state questions.

The next legitimate design problem is therefore deeper work-unit visual grammar.

---

## 2. Why this question matters

Research 037 and Research 038 both identified the same structural weakness in the current Cockpit prototype:

```text
most meaningful work units still share one generic rounded-card grammar
```

Meaning is therefore carried too heavily by:

```text
text
icon
color
status wording
```

Foundation 021 explicitly argues that Questions, Findings, Decisions, Runs and other meaningful project objects should not all collapse into generic cards with different headings.

Specification 008 also defines Cockpit work units as user-relevant project work rather than raw storage primitives. The visual grammar should therefore help the user recognize what kind of work a unit represents while preserving one coherent Cockpit language.

---

## 3. Critical separation: category is not status

The next experiment must preserve the multi-axis distinction already developed in Research 037/038:

```text
WHAT IS THIS?
    category / work-unit kind

WHAT IS ITS PROJECT DISPOSITION?
    active / recommended / deferred / completed / blocked / future

WHAT IS HAPPENING NOW?
    idle / queued / running / waiting / failed / waiting for human

HOW IMPORTANT IS IT NOW?
    required / recommended / relevant / lower priority
```

This slice tests primarily the first question:

```text
WHAT IS THIS?
```

It should not try to solve the complete multi-axis state system at the same time.

A Question should remain recognizably a Question whether it is active, blocked, completed or deferred. A model-related work unit should remain recognizably model work whether it is idle or running.

---

## 4. Governing visual constraints

The experiment should preserve:

```text
G4 world substrate
H4 accepted rest/hover interaction lighting
current dark-first sequencing
representative project content
professional long-session calm
```

The experiment should avoid:

```text
arbitrary novelty shapes with no reusable grammar
large shape changes that destroy scanning/alignment
using color as the only category signal
using animation as the only category signal
encoding project status into category shape
turning every category into an unrelated mini-design
```

Decorative polish remains legitimate. A detail may exist because it makes the Cockpit look better, provided decorative treatment does not masquerade as project/runtime meaning.

---

## 5. Candidate visual channels

The broad research already identified several channels worth testing:

```text
silhouette / edge geometry
small semantic glyph
surface material
left/top signature band
status marker
relation-port treatment
```

For this slice, status markers should remain controlled so they do not contaminate the category comparison.

The strongest category channels to isolate first are:

```text
silhouette / corner geometry
semantic edge/signature treatment
glyph placement
surface/frame structure
```

Relation-port treatment may be previewed lightly but final connector semantics belong to a later slice.

---

## 6. Representative category set

The first browser experiment should not attempt to design every future ADS work-unit kind.

Use a small heterogeneous set that exercises meaningfully different project roles:

```text
QUESTION / BLOCKER
    unresolved definition or project question

INVESTIGATION
    evidence-seeking analytical investigation

VALIDATION / ANALYSIS WORK
    designed analytical procedure or validation work

MODEL WORK
    baseline or alternative model development

EVALUATION / DECISION-RELEVANT WORK
    comparison, evaluation or decision-bearing downstream work
```

The labels are design-fixture categories, not a frozen production taxonomy.

---

## 7. First-round browser variants

The goal is to compare materially different degrees of category expression while holding content, G4 and H4 constant.

### W1 Unified Precision Frame

One stable rectangular work-unit silhouette for every category.

Category identity comes from:

```text
small semantic glyph
restrained accent/signature band
minor internal header treatment
```

Purpose:

```text
establish the lowest-complexity professional baseline
```

Risk:

```text
may remain too close to the current generic-card problem
```

### W2 Edge-Signature Grammar

Keep a highly consistent body and dimensions, but give categories distinct restrained edge geometry.

Candidate mechanisms include:

```text
notched accent edge
short top rail
inset corner marker
split side rail
small framed tab
```

Purpose:

```text
make category visible from silhouette/edge rhythm without destroying alignment
```

Risk:

```text
may feel like superficial decoration if category recognition does not improve
```

### W3 Structural Silhouette Family

Give categories more visibly distinct but still related outer geometries.

The family should share:

```text
common dimensions
common typography
common internal spacing
common H4 lighting behavior
common border/material language
```

while varying a small number of structural features such as corner cuts, tabs, framed edges or bracket-like features.

Purpose:

```text
test whether stronger pre-attentive category recognition is worth a more expressive shape system
```

Risk:

```text
can become diagrammatic, gimmicky or visually noisy
```

### W4 Hybrid Semantic Instrument

Combine the strongest restrained mechanisms:

```text
mostly consistent body family
+
small category-specific silhouette cue
+
semantic glyph
+
category signature edge/frame
+
accepted H4 lighting
```

Purpose:

```text
test whether several quiet category cues together produce the strongest premium professional result
```

Risk:

```text
too many individually subtle cues may still create unnecessary visual complexity
```

---

## 8. Comparison scenes

The browser experiment should expose two views.

### Category comparison strip

Show the same neutral/resting project disposition across all representative categories.

Purpose:

```text
isolate category recognition from project status
```

### Small realistic project scene

Reuse the current churn-project fixture so the grammar can be judged inside actual Cockpit composition.

Representative content:

```text
Prediction moment
Production missingness
Chronological validation
Baseline logistic model
Evaluation
```

Purpose:

```text
check whether the visual grammar still reads well among connectors, G4 ambient motion and H4 lighting
```

---

## 9. Human evaluation questions

The review should answer:

```text
Can I distinguish work-unit kinds before reading every title?
Does the category system still feel like one coherent product language?
Which variant looks best overall?
Which feels most premium and professional?
Does any shape treatment look arbitrary or gimmicky?
Does stronger silhouette differentiation improve understanding enough to justify the added visual complexity?
Does H4 lighting still look correct across all category treatments?
Do the work units remain comfortable at realistic information density?
Would a combination of two variants be better than either literally?
```

Category recognition should not be judged only by memorizing the experiment legend. The visual language should become learnable and reinforce meaning, but exact universal recognition from shape alone is not required.

---

## 10. What this slice does not freeze

```text
final production work-unit taxonomy
final semantic color palette
project disposition styling
runtime / waiting / blocked / approval styling
selected/focused persistent treatment
connector semantics
semantic zoom representations
node dimensions at all zoom levels
final typography
production graph/canvas implementation
production motion library
```

Those remain later design questions.

---

## 11. Implementation boundary

The next implementation should remain isolated under:

```text
frontend/design-lab/**
```

Expected new review surface:

```text
frontend/design-lab/work-unit-grammar.html
frontend/design-lab/work-unit-grammar.css
frontend/design-lab/work-unit-grammar.js
```

No production `/cockpit` component should change.

No new frontend dependency is justified merely to test this visual grammar.

---

## 12. Immediate next action

```text
1. preserve G4 and H4 as controls
2. build W1-W4 browser-rendered work-unit grammar variants
3. keep category separate from status/runtime/importance
4. expose a neutral category strip and one realistic project scene
5. let the project owner compare directly in the browser
6. record preferred/rejected/combine/refine disposition
7. refine once if useful
8. then decide whether multi-axis status treatment or connector visual language is the higher-value next slice
```
