# Research 038: MC-0004 Comparative Cockpit Design Synthesis and Mockup Direction Set

**Date:** 2026-08-26  
**Status:** Active product-design synthesis, not an accepted visual specification  
**Scope:** Synthesizes Research 037, Claude's independently frozen MC-0004 Phase-A proposal, and Claude's Phase-B comparative review into a bounded set of evidence-backed mockup directions and unresolved questions.  
**Authority:** Research/design synthesis only. Specification 008 remains the promoted V1 Project Cockpit interaction architecture unless later evidence and normal governance revise it.  
**Primary interaction environment:** ChatGPT  
**Project / workspace:** Autonomous Data Science System  
**Interaction session:** chatgpt-07  
**Conversation title:** 07 - Project Cockpit Design Exploration  
**Companion collaboration thread:** MC-0004

---

# 1. Evidence base

This synthesis is based on three deliberately separated evidence layers:

```text
Research 037
    broad ChatGPT product/interaction/technology research
    external product references
    multiple candidate directions
    intentionally noncommittal on final design

Claude Phase A
    independent design proposal
    frozen before Claude saw Research 037
    BLIND_TO_CANDIDATE
    commit cd2e12f2c79ee3b2f205457c5940eb2022b4631a

Claude Phase B
    comparative review after the independence gate lifted
    COMPARATIVE_ONLY
    commit d94d696214a41d2a3904aa9ce2a42bdab5f2f3ce
```

Claude's Phase-B commit changed only:

```text
docs/model_collaboration/threads/MC-0004/messages/002_claude_comparative_review.md
```

so the declared collaboration write boundary was respected.

The current Cockpit implementation remains the control baseline. No frontend implementation file has been changed during this design-exploration phase.

---

# 2. Strongest independently reinforced findings

The most valuable outcome of MC-0004 is not that two models produced similar aesthetic preferences. It is that two independent passes converged on several concrete structural weaknesses and high-value opportunities.

## 2.1 Current implementation diagnosis

Research 037 and Claude Phase A independently identified essentially the same four implementation-level gaps:

```text
1. mostly shared generic card grammar across different work-unit types
2. fixed / manually-authored connector geometry with weak semantic meaning
3. geometric zoom without a true semantic-zoom information architecture
4. representative fixed pixel positions that do not constitute a scale strategy
```

This convergence is stronger than either proposal alone because the two analyses were produced independently from the same codebase before cross-exposure.

## 2.2 Semantic zoom is the highest-confidence first mockup mechanism

Both sides independently treat semantic zoom as one of the largest remaining quality and scale opportunities.

The strongest candidate representation model remains:

```text
PROJECT SCALE
    stage / topology / branch structure
    compact work-unit identity
    major blocker / approval / active-route information

WORK SCALE
    title
    type
    disposition
    compact key metrics or counts
    primary relations

INSPECTION SCALE
    concise description
    evidence / question counts
    current action
    richer relation labels

FOCUS
    normal full-resolution analytical or conversational workspace
```

The core principle is stable semantic identity. Zoom may change representation density, but it must not silently change the meaning or authority of project state.

## 2.3 Connectors should become a real project-state language

Both independent positions reject decorative edge animation as the goal.

The governing rule for mockups is:

> If a relation is moving, the user should be able to explain what is currently moving in the project.

The mockup vocabulary should test at least:

```text
settled / satisfied relation
active dependency / current flow
unresolved dependency
blocking dependency
candidate / alternative relation
deferred path
execution in progress
failed execution
```

Direction, type and state must remain understandable without animation.

Claude's concrete hypothesis of no more than roughly one to three simultaneously animated connectors in the representative scene is useful because it is falsifiable. It is not accepted as a production limit. It should be tested as a first-round motion-budget hypothesis.

## 2.4 Motion should be scarce, event-driven and calm at rest

The two independent designs converge strongly on:

```text
project changing
    visibly alive

project settled
    visibly calm
```

Persistent motion should require persistent underlying activity.

This means the design should not attempt to look advanced by making the entire grid, every relation or every node continuously shimmer or pulse.

## 2.5 The Conversation Workspace is first-class

The compact Cockpit composer remains useful, but both sides agree that it cannot be the complete conversation experience.

The product must support:

```text
long multi-turn dialogue
visible previous messages
search / navigation / re-entry
continuation of earlier discussion
links between messages and project work
structured project outcomes derived from conversation
```

The strongest shared interaction hypothesis is that full conversation can reuse the same spatial focus / workspace handoff principle already validated for Data, EDA and Missingness.

However, the exact presentation remains open and should be compared through mockups:

```text
docked conversation lens
conversation focus workspace
split analytical + conversation workbench
canvas-anchored expansion
dedicated direct Conversation route
```

The persistence/threading data model is explicitly not frozen by this design phase.

## 2.6 2.5D before full 3D

Both proposals converge on restrained depth rather than a permanently perspective-distorted 3D world.

Promising depth uses include:

```text
selected work lifts slightly
active path gains one visual layer
project recedes during focus
conversation / analytical workspaces occupy clear depth planes
approval surfaces sit above ordinary inspection surfaces
```

True 3D remains a later experiment only if 2D/2.5D fails to solve a real orientation or comprehension problem.

---

# 3. Improvements contributed primarily by Research 037

Claude's Phase-B review identifies several places where Research 037 materially improves the independent proposal.

## 3.1 External product and technology evidence

Research 037 grounds hypotheses in current product/documentation evidence from React Flow, Dagster, Linear, VS Code, LangSmith Studio, Motion for React, Microsoft Semantic Zoom, Mapbox, Cytoscape.js, Sigma.js, PixiJS, React Three Fiber, Airflow and Prefect.

This does not select those products or libraries. It strengthens the plausibility and boundaries of the corresponding design mechanisms.

## 3.2 Information-density lenses

This is one of the strongest asymmetric additions from Research 037.

Semantic zoom answers:

```text
How much detail should be visible at this spatial scale?
```

A lens answers:

```text
Which dimension of project truth should be foregrounded for the user's current job?
```

Candidate lens families remain provisional:

```text
Project
Methodology
Evidence
Execution
Review
```

The mechanism deserves first-round mockup testing because it addresses a problem that zoom alone cannot solve.

## 3.3 Multi-axis state model

Research 037's sharper separation should govern visual exploration:

```text
WHAT IS THIS?
    Question / Investigation / Decision / Model work / Evaluation / Finding / Run-like unit

WHAT IS ITS PROJECT DISPOSITION?
    active / recommended / deferred / completed / blocked / future

WHAT IS HAPPENING NOW?
    idle / queued / running / waiting / failed / waiting for human

HOW IMPORTANT IS IT NOW?
    required / recommended / relevant / low priority
```

The design should not attempt to encode all four dimensions through one border color or one universal status badge.

## 3.4 Conversation persistence should remain open

Claude Phase B explicitly retracts its earlier overconfidence in a particular one-primary-thread model.

The current design phase should therefore separate:

```text
conversation UX
    what the user sees and how they navigate it

conversation persistence model
    how sessions, branches, summaries or history are represented in durable state
```

The second question needs later product/runtime evidence and should not be frozen from visual mockups.

---

# 4. Improvements contributed primarily by Claude's independent proposal

## 4.1 Forensic implementation specificity

Claude Phase A cited exact current implementation details rather than only conceptual limitations. That level of specificity should be carried into eventual prototype briefs and acceptance tests.

## 4.2 Falsifiable motion-budget hypothesis

The proposed one-to-three active animated-connector cap is useful precisely because it can be disproved through realistic scenes.

Mockups should deliberately create cases with:

```text
1 active relation
3 active relations
6+ potentially-active relations
```

and test whether the design can preserve attention without hiding real activity.

## 4.3 Decision-ready recommendation discipline

Research 037 appropriately stayed broad. Claude Phase A contributed a useful complementary discipline: nominate a preferred direction, name a genuine alternative, and state what evidence would reverse the preference.

Research 038 uses that discipline for the mockup set below while still avoiding premature visual-specification promotion.

---

# 5. Genuine unresolved disagreement

The strongest remaining substantive disagreement is command architecture at scale.

Current evidence supports the existing Jump/search model because it has real human-review history on the current representative fixture.

Research 037 raises a credible future-scale alternative:

```text
context-aware command surface
    actions adapt to selection / focus / run / conversation context
```

Claude correctly notes that neither side has evidence at the relevant project scale.

Therefore this remains deliberately unresolved.

Resolution evidence should come from a medium/large project fixture, not preference.

A useful test is:

```text
50-100 projected work units
multiple active branches
several blockers
several runs
multiple possible navigation targets
```

If current Jump/search plus direct controls remains clear and fast, redesign is unnecessary. If control proliferation or target discovery becomes materially worse, a contextual command architecture earns a prototype.

---

# 6. Technology scope is deliberately narrowed

Research 037's broad technology matrix was useful for reconnaissance, but Claude's scope-creep warning is valid.

The next design stage should not prototype seven libraries.

Before visual direction selection:

```text
NO React Flow adoption
NO PixiJS adoption
NO Sigma.js adoption
NO React Three Fiber adoption
NO layout-engine adoption
NO motion-library adoption
```

After a preferred visual direction exists, the first bounded technical comparators should be limited to the uncertainties that actually block implementation.

Current priority order if later earned:

```text
1. current DOM/CSS/SVG control baseline
2. React Flow comparator for semantic edges + semantic node content + grouping/zoom
3. Motion for React comparator for focus/conversation transitions if native transitions prove insufficient
```

GPU layers and true 3D should remain out of scope unless a later visual/performance problem specifically requires them.

---

# 7. Mockup direction set

The evidence supports three deliberately distinguishable directions for realistic visual comparison.

They are not final specifications.

## Direction M1: Living Precision Canvas

**Recommendation status:** preferred anchor for the first mockup round.

This direction combines the strongest independently reinforced parts of:

```text
Research 037 Direction A  Precision Instrument
Research 037 Direction B  Living Analytical Field
Claude Phase A            Living Process Canvas
```

The combination is intentional rather than accidental.

The product should be visually precise and calm by default, while actual project activity produces bounded life.

Character:

```text
premium precision-instrument baseline
high information hierarchy
fine technical spatial substrate
category-level work-unit grammar
semantic connectors
semantic zoom
local event-driven activity
completed regions visibly settle
subtle 2.5D selection/focus depth
long-session comfort
```

The critical restraint is:

```text
precision is the resting language
liveness is the transient state language
```

Potential failure mode:

```text
too much motion or glow turns it into decorative science fiction
```

Reversal evidence:

```text
if users cannot distinguish active/blocking/settled state quickly
without explanation, or if motion creates sustained distraction,
move toward M2 or a quieter variant of M1
```

## Direction M2: Spatial Control Room

**Recommendation status:** strongest alternative.

This direction emphasizes controllable information density and operational awareness more than expressive world behavior.

Character:

```text
spatial project topology
information-density lenses
strong execution/review visibility
compact live-state treatment
more explicit operational controls
restrained animation
high-density professional workbench
```

This is closest to Research 037 Direction C and becomes especially compelling if medium/large projects make current navigation and information density difficult.

Potential failure mode:

```text
becomes enterprise-dense, dashboard-like or visually generic
```

Reversal evidence:

```text
if lenses and operational controls add learning overhead
without improving task speed/comprehension, prefer M1
```

## Direction M3: Depth-Aware Analytical Workbench

**Recommendation status:** bounded high-upside alternative, especially for focus and conversation transitions.

This direction does not make the entire map three-dimensional. It uses 2.5D depth as a stronger interaction hierarchy.

Character:

```text
selected work visibly lifts
project topology recedes during focus
Conversation Workspace and analytical surfaces occupy clear planes
spatial continuity is strongly preserved during transitions
map remains front-readable and primarily 2D
```

Potential failure mode:

```text
novelty, animation or depth competes with analytical readability
```

Reversal evidence:

```text
if users report orientation is no better than the 2D baseline,
or reduced-motion substitutions feel like a different product,
keep depth only as subtle styling inside M1/M2
```

---

# 8. Required common mockup scenario

All three directions should use the same project state so the comparison tests design rather than content differences.

Representative scenario:

```text
Customer Churn Prediction

Objective
    predict churn early enough for intervention

Unresolved Question
    prediction moment / eligibility boundary

Active Investigation
    production missingness

Selected work
    chronological validation

Completed work
    baseline logistic model

Deferred work
    Random Forest benchmark

Downstream work
    evaluation / calibration / thresholding

Runtime state
    one active run
    one waiting-for-human decision

Conversation
    realistic long transcript with prior decisions,
    unresolved discussion and links back to visible work units
```

Each direction should show at least:

```text
1. resting overview
2. active investigation with bounded relation liveness
3. hard blocker and affected downstream path
4. completed versus unresolved branch
5. selected work unit
6. project-scale semantic zoom
7. work-scale semantic zoom
8. expanded long Conversation Workspace
9. conversation + analytical work coexistence
10. Execution or Review lens state
11. light appearance
12. dark appearance
```

---

# 9. Human evaluation questions

The first mockup review should prioritize comprehension and professional quality over novelty.

## 9.1 Five-second comprehension

```text
What is active?
What is blocked?
What is settled?
What currently needs the user?
Which relationship is actually live?
```

## 9.2 Spatial continuity

```text
Does the same work unit remain recognizably itself across zoom levels?
Does focus preserve where the user came from?
Does conversation expansion feel like the same ADS project environment?
```

## 9.3 Information density

```text
Does semantic zoom remove noise at project scale?
Do lenses reveal useful dimensions without making the model harder to learn?
Can the user recover hidden information easily?
```

## 9.4 Motion

```text
Is the resting world calm?
Can movement always be explained by real project activity?
Are one to three animated relations useful or still distracting?
Does reduced-motion preserve identical meaning?
```

## 9.5 Professional identity

```text
Could this support hours of serious analytical work?
Does it feel distinct from a generic SaaS dashboard?
Does it avoid becoming a decorative sci-fi visualization?
Does the light/dark identity preserve the same hierarchy?
```

---

# 10. Large-project test remains mandatory before implementation architecture

A visually successful ten-node mockup is not enough.

After first-round human direction review, the chosen one or two directions should be stress-tested with:

```text
small       10-20 projected work units
medium      50-100 projected work units
large       250+ projected work units represented through grouping
branchy     competing investigations / reopened work
run-heavy   multiple active and recently completed runs
```

The large fixture is also the evidence gate for the unresolved command-architecture question.

---

# 11. What is now strongly recommended versus still open

## Strongly recommended for first-round mockups

```text
semantic zoom
category-level work-unit visual grammar
semantic connector type + direction + state
sparse state-bearing liveness
calm resting state
full Conversation Workspace
conversation <-> structured project links
information-density lens experiment
multi-axis state treatment
2.5D only as bounded hierarchy/focus support
```

## Still deliberately open

```text
final visual identity
exact color/material system
exact work-unit silhouettes
exact connector styling
exact animation durations/easing
exact semantic-zoom thresholds
exact lens names/count
command architecture at scale
conversation persistence/threading model
final stage taxonomy/layout
auto-layout approach
final renderer / graph library
final motion library
production 2.5D use
full 3D
```

---

# 12. Synthesis recommendation

The strongest current direction is not a flashy 3D redesign and not a denser dashboard.

It is a **Living Precision Canvas**:

```text
precision-instrument visual discipline
+
semantic project topology
+
semantic zoom
+
meaningful relations
+
scarce event-driven liveness
+
first-class conversation depth
+
controlled information lenses
+
subtle depth where it improves orientation
```

This is a mockup recommendation, not a promoted visual specification.

The strongest alternative is the **Spatial Control Room**, especially if scale testing shows that operational density, command access and lens-driven visibility matter more than spatial expressiveness.

The **Depth-Aware Analytical Workbench** should remain a distinct third comparison because it may materially improve focus/conversation continuity even if its deeper visual language is not selected wholesale.

---

# 13. Next legitimate step

The next bounded step is:

```text
1. preserve this synthesis
2. move MC-0004 from comparative review into Phase C mockup direction evaluation
3. create realistic visual mockups for M1, M2 and M3 using the same scenario
4. include full Conversation Workspace states, not only the resting map
5. conduct human product review across the three directions
6. retain explicit unresolved questions rather than resolving them through aesthetics
7. only after a preferred one or two directions emerge, run bounded technical proof spikes
8. only after mockup + scale + accessibility evidence, freeze a prototype/implementation specification
```

No frontend implementation change is authorized by this synthesis.