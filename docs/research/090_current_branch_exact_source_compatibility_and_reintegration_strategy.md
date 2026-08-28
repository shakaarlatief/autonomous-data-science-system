# Research 090: Current-Branch Exact Source Compatibility and Reintegration Strategy

**Date:** 2026-08-28  
**Status:** Active reintegration evidence  
**Scope:** Records the result of comparing every manifest-bound historical source file against the current `v1-cockpit-design-exploration` branch and defines the safest composition strategy for the replacement holistic Cockpit.  
**Authority:** Integration-process evidence under Checkpoint 251. It does not create new product-design selections.  
**Interaction session:** `chatgpt-09`  
**Conversation title:** `09 - Project Cockpit Design Exploration`

## 1. Why this check matters

Exact historical provenance is necessary but does not by itself tell the integrator whether the current branch copy of a source file is still the exact accepted artifact or has changed since the manifest target.

Before beginning reintegration, the validator was extended to compare:

```text
historical accepted blob
    <integration SHA>:<path>

against

current branch blob
    HEAD:<path>
```

The comparison is intentionally informational. A later changed file could be a compatible refinement, but it would require deliberate review rather than being assumed equivalent.

## 2. Full-history result

GitHub Actions run:

```text
33156867031
```

Head under test:

```text
87bdbf2c82825fc17e5dbd9d8f9f803421f6372f
```

Result:

```text
Cockpit implementation manifest: PASS
entries=23 required=19 non_promotable=4
exact historical source verification: PASS
current-source compatibility: exact=84 diverged=0 absent=0
```

Therefore:

```text
ALL 84 declared historical source files
    exist on the current branch
    AND
    are byte-identical to their manifest-bound historical accepted blobs
```

No accepted source file currently requires historical reconstruction or a compatibility rebinding.

## 3. Important consequence

The safest replacement-integration strategy becomes materially simpler:

```text
DO NOT duplicate accepted source files into a new approximate implementation.

Instead:
    import/reuse the existing current-branch source files directly
    because CI proves they are the exact accepted historical blobs
```

This provides both implementation fidelity and repository maintainability.

The exact accepted artifact remains one source file rather than being copied into a second source family that could drift.

## 4. Composition strategy

The replacement holistic browser should use existing accepted source artifacts as dependencies wherever technically possible.

Preferred mechanisms:

```text
CSS
    import/link exact accepted stylesheets directly

DOM grammar
    use the exact accepted class/data-attribute contract

behavior
    execute accepted scripts directly where their initialization contract is reusable
    otherwise port the smallest exact behavior unit with explicit provenance comments

whole-product state orchestration
    new integration glue allowed only where no accepted whole-product controller exists
    keep that glue semantically thin and explicitly provisional
```

The failed `cockpit-integrated-baseline.*` family remains excluded.

## 5. First reintegration slice

The first replacement implementation slice should establish the source-faithful Project Grid substrate before Conversation and specialist-workspace composition are added.

It should directly compose:

```text
M02 G4 world
M03 canonical WorkUnit + H4
M04 scientific markers
M07/M06 connector semantic presentation where applicable
M08 P7 disposition
M12 BLOCKED/FAIL operational carriers
M13 A3 attention
M14 SEL2 selection
```

The current branch already contains an especially useful exact composite source:

```text
frontend/design-lab/work-unit-selection-state.html
frontend/design-lab/work-unit-selection-state.js
```

with the accepted stylesheet stack for G4/H4, appearance, disposition, operational condition, A3 and SEL2.

The replacement browser should reuse this grammar rather than synthesize a new WorkUnit.

## 6. Next layers after the Project Grid substrate

Once the source-faithful map layer is mounted and verified:

```text
X5 contextual expansion
    exact M15 source family

Z7 Deep Dive
    exact M17 source family

Quiet Graphite Conversation Workspace
    exact M19 source family

scope / Boxes-Text / A6
    exact M20 source family

Grid/X5/Deep-Dive access and state restoration
    exact M21 source family

Specification 008 shell capabilities
    exact M01 behavior requirements
```

Each layer should be integrated without changing the already-verified lower layer unless the manifest explicitly permits the adaptation.

## 7. Fidelity discipline

The key rule entering implementation is now:

```text
current branch accepted source
    == exact historical source

therefore

reuse current accepted artifact directly
    > copy and reinterpret it
    > redraw it from prose
```

A new source file is justified only for integration state orchestration, unresolved shell glue, or an adaptation that cannot be expressed by composing the accepted source directly.

Such code must identify itself as integration glue rather than a new accepted visual specification.
