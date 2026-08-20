# Foundation 021: Professional Product Interface and Frontend Design

**Date:** 2026-08-20  
**Status:** Foundational product-interface and experience design  
**Scope:** Long-term product interface and V1 frontend direction; does not freeze a specific frontend framework, component library, chart library, desktop wrapper, or agent-UI protocol  
**Design session:** 02  
**ChatGPT project:** Autonomous Data Science System  
**Session title:** 02 - Methodological Brain & Knowledge Units

## Purpose

Foundation 017 established the Autonomous Data Science System as a professional interactive data-science operating environment rather than a one-shot analysis generator or a prettier chat window.

This foundation strengthens the product-interface side of that vision.

The interface is not an ornamental layer to be added after the backend is complete. It is one of the places where methodological reasoning becomes inspectable, where the user understands current project state, where system recommendations can be challenged, and where consequential actions are approved or overridden.

The target is therefore both functional and aesthetic:

> **The Autonomous Data Science System should feel like a modern, premium professional analytical product: visually excellent, fast, coherent, information-dense without being overwhelming, and capable of making complex methodological state understandable and actionable.**

Visual quality is not a substitute for analytical correctness. Analytical correctness is not an excuse for a crude interface.

---

## 1. The interface is a reasoning and control surface

The product should make important system reasoning visible in forms the user can inspect and act on.

Examples include:

```text
recommended analyses
required / blocking concerns
applicable lower-priority options
unresolved Questions
current Findings
supporting Evidence
important assumptions
warnings and validity constraints
model / method alternatives
Decisions and rationale
historical changes
running or paused execution
human approval requests
```

The user should not need to inspect raw database rows, agent traces, or prompt transcripts to understand the current analytical situation.

Likewise, a chat response alone is not an adequate representation of the project.

---

## 2. Professional product character

The visual character should be closer to a high-quality modern developer/data product than to a generic admin template.

Required qualities include:

```text
clear information hierarchy
excellent typography
careful spacing and alignment
high-quality icons
coherent light and dark themes
restrained, purposeful use of color
subtle depth and elevation where useful
strong analytical visualization quality
consistent interaction patterns
fast, responsive feedback
carefully designed empty states
carefully designed loading and skeleton states
clear error and recovery states
subtle motion where motion improves orientation
polished hover/focus/selection states
high-quality keyboard interactions
accessible focus and screen-reader behavior
```

The product should avoid the common failure mode of oversized cards, excessive whitespace, decorative gradients, and low information density that make analytical software feel like a marketing page.

It should also avoid the opposite failure mode: dense legacy enterprise UI with weak hierarchy, tiny unreadable text, inconsistent controls, and no visual calm.

The desired balance is:

```text
compact enough for serious work
    +
clear enough for complex project state
    +
polished enough to feel premium
```

---

## 3. Desktop-first analytical workspace

V1 should optimize primarily for professional laptop and desktop use.

The core workflows involve:

```text
data tables
plots
methodological option comparison
project navigation
execution monitoring
code/artifact references
side-by-side evidence and reasoning
history / provenance inspection
```

These benefit from substantial screen area.

The interface should remain responsive across normal laptop/desktop sizes, but a fully equivalent mobile analytical workspace is not a V1 requirement.

Responsive design still matters because users may resize windows, use split-screen layouts, or eventually run the product in a desktop wrapper.

---

## 4. Candidate workspace anatomy

The exact layout remains subject to prototype testing, but Foundation 017's three-part concept remains useful:

```text
+--------------------+--------------------------------+----------------------+
| PROJECT NAVIGATION | PRIMARY WORKSPACE              | SYSTEM / CONTEXT     |
|                    |                                |                      |
| Overview           | tables                         | recommendations      |
| Data               | plots                          | required concerns    |
| EDA                | comparisons                    | questions            |
| Validation         | evidence                       | warnings             |
| Features           | decisions                      | alternatives         |
| Models             | run results                    | discuss / ask        |
| Experiments        | report content                 | approvals            |
| Evaluation         |                                |                      |
| Report             |                                |                      |
| Decisions          |                                |                      |
| History            |                                |                      |
+--------------------+--------------------------------+----------------------+
```

This is not a rigid requirement that all three regions are always visible. The context panel may collapse, become a drawer, or change by route. The principle is that project navigation, primary analytical work, and system guidance are distinguishable interaction responsibilities.

---

## 5. Recommendations should have visible epistemic status

The interface must make distinctions from Foundation 019 legible.

For example:

```text
REQUIRED / BLOCKING
    cannot be safely ignored without affecting downstream validity

RECOMMENDED
    high current value but not a hard validity requirement

RELEVANT / APPLICABLE
    methodologically appropriate but lower current priority

DEFERRED
    relevant but intentionally postponed

NOT CURRENTLY APPLICABLE
    known but prerequisites/scope do not match
```

These states should not be encoded by color alone.

The user should be able to ask or inspect:

```text
Why is this recommended?
Why is this required?
What evidence supports that?
What happens if I skip it?
Why was method X not recommended?
What information would change this assessment?
```

The product should support progressive disclosure so comprehensiveness does not create constant visual overload.

---

## 6. Project objects should have first-class visual representations

Question, Evidence, Finding, Claim, Decision, Run, Proposal, Investigation, and Artifact should not all be rendered as generic cards with different headings.

Their visual and interaction patterns should reflect their meaning.

Examples:

```text
Question
    current status
    why it matters
    possible ways to resolve
    dependencies / blockers

Finding
    concise statement
    supporting Evidence
    scope
    criterion/result where relevant
    provenance

Decision
    selected option
    alternatives considered
    rationale
    evidence / Findings used
    who/what authorized it
    supersession history

Run
    state / progress
    input/config version
    artifacts/results
    logs/telemetry link
    cancellation/retry controls
```

This reinforces the object model instead of hiding it behind prose.

---

## 7. Chat should be integrated, not dominant

Natural-language discussion remains important.

The user should be able to:

```text
ask why a recommendation exists
request an alternative
change project intent
approve / reject a proposal
request deeper explanation
ask the system to run selected work
challenge a Finding
request another visualization
```

But chat should not become the only durable record of these interactions.

Consequential outcomes should map back into structured project objects and history.

The system panel may provide conversational interaction, but the main workspace should continue to display the resulting project state directly.

---

## 8. Data experience

The Data area should feel like a serious analytical workspace.

Expected capabilities eventually include:

```text
large, virtualized or paginated tables where necessary
column typing and semantic role display
sorting/filtering/searching
missingness and cardinality summaries
variable metadata and lineage
column inspection
statistics panels
sampling controls
copy/export where appropriate
links to source artifacts
```

Data rendering must not silently imply that only the visible rows were analyzed.

Sampling, filtering, truncation, and aggregation should be explicit.

---

## 9. Visualization quality

Charts are evidence-bearing analytical artifacts, not decorative dashboard widgets.

The product should support:

```text
publication-quality defaults where feasible
interactive hover/selection/zoom where useful
clear axis and unit semantics
consistent typography and theme integration
accessible legends and labels
exportable figures
small multiples / comparison views
temporal and distribution visualizations
diagnostic plots
large-data strategies where needed
```

Charts should preserve the analytical semantics generated by the Python/statistical execution layer rather than being independently recomputed in the frontend without provenance.

The eventual chart library should be selected through a visual/technical spike rather than generic popularity.

Current serious candidates include Plotly.js and Apache ECharts for different strengths.

---

## 10. Execution and observability

Foundation 016 and P-022 remain important for the UI.

The frontend should observe persisted execution/run state and events rather than becoming part of execution correctness.

A running analysis might surface:

```text
queued
preparing
reasoning
waiting for tool
executing
waiting for approval
paused
completed
failed
cancelled
```

where meaningful.

The user should see enough information to understand what is happening without exposing internal reasoning traces as if they were authoritative explanations.

For consequential operations, an approval interaction should clearly show:

```text
what action is proposed
why it is proposed
what it can change
relevant inputs/parameters
whether it is reversible
what approval/rejection will do
```

---

## 11. History and provenance should be understandable

The product should make temporal/project evolution inspectable without forcing the user into Git history or database tooling.

Useful views may include:

```text
event timeline
Decision history
Finding supersession
knowledge revision influence
artifact/run lineage
what changed since prior project state
why a prior conclusion became stale
```

Visual history should distinguish:

```text
current state
historical state
superseded knowledge
stale evidence
invalidated claim
rejected alternative
```

History is not merely an activity feed. It is part of project traceability.

---

## 12. The product should complement VS Code

P-023 and P-024 remain binding.

Do not spend V1 effort building a full code editor, notebook runtime, debugger, Git client, terminal emulator, or IDE clone unless concrete workflows later justify specific embedded capabilities.

Instead, the interface should integrate with the developer workbench through capabilities such as:

```text
open artifact/file in VS Code
show source path
show Git commit/reference
show generated code associated with a Run
copy reproducible command
open terminal context
show repository status where useful
```

The system should own project/process control; VS Code remains the professional developer workbench.

---

## 13. Design system requirements

The frontend should establish a real design system from the first serious implementation rather than accumulating one-off component styles.

The foundation should include:

```text
design tokens
color roles
semantic status colors
typography scale
spacing scale
radius/elevation rules
icon conventions
focus treatment
motion durations/easing
layout breakpoints
component density variants
chart theme tokens
code/monospace typography
loading/empty/error conventions
```

The component library is an implementation aid, not the design system itself.

If shadcn/ui, Base UI, React Aria, Radix, or another primitive library is used, the product should still own its visual language rather than looking like an untouched starter template.

---

## 14. Accessibility

Accessibility is part of professional quality.

V1 frontend implementation should target:

```text
semantic HTML
keyboard navigation
visible focus
screen-reader labels
non-color-only status communication
adequate contrast
reduced-motion support where motion is present
accessible dialogs/menus/tooltips
accessible data-table and chart fallbacks where practical
```

Accessibility primitives from established libraries are preferred to reimplementing complex keyboard/focus behavior ourselves.

---

## 15. Performance and perceived responsiveness

A polished interface must remain responsive with realistic project sizes.

Frontend design should account for:

```text
large data previews
many Findings/Questions/Decisions
long execution histories
interactive plots
streaming run events
large methodological option sets
```

The UI should avoid rendering the complete global methodological catalog or complete project history when only a current slice is needed.

This mirrors the backend methodological-horizon principle.

Techniques may include:

```text
virtualization
pagination
incremental loading
memoized selectors
server-state caching
route-level code splitting
streaming event updates
bounded visible history
```

Specific performance technologies remain open until the frontend technical spike.

---

## 16. Product states deserve deliberate design

Professional applications spend substantial time outside the ideal success state.

The interface should deliberately design:

```text
first-run / no project
empty dataset
no applicable recommendation
loading
long-running operation
waiting for human
partial result
stale result
offline/local service unavailable
permission denied
validation error
execution failure
recoverable retry
irrecoverable failure
cancelled operation
```

Error states should describe recovery, not merely display stack traces.

Technical diagnostics can remain available through expandable details.

---

## 17. Frontend should start before backend completion

The frontend is now a parallel V1 development track.

The first serious shell may use deterministic typed mock data for project state while backend APIs are still being implemented.

This is intentional, not throwaway work.

Benefits:

```text
methodological concepts are tested against real human presentation
object-model awkwardness becomes visible early
backend APIs can be shaped around real product needs
visual language stabilizes before dozens of screens exist
agent/frontend interaction needs become concrete
end-to-end vertical slices become possible sooner
```

Mocks should use the same conceptual types the real backend will eventually expose and should be replaceable behind a data-access boundary.

---

## 18. First frontend product slice

The first product slice should be narrow but visually serious.

Candidate scope:

```text
application shell
project navigation
Overview
Data preview
EDA workspace shell
methodological recommendations panel
Questions
Findings
Decisions
run/activity stream
one human approval interaction
system discussion panel
light + dark appearance
```

Representative mock/project state can use the methodological knowledge examples already developed for V1.

The first slice does not need full analytical execution. Its purpose is to validate product architecture, visual hierarchy, interaction patterns, and the seam to future backend/runtime events.

---

## 19. Current frontend technology hypotheses

Technology selection is not promoted by this foundation, but current 2026 research narrows the serious options.

### React + TypeScript

Strong default hypothesis because the product is highly interactive and the current ecosystem for tables, analytical visualization, accessibility primitives, and agentic UI integration is strong.

### Vite versus Next.js

Vite is currently the stronger V1 hypothesis because ADS is local-first, has a Python application/backend layer, requires a highly interactive client application, has no demonstrated SEO/server-rendering requirement, and may later be packaged with a desktop wrapper.

Next.js remains technically capable, but its App Router defaults to Server Components and adds a Node/full-stack rendering layer whose value for this product has not yet been demonstrated.

Tauri's current frontend guidance explicitly recommends Vite for SPA-style desktop applications and notes that Tauri acts as a static web host rather than an SSR runtime.

This is strong evidence for Vite, but the final choice should still pass a small implementation spike.

### Component primitives

shadcn/ui is a strong candidate because it distributes component source into the application rather than hiding design behind an opaque package. In July 2026, new shadcn projects default to Base UI, while Radix remains supported and React Aria is also a first-class base.

The implementation should compare interaction/accessibility fit rather than blindly inherit the current default.

### Tables

TanStack Table v9 is a strong candidate for data/project tables because it is headless and preserves complete control over markup and styling.

### Charts

Plotly.js and Apache ECharts are serious candidates. ECharts provides broad chart types, Canvas/SVG, progressive rendering, large-data capabilities, responsive design, and strong visual customization. Plotly has direct alignment with analytical/scientific visualization and a maintained React component.

The choice should be tested with actual ADS plots rather than generic demos.

### Graph/dependency views

React Flow is a strong optional candidate if an interactive knowledge/dependency/history graph becomes useful. It should not be added merely because the backend contains relations.

### Desktop wrapper

Tauri 2 is a credible future packaging option because it supports any web frontend and targets Windows/macOS/Linux with a system WebView. It should be deferred until the browser-based frontend shell and Python service boundary are stable enough to justify native packaging.

---

## 20. Success criteria

The frontend is succeeding when a user can open a substantial project and quickly understand:

```text
What is this project trying to do?
What data do we have?
What is happening now?
What has already been learned?
What remains unresolved?
What does the system recommend next?
What is required for validity?
What alternatives exist?
Why does the system think that?
What can I run, change, approve, or reject?
What evidence supports the current conclusions?
How did the project arrive here?
```

and can do so through a product that feels coherent, fast, modern, visually refined, and trustworthy.

That is a materially higher bar than a functional dashboard.