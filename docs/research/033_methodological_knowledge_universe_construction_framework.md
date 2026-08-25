# Research 033: Methodological Knowledge Universe Construction Framework

**Date:** 2026-08-25  
**Status:** Prospective construction framework for the first serious methodological knowledge-universe stage  
**Authority:** Research and construction-design guidance. This memo does not replace Foundations 007, 008, 019, or 020; freeze a final ontology; promote any candidate knowledge into accepted authority; select a final authoring UI; or authorize a provider-backed experiment.  
**Origin:** Checkpoint 191 strategic transition, Research 028 forward architecture, and the accepted reusable-knowledge representation/persistence boundaries.

## Purpose

Checkpoint 191 deliberately changes the immediate development emphasis from repeated small-universe mechanism experiments to construction of the first serious governed methodological knowledge universe.

The new development sequence is:

```text
serious governed methodological knowledge universe
    -> navigation / selection
    -> project-specific concerns / questions / options
    -> prioritization / disposition
    -> execution and project-state update
    -> real end-to-end project trials
    -> governed knowledge evolution
```

This is chronological with feedback loops rather than a waterfall. Later stages are expected to expose missing knowledge, poor granularity, weak relations, over-broad rules, inadequate provenance, bad retrieval semantics, and other deficiencies that feed back into the knowledge universe.

The immediate problem is therefore not:

```text
How can we generate thousands of method descriptions quickly?
```

It is:

> **How should we construct a broad, deep, source-backed, governed methodological knowledge universe in a way that pressure-tests the existing representation while remaining correctable, reviewable, and operationally useful?**

The framework below defines the first construction cycle before bulk authoring.

---

## 1. Governing constraints from earlier work

Several earlier conclusions constrain this stage.

### 1.1 Persistent knowledge is larger than model context

Prototype V0 established the durable scaling rule:

```text
what the SYSTEM should remember
    !=
what the LLM should receive on every reasoning call
```

A large knowledge universe is therefore system memory and methodological structure. It is not an instruction to inject the entire universe into every model call.

### 1.2 The knowledge universe is broader than an algorithm catalog

Foundation 019 already distinguishes knowledge such as:

```text
methods
concepts
question templates
decision frameworks
hard rules
failure modes
investigation patterns
interpretation knowledge
follow-up / dependency knowledge
```

A model catalog alone would reproduce information that a strong LLM already knows while failing to preserve much of the professional methodology ADS is meant to remember reliably.

### 1.3 The representation is hybrid and revisioned

Foundation 020 establishes durable conceptual distinctions among:

```text
KnowledgeAsset
KnowledgeComponent
NarrativeFacet
KnowledgeRelation
Conditional KnowledgeRule
KnowledgeCollection
exact revision identity
provenance
```

and separates:

```text
global reusable knowledge
project-specific state
execution capability
presentation / navigation
```

These distinctions are the starting representation, not a final ontology that must survive every pressure test unchanged.

### 1.4 Knowledge governance has a higher bar than idea generation

Foundation 008 distinguishes:

```text
reasoning threshold
reuse threshold
enforcement threshold
```

and requires minimum justified generalization. Project observations, LLM proposals, external sources, and local examples may create candidate knowledge without automatically earning reusable or deterministic authority.

### 1.5 Existing persistence/interchange authority must remain intact

The accepted V1 interchange boundary already distinguishes normal candidate/benchmark material from accepted methodological authority. Knowledge-universe construction must use that governance seam rather than creating a second informal authority path.

---

## 2. Construction objectives

The first serious construction program should optimize for five properties simultaneously.

### Breadth visibility

The project should be able to see which major methodological neighborhoods exist and where coverage is absent or shallow.

### Operational depth

Knowledge should preserve the reasoning structure that helps a system act professionally, not merely definitions and summaries.

### Representation pressure

Real content should be allowed to break or refine the current representation. Discovering that an asset is too broad, a relation is too weak, or a rule is too rigid is a successful pressure-test result.

### Governance and traceability

Accepted reusable claims should be attributable to specific source evidence, scope, revision, review state, and limitations.

### Future navigability

Knowledge should expose enough semantics for later retrieval, applicability, relation expansion, coverage review, and project-specific instantiation without being engineered narrowly around the current retrieval implementation.

---

## 3. Deliberate non-objectives

The first construction cycle should not attempt to:

```text
complete all of data science
freeze a perfect universal taxonomy
freeze final production enums
encode every methodological sentence as a rule
turn a folder hierarchy into the ontology
choose a final vector database or reranker
automatically accept LLM-generated knowledge
maximize raw asset count
produce encyclopedic prose for every algorithm
copy entire source documents into the knowledge base
make every knowledge component deterministic
```

A count such as `2,000 assets` is not a success criterion. One hundred deeply operational and well-governed assets can be more useful than thousands of shallow summaries.

---

## 4. The coverage map is a planning layer, not methodological authority

The first durable construction artifact should be a broad coverage map.

Its purpose is to answer questions such as:

```text
What methodological neighborhoods exist?
Which neighborhoods have been decomposed?
Which have source material?
Which have operational components?
Which have relations and behavioral cases?
Which are still shallow or absent?
```

The coverage map must not become another source of methodological truth.

Conceptually:

```text
COVERAGE MAP
    planning / routing / gap visibility

KNOWLEDGE ASSETS + COMPONENTS + RELATIONS + RULES
    reusable methodological content
```

A topic appearing in the coverage map does not imply that the system knows it adequately, that any corresponding asset is accepted, or that the topic is applicable to a project.

The initial map lives in:

```text
docs/methodological_knowledge/COVERAGE_MAP.md
```

---

## 5. Coverage is multi-dimensional rather than one tree

A human-readable hierarchy is useful, but one hierarchy cannot represent the methodological universe completely.

For example:

```text
class imbalance
```

may interact with:

```text
EDA
metric selection
model fitting
resampling
thresholding
calibration
model comparison
monitoring
```

Likewise:

```text
temporal dependence
```

may affect:

```text
splitting
feature eligibility
preprocessing
validation
forecasting
uncertainty
drift monitoring
claim scope
```

The coverage map should therefore be treated as a navigational projection over a cross-linked knowledge universe, not as the internal ontology.

Useful coverage dimensions include:

```text
lifecycle neighborhood
analytical task / objective
data structure / regime
method family
knowledge function
project decision affected
risk / validity role
source coverage
operational depth
behavioral-test coverage
```

No single dimension should own the knowledge identity.

---

## 6. Coverage depth is separate from knowledge maturity

We need a way to say that a neighborhood is shallow without pretending to score epistemic confidence.

The first construction cycle therefore uses a provisional **coverage-depth** ladder:

```text
C0  MAPPED
    neighborhood exists in the coverage map only

C1  SOURCED
    candidate source bundle exists and has been registered

C2  DECOMPOSED
    canonical concepts / candidate assets / boundaries identified

C3  OPERATIONALIZED
    important questions, evidence requirements, alternatives,
    failure modes, assumptions, claim constraints, or diagnostics encoded

C4  CONNECTED
    important static relations and conditional guidance represented

C5  BEHAVIORALLY_TESTED
    positive, negative, boundary, or failure cases exist for important behavior

C6  PROJECT_EXPOSED
    knowledge has been exercised in one or more real project trials
```

These levels measure **coverage construction**, not truth, maturity, source quality, or enforcement authority.

A C6 heuristic can still be a heuristic. A C2 mathematical invariant can have strong epistemic support. Those dimensions must remain separate.

---

## 7. "Knowledge package" is an authoring concept, not automatically a new fundamental primitive

Foundation 007 used the useful idea of a package around one analytical concern. Foundation 020 refined the durable representation into assets, components, facets, relations, rules, and collections.

For the construction program, `package` should initially mean:

> a coherent authoring/review neighborhood containing one or more addressable assets, components, relations, rules, narrative facets, source links, and behavioral cases.

It does **not** automatically become a new persistence primitive.

Examples:

```text
missing-data package
validation-design package
tree-ensemble package
probabilistic-classification package
```

A package may later map naturally to a `KnowledgeCollection`, a set of related assets, or another structure. The pressure test should reveal whether an additional durable primitive is actually necessary.

---

## 8. Operational knowledge target

A useful methodological neighborhood should eventually be able to preserve, where appropriate:

```text
stable concepts and definitions
purpose and scope
question templates
evidence requirements
hard invariants
decision principles
candidate strategies / alternatives
investigation templates
assumption templates
failure modes
detection hooks
diagnostics
interpretation guidance
claim constraints
human / authority hooks
review / assurance hooks
static relations
conditional guidance rules
required context
semantic applicability questions
resolution criteria
reopen conditions
limitations and counterexamples
source provenance
revision and governance state
```

Not every asset needs every element.

The point is to represent enough of the reasoning opportunity space that ADS can remember professional methodological paths a model or human might otherwise omit.

---

## 9. Canonical concepts should be created before repeating them across methods

Cross-cutting ideas should usually have one reusable identity rather than being redefined inside every method.

Examples include:

```text
overfitting
bias-variance tradeoff
regularization
data leakage
prediction moment
target horizon
generalization regime
sampling variability
distribution shift
class prevalence
probability calibration
threshold
uncertainty
```

Method assets can then reference those concepts.

For example:

```text
random-forest
    IS_A -> tree-ensemble
    USES -> bagging
    RELATED_TO -> bootstrap-sampling
    ALTERNATIVE_TO -> gradient-boosted-trees
    MAY_REQUIRE_REVIEW_OF -> probability-calibration
```

This reduces duplication and allows concepts to accumulate richer cross-method relationships.

---

## 10. Source and authority policy must be proposition-sensitive

There should not be one global ranking such as:

```text
textbook > paper > documentation > project
```

because source authority depends on the proposition being supported.

Examples:

### Mathematical or statistical definition/theorem

Preferred support may include:

```text
canonical textbooks
primary theoretical papers
high-quality academic references
```

### Empirical methodological claim

Preferred support may include:

```text
methodological papers
comparative studies
systematic or strong review literature
well-scoped benchmark evidence
```

### Software/API behavior

Preferred support is usually:

```text
official current documentation
source code / release notes where necessary
```

### Standard or governance requirement

Preferred support may include:

```text
formal standards
official regulatory or organizational policy
```

### Practical workflow guidance

Support may legitimately combine:

```text
textbooks
methodological literature
official documentation
well-established professional guidance
project regression cases
```

### Local project fact

The authoritative source is the project evidence itself. It does not automatically support a reusable generalization.

The knowledge system should preserve which proposition a source supports rather than attaching a vague bibliography to a large package.

---

## 11. Component-level provenance is the default for consequential knowledge

Package-level references are too coarse when different components have different evidential bases.

For important components, provenance should eventually support reconstruction of:

```text
which source supports this proposition?
which source location or evidence fragment matters?
what interpretation was extracted?
what scope was asserted?
what transformation occurred between source and knowledge component?
who or what reviewed it?
which revision introduced or changed it?
```

A practical ingestion record may therefore need concepts such as:

```text
source identity
source revision / publication version
source type
source locator
extracted proposition
candidate knowledge target
support relationship
review note
freshness sensitivity
```

The exact schema remains open until the first vertical-slice pressure test.

---

## 12. LLMs are knowledge-engineering assistants, not independent authority

A strong model can help with:

```text
source decomposition
candidate concept extraction
proposed asset boundaries
proposed relations
proposed rules
alias generation
duplicate candidates
contradiction candidates
counterexample generation
behavioral-case drafting
scope challenge
```

But model generation alone does not create independent evidential support.

The preferred ingestion path remains:

```text
authoritative / useful source bundle
    -> LLM-assisted extraction and decomposition
    -> candidate assets/components/relations/rules
    -> duplicate and contradiction review
    -> provenance attachment
    -> semantic / behavioral QA
    -> explicit governance decision
    -> accepted exact revision when justified
```

---

## 13. Existing user-provided material is a controlled seed corpus, not automatic authority

The project already has a substantial controlled corpus covering machine-learning methodology, model families, probabilistic models, deep learning, sequential models, reinforcement learning, and time-series/econometric methodology, plus a detailed missing-data decision artifact.

That corpus is valuable for the first pressure test because:

```text
it is heterogeneous
its concepts are already familiar enough to review carefully
it contains both explanatory and operational material
it spans several very different methodological structures
```

However:

```text
available source != accepted authority
lecture note != universal rule
user-authored decision tree != independently verified methodology
```

Before candidate content from this corpus becomes accepted reusable knowledge, the source should be registered and the proposition-level support/scope should be reviewed under the same governance rules as other sources.

External authoritative sources should be added where needed to strengthen, update, challenge, or broaden the seed material.

---

## 14. Freshness is a property of the proposition, not merely the document date

Different knowledge changes at different rates.

Examples:

```text
AR(1) stationarity condition
    low freshness sensitivity

scikit-learn API behavior
    high freshness sensitivity

current model/provider capability
    very high freshness sensitivity

regulation or policy
    high freshness sensitivity
```

Source records and later review scheduling should therefore be able to distinguish freshness-sensitive from relatively timeless claims.

A recent document does not automatically make an old mathematical statement better, and an old software reference can be invalid even when its methodological principle remains sound.

---

## 15. Knowledge lifecycle must remain multi-dimensional

A single field such as `confidence = 0.87` would collapse several different questions.

The construction program should keep at least these conceptual dimensions separate:

```text
GOVERNANCE STATE
    candidate / reviewed / accepted / challenged / deprecated / superseded

EPISTEMIC SUPPORT
    what supports the proposition within its scope?

SCOPE CONFIDENCE
    how well are applicability boundaries understood?

FRESHNESS STATE
    how sensitive is the proposition to external change and when was it checked?

OPERATIONAL COVERAGE
    has the knowledge been behaviorally tested and project-exposed?

ENFORCEMENT ELIGIBILITY
    may it merely inform reasoning, recommend, constrain claims, or deterministically block?
```

The exact vocabularies remain provisional.

Maturity progression should not silently turn a heuristic into an invariant or an accepted advisory principle into a deterministic constraint.

---

## 16. Duplicate handling needs more than similarity search

Potential duplicates can have several forms.

### Exact semantic duplicate

Two units express the same proposition and scope.

Preferred response:

```text
choose / preserve one canonical identity
retain aliases and provenance ancestry
```

### Parent-child granularity overlap

One unit is a broad framework while another is a reusable subcomponent.

Preferred response:

```text
preserve both if independent identity adds value
connect them explicitly
```

### Scope variant

Two claims look similar but apply under different assumptions or project regimes.

Preferred response:

```text
preserve distinct scoped knowledge
make the boundary explicit
```

### Narrative duplication

The same explanation appears across several method assets.

Preferred response:

```text
move reusable semantics to a canonical concept/component
retain local narrative only where it adds context
```

Semantic similarity can propose duplicate candidates. It cannot decide the merge automatically.

---

## 17. Contradictions are not source-ranking problems

Apparent contradictions should be classified before resolution.

```text
apparent conflict
    -> compare definitions
    -> compare scope
    -> compare assumptions
    -> compare objective / estimand / deployment regime
    -> compare evidence type and source currency
```

Possible outcomes include:

```text
same claim, one source wrong or superseded
scope-specific recommendations that are both valid
terminology mismatch
objective-dependent tradeoff
unresolved genuine disagreement
```

The system should preserve genuine disagreement where appropriate rather than manufacture consensus by choosing the generically highest-ranked source.

A contradiction may narrow scope, reduce enforcement authority, trigger review, or create an explicit unresolved knowledge question.

---

## 18. Relations and rules need separate QA

Static relations and conditional guidance create different risks.

### Static relation QA

Examples:

```text
IS_A
PART_OF
ALTERNATIVE_TO
COMPLEMENTS
REQUIRES_CONCEPT
MAY_AFFECT
```

Checks should include:

```text
valid endpoints
valid relation family
scope compatibility
source/rationale where material
cycle checks where a relation is intended to be acyclic
```

### Conditional rule QA

A rule should be challenged for:

```text
condition precision
unknown behavior
false activation risk
false omission risk
scope
force / authority
interaction with competing soft guidance
whether flexible semantic reasoning is more appropriate than hard logic
```

The construction program must not reward converting nuanced methodology into brittle executable rules.

---

## 19. Knowledge QA should occur at multiple layers

The first serious universe should eventually support at least six QA layers.

### Structural QA

```text
valid identities and revisions
valid schema
required provenance present
no dangling relations
no invalid references
no forbidden governance transitions
```

### Source QA

```text
source exists
source locator is reproducible
claim is actually supported by the cited material
source type is appropriate for the proposition
freshness requirements are satisfied
```

### Semantic QA

```text
purpose is clear
scope is bounded
role is appropriate
claim strength does not exceed support
limitations/counterexamples are represented
```

### Cross-knowledge QA

```text
duplicate candidates
contradiction candidates
orphan concepts
inconsistent aliases
incompatible rules
unintended relation cycles
```

### Behavioral QA

Representative cases can test:

```text
positive applicability
negative applicability
missing-context boundary
failure detection
claim limitation
repair path
reopen condition
counterexample
```

### Project-level QA

Real project trials should eventually measure:

```text
important path missed
irrelevant knowledge surfaced
knowledge surfaced too late
rule too aggressive
question too vague
missing relation
human methodological intervention that the universe should have supported
```

---

## 20. Behavioral tests are first-class knowledge-engineering artifacts

Knowledge should increasingly be tested like software.

A useful behavioral record can say:

```text
Given project state X,
knowledge Y should be considered applicable or relevant.

Given project state Z,
Y should be inapplicable.

Given project state U with missing fact Q,
Y should remain unresolved / MISSING_CONTEXT rather than FALSE.
```

The goal is not to make every semantic judgment deterministic. Behavioral cases provide regression evidence about how the knowledge should participate in reasoning.

They can later support retrieval, applicability, navigation, and end-to-end evaluation without defining the complete project truth.

---

## 21. Retrieval metadata should support future navigation without overfitting to the current retriever

Knowledge construction should preserve distinctions among:

```text
semantic identity
retrieval cues
applicability conditions
required context
project relevance
```

A title, aliases, keywords, examples, and semantic descriptions may improve retrieval. They must not be mistaken for the methodology itself.

The current lexical/dense/hybrid retrieval path remains useful infrastructure, but the universe should not be authored to game one frozen retriever.

Later navigation experiments should occur against the serious universe rather than shaping the universe around the current 28-asset mechanism benchmark.

---

## 22. Deep vertical slices before broad bulk authoring

The first pressure-test cycle should use several structurally different neighborhoods.

### Slice A: Validation and generalization design

Why it is valuable:

```text
high methodological leverage
strong connection to intended use / deployment
question-heavy
contains hard information boundaries and soft tradeoffs
interacts with preprocessing, HPO, feature selection, calibration, and final claims
```

Pressure-test targets:

```text
question templates
evidence requirements
generalization-regime concepts
method alternatives
hard leakage constraints
claim constraints
sequencing relations
```

### Slice B: Missing data

Why it is valuable:

```text
branching concern rather than one method
feature missingness != target-label missingness
production regime changes the correct reasoning
many strategies are legitimate
selection-bias and information-legitimacy failure modes
claim limitations can matter
```

Pressure-test targets:

```text
framework vs asset granularity
question-to-decision relationships
strategy alternatives
cross-cutting safeguards
missing-context behavior
source-specific limitations
```

### Slice C: Feature selection

Why it is valuable:

```text
method family with filter / wrapper / embedded approaches
strong evaluation-boundary interactions
relations to regularization, dimensionality reduction, interpretability, and HPO
method choice depends on task, data scale, model, and objective
```

Pressure-test targets:

```text
method taxonomy without rigid hierarchy
pipeline-fit constraints
relation to dimensionality reduction
comparison/evidence requirements
implementation-independent semantics
```

### Slice D: Tree models and ensembles

Why it is valuable:

```text
model-family concepts and mechanisms
single trees, stumps, bagging, Random Forest, boosting
bias / variance relationships
many static relations
configuration and interpretation components
```

Pressure-test targets:

```text
canonical concepts reused across models
method components
alternative/complement relations
hyperparameter semantics
failure modes
interpretation caveats
execution separation
```

### Slice E: Class imbalance, metrics, calibration, and thresholding

Why it is valuable:

```text
strongly cross-cutting
project objective and error costs matter
accuracy can be misleading
ranking quality != probability quality != thresholded decisions
resampling can interact with probability interpretation
```

Pressure-test targets:

```text
cross-neighborhood relations
decision-context questions
metric purpose/scope
probability and threshold concepts
conditional guidance
human decision hooks
```

### Slice F: Time-series methodology

Why it is valuable:

```text
specialized data-generating structure
temporal dependence
stationarity / integration / cointegration concepts
forecasting and dynamic interpretation
model specification and diagnostics
validation cannot ignore ordering
```

Pressure-test targets:

```text
specialized concepts with mathematical structure
assumption dependencies
model-family relations
sequencing of tests and model classes
forecast/evaluation knowledge
claim-scope distinctions
large neighborhood composition
```

If the representation survives these six neighborhoods deeply, that is stronger evidence than shallowly encoding hundreds of unrelated algorithms.

---

## 23. The six slices should not all be forced into the same package shape

The pressure test should actively look for heterogeneity.

Expected differences include:

```text
Missing data
    framework / concern with branching questions and strategies

Validation
    framework + hard information-boundary rules + method alternatives

Feature selection
    method family with pipeline constraints and comparison logic

Tree ensembles
    method/concept network with mechanisms and configuration components

Imbalance / metrics / calibration
    cross-cutting framework spanning evaluation and decision semantics

Time series
    large specialized methodological domain with concepts, models,
    assumptions, diagnostics, and dynamic relations
```

If one universal mandatory schema feels awkward across these slices, the schema is the thing to change. Content should not be distorted merely to preserve a convenient object model.

---

## 24. First pressure-test deliverable per slice

Before authoring dozens of accepted assets, each slice should produce a bounded design packet containing:

```text
1. slice boundary and purpose
2. source bundle / source register entries
3. coverage decomposition
4. canonical concept candidates
5. candidate asset/component boundaries
6. important question templates
7. evidence requirements
8. alternatives / strategies / methods
9. failure modes and claim constraints
10. relation candidates
11. conditional-rule candidates
12. provenance granularity examples
13. duplicate / contradiction examples
14. behavioral cases
15. representation problems discovered
```

This makes the first stage a **representation pressure test using serious content**, not immediate catalog production.

---

## 25. Breadth-versus-depth expansion strategy

The recommended sequence is:

```text
KU-0  broad coverage map

KU-1  six deep representation pressure tests

KU-2  revise representation / source / lifecycle rules where necessary

KU-3  build accepted core for the supervised data-science lifecycle

KU-4  expand specialized domains and model families

KU-5  begin real project trials against materially larger coverage

KU-6  use project gap extraction to govern expansion and revision
```

Breadth should continue growing during deep work through the coverage map, but large-scale accepted content production should wait until the first six slices have exposed obvious representation defects.

---

## 26. No fixed asset-count target yet

The project should resist using catalog size as a milestone.

Useful construction metrics are closer to:

```text
coverage neighborhoods mapped
high-priority neighborhoods sourced
important operational components represented
important relations connected
behavioral cases present
source/provenance completeness
known contradiction debt
known coverage gaps
project interventions attributable to missing knowledge
```

Asset count can be reported as inventory, not as quality.

---

## 27. Candidate authoring workflow

A first governed authoring loop is:

```text
select coverage neighborhood
    -> register source bundle
    -> decompose source-backed propositions
    -> identify canonical concepts
    -> propose assets/components/facets
    -> propose relations and rules
    -> attach proposition-level provenance
    -> search duplicates / conflicts
    -> challenge scope and claim strength
    -> create behavioral cases
    -> semantic review
    -> import as CANDIDATE_SET through accepted interchange boundary
    -> explicit acceptance only after governance gate
```

The exact authoring representation and tooling remain open until the pressure tests show what authors actually need.

---

## 28. Candidate source-register requirements

Before serious acceptance, the system will likely need a source registry capable of representing at least:

```text
stable source identity
title / author / organization
source class
version / edition / publication date
locator / URL / repository identity
accessed or reviewed date
freshness sensitivity
scope notes
license / quotation constraints where relevant
status
```

Knowledge components should then reference exact source records plus a useful locator rather than embedding uncontrolled bibliographic strings repeatedly.

This is a construction requirement, not yet a frozen production schema.

---

## 29. Source ingestion should preserve source text separately from normalized knowledge

The knowledge universe should not treat extracted prose as the canonical source.

Conceptually:

```text
SOURCE MATERIAL
    original evidence / reference

EXTRACTION RECORD
    what proposition was interpreted from the source

NORMALIZED KNOWLEDGE
    reusable methodological representation
```

This separation allows later reviewers to challenge the extraction without losing the source relationship.

It also supports source updates, changed interpretations, and competing source evidence.

---

## 30. Candidate knowledge changes must remain reviewable diffs

As the universe grows, review should focus on semantic change rather than opaque database mutation.

A useful future change proposal should make visible:

```text
asset/component created or changed
old vs new scope
old vs new proposition
source evidence added/removed
relation/rule changes
maturity/governance change
known dependent assets/projects
behavioral cases added/changed
reason for change
```

The existing exact revision model makes this feasible. Authoring infrastructure should preserve that advantage.

---

## 31. Real projects are part of the construction program, not only final evaluation

Once a materially larger core exists, real projects should begin before the universe is "complete".

Project review should ask:

```text
Which important consideration did ADS miss?
Which knowledge appeared too late?
Which irrelevant knowledge consumed attention?
Which question was too vague to resolve?
Which relation was missing?
Which rule was too aggressive?
Which method family was absent?
Which human methodological intervention added a path the system should have surfaced?
```

The result is a **candidate knowledge change proposal**, not an automatic trusted-library mutation.

This makes the universe dynamic without turning experience into authority by default.

---

## 32. Knowledge-universe gaps and navigation gaps must remain distinct

Specification 022 was designed around a useful failure-attribution distinction that remains valid even though the live execution was incomplete:

```text
UNIVERSE GAP
    the relevant knowledge is absent

NAVIGATION GAP
    the knowledge exists but the system fails to surface it

REASONING / USE GAP
    the knowledge is surfaced but downstream reasoning fails to use it well
```

Building the serious universe makes this distinction more meaningful, not less.

A future navigation benchmark should not penalize the retriever for knowledge that was never curated, and a knowledge-construction program should not hide navigation failure by adding project-specific keywords to assets.

---

## 33. Construction should make uncertainty visible

The universe should be able to say:

```text
coverage unknown
source support incomplete
scope disputed
behavioral coverage weak
freshness overdue
candidate contradiction unresolved
```

Absence of a warning must not imply that the knowledge is complete.

This is especially important during early expansion, when the catalog will necessarily be uneven.

---

## 34. The first construction cycle should produce architecture evidence

Success for KU-1 is not merely "we created six folders."

It should answer questions such as:

```text
Does KnowledgeAsset / Component / Facet remain sufficient?
When does a component deserve promotion to an asset?
Do we need a durable package primitive or are collections/relations enough?
What provenance granularity is practical?
Which relation families recur?
Which rule patterns recur?
Where does hard structure become artificial?
How should contradictions be represented?
What authoring information is repeatedly missing?
Which QA checks can be deterministic?
What kinds of behavioral cases are reusable?
```

Representation changes discovered here should be made before large-scale catalog migration cost accumulates.

---

## 35. Initial coverage map structure

The companion coverage map begins with broad neighborhoods including:

```text
project formulation and objectives
data semantics and generation
data quality and missingness
EDA and descriptive analysis
validation and generalization
preprocessing and representation
feature engineering and feature selection
supervised model families
model fitting / optimization / HPO
metrics / probability / calibration / thresholding
diagnostics / uncertainty / robustness / interpretability
time series / sequential / longitudinal methods
causal / experimental / inferential methods
unsupervised / representation learning
specialized modalities and tasks
deployment / monitoring / revalidation
admissibility / ethics / risk / assurance
reporting / reproducibility / communication
```

This map is deliberately broad and incomplete. Its job is to make incompleteness visible.

---

## 36. Immediate construction gates

Before broad accepted-asset authoring begins, the project should complete these gates:

```text
KU-G01
Coverage map exists and distinguishes coverage depth from knowledge maturity.

KU-G02
The six first vertical slices are explicitly bounded and structurally heterogeneous.

KU-G03
A proposition-sensitive source/authority policy is documented.

KU-G04
Component-level provenance is required for consequential reusable claims.

KU-G05
Duplicate and contradiction handling distinguishes semantic identity from scope conflict.

KU-G06
Knowledge QA covers structure, source support, semantics, cross-unit consistency,
behavior, and eventual project exposure.

KU-G07
Candidate knowledge cannot bypass existing interchange/governance authority.

KU-G08
No raw asset-count target is treated as a quality gate.

KU-G09
Real projects are explicitly part of the later coverage-gap loop.

KU-G10
The first pressure-test cycle is allowed to revise the current representation.
```

These are construction-design gates, not a provider-backed scientific experiment.

---

## 37. Open questions deliberately retained

This framework does not yet freeze:

```text
exact source-registry schema
exact authoring file format
exact candidate asset template
exact maturity-state enum
exact source-authority taxonomy
exact relation vocabulary
exact rule consequence vocabulary
exact contradiction object model
exact coverage metrics
exact review roles / permissions
exact acceptance workflow UI
exact automated extraction tooling
exact external source bundle for each vertical slice
exact behavioral test schema
exact production package primitive
```

Those should be resolved through the six-slice pressure test rather than by speculation alone.

---

## 38. Recommended immediate next sequence

```text
1. freeze this construction framework and the initial broad coverage map
2. create a source-register / source-bundle candidate design
3. perform one coordinated representation pressure test across the six deep slices
4. preserve every representation defect discovered
5. revise Foundation-020-adjacent implementation assumptions only where evidence warrants
6. then begin accepted core construction at materially larger scale
7. resume navigation/selection evaluation against that serious universe
8. begin real project trials before the universe is remotely complete
```

No immediate Specification 022 rerun is required for this sequence.

No provider-backed construction benchmark is required merely to begin building the knowledge universe.

---

## 39. Central construction principle

The strongest synthesis for this stage is:

> **Build broad enough to see the methodological universe, deep enough to expose real representation failures, governed enough that reusable knowledge remains trustworthy, and incrementally enough that the architecture can still change cheaply.**
