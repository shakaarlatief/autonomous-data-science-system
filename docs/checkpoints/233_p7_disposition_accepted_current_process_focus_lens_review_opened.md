# Checkpoint 233: P7 Disposition Accepted, Current-Process Focus Lens Review Opened

**Date:** 2026-08-27  
**Branch:** `v1-cockpit-design-exploration`  
**Status:** Phase-C human browser review open

## Preserved human result

The project owner accepted the practical P7 disposition treatment:

```text
P7  Neutral Tag + Tone
    category color dominant at rest
    neutral disposition tag at rest
    state-colored disposition tag on hover
    selective tonal recession retained
```

Human result:

```text
perfect
```

## New design requirement

The project owner then requested a more dramatic suppression mechanism for boxes that remain part of the wider project context but are not currently part of the active process.

The requirement is interpreted as a separate view/emphasis lens rather than another project-disposition encoding.

## New semantic separation

```text
project disposition
    semantic state of the work unit

current-process membership
    whether the work unit belongs to the currently emphasized process

view emphasis
    how strongly contextual work is visually suppressed
```

## New browser slice

```text
http://localhost:5173/design-lab/work-unit-process-focus.html
```

Modes:

```text
Context visible
    accepted P7 presentation remains readable

Focus current process
    current-process fixtures remain full salience
    contextual fixtures are strongly suppressed
    contextual connector segments also recede
    hover partially restores contextual nodes for inspection
```

Exact implementation target:

```text
b311796f86ff577354a2bfe14b850bd6a49a9c06
```

Research:

```text
docs/research/062_current_process_focus_lens_and_context_suppression_experiment.md
```

## Current human gate

```text
compare Context visible vs Focus current process
-> judge strength and aesthetics of suppression
-> judge hover recoverability
-> judge connector suppression
-> refine / accept / reject the lens
```

The final current-process-membership semantics remain unfrozen.

Production `/cockpit` remains untouched.
