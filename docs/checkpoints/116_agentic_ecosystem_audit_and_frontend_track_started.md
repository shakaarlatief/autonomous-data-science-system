# Checkpoint 116: Agentic Ecosystem Audit and Frontend Track Started

**Date:** 2026-08-20  
**Status:** Historical design, research, and architecture checkpoint  
**Checkpoint class:** MIXED  
**Project stage:** Post-V0 V1 methodological-brain implementation; agent-runtime and professional-frontend architecture boundary  
**Scope:** Records the 2026 agentic ecosystem audit, promotion of the reusable-knowledge interchange contract, establishment of the professional frontend foundation, new architecture principles, and candidate runtime/frontend evaluation contracts. Also records the still-open governed PostgreSQL round-trip confirmation accurately.  
**Authority:** Historical rationale and transition record. Current foundations, principles, accepted decisions, and specifications govern their declared scopes.  
**Design session:** 02  
**ChatGPT project:** Autonomous Data Science System  
**Session title:** 02 - Methodological Brain & Knowledge Units

## 1. Why this checkpoint exists

After the first reusable-knowledge interchange and production persistence slices, the user explicitly challenged whether the project might be rebuilding infrastructure already provided by modern AI-agent technology such as MCP, agent frameworks, multi-agent protocols, and related tooling.

The user also reiterated an important product requirement: the frontend should be a genuinely professional, modern, visually excellent application and should not be postponed until the entire backend is complete.

These questions deserved a stage-boundary audit before additional orchestration or retrieval infrastructure was implemented.

---

## 2. Main conclusion from the agentic ecosystem audit

The current ADS work on methodological knowledge, project objects, revision history, governance, provenance, Findings, Questions, Decisions, and selective context is not made redundant by MCP or agent frameworks.

Those are durable product/domain semantics.

Modern agent technology mostly addresses a different layer:

```text
agent loop
model/tool dispatch
workflow durability
pause/resume
human approval
external tool interoperability
remote agent interoperability
frontend/agent event transport
operational tracing
```

The resulting architecture principle is:

```text
ADS domain/project semantics
        !=
agent/runtime/protocol state
```

Frameworks should sit beneath replaceable application boundaries rather than becoming the meaning of the project.

Detailed research:

```text
docs/research/001_2026_agentic_ecosystem_and_integration_architecture_audit.md
```

---

## 3. Current external ecosystem conclusions

### MCP

MCP is a strong future interoperability boundary for external tools/resources/services.

The current 2026-07-28 protocol direction is materially different from earlier MCP assumptions: the core is stateless and Roots, Sampling, and Logging have been deprecated. ADS should not build new architecture around those deprecated features.

MCP should not become the internal application bus or the model-provider abstraction.

### Agent runtimes

Four candidates deserve an ADS-shaped bakeoff:

```text
OpenAI Agents SDK
LangGraph
Microsoft Agent Framework
Google ADK 2.0
```

No runtime is accepted yet.

The first runtime should begin with one capable principal reasoner plus explicit tools and bounded context. Multi-agent decomposition should earn its complexity through evaluation.

### A2A

A2A is useful for independently deployed agent systems across framework/process/vendor boundaries. It is not needed merely because ADS may later have several internal specialist agents.

A2A is therefore deferred.

### AG-UI

AG-UI is relevant to the frontend-agent interaction seam and should be tested before inventing a large custom transport protocol.

It should remain an adapter around ADS-owned interaction/run events rather than defining Question/Finding/Decision/project-event semantics.

### Observability

Framework-native tracing is useful but not sufficient as the permanent ADS observability contract. Project provenance remains ADS-owned, with OpenTelemetry-compatible operational export a strong future direction.

---

## 4. New durable architecture principles

Three principles were promoted:

```text
P-027
Agent frameworks and interoperability protocols are infrastructure,
not ADS domain authority.

P-028
Prefer deterministic software for explicit work and agent reasoning
for genuine ambiguity.

P-029
The product interface is a first-class reasoning, control, and
quality surface.
```

Source:

```text
docs/PRINCIPLES.md
```

P-028 is especially important because it prevents the project from converting normal software responsibilities into agents simply because an agent framework exists.

---

## 5. Professional frontend requirement strengthened

Foundation 017 already described a professional interactive data-science workspace.

The user's explicit quality requirement is now promoted more strongly in:

```text
docs/foundations/021_professional_product_interface_and_frontend_design_foundation.md
```

The frontend must be:

```text
modern
visually excellent
premium/professional
information-rich without becoming cluttered
carefully typographic
responsive at professional desktop/laptop sizes
accessible
fast and polished
coherent in light and dark modes
well-designed in loading/empty/error/offline states
```

The frontend is also now explicitly an early parallel development track rather than an end-of-project styling phase.

This is product architecture, not visual decoration. The interface is where methodological relevance, Questions, Findings, Decisions, provenance, run state, and human approvals become understandable and actionable.

---

## 6. Frontend technology direction is narrowed but not yet accepted

Current research makes the following the leading V1 hypothesis:

```text
React
TypeScript
Vite
TanStack Router
TanStack Query
TanStack Table v9
shadcn/ui source-distributed components
ADS-owned design tokens and visual language
Playwright
Vitest
```

Why Vite is favored for the first spike:

```text
local-first application
Python backend/service
highly interactive SPA
no demonstrated SEO/SSR requirement
possible Tauri packaging later
```

Next.js remains capable but does not currently justify adding a Node/full-stack rendering layer.

Charting remains deliberately unresolved. The frontend spike will compare ECharts and Plotly on the same ADS analytical examples.

Tauri remains a later packaging candidate, not part of the first browser-based product shell.

Candidate specification:

```text
docs/specifications/006_v1_frontend_architecture_and_visual_spike.md
```

---

## 7. Agent-runtime bakeoff contract established

Specification 005 defines an empirical comparison rather than a framework popularity contest:

```text
docs/specifications/005_v1_agent_runtime_and_interoperability_bakeoff.md
```

Mandatory test areas include:

```text
domain isolation
single-agent tool loop
current MCP integration
human approval interrupt
durable resume
external ADS project-state authority
context transparency
cancellation / timeout
failure / retry semantics
structured output
observability
provider / test substitution
```

An optional specialist-agent challenge happens only after the single-agent path passes.

A valid bakeoff result remains:

```text
Use simpler direct model calls for the first V1 slice
because no agent framework earns its complexity yet.
```

The evaluation is not biased toward adopting a framework.

---

## 8. Reusable-knowledge interchange promotions completed

Checkpoint 115 already demonstrated KI-01 through KI-10.

The pending promotion work has now been completed:

```text
Specification 004
    Candidate v0.1
        -> Accepted V1 technical specification v1.0

D-031
    accepted V1 reusable-knowledge interchange decision
```

The accepted interchange remains:

```text
JSON
+ JSON Schema Draft 2020-12
+ application semantic validation
+ deterministic serialization
```

Candidate/benchmark content cannot silently create accepted methodological authority.

---

## 9. Governed production round-trip remains open

Do not conflate the accepted interchange-format gate with the separate production database round-trip gate.

Current confirmed evidence is:

```text
SQLite roundtrip
    PASS

first PostgreSQL 18 roundtrip
    FAIL
```

The PostgreSQL failure was diagnosed as a physical migration portability defect:

```text
constraint identifier exceeded PostgreSQL's 63-character identifier limit
```

The migration constraint names were shortened in:

```text
ba6a92f83aac3a63ebfb7f97a4378c93fa28547b
Shorten interchange migration identifiers for PostgreSQL
```

The workflow was then made source-commit traceable in:

```text
a69b8859696fbd3b45124c257d085989d692a207
Make roundtrip gate status traceable to source commit
```

At this checkpoint, the repository has not yet persisted a new confirmed PASS from the corrected PostgreSQL run.

Therefore the governed round-trip must remain open.

Temporary diagnostic machinery should be removed after the corrected gate is conclusively resolved.

---

## 10. New development shape

The project is no longer a single backend-first line.

The justified near-term structure is:

```text
                    V1 CORE
                      |
          +-----------+-----------+
          |           |           |
          v           v           v
 governed knowledge  agent      frontend
 persistence seam    runtime     product shell
          |          bakeoff        |
          |           |             |
          +-----+-----+-------------+
                |
                v
      first real end-to-end
       product vertical slice
                |
                v
        retrieval/horizon work
        integrated as measured
```

Retrieval is not abandoned. It remains a critical parallel methodological-brain track.

The new ordering prevents us from building large invisible infrastructure before testing the actual product and modern runtime ecosystem.

---

## 11. Promotion audit

### External-ecosystem research memo

Promoted as a current research source:

```text
docs/research/001_2026_agentic_ecosystem_and_integration_architecture_audit.md
```

Because the ecosystem changes rapidly, framework-specific facts must be rechecked before dependency selection.

### New foundation

Yes:

```text
Foundation 021
Professional Product Interface and Frontend Design
```

The user's frontend quality requirement and early-frontend development strategy are now durable product knowledge.

### New principles

Yes:

```text
P-027 through P-029
```

### New accepted decision

D-031 was promoted from the already-passing Checkpoint 115 interchange evidence.

No agent-runtime, MCP-internal architecture, A2A, AG-UI, frontend stack, chart library, or desktop-wrapper decision is accepted yet.

### New candidate specifications

Yes:

```text
Specification 005
V1 Agent Runtime and Interoperability Bakeoff

Specification 006
V1 Frontend Architecture and Visual Spike
```

These are evaluation contracts, not accepted implementation choices.

### Major-changes / routing / current-state update

Required and performed as part of this stage-boundary reconciliation.

---

## 12. Exact continuation

The next work should proceed in three bounded tracks.

```text
A. GOVERNED ROUNDTRIP CLOSURE
   rerun corrected PostgreSQL gate
   inspect result
   fix if necessary
   remove temporary diagnostics
   close with a dedicated checkpoint only after real PASS

B. AGENT RUNTIME BAKEOFF
   implement the smallest representative Specification 005 harness
   begin with single-agent path
   do not adopt multi-agent architecture by default

C. FRONTEND VISUAL/TECHNICAL SPIKE
   scaffold the Specification 006 shell
   use deterministic typed ADS mock state
   establish the actual design system
   build Overview/Data/EDA/Decision-History slice
   compare ECharts and Plotly
   test accessibility / interaction / screenshots
```

Retrieval-quality benchmarking remains a fourth connected track and should begin once the current preservation and round-trip closure are stable enough to avoid competing changes to the same knowledge fixtures.
