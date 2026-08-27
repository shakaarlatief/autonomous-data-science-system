# Research 062: Current-Process Focus Lens and Context Suppression Experiment

**Date:** 2026-08-27  
**Status:** Active Phase-C product-design evidence  
**Scope:** Preserves acceptance of the P7 Neutral Tag + Tone disposition treatment and opens a separate view-lens experiment for stronger suppression of work that remains useful context but is not currently part of the active process.  
**Authority:** Research/design evidence only. Neither the final project-disposition ontology nor the final definition of current-process membership is frozen.

## 1. Human evidence

The project owner accepted the latest practical P7 scene:

```text
Neutral Tag + Tone
    accepted visual direction
    disposition tag neutral at rest
    disposition tag state-colored on hover
    existing tonal recession retained
```

The project owner then identified a different need:

> the Cockpit should also have a more dramatic way to suppress boxes that are not currently actually part of the process, while keeping the current boxes as the clear process and retaining the other boxes as nicely suppressed context.

This is not treated as another project-disposition state.

## 2. Key semantic separation

The new design question introduces a distinct axis:

```text
PROJECT DISPOSITION
    where the work unit stands in the project

CURRENT-PROCESS MEMBERSHIP
    whether the work unit belongs to the currently emphasized process path / horizon

VIEW EMPHASIS
    how strongly contextual work is visually suppressed in the current Cockpit lens
```

The experiment therefore does not infer current-process membership from disposition.

A Completed work unit, for example, could be context in one view but still be intentionally emphasized in another. Likewise, Blocked work can remain part of the current process even though it cannot proceed.

## 3. Held P7 disposition treatment

The new slice holds the accepted P7 treatment constant:

```text
REST
    category color remains dominant
    disposition tag is visible and neutral
    Completed / Deferred / Future retain existing tonal recession

HOVER
    disposition tag reveals state-specific color
    accepted H4 hover behavior remains
```

The purpose is to avoid reopening the disposition carrier while testing a stronger map-level emphasis lens.

## 4. Process-focus lens

The browser exposes two presentation modes over the same project state:

```text
Context visible
    existing P7 treatment
    all contextual work remains normally readable

Focus current process
    current-process work units retain full salience
    context work units become dramatically quieter
    context connectors recede together with context nodes
    contextual nodes remain hover-recoverable
```

The focus lens is presentation-only. It does not delete work units or mutate their disposition.

## 5. Representative fixture

For the browser test only:

```text
CURRENT-PROCESS FIXTURES
    Question / Blocker      BLOCKED
    Investigation           ACTIVE
    Validation / Analysis   NEXT

CONTEXT FIXTURES
    Model Work              DONE
    Evaluation              DEFER
    Investigation           FUTURE
```

This assignment exists only to test the visual mechanism.

The final ADS rules for determining current-process membership remain open.

## 6. Strong suppression behavior

In Focus current process mode, context nodes use stronger visual recession than ordinary disposition tone:

```text
substantially lower whole-node opacity
reduced saturation and brightness
resting glow / spill strongly reduced
context connector segments strongly reduced
```

On hover, a contextual node partially recovers:

```text
more opacity
more saturation / brightness
neutral disposition tag reveals its state hue
some local resting illumination returns
```

It intentionally does not recover all the way to current-process salience. This preserves the active-process hierarchy while still allowing inspection.

## 7. Browser implementation

Files:

```text
frontend/design-lab/work-unit-process-focus.html
frontend/design-lab/work-unit-process-focus.css
frontend/design-lab/work-unit-process-focus.js
```

Local URL:

```text
http://localhost:5173/design-lab/work-unit-process-focus.html
```

Exact browser implementation target:

```text
b311796f86ff577354a2bfe14b850bd6a49a9c06
```

## 8. Human review gate

The next review should answer:

```text
Does Context visible remain the right calm all-context view?
Does Focus current process suppress contextual work enough that the active process becomes immediately dominant?
Is the suppression still aesthetically coherent with the premium Cockpit design?
Does hover recovery make contextual work inspectable without making it compete with current work?
Do contextual connector segments recede enough together with contextual nodes?
Should this remain a binary lens or later support additional user-adjustable levels?
```

No answer to the final current-process-membership semantics is required in this gate.

## 9. Production boundary

No production `/cockpit` file changed.

No final current-process-membership model is promoted.

No final user setting or persistence mechanism is selected.

No final project-disposition ontology is frozen.
