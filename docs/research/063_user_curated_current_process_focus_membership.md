# Research 063: User-Curated Current-Process Focus Membership

**Date:** 2026-08-27  
**Status:** Active Phase-C product-design evidence  
**Scope:** Extends the accepted current-process focus lens so the user can explicitly add or remove work units from the current focus set without deleting the work unit or changing its project disposition.  
**Authority:** Research/design evidence only. Final ownership, persistence and automatic focus-membership logic remain unfrozen.

## 1. Human evidence

The project owner reviewed the current-process focus lens and concluded:

```text
Perfect. This is exactly what I meant.
```

They then added a durable product requirement:

```text
focus mode should be flexible
user should be able to add work units to the focus set
user should be able to remove work units from the focus set
```

The important interpretation is that this means editing the **focus set**, not deleting work units from the project.

## 2. Semantic separation

The experiment now preserves four different concepts:

```text
WORK-UNIT EXISTENCE
    whether the work unit exists in the project at all

PROJECT DISPOSITION
    Active / Recommended / Deferred / Completed / Blocked / Future, etc.

CURRENT-FOCUS MEMBERSHIP
    whether this work unit belongs to the process set emphasized by the current focus lens

VIEW EMPHASIS
    how strongly context outside the current focus is visually suppressed
```

Changing current-focus membership therefore does not mutate category, disposition, runtime state, priority or project existence.

## 3. Interaction model

The browser now exposes:

```text
Context visible
Focus current process
Edit focus set
Reset example
```

When `Edit focus set` is active, every work unit exposes a compact membership control:

```text
+ FOCUS
    add this work unit to the current focus set

- FOCUS
    remove this work unit from the current focus set
```

The edit control is intentionally separate from ordinary node interaction so later node opening/focus behavior is not overloaded.

## 4. Immediate visual feedback

Membership changes update immediately:

```text
node data-process-scope
focus-set membership count
strong suppression in Focus current process mode
connector context/current classification
```

A relation is treated as a contextual relation whenever either endpoint lies outside the current focus set. This means the visual process path updates consistently when the user changes membership.

## 5. Editing while the focus lens is active

Strong suppression is useful for normal focused work but can make an edit control difficult to operate.

Therefore, while `Edit focus set` is active:

```text
contextual nodes remain visibly recessed
but are temporarily raised to a more operable salience
membership controls remain clearly visible
```

Leaving edit mode restores the full focus suppression immediately.

This is an interaction-mode exception, not a change to the focus hierarchy.

## 6. Prototype persistence

The design-lab browser stores the chosen focus set in browser `localStorage` so the user can change membership, refresh the page and continue evaluating the same arrangement.

This is deliberately classified as:

```text
PROTOTYPE CONVENIENCE ONLY
```

It does not decide production persistence.

Potential later production models include:

```text
project-level focus set
view-specific focus set
user-personal focus set
system-suggested focus set with human overrides
multiple named focus sets / lenses
```

No one model is selected here.

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

Exact editable-focus browser implementation target:

```text
da115b74de526fca05ed6f468bef39bdb801355c
```

## 8. Human review gate

The next review should verify:

```text
Edit focus set is visually clear and not confused with deleting work
+ FOCUS / - FOCUS controls are unobtrusive but discoverable
membership changes immediately update the focused hierarchy
connector suppression follows the edited focus set
edit mode keeps suppressed nodes operable
leaving edit mode restores the stronger suppression cleanly
browser persistence behaves naturally for the prototype
```

The human does not need to select production persistence semantics yet.

## 9. Production boundary

No production `/cockpit` file changed.

No final current-focus membership model is promoted.

No automatic focus-selection algorithm is selected.

No production persistence mechanism is selected.
