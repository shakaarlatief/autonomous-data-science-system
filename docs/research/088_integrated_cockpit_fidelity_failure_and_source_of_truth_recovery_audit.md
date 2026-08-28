# Research 088: Integrated Cockpit Fidelity Failure and Source-of-Truth Recovery Audit

**Date:** 2026-08-28  
**Status:** ACTIVE RECOVERY AUDIT / INTEGRATION FIDELITY FAILURE CONFIRMED  
**Scope:** Audits why the first holistic integrated Cockpit at `8e554d847bb3b6318db432abcb5dff742f0fa523` did not resemble the product direction already selected throughout Phase C, and determines whether the failure originates primarily in repository preservation or in the reconstruction method.  
**Authority:** Current recovery evidence. This memo explicitly invalidates the first holistic browser as an accepted visual/product baseline. It does not invalidate the underlying accepted Phase-C decisions or their exact historical target SHAs.

## 1. Trigger

The project owner reviewed the first holistic integrated Cockpit and immediately judged it to be fundamentally inconsistent with the Cockpit that had been designed throughout the preceding Phase-C work.

The concern is architectural, not cosmetic:

```text
If the repository really preserves the decisions,
why did a repository-driven reconstruction look like a different product?
```

This audit therefore stops further design iteration and tests two competing explanations:

```text
H1  repository knowledge was not preserved precisely enough

H2  repository knowledge exists,
    but the integration process failed to consume the precise source artifacts
```

## 2. Primary finding

Current evidence strongly supports **H2**.

The repository contains exact accepted target SHAs and executable HTML/CSS/JS artifacts for the major Phase-C decisions. The failed integration did not compose or port those artifacts faithfully. Instead, it created a new monolithic HTML/CSS/JS implementation and used textual decision summaries as design guidance.

That reconstruction method introduced visual and behavioral reinterpretation where the task required fidelity.

Therefore:

```text
repository preservation
    NOT exonerated from further hardening
    but NOT the primary observed failure

integration method
    FAILED

first holistic browser
    INVALID as an accepted Cockpit baseline
    preserved only as failure evidence
```

## 3. Concrete implementation evidence

### 3.1 The integrated browser is a fresh monolithic reimplementation

The failed browser is implemented through:

```text
frontend/design-lab/cockpit-integrated-baseline.html
frontend/design-lab/cockpit-integrated-baseline.css
frontend/design-lab/cockpit-integrated-baseline.js
```

It does not directly reuse the accepted Phase-C source modules as implementation dependencies. Accepted visual systems were manually recreated inside the new files.

This is the central process error.

### 3.2 Canonical WorkUnit geometry and surface grammar changed

At the accepted WorkUnit/SEL2 target:

```text
e7304fe834d86166d843fda7e1df0f4ddb1f793a
```

`work-unit-grammar.css` renders project-scene WorkUnits at approximately:

```text
width   176px
height   92px
radius    9px
padding  11px 11px 10px 14px
```

The failed integrated browser instead introduced a new WorkUnit implementation approximately:

```text
width   230px
height  132px
radius   10-12px
padding  13px 14px 11px
```

That is not a neutral integration detail. It materially changes the visual object that had already been designed and reviewed.

The accepted WorkUnit source also contains a layered H4/rest-light grammar including separate resting spill, resting light, hover halo, world light, pointer-follow light and perimeter sweep. The failed integrated browser compresses this into a different `node-light` treatment and new surface styling.

### 3.3 G4 world behavior was reauthored instead of carried forward

The accepted work-unit/world implementation at the accepted target dynamically assigns current orientation/position/timing and places glints on 100px major-grid intersections in JavaScript.

The failed integration instead hard-codes two ambient currents at authored coordinates such as:

```text
horizontal current top = 420px
vertical current left = 1420px
```

and adds fixed radial world gradients at authored percentages.

This contradicts the held G4 direction that travelling currents/glints should not collapse into a few fixed authored ambient focal coordinates.

### 3.4 Quiet Graphite was approximated rather than reused

The independently frozen Quiet Graphite source at:

```text
c66f72a74e681f89fd52ba591a1387ea50f0e959
```

contains its own concrete palette, geometry, transcript width, message spacing and typography variables.

The failed integration defines a new global palette and typography in `cockpit-integrated-baseline.css` rather than consuming the accepted Quiet Graphite implementation unchanged and adapting only the minimum integration boundaries.

For example, the accepted Quiet Graphite root begins from values including:

```text
bg      #070a0f
stage   #0b1017
panel   #0f151d
accent  #69d9c2
```

while the failed integration begins from a different global palette and new font system.

The difference is small in individual token values but large in aggregate because the entire product was restyled at the same time.

### 3.5 Repository summaries claimed fidelity without an implementation-level gate

Research 087 correctly stated the intended rule:

```text
reconstruct from accepted invariants
not from incidental later fixture regressions
```

But there was no deterministic integration manifest requiring each accepted mechanism to point to:

```text
exact target SHA
exact source file(s)
exact implementation to reuse/port
known fixture caveats
allowed adaptation boundary
fidelity verification result
```

As a result, a prose-level audit could say an invariant was present while the actual CSS/JS embodied a substantially different interpretation.

## 4. What this says about repository knowledge

The repository is not currently showing evidence of having forgotten the major selected decisions.

It preserves, among other things, exact targets for:

```text
directionality
relation class E5
P7 disposition
current-process focus
T7 Soft Shade
runtime carrier
BLOCKED / FAIL carrier
A3 attention
SEL2 selection
X5 contextual expansion
Z7 specialist transition
Quiet Graphite
A6 no-floating-box refinement
```

The failure is that current navigation documents make it possible for an integrator to stop at the semantic summary and then redraw the design from memory/specification.

That is insufficient for a project whose visual decisions are earned through browser review.

So a second-order repository hardening is still warranted:

```text
semantic decision record
    +
exact implementation provenance
    +
fidelity gate
```

## 5. Immediate disposition of the failed integrated browser

```text
8e554d847bb3b6318db432abcb5dff742f0fa523
    FAILED INTEGRATION ATTEMPT

not an accepted baseline
not a source for new visual decisions
not a production target
preserved only as diagnostic evidence
```

Production `/cockpit` remains untouched.

No accepted Phase-C decision is revoked by this failure.

## 6. Recovery protocol before another holistic rebuild

Do **not** immediately redraw the Cockpit again.

First construct an explicit accepted-implementation manifest covering every held mechanism that will appear in the integrated product.

For each item the manifest must contain:

```text
semantic decision
status
exact accepted target SHA
exact source HTML/CSS/JS files
what visual/behavioral properties are invariant
what is allowed to adapt during integration
known historical fixture defects
verification method
```

Then rebuild the integrated Cockpit using this rule:

```text
accepted component exists
    -> reuse or port its exact implementation
    -> do not restyle from prose

accepted interaction exists
    -> reuse or port its exact behavior
    -> do not substitute a merely similar animation

no accepted whole-product answer exists
    -> add only the minimum provisional integration glue
    -> label it explicitly provisional
```

## 7. Fidelity validation required for the next integrated Cockpit

The next integrated build should not be called a baseline until an explicit audit checks at least:

```text
G4 world
H4 rest/hover
canonical WorkUnit component
category markers
appearance options
E5 relation treatment
D0-D3 directionality
P7 disposition
current-process focus
runtime carrier
T7 Soft Shade
BLOCKED / FAIL
A3 attention
SEL2 four-corner selection
X5 geometry and context behavior
Z7 Deep Dive
specialist end-state / compass
S0 geometric zoom behavior
Quiet Graphite
Boxes / Text rail
A6
conversation access from Grid and Deep Dive
source-state restoration
```

For visually accepted items, the audit should compare the integrated rendering against the exact accepted target, not merely against a prose description.

## 8. Current conclusion

The project owner was correct to stop the process immediately.

The current evidence does **not** justify concluding that the repository knowledge architecture has failed wholesale.

It does justify concluding that the integration protocol was not strong enough for the repository architecture we have built.

The recovery task is therefore:

```text
preserve the failure
harden implementation provenance
construct exact accepted-implementation manifest
rebuild by composition/porting rather than reinterpretation
validate fidelity before holistic product review resumes
```
