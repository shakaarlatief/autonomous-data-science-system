# Research 002: Primary Project Cockpit Interface Concept

**Date:** 2026-08-20  
**Status:** Active design exploration, not an accepted interface specification  
**Scope:** Primary active-work interface for an Autonomous Data Science System project  
**Design session:** 02  
**ChatGPT project:** Autonomous Data Science System  
**Session title:** 02 - Methodological Brain & Knowledge Units

## 1. Why this exploration exists

The first professional frontend spike successfully demonstrated useful project views such as Overview, Data, EDA, methodological guidance, and Decisions & History.

Human review identified an important missing product layer.

The current screens are primarily project views, inspectors, records, and dashboards. They are useful and should remain extensive, but they are not yet the place where the user feels that they are actively working with the Autonomous Data Science System itself.

The product needs a primary immersive work surface, provisionally called the **Project Cockpit** in this memo.

The name is descriptive only. The system itself may receive a separate product/persona name later.

The desired role of this surface is:

```text
open project
    -> communicate intent and inputs to the system
    -> see the project take shape
    -> understand what the system is doing and why
    -> navigate the evolving analytical process spatially
    -> inspect generated work and evidence
    -> answer questions / approve consequential actions
    -> redirect or extend the investigation
    -> continue until a defensible project result emerges
```

This should feel like the main operating environment rather than another dashboard page.

---

## 2. Relationship to the current frontend

The current frontend is not discarded.

It should become the project's deep inspection and record layer:

```text
Cockpit
    primary active-work surface

Overview
    project state summary

Data
    dedicated data inspection

EDA
    dedicated exploratory analysis

Validation / Features / Models / Experiments / Evaluation
    specialist work and inspection views

Decisions & History
    rationale, provenance, event history

Report
    synthesis and publication
```

The Cockpit and specialist pages therefore have different jobs.

The Cockpit answers:

```text
Where are we?
What is happening now?
What should happen next?
What has branched or become blocked?
What does the system need from me?
Where can I intervene?
```

The specialist views answer:

```text
Show me this object or analytical area in depth.
```

---

## 3. External interface patterns worth learning from

This exploration should learn patterns from existing products without copying any product wholesale.

### Dataiku Flow

Dataiku represents a project's connected datasets, transformations, models, and other objects as a Flow. It uses nodes, edges, a visual grammar, and zones that can represent phases and can be collapsed as complexity grows.

Useful lessons for ADS:

```text
project complexity benefits from a navigable spatial map
visual grammar can communicate object type quickly
zones can represent stages without making every object identical
collapse / focus mechanisms are necessary for large projects
```

ADS should not copy Dataiku's data-pipeline semantics directly because the ADS methodological process also contains Questions, Findings, Decisions, uncertainty, loops, and human interaction.

### KNIME workflow editor

KNIME treats discrete operations as nodes connected into workflows and makes execution state visible.

Useful lessons:

```text
small visual units can make complex work understandable
connections should have explicit meaning
execution status can be visible directly on the work map
users benefit from acting on a selected unit without leaving the map
```

ADS should avoid turning the entire data-science methodology into a manually authored low-code pipeline.

### Replit Project Editor

Replit's project editor combines conversation with an Agent, live project output, tasks, and other tools in one working environment.

Useful lessons:

```text
conversation can be a control surface rather than a separate chatbot product
agent work should be visible while it happens
work output and conversation can coexist without forcing constant navigation
background tasks need compact state and inspectability
```

ADS needs a richer methodological and analytical state model than a coding-agent workspace, but the interaction pattern is highly relevant.

### Hex

Hex projects use notebook cells as building blocks for querying, transforming, visualizing, and documenting analysis, with an AI agent integrated into the project.

Useful lessons:

```text
analytical work needs directly inspectable outputs, not only status cards
code, tables, charts, text, and controls can coexist in one project surface
AI assistance is more useful when it understands the active project context
```

ADS should not reduce its project model to a notebook because the project contains broader methodological state, decisions, investigations, runs, and project history.

### React Flow

React Flow is a current implementation candidate for an interactive node canvas. It already provides pan, zoom, selection, custom React nodes, minimaps, controls, and related primitives.

It is an implementation possibility only. The cockpit interaction model must be designed before selecting the canvas library.

---

## 4. Core design hypothesis

The strongest current hypothesis is a hybrid between:

```text
visual project map
+ conversational system interaction
+ focused analytical artifact/work surface
```

not any one of these alone.

Conceptually:

```text
+--------------------------------------------------------------------+
| minimal global chrome                                               |
| project / command / status                              controls    |
+--------------------------------------------------------------------+
|                                                                    |
|                    PROJECT OPERATING CANVAS                        |
|                                                                    |
|   [Intent] -> [Data understanding] -> [Validation]                 |
|                  |                    |                             |
|                  +-> [Missingness]    +-> [Temporal cutoff]        |
|                  |                         |                        |
|                  +-> [Target study]        v                        |
|                                      [Baseline models]             |
|                                             |                      |
|                                             +-> [RF benchmark]      |
|                                                                    |
|      selected node can expand into a focused table/chart/work area |
|                                                                    |
|                                                   optional drawer  |
|                                                   evidence/system  |
+--------------------------------------------------------------------+
|  Ask / direct the system...   attach   command   approve   send    |
+--------------------------------------------------------------------+
```

The diagram is conceptual. It does not prescribe exact visual styling or topology.

---

## 5. Fixed stages plus dynamic work units

A purely fixed pipeline is too rigid for real data science.

A purely unconstrained graph is likely to become unreadable and makes it harder to understand project progress.

A promising compromise is:

```text
FIXED OR SEMI-FIXED STAGE ZONES
    provide orientation

DYNAMIC WORK UNITS
    appear as the project actually develops
```

Candidate stage backbone:

```text
Intent & framing
Data acquisition / understanding
Exploration & data quality
Validation design
Feature / representation work
Modeling
Evaluation & robustness
Synthesis / reporting
Deployment / monitoring when relevant
```

These are orientation zones, not a mandatory linear checklist.

A project may:

```text
skip a zone
reopen an earlier zone
branch into several investigations
run work in parallel
block downstream work on an unresolved Question
return from evaluation to features or validation
```

This preserves the real non-linear character of data science.

---

## 6. What a dynamic block should mean

A visual block should not automatically equal a persisted domain object and should not automatically equal an agent.

The cockpit is a derived view over project state.

Candidate visual work units include:

```text
Stage anchor
Active investigation
Question / blocker
Run or execution bundle
Evidence / finding milestone
Decision point
Artifact / result
```

However, showing every persisted Question, Finding, Evidence object, Run, and relation as an individual node would recreate the graph-overload problem already rejected elsewhere in the architecture.

Therefore:

```text
project objects
    -> view projection / grouping
    -> bounded set of cockpit work units
```

The cockpit should communicate the active project structure, not expose the whole database graph.

---

## 7. Conversation should be native to the cockpit

The system should feel like something the user works with directly.

The current hypothesis is a persistent composer anchored to the cockpit rather than a permanently dominant traditional chat column.

The user should be able to say things such as:

```text
Here is my dataset and the business objective.

Why is temporal validation blocking us?

Investigate the missing values first.

Skip Random Forest for now and explain the consequence.

Open the evidence behind this Finding.

Compare the two validation strategies.
```

The system can answer through a combination of:

```text
short conversational response
project-map change
new Question / investigation
opened artifact
approval request
highlighted dependency
new Finding or Decision candidate
```

This is important. A response from the system is not always best represented as prose in a chat transcript.

---

## 8. From empty project to active project

The empty cockpit should make the system's purpose obvious.

Possible initial experience:

```text
                  New data-science project

        What are you trying to understand or predict?

        [ Describe the objective, context and constraints... ]

        + Add data     + Connect source     + Add documents

                         Start project
```

After input:

1. The system identifies missing project-intent information.
2. Clarifying Questions appear naturally in the interaction surface.
3. Once framing is sufficient, the first project map materializes.
4. Data is represented as a real project input/artifact.
5. The current methodological horizon produces candidate work.
6. The map grows only as justified work becomes relevant.

The experience should visually communicate that the system is constructing and maintaining a real project, not merely answering messages.

---

## 9. Focus mode inside the cockpit

Clicking a work unit should not always navigate to a different page.

A selected work unit could expand into a focused work surface while the surrounding project map remains available as context.

Examples:

```text
Missingness investigation
    -> table + missingness plot + interpretation + actions

Temporal validation
    -> cutoff visualization + candidate splits + methodological rationale

Model comparison
    -> experiment matrix + metrics + calibration / threshold views

Question
    -> why unresolved + evidence needed + downstream effects

Decision
    -> options + rationale + evidence + approval
```

A separate specialist page should remain available when the user wants the full deep view.

---

## 10. Immersive layout requirement

The cockpit should intentionally use much more of the screen than the current project pages.

Candidate rule:

```text
Cockpit route
    immersive full-window mode
    very small persistent global chrome
    navigation collapsible or icon-only
    inspector drawers closed until needed
    conversation composer integrated into the canvas

Specialist routes
    normal project navigation shell
```

This directly addresses the requirement that the main working interface should feel like the entire application rather than one page placed between permanent sidebars.

---

## 11. Visual character should be explored deliberately

The first ADS frontend and the separate Interactive Regression Likelihood Explorer share a recognizable design grammar:

```text
Inter / system sans typography
white or near-white panels
slate text
blue / indigo accent
rounded cards
soft borders
subtle shadows
small uppercase eyebrow labels
```

That language is clean and useful, but it should not become an automatic default for every project.

The cockpit deserves a deliberate visual exploration from first principles.

Potential directions to test:

### Direction A: Precision Canvas

```text
large calm canvas
subtle technical grid / spatial depth
compact geometric work units
thin meaningful connectors
restrained color
strong focus and selection states
minimal surrounding chrome
```

### Direction B: Analytical Control Room

```text
more information-dense
persistent project status rail
active-stage focus
small live system activity indicators
artifact panes that dock into the canvas
strong keyboard / command-palette orientation
```

### Direction C: Living Project Map

```text
stage zones as larger spatial regions
work units emerge and connect dynamically
completed areas visually recede
active and blocked work becomes prominent
zoom from project overview into detailed investigation
```

The likely final solution may combine A and C with selected control-room behavior from B.

Avoid copying the current rounded-card dashboard visual language by default.

---

## 12. Important semantic distinction: process map versus lineage graph

ADS will eventually contain several graphs that must not be confused.

```text
PROJECT PROCESS / REASONING MAP
    where the investigation is going

DATA / ARTIFACT LINEAGE
    how datasets and artifacts derive from one another

KNOWLEDGE RELATION GRAPH
    reusable methodological relationships

EVENT HISTORY
    what happened over time
```

The Cockpit should primarily visualize the first.

It may reference the others, but combining all four into one graph would be misleading and visually unmanageable.

---

## 13. Main open design questions

The following should be resolved through mockups and interaction testing rather than prose alone:

```text
1. Should stage orientation run horizontally, vertically, or spatially?
2. Are stage zones always visible or only when zoomed out?
3. How much freedom should the user have to rearrange blocks?
4. When does a project object become its own visible work unit?
5. How do loops and reopened work appear without visual clutter?
6. Where does the conversational transcript live when the composer is minimal?
7. How should system activity be shown while autonomous work is running?
8. How does approval appear without interrupting low-risk work?
9. How does a selected node become a real analytical work surface?
10. How do we preserve keyboard accessibility in a spatial canvas?
11. What visual language makes the cockpit distinctive without becoming decorative?
```

---

## 14. Recommended next design step

Do not immediately implement one graph concept as production UI.

The next bounded frontend exploration should produce several realistic cockpit compositions using the same representative ADS project state.

At minimum compare:

```text
Concept 1
stage-zone project map + bottom system composer

Concept 2
conversation / activity lane + central dynamic project map

Concept 3
project map + expandable analytical focus surface
```

Each concept should show the same scenario:

```text
Customer Churn Prediction
prediction moment unresolved
missingness investigation awaiting approval
chronological validation selected
baseline model completed
Random Forest benchmark deferred
```

Then evaluate:

```text
Does the project feel alive?
Can the user tell where they are?
Is system reasoning understandable?
Is there enough room for real analytical work?
Does conversation feel integrated rather than bolted on?
Can complexity grow without becoming a spaghetti graph?
Does the interface feel distinctive and premium?
```

Only after that visual/interaction comparison should the Cockpit implementation stack and node-canvas library be selected.

---

## 15. Current design conclusion

The strongest current direction is not a dashboard, a normal chatbot, a notebook, or a low-code workflow editor by itself.

It is a **project operating canvas** in which:

```text
the user talks to the system
        +
the system changes a visible project structure
        +
analytical work opens directly inside that structure
        +
Questions / blockers / approvals remain explicit
        +
specialist pages provide deep inspection when needed
```

This direction is promising but remains intentionally unaccepted until visual concepts and human review make it concrete.
