# Checkpoint 257: Canonical Cockpit Review Route Normalized

**Date:** 2026-08-29  
**Status:** Current human-review checkpoint  
**Checkpoint class:** CONTINUITY / ROUTING / WHOLE_PRODUCT_INTEGRATION  
**Project stage:** V1 next-generation Project Cockpit advanced whole-product design exploration on the source-faithful integrated substrate  
**Interaction environment:** ChatGPT  
**Interaction session:** `chatgpt-09`  
**Conversation title:** `09 - Project Cockpit Design Exploration`

## 1. Boundary transition

Checkpoint 256 established the current human-review surface:

```text
structural visible Conversation WorkUnit spacing
current compact flat Project Grid rail control set
current-process Focus unchanged
Checkpoint 255 live topology compass carried forward
```

That surface was still reached through the historical study query:

```text
?edge=angled
```

The project owner requested that the current changes become available on the normal Cockpit link without the historical query suffix.

This checkpoint performs that routing/integration normalization only. It introduces no new visual or semantic design decision.

## 2. Canonical current review route

The current Cockpit human-review route is now:

```text
http://localhost:4173/design-lab/cockpit-reintegration.html
```

No query parameter is required.

The plain route mounts the same current flat rail and Checkpoint 256 corrections that were previously reached through `?edge=angled`.

## 3. Historical routes remain isolated

Historical study routes remain available for regression evidence and design history:

```text
?edge=angled
?edge=hinge
?edge=stack
?edge=console
?rail=blade
?rail=deck
?rail=float
```

The current canonical loader does not mount the current flat rail on top of explicit `edge=` or `rail=` study routes.

An internal regression-only route is also used:

```text
?edge=none
```

Its purpose is to preserve deterministic tests of accepted source mechanisms that intentionally depend on the earlier shell controls. It is not a product route, not a human-review route and not a design candidate.

## 4. Why the test split is necessary

Making the current rail canonical correctly hides two controls that Checkpoint 256 removed from the current rail composition:

```text
Expand selected WorkUnit
Hide project HUD
```

Several older regression tests intentionally exercise those underlying mechanisms and historical shell capabilities. Running those tests against the current shell would conflate:

```text
mechanism preservation
with
current shell composition
```

The route split preserves both truths:

```text
canonical no-query route
    verifies the current human-review Cockpit exactly as the user sees it

?edge=none regression substrate
    verifies historical/accepted mechanisms without requiring them to remain visible in the current rail

explicit edge/rail study routes
    preserve historical spatial-rail experiments without contamination from the current default rail
```

No deterministic coverage was removed.

## 5. Deterministic validation

Implementation target:

```text
59e5d19b310c4cc89fefc46fb4d116d67bdeefd5
```

Complete Cockpit fidelity workflow:

```text
workflow run  33236756483
job           99058967008
result        SUCCESS
browser tests 68 / 68 passing
```

The successful run proves simultaneously that:

```text
the plain canonical route mounts the current Checkpoint 256 rail
Conversation structural spacing passes on the plain route at desktop width
the same spacing passes on the plain route at narrow width
Fullscreen is present on the current plain-route rail
Expand selected WorkUnit is absent from the current plain-route rail
Hide project HUD is absent from the current plain-route rail
historical source-mechanism regression tests still pass
historical Gen 1 and Gen 2 rail-study routes remain isolated and functional
all prior source-faithful Cockpit regression checks remain green
```

## 6. Current product-design gate is unchanged

Checkpoint 257 changes routing, not the design question.

The human-review task remains:

```text
1. inspect actual visible Conversation Boxes spacing
2. inspect the current flat right-side Project Grid rail control set
```

Current-process Focus remains explicitly unchanged and working.

The live Checkpoint 255 topology compass remains carried forward unchanged.

## 7. Preservation boundary

The canonical current link is now the normal no-query route.

Do not reintroduce `?edge=angled` as the current human-review instruction. It remains historical implementation/study plumbing only.

Production `/cockpit` remains untouched.
