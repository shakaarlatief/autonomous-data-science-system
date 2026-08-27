# Checkpoint 234: User-Curated Current-Process Focus Set Review Opened

**Date:** 2026-08-27  
**Status:** Phase-C human browser review open  
**Checkpoint class:** CONTINUITY / PRODUCT_DESIGN  
**Project stage:** V1 next-generation Project Cockpit browser-rendered design exploration  
**Scope:** Preserves acceptance of the stronger current-process focus lens, adds explicit user editing of focus-set membership, and opens human verification of add/remove focus interactions without deleting work or changing disposition.  
**Authority:** Current Phase-C routing/evidence boundary. User-curated focus membership is an accepted design direction under review, while final ownership, automatic membership logic and production persistence remain unfrozen. Production `/cockpit` remains untouched.  
**Interaction environment:** ChatGPT  
**Project / workspace:** Autonomous Data Science System  
**Interaction session:** chatgpt-08  
**Conversation title:** 08 - Project Cockpit Design Exploration  
**Primary collaborator:** ChatGPT  
**Branch:** `v1-cockpit-design-exploration`

## Preserved human result

The project owner accepted the stronger current-process focus lens:

```text
Perfect. This is exactly what I meant.
```

They then required the focus set itself to remain flexible and user-adjustable.

## New interaction requirement

```text
user can add a work unit to the current focus
user can remove a work unit from the current focus
this does NOT delete the work unit from the project
this does NOT change its project disposition
```

## Browser implementation

The current-process focus browser now includes:

```text
Context visible
Focus current process
Edit focus set
Reset example
```

When edit mode is active, every work unit exposes:

```text
+ FOCUS
- FOCUS
```

Membership changes immediately update both node suppression and connector suppression.

Browser-local persistence is used only for design-lab convenience and does not freeze production persistence semantics.

## Browser route

```text
http://localhost:5173/design-lab/work-unit-process-focus.html
```

Exact browser implementation target:

```text
da115b74de526fca05ed6f468bef39bdb801355c
```

Research:

```text
docs/research/063_user_curated_current_process_focus_membership.md
```

## Current human gate

```text
verify Edit focus set is clear
verify + FOCUS / - FOCUS do not imply deletion
verify membership changes update the focused hierarchy immediately
verify connector suppression follows membership changes
verify editing suppressed nodes remains comfortable
verify leaving edit mode restores strong suppression
```

Production `/cockpit` remains untouched.