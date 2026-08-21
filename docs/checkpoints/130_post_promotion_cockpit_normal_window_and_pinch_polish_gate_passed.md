# Checkpoint 130: Post-promotion Cockpit normal-window and pinch polish gate passed

**Date:** 2026-08-21  
**Status:** Automated implementation gate passed; short real-browser human retest remains open  
**Active branch:** `v1-runtime-bakeoff`  
**Design session:** 03  
**ChatGPT project:** Autonomous Data Science System  
**Session title:** 03 - Project Cockpit & V1 Integration

## What changed

A post-promotion human review of Specification 008 found two bounded implementation issues rather than a new architecture problem:

```text
1. Jump/search was collision-safe in true fullscreen but could overlap the
   persistent composer in a shorter normal Chrome window.

2. Native pinch was substantially smoother than earlier versions but still
   changed project scale too little per natural physical gesture.
```

The tiny occasional pinch hitch remains explicitly deferred non-blocking polish.

## Implemented repair

### Jump/search

The palette now measures the actual rendered composer boundary while open and re-clamps on resize, fullscreen changes, and composer resize events.

Invariant:

```text
palette bottom + safety gap <= actual composer top
```

The results area remains internally scrollable, so shorter windows reduce the visible result list rather than allowing it to enter the composer region.

CSS uses `100dvh` as a fallback; rendered composer geometry is authoritative when available.

### Pinch responsiveness

```text
PINCH_SENSITIVITY
0.0018 -> 0.0024
```

No change was made to frame coalescing, delta bounding, exponential scaling, or gesture anchoring.

## Strengthened regression coverage

The browser gate now explicitly tests the user's failure class by opening Jump/search at `1600x900`, resizing to `1600x720`, requiring a clear composer gap, scrolling to the last result, and selecting it successfully.

The pinch regression now expects the deliberately faster response while still bounding one-gesture scale movement and checking anchor stability.

## Validation

Implementation head:

```text
ae83e920b3fa43ee8242bdb1ca2640d23a474c71
```

V1 frontend spike:

```text
run 167 / 32503861255

Ubuntu build + unit tests                  PASS
Windows build + unit tests                 PASS
Chromium interaction/accessibility         PASS
controlled direct-view visual regression   PASS
normal-window Jump re-clamp regression      PASS
faster anchored pinch regression            PASS
```

The concurrent V1 runtime bakeoff workflow also remained green:

```text
run 20 / 32503861259

Direct-call control Ubuntu                  PASS
Direct-call control Windows                 PASS
OpenAI Agents core Ubuntu                   PASS
OpenAI Agents core Windows                  PASS
existing Python suite                       PASS
```

## Architecture status

Specification 008 remains accepted and is not reopened.

This checkpoint does **not** select or freeze:

```text
final pinch sensitivity or zoom range
remaining tiny pinch-hitch polish
final responsive breakpoint constants
final Jump/composer styling
final gesture library
```

The repair strengthens the already-promoted interaction architecture at the implementation/product-polish level.

## Runtime-track status at this boundary

The runtime bakeoff remains the main active execution track.

Checkpoint 129 already established the executable direct-call control. Since then, the OpenAI Agents SDK 0.19.4 core candidate has passed its deterministic cross-platform core subgate, while Research 011 records an important released-package/documentation mismatch around `agents.testing.ScriptedModel`.

No runtime is selected.

Outstanding OpenAI candidate gates remain:

```text
AR-03 current MCP integration
AR-08 cancellation and bounded timeout
AR-09 controlled failure/retry behavior
AR-11 normalized observability
```

## Exact next actions

```text
1. human frontend retest:
       normal-window Jump/search collision
       fullscreen non-regression
       faster real-trackpad pinch feel

2. in parallel/after that, continue the runtime bakeoff:
       OpenAI AR-03 / AR-08 / AR-09 / AR-11
       then compare complete OpenAI evidence with direct-call control
       then implement LangGraph durability comparator if still decision-relevant
```

Primary supporting research:

```text
docs/research/012_post_promotion_cockpit_normal_window_and_pinch_sensitivity_review.md
```