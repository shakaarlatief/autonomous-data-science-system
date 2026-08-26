# Research 028: System Identity, Methodological Navigation, and Knowledge-Universe Construction

**Date:** 2026-08-24  
**Status:** Architectural synthesis and forward design note  
**Authority:** Research only. This note does not change accepted production semantics, Specification 020, or any live-experiment authorization.

## Purpose

This memo captures three architectural conclusions that have become clearer through the V0/V1 evidence program and recent design review:

1. the defining distinction between a capable LLM doing data-science work and the intended ADS is system-owned project state;
2. the next defining component is methodological navigation from that state into applicable, relevant, recommended, and required/blocking considerations;
3. the long-term methodological knowledge base should be built as a governed, revisioned methodological universe rather than as a large undifferentiated RAG corpus.

The memo is intentionally broader than the current Specification 020 diagnostic. It preserves durable architectural reasoning that should guide later knowledge-engineering and product phases without prematurely freezing a production ontology.

---

## 1. Defining system distinction: the system owns the project

A standalone LLM can already perform much of the intellectual work of data science:

```text
inspect data
identify missingness and leakage
write and debug code
fit and compare models
reason about validation
interpret metrics
propose transformations
write reports
suggest next investigations
```

Increasing model capability will improve those abilities further. A durable ADS therefore should not be defined primarily by competing with the model on raw intelligence.

The more fundamental distinction is:

```text
LLM DATA SCIENTIST
    intelligence operating over supplied context

AUTONOMOUS DATA SCIENCE SYSTEM
    intelligence operating over persistent,
    authoritative, structured project state
```

Or more compactly:

```text
The LLM reasons about the project.
The system owns the project.
```

System-owned project state gives durable identity to objects such as:

```text
Objectives
Constraints
Questions
Investigations
Runs
Evidence
Findings
Claims
Decisions
Requirements
Dependencies
Approvals
Artifacts
Uncertainty
History
```

and preserves their relations independently of any particular model response.

This extends Foundation 018's core separation:

```text
Objects != Relations != Events != Views
Evidence != Finding != Claim != Decision
current state != event history
persisted object != derived recommendation
```

### Why model intelligence alone is insufficient

A model can infer a dependency in one response. The system must be able to represent that dependency as a persistent, inspectable relation.

For example:

```text
future-generalization-claim
    DEPENDS_ON
future-valid-validation

future-valid-validation
    DEPENDS_ON
prediction-time-feature-audit
```

The project should not depend on the model remembering or reconstructing these relations consistently on every future call.

Persistent state also makes evidence revision operational. New evidence may challenge a claim, which may stale a dependent decision, without requiring the model to reconstruct the entire causal history from prose.

---

## 2. Second defining component: methodological navigation

Structured project state alone would be an intelligent project database. The next defining component is the mechanism that answers:

> Given what is currently true about this project, what methodological considerations are applicable, relevant, recommended, required, or blocking now?

The high-level sequence remains Foundation 019:

```text
KNOWN
    -> APPLICABLE
    -> RELEVANT
    -> RECOMMENDED
    -> REQUIRED / BLOCKING
```

This component connects:

```text
WHAT THE PROJECT IS
        ↓
WHAT METHODOLOGICALLY MATTERS NOW
        ↓
WHAT THE MODEL SHOULD REASON ABOUT
```

It should not be reduced to semantic retrieval. A useful methodological-navigation layer combines:

```text
structured project state
+ deterministic checks
+ reusable knowledge retrieval
+ applicability evaluation
+ conditional methodological rules
+ explicit missing-context handling
+ flexible LLM reasoning
```

### Reactive question answering versus process navigation

A normal LLM interaction is predominantly reactive:

```text
user question
    -> model reasoning
    -> answer
```

The intended ADS should support a state-driven loop:

```text
project state changes
    -> methodological implications change
    -> new concerns become relevant
    -> existing recommendations may become stale
    -> some blocked work may become available
    -> new questions/investigations become justified
```

This is important because neither the user nor the model should be required to remember every expert question spontaneously.

Examples of methodological questions the system should eventually be able to surface from project state include:

```text
What is the prediction moment?
Are all features available at that moment?
Does validation simulate deployment?
Are repeated entities split safely?
Was preprocessing fitted only on training data?
Will the same missingness occur in production?
Is accuracy appropriate for the observed prevalence?
Are calibrated probabilities required downstream?
Is threshold selection isolated from final test evaluation?
Has an earlier project-state change invalidated a downstream claim?
```

### Coverage, not just plausible reasoning

A strong model may produce an excellent analysis while failing to mention one critical concern. A methodological system should increasingly support coverage accounting:

```text
relevant considerations
    -> addressed
    -> resolved
    -> open
    -> missing context
    -> inapplicable
    -> blocking
```

This is a major reason to maintain an explicit methodological universe instead of relying entirely on model recall.

---

## 3. The MethodologicalHorizon remains the scaling boundary

The durable V0 lesson remains:

```text
what the SYSTEM should remember
    !=
what the LLM should receive on every reasoning call
```

The large methodological universe should therefore not become a giant always-on prompt.

The intended flow is:

```text
GLOBAL METHODOLOGICAL UNIVERSE
        ↓
project-conditioned retrieval
        ↓
applicability / missing-context evaluation
        ↓
explained MethodologicalHorizon
        ↓
selective exact-revision context
        ↓
LLM reasoning
```

Specification 013 and Specification 014 already provide bounded evidence for this architecture. The first real-model comparison preserved frozen reasoning quality with a substantial reduction in provider input tokens under SELECTIVE context.

The knowledge universe therefore exists primarily for system memory, coverage, navigation, provenance, and selective activation, not for wholesale prompt injection.

---

## 4. The knowledge base should be a governed methodological universe

The long-term knowledge base should not be designed as:

```text
many documents
    -> embeddings
    -> retrieve similar chunks
```

That can remain one retrieval mechanism, but it is insufficient as the system's methodological brain.

The target is a governed, revisioned universe containing small reusable assets with different knowledge roles.

Foundation 020 already provides the right broad primitives:

```text
KnowledgeAsset
KnowledgeComponent
NarrativeFacet
KnowledgeRelation
KnowledgeRule
KnowledgeCollection
exact revision identity
provenance
maturity/governance
```

A knowledge asset should support much more than an encyclopedia definition. Depending on its type, it may include:

```text
stable identity
intrinsic concepts
reasoning functions
applicability conditions
questions to raise
risks and failure modes
candidate investigations/actions
evidence expectations
static relations
conditional rules
contraindications
narrative facets
implementation guidance
provenance
revision/maturity state
```

### Example: missing data

A useful `missing-data` asset should eventually support questions such as:

```text
Which variables are missing?
How much is missing?
Is missingness associated with the target or predictors?
Is it structural?
Could missingness itself carry information?
Will the same regime occur in production?
Did missingness arise before or after the prediction moment?
```

and risks such as:

```text
global imputation leakage
selection bias from deletion
production mismatch
informative missingness
variance underestimation
inappropriate deterministic imputation
```

This is qualitatively different from storing only a paragraph explaining MCAR/MAR/MNAR.

---

## 5. Build a coverage map before trying to build everything

The first large-scale knowledge-engineering artifact should be a coverage map of the methodological universe, not thousands of individual entries.

Candidate top-level areas include:

```text
problem formulation
measurement and data generation
dataset structure
data quality
exploratory analysis
train/validation/test design
preprocessing
feature engineering
feature selection
model families
model fitting
hyperparameter optimization
evaluation
diagnostics
uncertainty
interpretability
robustness
causal inference
time series
survival/event-time methods
unsupervised learning
NLP
computer vision
sequential modelling
deployment
monitoring
```

The map should be decomposable so the repository can answer operational questions such as:

```text
what areas exist?
which assets are implemented?
which areas are shallow?
which assets lack applicability rules?
which concepts lack behavioral tests?
```

This prevents knowledge growth from being driven only by whichever topics happen to appear in recent projects.

---

## 6. Canonical concepts before duplication

Cross-cutting concepts should exist once and be related to many methods rather than rewritten repeatedly.

Examples:

```text
overfitting
bias-variance tradeoff
regularization
data leakage
sampling variability
distribution shift
prediction moment
calibration
uncertainty
```

Method/model assets can then compose these concepts through relations.

For example:

```text
random-forest
    IS_A -> tree-ensemble
    USES -> bootstrap-sampling
    USES -> random-feature-subsets
    RELATED_TO -> bagging
    ALTERNATIVE_TO -> gradient-boosted-trees
    MAY_HELP_WITH -> nonlinear-effects
    MAY_HELP_WITH -> interactions
```

This should remain a methodological graph rather than a hierarchy alone.

---

## 7. Methodology deserves at least as much coverage as algorithms

A broad ADS knowledge universe must not become a catalogue of models while neglecting professional methodology.

High-value knowledge often concerns:

```text
target validity
unit of observation
prediction moment
feature availability
sampling
validation realism
preprocessing isolation
metric interpretation
uncertainty
decision context
distribution shift
claim validity
```

The system's advantage over a generic model may depend more on reliably remembering these paths than on knowing an additional long tail of algorithms.

---

## 8. Separate intrinsic knowledge, relations, rules, and narrative

Different knowledge types should not be collapsed into one text blob.

Example:

```text
Random forest is a tree ensemble.
```

is intrinsic knowledge.

```text
random-forest IS_A tree-ensemble
```

is a static relation.

```text
IF supervised prediction
AND nonlinear interactions are plausible
AND a nonlinear comparator is decision-relevant
THEN random-forest may become RELEVANT
```

is a conditional methodological rule.

A prose explanation of why bagging reduces variance is a narrative facet.

This separation lets the system remain structured where structure is justified while retaining flexible explanatory knowledge where hard logic would be artificial.

---

## 9. Expert questions are first-class knowledge

A major part of professional expertise is remembering what to ask.

The knowledge-engineering program should therefore explicitly encode expert questions and evidence expectations, not only facts and model descriptions.

Examples:

```text
Temporal prediction
    What is prediction time?
    What is the prediction horizon?
    Which information exists then?
    Does validation preserve temporal ordering?
    Can feature construction see the future?

Class imbalance
    What is positive prevalence?
    Which error matters operationally?
    Is accuracy meaningful?
    Are calibrated probabilities needed?
    Could resampling distort probability calibration?

Missing data
    Is missingness informative?
    Is it structural?
    Does it differ across subgroups?
    Will it recur in production?
```

This is one of the clearest ways the knowledge universe can help the system remember methodological paths that a model may omit in a particular response.

---

## 10. Relations create methodological pathways

Long-term value comes from connected methodological structure such as:

```text
prediction-time-feature-eligibility
    PRECEDES -> defended-model-selection

temporal-validation
    SUPPORTS -> future-generalization-claim

class-imbalance
    AFFECTS -> metric-selection

resampling
    MAY_AFFECT -> probability-calibration

threshold-tuning
    REQUIRES -> held-out-validation

feature-selection
    MUST_BE_FIT_WITHIN -> training-fold

hyperparameter-tuning
    MUST_NOT_USE -> final-test-set
```

These relations can support retrieval expansion, applicability reasoning, sequencing, coverage checks, and later dependency-backed recommendations.

They must not automatically imply production blocking status. Specification 020 is separately testing what structural evidence is required for that stronger classification.

---

## 11. Collections organize neighborhoods without becoming always-on prompts

Reusable collections can group common methodological neighborhoods such as:

```text
binary-classification-core
future-temporal-prediction
missing-data-core
probabilistic-prediction-core
```

Collections should aid organization, retrieval, authoring, and coverage analysis. They should not imply that every contained asset is sent to every model call.

The Horizon/selective-context boundary remains authoritative for prompt construction.

---

## 12. Governance and revision are mandatory at scale

Each accepted asset should be revisioned rather than silently overwritten.

A future reasoning trace should be able to bind to exact knowledge revisions such as:

```text
missing-data@revision
class-imbalance@revision
probability-calibration@revision
```

Candidate maturity states may include concepts such as:

```text
CANDIDATE
REVIEWED
ACCEPTED
DEPRECATED
SUPERSEDED
```

but maturity, scientific confidence, scope confidence, provenance strength, and operational coverage should remain separate dimensions rather than one quality score.

The exact production taxonomy remains open.

---

## 13. Source-backed construction, with LLMs as knowledge-engineering assistants

The broad knowledge universe should not be generated from model memory alone.

The preferred ingestion model is:

```text
authoritative source bundle
    ↓
LLM-assisted extraction/decomposition
    ↓
candidate concepts/assets/facets
    ↓
proposed relations and rules
    ↓
deduplication and contradiction checks
    ↓
schema and semantic validation
    ↓
review
    ↓
accepted exact revision
```

Potential source classes include:

```text
canonical textbooks
high-quality academic material
seminal and methodological papers
review papers
official library/documentation sources
standards or professional guidance where applicable
```

The project's existing methodological materials are a strong controlled seed corpus for validating this ingestion process before scaling to much broader external sources.

---

## 14. Internal methodological core versus external/current research

The system should not attempt to permanently curate every paper or software detail.

A useful distinction is:

```text
CURATED METHODOLOGICAL CORE
    stable
    governed
    revisioned
    reusable

EXTERNAL / CURRENT KNOWLEDGE
    recent papers
    software documentation
    new methods
    domain-specific evidence
    changing capabilities
```

The internal core should help the system recognize when external research is needed and what question that research must answer.

---

## 15. Knowledge assets should be tested like software

At scale, the knowledge system should support deterministic and behavioral quality checks such as:

```text
duplicate concept detection
dangling relations
invalid cycles where prohibited
missing provenance
deprecated assets still referenced
unresolved aliases
contradictory rules
overly broad applicability
assets never retrieved
assets retrieved constantly but never selected
rules that systematically over-recommend
```

Behavioral regression examples may include:

```text
Given state X, asset Y should enter the Horizon.
Given state Z, Y should be INAPPLICABLE.
Given missing fact Q, applicability should be MISSING_CONTEXT rather than FALSE.
```

This turns the knowledge universe into an empirically maintainable system rather than a static encyclopedia.

---

## 16. Real projects should expose coverage gaps

Long-term improvement should come from project replay and governed review:

```text
real project
    ↓
which important consideration was absent?
which appeared too late?
which irrelevant asset appeared?
which rule was too aggressive?
which concept/relation was missing?
    ↓
candidate knowledge revision
    ↓
review
    ↓
accepted or rejected change
```

Project experience must not imply automatic methodological promotion.

```text
experience != authority
candidate learning != accepted knowledge
```

---

## 17. Scaling strategy

Do not build the full universe before validating the knowledge-engineering process.

A sensible staged expansion is:

```text
Stage 1
    tens of high-value foundational assets

Stage 2
    core supervised-data-science lifecycle

Stage 3
    broader modelling, diagnostics, uncertainty, deployment

Stage 4
    time series, causal, unsupervised, and specialized methods

Stage 5
    broad professional data-science coverage

Stage 6
    continuously governed expansion
```

At each stage evaluate:

```text
coverage
retrieval
applicability
relations
selective-context behavior
recommendation effects
```

before multiplying scale.

---

## 18. Candidate future knowledge-engineering pipeline

Once the representation is sufficiently stable, most content production should be assisted or automated while promotion remains governed.

A future pipeline may look like:

```text
source bundle
    ↓
extractor
    ↓
asset decomposition
    ↓
relation proposal
    ↓
rule proposal
    ↓
overlap / duplicate analysis
    ↓
contradiction review
    ↓
coverage review
    ↓
deterministic validation
    ↓
human or governed model review
    ↓
accepted exact revision
```

Specialized agents may eventually be justified for separable roles such as extraction, relation review, contradiction analysis, or coverage review, but multi-agent machinery should still earn its complexity empirically.

---

## 19. Architectural synthesis

The three core layers can be stated compactly:

```text
SYSTEM-OWNED PROJECT STATE
    answers: What is true about this project?

METHODOLOGICAL NAVIGATION
    answers: Given what is true, what matters now?

LLM REASONING
    answers: Given what matters, how should we reason about it?
```

followed by a governed transition layer:

```text
SYSTEM
    decides what state change is admissible,
    authorized, persistent, and auditable
```

The intended long-term loop is therefore:

```text
human intent
    ↓
structured project state
    ↓
methodological universe
    ↓
MethodologicalHorizon
    ↓
selective exact-revision context
    ↓
LLM reasoning
    ↓
candidate recommendations
    ↓
requirements / dependencies / defended scopes
    ↓
governed state transition or execution
    ↓
evidence / findings / claims / decisions
    ↓
updated project state
```

This architecture remains compatible with increasingly capable future models because model intelligence can improve without transferring project identity, authority, provenance, durable state, or governance into the model itself.

---

## 20. Consequence for the current development program

This memo does not justify interrupting the current Specification 020 diagnostic to build the large knowledge universe immediately.

The current program should continue to validate recommendation/blocking semantics first. A broad knowledge-engineering phase becomes much more valuable once the system can distinguish:

```text
knowledge that is merely relevant
knowledge that supports a recommendation
work that is useful
work that is required
work that genuinely blocks a defended downstream scope
```

The knowledge-base construction strategy should therefore remain a forward architectural program while Specification 020 continues on its frozen empirical path.
