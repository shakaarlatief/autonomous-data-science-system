# Research 129: Consolidation Fidelity, Provenance, and Maintenance Economics Deep Dive

**Date:** 2026-09-13
**Status:** D7-D8 TARGETED EVIDENCE DEEP DIVE COMPLETE / CONSOLIDATION-FIDELITY AND SCALING-ECONOMICS CONSTRAINTS ESTABLISHED / REQUIREMENTS-EVIDENCE RECONCILIATION NEXT / TARGET ARCHITECTURE NOT SELECTED
**Scope:** Deepen Research 125 discriminators D7 (consolidation fidelity and provenance) and D8 (maintenance economics at 5x/10x scale). Examine summarization factuality and content-selection evaluation, systematic-review extraction/reconciliation practice, certainty/heterogeneity reporting, provenance requirements, long-context failure behavior, ontology evolution, materialized-view maintenance, incremental computation and build-system dependency models. Establish architecture-neutral fidelity and scaling constraints for later candidate comparison without selecting a consolidation algorithm, semantic schema, graph/database, retrieval system or target architecture.
**Authority:** Supporting external-evidence research under Research 124. This record completes the planned targeted evidence-deep-dive set and constrains the next requirements/evidentiary-provenance reconciliation. It does not select the successor architecture or replace current project-development knowledge authority.
**Declared references:** `research:124`, `research:125`, `research:126`, `research:127`, `research:128`, `checkpoint:467`, `path:docs/KNOWLEDGE_MAP.md`, `path:docs/DEVELOPMENT_METHOD.md`

## 1. Questions under investigation

D7 asks:

> **How can detailed project history be compressed into durable synthesis without introducing unsupported claims, omitting critical constraints, flattening uncertainty/conflict, altering authority, or losing the source/provenance path needed to audit the synthesis?**

D8 asks:

> **How can richer semantic organization, provenance, derived views, validation and consolidation remain economically maintainable when the repository reaches roughly 5x or 10x its current scale?**

These questions are coupled because a fidelity mechanism that requires exhaustive manual review of every artifact can become unusable, while an extremely cheap consolidation mechanism can silently destroy project understanding.

The optimization target is therefore not maximum compression or maximum structure. It is:

```text
high-fidelity durable understanding
    under
bounded capture + maintenance + validation + reconstruction cost
```

## 2. Evidence families

The deep dive uses these evidence families:

```text
ACL / NLP summarization evaluation
    factual consistency, content coverage/salience, atomic content units,
    long-document evaluation limitations

Cochrane systematic-review methodology
    duplicate extraction for critical information, reconciliation of disagreements,
    transparent certainty/heterogeneity reporting

W3C PROV-O + Research 127 provenance evidence
    traceability from synthesis through transformation to source

long-context LLM research
    more context is not equivalent to more usable understanding

materialized-view / incremental-view-maintenance research
    read cost, maintenance cost and extra maintained views

self-adjusting computation / dependency tracking
    update the affected computation neighborhood where possible

Build Systems à la Carte
    dependency/rebuild systems occupy a trade-off landscape

ontology-evolution research
    semantic structure itself incurs evolution and consistency cost
```

The goal is cross-domain convergence, not direct transplantation.

## 3. Factual consistency is separate from surface similarity

**Primary research:** Kryscinski et al., *Evaluating the Factual Consistency of Abstractive Text Summarization*, EMNLP 2020.

URL: https://aclanthology.org/2020.emnlp-main.750/

The paper observes that common summarization metrics do not determine whether a generated summary is factually consistent with its source. Their approach checks summary sentences against source evidence and identifies inconsistent spans.

**Transfer:** A fluent durable synthesis can be semantically wrong even when it resembles its sources. Consolidation qualification therefore needs an explicit **source-support/factual-consistency** dimension rather than assuming readability or lexical overlap proves fidelity.

**Transfer limit:** Project-development synthesis contains authority, uncertainty, temporal and relational semantics beyond ordinary factual summarization.

## 4. Factuality and coverage are different fidelity dimensions

**Primary research:**
- Nenkova and Passonneau, *Evaluating Content Selection in Summarization: The Pyramid Method*, HLT-NAACL 2004. https://aclanthology.org/N04-1019/
- Liu et al., *Revisiting the Gold Standard: Grounding Summarization Evaluation with Robust Human Evaluation*, ACL 2023. https://aclanthology.org/2023.acl-long.228/
- Nawrath et al., *On the Role of Summary Content Units in Text Summarization Evaluation*, NAACL 2024. https://aclanthology.org/2024.naacl-short.25/

Pyramid-style evaluation decomposes summaries into semantically meaningful content units and measures whether important content has been selected. Atomic Content Unit work likewise uses fine-grained semantic units to evaluate salience/content coverage.

The key transfer is:

```text
A summary can contain no invented facts
    and still be a bad consolidation
    because it omitted something critical.
```

For ADS, omission is especially material when it removes a governing constraint, known limitation, rejected alternative with important rationale, reopen trigger, dependency/resume condition, conflicting finding, private/public boundary or temporal/supersession qualifier.

Later consolidation mechanisms therefore need a **coverage/completeness** criterion separate from factual consistency.

## 5. Long-document factuality evaluation is itself difficult

**Research:** Bishop, Ananiadou and Xie, *LongDocFACTScore: Evaluating the Factuality of Long Document Abstractive Summarisation*, LREC-COLING 2024.

URL: https://aclanthology.org/2024.lrec-main.941/

The work notes that factual consistency is critical, conventional metrics are inadequate, and many factuality metrics have input-length constraints that make long-document evaluation difficult. It builds a human-annotated long-scientific-document benchmark and a framework for extending factuality assessment to longer sources.

A 2026 ACL study, *Stress Testing Factual Consistency Metrics for Long-Document Summarization*, further reports that widely used reference-free factuality metrics can be sensitive to factuality-preserving perturbations and retrieval context.

URL: https://aclanthology.org/2026.acl-long.1472/

**Transfer:** One automatic summary score is not enough to qualify long project consolidations. High-consequence consolidation needs direct drill-down and proportionate verification.

## 6. Evidence synthesis treats extraction errors as serious and uses reconciliation

**Primary source:** Cochrane Handbook, Chapter 5, *Collecting data*.

URL: https://www.cochrane.org/authors/handbooks-and-manuals/handbook/current/chapter-05

Cochrane recommends more than one person for data extraction because extraction errors can be difficult for downstream reviewers/users to detect. At minimum, subjectively interpreted and interpretation-critical information should be independently extracted by at least two people; disagreements are compared and resolved explicitly.

A methodological review reports extraction-error rates up to 50% in the small included methodological literature.

URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC5704562/

**Transfer:** This is strong non-AI precedent for independent extraction/reconciliation on high-consequence synthesis. It does not imply that every low-risk ADS summary needs two humans or two models. The transferable principle is proportional redundancy for critical consolidation.

Possible later mechanisms include independent model extraction plus reconciliation, model extraction plus deterministic source-unit checks, human/owner review for authority promotions, or another bounded mechanism.

## 7. Good synthesis preserves uncertainty and inconsistency rather than forcing one clean story

**Primary source:** Cochrane Handbook, Chapter 14, *Completing Summary of findings tables and grading the certainty of the evidence*.

URL: https://www.cochrane.org/authors/handbooks-and-manuals/handbook/current/chapter-14

Cochrane's GRADE process requires evidence certainty to be considered explicitly using dimensions such as risk of bias, inconsistency, indirectness, imprecision and publication bias. Judgements are documented and uncertainty is communicated in the summary. Unexplained heterogeneity lowers certainty rather than being averaged away.

**Transfer:** ADS consolidation should preserve **epistemic structure**, not merely conclusions. Where material, durable synthesis must preserve disagreement, conditionality, provisional status, weak/indirect evidence and negative evidence that limits a conclusion.

Flattening source material into one confident narrative is a fidelity failure even when each individual sentence is source-supported.

## 8. High-fidelity consolidation has multiple dimensions

External evidence plus Research 126-128 support treating consolidation fidelity as a vector rather than one score:

```text
F1  SOURCE-SUPPORT FIDELITY
    no material synthesized claim is unsupported by its declared source basis

F2  COVERAGE FIDELITY
    required/important source knowledge is not silently omitted

F3  EPISTEMIC FIDELITY
    uncertainty, disagreement, confidence and unresolved state survive synthesis

F4  AUTHORITY FIDELITY
    synthesis does not silently promote/demote current, candidate, rejected,
    superseded or historical material

F5  RELATIONAL FIDELITY
    important dependency, rationale, supersession, evidence and resume relations survive

F6  TEMPORAL FIDELITY
    required applicability/history/recording distinctions survive

F7  NEGATIVE / MINORITY-EVIDENCE FIDELITY
    important exceptions, counterevidence and rejected rationale are not erased

F8  PROVENANCE FIDELITY
    material synthesis claims retain a traversable route to their source basis

F9  TASK/ABSTRACTION FIDELITY
    the synthesis preserves the information required for its declared use
```

This is an evaluation model, not a requirement that every summary store nine numeric scores.

## 9. “Lossless summary” is the wrong universal target

Any useful synthesis omits detail. Fidelity therefore cannot mean literal preservation of every token in every higher-level view.

> **Compression may discard detail from the active representation only when the discarded detail remains durably recoverable and the synthesis preserves every semantic property required by the view's contract.**

A project-orientation view can omit exact implementation steps. An operational synthesis cannot omit or reorder mandatory steps. An authority view cannot erase supersession/uncertainty. A provenance view may hide current-task noise but cannot destroy the route to original evidence.

## 10. Consolidation should support source-unit drill-down

The Pyramid/ACU literature supports fine-grained semantic units for evaluation. PROV-O and Research 127 establish source/transformation provenance.

A later candidate should therefore demonstrate a way to inspect the source basis for material synthesized units without rereading the full corpus. Possible mechanisms include claim/source links, section-level provenance, source-span references, structured extraction records or source-object relations.

Research 129 does not select a granularity. Universal sentence-level provenance remains unjustified.
## 11. Long context is not a substitute for consolidation

**Research:** Liu et al., *Lost in the Middle: How Language Models Use Long Contexts*, TACL 2024.

URL: https://aclanthology.org/2024.tacl-1.9/

The study finds that model performance can degrade substantially depending on where relevant information appears within long contexts, and that adding more retrieved documents can yield diminishing gains before retriever recall saturates.

**Transfer:** At 5x/10x project scale, the architecture should not treat ever-larger context windows as the primary scaling mechanism.

```text
more durable knowledge
    -> better indexing / consolidation / task-shaped reconstruction
```

is safer than:

```text
more durable knowledge
    -> inject proportionally more raw text into every reasoning context
```

This directly reinforces KA-I12 and the active-knowledge-surface concept.

## 12. D8 empirical ADS scaling snapshot

At Checkpoint 467 / Research 128, the repository contains approximately:

```text
tracked files                         1,554
docs/ files                           1,018
Markdown files                        1,040
Markdown bytes                    9,847,756  (~9.4 MiB)
numbered checkpoints                    468
numbered research records               128
development-governance direct paths     318
```

These are not target thresholds. They are the current empirical anchor for scaling thought experiments.

If the present structures grew approximately linearly without consolidation or structural change:

```text
                         current       5x          10x
tracked files              1,554      7,770       15,540
docs/ files                1,018      5,090       10,180
Markdown files             1,040      5,200       10,400
Markdown volume            9.4 MiB    47.0 MiB     93.9 MiB
numbered checkpoints         468      2,340        4,680
numbered research records    128        640        1,280
development-governance
  direct paths               318      1,590        3,180
```

This is a **linear-pressure thought experiment**, not a forecast that the project will preserve today's artifact ratios.

The 318-path development-governance block is already a warning: a semantically correct routing list can become an expensive human/model navigation surface long before storage volume is technically large.

## 13. Materialized-view research makes read speed versus maintenance cost explicit

**Research:**
- Gupta, Mumick and Subrahmanian, *Maintaining Views Incrementally*, SIGMOD 1993. https://doi.org/10.1145/170036.170066
- Gupta and Mumick, *Maintenance of Materialized Views: Problems, Techniques, and Applications*, IEEE Data Engineering Bulletin 1995. https://sigmod.org/publications/dblp/db/journals/debu/GuptaM95.html
- Ross, Srivastava and Sudarshan, *Materialized view maintenance and integrity constraint checking: trading space for time*, SIGMOD 1996. https://doi.org/10.1145/233269.233361

Materialized views improve query/read performance but incur update/maintenance cost. View-selection research explicitly treats query cost, storage and view-maintenance cost as competing quantities. Incremental maintenance avoids recomputing an entire view when only part of its source changes.

**Transfer:** A future ADS architecture should not generate every conceivable semantic/current-state/task view merely because derived views are rebuildable. Each persistent view creates generation, refresh, freshness, validation and operational cost and must earn that cost through reconstruction/activation value.

## 14. Dependency-local change propagation is a strong scaling principle

**Research:** Acar et al., *A Library for Self-Adjusting Computation*; Acar, Blume and Donham, *A Consistent Semantics of Self-adjusting Computation*.

URLs:
- https://doi.org/10.1016/j.entcs.2005.11.043
- https://doi.org/10.1017/S0956796813000099

Self-adjusting computation tracks dependencies and propagates changes through the affected computation rather than recomputing everything. Reported experiments show large benefits when changes touch a small portion of a large computation, while also showing that dependency tracking has overhead and application-dependent effectiveness.

**Transfer:** The target principle is not “never run a global rebuild.” It is:

> **Routine project changes should normally update only the semantic/dependency neighborhood they actually affect, while occasional automated full rebuilds remain available for repair and qualification.**

Later candidates should therefore measure **change fan-out** explicitly.

## 15. Build-system research reinforces explicit dependency structure

**Research:** Mokhov, Mitchell and Peyton Jones, *Build Systems à la Carte*, ICFP 2018 / JFP 2020.

URL: https://www.microsoft.com/en-us/research/publication/build-systems-la-carte/

The work decomposes build systems into a landscape of choices around dependency discovery, scheduling, rebuilding and correctness rather than treating one build architecture as universally best.

**Transfer:** A generated knowledge view should know enough about its dependencies to decide what needs regeneration after a source change. Hidden implicit dependencies force broad rebuilds or stale outputs. Richer dependency metadata also costs more to maintain, so dependency precision itself is an economic design choice.

## 16. Ontology evolution is a warning about semantic-maintenance cost

**Research:** Zablith et al., *Ontology evolution: a process-centric survey*, The Knowledge Engineering Review.

URL: https://doi.org/10.1017/S0269888913000349

Ontology evolution is a multi-stage process needed to keep semantic models aligned with changes in the modeled domain and information-system requirements. Related work identifies change representation, impact analysis, consistency, validation, traceability, propagation and versioning as maintenance concerns.

**Transfer:** A formal semantic layer is not free. Every additional universal entity type, relation type, lifecycle state or validation invariant can create capture, migration, impact-analysis, consistency, validator and reconstruction burden. Semantic richness must therefore be demand-driven rather than maximal.

## 17. Maintenance economics needs an explicit cost model

Research 129 introduces an architecture-neutral cost decomposition for later candidate comparison:

```text
C_capture
    marginal cost to represent new durable knowledge correctly

C_rel
    marginal cost to maintain necessary relationships/metadata

C_change
    cost of updating existing semantic objects/authority after a change

C_propagate
    cost of refreshing affected derived views/indexes/routes

C_validate
    deterministic + semantic validation/reconciliation cost

C_consolidate
    cost of moving detail out of the active surface while preserving fidelity

C_reconstruct
    cost paid by a fresh collaborator to acquire sufficient understanding

C_migrate
    cost of schema/architecture evolution and repair

C_failure
    expected cost of stale/incorrect/missed knowledge and recovery
```

A candidate that minimizes `C_reconstruct` by exploding `C_capture + C_rel + C_validate` may be worse overall.

No monetary unit is required. Time, model/tool calls, manual decisions, bytes/context, changed artifacts and validation work can be measurable proxies.

## 18. The key D8 scaling metric is marginal fan-out, not total corpus size alone

For one ordinary new knowledge item or local edit, later candidates should measure:

```text
manual artifacts touched
machine-derived artifacts regenerated
authority/relationship objects updated
validators executed
semantic review decisions required
context/tokens consumed to perform the maintenance
```

The desired property is roughly:

```text
ordinary local change cost
    proportional to the affected semantic/dependency neighborhood
    rather than proportional to total historical corpus size
```

Periodic full integrity validation, complete derived-index rebuild or migration may legitimately be corpus-proportional if automated and infrequent.

## 19. Manual global registries are especially dangerous at 5x/10x scale

The current Knowledge Map development-governance block has 318 direct paths. A purely linear continuation would reach roughly 1,590 at 5x and 3,180 at 10x.

The problem is not that a machine cannot store 3,180 strings. It is that each artifact addition may require a human/model to decide whether and where to edit global routing surfaces, creating synchronization burden, drift risk, review burden, collision surface and cognitive overload.

Research 129 therefore strengthens the principle that global navigation views should be generated or consolidated from local authoritative declarations wherever practical rather than manually enumerated forever. This does not select the declaration mechanism.

## 20. Active-surface cost must be measured separately from archival cost

Storage is cheap relative to reasoning attention. An architecture can preserve complete history successfully while still failing because too much history remains permanently active in bootstrap/routing/context surfaces.

At 10x scale, the question is not just whether roughly 94 MiB of Markdown fits on disk. It is whether a fresh collaborator can still identify what matters now, what governs the task, what remains unresolved, what can stay latent and where to drill down without scanning thousands of active routes or loading large portions of the archive into context.

The active knowledge surface therefore needs its own size, fan-out and reconstruction-cost metrics.
## 21. Validation must also scale incrementally

A future architecture with strong integrity checks can still fail economically if every minor edit requires expensive full-corpus semantic validation.

Later candidates should support a layered model such as:

```text
local deterministic checks
    run on every relevant change

impact/dependency-aware checks
    run on the affected neighborhood

broader generated-view rebuild/consistency checks
    run when dependent source sets change

full-corpus qualification / repair rebuild
    run periodically, at milestones or before authority migration
```

This is a comparison principle, not a frozen CI design.

## 22. Consolidation itself is an economic control loop

Without consolidation, active/history surfaces accumulate indefinitely. But consolidation has cost and fidelity risk.

A viable architecture therefore needs an explicit control loop:

```text
knowledge accumulates
    -> active-surface / fan-out / reconstruction metrics rise
        -> consolidation candidate identified
            -> synthesis fidelity checked
                -> active detail moves to latent/history representation
                    -> provenance/drill-down preserved
                        -> active-surface cost falls
```

The trigger should be based on measurable pressure or lifecycle transition, not arbitrary file-count aesthetics.

## 23. D7 architecture-neutral constraints

Research 129 freezes the following fidelity constraints for later reconciliation:

```text
D7-C1  Consolidation fidelity is multidimensional. Factual/source support alone is insufficient;
       coverage, epistemic state, authority, relationships, temporal meaning, negative/minority
       evidence and provenance may all matter.

D7-C2  A fluent or lexically similar synthesis must not be presumed faithful. Material claims need
       source support appropriate to consequence.

D7-C3  Omission is a first-class consolidation failure when the omitted unit affects governing
       constraints, known limitations, uncertainty, dependency/resume, supersession, triggers or
       other information required by the synthesis/view contract.

D7-C4  Contradictory, heterogeneous, uncertain, rejected or minority evidence must not be silently
       averaged into false consensus when it materially affects project understanding.

D7-C5  Higher-level synthesis may intentionally omit detail only when omitted detail remains
       durably recoverable and every semantic property required by the view contract is preserved.

D7-C6  High-consequence consolidation must support proportionate independent verification or
       reconciliation; one unverified generative pass is not sufficient evidence of fidelity.

D7-C7  Material synthesis units must retain a traversable provenance route to source evidence at
       a granularity sufficient to audit the claim without rereading the entire corpus.

D7-C8  Fidelity evaluation must be task/representation-specific. Project orientation, operational
       procedure, authority synthesis and historical narrative have different must-preserve units.

D7-C9  Automatic fidelity metrics may assist validation but must not be the sole qualification
       gate for high-consequence long-document consolidation.

D7-C10 Consolidation should preserve the distinction between summary/current understanding and
       original historical evidence so later reinterpretation remains possible.
```

## 24. D8 architecture-neutral constraints

Research 129 freezes the following scaling/maintenance constraints:

```text
D8-C1  Routine addition or local modification of project knowledge must not require manual edits
       proportional to total corpus size or total project history.

D8-C2  Ordinary change propagation should normally be bounded by the affected semantic/dependency
       neighborhood; occasional automated full rebuild/qualification may remain corpus-proportional.

D8-C3  Every persistent derived view/index creates maintenance/freshness/validation cost and must
       justify that cost through reconstruction, activation or verification value.

D8-C4  Global routing/navigation surfaces should be generated/consolidated from authoritative local
       structure where practical rather than growing as indefinitely hand-maintained enumerations.

D8-C5  Semantic schema richness must be demand-driven. New universal entity/relation/status types
       must earn their capture, migration, validation and change-propagation cost.

D8-C6  Dependency precision is an economic trade-off. Hidden dependencies cause stale state or broad
       rebuilds; excessive dependency metadata can itself dominate maintenance.

D8-C7  Validation should have local/impact-aware and full-qualification modes so routine maintenance
       does not require expensive global semantic verification on every change.

D8-C8  Active knowledge surface size/fan-out/reconstruction cost must be measured separately from
       archival storage size. Cheap storage does not imply cheap reasoning.

D8-C9  Consolidation is a recurring lifecycle mechanism for controlling active-surface growth, not a
       one-time migration cleanup. Its triggers should be measurable and its provenance reversible.

D8-C10 Candidate architecture evaluation at 5x/10x scale must measure marginal maintenance fan-out,
       reconstruction cost, derived-view refresh cost and semantic-review burden, not only storage
       capacity or search latency.

D8-C11 The total system should optimize lifecycle cost across capture, relationships, propagation,
       validation, consolidation, reconstruction, migration and failure recovery rather than
       minimizing any one of those costs in isolation.

D8-C12 Long context must not be used as the primary scaling escape hatch; reconstruction cost and
       active context should remain task-shaped as corpus volume grows.
```

## 25. Candidate-scale qualification metrics introduced by D8

Without yet defining pass thresholds, later candidates should be instrumentable for metrics such as:

```text
M1  manual-touch fan-out per ordinary knowledge addition/change
M2  generated/dependent-view fan-out per change
M3  full-rebuild time/cost
M4  incremental refresh time/cost
M5  validator footprint per change
M6  semantic-review decisions per change
M7  active-route count / active-surface bytes or tokens
M8  cold-start reconstruction reads/tokens/tool calls
M9  governing-source-resolution reads/calls for narrow tasks
M10 consolidation frequency + review cost
M11 stale-derived-view detection/repair latency
M12 schema migration/change-impact footprint
```

These metrics can be measured on the current corpus and mechanically scaled/simulated against 5x/10x synthetic project states during candidate qualification.

## 26. D7-D8 combined stress tests for later candidates

### 26.1 Faithful consolidation under contradiction

Two accepted research streams disagree and one minority stream carries a known limitation. Consolidation must not manufacture consensus and must preserve source drill-down.

### 26.2 Operational detail compression

A long operational history is compressed, but one current mandatory step appears only in an older source plus a later update. The synthesis must preserve the current action contract.

### 26.3 10x local edit

At a synthetic 10x corpus, one local knowledge-unit update should not require touching thousands of unrelated routes/relations or rereading the corpus.

### 26.4 High-degree semantic object

One central concept participates in many relationships. A change must identify the real affected neighborhood and surface unusually high fan-out rather than silently propagating incomplete state.

### 26.5 Derived-index deletion

Delete all semantic/vector/current-state derived indexes. Unique accepted truth must survive; full regeneration must be possible according to each view's declared rebuildability class.

### 26.6 Schema evolution

Introduce, rename or split one semantic relation/type. Measure migration/validation fan-out and whether historical/project authority remains reconstructable during the transition.

### 26.7 Consolidation validator disagreement

A generated synthesis passes factuality checks but fails coverage or authority-state checks. The candidate must refuse promotion or route the discrepancy for reconciliation.

### 26.8 Active-surface saturation

Archive size remains manageable but active routing/reconstruction surfaces exceed their intended budget. The architecture must consolidate or repartition without deleting provenance.

## 27. Counterweights and anti-overengineering conclusions

D7 and D8 together provide a strong brake on several seductive designs:

```text
"store every sentence as a graph node"
    likely excessive identity/relationship maintenance

"generate every useful view continuously"
    likely excessive refresh/validation surface

"summarize aggressively and delete the detail"
    unacceptable provenance/fidelity loss

"keep everything active because storage is cheap"
    ignores reasoning/context cost

"validate every semantic property globally on every edit"
    can make routine maintenance scale with corpus size

"trust one LLM judge score for fidelity"
    insufficient for high-consequence long-document consolidation

"avoid structure entirely to reduce maintenance"
    shifts cost into reconstruction, ambiguity, stale knowledge and failure recovery
```

The goal is a **bounded semantic core with selective structure, generated views, progressive drill-down and measurable lifecycle economics**. That sentence is a design-space orientation, not a target architecture selection.

## 28. Full targeted evidence program status

The planned D1-D8 external-evidence deep dives are now complete:

```text
Research 126
    D1 stable knowledge identity
    D2 multi-axis organization and views

Research 127
    D3 capture -> consolidation -> promotion
    D4 canonical source versus rebuildable derived state

Research 128
    D5 authority-aware retrieval and pre-action activation
    D6 temporal / supersession semantics

Research 129
    D7 consolidation fidelity and provenance
    D8 maintenance economics at 5x / 10x scale
```

The evidence field is now broad enough that continuing to collect general examples risks diminishing returns and confirmation bias.

## 29. Next boundary: requirements/evidentiary-provenance reconciliation

Research 124 originally froze 45 requirements and 15 invariants before this external evidence program. Those statements must now be revisited systematically.

The next phase should **not** immediately design the architecture.

It should produce a reconciliation matrix that asks for every requirement/invariant:

```text
What internal failure or owner goal motivated it?
What external evidence supports or weakens it?
Did D1-D8 add a missing distinction?
Is the requirement too solution-shaped?
Is it redundant with another requirement?
Should its strength be MUST / SHOULD / MAY / candidate discriminator?
What evidence is still only analogy rather than direct project proof?
Which requirements remain primarily owner-value choices rather than empirical claims?
```

Only after that reconciliation should the project create neutral candidate architecture families and expose the withheld owner paper/video at the planned anti-anchoring point.

The target architecture remains unselected.

```text
RESEARCH129_D7_D8=COMPLETE
TARGETED_EXTERNAL_EVIDENCE_D1_D8=COMPLETE
CONSOLIDATION_FIDELITY=MULTIDIMENSIONAL
FACTUALITY_ALONE=INSUFFICIENT
COVERAGE_AND_EPISTEMIC_STATE=FIRST_CLASS
HIGH_CONSEQUENCE_SYNTHESIS=REQUIRES_PROPORTIONATE_RECONCILIATION
ROUTINE_MAINTENANCE_COST=SHOULD_TRACK_AFFECTED_NEIGHBORHOOD_NOT_CORPUS
ACTIVE_SURFACE_COST=SEPARATE_FROM_ARCHIVAL_STORAGE
TARGET_ARCHITECTURE=NOT_SELECTED
NEXT=REQUIREMENTS_EVIDENTIARY_PROVENANCE_RECONCILIATION
WITHHELD_OWNER_SOURCE=STILL_WITHHELD
```