# Research 070: Shared Operational Status Carrier, Blocker Relationship, and Work-Unit Detail Deferment

**Date:** 2026-08-27  
**Status:** Active Phase-C refinement inside Checkpoint 238  
**Scope:** Refines the first BLOCKED progress-constraint experiment after human review proposed reusing the already accepted runtime carrier language for BLOCKED, preserving explicit blocker-to-blocked cause relationships, and separately noting future expanded work-unit detail interaction.  
**Authority:** Design evidence only. This memo does not freeze the final project-disposition ontology, runtime ontology, progress-constraint ontology, compatibility matrix, work-unit detail architecture, or production visual system.

## 1. Human refinement

The project owner rejected the need for a completely separate family of blocked-only node ornaments as the likely direction and proposed a simpler visual reuse:

```text
BLOCKED can look like another operational status

Dot mode
    same compact red dot / dynamic ring family

Tag mode
    same soft-shade status-tag family
    explicit text = BLOCKED

Global switch
    change every status carrier together

Local switch
    click one work unit's carrier
    switch only that work unit
```

The important qualification is semantic:

```text
shared visual carrier
    !=
merged ontology
```

The visual slot can be shared even if BLOCKED remains a progress constraint rather than a runtime state in the project model.

## 2. Cause, effect, and execution failure

The resulting conceptual distinction is:

```text
BLOCKER
    cause / unresolved object preventing progress

BLOCKS
    relationship from cause to affected work

BLOCKED
    current progress constraint on the affected work unit

FAIL
    failed current execution attempt
```

A visible blocker may be a Question / Blocker work unit, for example:

```text
[Resolve data contract]
Question / Blocker
CURRENT + HUMAN

        BLOCKS
           ↓

[Production missingness]
Investigation
CURRENT + BLOCKED
```

The source work unit need not itself be Blocked.

One blocker can block several work units, and one work unit can eventually have multiple blocker causes. The exact many-to-many data model and relation ontology remain future work.

## 3. BLOCKED versus FAIL in the shared carrier

Both may use the red status family, but they retain different meanings.

### Dot / ring mode

```text
BLOCKED
    red center dot
    circular dynamic ring

FAIL
    red center dot
    sharper non-circular / rotated failure ring
```

This retains a compact learned distinction even when explicit text is not shown.

### Tag mode

```text
BLOCKED
    red T7 Soft Shade tag
    text = BLOCKED

FAIL
    red T7 Soft Shade tag
    text = FAIL
```

Explicit text makes the semantic difference direct.

## 4. Operational-status presentation slot

The new browser tests a presentation abstraction:

```text
one bottom-right operational-status slot
```

That slot may currently present:

```text
live runtime state
or
blocking constraint
```

This is a UI composition rule, not a claim that runtime and progress constraints are the same model field.

A useful working interpretation is:

```text
if Blocked
    normally no live runtime episode is shown
    status slot presents BLOCKED

if current attempt Failed but work can still proceed/retry
    status slot presents FAIL

if a failed attempt creates a new unresolved blocker
    current status may become BLOCKED
    failed attempt remains available as execution history/provenance
```

The exact state-transition rules remain unfrozen.

## 5. New browser

Local route:

```text
http://localhost:5173/design-lab/work-unit-blocked-carrier.html
```

Files:

```text
frontend/design-lab/work-unit-blocked-carrier.html
frontend/design-lab/work-unit-blocked-carrier.css
frontend/design-lab/work-unit-blocked-carrier.js
```

Exact browser implementation target:

```text
b65df18f8d04c149979854c0aee695abb9a9036e
```

The browser preserves the earlier C0-C6 experiment as predecessor evidence rather than deleting it.

## 6. Browser structure

The controlled comparison shows:

```text
BLOCKED + dot
BLOCKED + tag
FAIL + dot
FAIL + tag
```

The practical scene contains:

```text
Question / Blocker    CURRENT + HUMAN
    BLOCKS -> Investigation
    BLOCKS -> Validation

Investigation         CURRENT + BLOCKED
Validation            NEXT + BLOCKED
Model Work            CURRENT + FAIL
Investigation         CURRENT + RUN
Evaluation            DEFER + NONE
```

The BLOCKS relationships use a restrained direction arrow plus explicit relation tag so cause and effect can be read directly.

The relation presentation is visual-test evidence only. Final relation taxonomy and production BLOCKS relation semantics remain unfrozen.

## 7. Global and local switching

The accepted runtime-carrier configurability is generalized visually:

```text
GLOBAL
    Dot + dynamic ring
    or
    Soft-shade status tag

    applies to runtime and BLOCKED carriers
    clears local overrides

LOCAL
    click visible carrier on one work unit
    switch only that work unit
```

Work units with no operational status show no carrier.

Reduced motion preserves static status identity while stopping semantic animation.

## 8. Work-unit expansion / detail interaction

The project owner also raised a separate future interaction idea:

```text
click a compact work-unit box
    -> expand it elegantly
    -> reveal more information about that work unit
```

This should **not** be mixed into the current BLOCKED carrier experiment because it changes information density, node geometry, navigation, and interaction depth simultaneously.

The broader need is already compatible with promoted Specification 008, which requires selecting a supported work unit to transition from the project map into real specialist/deep-work content rather than permanently mounting every specialist workspace inside every node.

The exact intermediate interaction remains unfrozen. A promising future hierarchy to test is:

```text
compact map work unit
    -> expanded contextual/detail card
    -> full specialist workspace / deep focus
```

But the middle expanded-card level has not yet earned promotion.

It should be revisited with:

```text
semantic zoom
C5 Internal Layout Grammar
information-density lenses
selected/focused persistent treatment
work-unit detail / provenance presentation
```

This idea is preserved now so it is not lost, but implementation is deliberately deferred.

## 9. Current review questions

```text
1. Does BLOCKED look natural in the same carrier family as runtime?
2. In compact dot mode, is circular BLOCKED sufficiently distinct from sharper FAIL?
3. In tag mode, do BLOCKED and FAIL remain immediately explicit?
4. Does the BLOCKS relation make the blocker cause/effect model intuitive?
5. Does the Question / Blocker source remain conceptually different from a BLOCKED target?
6. Does one shared operational-status slot reduce clutter without collapsing semantics?
7. Does global + local carrier switching remain useful across both runtime and constraint statuses?
```

## 10. Checkpoint hygiene

No new checkpoint is created yet.

Reason:

```text
Checkpoint 238 already owns the BLOCKED semantic/visual review boundary
+
this refinement changes the active visual hypothesis and adds cause/effect evidence
+
but the overarching question remains how BLOCKED should coexist with disposition, runtime and blocker causes
```

If human review accepts this shared-carrier + BLOCKS relationship model and we move to a distinct next semantic slice, that transition should create the next checkpoint.

## 11. Still unfrozen

```text
final progress-constraint ontology
whether BLOCKED is binary or multi-class
exact compatibility rules between constraint and runtime
multiple simultaneous blockers
blocker cause object taxonomy
final BLOCKS relation semantics
final operational-status slot semantics
production status-carrier preference/persistence
work-unit inline expansion behavior
semantic zoom and C5 Internal Layout Grammar
specialist workspace transition details
```
