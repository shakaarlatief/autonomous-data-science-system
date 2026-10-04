# Architecture Program Overview and Working Roadmap

**Status:** TEMPORARY HUMAN ORIENTATION / NON-AUTHORITATIVE / NON-GOVERNING  
**Date:** 2026-10-04  
**Purpose:** Provide one standalone overview of the architecture program, what has been completed, what remains open, where the project is now, and what the forward plan is.  
**Important:** This file is not part of the intended future Project System architecture. It is not a source of governing truth, does not supersede accepted research/specifications/decisions, and may be revised or deleted later. If this overview conflicts with an authoritative decision, specification, research acceptance, current routing record, or owner decision, the authoritative source wins.

---

## 1. Current position in one paragraph

The project has completed most of the major **logical architecture** work for the ADS Project System, including the Product/Project split, Project bounded responsibilities, Project information architecture, Project-system materialization direction, Activation/Orchestration, assurance/admission through WARRANT-F, and the governing semantic/control kernel now selected as **THIN_CENTRED_HYBRID_V03**. The project is **not** yet at final implementation or migration. It has entered **R0**, whose purpose is to determine the best concrete physical/software realization of the integrated Project System before implementation. Some architectural questions remain intentionally open, most importantly the final semantic organization/navigation architecture that historically used Research 217's subject hierarchy. That old subject system is evidence, not an inherited target. The current plan is to make that remaining semantic obligation explicit, complete independent physical/system design, reconcile alternatives, run decision-relevant probes where needed, select the physical target, implement it, inventory and migrate current live semantics in bounded waves, run shadow/untouched qualification, and only then consider an explicit authority switch.

---

## 2. Whole-system picture

The repository contains two major planes:

```text
AUTONOMOUS DATA SCIENCE SYSTEM REPOSITORY

PRODUCT PLANE
    The ADS Product itself:
    data-science / AI reasoning
    analytical execution
    user interaction
    runtime
    product-facing capabilities

PROJECT PLANE
    The system that designs, governs, researches, builds,
    qualifies, preserves, migrates, operates and evolves ADS.

    Knowledge / State / Authority
        THIN_CENTRED_HYBRID_V03
        J1 -> J2 -> J3
        completion
        lineage
        orientation

    Activation / Orchestration, AO
        what is happening
        what activates
        what happens next

    Assurance / Admission, WARRANT-F
        what must be established
        before consequences admit

    Engineering / Delivery / Migration / Recovery

    Observation / Continuity / AO-4 Architecture Evolution

Around the concrete ADS Project System:

GENERIC / REUSABLE PROJECT FRAMEWORK IDEA
        ↓ materialize / instantiate
SELF-CONTAINED PROJECT-SOVEREIGN INSTANCE

This is the PSMF / Generalizable Project Operating Architecture direction.
```

The important point is that these are different architectural dimensions of one larger system, not mutually exclusive alternatives.

---

## 3. What THIN_CENTRED_HYBRID_V03 actually is

THIN_CENTRED_HYBRID_V03 is **not**:

- the whole ADS architecture;
- the whole Product architecture;
- the whole Project architecture;
- Activation/Orchestration itself;
- WARRANT-F itself;
- the final file/folder layout;
- the final CI/CD design;
- the final storage model;
- the final semantic navigation hierarchy.

It is the selected **governing semantic/control kernel** of the Project System.

Its core job is to define how governing meaning becomes traceable operational truth without allowing later model inference, generated state, or implementation facts to become accidental authority.

### J1: governing acceptance

J1 contains the meaning the owner actually accepted, including as applicable:

- owner-visible accepted meaning;
- typed machine consequences;
- explicit accounting;
- completion authority;
- lifecycle/lineage decisions;
- exact source/revision bindings.

Only accepted J1 meaning is normative semantic authority.

### J2: natural-owner realization

J2 contains the real-world facts that realize accepted meaning, such as:

- implementation artifacts;
- procedures;
- migrations;
- coverage;
- evidence;
- qualification;
- activation;
- natural-owner revisions.

J2 does not get to redefine J1.

### J3: mechanically derived operational truth

J3 answers things such as:

- is a requirement satisfied?
- is evidence stale?
- is realization missing?
- is a control violated?
- what is the next operational gap?
- does something require review?

J3 is derived from accepted J1 plus current J2 and shared predicates.

### Additional V03 mechanisms

V03 also selects:

- stable accepted-effect identity;
- REQUIRE / PROHIBIT / GATE / AUTHORIZE / DEFER / LIFECYCLE / SEQUENCE consequence grammar;
- closed accounting of accepted machine effects;
- governing-side completion authority;
- anti-self-certification;
- many-to-many realization coverage;
- N:M semantic lineage;
- CARRY_FORWARD / REPLACE / SPLIT / MERGE / REPARTITION / RETIRE / REINSTATE;
- explicit realization succession;
- default OPEN_RESET across semantic succession;
- explicit carry only for revalidation;
- ordered zero-to-many realization initialization;
- generated non-authoritative orientation;
- explicit REVIEW_REQUIRED ownership;
- detective safeguards that do not become authority;
- explicit legacy-unreconciled handling;
- same-revision acyclic evaluation with feedback through later revisions.

Key references:

```text
docs/research/500_thin_centred_hybrid_v03_owner_decision_candidate.md
docs/research/502_v03_owner_selection_and_realization_program_opening.md
```

---

## 4. Major architecture components and their status

| Architecture / program | What it answers | Current status |
|---|---|---|
| **PKA-CANDIDATE-01 / Specification 028** | Earlier Project Knowledge Architecture and current implementation/migration contracts | Historical selected target and **still current operational authority** until explicit successor cutover |
| **W0-W5** | Earlier production substrate, integration, shadowing, capture/promotion, information/navigation work | Completed as historical implementation/qualification evidence; some physical targets later superseded |
| **AO / Activation-Orchestration** | What activates, what process applies, what happens next, which actor/tool/workstream is involved | Substantial logical architecture designed; concrete production realization still to be selected/implemented |
| **AO-4** | How architecture evolution is triggered, classified, governed and accepted | Designed; needs production realization |
| **PSMF** | Relationship between generic reusable Project framework and project-local self-contained instance | Accepted architectural direction; generic extraction intentionally postponed |
| **G-DUAL** | Highest-level Product / Project repository split | Accepted Level-1 architecture |
| **R6** | Professional responsibilities, bounded contexts and workspace boundaries | Accepted architecture |
| **R7** | Project information-role architecture | Accepted architecture direction; exact physical realization remains open |
| **R8-A** | Earlier exact repository/workspace realization direction | Important evidence; physical details remain redesignable in current R0 |
| **WMR-H** | Representation architecture for human knowledge, machine metadata/state, generated views and indexes | Accepted direction/evidence; exact production mechanism remains open |
| **WARRANT-F** | Assurance/admission architecture: CLAIM, VERIFIER, WARRANT, EVIDENCE, DECISION, etc. | Accepted semantic architecture; exact CI/CD/provider/workflow realization remains open |
| **Whole Project Operating Architecture** | Composition of AO, knowledge/state/authority, assurance, delivery, recovery/evolution | Accepted high-level integration vision |
| **THIN_CENTRED_HYBRID_V03** | Governing semantic/control kernel connecting J1, J2 and J3 | **Owner-selected successor logical target** |
| **Semantic organization / subjects / navigation** | How knowledge is semantically organized, discovered, navigated, retrieved and activated | **Still intentionally unresolved** at final-target level |
| **Codexless Runtime Bridge** | Reusable bounded local/developer execution infrastructure used by ADS and potentially other projects | Active tool today; **long-term standalone-product boundary now explicit**, extraction deferred |
| **R0 physical/software realization architecture** | How the integrated Project System actually exists in code/repository/storage/workflow/CI/runtime | **Current active stage** |
| **Production successor implementation** | Build the selected physical target | Not started |
| **Semantic migration** | Reconcile current live knowledge/control into successor semantics | Not started |
| **Shadow / untouched qualification / cutover** | Prove successor safely before authority switch | Future |

---

## 5. Chronological architecture evolution

### Phase A: earlier Project Knowledge Architecture

The project first developed and selected PKA-CANDIDATE-01 and Specification 028.

That program led to W0-W5.

### W0-W5

Broadly:

```text
W0
    production Project Knowledge substrate
    identity / authority / workstreams / views / state generation
    capture / public-private handling / rebuild / CLI / tests

W1
    real-project integration

W2
    shadow derived views

W3
    compatibility shadow

W4
    production capture / promotion

W5
    future information architecture / semantic navigation / authoring
```

Research 217's semantic-subject system came from W5.

Research 218 froze the then-current W5 target.

Later architecture work deliberately reopened the larger frame, so W5 is now important evidence rather than an unquestioned final target.

### Phase B: Activation / Orchestration

Research 219 onward opened AO because strong knowledge preservation did not guarantee that the system actually activated the right knowledge/process automatically.

AO asks:

- what happened?
- what does the event mean operationally?
- what knowledge must activate?
- what process applies?
- what workstream is current?
- what actor/tool should act?
- what action is allowed?
- what comes next?
- what should be preserved?
- should architecture itself be reconsidered?

AO-4 added governed architecture evolution.

### Phase C: whole-repository architecture reset

PKIA-E01 deliberately asked a higher-level question:

> If the repository and Project System were designed professionally from first principles, what responsibilities and boundaries should actually exist?

This is where the project stopped treating current folders/packages/workflows as target assumptions.

### PSMF

PSMF means:

```text
PROJECT-SOVEREIGN MATERIALIZED FRAMEWORK
```

Conceptually:

```text
generic reusable architecture/framework
          ↓ materialize
specific project receives a complete self-contained Project System
```

The project-local system remains sovereign rather than constantly depending on a central external framework.

Generic framework extraction is postponed until ADS itself has been implemented, migrated, operated and qualified enough to reveal what is genuinely reusable.

### G-DUAL

G-DUAL established the top-level repository distinction:

```text
product/
    operational ADS Product

project/
    system that designs/builds/governs/qualifies/evolves ADS
```

This is the accepted Level-1 architecture.

### R6

R6 derived bounded professional responsibilities/contexts from first principles before mapping current folders.

Important Project-side responsibilities include:

- Project Direction, Architecture and Memory;
- Project Development Control System;
- Research and Qualification;
- Engineering, Verification and Delivery;
- Collaboration and Contribution;
- Historical Preservation.

### R7

R7 redesigned the Project information architecture and superseded the old W5 physical target as the final target.

It distinguished information role/ownership from semantic meaning.

For example, an information-role structure may distinguish:

```text
governance
evidence
operations
history
```

while semantic organization remains a separate dimension.

### R8-A / R8-B / R8-C

R8 progressively explored exact realization dimensions.

R8-A addressed repository/workspace realization.

R8-B produced WMR-H representation architecture.

R8-C produced WARRANT-F assurance/admission architecture.

### Whole Project Operating Architecture synthesis

Research 309/310 recognized one integrated Project operating architecture:

```text
HUMAN / AGENT / EXTERNAL EVENTS
        ↓
ACTIVATION + ORCHESTRATION
        ↓
KNOWLEDGE / STATE / AUTHORITY
        ↓
ASSURANCE / ADMISSION
        ↓
EXECUTION + DELIVERY
        ↓
OBSERVATION / RECOVERY / EVOLUTION
        └────────────→ next cycle
```

### AO-10 semantic-authority reconciliation

Later integration exposed an unresolved issue:

> How should governing human meaning become reliable machine-operational control without asking a later semantic interpreter to reconstruct authority from prose?

R2 showed that the previous richer inference-authoritative reconstruction was underdetermined under the tested contract.

That opened the C1-C9 and D1-D3 successor-design program.

### THIN_CENTRED_HYBRID_V03

The successor semantic/control kernel was designed, challenged, qualified and owner-selected.

Decision:

```text
D-036
THIN_CENTRED_HYBRID_V03
OWNER DECISION = ACCEPT
```

### R0

The project has now moved from logical semantic/control selection into first-principles physical/software realization design.

This is the current stage.

---

## 6. The semantic-subject / hierarchy example

This is an important unresolved item.

### What Research 217 previously selected

Research 217 accepted a controlled navigation architecture containing:

```text
18 assignable semantic subjects
6 non-assignable navigation parents
polyhierarchy
preferred_subject
source-owned memberships
generated navigation projection
```

It performed materially better than unconstrained semantic interpretation in the tested corpus.

### What later work changed

Research 313 explicitly removed target-preservation rights from:

- the 18 subjects;
- the six parent nodes;
- polyhierarchy;
- preferred_subject;
- explicit source-owned membership;
- the catalog shape;
- even the assumption that the future architecture must be subject-based.

Research 313 preserved the empirical lessons, not the exact mechanism.

The future question became:

> What semantic organization, discovery, retrieval, activation and reconstruction architecture should the professional ADS Project System have now?

Research 315/316 preregistered **DRP-02: SEMANTIC NAVIGATION ARCHITECTURES**, but the later path did not execute a final DRP-02 selection.

Therefore:

```text
FINAL_SEMANTIC_ORGANIZATION_ARCHITECTURE = OPEN
RESEARCH_217 = EMPIRICAL_EVIDENCE / COMPARATOR
OLD_18_SUBJECT_VOCABULARY = NO PRESERVATION RIGHT
```

### Required correction to the current R0 program

Before final physical architecture selection, the R0 program should explicitly include a dedicated semantic-organization/navigation obligation.

That work should:

1. derive requirements from first principles;
2. compare materially different architectures;
3. use Research 217 as one fair comparator;
4. test human navigation;
5. test fresh-agent reconstruction;
6. test retrieval/context selection;
7. test AO activation;
8. test impact analysis;
9. test migration reasoning;
10. test architecture-evolution support;
11. either select a target or explicitly preserve a bounded unresolved choice.

This should be made explicit in the R0 charter/handoff before Claude's independent physical-design response.

---

## 7. What R0 is actually doing

R0 is **not just choosing folders and Python modules**.

Its task is to determine the concrete professional realization of the integrated Project System.

That includes potentially redesigning:

```text
repository topology
files/folders
canonical source forms
schemas
serialization
storage
indexes
caches
packages/modules
APIs
CLI
UI
AO hosting/runtime model
WARRANT-F execution model
semantic organization/navigation
predicate runtime
J1/J2/J3 machinery
lineage
orientation
tests
test hierarchy
CI/CD
branch strategy
merge/review workflow
collaboration procedures
concurrency
recovery
migration tooling
rollback
observability
deployment
documentation architecture
```

No current mechanism has automatic preservation rights.

Existing mechanisms are:

- evidence;
- current-authority constraints where genuinely live;
- migration inputs;
- possible reusable material.

They are not target constraints.

---

## 8. Activation / Orchestration status

AO is already substantially designed logically.

It includes ideas such as:

- event/intent activation;
- knowledge activation;
- governing-process activation;
- workstream routing;
- collaborator/tool routing;
- ActionShape;
- preflight/postflight;
- Git lifecycle;
- recovery and continuity;
- architecture-evolution triggers;
- AO-4;
- control observations;
- successor bridging.

What remains open is exact production realization.

R0 must decide questions such as:

```text
Is AO a library, CLI, service, daemon, or multiple components?

How is AO state persisted?

Which parts are canonical versus derived?

How does ChatGPT enter the system?

How does Claude enter the system?

How does Codexless enter the system?

How does GitHub enter the system?

How are ActionShapes represented?

How does AO bind to V03 accepted effects?

How does AO invoke WARRANT-F?

How do assurance results re-enter AO?

How is recovery persisted?

How are concurrent/stale actions prevented?

What is local versus remote?

What is checked in CI?
```

Expected sequence:

```text
AO logical architecture
        ↓
V03 semantic/control integration
        ↓
R0 physical realization design
        ↓
R1 physical contract
        ↓
R2 production implementation
        ↓
shadow + migration + untouched qualification
        ↓
authority switch
```

---

## 9. WARRANT-F / CI/CD status

WARRANT-F is broader than CI/CD.

Its logical architecture includes:

```text
CLAIM
VERIFIER
WARRANT
GATE POLICY
PROFILE
EVIDENCE
DECISION
PLANNER
```

and concepts such as:

- exact subject/revision binding;
- evidence freshness;
- trust semantics;
- verifier warrants;
- base-revision policy ratchet;
- exact-result promotion;
- stochastic versus deterministic qualification;
- public/private held-out evidence;
- assurance/orchestration/delivery separation.

Research 311 explicitly did **not** permanently select:

- branch model;
- PR model;
- merge queue;
- direct-push policy;
- GitHub Actions;
- CI provider;
- runner provider;
- host-protection mechanism;
- identity provider;
- status/check publisher;
- exact test framework;
- evidence store;
- deployment provider;
- release topology.

Those remain realization questions.

Therefore R0 must turn WARRANT-F's logical guarantees into an actual professional CI/CD/assurance architecture.

---

## 10. WMR-H status

WMR-H provides important representation principles, including distinctions among:

- human-authored knowledge;
- machine-readable governed metadata;
- machine-maintained state;
- generated non-authoritative views;
- query/search indexes;
- recovery/rebuild behavior.

Its accepted direction is evidence and architectural input.

However, current R0 has explicit first-principles freedom over the exact physical realization.

Therefore WMR-H should be preserved where it wins on merit, refined where needed, or reimplemented behind the same logical guarantees.

---

## 11. Current operational authority versus selected successor

This distinction must remain explicit.

### Selected successor target

```text
THIN_CENTRED_HYBRID_V03
```

is selected as the intended successor semantic/control architecture.

### Current operational authority

```text
Specification 028
+ currently accepted continuity surfaces
```

still governs actual current implementation/migration behavior.

Therefore:

```text
ARCHITECTURE_TARGET_SELECTED = true
PRODUCTION_TARGET_SELECTED = true

PRODUCTION_ACTIVATED = false
PHYSICAL_MIGRATION_AUTHORIZED = false
AUTHORITY_SWITCH_AUTHORIZED = false
```

"Production target selected" means intended future production target, not deployed/current authority.

---

## 12. What "migration" will eventually mean

The current phase is **not migration**.

Future migration means moving the live Project-development system from current authority/representation into the selected successor realization.

That may eventually affect:

- current Project knowledge;
- current identities and authority records;
- current routing/state/continuity surfaces;
- current `tools/project_knowledge`;
- tests;
- CI/CD;
- branch/workflow procedures;
- collaboration mechanisms;
- storage/indexes;
- knowledge carriers;
- semantic navigation;
- AO integration;
- WARRANT-F integration;
- recovery;
- migration/rollback tooling.

It is primarily a **Project System migration**, not a rewrite of ADS Product algorithms under V03.

The Product plane remains a separate bounded domain, though repository/workspace boundaries may be affected by the final whole-repository realization.

---

## 13. Status of W0-W5 and old architecture

W0-W5 are neither "still the unquestioned final target" nor "discarded."

Their current role is:

```text
historical implementation evidence
qualification evidence
migration evidence
compatibility evidence
possible reusable mechanisms
possible test oracles
```

Later architecture may:

- preserve;
- refine;
- reimplement;
- use as compatibility only;
- use as migration source;
- retire after successor;
- supersede explicitly.

Important distinction:

```text
superseded as future target
    !=
already removed from current operational authority
```

Specification 028 still governs current operations until an explicit later cutover.

---

## 14. PSMF / reusable external framework plan

PSMF remains part of the longer-term architecture.

The intended relationship is:

```text
generic Project architecture/framework
        ↓ materialization
project-specific complete local Project System
```

The local project should remain self-contained and sovereign.

However, the project has deliberately postponed extraction of the generic framework.

Current plan:

```text
design through ADS
        ↓
implement through ADS
        ↓
migrate ADS
        ↓
operate / qualify ADS
        ↓
learn what is actually reusable
        ↓
only then extract the generic framework
```

This prevents speculative over-generalization.

---

## 15. Codexless Runtime Bridge ownership and future professionalization

Codexless Runtime Bridge is now explicitly treated as **reusable external developer infrastructure**, not as a generic subsystem that ADS should canonically own forever.

Its generic role is approximately:

```text
ChatGPT / compatible caller
        ↓
bounded trusted capability surface
        ↓
local machine / repositories / Git / GitHub / browser / tools / processes
```

The long-term ownership direction is:

```text
STANDALONE RUNTIME BRIDGE PRODUCT
    generic source
    architecture
    security model
    capability interfaces
    tests / CI / releases / docs

PRIVATE HOST / DEPLOYMENT STATE
    credentials references
    machine-specific deployment/configuration
    private runtime evidence

ADS
    ADS requirements
    ADS workspace/policy configuration
    ADS-specific capability packs/adapters
    qualified Runtime Bridge version
    AO / WARRANT-F integration
    ADS-specific qualification evidence
```

The current `autonomous-data-science-system-local-runtime` repository must be classified before deciding whether it should remain ADS-specific, be split, or become part of a more generic private deployment boundary.

Runtime Bridge is related to PSMF only by analogy. PSMF materializes a project-sovereign Project System. Runtime Bridge is more naturally a reusable external execution/tool product that can be configured or extended for many projects.

R0 must therefore define a provider-neutral execution/action-adapter boundary so that:

```text
Project System / AO
    -> executor interface
        -> Codexless Runtime Bridge
        -> GitHub connector
        -> Claude-side connector
        -> local/direct executor
        -> future executors
```

The dedicated Runtime Bridge extraction/professionalization program is **future work**, not the current R0 migration. Existing ADS Runtime Bridge research remains valid historical evidence and should not be rewritten.

Authoritative design-input record:

```text
docs/research/506_codexless_runtime_bridge_standalone_product_boundary.md
```

---

## 16. Exact forward plan

### R0: integrated realization requirements and physical/software architecture

**Current active stage.**

Goals:

- make all remaining logical obligations explicit;
- include semantic organization/navigation explicitly;
- compare physical architecture alternatives;
- independently design whole-system realizations;
- reconcile AO, V03, WARRANT-F, information architecture, WMR-H, engineering, workflow, recovery and migration;
- run focused probes where real uncertainty remains.

### R1: accepted physical realization contract

Freeze the concrete target after R0 comparison and evidence.

Expected output should make it possible to answer:

- what components exist?
- where do they live?
- what is authoritative?
- what is generated?
- how do they communicate?
- how is concurrency handled?
- how does AO work physically?
- how does WARRANT-F work physically?
- how is semantic organization implemented?
- how are tests and CI/CD structured?
- how is the successor migrated and recovered?

### Prospective specification/authority reconciliation

Before major successor implementation, reconcile Specification 028 with the selected realization so implementation does not operate under contradictory governing contracts.

### R2: production-quality successor implementation

Build the actual Project System.

This includes, as selected by R1:

- V03 mechanisms;
- AO production realization;
- semantic organization/navigation;
- J2/J3;
- lineage;
- orientation;
- WARRANT-F integration;
- engineering/verification tooling;
- indexes/query surfaces;
- CLI/API/UI as justified;
- recovery;
- validation;
- CI/CD;
- workflow;
- observability.

### R3: semantic migration inventory

Inventory live current semantics by responsibility and obligation, not merely by existing file path.

Every live legacy item receives a disposition, such as:

- preserve;
- translate;
- replace;
- split;
- merge;
- retire;
- compatibility-only;
- historical-only;
- unresolved.

### R4: shadow realization and semantic parity

Run the successor without giving it authority.

Compare:

- semantic decisions;
- reconstruction;
- AO activation;
- control outputs;
- assurance;
- orientation;
- recovery behavior.

### R5: bounded reversible migration waves

Migrate only qualified scopes.

Each wave needs:

- lineage closure;
- no duplicate authority;
- semantic parity;
- reverse-reference safety;
- evidence/qualification closure;
- rollback evidence.

### R6: untouched confirmation and cutover qualification

Use fresh/untouched evaluators and the actual implementation/migrated state.

Re-test:

- acceptance authenticity;
- closed accounting;
- completion authority;
- J2/J3 separation;
- lineage;
- semantic organization/retrieval;
- AO activation;
- orientation;
- WARRANT-F;
- rebuildability;
- concurrency;
- interruption/recovery;
- public/private degradation;
- rollback;
- fresh-collaborator reconstruction.

### R7: explicit authority-switch decision

Only after R6.

The owner explicitly decides whether the successor becomes operational authority.

### Later: reusable-framework extraction

After actual operational evidence, revisit PSMF / Generalizable Project Operating Architecture extraction.

---

## 17. Current independent-design plan

The project opened MC-0030 using:

```text
INDEPENDENT_THEN_COMPARATIVE
```

Sequence:

```text
neutral R0 requirements
        ↓
ChatGPT independent physical/system design
        ↓
freeze
        ↓
Claude independent design while blind to ChatGPT design
        ↓
freeze
        ↓
comparative exposure
        ↓
reconciliation
        ↓
decision-relevant probes
        ↓
physical target decision
```

Important correction before Claude:

```text
explicitly add semantic organization/navigation
as a named R0 obligation
```

so Claude and ChatGPT are both solving the whole intended Project System problem.

---

## 18. Completion checklist

### Completed or selected

- [x] Earlier PKA-CANDIDATE-01 selected and implemented/qualified through major W0-W5 stages
- [x] Activation/Orchestration architecture developed substantially
- [x] AO-4 architecture-evolution governance designed
- [x] PSMF direction established
- [x] G-DUAL Product/Project split accepted
- [x] R6 professional responsibilities/bounded contexts accepted
- [x] R7 Project information-role architecture accepted
- [x] R8-A realization architecture evidence produced
- [x] WMR-H representation architecture accepted as direction/evidence
- [x] WARRANT-F assurance/admission architecture accepted
- [x] Whole Project Operating Architecture synthesis established
- [x] Semantic architecture explicitly reopened from first principles
- [x] R2 underdetermination preserved
- [x] C1-C9 successor semantic/control evidence completed
- [x] D3 dependency proof passed
- [x] D2 extended lineage qualified at mechanism level
- [x] D1 real integrated replay executed and reconciled
- [x] THIN_CENTRED_HYBRID_V03 owner-selected
- [x] MC-0029 resolved
- [x] R0 opened
- [x] Neutral R0 physical-realization charter frozen
- [x] ChatGPT independent R0 physical candidate frozen
- [x] Runtime Bridge long-term standalone-product ownership boundary captured

### Explicitly still open before physical-target selection

- [ ] Amend/strengthen R0 so semantic organization/navigation is an explicit named obligation
- [ ] Add the Runtime Bridge/external-executor ownership boundary explicitly to the neutral R0 charter
- [ ] Run Claude blind independent R0 whole-system design
- [ ] Compare independent ChatGPT and Claude physical/system architectures
- [ ] Reconcile into one candidate or bounded finalist set
- [ ] Perform first-principles semantic-organization/navigation comparison
- [ ] Use Research 217 as comparator/evidence, not inherited answer
- [ ] Resolve any other architecture choices that remain decision-relevant
- [ ] Run the smallest necessary empirical probes for uncertain mechanisms
- [ ] Freeze/select the physical/software realization target

### After physical-target selection

- [ ] Reconcile/amend successor governing specifications prospectively
- [ ] Implement production-quality successor Project System
- [ ] Implement concrete AO realization
- [ ] Implement concrete WARRANT-F / CI/CD / admission realization
- [ ] Implement selected semantic organization/navigation
- [ ] Implement V03 J1/J2/J3, completion, lineage and orientation
- [ ] Implement recovery/rebuild/concurrency/public-private behavior
- [ ] Inventory current live legacy semantics
- [ ] Define exact migration graph and dispositions
- [ ] Run shadow realization
- [ ] Execute bounded reversible migration waves
- [ ] Perform untouched/fresh confirmation
- [ ] Rehearse rollback/recovery
- [ ] Seek explicit owner cutover/authority-switch decision
- [ ] Retire legacy compatibility/oracles only after qualified successor authority
- [ ] Reassess generic PSMF/framework extraction after operational experience
- [ ] Run a dedicated Codexless Runtime Bridge extraction/professionalization program after ADS's execution-interface requirements are stable

---

## 19. "Do not confuse these" quick reference

### V03 versus AO

```text
V03
    what governing semantic truth is
    how accepted effects are identified
    how realization maps to them
    how operational truth is derived

AO
    what event happened
    what should activate
    what governed process applies
    who/what should act
    what happens next
```

### V03 versus WARRANT-F

```text
V03
    governing consequences + realization + J3 truth

WARRANT-F
    what evidence/verification/warrant is required
    before an exact consequence is admissible
```

### Information architecture versus semantic organization

```text
information architecture
    what role information plays
    who naturally owns it
    where responsibility belongs

semantic organization
    what information means
    what it concerns
    how concepts relate
    how humans/agents discover and navigate it
```

### Selected logical architecture versus implementation

```text
selected logical architecture
    guarantees / semantics / authority / responsibilities

physical realization
    repository / packages / storage / APIs / workflow / CI / runtime

implementation
    actual production code and infrastructure

migration
    moving live current authority/data/control into successor

cutover
    switching operational authority
```

---

## 20. Key source map

This overview is intentionally secondary. Important authoritative/evidence sources include:

```text
Research 217
    W5 controlled semantic-subject architecture evidence

Research 219+
    Activation / Orchestration program

Research 238
    PSMF reconciliation

Research 245-248
    G-DUAL Product/Project architecture

Research 249-251
    R6 responsibilities / bounded contexts

Research 253-256
    R7 Project information architecture

Research 257+
    R8 exact realization progression

Research 272
    WMR-H acceptance

Research 273-311
    WARRANT-F assurance architecture and qualification

Research 309-310
    whole/generalizable Project operating architecture synthesis

Research 313
    explicit first-principles semantic architecture reopening
    and whole-system integration requirement

Research 314-316
    integrated-system reconciliation and DRP planning,
    including semantic-navigation DRP-02

Research 500
    THIN_CENTRED_HYBRID_V03

Research 502
    V03 owner selection and realization-program opening

Research 503
    R0 physical/software realization charter

Research 506
    Codexless Runtime Bridge standalone-product boundary and extraction obligation

Specification 028
    current operational implementation/migration authority

docs/DECISIONS.md
    accepted decisions including D-036
```

---

## 21. Update policy for this file

This file should remain deliberately lightweight in authority terms.

It may be updated when:

- a major architecture stage closes;
- a major new stage opens;
- an old target is superseded;
- an important unresolved obligation is discovered;
- migration/cutover status materially changes.

It should **not** become:

- a second source of truth;
- a substitute for accepted research;
- a hidden specification;
- an implementation contract;
- an authority oracle.

If the future Project System provides a better orientation/reconstruction view, this file may simply be retired.

---

## 22. Current "you are here" marker

```text
MAJOR LOGICAL ARCHITECTURE
    mostly established
            ↓
V03 semantic/control kernel
    selected
            ↓
remaining semantic-organization obligation
    still open
            ↓
R0 integrated physical/software architecture
    CURRENT
            ↓
independent designs
            ↓
comparative reconciliation + focused probes
            ↓
R1 physical target
            ↓
R2 implementation
            ↓
R3 semantic migration inventory
            ↓
R4 shadow
            ↓
R5 bounded migration
            ↓
R6 untouched confirmation
            ↓
R7 explicit authority switch
            ↓
operate / learn / evolve
            ↓
eventual generic framework extraction if justified
```
