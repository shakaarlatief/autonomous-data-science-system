# Specification 006: V1 Frontend Architecture and Visual Spike

**Date:** 2026-08-20  
**Status:** Candidate V1 product/frontend evaluation specification v0.1  
**Scope:** First professional ADS frontend shell, visual system, representative product screens, testing discipline, chart comparison, and frontend-agent transport feasibility  
**Authority:** Candidate evaluation contract subordinate to Foundation 021. No frontend framework, component foundation, charting library, desktop wrapper, or AG-UI adoption is accepted until the relevant spike evidence is reviewed and promoted explicitly.  
**Design session:** 02  
**ChatGPT project:** Autonomous Data Science System  
**Session title:** 02 - Methodological Brain & Knowledge Units

## 1. Purpose

The frontend is now a parallel V1 development track rather than an end-stage presentation task.

The immediate goal is not to build the entire application. It is to construct one visually serious product shell that tests whether the current project object model, methodological-navigation model, and user-control model can be presented clearly in a modern professional interface.

The spike must answer two different questions:

```text
TECHNICAL
Can the selected frontend architecture support the V1 application efficiently,
accessibly, testably, and without constraining future desktop/backend integration?

PRODUCT / VISUAL
Can the system's methodological state become understandable, useful,
and genuinely pleasant to work with in a polished analytical workspace?
```

A build that compiles but looks generic or communicates methodological state poorly is not a pass.

---

## 2. Leading V1 architecture hypothesis

The leading implementation hypothesis is:

```text
React
TypeScript
Vite
TanStack Router
TanStack Query
TanStack Table v9
shadcn/ui source-distributed components
custom ADS design tokens and visual language
Playwright for end-to-end / accessibility / visual checks
Vitest for frontend unit/component logic where useful
```

Current Node baseline for the spike should use the active Node 24 LTS line rather than the Node 26 Current line.

This is a hypothesis to validate, not an excuse to inherit default starter aesthetics.

### Why Vite is the leading hypothesis

ADS is currently:

```text
local-first
Python-backed
highly interactive
desktop/laptop oriented
not SEO dependent
not dependent on server-rendered public pages
potentially packageable in a desktop shell later
```

Vite directly supports React + TypeScript and is a natural SPA foundation. Current Tauri guidance also aligns well with Vite-style SPA frontends if native desktop packaging becomes justified later.

Next.js remains a capable alternative but is not a mandatory bakeoff candidate because ADS has no demonstrated requirement for its server-rendering/full-stack React layer. Introducing a second application server/runtime should earn its place through an actual requirement.

If the Vite spike exposes a requirement that Next.js or another meta-framework uniquely solves, reopen the comparison.

---

## 3. Frontend application boundary

The UI must not import persistence or agent-runtime implementation types directly.

Conceptually:

```text
ADS web application
        |
        v
FrontendDataSource
        |
        +-> TypedMockDataSource       first spike
        +-> HttpApiDataSource         later production service
        +-> future desktop/local bridge if justified

InteractionStream
        |
        +-> MockInteractionStream
        +-> native application stream
        +-> optional AG-UI adapter if validated
```

The first shell may be entirely powered by deterministic typed fixtures.

The important property is that replacing mocks with real backend calls should not require rewriting page/component semantics.

---

## 4. Representative product state

The mock corpus should not be generic dashboard data.

Use ADS-shaped representative state based on existing concepts:

```text
Project
    Telco-style binary prediction example or another neutral representative project

Project Intent
    objective
    target
    intended prediction/deployment context

Data
    several representative variables
    numeric / categorical / identifier / temporal examples
    missingness summaries

Methodological state
    Missing Data
    Temporal Validation
    Prediction-Time Feature Eligibility
    Class Imbalance
    Random Forest

Questions
    unresolved prediction moment
    production missingness question

Findings
    target imbalance finding
    temporal coverage finding

Recommendations
    REQUIRED / BLOCKING
    RECOMMENDED
    RELEVANT / APPLICABLE
    DEFERRED

Runs
    completed
    running
    waiting for approval

Decision
    validation strategy selection
```

No fixture should claim to be accepted methodological truth merely because it is rendered in the frontend. It is representative product state.

---

## 5. Visual direction

The first shell should establish the real product character.

### Desired feel

```text
premium professional analytical application
calm but information-rich
precise rather than decorative
modern without trend-chasing
strong typography
compact professional density
subtle depth
clear state hierarchy
excellent dark and light themes
```

### Avoid

```text
generic SaaS landing-page aesthetics
huge cards with little information
excessive rounded rectangles
random gradients
glassmorphism for its own sake
stock shadcn starter appearance
color used as the only status signal
legacy enterprise visual clutter
over-animation
```

The design must remain legible during serious analytical work for hours, not merely look impressive in a screenshot.

---

## 6. Design-system foundation

The spike should establish tokens before proliferating components.

Initial token families:

```text
color
    canvas / surface / elevated surface
    text primary / secondary / muted
    border / separator
    accent
    semantic status roles
    chart palette roles

typography
    UI sans
    data/monospace
    display / heading / body / caption
    numeric tabular treatment

spacing
    compact professional scale

shape
    radius scale
    borders
    elevation/shadow rules

motion
    duration
    easing
    reduced-motion behavior

layout
    sidebar widths
    context panel widths
    workspace max/min dimensions
    breakpoints
```

Do not hard-code one-off colors and spacing throughout components.

---

## 7. Component foundation hypothesis

shadcn/ui is the leading component-source workflow because it gives ADS ownership over component source and styling rather than making the design system an opaque package.

The underlying primitive choice should remain pragmatic.

Current shadcn releases support multiple primitive bases. The first spike may use the current Base UI path unless an accessibility or interaction requirement is better served by React Aria or Radix.

Do not create a three-way component-library benchmark without a concrete problem. Established accessible primitives should be reused rather than reimplementing focus management, dialogs, popovers, menus, or keyboard behavior.

The visual language remains ADS-owned regardless of primitive source.

---

## 8. Routing and URL-state hypothesis

TanStack Router is the leading hypothesis because ADS will likely need stateful analytical routes such as:

```text
/project/:projectId/data?dataset=...&columns=...&filter=...
/project/:projectId/eda?view=distribution&variable=tenure
/project/:projectId/history?objectType=finding
```

Typed and validated search parameters make views bookmarkable, refresh-stable, and shareable without turning all interface state into a global client store.

The spike should prove this with at least one data/EDA view whose selected object/filter state survives refresh and deep linking.

---

## 9. Server-state hypothesis

TanStack Query is the leading hypothesis for eventual API-backed server/application state.

It should own asynchronous fetch/cache/mutation lifecycle, not ADS domain semantics.

The spike should preserve the distinction:

```text
server/application state
    fetched/cached through Query

URL view state
    Router search params where appropriate

short-lived local UI state
    React/component state

ADS domain/project state
    backend authority
```

Avoid adding a broad client global-state library until a concrete state category cannot be handled cleanly by these layers.

---

## 10. Data-table hypothesis

TanStack Table v9 is the leading choice for serious data/project tables because it is headless and keeps markup/styling under ADS control.

The spike should include:

```text
column headers
sorting
filtering
column visibility
row selection or row focus where useful
sticky header
horizontal overflow handling
numeric alignment
missing-value rendering
semantic type indicators
large-row strategy demonstration
```

For the mock slice, client-side rows are acceptable. The architecture must not imply that production datasets will be loaded fully into the browser.

Virtualization or server-side pagination should be added only where the representative performance test justifies it.

---

## 11. Chart bakeoff

Do not select ECharts or Plotly from generic demos.

Implement the same ADS visual examples in both candidates:

```text
1. quantitative distribution / histogram
2. temporal target or feature trend
3. missingness comparison
4. model / validation metric comparison
```

Evaluate:

```text
visual quality out of the box
ability to implement ADS design tokens
interaction quality
hover/selection semantics
dark/light theme integration
responsive resizing
large-data behavior relevant to previews
accessibility support
export behavior
React integration ergonomics
bundle/dependency impact
ability to preserve analytical semantics from backend results
```

Current external evidence makes ECharts a serious candidate because it supports Canvas/SVG, progressive rendering, broad chart types, data transforms, responsive customization, and accessibility features. Plotly remains a serious candidate because of its strong scientific/analytical ecosystem and React integration.

The winner may be one library, or a deliberate split if evidence demonstrates materially different needs. Prefer one primary chart system unless the benefits of two justify the extra visual/technical surface.

---

## 12. First screen set

The visual spike should contain real navigation among at least these routes:

```text
Overview
Data
EDA
Decisions / History
```

The persistent project navigation should also visibly reserve the longer-term structure:

```text
Validation
Features
Models
Experiments
Evaluation
Report
```

Inactive/future sections should be clearly distinguished from broken links.

### Overview

Should answer quickly:

```text
What is the project?
What is the current analytical state?
What matters now?
What is blocked?
What recently changed?
What is running?
```

### Data

Should provide a professional dataset/variable inspection experience.

### EDA

Should combine analytical visual workspace with methodological recommendations and options.

### Decisions / History

Should show that ADS tracks rationale/provenance rather than just current outputs.

---

## 13. Methodological recommendation interaction

The spike must visually distinguish:

```text
REQUIRED / BLOCKING
RECOMMENDED
RELEVANT / APPLICABLE
DEFERRED
```

For each item, the user should be able to expose at least representative content for:

```text
why it is here
what it can establish
what context/evidence it depends on
what happens if skipped
alternative/complementary methods
```

The exact interaction can be a context panel, drawer, detail view, or expandable section.

A colored badge alone is insufficient.

---

## 14. Object-specific UI

At least three domain objects should have deliberately different visual/interaction forms:

```text
Question
Finding
Decision
```

The test is whether a reviewer can understand the object type and its purpose without relying solely on a title label.

At least one Decision should expose:

```text
selected option
alternatives
rationale
supporting Finding/Evidence references
history/status
```

---

## 15. Approval and run interaction

The spike should simulate a run that reaches:

```text
WAITING_FOR_APPROVAL
```

The approval panel/dialog must show:

```text
action proposed
reason
important parameters
side-effect level
what approval does
what rejection does
```

Approval/rejection changes mock run state through the same interaction boundary intended for the later real runtime.

This is the first practical test of the future human-in-the-loop interface.

---

## 16. AG-UI feasibility test

Do not make AG-UI the internal domain event model.

Define a small ADS-owned event vocabulary for the spike, such as:

```text
run.started
run.status_changed
message.delta
message.completed
tool.started
tool.completed
approval.requested
approval.resolved
artifact.created
```

Then implement a small mapping experiment from representative AG-UI events into or out of this vocabulary.

Pass criterion:

```text
AG-UI can be adopted as a transport adapter without forcing
Question/Finding/Decision/project-event semantics to become AG-UI types.
```

If the mapping is awkward or protocol maturity is insufficient, keep the native ADS stream and defer AG-UI.

---

## 17. Testing stack

### Unit/component logic

Vitest is the leading hypothesis because it aligns naturally with the Vite application and provides a fast test runner for pure frontend logic.

### Browser/e2e

Playwright is the leading browser-level test framework.

The spike should use Playwright for:

```text
navigation
keyboard interaction
approval flow
responsive viewport checks
basic accessibility scans
ARIA/semantic structure snapshots where useful
visual screenshot regression
```

Playwright's official tooling supports screenshot comparisons and accessibility testing with axe. Automated accessibility tests are not a replacement for manual review.

Visual screenshot baselines should be generated in one controlled CI environment because browser/OS rendering differences can create noise.

---

## 18. Visual review process

Automated screenshot comparison protects against accidental drift. It cannot decide whether the product is attractive or well designed.

For the initial visual spike, preserve screenshots at representative widths:

```text
1440px
1280px
1024px
```

and in:

```text
light mode
dark mode
```

for the key screens.

The design review should explicitly inspect:

```text
hierarchy
density
typography
alignment
status clarity
panel balance
chart integration
table readability
empty/loading/error treatment
visual consistency
professional/premium character
```

A human visual review is part of the gate.

---

## 19. Accessibility gate

At minimum:

```text
keyboard can navigate primary shell and main actions
focus is always visible
buttons/controls have accessible names
status is not communicated by color alone
modal/popover focus behavior is correct
contrast passes common automated checks
reduced-motion mode does not break understanding
core routes have no critical automated axe violations
```

The first spike does not claim full WCAG certification.

---

## 20. Responsive/performance gate

The product is desktop-first, but normal professional window sizes must remain usable.

Required viewports:

```text
1440x900
1280x800
1024x768
```

At 1024px the interface may collapse/reconfigure the system context panel, but the core analytical workspace must remain usable.

Representative mocked state should include enough rows/items to expose obvious rendering/pathology issues rather than testing only three cards.

---

## 21. Loading, empty, error, and offline states

The spike must implement representative non-success states:

```text
initial loading/skeleton
empty recommendations
recoverable API-style error
offline/backend unavailable
run failure
waiting for approval
```

These states must look designed, not like afterthoughts.

---

## 22. Frontend spike gates

```text
FE-01  React + TypeScript + Vite build/lint/test works on Linux and Windows
FE-02  real project shell/navigation works at 1440/1280/1024 widths
FE-03  Overview communicates current state, blockers, recent change, and run status
FE-04  Data route implements professional table inspection and URL-preserved view state
FE-05  EDA route integrates plots with methodological navigation
FE-06  REQUIRED/RECOMMENDED/RELEVANT/DEFERRED states are visibly and semantically distinct
FE-07  Question/Finding/Decision have object-specific representations
FE-08  run/activity stream and approval interaction work through an application boundary
FE-09  coherent light and dark themes use shared design tokens
FE-10  keyboard/focus/accessibility baseline passes automated and manual checks
FE-11  loading/empty/error/offline/waiting states are deliberately designed
FE-12  controlled Playwright screenshot baselines exist for key routes/viewports/themes
FE-13  mock data source can be replaced behind typed frontend data-access contracts
FE-14  AG-UI mapping feasibility is evaluated without domain-event coupling
FE-15  ECharts and Plotly are compared using the same ADS analytical examples
FE-16  no full dataset/project history/global knowledge catalog is assumed to live in browser memory
FE-17  visual review explicitly concludes whether the shell meets the premium professional product bar
```

FE-17 cannot be automated away.

---

## 23. Desktop packaging

Do not add Tauri in the first frontend spike.

Preserve compatibility by keeping the V1 frontend a normal SPA and avoiding assumptions that require a public web server.

After the web shell and Python service boundary work, run a separate desktop-packaging spike only if benefits such as these become valuable:

```text
single desktop application install
native filesystem integration
system tray/background controls
native dialogs
local-service lifecycle management
stronger desktop permission model
```

Tauri 2 is the current leading future candidate, not an accepted dependency.

---

## 24. What this spike does not build

```text
complete backend HTTP API
real LLM/agent runtime integration
full project object model
full dataset viewer for arbitrary billions of rows
notebook editor
IDE/debugger
all project sections
production authentication
cloud deployment
mobile-equivalent workspace
Tauri desktop package
final charting library before FE-15
final AG-UI decision before FE-14
```

---

## 25. Promotion criteria

If the spike passes FE-01 through FE-17 without requiring a different architectural foundation, promote:

```text
frontend architecture specification
selected core frontend stack
selected chart strategy
selected or deferred AG-UI boundary
initial ADS design system
```

If the visual/product result is merely functional but not excellent, do not promote the frontend as complete. Refine the design system and shell while the surface is still small.

The target is not a demo dashboard. It is the foundation of the actual product.

---

## 26. Current official references reviewed

```text
Vite guide
https://vite.dev/guide/

TanStack Router search params
https://tanstack.com/router/latest/docs/guide/search-params

TanStack Query
https://tanstack.com/query/latest/docs/framework/react

TanStack Table v9
https://tanstack.com/table/v9/docs/framework/react

Apache ECharts
https://echarts.apache.org/en/

Playwright visual comparisons
https://playwright.dev/docs/test-snapshots

Playwright accessibility testing
https://playwright.dev/docs/accessibility-testing

Node.js release status
https://nodejs.org/en/about/previous-releases
```

Framework/library claims should be rechecked before final dependency pinning because this ecosystem changes quickly.