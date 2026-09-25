# MC-0029 Message 001: Claude Independent Specification 028 Reconciliation and AO-10 Realization Design — KEYSTONE

```text
Thread                          MC-0029
Message                         001
Author / collaborator           Claude
Role                            INDEPENDENT_REVIEWER / RESEARCHER / CRITIC / COUNTER_DESIGNER
Interaction environment         Claude
Interaction session             claude-04
Conversation title              04 - Assurance and Delivery Architecture Design
Coordination branch             v1-source-vault-bootstrap-resume
Frozen independent base         0a68787aee5f2c6332d6ee1fb6adbf0efe92a41d
Mode                            INDEPENDENT_THEN_COMPARATIVE / independent design
Architecture name               KEYSTONE — one semantic kernel, many governed projections
Authority                       Collaboration evidence only. Selects nothing. Authorizes nothing.
```

## 0. Independence boundary and material read

**Read at branch head `21ffc1a5…`, for instructions only:** `docs/current_routing.json`, `docs/model_collaboration/REVIEW_INBOX.md`, and MC-0029 `BRIEF.md`, `THREAD.md` and `STATE.json`. The commit list at head shows that a ChatGPT commit freezing a Specification 028 / AO-10 candidate exists. I read none of its content, did not open Research 312 or any file added after the frozen base, and inferred nothing from commit titles. The owner clarification in the brief (semantic architecture has no preservation right; one integrated professional Project system) is applied as instruction.

**Read at the frozen base `0a68787…` (local checkout of that exact commit):**

- Specification 028 in full.
- Research 311, 309, 310 and 235 in full.
- Research 276: opening sections and the WF-A34 to WF-A36 sections.
- Research 222 §2, §14, §18 and §24.
- Research 226 §2 to §4, §13, §19 and §21.
- Research 217 in full.
- The tail of Research 256.
- Research 301 §3 to §5.
- The section headings of Research 219 to 226.
- Requirements V0.2: KA-R51, KA-R52, and invariants KA-I01 to KA-I09.
- Repository inventory: the JW1 package, schemas and generated views, the count of carriers using the current structured-declaration marker, the test inventory, and the sizes of `CURRENT_STATE.md`, `KNOWLEDGE_MAP.md` and `CONTINUITY.md`.

I also carry my MC-0028 work (Messages 001 and 003), which is within the base.

**Not used:** external web sources. This design question is internal to accepted ADS architecture; no current external fact changes it.

## 1. Summary

**Thesis.** The accepted layers — Candidate 01 semantics, Research 217 navigation, AO-3 to AO-7, WMR-H, WARRANT-F, and the KA-R51 and KA-R52 needs — were each designed well in isolation. Together they now carry at least **five partially overlapping type systems**:

```text
Candidate 01 declarations   authority_class, kind, profile, relations, scope
Research 217 navigation     subjects, parents, preferred routes
AO logical records          EventInterpretation ... ControlObservation
WARRANT-F                   claims, warrants, evidence, gate policy, decisions
KA-R52 (not yet realized)   obligations, realization paths, deferrals
```

The owner's integration requirement is best met by **one small semantic kernel**. Every other layer becomes a governed projection or a consumer of it, not a peer type system. That kernel is KEYSTONE.

**Headline dispositions:**

```text
SPECIFICATION 028          PROSPECTIVELY SUPERSEDE AS A WHOLE, via three successor
                           contracts split by change rate and owner (§6); clause-level
                           lineage for every section; Spec 028 keeps temporal
                           authority over current-layout operation until each
                           successor clause is effective

SEMANTIC KERNEL            RETAIN selective identity, path != identity/authority,
                           natural-owner relations, the four governing relation modes,
                           capture != promotion, derived != truth
                           SPLIT authority_class into ROLE x STATUS (§4.2)
                           ADD obligation units + REALIZES / DEFERS relations (§11)

RESEARCH 217               RETAIN its membership rules and calibration method
                           SUPERSEDE its 18-subject vocabulary and 6 parents; it was
                           derived from a pre-G-DUAL corpus and conflates owner,
                           plane and concern (§5)
                           REPLACE with ownership position + small concern vocabulary
                           + relations + derived search, qualified against 217 itself

AO-10                      a deterministic JW1 control protocol (begin / preflight /
                           postflight) hosted by any executor; model assistance
                           only where input is unstructured (§9)

KA-R52                     realized through obligation units linked to WARRANT-F
                           claims or to governed realization/deferral records;
                           "no third state" becomes itself a warranted claim (§11)

KA-R51                     control observations as machine captures from four
                           mechanical detectors, qualified with AO-9 corpus
                           witnesses (§10)

CURRENT LIVE SURFACES      current_routing -> control state + projection
                           CURRENT_STATE   -> bounded generated orientation +
                                              milestone history; no live carrier
                                              may accumulate narrative (§14)

UPSTREAM REOPEN            none required; two AO-4 CLARIFY items are recorded (§21)
```

## 2. Evidence from the frozen base

```text
E1  SUCCESSOR ADOPTION IS NEAR ZERO
    After W0-W4 acceptance, about ten live carriers (outside research
    fixtures and collaboration threads) carry the current structured-
    declaration marker. The successor semantic system exists but governs
    almost nothing.

E2  THE LEGACY LIVE SURFACE KEEPS GROWING
    CURRENT_STATE.md is 413 KB (the MC-0028 base had about 388 KB);
    649 checkpoints; KNOWLEDGE_MAP.md is 90 KB. The live-state carrier
    accumulates chronological narrative. This is the largest daily cost,
    and the one the migration most needs to remove.

E3  ACCEPTED OBLIGATIONS WENT UNREALIZED WITHOUT TRACE
    Spec 028 §3 requires reconstruction, migration, validation and git
    responsibility modules; none exists in tools/project_knowledge at the
    base. AO-1 found the reconstruction planner selected but not
    implemented; AO-9 found the AO-6 ROTATE gap. These are KA-R52's own
    evidence and ideal sensitivity witnesses for its realization.

E4  authority_class CONFLATES TWO AXES
    Spec 028 §9 values {canonical, candidate, historical, derived, evidence,
    capture} mix WHAT KIND of information a carrier is (governing /
    evidence / derived / capture) with WHERE it is in a governing lifecycle
    (candidate / in force / historical). "historical" cannot say whether a
    governing record was superseded, retired, or never accepted, although
    KA-I04 requires those states to stay distinguishable.

E5  RESEARCH 217'S VOCABULARY PREDATES THE ACCEPTED ARCHITECTURE
    The 18 subjects mix Product-plane concerns (runtime-persistence,
    retrieval-context, recommendation-action, methodological-knowledge,
    source-universe) with Project-plane concerns (project-orchestration,
    development-governance, model-collaboration, tooling-integrations).
    Four of the 18 are cockpit-* subjects, reflecting the cockpit-era corpus
    density. One subject is named after a retired implementation identity
    (project-knowledge-architecture). Its comparator was the legacy
    Knowledge Map, not an ownership-tree + relations + search alternative.

E6  REPRESENTATION-INDEPENDENT SEMANTICS SURVIVE
    P-D4 (Research 301/304) showed the routing oracle's invariants survive a
    deliberate representation change when translated. The same method
    applies to every current live surface.

E7  AO RECORDS ARE LOGICAL, NOT YET REPRESENTED
    AO-3 §14 selects logical records without storage; AO-7 defines bridge
    modes DISABLED / SHADOW / ACTIVE_SUBORDINATE / SUSPENDED and an
    authority membrane; AO10-Q01..Q06 and O01..O02 are the qualification
    envelope.

E8  CONVENIENCE INDICES DRIFT WHEN HAND-MAINTAINED
    REVIEW_INBOX.md contradicted thread STATE.json during MC-0028 (Message
    003 §X1). A hand-maintained projection of machine state is a
    recurring defect class.

E9  WARRANT-F ALREADY OWNS "REALIZATION -> EVIDENCE -> QUALIFICATION"
    Its claim -> verifier -> warrant -> evidence -> decision chain is the
    same shape KA-R52 requires for verifiable obligations.
```

## 3. What the Project system must do

Before choosing mechanisms, these are the functions the integrated system exists for. Every KEYSTONE element is justified against them.

```text
PF1  HOLD governing meaning with its temporal status (what governs now,
     what governed when, what was superseded or rejected)
PF2  KNOW current operating state (focus, workstreams, bridge/authority
     mode, collaboration obligations) and recover it without derivatives
PF3  ACTIVATE what applies to an event (obligations, governing sources,
     procedures, triggers) without owner reminder
PF4  GATE consequential action on authority, action contract and assurance
PF5  REMEMBER accepted obligations until realized or explicitly deferred
PF6  PRESERVE evidence and receipts proportionally to consequence
PF7  EVOLVE itself through governed cases, never silently
PF8  NAVIGATE for humans and agents at bounded cost
PF9  TRANSITION between architectures without losing authority or history
```

## 4. The semantic kernel

### 4.1 Kernel principle

One small typed model is shared by knowledge, JW1, AO, WARRANT-F and migration. Layers may add **projections** (derived views), **records** (representations of kernel objects) and **consumers**. They may not add a parallel type system for the same meaning.

### 4.2 Two axes replace authority_class

```text
ROLE    what kind of information a carrier/record is
        GOVERNING   states what must hold / what is decided
        EVIDENCE    observes, measures or records what happened
        CONTROL     machine-maintained operating state (JW1 writer)
        PROPOSAL    capture / candidate / unaccepted suggestion
        DERIVED     rebuildable projection; never truth

STATUS  where a GOVERNING (or PROPOSAL) item is in its governing lifecycle
        PROPOSED    under consideration; not in force
        IN_FORCE    governs prospectively from an effective boundary
        HELD        in force but its effect is suspended by a governed hold
                    (AO-4 AFFECTED_SCOPE_HOLD)
        SUPERSEDED  replaced by an identified successor from a boundary
        RETIRED     no longer governs; no successor
        REJECTED    considered and not accepted
```

Mapping from Spec 028 §9: `canonical` becomes GOVERNING and IN_FORCE. `candidate` becomes PROPOSAL, or GOVERNING and PROPOSED. `historical` becomes GOVERNING with one of SUPERSEDED, RETIRED or REJECTED — the split E4 requires. `evidence`, `derived` and `capture` map directly to EVIDENCE, DERIVED and PROPOSAL.

EVIDENCE, CONTROL and DERIVED carry no governing status. Evidence is never "superseded". It remains true about what it observed; later evidence may outweigh it.

### 4.3 Identity (RETAIN)

Selective durable identity: identity is not the path, the blob or the title, and an identifier is minted only where continuity or cross-reference matters. Transition classes are retained (Spec 028 §11). The index is derived and rebuildable.

### 4.4 Relations: a closed set in five families

```text
GOVERNING     REPLACES | SUPPLEMENTS | SPECIALIZES | CORRECTS     (RETAIN)
SUPPORT       EVIDENCED_BY | DERIVED_FROM                          (formalize)
REALIZATION   REALIZES | DEFERS                                    (ADD; §11)
DEPENDENCY    DEPENDS_ON | CHILD_OF                                (workstreams)
TRIGGER       REOPENS_IF                                           (risk/reopen)
```

Every relation is authored once, by its natural owner end; reverse edges and closure are derived (RETAIN, Spec 028 §12). A new relation type is itself a governed kernel change. The closed set is what keeps authoring, validation, witnessing and navigation cost bounded.

### 4.5 Scope, applicability and time (RETAIN)

Explicit scope is required where applicability is not global. Temporal fields are selective. Latest commit never substitutes for authority (Spec 028 §14).

### 4.6 Kernel object kinds

```text
GOVERNING   Decision | Contract | Policy | Procedure(+ActionContract) |
            Requirement
            each may contain OBLIGATION UNITS (§11)
CONTROL     Workstream | FocusState | BridgeState | AuthorityMode |
            CollaborationThreadState | EvolutionCase | RecoveryCase |
            RealizationState (per obligation unit)
EVIDENCE    ResearchResult | QualificationEvidence | Receipt (control /
            assurance-decision) | Milestone | ControlObservation
PROPOSAL    Capture (human-rich or machine-first)
DERIVED     indexes, orientation, navigation, compatibility projections
```

WARRANT-F claims, warrants, gate policies and profiles are GOVERNING Policy content owned by their semantic owners (per WARRANT-F). They are not a separate kernel. Assurance decisions are EVIDENCE.

This one move makes WARRANT-F, AO and knowledge share identity, status and relation semantics — and one validator family instead of three.

## 5. Semantic organization and navigation — first-principles disposition of Research 217

### 5.1 What navigation must do

Navigation serves PF8. It answers "what should I read to understand or act on X?" at bounded cost, for a cold human or agent. It must not carry authority (KA-I02) and must not duplicate facts owned elsewhere.

### 5.2 The duplication problem in the 217 pattern

Under accepted R7 and R8-A, a carrier's **position** already states its owner and responsibility: which plane, which Project context, and whether it is governance, evidence, operations or history. The 217 vocabulary predates that architecture and re-encodes much of the same information as subjects (E5). Examples:

```text
project-orchestration, development-governance        ~ Project contexts / areas
runtime-persistence, retrieval-context, ...          ~ Product contexts PC1-PC7
cockpit-product/-interaction/-visual/-implementation ~ one Product context (PC6)
                                                       plus design research
```

Two independent encodings of ownership drift, and E8 shows the project's drift rate for hand-kept parallel structures. What position cannot express is **cross-cutting concern**: security, assurance, recovery, provenance, architecture evolution, collaboration, cost, public/private boundary. That is the genuine job for a vocabulary.

### 5.3 KEYSTONE navigation model

```text
LAYER 1  POSITION           derived from the carrier's owner area under R7/R8-A
                            (no authored metadata)
LAYER 2  RELATIONS          the closed kernel relation set (§4.4), derived closure
LAYER 3  CONCERNS           small controlled vocabulary of CROSS-CUTTING concerns,
                            source-owned membership, selective
LAYER 4  SEARCH             derived SQLite/FTS (accepted by WMR-H); ranking never
                            confers authority
ENTRY    ORIENTATION        generated, bounded, per role (§14.2)
```

The concern vocabulary is derived from the accepted responsibility model and the assurance claim families, not from corpus frequency. It starts small (on the order of 8–12), is separately scoped per plane where meanings differ, and evolves through stable identifiers, aliases and redirects.

Product-owned knowledge, such as methodological knowledge (PC2), is Product content with Product navigation. It is not tagged into Project navigation.

### 5.4 Research 217 disposition

```text
RETAIN (evidence-backed, architecture-independent)
    membership threshold: assign only when the carrier substantively
      develops, governs, specifies, evaluates or preserves durable
      meaning about the concern
    every secondary membership clears the same threshold
    source-owned membership; no central member registry
    catalog holds vocabulary/parentage only
    polyhierarchy allowed; preferred route optional
    structural/resolver facets kept separate from navigation
    stable IDs + aliases + redirects for vocabulary evolution
    the blind-calibration METHOD (MC-0019/MC-0020) as the qualification
      pattern for any vocabulary

SUPERSEDE (with explicit loss accounting)
    the 18 assignable subjects and 6 parents
      loss: 217's 9/9 navigation-scenario result and 0.852 mean Jaccard
      are evidence for the old vocabulary against the legacy Knowledge
      Map; they become the BAR the successor must meet (P2), not a
      preservation right
    subjects as the primary organizing axis (replaced by position +
      relations; concerns become one of four layers)

ADD
    plane scoping of concern vocabularies
    explicit rule that a concern may not restate owner/position
```

If P2 (§20) shows position, relations and search alone meet the 217 bar, the concern layer shrinks to what the scenarios still need. If the 217 vocabulary beats every alternative on the same scenarios, that is a falsifier, and the vocabulary survives on merit.

## 6. Specification 028 disposition

### 6.1 Whole-document decision: prospectively supersede

Piecemeal amendment would leave a 46-section contract in which roughly half the clauses bind paths, formats and a wave program superseded by R8-A, WMR-H and WARRANT-F. Readers — human and machine — could no longer tell which clause governs. The KEYSTONE disposition is **prospective supersession by three successor contracts**, split by change rate and owner. It follows the permanent-mechanism versus one-time-migration separation (Research 258 AM-7) and the PSMF framework/instance seam.

```text
SC-1  PROJECT SEMANTIC CONTRACT               stable; framework-level
      kernel (§4), identity, relations, authority resolution, reconstruction
      semantics, capture/promotion, workstreams, procedures/action contracts,
      obligation units, source-revision descriptor, derived-view semantics
      owner: JW1 framework (PSMF candidate)

SC-2  ADS PROJECT-SYSTEM REALIZATION CONTRACT  changes with implementation
      JW1 modules and CLIs, WMR-H bindings per object kind, generated views,
      control-record placement, bridge, Engineering interfaces, WARRANT-F
      profile bindings, provider-neutral adapter boundary
      owner: ADS instance (JW1 instance + Engineering)

SC-3  R8 TRANSITION CONTRACT                  one-time; retires after W8
      migration waves (successor to W5-W8), unit dispositions, oracle
      retirement, compatibility projections, cutover, rollback, authority
      switch
      owner: ADS instance transition program (instance execution state)
```

**Temporal authority.** Spec 028 remains governing for the current layout until each successor clause becomes effective by governed decision. W0–W4 acceptance stays historically valid against Spec 028's gates (Research 235 §5 rule). Every Spec 028 section receives a lineage entry (§6.2); no clause silently lapses.

Why three and not one: SC-1 is the reusable-core candidate (Research 309), SC-2 is ADS-specific, and SC-3 must be able to retire whole. Merging them reproduces the mixed-lifetime problem that makes Spec 028 hard to amend now. §19 lists the falsifier if three contracts prove to be ceremony.

### 6.2 Clause lineage (condensed; all 46 sections)

```text
§   TOPIC                               DISPOSITION                -> SUCCESSOR
1   purpose / frozen boundary           RETAIN distinction logical /  SC-1, SC-3
                                        physical / operational
2   product/runtime separation          GENERALIZE to R8-A planes     SC-2
3   package surface tools/...           SUPERSEDE (R8-A JW1 modules)  SC-2
4   canonical source-location rule      RETAIN (natural owner)        SC-1
5   repository directories              SUPERSEDE (R7/R8-A)           SC-2
6   Markdown embedded JSON declaration  SUPERSEDE (WMR-H visible       SC-2 / SC-3
                                        TOML); legacy parser kept as
                                        transition reader until W8
7   native JSON carrier rule            GENERALIZE (writer-matched)   SC-2
8   profile schemas                     AMEND (kernel kinds; JSON      SC-1 / SC-2
                                        Schema over normalized data)
9   governed-source envelope            AMEND (ROLE x STATUS)          SC-1
10  semantic identity                   RETAIN                        SC-1
11  identity transitions                RETAIN                        SC-1
12  relation semantics                  AMEND (closed 5-family set)   SC-1
13  joint authority J1-J6               RETAIN                        SC-1
14  temporal semantics                  RETAIN                        SC-1
15  workstream profile                  AMEND (definition in           SC-1 / SC-2
                                        governing carrier; state as
                                        CONTROL record per WMR-H)
16  interruption / concurrency          RETAIN + WMR-H revision         SC-1 / SC-2
                                        history rule
17  procedure / action contract         RETAIN                        SC-1
18  source-revision descriptor          RETAIN                        SC-1
19  same-commit generated-view binding  RETAIN                        SC-1
20  persistent derived views (paths)    AMEND (bounded committed       SC-2
                                        orientation only; others
                                        uncommitted by default)
21  derived-view manifest               RETAIN semantics               SC-1 / SC-2
22  canonical JSON serialization        RETAIN                        SC-2
23  full rebuild                        RETAIN                        SC-2
24  incremental refresh                 RETAIN (+ WARRANT-F           SC-2
                                        HEAD_FULL audit)
25  authority resolver                  RETAIN statuses; bind to      SC-1
                                        ROLE x STATUS
26  reconstruction planner              RETAIN + REALIZE (E3)          SC-1 / SC-2
27  capture / promotion                 RETAIN semantics; paths        SC-1 / SC-2
                                        SUPERSEDED
28  public / private                    RETAIN                        SC-1
29  optional retrieval caches           RETAIN (WMR-H SQLite/FTS)     SC-2
30  compatibility surfaces              SUPERSEDE by §14 successors   SC-3
31  architecture documentation          AMEND (R7 knowledge homes)    SC-2
32  CLI contract                        AMEND (§8.3)                  SC-2
33  validation layers                   AMEND into WARRANT-F claims   SC-2
34  repository-integrity integration    SUPERSEDE (WARRANT-F; current SC-3
                                        aggregate = migration oracle)
35  migration waves W0-W8               SUPERSEDE (W0-W4 historical;  SC-3
                                        W5-W8 re-planned)
36  migration-unit dispositions         RETAIN vocabulary             SC-3
37  no mass historical conversion       RETAIN                        SC-1
38  research-code reuse                 RETAIN                        SC-2
39  W0 gates                            HISTORICAL (accepted)         —
40  W1 gates                            HISTORICAL (accepted)         —
41  documentation acceptance            AMEND                         SC-2
42  cutover qualification minimum       RETAIN + extend (bridge,      SC-3
                                        KA-R51/52, WARRANT-F G7)
43  authority-switch prohibition        RETAIN verbatim in substance  SC-3
44  non-goals                           RETAIN (re-validated)         SC-1 / SC-2
45  program states                      SUPERSEDE (SC-3 states)       SC-3
46  frozen continuation                 HISTORICAL                    —
```

## 7. The integrated system

### 7.1 One kernel, five roles

```text
               governed changes (AO-4)          owner decisions
                        |                             |
                        v                             v
  +-----------------------------------------------------------------+
  |                 KEYSTONE SEMANTIC KERNEL (JW1)                   |
  |  identity | ROLE x STATUS | relations | scope/time | obligations |
  +-----------------------------------------------------------------+
     ^ read/write via JW1        ^ read            ^ read          ^ read
     |                           |                 |               |
  KNOWLEDGE CARRIERS        AO CONTROL          WARRANT-F       NAVIGATION /
  (human + TOML meta)       (JW1 activation,    (Engineering    ORIENTATION
  CONTROL RECORDS           continuity,         kernel; claims   (derived)
  (JSON, JW1 writer)        evolution, bridge)  owned by owners)
                                 |                 |
                                 +--> admissibility requests --> decisions
                                 |                                  |
                                 v                                  v
                           ENGINEERING / DELIVERY: governed mutation after both
```

### 7.2 Seam rules

```text
SEAM                          RULE
knowledge <-> kernel          carriers hold meaning; kernel metadata only where
                              machine semantics are needed (WMR-H selective)
kernel <-> AO                 AO reads kernel objects; writes only CONTROL records
                              through JW1 transitions; never writes GOVERNING
                              status (only owner decisions do, via promotion)
AO <-> WARRANT-F              AO requests a profile for a consequence; the decision
                              returns as an AO event (Research 309 §6); neither
                              computes the other's result
kernel <-> WARRANT-F          claims are GOVERNING Policy objects with kernel
                              identity/status; assurance decisions are EVIDENCE
                              stored outside the qualified tree; control receipts
                              stay in-tree (Research 276)
AO/WARRANT-F <-> Engineering  Engineering mutates only with an AO transition AND
                              a required admission decision; Engineering invokes
                              JW1 by CLI/result contract (Research 311 §5)
everything <-> provider       provider mechanisms are adapters under WF-A36;
                              no kernel object names a provider mechanism
```

## 8. JW1 and Engineering realization boundaries

### 8.1 JW1 (project/system) capability modules

Realized only when implemented (Research 258 AM-5):

```text
semantics      kernel model, parsing (WMR-H readers), identity, relations,
               authority resolution, obligation units        RETAINED+AMEND
views          derived views, manifests, orientation, navigation, search
               index builder                                  RETAINED+AMEND
preservation   capture / review / promotion                   RETAINED
transitions    identity transitions, successor bridges, cutover/rollback
               mechanism, transition receipts                 PARTIAL -> REALIZE
reconstruction reconstruction planner (E3 gap)                PARTIAL -> REALIZE
activation     AO-3 control cycle, shape screen, obligation screening
                                                              PROSPECTIVE
continuity     AO-5 envelopes, continuation receipts, recovery cases
                                                              PROSPECTIVE
evolution      AO-4 EvolutionCase lifecycle                   PROSPECTIVE
workstreams    workstream + branch-role policy (AO-6 policy)  RETAINED+AMEND
```

PSMF seam: generic mechanism lives under the framework package. ADS policy — concern vocabulary, branch-role policy, trigger catalog, consequence thresholds — and ADS control state live in the instance.

### 8.2 Engineering (project/engineering; independent Python project)

```text
assurance kernel    WARRANT-F catalog, ratchet, evaluator, adapters (TCB)
host adapters       Git/host/CI/provider adapters, status publication
git mechanics       AO-6 mechanics: branch attach/switch/rotate/publish
                    (AO10-O01), exact-result promotion realization
delivery            governed mutators consuming decisions
transition ops      SC-3 migration orchestration, shadow runs, oracle
                    replay, cutover execution under JW1 transitions
bootstrap           one entry preparing Product / JW1 / Engineering envs
```

### 8.3 JW1 CLI and result contract (successor to Spec 028 §32)

```text
validate | rebuild | refresh | check-freshness            (retain)
resolve-authority <task-spec>                             (retain)
reconstruct <task-spec>                                   (realize)
control begin <event>        -> ControlObligationSet + ReconstructionContract
                                + RouteDecision
control preflight <proposal> -> shape screen + authority + action-contract
                                conformance result
control postflight <record>  -> receipts, captures, ControlObservations,
                                continuation receipt
obligations status [--scope]  -> realization coverage (KA-R52)
bridge status | bridge transition <mode>                  (AO-7)
evolution open | evolution status                         (AO-4)
```

Every command returns a JW1-owned, versioned result contract. Engineering adapts it (WARRANT-F consumer-side adaptation). JW1 never emits Engineering's evidence shape (WF-A13).

## 9. AO-10 realization

### 9.1 Execution model

AO is a **deterministic protocol plus a library**. It is not a daemon or a service. Any executor hosts it: a local CLI, the Runtime Bridge, or a hosted runner. There is no always-on process to keep alive, recover or secure. That is the property that keeps AO provider-neutral and makes break-glass recovery independent of AO being up.

```text
COLLABORATOR CLASSES (from WF-A34 capability model, not by model name)
  EXECUTING      can run JW1 (local, bridge, hosted)
                 -> full begin / preflight / postflight
  READ_ONLY      can read repository content only
                 -> reads generated orientation + control records
                    (break-glass readable); its proposed consequential
                    actions are pre-dispatch-screened when an EXECUTING
                    surface performs them
  NONE           owner-only / offline
                 -> CONTINUITY bootstrap procedure + anchor
```

This makes a present reality explicit: a model reading through a Git-host connector cannot run AO. Correct behavior for it must come from readable state, not from a service it cannot call.

### 9.2 AO-3 cycle realization

```text
S1 ingress + intent       model-assisted interpretation; explicit owner
                          directives recorded verbatim
S2 baseline context       deterministic: read FocusState, active Workstreams,
                          BridgeState, open EvolutionCases, pending
                          collaboration obligations
S3 obligation screening   deterministic predicates over S2 + event features
                          (trigger catalog REOPENS_IF, workstream conditions,
                          open obligations touching scope) + model-proposed
                          hypotheses that must name a kernel object to count
S4 reconstruction         deterministic closure (reconstruction planner)
S5 routing                deterministic policy over RouteDecision inputs;
                          executor chosen by capability (WF-A34)
S6 authority / action     deterministic resolver + ActionContract load
   contract preflight
S7 execute / hand off     executor
S8 pre-dispatch           AO9-P7-D01 SHAPE SCREEN:
   conformance            TOOL-MEDIATED actions (writes, pushes, ref changes,
                          dispatches) are classified DETERMINISTICALLY from
                          typed tool calls; only PROSE outputs (e.g. ordered
                          operational steps in an answer) need model-assisted
                          shape detection
S9 postflight             receipts, captures, ControlObservations,
                          continuation receipt, Git-lifecycle consequences
```

The S8 split matters for AO10-Q02 and Q03. Most consequential actions in ADS are tool calls, so the high-precision deterministic path covers them. The noisier model-assisted path is confined to prose. Probe P5 measures that split on real sessions.

Fast path: S1 to S3 with no activated obligations exits immediately. No reconstruction and no index rebuild are needed (Research 222 §18).

### 9.3 Record persistence (selective; WMR-H)

```text
RECORD                    PERSISTED?                    REPRESENTATION
EventInterpretation       no (session)                  —
ControlObligationSet      only in ContinuationReceipt   JSON (control)
ReconstructionContract    no (recomputable)             —
RouteDecision             only if consequential         within execution receipt
AuthorityReceipt          when consequential action     JSON receipt (control)
Execution/Handoff Receipt when consequential            JSON receipt (control)
ContinuationReceipt       when interruption possible    JSON (control)
ControlObservation        when material (§10)           JSON machine capture
EvolutionCase             always                        human carrier + JSON state
RecoveryCase              always                        JSON state + runbook ref
BridgeState               always                        JSON control record
```

### 9.4 AO-4, AO-5, AO-6, AO-7

- **AO-4.** EvolutionCase = a human governing-proposal carrier (rationale, evidence, disposition) plus a JSON control record (state, affected contract identifiers, hold scope). A disposition to AMEND or SUPERSEDE creates obligation units with REALIZES/DEFERS tracking. This closes the "decision is not realization" gap.
- **AO-5.** Interaction continuity envelopes and ContinuationReceipts are control records. Recovery authority lives in governing procedures; transport is an executor concern. Break-glass: `project_anchor.json`, then the control-state locator, then governing knowledge, with no derivative needed.
- **AO-6.** Branch roles (ACCEPTED_STATE, COORDINATION, EXPERIMENT, FROZEN, …) are JW1 instance policy. Lifecycle actions are JW1 transitions. Mechanics are Engineering host adapters. AO10-O01 (attach, switch, rotate, reconcile) is an Engineering mechanic with a JW1 policy check before it and a receipt after it.
- **AO-7.** Bridge modes as defined, persisted as BridgeState. Transitions between modes are governed (§16).

## 10. KA-R51 control-miss observability

Four mechanical detectors produce candidate ControlObservations:

```text
D1 OWNER-REMINDER DETECTOR
   owner event references a kernel object (obligation, trigger, procedure,
   workstream, open case) that S3 SHOULD have activated earlier: its
   activation condition was already satisfied in a prior cycle's S2 state
   -> candidate miss

D2 LATE-ACTIVATION DETECTOR
   an obligation activates in cycle n whose condition was satisfied in an
   earlier cycle m < n -> candidate miss with measured lag

D3 DOWNSTREAM-CATCH DETECTOR
   WARRANT-F REFUSE/REVIEW, or a conformance failure, that a declared
   earlier control stage was responsible for preventing -> candidate miss

D4 TRIGGER AUDIT (scheduled)
   recent events x REOPENS_IF catalog -> unmatched intersections
```

Precision rules:

- Candidates carry a consequence estimate. Below a threshold they are aggregated counts, not individual captures.
- Candidates are PROPOSAL-role machine captures. They are never architecture changes (KA-R51 text). Periodic triage feeds AO-4 intake.
- D1 requires the owner's reference to resolve to a kernel object. Free-text reminders go to a model-assisted secondary queue, labelled lower-confidence.

Qualification as WARRANT-F claims:

- **Sensitivity witnesses:** AO-9 preregistered historical scenarios in which a miss or owner reminder occurred, plus the Research 124 failure corpus cases.
- **Specificity witnesses:** ordinary low-consequence interactions that must produce no candidate.

## 11. KA-R52 obligation realization traceability

### 11.1 Obligation units

Per-MUST tracking is disproportionate: Spec 028 alone has 104 MUST occurrences across 94 lines. Tracking only per document hides unrealized parts (E3 happened inside an accepted document).

```text
OBLIGATION UNIT := the smallest group of accepted MUST statements that share
                   ONE realization boundary and ONE evidence path

declared in:       the governing carrier's visible TOML metadata (WMR-H),
                   with stable unit IDs and the section anchors they cover
granularity rule:  split when parts realize at different gates or by
                   different owners; merge when they always realize together
```

### 11.2 Realization links

```text
unit --REALIZES<-- realization object, one of:
       WARRANT-F claim (machine-verifiable property)          preferred
       implementation module / CLI contract + its claim
       procedure (human-executed) + evidence expectation
       owner decision (normative-only obligations)
       activation (AO trigger/obligation for runtime behavior)

unit --DEFERS<--  governed deferral record:
       reason, blocking dependency, reactivation/closure condition,
       future evidence path, owner/decision reference

RealizationState (CONTROL, JW1-written):
       UNLINKED | LINKED | EVIDENCED | QUALIFIED | OPERATIONAL | DEFERRED
```

### 11.3 No third state as a warranted claim

A WARRANT-F governance claim, bound at G2 over all IN_FORCE governing carriers:

> Every obligation unit is LINKED or beyond, or DEFERRED with a valid deferral.

Its sensitivity witnesses are the real historical gaps: the Spec 028 §3 missing modules, the reconstruction/CLI realization gap and the AO-6 ROTATE gap (E3). A correct realization must surface all three from the historical state.

**Scope rule.** It applies to carriers whose status is IN_FORCE after the rule's own effective boundary. Historical acceptance is not retro-audited, per Research 235 §5. Adoption for pre-existing IN_FORCE contracts is itself an SC-3 migration obligation.

## 12. WMR-H integration

```text
OBJECT                         REPRESENTATION (WMR-H)
governing carriers             Markdown + visible TOML metadata (selective)
obligation units               TOML in governing carrier metadata
instance policy (vocabulary,   TOML
 branch roles, triggers,
 thresholds, WARRANT-F policy)
control records                sharded pretty JSON; expected-revision writes;
                               monotonic revision history over commits
receipts (control)             individual immutable JSON, content-derived locator
assurance decisions            outside the qualified tree (WARRANT-F)
captures                       writer-matched (Markdown or JSON)
orientation                    generated current.md / current.json (bounded)
indexes / navigation / search  derived; SQLite/FTS rebuildable; uncommitted
                               by default
compatibility projections      generated during bridge phase only (SC-3)
```

No kernel concept requires a representation WMR-H lacks. Obligation units and realization state fit the existing descriptive-metadata / control-record split exactly: the definition lives in the governing carrier, and the state lives in a JW1 control record.

## 13. WARRANT-F integration

```text
AO consequence classes -> WARRANT-F profiles
    accepted-state advancement      G2 (or G2-D detective during transition)
    bridge mode transition          bridge-qualification profile (§16)
    cutover / authority switch      G7
    release / activation            G3-G6 (Product and Project tooling)
KEYSTONE governance claims (examples)
    kernel validity (identity uniqueness, closed relations, ROLE x STATUS)
    obligation "no third state" (§11.3)
    orientation freshness and size budget (§14.2)
    projection equality: every generated projection equals regeneration
    control-record revision monotonicity (WMR-H)
    AO shape-screen and KA-R51 detector qualification (§9.2, §10)
current oracles
    remain migration oracles; kill-set + known-good + translated cases on
    the current layout BEFORE G7 (WF-A19..A21)
```

## 14. Migration and current-oracle retirement

### 14.1 Successors for current live surfaces

```text
current_routing.json  -> FocusState / AuthorityMode control records (JW1)
                         + generated compatibility projection during bridge
                         (P-D4 translated semantics as the successor contract)
CURRENT_STATE.md      -> generated bounded orientation (current focus, active
                         workstreams, open obligations, pending collaboration,
                         recent milestones) + history/milestones carriers
                         (no chronological narrative in any live carrier)
KNOWLEDGE_MAP.md      -> generated navigation (§5.3)
CONTINUITY.md         -> governing bootstrap/recovery procedure (small) +
                         project_anchor.json
REVIEW_INBOX.md       -> generated from collaboration thread control records
                         (removes the E8 drift class by construction)
checkpoints           -> milestone evidence records for meaningful boundaries
                         only; the coordination "clock" is control-state
                         revision + Git history, not a checkpoint counter
```

### 14.2 Bounded-orientation invariant

A live orientation projection has a preregistered size budget and is regenerated, never appended. Exceeding the budget is a WARRANT-F claim failure. This removes E2's accumulation mechanically instead of by editorial discipline.

### 14.3 Sequencing (SC-3)

```text
T0  SC-1/SC-2/SC-3 accepted (owner) ; Spec 028 lineage table accepted
T1  JW1 kernel amendments + reconstruction + activation in SHADOW
    (current layout; legacy declaration reader retained)
T2  obligation-unit adoption for IN_FORCE contracts; realization coverage view
T3  control records + generated projections in SHADOW beside live surfaces;
    oracle kill-set / known-good / translated qualification (current layout)
T4  bridge ACTIVE_SUBORDINATE (after §16 gate)
T5  physical migration (separately authorized) with translated oracles
T6  cutover candidate; G7 qualification (Spec 028 §42 minimum + extensions)
T7  W8-equivalent explicit owner authority switch; rollback drill fresh
```

Physical migration (T5) comes after the semantic successor runs in shadow on the current layout. Physical and semantic migration are never performed in the same step, so every divergence is attributable to one of them.

## 15. Provider and workflow neutrality

No kernel object, AO record or SC-1 clause names a provider mechanism. Branch roles are semantic; accepted-state advancement is a semantic transition (WF-A36). The Runtime Bridge, a Git-host connector and a CI runner are executors described by capabilities (WF-A34). The AO protocol is a JW1 CLI/result contract; an MCP tool surface is one adapter of it. The provider qualification gap (P-H scoped INCONCLUSIVE) blocks only provider-dependent cutover steps, not the semantic design.

## 16. Shadow bridge and ACTIVE_SUBORDINATE qualification

```text
SHADOW entry         implementation exists; bridge writes only shadow receipts
SHADOW evidence      replay AO-9 P1 scenarios + recorded real sessions:
                     obligation-set agreement vs evaluator key, miss rate,
                     false-positive rate, read/tool cost vs frozen budgets
                     (AO10-Q01..Q05), authority-membrane leak tests (AO-7 §21)
ACTIVE_SUBORDINATE   WARRANT-F bridge-qualification profile ADMIT
entry                + explicit owner enable decision (bridge never self-enables)
ACTIVE monitoring    D3 downstream-catch rate and membrane violations as live
                     claims; material failure -> SUSPENDED automatically
                     (detective, fail-safe to current continuity path)
exit to W8           bridge cannot self-promote; authority switch is G7 + owner
```

## 17. Recovery, rollback and authority switch

- **Break-glass** is derivative-free: anchor, then control locator, then governing knowledge. It is exercised as a drill (WARRANT-F M1) on the current layout and again after physical migration.
- **Rollback representation:** before T7, legacy live surfaces are frozen as an exact snapshot, and a reverse projection from control records to legacy surfaces is qualified. Rollback is a JW1 transition with a receipt.
- **Authority switch:** changes only AuthorityMode, through a G7-admitted, owner-decided transition. No generator, CLI or bridge path can write AuthorityMode (a witnessed claim).
- **Recovery versus collaboration continuity** stay distinct (Research 258 AM-8).

## 18. Locally attractive designs that weaken the whole system

```text
L1  A RICH ONTOLOGY for better navigation
    multiplies authoring, witness and ratchet surface; conflicts with
    WMR-H selectivity -> closed relation set + small concern vocabulary

L2  WARRANT-F AS THE OBLIGATION LEDGER
    assurance would absorb governance; non-verifiable obligations would be
    forced into fake claims -> claims realize only verifiable units

L3  AO AS A SERVICE/DAEMON
    availability, security and provider coupling; break-glass would depend
    on it -> protocol + library + CLI

L4  CONTROL STATE IN GENERATED VIEWS for convenience
    derived truth (KA-I03 breach) -> control records written by JW1 only

L5  SUBJECTS THAT RESTATE OWNERSHIP
    two drifting encodings of one fact -> position is derived

L6  PER-MUST TRACKING
    ceremony collapse -> obligation units

L7  PHYSICAL AND SEMANTIC MIGRATION IN ONE STEP
    unattributable divergence -> T3 before T5

L8  A GENERIC "EVENT LOG" TO SATISFY KA-R51/R52
    broad event sourcing is already rejected by WMR-H; selective
    receipts + captures suffice

L9  MODEL-ASSISTED SHAPE SCREENING FOR TOOL CALLS
    lower precision where determinism is free -> typed tool-call classifier

L10 ONE AMENDED SPEC 028
    mixed lifetimes; unreadable authority -> three successor contracts
```

## 19. Risks and falsifiers

```text
F1  ROLE x STATUS cannot classify real historical carriers reliably
    (blind agreement below preregistered threshold)       -> revisit kernel axes
F2  closed relation set leaves recurring facts unrepresentable (P1)
                                                          -> governed extension
F3  position + relations + search meets the 217 bar without concerns
                                                          -> drop concern layer
F4  the 217 vocabulary beats all successor arms on the same scenarios
                                                          -> retain it on merit
F5  obligation units cannot be delimited consistently (blind unit
    agreement low) or exceed an effort budget             -> coarser units
F6  prose-only consequential outputs dominate (P5)        -> invest in
                                                             model-assisted screen
F7  KA-R51 detectors' precision below threshold on ordinary sessions
                                                          -> raise consequence cut
F8  bounded orientation fails cold-continuation parity with the current
    path (P6)                                             -> larger budget or
                                                             role-specific views
F9  three successor contracts create more coordination cost than they
    remove (cross-reference churn)                        -> merge SC-2/SC-3
F10 bridge SHADOW agreement cannot reach the AO-9 bar within cost
                                                          -> planner-only fallback
                                                             (Research 234 option)
F11 READ_ONLY collaborators act on stale orientation often enough to
    cause consequential errors                            -> require EXECUTING
                                                             preflight for all
                                                             consequential proposals
```

## 20. Recommended empirical probes (decision-relevant)

Every gate carries its own negative control (the MC-0027 lesson).

```text
P1  KERNEL SUFFICIENCY
    express 25-30 real items (Spec 028 clauses, AO decisions, WARRANT-F rules,
    a workstream, a procedure, an EvolutionCase) in the kernel; count
    unrepresentable facts; blind ROLE x STATUS classification of 40 historical
    carriers vs authority_class                            (F1, F2)

P2  NAVIGATION ARMS
    A position+relations+search / B A+concern vocabulary / C 217 vocabulary;
    217's 9 scenarios + new cold-start and Project-plane scenarios;
    blind calibration per MC-0019/0020 method             (F3, F4)

P3  OBLIGATION UNITS ON REAL CONTRACTS
    delimit units in Spec 028, AO-9 P7 and WARRANT-F; blind second delimiter;
    coverage run must surface the three E3 historical gaps (sensitivity) and
    no false gaps on a realized contract (specificity)    (F5)

P4  KA-R51 DETECTORS
    AO-9 scenarios + failure-corpus reminder cases (sensitivity); ordinary
    session sample (specificity)                          (F7)

P5  SHAPE-SCREEN DETERMINISM
    share of consequential actions in recorded real sessions that are typed
    tool calls vs prose-only                              (F6)

P6  BOUNDED ORIENTATION COLD START
    fresh-collaborator continuation: generated bounded orientation + control
    records vs current CURRENT_STATE path, preregistered tasks (Q1/Q2 style)
                                                          (F8)

P7  SPEC 028 LINEAGE COMPLETENESS
    desk probe: every section and every MUST-bearing paragraph reaches a
    disposition and successor; independent second pass    (F9 input)

P8  BRIDGE SHADOW REPLAY
    AO-9 P1 scenarios through a shadow implementation     (F10)
```

Realization-stage, not decision-relevant: CLI determinism, projection equality, revision-monotonicity enforcement, rollback reverse projection, and host/provider qualification (P-H successor).

## 21. Upstream findings

```text
U1  NO REOPEN. R5-R8C accepted architecture holds.
U2  AO-4 CLARIFY candidate: authority_class -> ROLE x STATUS is a kernel
    amendment to a Candidate 01 contract; it tightens KA-I04 realization
    rather than contradicting it.
U3  AO-4 CLARIFY candidate: Research 217 vocabulary superseded, rules retained
    (owner already removed its preservation right; this records the
    disposition and the qualification bar).
U4  No new Level-1/Level-2 structure; all realization fits R8-A JW1 +
    Engineering boundaries.
```

## 22. Open decisions

```text
OD1  successor contract identities/numbering and family placement (R7)
OD2  initial concern vocabulary (after P2)
OD3  obligation-unit metadata schema (after P3)
OD4  KA-R51 consequence thresholds; triage cadence
OD5  orientation size budget and role-specific views (after P6)
OD6  exact control-record sharding (FocusState, BridgeState, threads)
OD7  typed tool-call taxonomy for the shape screen (after P5)
OD8  whether checkpoints survive as a family or only as milestone records
OD9  rollback reverse-projection scope (which legacy surfaces must be
     reconstructible)
```

## 23. Comparison-ready summary

```text
ARCHITECTURE            KEYSTONE — one semantic kernel, many governed projections
SPEC 028                prospectively SUPERSEDED as a whole by SC-1 semantic /
                        SC-2 realization / SC-3 transition; clause lineage for
                        all 46 sections; temporal authority until effective
KERNEL                  selective identity; ROLE x STATUS (replaces
                        authority_class); closed 5-family relation set;
                        obligation units
SEMANTIC ORGANIZATION   position (derived) + relations + small cross-cutting
                        concern vocabulary + derived search
RESEARCH 217            rules and calibration method RETAINED; 18-subject
                        vocabulary SUPERSEDED; must be beaten on its own bar
AO-10                   deterministic JW1 control protocol (begin / preflight /
                        postflight), executor-hosted, no daemon; collaborator
                        classes by capability
AO9-P7-D01              shape screen deterministic for typed tool calls,
                        model-assisted only for prose
KA-R51                  four mechanical detectors -> machine captures;
                        warranted with AO-9 witnesses
KA-R52                  obligation units + REALIZES/DEFERS + RealizationState;
                        "no third state" is a G2 warranted claim
WMR-H                   no new representation needed
WARRANT-F               AO requests profiles; kernel governance claims;
                        oracles qualified on current layout before G7
LIVE SURFACES           routing -> control records; CURRENT_STATE -> bounded
                        orientation + milestones; inbox generated
MIGRATION ORDER         semantic successor in shadow BEFORE physical migration
BRIDGE                  SHADOW replay -> profile ADMIT + owner enable ->
                        ACTIVE_SUBORDINATE; auto-SUSPEND on material failure
AUTHORITY SWITCH        only AuthorityMode, only via G7 + owner decision
UPSTREAM                no reopen; two AO-4 CLARIFY candidates
```

```text
MC0029_MESSAGE001=COMPLETE
INDEPENDENT_BASE=0a68787aee5f2c6332d6ee1fb6adbf0efe92a41d
RESEARCH312_READ=false
SPECIFICATION028_DISPOSITION_RECOMMENDED=PROSPECTIVE_SUPERSESSION_BY_THREE_SUCCESSORS
RESEARCH217_VOCABULARY_DISPOSITION=SUPERSEDE_RULES_RETAINED
UPSTREAM_ARCHITECTURE_REOPEN=NO
EMPIRICAL_PROBES_RECOMMENDED=P1_TO_P8
PRODUCTION_IMPLEMENTATION_AUTHORIZED=false
PHYSICAL_MIGRATION_AUTHORIZED=false
AUTHORITY_SWITCH_ALLOWED=false
NEXT=CHATGPT_COMPARATIVE_RECONCILIATION
```
