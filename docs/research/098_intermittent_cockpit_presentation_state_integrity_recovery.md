# Research 098: Intermittent Cockpit Presentation-State Integrity Recovery

**Date:** 2026-08-29  
**Status:** IMPLEMENTED / DETERMINISTICALLY VERIFIED / AWAITING HUMAN CONFIRMATION  
**Scope:** Root-cause analysis and recovery of two intermittent integrated-Cockpit presentation failures reported during Adaptive Conversation Dock review: disappearing Conversation WorkUnit spacing and desynchronized current-process Focus recession.  
**Interaction environment:** ChatGPT  
**Interaction session:** `chatgpt-09`  
**Branch:** `v1-cockpit-design-exploration`

## 1. Trigger

Before judging the Adaptive Conversation Dock candidate, the project owner reported two failures that had appeared, disappeared and reappeared across otherwise similar browser sessions:

```text
Conversation Boxes rail
    previously accepted visible gaps sometimes collapse again

current-process Focus
    sometimes behaves correctly
    sometimes context WorkUnit boxes do not recess correctly
    sometimes relation lines recess while the WorkUnit boxes do not
```

The supplied screenshots included both the accepted-looking and failed-looking states. Because the symptoms were intermittent, this investigation treated them as lifecycle/composition-integrity failures rather than as requests for new visual tuning.

## 2. Conversation spacing diagnosis

Checkpoint 256 had correctly recognized that transformed canonical WorkUnits require real row geometry in addition to grid row-gap. However, the current Conversation renderer identifies WorkUnit rows with:

```text
data-thread-scope="work"
```

while the structural Checkpoint 256 padding rule still targeted the historical selector:

```text
.is-workunit-thread
```

That class is not emitted by the current Conversation renderer.

This was a real selector-drift defect. The 16px list gap could still make deterministic geometry tests pass in some compositions, but the 6px structural row padding was not actually bound to the current WorkUnit rows.

A second fragility existed around composition order. The Checkpoint 256 correction stylesheet was mounted through the current flat-rail study module, which is loaded late. The accepted Conversation spacing therefore depended unnecessarily on a separate shell module and its stylesheet lifecycle. The Adaptive Conversation study adds another late-mounted presentation layer, increasing the number of possible load/order combinations.

## 3. Conversation spacing recovery

The recovery separates the accepted spacing guarantee from route-specific rail composition.

A new statically loaded integrity layer now owns only the already-accepted Conversation spacing contract:

```text
frontend/design-lab/cockpit-reintegration-presentation-integrity.css
```

It enforces:

```text
Boxes list row-gap                     16px
current WorkUnit row identity          [data-thread-scope="work"]
WorkUnit row structural padding        6px top + bottom
historical .is-workunit-thread         compatibility fallback only
canonical WorkUnit footprint           unchanged
```

The original Checkpoint 256 stylesheet was also corrected to target the actual current DOM identity while retaining the historical class selector as a compatibility fallback.

This means accepted Conversation spacing no longer depends on the current flat-rail module loading first or remaining present.

## 4. Focus diagnosis

The Focus failure had an asymmetric lifecycle.

The current-process Focus JavaScript established node membership once at startup:

```text
q, i, v -> current
other WorkUnits -> context
```

Relations, by contrast, had a MutationObserver that continuously reclassified relation groups as current/context edges when relation geometry was regenerated.

Therefore the system could reach an inconsistent presentation state if WorkUnit DOM was rebuilt or replaced while project semantics stayed constant:

```text
relation groups
    continuously resynchronized

WorkUnit data-process-scope
    initialized only once
```

That asymmetry directly explains the reported failure shape in which lines can recess while boxes do not.

There was also a stylesheet-readiness/precedence weakness. The accepted Focus stylesheet was injected from JavaScript at runtime rather than being part of the browser's static stylesheet graph. Later-mounted whole-product study styles could therefore participate in source-order competition around an already-accepted view-composition contract.

## 5. Focus recovery

Focus membership is now represented by one authoritative in-memory membership set instead of by whichever WorkUnit elements happen to be mounted.

The adapter now:

```text
owns current membership independently of DOM instances
reapplies data-process-scope to all mounted WorkUnits
observes direct WorkUnit remount/replacement
restores membership controls on replacement nodes
resynchronizes relation current/context classes after node repair
preserves user-edited membership through a WorkUnit remount
resets explicitly to the accepted q/i/v example set on Reset
```

The Focus stylesheet is now statically linked by the integrated browser. The runtime installer remains only as a fallback for historical/isolated entry points.

The accepted Focus opacity/filter contract is also given explicit composition precedence so late-mounted study styles cannot silently cancel it:

```text
focused context WorkUnit opacity    0.27
focused current WorkUnit opacity    1.00
context-edge opacity                0.16
current-edge opacity                1.00
```

The accepted hover and edit-mode lift behavior remains intact.

No WorkUnit semantic state, selection, X5 state, conversation ownership or focus-membership meaning was changed.

## 6. Deterministic regression expansion

A new browser regression surface was added:

```text
frontend/e2e/cockpit-reintegration-presentation-integrity.spec.ts
```

It adds two high-value lifecycle tests.

### Conversation lifecycle test

Uses a route matching the reported integrated state closely:

```text
?conversation=adaptive-dock&focus=work&work=i&depth=x5
```

It verifies accepted visible WorkUnit separation through:

```text
full-focus Conversation
Boxes -> Text -> Boxes switching
co-present mode
Threads drawer invocation
return to full focus
```

### Focus lifecycle test

It verifies:

```text
Focus stylesheet is ready in the static stylesheet graph
context/current node recession is synchronized
context/current relation recession is synchronized
three repeated context <-> focused cycles remain stable
replacement of a WorkUnit DOM carrier repairs data-process-scope
replacement node receives its membership control again
relation recession remains synchronized after the remount
```

## 7. Verification

Implementation target:

```text
0374d624ec0e88d65060fb2424ce18291ca40792
```

Complete Cockpit fidelity workflow:

```text
workflow run  33240152004
job           99067985262
result        SUCCESS
browser tests 73 / 73 passing
```

All previous 71 tests remain green. The two new presentation-integrity tests also pass.

## 8. Interpretation

These bugs were not evidence that the accepted spacing or Focus designs were wrong. They were integration-integrity defects:

```text
accepted presentation rule
    + stale selector / asymmetric lifecycle / late style composition
    -> intermittent rendered state
```

The recovery therefore does not reopen M09 Focus semantics or the accepted Conversation spacing values.

## 9. Human gate

Deterministic coverage now exercises the exact failure families, but the project owner should still confirm the repaired browser visually because the original report was intermittent and emerged under normal human use.

Next human check:

```text
1. pull the latest branch
2. reload the normal Cockpit and exercise Focus repeatedly
3. open Conversation in Boxes mode and switch presentation/modes repeatedly
4. confirm the prior intermittent failures no longer reproduce
5. once stable, resume evaluation of the Adaptive Conversation Dock itself
```
