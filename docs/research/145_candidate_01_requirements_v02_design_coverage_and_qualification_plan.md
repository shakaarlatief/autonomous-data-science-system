# Research 145: Candidate 01 Requirements V0.2 Design Coverage and Qualification Plan

**Date:** 2026-09-14
**Status:** 50/50 KA-R + 17/17 KA-I DESIGN-MAPPED / Q4 REAL-SOURCE STRESS SUPPORT PASSED / EVIDENCE RECONCILIATION V0.3 NEXT / TARGET ARCHITECTURE NOT SELECTED
**Candidate:** `PKA-CANDIDATE-01` from Research 144
**Scope:** Systematically map the whole-architecture candidate against every frozen Requirements V0.2 requirement/invariant, distinguish design coverage from actual qualification evidence, identify selection-blocking proof clusters, and freeze the minimum implementation/behavioral evidence needed before target selection.
**Authority:** Candidate qualification planning only. Requirements V0.2 remain the acceptance authority. A mapped design mechanism is not a qualified pass.
**Declared references:** `research:124`, `research:130`, `research:143`, `research:144`, `path:docs/research/PROJECT_KNOWLEDGE_ARCHITECTURE_REQUIREMENTS_V02.md`, `path:docs/research/project_knowledge_candidate_01/QUALIFICATION_MATRIX_V01.json`, `checkpoint:488`

## 1. Qualification semantics

This review deliberately separates two gates:

```text
DESIGN COVERAGE GATE
    Does the candidate specify a credible mechanism for every frozen requirement/invariant?

EVIDENCE / QUALIFICATION GATE
    Has the integrated candidate actually demonstrated that mechanism structurally and behaviorally
    under the required failure, scale, migration and degraded-mode conditions?
```

Candidate 01 currently clears only the first gate.

```text
50 KA-R design-mapped       yes
17 KA-I design-mapped       yes
identified design gaps       0
final qualified passes       0
target selection allowed     no
```

`final qualified passes = 0` is intentionally conservative. Earlier probes de-risk individual mechanisms, but the new whole candidate has not yet been implemented and qualified as one integrated successor.

## 2. Design-coverage status vocabulary

```text
DESIGN_COVERED
    candidate contains an explicit mechanism addressing the requirement

QUALIFICATION_RULE_MAPPED
    the requirement governs how candidate qualification must be executed rather than one runtime component

PENDING_INTEGRATED_EVIDENCE
    design is mapped but direct candidate implementation/behavior evidence is still required
```

## 3. Full KA-R01..KA-R50 mapping

| ID | Requirement | Coverage | Candidate mechanism | Cluster |
|---|---|---|---|---|
| KA-R01 | persistent project understanding | DESIGN_COVERED | canonical semantic sources preserve rich rationale, status and provenance; derived views are subordinate | Q5 |
| KA-R02 | stable project-controlled bootstrap | DESIGN_COVERED | small authored bootstrap core plus generated committed routing/current views | Q1 |
| KA-R03 | conversation and model independence | DESIGN_COVERED | public repository is authority; capture/promotion prevents chat-only truth | Q5 |
| KA-R04 | task-shaped safe orientation | DESIGN_COVERED | reconstruction planner selects broad continuation or task-shaped safe narrow path | Q1 |
| KA-R05 | progressive disclosure | DESIGN_COVERED | progressive bootstrap -> view -> semantic source -> evidence drill-down | Q1 |
| KA-R06 | active route reconstruction | DESIGN_COVERED | single-source workstream declarations plus generated active route graph | Q4 |
| KA-R07 | relevant discovery with safety-calibrated recall | DESIGN_COVERED | exact/structured/lexical/optional semantic retrieval plus generated risk/governance indexes | Q1 |
| KA-R08 | reconstruction and authority-resolution receipts | DESIGN_COVERED | authority/reconstruction receipts bind sources, revisions, freshness and activated constraints | Q2 |
| KA-R09 | consequential-action authority activation and contract fidelity | DESIGN_COVERED_AFTER_MC0016_AMENDMENT | sole-normative structured contract facts + stable constraint IDs + deterministic execution-plan conformance + independent verification where deterministic equivalence is insufficient | Q2 |
| KA-R10 | known-risk and evolution-trigger activation | DESIGN_COVERED | source-owned risk/reopen triggers exposed through generated indexes and task activation | Q2 |
| KA-R11 | uncertainty visibility | DESIGN_COVERED | explicit unresolved/conflict/unavailable/stale states and consequence-sensitive failure | Q2 |
| KA-R12 | explicit epistemic role | DESIGN_COVERED | typed source profiles preserve material epistemic/lifecycle distinctions selectively | Q3 |
| KA-R13 | action-shaped authority resolution | DESIGN_COVERED | resolver uses action, scope, state, actor if material, time and authority closure | Q2 |
| KA-R14 | supersession, supplementation and conflict visibility | DESIGN_COVERED_AFTER_MC0016_AMENDMENT | REPLACE/SUPPLEMENT/SPECIALIZE/CORRECT + fail-visible conflicts; joint-authority exception uses explicit J1-J6 promotion gate | Q2 |
| KA-R15 | relationship semantics | DESIGN_COVERED | directional source-owned relations by default; rich relation source only when relation lifecycle warrants it | Q3 |
| KA-R16 | current state, history and selective temporal semantics | DESIGN_COVERED | Git history plus selective applicability/authority temporal qualifiers and generated current views | Q3 |
| KA-R17 | view-contract consolidation fidelity | DESIGN_COVERED_AFTER_MC0016_AMENDMENT | must-preserve manifest + unit-level coverage disposition + source drill-down + consequence-shaped independent verification | Q5 |
| KA-R18 | synthesis provenance and auditability | DESIGN_COVERED | promoted synthesis and consequential transformations retain source/transformation provenance | Q5 |
| KA-R19 | one explicit project-development authority | DESIGN_COVERED | public ADS repository remains one explicit project-development authority | Q9 |
| KA-R20 | explicit authority class for stores and views | DESIGN_COVERED | source/view profiles declare canonical, candidate, historical, derived or evidence authority role | Q6 |
| KA-R21 | rebuildability appropriate to representation | DESIGN_COVERED | derived-view manifests declare inputs, generator, rebuildability and deletion/rebuild behavior | Q6 |
| KA-R22 | explicit promotion of unique accepted synthesis | DESIGN_COVERED | unique accepted synthesis crosses explicit source-traceable promotion into canonical source | Q5 |
| KA-R23 | freshness, source and authority-closure binding | DESIGN_COVERED | persistent derived views bind source revision/digest, generator and freshness state | Q6 |
| KA-R24 | probabilistic retrieval is not sole governing authority | DESIGN_COVERED | probabilistic retrieval nominates candidates but cannot silently resolve governing authority | Q2 |
| KA-R25 | explicit workstream identity and state | DESIGN_COVERED | durable workstream profile with explicit single-source state | Q4 |
| KA-R26 | explicit pause and return semantics | DESIGN_COVERED | paused work requires pause reason, return condition and resume target | Q4 |
| KA-R27 | multiple dependencies | DESIGN_COVERED | workstream profile supports multiple depends_on edges and generated DAG validation | Q4 |
| KA-R28 | interruption recovery | DESIGN_COVERED | resume reconstruction uses durable workstream state plus completed project evidence, not prior-chat plan | Q4 |
| KA-R29 | concurrent collaborator safety | DESIGN_COVERED | expected Git/source revision preconditions make stale/conflicting authoritative updates fail | Q4 |
| KA-R30 | bounded qualification budgets | QUALIFICATION_RULE_MAPPED | task-class-specific read/context budgets measured during candidate qualification | Q10 |
| KA-R31 | non-linear-history reconstruction cost | DESIGN_COVERED_AFTER_MC0016_AMENDMENT | normal reconstruction consumes bounded current views and does not rescan whole history; periodic rebuild cost is measured separately | Q8 |
| KA-R32 | bounded mandatory active core | DESIGN_COVERED | payload-light bootstrap and generated active surfaces remain separate from historical archive | Q8 |
| KA-R33 | dependency-local marginal maintenance | DESIGN_COVERED_AFTER_MC0016_AMENDMENT | ordinary local changes use dependency-aware incremental refresh; periodic automated full rebuild remains allowed | Q8 |
| KA-R34 | saturation and active-surface observability | DESIGN_COVERED | active-view size, routing payload, fan-out, staleness and consolidation pressure are observable | Q8 |
| KA-R35 | human and model inspectability | DESIGN_COVERED | rich repository sources plus inspectable structured declarations/manifests | Q1 |
| KA-R36 | provider and tool portability | DESIGN_COVERED | project-controlled repository semantics and deterministic views remain reconstructable across capable providers/tools | Q1 |
| KA-R37 | explicit public/private authority boundary | DESIGN_COVERED | public authority constitution plus explicitly delegated private dependency semantics | Q7 |
| KA-R38 | private-data non-leakage | DESIGN_COVERED | public-view generation includes private-field/path non-leakage validation | Q7 |
| KA-R39 | bounded private dependency | DESIGN_COVERED | public reconstruction works independently; private-required tasks expose dependency/verification status | Q7 |
| KA-R40 | structural and behavioral qualification | QUALIFICATION_RULE_MAPPED | layered structural and behavioral qualification suite is part of candidate contract | Q10 |
| KA-R41 | multidimensional reconstruction qualification | QUALIFICATION_RULE_MAPPED | qualification remains multidimensional and case-level with no aggregate winner score | Q10 |
| KA-R42 | consequence-sensitive degraded mode | DESIGN_COVERED | consequence-sensitive degraded mode separates optional retrieval gaps from required authority failure | Q7 |
| KA-R43 | migration preservation and identity reconciliation | DESIGN_COVERED_AFTER_MC0016_AMENDMENT | M0-M7 migration preserves identity, authority, provenance, history and reverse references with explicit semantic parity checks | Q9 |
| KA-R44 | old authority remains until successor qualification | DESIGN_COVERED_AFTER_MC0016_AMENDMENT | candidate stays shadow/non-authoritative until qualification; rollback exporter and stabilization window enable explicit lossless reverse switch | Q9 |
| KA-R45 | self-hosting evolution | DESIGN_COVERED | same capture, workstream, migration and authority-transition mechanisms can coordinate architecture evolution | Q9 |
| KA-R46 | representation-independent continuity of identity | DESIGN_COVERED_AFTER_MC0016_AMENDMENT | semantic IDs + transition/tombstone history + generated flattened current-target lookup survive carrier changes without normal history scans | Q3 |
| KA-R47 | multi-axis organization without truth duplication | DESIGN_COVERED | source-local declarations generate orthogonal subject/authority/workstream/provenance/temporal views without copied truth | Q6 |
| KA-R48 | capture, consolidation and promotion boundary | DESIGN_COVERED | capture -> consolidated candidate -> explicit promotion -> derived consumption roles remain distinct | Q5 |
| KA-R49 | selective temporal and supersession semantics | DESIGN_COVERED | selective effective/authority time plus explicit transition modes only where semantics require them | Q3 |
| KA-R50 | recurring active-surface consolidation lifecycle | DESIGN_COVERED_AFTER_MC0016_AMENDMENT | active-surface and capture-backlog pressure trigger governed consolidation while preserving drill-down/history | Q5 |

## 4. Full KA-I01..KA-I17 mapping

| ID | Invariant | Coverage | Candidate mechanism | Cluster |
|---|---|---|---|---|
| KA-I01 | durable repository authority outranks transient model/chat memory | DESIGN_COVERED | public repository authority boundary and explicit promotion | Q1 |
| KA-I02 | one explicit project-development authority; derived stores cannot silently compete | DESIGN_COVERED | canonical source roles plus derived-view manifests | Q1 |
| KA-I03 | derived state contains no unique accepted truth unless explicitly promoted | DESIGN_COVERED | derived deletion/rebuild contract plus promotion boundary | Q5 |
| KA-I04 | material current/historical/superseded/rejected/unresolved distinctions survive | DESIGN_COVERED | source lifecycle profiles plus selective temporal semantics | Q1 |
| KA-I05 | consequential guidance resolves/consumes authority and preserves material action contract | DESIGN_COVERED_AFTER_MC0016_AMENDMENT | resolver receipts + sole-normative constraint IDs + deterministic plan conformance + independent high-consequence semantic verification where needed | Q2 |
| KA-I06 | missing required evidence or unresolved governing conflict is surfaced | DESIGN_COVERED | explicit unresolved/unavailable/conflict result states | Q2 |
| KA-I07 | provenance and must-preserve view semantics survive synthesis/compression/migration | DESIGN_COVERED | view-contract fidelity, source drill-down and migration reconciliation | Q5 |
| KA-I08 | old continuity remains operational until explicit qualified switch | DESIGN_COVERED | M0-M7 shadow migration and explicit authority transition | Q9 |
| KA-I09 | resumable paused work preserves reason, return condition, parent relationship and target | DESIGN_COVERED | workstream profile conditional fields | Q4 |
| KA-I10 | public/private authority separation and non-leakage are preserved | DESIGN_COVERED | delegated private dependency model plus publication validator | Q7 |
| KA-I11 | fresh continuation does not depend on previous conversation | DESIGN_COVERED | stable bootstrap plus committed canonical sources/views | Q1 |
| KA-I12 | required reconstruction cost is not structurally proportional to accumulated history | DESIGN_COVERED_AFTER_MC0016_AMENDMENT | normal reconstruction consumes bounded current views; periodic full rebuild may remain corpus-proportional | Q8 |
| KA-I13 | routine local change avoids unbounded manual/global maintenance | DESIGN_COVERED | source-local declarations plus dependency-aware regeneration | Q8 |
| KA-I14 | optional probabilistic retrieval failure cannot bypass authority safety | DESIGN_COVERED | retrieval subordinate to explicit authority resolver | Q7 |
| KA-I15 | durable state exposes live route/authority/reconstruction/qualification/freshness health | DESIGN_COVERED | generated routing/current views plus manifests and validation receipts | Q1 |
| KA-I16 | capture does not imply authority | DESIGN_COVERED | capture/candidate/promotion roles and explicit authority transition | Q5 |
| KA-I17 | intended semantic continuity is not forced to equal carrier continuity | DESIGN_COVERED_AFTER_MC0016_AMENDMENT | semantic IDs + merge/split/move/representation transitions + generated bounded current-target lookup | Q9 |

## 5. Design-coverage result

The systematic mapping finds **no requirement or invariant that Candidate 01 simply ignores at the design level**. That is a meaningful readiness result: the candidate is now whole enough to prototype without first inventing another architecture family to plug an obvious frozen-requirement hole.

It is not evidence that the candidate should be selected. Several mechanisms are selection-blocking precisely because the difficult part is behavioral proof rather than prose coverage.

## 6. Selection-blocking qualification clusters

### Q1: bootstrap / reconstruction / discovery

Must prove cold continuation, task-shaped narrow orientation, high-recall governing/risk discovery, provider/tool portability and human/model inspectability under bounded read/context budgets.

### Q2: authority resolution / action-contract fidelity

Must prove deterministic governing-source closure, supplement/replacement semantics, explicit ambiguity/unavailability, source-consumption receipts and BL-001-style post-activation action-contract fidelity.

### Q3: identity / relationship / temporal semantics

Must prove selective durable identity, rename/move/merge/split/tombstone behavior, rich relation semantics, selective time dimensions and the bounded joint-authority exception without a creeping registry.

### Q4: workstream continuation / concurrency

Must prove parent/dependency DAG reconstruction, pause/return/resume semantics, interruption recovery and stale concurrent-write rejection on realistic nested workstreams.

### Q5: capture / promotion / consolidation fidelity

Must prove low-friction capture, candidate consolidation, explicit promotion, rejected/historical rationale retention, provenance and multidimensional consolidation fidelity without global review cost.

### Q6: derived views / freshness / multi-axis projection

Must prove deletion/rebuild of all derived structural views, freshness/source binding, multi-axis projections, generated compatibility views and absence of unique truth in indexes/summaries.

### Q7: public-private boundary / degraded mode

Must prove public/private delegation, public non-leakage, ordinary public reconstruction without private detail, fail-visible private dependency and consequence-sensitive degraded mode.

### Q8: scaling / maintenance economics

Must prove 5x/10x passive-history boundedness, dependency-local maintenance, active-surface budgets, generated-view refresh economics and recurring consolidation triggers.

### Q9: migration / authority switch / self-hosting evolution

Must prove staged migration, semantic identity/provenance preservation, reverse-reference safety, rollback, self-hosted redesign continuity and explicit single-authority switch.

### Q10: qualification methodology / budgets

Must execute the multidimensional structural/behavioral qualification itself with task-specific budgets and no single aggregate winner score.

## 7. Existing evidence that partially de-risks the candidate

The evidence gate is not blank. Earlier work lowers uncertainty around several mechanisms, but none substitutes for integrated Candidate 01 qualification:

```text
V0.1 common fixture
    source-local directional ownership + derived closure can satisfy hard cases without duplicate truth

V0.2 lifecycle fixture
    selective relation lifecycle/temporal/concurrency mechanics are implementable, with family-boundary corrections preserved

real ADS corpus + MC-0015
    single-source authority dominates sampled cases; derived-only views are real; durable identity can coexist with one source

BL-001
    directly motivates the action-contract fidelity gate

BL-002/003/004
    calibrate process discoverability, broad orientation cost and exact-source descent

D1-D8 + ICM
    independently support selective identity, source/derived separation, task-shaped context, explicit provenance, local fan-out and cold-walk testing
```

These are **mechanism priors**, not Candidate 01 pass certificates.

## 8. Minimum integrated qualification program

The next implementation phase should build the smallest shadow prototype capable of exercising all ten clusters rather than fully migrating the repository first.

### Phase P0: semantic declaration substrate

Implement one repository-native declaration syntax and schemas for: workstream, governing procedure/action contract, ordinary knowledge source, identity transition, exceptional joint-authority declaration, capture candidate and derived-view manifest. Only active/high-value fixtures need conversion.

### Phase P1: deterministic structural generators

Generate identity index, workstream graph/current route, authority candidate/closure index and a small subject/navigation view from those declarations. Generated outputs must carry source/generator/freshness binding.

### Phase P2: authority and action-contract path

Implement narrow governed-task resolution, replacement/supplement semantics, receipts and contract checks. Replay BL-001-style cases plus missing/conflicting authority.

### Phase P3: continuation and failure behavior

Run generic cold continuation, nested pause/resume, stale concurrent update, optional retrieval outage, derived-view deletion/rebuild and provider/model-switch tests.

### Phase P4: capture/consolidation and scale

Exercise real conversation-born capture through promotion, one high-consequence consolidation with fidelity checks, and 1x/5x/10x passive-history plus local-change fan-out measurements.

### Phase P5: public/private and migration shadow

Use synthetic private-only markers to qualify non-leakage/degraded behavior. Produce shadow generated `current_routing`, `CURRENT_STATE` and `KNOWLEDGE_MAP` equivalents and compare them to current authority without switching authority.

### Phase P6: full requirement evidence matrix

For every KA-R/KA-I, replace `PENDING_INTEGRATED_EVIDENCE` only with an explicit test/proof reference. Any unresolved item blocks target selection unless the requirement itself is conditional and the condition is demonstrably absent.

## 9. Candidate-specific falsification priorities

The first prototype should prioritize attempts to disprove the candidate rather than polishing generated views. Highest-value failure probes are:

```text
1. BL-001-style source-read-but-contract-violated output
2. identity split/merge with historical references and no global manual repair
3. genuinely joint governing source set with missing precedence -> fail visible
4. nested workstream interruption/resume after unrelated work completes
5. delete every derived view and reconstruct safely
6. 10x passive history with unchanged active semantic state
7. one ordinary local source edit and measured manual/generated fan-out
8. capture -> consolidate -> promote -> delete temporary capture without accepted insight loss
9. synthetic private-required governed task with private unavailable
10. migration shadow parity and rollback from generated compatibility views
```

## 10. H3 / alternative-family reopening rule

Candidate 01 should not monopolize the design space merely because it maps all requirements. Reopen Object-Primary/H3 or another family if prototype evidence shows:

```text
selective source profiles accumulate object/relationship machinery comparable to a general object substrate
AND
an object-primary representation materially simplifies identity, workstream, joint-authority or migration cases
WITHOUT
unacceptable capture/migration/inspectability cost
```

Likewise, if Candidate 01 requires a proliferating set of joint-authority/identity-transition special objects that behaves like a central registry in practice, the original H2 risk has reappeared under another name.

## 11. Design-gate disposition

Candidate 01 clears the **whole-architecture design-coverage gate**: every frozen requirement/invariant has an explicit intended mechanism, and no uncovered requirement currently forces a different family.

It does **not** clear the evidence/selection gate.

```text
CANDIDATE=PKA-CANDIDATE-01
KA_R_DESIGN_MAPPED=50_OF_50
KA_I_DESIGN_MAPPED=17_OF_17
IDENTIFIED_DESIGN_COVERAGE_GAPS=0
FINAL_QUALIFIED_PASSES=0
SELECTION_BLOCKING_QUALIFICATION_CLUSTERS=10
DESIGN_COVERAGE_GATE=PASS
EVIDENCE_GATE=PENDING
TARGET_ARCHITECTURE=NOT_SELECTED
NEXT=SHADOW_PROTOTYPE_AND_ADVERSARIAL_CANDIDATE_REVIEW
```

## 12. MC-0016 Message 001 correction to the design-coverage claim

Claude's exact-target adversarial review did not accept the original blanket `50/50 + 17/17` statement without qualification. At commit `69aed186a0d63b3c395a133cd920099d5fa8e000`, Claude judged seven KA-R and one KA-I entries partially covered and identified additional non-matrix design risks. Research 146 preserves that result and distinguishes actual mechanism under-specification from requirement-scope conflation.

The task-owner disposition accepts substantive amendments for action-contract precedence/assurance, consolidation fidelity, incremental routine refresh, identity lookup, capture backlog, paused-workstream salience, rollback and complexity observability. It also adds a concrete J1-J6 joint-authority admission gate.

Three scope corrections matter:

```text
KA-R31 / KA-I12
    govern required reconstruction cost, not periodic full-rebuild scan complexity;
    periodic global rebuild remains explicitly permitted by KA-R33.

KA-R46
    governs semantic continuity across carriers; bounded lookup is an important index/scale
    refinement but was not the missing semantic identity mechanism itself.

KA-R43 versus KA-R44
    forward semantic preservation is KA-R43; the missing rollback mechanism belongs most
    directly to KA-R44's authority-switch/recovery criteria.
```

The current working matrix therefore returns every requirement/invariant to design-covered **after amendment**, not because Claude's review was rejected, but because the concrete missing mechanisms have now been added. Final qualification remains zero across the board.

One narrow MC-0016 follow-up remains before implementation, limited to:

```text
1. sole-normative action-contract precedence rule
2. J1-J6 joint-authority admission/governance rule
```

If those survive review without another architecture-level defect, Candidate 01 is ready for the smallest falsification-first shadow prototype.

```text
DESIGN_COVERAGE_AFTER_MC0016_AMENDMENT=50_KA_R__17_KA_I
FINAL_QUALIFIED_PASSES=0
MC0016_NARROW_FOLLOWUP=PENDING
TARGET_ARCHITECTURE=NOT_SELECTED
```

## 13. MC-0016 final narrow closure

Claude Message 003 closes the normative-precedence question and identifies one final precision defect in the reviewed J2/J3 wording. That defect is now corrected in Research 144: ordinary source-owned relations remain preferred whenever a natural semantic direction exists, while a joint-authority semantic source is admissible only when correct governing semantics would otherwise require an arbitrary non-semantic directional tie-break among otherwise symmetric participants and an independently relevant set-level authoritative fact exists.

The adjacent source-integrity risk is also carried into the prototype: edits to governed procedure prose or structured contracts must trigger a semantic-drift review. This check flags possible mismatch but never treats prose as a second normative authority.

The design-coverage matrix therefore remains 50 KA-R / 17 KA-I after amendment, with zero final qualified passes. MC-0016 is complete and the next gate is empirical shadow implementation rather than another architecture-dialogue round.

The first slice is deliberately smaller than the full P0-P6 plan. It must falsify the foundational assumptions first: contract-home/drift detection, natural-direction versus irreducible joint authority, BL-001 prevention, dependency-local refresh/full rebuild separation and bounded current identity lookup. Broader workstream, capture, private-boundary and migration machinery should wait until those foundations survive.

```text
MC0016=RESOLVED
DESIGN_COVERAGE=50_KA_R__17_KA_I_AFTER_AMENDMENT
FINAL_QUALIFIED_PASSES=0
PROTOTYPE_READY_AT_DESIGN_LEVEL=YES
TARGET_ARCHITECTURE=NOT_SELECTED
NEXT=FALSIFICATION_FIRST_SHADOW_PROTOTYPE
```

## 14. Shadow V0.1 evidence enters the qualification program

Research 149 adds narrow synthetic evidence for mechanisms associated with KA-R09, R14, R15, R21, R31, R33, R46 and KA-I05, I12, I17. The machine matrix records this as `NARROW_SYNTHETIC_SUPPORT` with `final_qualification_credit=false`.

The first-run result passed the separately frozen oracle without implementation repair, but the evidence remains deliberately weaker than a final requirement pass because the fixture is synthetic and omits major ordinary-operation surfaces. The next slice should therefore prioritize workstream recovery, capture/promotion/consolidation, generated current-state/routing parity, public/private degraded mode and consequence-sensitive unavailable/conflicting authority.

```text
FOUNDATIONAL_SHADOW_EVIDENCE=RECORDED
FINAL_QUALIFIED_PASSES=0
NEXT=BROADER_SHADOW_OPERATIONAL_BEHAVIOR_SLICE
```

## 15. Operational Shadow V0.2 expands synthetic evidence

Research 151 adds broader integration support for workstream continuity, explicit promotion, must-preserve fidelity, derived current views, public/private degraded mode, uncertainty and stale-update safety. The machine matrix records this as `BROADER_SYNTHETIC_INTEGRATION_SUPPORT` with no final qualification credit.

The preserved first run also demonstrates why defect-first prototype evidence matters: 35/38 oracle checks passed immediately, while a real directional-authority ordering defect and two view-order fidelity defects were visible before repair. The frozen oracle remained unchanged.

Future evidence should now reduce synthetic-protocol bias rather than adding more synthetic breadth.

```text
SYNTHETIC_OPERATIONAL_INTEGRATION=SUPPORTED
FINAL_QUALIFIED_PASSES=0
NEXT=REAL_REPOSITORY_SHADOW_PARITY_AND_BEHAVIOR
```

## 16. Real-repository Shadow V0.1 adds migration-seed evidence

Research 153 adds the first bounded real-repository support to the qualification program. It demonstrates exact routing compatibility parity, real governing-procedure contract checking and real-source navigation/reconstruction while withholding current global views from generation.

The evidence is intentionally not credited as final routing qualification because parity still uses measured migration seeds. One live workstream semantic unit lacks a successor-native canonical source, three project-control facts were explicitly migrated from today's global live-state authority, and the active branch came from the frozen experiment context.

This converts an abstract migration concern into a concrete next gate: successor-native shadow ownership of the active workstream anchor and Project Integration Boundary must reproduce routing with zero global live-state seeds.

```text
REAL_REPOSITORY_SHADOW_SUPPORT=RECORDED
ZERO_SEED_ROUTING_PARITY=PENDING
FINAL_QUALIFIED_PASSES=0
TARGET_ARCHITECTURE=NOT_SELECTED
```

## 17. Zero-seed routing subsystem evidence

Research 155 records the first Candidate 01 real-repository subsystem result with zero global live-state facts in the generation path. Exact routing compatibility parity is achieved from natural successor owners after two explicit migration touches.

The evidence strengthens routing/rebuild/maintenance requirements but remains subsystem support rather than final requirement qualification because the successor sources are still shadow-only and the full continuity system has not migrated or rolled back.

```text
ZERO_SEED_ROUTING_SUBSYSTEM_SUPPORT=PASS
FINAL_QUALIFIED_PASSES=0
NEXT=CURRENT_STATE_DECOMPOSITION_AND_SOURCE_OWNERSHIP_AUDIT
```

## 18. Real CURRENT_STATE decomposition evidence

Research 156 adds direct real-authority evidence for active-surface boundedness, derived-view separation, task-shaped reconstruction and migration preservation. The result is not a final requirement pass: the 98.28% D-category share is a block-level future-role classification, not deletion authorization, and the Source Vault A-category facts still need a successor canonical owner.

The four reproduced drift defects strengthen the case that global copied current/history/navigation surfaces create maintenance risk. The next evidence gate is therefore source migration plus generated-core parity, not further abstract decomposition.

```text
CURRENT_STATE_DECOMPOSITION_SUPPORT=RECORDED
SOURCE_VAULT_A_CATEGORY_GAP=OPEN
FINAL_QUALIFIED_PASSES=0
```

## 19. Current-state-core real shadow evidence

Research 158 records real-repository compact-current-state support with 23/23 must-preserve semantics recoverable and no global-target input during generation. It strengthens workstream, derived-view, bounded-current-surface, maintenance and capture/preservation mechanisms while retaining zero final qualification credit.

The next qualification action is cluster-level evidence reconciliation across Q1-Q10. Further experiments should be selected by unresolved architectural risk rather than by the order of existing repository files.

```text
CURRENT_STATE_CORE_SUPPORT=RECORDED
FINAL_QUALIFIED_PASSES=0
NEXT=WHOLE_ARCHITECTURE_EVIDENCE_RECONCILIATION
```

## 20. Whole-architecture evidence reconciliation

Research 159 converts the accumulated prototype record into a cluster-level evidence audit. Of 67 frozen KA-R/KA-I items, 50 now have synthetic-or-better Candidate 01 evidence and 32 have some real-repository evidence. These counts are descriptive only; final qualified passes remain zero.

The audit identifies Q6 and Q8 as the strongest real subsystem clusters, while Q3, Q7, Q9 and Q10 remain the clearest P0 uncertainties. Q3 is chosen next because it is both weakly evidenced and most architecture-family-discriminating.

```text
WHOLE_ARCH_EVIDENCE_AUDIT=COMPLETE
FINAL_QUALIFIED_PASSES=0
NEXT=Q3_REAL_IDENTITY_RELATIONSHIP_TEMPORAL_FALSIFICATION
```

## 21. Q3 real falsification fixture freeze

Research 160 freezes the first real Candidate 01 Q3 implementation challenge. The fixture intentionally does not convert a legacy global surface. It targets the weakest architecture cluster and carries an explicit H3 reopening rule.

Real cases cover D-015/D-033 scoped supersession, D-011 multi-successor residual applicability, Specification 027 historical-intermediate identity repair, Cockpit durable paused identity and MC-0013 epistemic-role transition.

```text
Q3_REAL_IMPLEMENTATION_EVIDENCE=PENDING
H3_REOPEN_RULE=PROSPECTIVELY_FROZEN
NEXT=IMPLEMENT_Q3_REAL_V01
```

## 22. Q3 real subsystem evidence

Research 161 adds real Candidate 01 support for KA-R12, R15, R16, R46 and R49 plus material support for KA-I04/I17. Five real ADS cases pass the frozen oracle after one preserved implementation repair. No H3/Object-Primary reopening trigger fires.

The result remains subsystem evidence with `final_qualification_credit=false`; merge/split/tombstone still lack equivalent real implementation evidence. Research 159's next P0 gap is Q7, where all six items remain synthetic-only.

```text
Q3_REAL_EVIDENCE=RECORDED
H3_REOPEN=NO
FINAL_QUALIFIED_PASSES=0
NEXT=Q7_REAL_PUBLIC_PRIVATE_BOUNDARY_QUALIFICATION
```

## 23. Q7 real public/private fixture freeze

Research 162 freezes a real cross-repository Q7 challenge after Q3 passes its real subsystem probe. The test covers R37/R38/R39/R42 and I10/I14 through inaccessible-private, stale-accessible-private, private-required and redacted-projection scenarios.

No private-only value is copied into the public fixture. The real private companion participates only as runtime evidence under its delegated role.

```text
Q7_REAL_IMPLEMENTATION_EVIDENCE=PENDING
PRIVATE_NONLEAKAGE_GATE=FROZEN
NEXT=IMPLEMENT_Q7_REAL_V01
```

## 24. Q7 real subsystem evidence

Research 163 adds real cross-repository Candidate 01 support for KA-R37, R38, R39, R42 and KA-I10/I14. The first run passes unchanged, exact private values remain inside the private authority boundary, the public-safe result leaks zero private values/paths, and a real stale private anchor fails visibly without contaminating public integrity.

Current descriptive evidence coverage rises to 45/67 items with some real Candidate 01 evidence and 54/67 with synthetic-or-better evidence. Final qualified passes remain zero. Q9 is now the next P0 experiment because migration/rollback and the authority switch remain design-dominant.

```text
Q7_REAL_EVIDENCE=RECORDED
FINAL_QUALIFIED_PASSES=0
NEXT=Q9_MIGRATION_AUTHORITY_SWITCH_ROLLBACK_SHADOW
```

## 25. Q9 migration/rollback fixture freeze

Research 164 freezes the direct behavioral challenge for KA-R19/R43/R44/R45 and KA-I08/I17. The test maps ten real migration-critical semantics, preserves three successor semantic identities, measures reverse references to compatibility paths, requires a temporary rollback export that the legacy routing validator accepts, keeps the switch gate closed at 0/67 final passes, and requires Candidate 01 to represent the migration of itself.

```text
Q9_REAL_BASE_SHADOW_IMPLEMENTATION=PENDING
AUTHORITY_SWITCH=FORBIDDEN
NEXT=IMPLEMENT_Q9_MIGRATION_V01
```

## 26. Q9 real-base shadow subsystem evidence

Research 165 adds real-base shadow Candidate 01 support for KA-R19/R43/R44/R45 and KA-I08/I17. Ten migration units preserve exact parity, the rollback exporter produces legacy-compatible surfaces accepted by the current routing validator, live authority remains untouched, and the switch gate remains closed. Candidate 01 also self-hosts the migration workstream.

Descriptive evidence coverage is now 49/67 real and 58/67 synthetic-or-better, still with 0 final qualified passes. Q3, Q7 and Q9 have materially changed since Research 159, so a V0.2 whole-architecture evidence audit is required before choosing the next falsification.

```text
Q9_SHADOW_EVIDENCE=RECORDED
FINAL_QUALIFIED_PASSES=0
NEXT=WHOLE_ARCHITECTURE_EVIDENCE_RECONCILIATION_V02
```

## 27. Whole-architecture evidence V0.2

Research 166 updates descriptive evidence coverage to 49/67 real and 58/67 synthetic-or-better. Q3/Q6/Q7/Q8/Q9 have real evidence on every cluster item; Q1/Q2/Q4/Q5 retain design/synthetic gaps; Q10 remains entirely design-level as the final governing program.

The next qualification unit is an integrated Q1+Q2+Q5 cold-continuation / authority-activation / capture-promotion challenge. No final pass status changes yet.

## 28. Integrated Q1/Q2/Q5 fixture freeze

Research 167 freezes a cross-cluster test for the remaining high-value Q1/Q2/Q5 gaps. The run will directly exercise KA-R01/R03/R07/R08/R09/R10/R11/R13/R22/R48 and KA-I01/I05/I06/I11/I16 at integrated shadow level where the frozen task reaches them. Evidence credit will depend on the actual fresh-collaborator result, not the fixture design.

## 29. Integrated Q1/Q2/Q5 fresh-collaborator evidence

Research 168 adds real fresh-collaborator support to KA-R01/R03/R07/R09/R10/R11/R13/R18/R22/R48 and KA-I01/I03/I05/I06/I11/I16. KA-R08 is directly exercised but recorded with a source-revision-basis limitation exposed by the run. The Candidate 01 design now requires explicit revision-basis descriptors for future receipt/index bindings.

Descriptive coverage becomes 58/67 real and 63/67 synthetic-or-better. Q5 now joins Q3/Q6/Q7/Q8/Q9 as a cluster with real subsystem evidence on every item. Q4 is the next real-behavior stress target.

## 30. Q4 real-source workstream stress fixture freeze

Research 169 freezes the direct real-source challenge for KA-R27/R28/R29 after Q5 becomes fully real-supported at subsystem level. Two multi-dependency nodes are grounded in current Candidate 01 qualification work units, interruption recovery is bound to durable S1/S2 receipts, and stale-write rejection uses an exact Git-blob revision descriptor over the real Cockpit workstream source.

Evidence credit remains pending implementation. Current authority mutation is forbidden.

## 31. Q4 real-source subsystem evidence

Research 170 adds real-source support to KA-R27/R28/R29. Together with prior evidence for KA-R06/R25/R26 and KA-I09, every Q4 item now has real Candidate 01 subsystem evidence.

Current descriptive coverage is 61/67 real and 63/67 synthetic-or-better. Six items remain without real evidence: KA-R14, KA-R24, KA-R30, KA-R36, KA-R40 and KA-R41. A whole-architecture V0.3 reconciliation will choose the next falsification before Q10.
