# Checkpoint 237: Switchable Runtime Carrier Convergence Review Opened

**Date:** 2026-08-27  
**Status:** Current product-design checkpoint  
**Checkpoint class:** CONTINUITY / PRODUCT_DESIGN / VISUAL_CONVERGENCE  
**Project stage:** V1 next-generation Project Cockpit browser-rendered design exploration  
**Scope:** Verifies the human observation that the earlier R1 Status Lamp and R5 Motion Signal were perceptually collapsing together, retires their distinction from active convergence, and opens a narrower runtime-carrier experiment with exactly one live-runtime carrier per work unit plus global and per-work-unit switching.  
**Authority:** Current Phase-C routing/evidence boundary only. The final runtime carrier, runtime ontology, project-disposition ontology, Blocked semantics, and production preference-persistence model remain unfrozen.  
**Interaction environment:** ChatGPT  
**Project / workspace:** Autonomous Data Science System  
**Interaction session:** chatgpt-08  
**Conversation title:** 08 - Project Cockpit Design Exploration  
**Primary collaborator:** ChatGPT

## 1. Human review evidence

The project owner identified two important problems in the corrected R0-R6 runtime browser:

```text
R1 Status Lamp and R5 Motion Signal look effectively the same
except Failed makes the difference more apparent

+

dot + runtime tag together is not the right composition
```

The project owner proposed a more focused two-carrier design:

```text
A. dot with dynamic outer circle/ring
B. runtime tag with a circulating perimeter line
```

and requested two switching scopes:

```text
global switch for every box
+
per-box switch by clicking the visible runtime carrier
```

## 2. R1/R5 implementation verification

Direct implementation inspection confirms:

```text
R1
    runtime lamp only

R5
    same runtime lamp
    + runtime motion ring
```

Therefore they were not literally identical in code.

However, for Queued / Running / Waiting / Waiting for Human, the R5 ring occupied nearly the same small location and used low-salience pulse treatment around the R1 lamp. Failed altered the ring shape more visibly.

Result:

```text
implementation difference exists
visual differentiation at working scale is insufficient
```

The human observation is therefore accepted as valid design evidence.

## 3. Current convergence architecture

Runtime remains conditional under Research 066.

For a work unit with a live runtime episode:

```text
exactly ONE runtime carrier is active
```

Current candidates:

```text
Dot + dynamic ring
Animated runtime tag
```

The earlier dot-plus-tag hybrid is not carried forward as the active composition.

## 4. Dot + dynamic ring

The dot carrier uses:

```text
state-colored core dot
stronger state-colored outer ring
state-sensitive animation pacing
sharper Failed ring treatment
```

The ring is intentionally more legible than the previous R5 motion ring so that this carrier does not collapse into the static-lamp appearance.

## 5. Animated runtime tag

The tag carrier uses:

```text
explicit state text
state-colored text
state-colored perimeter
circulating bright perimeter trace
```

The tag animation is deliberately different from the dot's breathing/expanding ring.

## 6. Switching behavior

Global control:

```text
Dot + dynamic ring
Animated runtime tag
```

Selecting a global carrier:

```text
changes all live-runtime nodes
clears local overrides
```

Per-box interaction:

```text
click visible dot/ring
    -> switch only that node to tag

click visible tag
    -> switch only that node to dot/ring
```

If the node differs from the current global carrier, it is a local override. Switching it back to the global carrier removes the override.

## 7. No-runtime invariant

No current runtime episode means:

```text
no dot
no ring
no runtime tag
no carrier switch target
```

The practical scene retains Deferred + NONE and Future + NONE as explicit checks.

## 8. Reduced motion

Reduced motion disables runtime animation but keeps static state identity:

```text
static dot + ring
or
static runtime tag + perimeter
```

No state depends on motion alone.

## 9. Browser target

Local route:

```text
http://localhost:5173/design-lab/work-unit-runtime-carrier-switch.html
```

Exact browser implementation target:

```text
3a862c659e60e53832eaa5940ddb60d05734cd7d
```

Research:

```text
docs/research/067_switchable_runtime_carrier_convergence_and_r1_r5_verification.md
```

Production `/cockpit` remains untouched.

## 10. Current human gate

The next actor is the human project owner.

Review:

```text
1. pull v1-cockpit-design-exploration
2. open work-unit-runtime-carrier-switch.html
3. compare Dot + dynamic ring with Animated runtime tag
4. verify the dot ring is now clearly visible as dynamic
5. verify the tag perimeter trace feels clean and distinct from the dot animation
6. use the global switch in both directions
7. click individual runtime carriers to create local overrides
8. judge a mixed practical scene with both carrier types present
9. toggle Reduced motion
10. confirm NONE / DEFER + NONE / FUTURE + NONE remain free of runtime instrumentation
11. prefer / reject / combine / refine
12. keep production Cockpit untouched
```
