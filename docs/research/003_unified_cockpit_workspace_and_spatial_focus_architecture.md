# Research 003: Unified Cockpit Workspace and Spatial Focus Architecture

**Date:** 2026-08-20  
**Status:** Active design exploration, strongly preferred interaction direction after human review; not yet an accepted interface specification  
**Scope:** Professional/scalable implementation model for making the Project Cockpit the complete active-work surface, including deep Data/EDA/Validation/Modeling work without visible page-style navigation  
**Design session:** 02  
**ChatGPT project:** Autonomous Data Science System  
**Session title:** 02 - Methodological Brain & Knowledge Units

## 1. Why this research exists

Research 002 established the Project Cockpit as the missing primary active-work surface and proposed a living project map with dynamic work units, stage orientation, conversation, and focused analytical work.

Human review strongly confirmed one interaction in particular:

```text
click a work block
    -> smoothly zoom/focus into it
    -> perform the real work there
    -> return to the surrounding project context
```

A follow-up question then sharpened the design significantly:

> Should deep Data, EDA, Validation, Features, Modeling, Evaluation, and other specialist work also be possible inside this same spatial/focus experience, rather than eventually forcing the user to leave the Cockpit for a traditional page?

This memo answers that question from a product, frontend architecture, performance, state-management, accessibility, and scalability perspective.

The current conclusion is **yes**: this is technically normal and professionally achievable, and for ADS it is likely the stronger product direction, provided the implementation is structured as a persistent application workspace rather than one enormous always-mounted DOM/canvas tree.

---

## 2. Product conclusion

The preferred interaction model should now be:

```text
PROJECT COCKPIT
    primary complete active-work environment

    zoomed-out project map
        -> select work unit / stage / artifact
        -> spatial focus transition
        -> full analytical work surface
        -> deeper local focus when needed
        -> back / zoom out to project structure

OVERVIEW / DATA / EDA / VALIDATION / FEATURES / MODELS / ...
    still exist as direct inspectable entry points
    still useful for users who enter through the project-information/navigation side
    but are not mandatory escape hatches from the Cockpit
```

The key architectural distinction is therefore no longer:

```text
Cockpit = shallow
Specialist page = deep
```

It becomes:

```text
Cockpit = integrated active-work navigation and focus system
Specialist view = reusable analytical surface
```

The same specialist analytical surface can be opened in two contexts:

```text
1. inside Cockpit focus mode
2. directly from normal project navigation
```

This avoids duplicating functionality while preserving both interaction styles.

---

## 3. No full browser page reload is required

A modern React application can remain a single persistent application shell while changing major views, route state, and focus state without reloading the browser document.

The browser can retain:

```text
project shell
system connection
active run indicators
project-level state/cache
conversation context
navigation history
```

while the central workspace changes from:

```text
project map
```

into:

```text
data inspector
EDA workspace
validation designer
model comparison
finding/evidence inspection
report composition
```

and back again.

The user can experience this as a continuous spatial transition even if the application internally updates route state, mounts a different component tree, fetches additional data, or lazy-loads code.

This is an important separation:

```text
INTERNAL SOFTWARE NAVIGATION
    may use routes, components, data loaders, caches and lazy chunks

VISIBLE USER EXPERIENCE
    can remain one continuous cockpit with smooth spatial transitions
```

The implementation should exploit that separation rather than equating a URL/route change with a visible page change.

---

## 4. Recommended dual-access architecture

Each major analytical capability should have one reusable domain-facing frontend module.

For example:

```text
DataWorkspace
EDAWorkspace
ValidationWorkspace
FeatureWorkspace
ModelWorkspace
ExperimentWorkspace
EvaluationWorkspace
ReportWorkspace
```

These modules should not own the global navigation shell.

They can be hosted by different presentation contexts:

```text
CockpitFocusHost
    immersive, spatially entered work surface

SpecialistRouteHost
    normal project-navigation entry point
```

Conceptually:

```text
                         +--------------------+
                         |   DataWorkspace    |
                         +---------+----------+
                                   |
                    +--------------+--------------+
                    |                             |
                    v                             v
          CockpitFocusHost              SpecialistRouteHost
       smooth zoom / focus mode         direct Data navigation
```

The same principle applies to EDA, Validation, Models, Evaluation, and so on.

This gives ADS both of the experiences requested by the user:

```text
A. immersive active work
    enter Cockpit
    never need to visibly leave it

B. information/inspection navigation
    enter project through Overview/Data/EDA/etc.
    jump directly to the area wanted
```

Neither path is secondary in capability. They are alternative views onto the same underlying project state and analytical modules.

---

## 5. Spatial zoom should be a transition model, not literal permanent CSS scaling

A naive implementation would put every detailed analytical view physically inside a graph node and continuously CSS-transform the entire tree as the user zooms.

That is not the recommended architecture.

Problems with literal permanent scaling include:

```text
blurred text at fractional transforms
awkward browser focus behavior
large DOM trees remaining mounted
poor table/chart interaction inside transformed containers
complex clipping/stacking contexts
screen-reader confusion
harder responsive layout
harder independent scrolling
performance degradation as project complexity grows
```

The professional pattern should instead be a **spatial handoff**:

```text
1. user selects block
2. block is visually identified as transition origin
3. transition begins from the block's screen geometry
4. macro project canvas recedes / scales / fades
5. a normal full-resolution DOM focus surface becomes the active view
6. detailed workspace is interactive at normal scale
7. reverse transition returns to the same project location
```

So visually it feels like:

```text
small block
    -> expands / zooms toward user
    -> becomes full analytical workspace
```

but technically the destination is a properly laid-out application surface, not a tiny node magnified 800%.

This distinction is central to scalability.

---

## 6. Browser/platform support for smooth view transitions

Modern browser APIs now explicitly support animated transitions between DOM states in single-page applications.

The Web View Transition API supports same-document SPA transitions, including transitions between different element states and application views. Element-scoped transitions can limit animation to a subtree while other parts of the application remain interactive.

Relevant official references:

- MDN, View Transition API: https://developer.mozilla.org/en-US/docs/Web/API/View_Transition_API
- MDN, Using the View Transition API: https://developer.mozilla.org/en-US/docs/Web/API/View_Transition_API/Using
- MDN, element-scoped view transitions: https://developer.mozilla.org/en-US/docs/Web/API/View_Transition_API/Using_element-scoped

This means ADS does not need to invent the entire transition mechanism from low-level animation primitives. The application can use platform view transitions where supported and a controlled transform/opacity fallback where necessary.

The interaction must remain correct without animation. Animation is progressive enhancement, not domain state.

---

## 7. URL and navigation state should still exist

A seamless Cockpit should not become an opaque stateful canvas where browser back, refresh, bookmarking, or direct linking stops working.

The smooth interaction should still correspond to addressable application state.

Candidate conceptual URL states:

```text
/projects/churn/cockpit
/projects/churn/cockpit?focus=data
/projects/churn/cockpit?focus=data&column=tenure_months
/projects/churn/cockpit?focus=eda&view=missingness
/projects/churn/cockpit?focus=validation&investigation=temporal-split
/projects/churn/cockpit?focus=modeling&comparison=baseline
```

or nested route equivalents.

The exact syntax is not selected yet.

What matters is the contract:

```text
visual focus state
    <->
validated route/search state
```

Benefits:

```text
browser Back returns to previous focus
refresh reconstructs the same workspace
links can open a specific analytical state
user can share/bookmark an investigation
specialist direct routes can resolve to the same modules
history remains understandable
```

TanStack Router is currently a leading V1 candidate precisely because it supports typed/validated route and search state, inherited search parameters, and lazy route code. This remains candidate evidence rather than an accepted final selection.

Relevant official references:

- TanStack Router search params: https://tanstack.com/router/latest/docs/guide/search-params
- TanStack Router code splitting: https://tanstack.com/router/latest/docs/guide/code-splitting

---

## 8. The Cockpit must not keep the entire product mounted

The fact that everything can be *reachable* from the Cockpit does not mean everything should be simultaneously loaded and rendered.

Avoid:

```text
project map
+ every data table
+ every EDA chart
+ every experiment matrix
+ every report editor
+ full event history
+ every methodological detail
all mounted at once
```

Instead use bounded composition:

```text
persistent lightweight cockpit shell
    project map projection
    global composer
    compact run/approval state

selected focus workspace
    only current detailed analytical module mounted

background data/cache
    controlled by application query/cache layer

inactive heavy modules
    unmounted and/or code-split
```

React supports lazy component loading and Suspense boundaries so heavy analytical modules can be loaded only when needed. TanStack Router also supports route-level code splitting.

Official references:

- React APIs (`lazy`, `startTransition`): https://react.dev/reference/react/apis
- React Suspense: https://react.dev/reference/react/Suspense

This allows the Cockpit to feel continuous without turning the initial JavaScript bundle into the entire ADS application.

---

## 9. Large data must remain backend-driven

The Cockpit architecture does not change the production data rule already used in the frontend spike:

```text
large production dataset
    !=
load entire dataset into browser memory
```

A focused Data workspace can use:

```text
server/backend pagination
streaming / incremental fetch
server-side filtering
server-side sorting where required
column projection
sampling / representative preview
virtualized rows/columns for already-loaded client windows
```

Virtualization reduces DOM size but is not a substitute for server-side data access when the dataset itself is too large for the browser.

TanStack's official virtualization guidance makes the same distinction: virtualization keeps the rendered DOM small, while genuinely large datasets still require server-side operations or incremental loading.

Reference:

- TanStack Table virtualization: https://tanstack.com/table/latest/docs/framework/react/guide/virtualization

Therefore a full Data workspace inside the Cockpit is production-compatible.

---

## 10. Charts and analytical surfaces can also live inside focus mode

The same architecture works for analytical visualization.

A selected EDA work unit might transition into:

```text
+------------------------------------------------------------------+
| EDA / Missingness                                                 |
|                                                                  |
| [Overview] [By variable] [By target] [Patterns] [Temporal]       |
|                                                                  |
|  large chart / matrix / table                                   |
|                                                                  |
|  interpretation                                                  |
|  methodological guidance                                        |
|  evidence / finding candidates                                  |
|                                                                  |
|  Ask system about this view...                                  |
+------------------------------------------------------------------+
```

This can be the exact same `EDAWorkspace` rendered through the direct EDA route.

The Cockpit transition does not constrain the analytical module's internal layout. Once focused, it may use almost the entire viewport.

---

## 11. Focus can be hierarchical, but depth must remain bounded and legible

A useful interaction hierarchy is:

```text
LEVEL 0
project map

LEVEL 1
stage / work-unit focus

LEVEL 2
detailed analytical mode

LEVEL 3
specific object/evidence/detail drawer when needed
```

Example:

```text
Project map
    -> Exploration & data quality
        -> Missingness investigation
            -> support_tickets pattern detail
```

The UI should preserve a lightweight spatial breadcrumb such as:

```text
Project / Exploration / Missingness / support_tickets
```

while still making the reverse motion feel like zooming back out.

Do not create infinite spatial nesting. Very deep object detail should use drawers, tabs, inspectors, or local navigation inside the focused workspace rather than endless nested zoom levels.

---

## 12. The map and the focused analytical surface should use different rendering regimes

This is a useful production boundary.

### Macro regime: project map

Optimized for:

```text
pan / zoom
selection
small bounded work units
stage regions
connectors
status
branching
project orientation
```

A node-canvas library such as React Flow may eventually be appropriate here, but is not selected yet.

### Micro regime: focused workspace

Optimized for:

```text
normal DOM layout
large tables
charts
forms
text
code/results when appropriate
scrolling
keyboard interaction
screen readers
responsive sizing
```

Do not force all detailed analysis into the canvas library's node rendering model.

Conceptually:

```text
canvas is the spatial navigator
focus host is the workbench
```

The transition makes them feel continuous.

---

## 13. State architecture required for this to remain professional

The Cockpit should not own all state in one giant React component.

Separate at least:

```text
DOMAIN / PROJECT STATE
    Questions
    Findings
    Decisions
    investigations
    runs
    artifacts
    methodological state
    persisted outside frontend component lifecycle

SERVER STATE / DATA CACHE
    datasets
    paginated rows
    statistics
    experiment results
    charts/data queries

ROUTE / VIEW STATE
    current focus
    selected variable
    selected investigation
    filter/sort/tab
    zoom/focus location where useful

TRANSIENT UI STATE
    hover
    open popover
    animation phase
    temporary selection gesture
```

A route transition should never be the source of truth for domain state.

Closing a focus surface should not delete work. Reloading the application should reconstruct meaningful view state from URL + project state rather than relying on one long-lived browser process.

---

## 14. Running work must survive visual navigation

A user may zoom from a running model investigation into Data, then to EDA, then back to the project map while execution continues.

Therefore:

```text
visual component lifecycle
    !=
run lifecycle
```

Long-running operations belong to the backend/application/runtime layer.

The frontend subscribes to or polls the authoritative run state and can remount a run view later.

This prevents a dangerous coupling in which unmounting a React component accidentally implies cancelling real work.

Cancellation must be explicit.

---

## 15. Conversation should follow focus context without losing project context

The persistent system composer becomes more powerful under this model.

At project-map level:

```text
"What should we investigate next?"
```

Inside Missingness:

```text
"Compare this pattern by target and signup cohort."
```

Inside a model comparison:

```text
"Why is this model better on ROC AUC but worse on calibration?"
```

The application can provide a bounded active-view context pointer to the system while preserving the broader project state outside the model call.

This fits the established scaling lesson:

```text
what the SYSTEM remembers
    !=
what every LLM call receives
```

The active visual focus can become one strong signal for context assembly without becoming the entire context policy.

---

## 16. Direct specialist navigation remains valuable

Keeping direct Data/EDA/etc. navigation is still useful even if the Cockpit can do everything.

Examples:

```text
user knows exactly what they want
    -> click Data

user opens a shared link from a colleague
    -> direct Model comparison state

user is reviewing rather than actively steering
    -> Overview / Decisions & History

user wants immersive project operation
    -> Cockpit
```

This is not duplication when both paths reuse the same underlying analytical modules.

The product can therefore support two complementary mental models:

```text
Cockpit
    project as a living process

Project navigation
    project as an inspectable information system
```

This combination is stronger than forcing every user task through only one navigation metaphor.

---

## 17. Accessibility and reduced motion are non-negotiable

A spatial interface can become inaccessible if animation is treated as the only way to understand navigation.

Requirements:

```text
keyboard-selectable work units
logical focus movement after transition
semantic headings in focused workspaces
browser back support
visible breadcrumb/path
screen-reader labels independent of spatial position
no information encoded only by animation
prefers-reduced-motion support
instant/fade fallback when motion is reduced
transition cancellation/skip safety
```

The final state must be identical whether the animation runs or not.

The browser View Transition API documentation itself notes accessibility/focus concerns that historically arise when old and new DOM states are simultaneously present, which reinforces keeping the transition boundary disciplined.

---

## 18. Performance strategy

A professional implementation should combine several independent controls rather than rely on one optimization.

```text
INITIAL LOAD
    code splitting
    lazy analytical modules
    small project-map projection

PROJECT MAP
    bounded visible nodes
    clustering/stage collapse
    avoid rendering full project object graph

DATA
    backend pagination/streaming
    virtualization where useful

CHARTS
    render only active/visible heavy charts
    downsample/aggregate when semantically valid

RUN STATE
    lightweight event/status updates
    detailed logs/results fetched on demand

TRANSITIONS
    transform/opacity or View Transition API
    short durations
    no layout-thrashing animation loops

CACHE
    explicit server-state cache lifecycle
    invalidate from authoritative project events
```

This makes the architecture scale by keeping the user's **reachable space large** while keeping the **currently rendered space bounded**.

That is the main technical idea.

---

## 19. Important non-goals

The new direction does not imply:

```text
one React component for the whole product
one giant graph containing every project object
all pages permanently mounted
all data in browser memory
all code downloaded on first load
literal infinite zoom into arbitrary DOM
removing URLs/history
making animation required for correctness
forcing every user to enter through the Cockpit
```

Those would undermine scalability.

---

## 20. Preferred product architecture after this review

The strongest current product hypothesis is now:

```text
                         AUTONOMOUS DATA SCIENCE SYSTEM

              +--------------------------------------------+
              |              PROJECT COCKPIT               |
              |                                            |
              |  living project map                        |
              |       -> spatial focus transition          |
              |       -> complete analytical workspace     |
              |       -> system interaction                |
              |       -> evidence / decisions / approvals  |
              |       -> smooth return to project context  |
              +--------------------------------------------+
                               |
                     same project modules/state
                               |
       +----------+----------+----------+----------+----------+
       |          |          |          |          |          |
     Overview    Data       EDA     Validation   Models    History ...
       direct inspectable/navigation entry points when desired
```

The Cockpit should be capable of completing essentially all normal project work without a visible traditional page jump.

Direct specialist navigation remains because it is useful, not because the Cockpit is incapable of depth.

---

## 21. Design implication for upcoming mockups

The next Cockpit concepts should no longer stop at a shallow expanded block.

At least one realistic concept must demonstrate the full transition chain:

```text
project map
    -> click Missingness investigation block
    -> spatial expansion
    -> full EDA-quality missingness workspace
    -> select support_tickets
    -> inspect detailed table/chart/evidence
    -> ask system a scoped question
    -> produce/update a Finding candidate
    -> zoom back out
    -> project map reflects the resulting state
```

A second example should demonstrate Data:

```text
project map
    -> Data understanding block
    -> full Data workspace
    -> select variable
    -> filter/sort/paginate rows
    -> inspect semantic role / missingness
    -> return to map
```

This is necessary to verify that the Cockpit is a real work environment rather than an attractive project overview.

---

## 22. Promotion status

This research does **not** yet select:

```text
React Flow
View Transition API as mandatory implementation
exact URL schema
exact animation library
exact stage geometry
exact cockpit component hierarchy
```

It does establish a much stronger design requirement/hypothesis:

```text
The primary ADS Cockpit should be architected as a persistent, immersive,
route-addressable active-work environment in which deep specialist analytical
surfaces can be entered and exited through smooth spatial focus transitions,
while the same analytical modules remain directly accessible through the
normal project-navigation/inspection interface.
```

This should be tested in the next frontend design spike before promotion into an accepted interface specification.
