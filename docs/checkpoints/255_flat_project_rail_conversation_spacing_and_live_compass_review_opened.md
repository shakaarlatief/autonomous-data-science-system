# Checkpoint 255: Flat Project Rail, Conversation Spacing and Live Compass Review Opened

**Date:** 2026-08-28  
**Status:** Current human-review checkpoint  
**Checkpoint class:** CONTINUITY / PRODUCT_DESIGN / WHOLE_PRODUCT_CORRECTION  
**Project stage:** V1 next-generation Project Cockpit advanced whole-product design exploration on the source-faithful integrated substrate  
**Interaction environment:** ChatGPT  
**Interaction session:** `chatgpt-09`  
**Conversation title:** `09 - Project Cockpit Design Exploration`

## 1. Boundary transition

Checkpoint 254 opened review of a resting angled right-side rail.

Human review then made three concrete corrections:

```text
Conversation WorkUnit boxes need more vertical breathing room.
The current right-side rail should keep its structure but become normal 2D.
The Deep Dive project-position compass needs a corrected container and real behavior.
```

Research 095 preserves the diagnosis, implementation and verification evidence.

## 2. Current live review state

Primary route:

```text
http://localhost:4173/design-lab/cockpit-reintegration.html?edge=angled
```

The `edge=angled` query remains only as historical study plumbing. The visible active rail on that route is now flat 2D.

Current review surfaces:

```text
Conversation
    Boxes mode uses deliberate 10px list separation

Project Grid
    compact right rail is flat 2D
    same real controls remain mounted
    optional clarity expansion still reveals labels

Deep Dive
    compact topology compass uses one coherent outer container
    mini-map is live and project-derived
    all actual WorkUnits and current relation links are represented
    selected source WorkUnit is highlighted
```

## 3. Rail disposition

```text
3D / angled resting treatment
    REJECTED for the current rail direction

flat compact rail
    CURRENT HUMAN-REVIEW CANDIDATE

clarity-only expansion
    RETAINED
```

Research 092, 093 and 094 remain preserved as design history. Their 3D/direct-manipulation ideas are not active requirements.

## 4. Compass semantic boundary

M17 remains authoritative for the held capability:

```text
compact topology compass retained
```

The new live implementation improves fidelity to the capability without changing ownership:

```text
Project Grid owns topology and selection.
Compass reads that state.
Compass does not create or mutate selection.
Compass does not become a second navigator.
```

The old hard-coded five-dot fixture is no longer treated as adequate integrated behavior.

## 5. Deterministic validation

Implementation target:

```text
10cf3cfd26553d95c3b786df6d3a14137a29767a
```

Complete browser gate:

```text
workflow run  33207377429
job           98971755372
result        SUCCESS
browser       65 / 65 passing
```

The new checks cover:

```text
normal 2D rail geometry
clarity expansion without project-state mutation
real rail controls and full-stage ownership
Conversation WorkUnit spacing
live compass node count
live compass relation count
current WorkUnit highlighting
selection-change synchronization
single-box compass hierarchy
compass/panel collision clearance
```

## 6. Accepted mechanisms unchanged

No held Phase-C semantic or interaction mechanism is revoked by these shell corrections.

In particular:

```text
G4/H4
scientific markers
E5 + D0-D3
P7
focus lens
runtime carriers
BLOCKED/FAIL distinction
A3
SEL2
X5
Z7
S0
Quiet Graphite
Boxes/Text
A6
Conversation access/coexistence
Specification 008 navigation/recovery/fullscreen capability
```

remain intact.

Production `/cockpit` remains untouched.

## 7. Current human-review gate

The next actor is the human reviewer.

Review in order:

```text
1. Conversation Boxes rail spacing
2. flat 2D right-side Project Grid rail
3. Deep Dive live topology compass
```

The next implementation step should be based on concrete visual reactions to those three corrected surfaces. Do not revive the 3D rail unless the project owner explicitly reopens that direction.
