# Checkpoint 224: User-Configurable Cockpit Visual Grammar Prototype Opened

**Date:** 2026-08-26  
**Status:** Current product-design checkpoint  
**Checkpoint class:** CONTINUITY / PRODUCT_DESIGN  
**Project stage:** V1 next-generation Project Cockpit browser-rendered design exploration  
**Scope:** Records the product-owner decision that positively reviewed Cockpit visual treatments should coexist as user-configurable appearance choices, preserves the semantic/presentation boundary, and opens a live browser configurator for human review.  
**Authority:** Current Phase-C routing/evidence boundary only. No production settings storage or final visual-system contract is promoted. Specification 008 remains the promoted Cockpit interaction architecture.

## 1. Product-owner decision

The project owner identified that the visual design process does not need to force one mandatory appearance when several mechanisms are good and semantically compatible.

Explicit product intent:

```text
user can design/personalize the Cockpit appearance
normal boxes and differentiated shapes can coexist
micro design can be enabled or disabled
multiple approved visual mechanisms can coexist as configuration
```

This is consistent with ADS being a long-lived professional workspace for the user's own data-science projects.

## 2. Architecture opened

The design direction now separates:

```text
semantic project model
    governed by ADS

presentation profile
    safely configurable by the user
```

Current semantic invariants:

```text
scientific marker mapping stays fixed
Reduced in-box light stays the preferred baseline
category/status/runtime/importance meanings do not change with appearance
accessibility constraints override decorative preference where necessary
```

Current configurable dimensions:

```text
Box shape
    Normal
    Subtle shapes

Micro design
    None
    Micro material
    Micro light
```

## 3. Browser prototype

New route:

```text
frontend/design-lab/work-unit-grammar-customizable.html
frontend/design-lab/work-unit-grammar-customizable.css
frontend/design-lab/work-unit-grammar-customizable.js
```

Local URL:

```text
http://localhost:5173/design-lab/work-unit-grammar-customizable.html
```

Exact browser implementation target before documentation/routing commits:

```text
ac16df1bbcd456b63c042c28e52516679139bf32
```

Controls:

```text
Project scene / Category strip
Normal / Subtle shapes
None / Micro material / Micro light
Clean / Structured / Rich presets
Reduced motion
Reset preview
```

The prototype persists shape/surface preference through browser-local storage only. This demonstrates preference continuity but does not select production persistence architecture.

## 4. Important conceptual change

The visual-grammar design objective is no longer necessarily:

```text
select one universal winner among every attractive visual mechanism
```

It can instead become:

```text
freeze semantic invariants
identify safe configurable visual dimensions
design strong defaults and presets
let the user choose among approved combinations
```

This allows previously competing visual candidates to become orthogonal presentation choices.

## 5. Persistence architecture remains open

Plausible later hierarchy:

```text
user appearance profile
    global personal default

project appearance override
    optional per-project setting

semantic project state
    independent
```

Not yet promoted:

```text
account synchronization
per-project precedence contract
team/shared-project behavior
settings import/export
additional configurable dimensions
whether category marker vocabulary itself may vary
```

## 6. Promotion audit

The user-configurable appearance principle has strong product-owner support and an executable browser proof now exists, but production promotion is premature until the configurator itself receives human browser review.

Therefore:

```text
product direction           PRESERVED / ACTIVE
browser proof               IMPLEMENTED
human configurator review   OPEN
production persistence      UNSELECTED
production /cockpit         UNCHANGED
```

## 7. Exact continuation

```text
1. pull v1-cockpit-design-exploration
2. open http://localhost:5173/design-lab/work-unit-grammar-customizable.html
3. switch Normal <-> Subtle shapes
4. switch None <-> Micro material <-> Micro light
5. try Clean / Structured / Rich presets
6. verify semantic category markers stay stable while appearance changes
7. verify the choices feel like one coherent product rather than unrelated themes
8. verify Project scene and Category strip both remain readable
9. human reviews whether this configurability model should become a durable Cockpit product requirement
10. only after that review decide whether to promote the principle into a foundation/specification and design production settings persistence
11. keep production Cockpit untouched
```
