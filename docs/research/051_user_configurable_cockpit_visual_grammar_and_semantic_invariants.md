# Research 051: User-Configurable Cockpit Visual Grammar and Semantic Invariants

**Date:** 2026-08-26  
**Status:** Active Phase-C product-design evidence  
**Scope:** Preserves the human product decision that multiple positively reviewed Cockpit visual mechanisms should coexist as user-configurable appearance choices instead of forcing one universal visual treatment, and opens a browser proof of that architecture.  
**Authority:** Research/design evidence only. No production persistence contract or final settings architecture is promoted yet. Specification 008 remains the promoted Cockpit interaction architecture.

## 1. Human product decision

After selecting scientific category markers and positively reviewing both subtle true-shape boxes and optional micro-surface treatments, the project owner identified a stronger product model:

```text
these visual treatments do not need to be mutually exclusive global decisions
users should be able to configure how their Cockpit looks
```

Concrete examples explicitly requested:

```text
normal boxes
subtle differentiated box shapes
micro design enabled
micro design disabled
```

The motivation is product-level rather than experimental convenience. ADS is intended to be a professional working environment for a user's own data-science project, so controlled visual personalization is a legitimate part of owning that environment.

## 2. Architectural interpretation

The Cockpit should distinguish:

```text
SEMANTIC PROJECT MODEL
    what a work unit is
    project disposition
    runtime state
    importance / recommendation strength
    dependencies and evidence

from

PRESENTATION PROFILE
    box-shape treatment
    optional micro-surface treatment
    optional decorative richness
    other future safe appearance preferences
```

This allows multiple attractive designs to coexist without weakening methodological or project semantics.

## 3. Semantic invariants

Configurability must not turn semantic meaning into an arbitrary theme choice.

Current invariants for the prototype are:

```text
scientific category-marker mapping remains stable
    Question        circle
    Investigation   square
    Validation      triangle
    Model           diamond
    Evaluation      plus

Reduced in-box resting light remains the held preferred baseline
project category/state/runtime/importance data remain unchanged
accessibility constraints remain authoritative
appearance choices must not masquerade as semantic state
```

A later production design may expose more appearance choices, but semantic channels require explicit governance before becoming customizable.

## 4. Configurable presentation dimensions opened now

The browser proof exposes two independent appearance dimensions:

```text
Box shape
    Normal
    Subtle shapes

Micro design
    None
    Micro material
    Micro light
```

Because these are independent, the user can create combinations such as:

```text
normal + none
normal + micro material
normal + micro light
subtle shapes + none
subtle shapes + micro material
subtle shapes + micro light
```

This directly demonstrates the product-owner insight that previously competing browser candidates can instead become orthogonal user preferences.

## 5. Presets

The design-lab prototype also exposes convenience presets:

```text
Clean
    normal boxes + no micro design

Structured
    subtle shapes + no micro design

Rich
    subtle shapes + micro material
```

Presets are convenience compositions over the same underlying independent controls. They are not separate semantic modes.

## 6. Persistence model

The browser proof uses local browser persistence only:

```text
localStorage
    ads-design-lab-cockpit-appearance-v1
```

This is deliberately not a production storage decision.

A plausible production architecture to evaluate later is:

```text
user appearance profile
    global personal default

optional project appearance override
    project-specific visual preference

semantic project state
    independent from both
```

This hierarchy is attractive because a user may prefer one default visual style while choosing a different presentation for a specific project.

## 7. Browser proof

New design-lab route:

```text
frontend/design-lab/work-unit-grammar-customizable.html
frontend/design-lab/work-unit-grammar-customizable.css
frontend/design-lab/work-unit-grammar-customizable.js
```

Local URL:

```text
http://localhost:5173/design-lab/work-unit-grammar-customizable.html
```

Exact browser implementation target before routing/documentation updates:

```text
ac16df1bbcd456b63c042c28e52516679139bf32
```

The page provides:

```text
Project scene / Category strip
Normal / Subtle shapes
None / Micro material / Micro light
Clean / Structured / Rich presets
Reduced motion
Reset preview
```

Scientific markers and Reduced in-box light remain held beneath these appearance choices.

## 8. Product implications

If human browser review validates this interaction model, Cockpit visual-grammar work should no longer aim to collapse every positively reviewed mechanism into one mandatory final style.

Instead, the system can define:

```text
safe semantic invariants
+
approved configurable presentation dimensions
+
well-designed defaults/presets
```

This changes the design objective from:

```text
find the one universally correct box appearance
```

into:

```text
design a coherent appearance system
whose safe dimensions can be personalized
without changing project meaning
```

That is a materially stronger long-term product model.

## 9. Promotion boundary

Not yet frozen:

```text
production settings storage
account-level synchronization
per-project override precedence
which additional visual dimensions become configurable
whether category marker style itself may ever vary
light/dark theme relation to Cockpit appearance profiles
settings import/export
shared/team project appearance behavior
```

These should be resolved separately rather than inferred from the design-lab localStorage proof.

No production `/cockpit` file is changed.
