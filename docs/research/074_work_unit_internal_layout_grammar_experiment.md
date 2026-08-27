# Research 074: Expanded Work-Unit Internal Layout Grammar Experiment

**Date:** 2026-08-27  
**Status:** Active Phase-C information-design experiment  
**Scope:** Closes the contextual-detail expansion geometry question after explicit human selection of X5 without context recession, then opens a bounded comparison of internal information layouts inside the accepted balanced two-axis expanded work unit.  
**Authority:** Research evidence only. This memo does not freeze the final work-unit semantic schema, provenance model, evidence representation, command surface, deep-focus transition or production component architecture.

## 1. Human acceptance closing the geometry question

Research 073 compared:

```text
X0  Compact Control
X1  Vertical Drawer
X2  Right Sidecar
X3  Attached Sheet
X4  Wide Split Card
X5  Context Lens
X6  Layered Reveal
X7  Peek Rail
X8  Inspector Dock
```

The project owner narrowed the final comparison to X4 versus X5 and then explicitly separated X5's shape from its original surrounding-context recession behavior.

The accepted result is:

```text
X5 BALANCED TWO-AXIS EXPANSION
    width   390px
    height  210px
    one integrated work-unit object
    grows in width and height
    surrounding project map remains at normal salience
    no X5-specific context recession
```

Human decision:

```text
I choose X5 without the context recession.
```

The original context-recession mechanism is not promoted as part of contextual expansion. It remains historical design evidence and may still inform a different future interaction layer if justified.

Accepted refined browser route:

```text
http://localhost:5173/design-lab/work-unit-detail-expansion.html
```

The accepted X5 refinement is implemented through:

```text
frontend/design-lab/work-unit-detail-expansion-x5-accepted.css
frontend/design-lab/work-unit-detail-expansion-x5-accepted.js
```

Exact refined X5 implementation target:

```text
94bc1100b7388cc56497cafc03051ce326424a80
```

Production `/cockpit` remains untouched.

## 2. Why internal layout is now the next bounded question

The interaction hierarchy is now comparatively mature through the contextual-detail geometry layer:

```text
compact map work unit
    -> selected compact work unit
    -> X5 balanced two-axis contextual expansion
    -> full specialist workspace / deep focus
```

The next unresolved question is no longer primarily the outside shape. It is:

```text
INTERNAL LAYOUT GRAMMAR
    once the selected work unit expands,
    how should richer contextual information be organized
    so the work unit remains quickly scannable and still feels like a map object?
```

This is deliberately separated from the final semantic schema.

## 3. Held controls

```text
G4 Adaptive Hybrid world
H4 hover/world response
Reduced in-box resting light
scientific category markers
P7 Neutral Tag + Tone disposition
accepted operational-status carrier
BLOCKED sharper compact ring
FAIL smoother circular compact ring
A3 Signal Bars for HIGH attention
SEL2 Corner Brackets for persistent selection
X5 balanced 390 x 210 two-axis expansion
NO surrounding-context recession
```

## 4. Provisional information payload

Every layout receives the same six pieces of placeholder information:

```text
Purpose
Constraint
Evidence
Next action
Blocking cause
Recent activity
```

Representative fixture values:

```text
Purpose          Profile production missingness
Constraint       Blocked by unresolved target definition
Evidence         Schema + missingness profile
Next action      Resume after blocker clears
Blocking cause   Resolve target definition
Recent activity  Missingness profile generated
```

These are comparison fixtures only. They do not freeze the final work-unit schema, required fields, provenance structure or C5 semantics.

## 5. Candidate internal layouts

```text
L0  Flat Fields
L1  Structured Grid
L2  Narrative Stack
L3  Summary + Rail
L4  Action First
L5  Dependency Path
L6  Evidence Center
L7  Module Cards
L8  Balanced Instrument
```

### L0 Flat Fields
Six equal fields in a neutral two-column grid. This is the hierarchy-light control.

### L1 Structured Grid
A compact matrix with mild internal grouping. Tests whether modest chunking improves scanability without imposing a strong narrative.

### L2 Narrative Stack
One vertical reading sequence. Tests clarity for longer prose at the cost of density.

### L3 Summary + Rail
Primary context stays in a wider main column while supporting evidence/action/activity occupy a narrower rail.

### L4 Action First
The next action receives the strongest internal placement. Tests an operationally oriented work-unit composition.

### L5 Dependency Path
Blocking cause, current constraint and next action form a compact process path, with supporting context beneath.

### L6 Evidence Center
Evidence occupies the visual center while other fields remain peripheral. Tests whether evidentiary grounding should visually dominate contextual inspection.

### L7 Module Cards
Each field becomes a small internal module. This deliberately tests strong chunking against the risk of turning the work unit into a miniature dashboard.

### L8 Balanced Instrument
Compact metadata, structured middle modules and a lower action strip produce a more explicitly hierarchical technical composition.

## 6. Browser implementation

Local route:

```text
http://localhost:5173/design-lab/work-unit-internal-layout.html
```

Files:

```text
frontend/design-lab/work-unit-internal-layout.html
frontend/design-lab/work-unit-internal-layout.css
frontend/design-lab/work-unit-internal-layout.js
```

Exact initial browser implementation target:

```text
871075bcda8ff812e1a96b18b442c803d5da7faf
```

The browser header is intentionally non-sticky so vertical comparison space remains available during long review sessions.

## 7. Practical scene

The practical scene holds the surrounding map at full salience and changes only the internal composition of the expanded work unit.

```text
selected node
    Investigation
    Current
    BLOCKED
    HIGH attention
    SEL2 selected
    X5 expanded

surrounding map
    visible
    normal salience
    not suppressed by expansion
```

Buttons L0-L8 switch only the internal layout.

## 8. Human review gate

Review:

```text
1. compare L0-L8 with outer geometry held constant
2. identify the fastest scan path for purpose, obstruction, evidence and next action
3. reject layouts that feel like miniature dashboards rather than expanded map objects
4. inspect robustness to longer text
5. inspect whether provenance/evidence could later expand naturally
6. inspect whether the layout still leaves room for future commands without forcing them now
7. prefer / reject / combine / refine
8. keep the final semantic field schema unfrozen
```

## 9. Still unfrozen

```text
final internal work-unit information schema
required versus optional fields
provenance/evidence presentation
blocking-cause representation inside expanded work units
recent-activity/history representation
selected-node command surface
multiple expanded work units
large-project collision avoidance
semantic zoom interaction
expansion persistence
transition from contextual detail to specialist workspace
URL state for selected / expanded / deep focus
production component architecture
```
