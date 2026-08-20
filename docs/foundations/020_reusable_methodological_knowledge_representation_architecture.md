# Foundation 020: Reusable Methodological Knowledge Representation Architecture

**Date:** 2026-08-20  
**Status:** Foundational methodological-knowledge representation direction  
**Scope:** Long-term Autonomous Data Science System methodological-knowledge layer. This foundation defines durable conceptual separations and representation requirements, not a final ontology, physical schema, storage engine, retrieval engine, rules engine, backend stack, or V1 implementation.

## Purpose

Foundation 019 established the methodological-navigation brain and the idea of a project-specific methodological horizon. The next design question was how reusable methodological knowledge should actually be represented without falling into either of two failures:

```text
one giant unstructured knowledge blob
```

or:

```text
one rigid object or rule for every methodological sentence
```

The representation was stress-tested in two stages.

The first stage used five deliberately different examples:

```text
Histogram
Missing-data investigation
Temporal validation
Random Forest
Prediction-time feature eligibility
```

Checkpoint 102 proposed the first explicit contract. Checkpoint 104 then attacked it adversarially. That review found important defects in the single-role vocabulary, the asset-versus-facet binary, the use of pairwise relations for conditional branch logic, the candidate Assessment object, and the conflation of retrieval with applicability.

A second stress test in Checkpoint 105 re-encoded the five examples using refined primitives and added a new cross-cutting concern:

```text
Class imbalance
```

The refined architecture required no new fundamental primitive across those cases.

This foundation promotes the conceptual conclusions that survived those tests while deliberately leaving exact taxonomies and physical implementation open.

---

## 1. Representation layers remain distinct

The methodological-knowledge system should preserve four conceptual layers:

```text
GLOBAL REUSABLE METHODOLOGICAL KNOWLEDGE
    reusable concepts, methods, frameworks, questions, rules,
    investigation patterns, components, and relations

PROJECT-SPECIFIC KNOWLEDGE AND STATE
    definitions, questions, evidence, findings, claims,
    proposals, investigations, runs, constraints, decisions

EXECUTION CAPABILITY
    concrete implementations capable of realizing selected
    methods or investigations

PRESENTATION / NAVIGATION
    methodological horizon, decision trees, comparison views,
    workspace sections, explanations, reports
```

These must not collapse.

In particular:

```text
global knowledge != project state
project state != execution implementation
internal representation != human-facing view
```

This is consistent with Foundations 017, 018, and 019 and with Prototype V0's core lesson that persistent system memory should not imply sending the entire persistent representation to the LLM on every reasoning call.

---

## 2. The common reusable unit remains an addressable KnowledgeAsset

`KnowledgeAsset` remains a useful conceptual abstraction for independently meaningful reusable methodological knowledge.

An asset should have a deliberately small common semantic/governance envelope, conceptually including:

```text
stable asset identity
revision identity
human-readable title
intrinsic asset kind
purpose
scope
governance / maturity state
provenance
known limitations / counterexamples
```

Optional cross-role structures may include:

```text
reasoning functions / traits
retrieval profile
applicability specification
context requirements
semantic applicability checks
components
```

The exact physical fields are not fixed by this foundation.

### Stable identity versus revision identity

Reusable knowledge evolves.

The system should distinguish:

```text
stable knowledge identity
    from
specific revision used at a point in time
```

Historical project reasoning that materially depended on knowledge should be able to identify which revision influenced it.

New knowledge revisions must not silently rewrite the historical methodological basis of old project decisions or claims.

---

## 3. Intrinsic knowledge form and reasoning function are separate dimensions

The first candidate representation used one semantic-role field containing values such as:

```text
METHOD
FRAMEWORK
EVIDENCE_REQUIREMENT
FAILURE_MODE
INTERPRETATION
CONSTRAINT
STRATEGY
HUMAN_HOOK
```

The stress tests showed that this mixes two different questions:

```text
What kind of reusable object is this?
```

and:

```text
What function does this knowledge play in reasoning?
```

A single knowledge unit may legitimately play several reasoning functions at once.

For example, Prediction-Time Feature Eligibility can simultaneously function as:

```text
hard validity constraint
eligibility criterion
claim constraint
failure-prevention rule
revalidation trigger
```

The representation should therefore separate:

```text
INTRINSIC ASSET KIND
```

from:

```text
REASONING FUNCTIONS / TRAITS
```

A provisional intrinsic-kind vocabulary that survived the stress tests is:

```text
CONCEPT
METHOD
FRAMEWORK
QUESTION_TEMPLATE
RULE
INVESTIGATION_PATTERN
```

This vocabulary is not frozen.

Candidate reasoning functions include:

```text
evidence requirement
validity constraint
interpretation guidance
failure mode
strategy / repair option
human escalation / authority hook
claim limitation
follow-up trigger
```

The durable conclusion is the dimensional separation, not the exact enum labels.

---

## 4. Reusable methodological concepts require first-class identity

The system needs reusable concepts that are neither Methods nor Frameworks.

Examples include:

```text
prediction moment
target horizon
semantic variable type
availability time
bagging
class prevalence
complete case
```

These concepts can provide stable semantic targets for relations, rules, question templates, and project Definitions.

For example:

```text
Global concept:
prediction moment

Project Definition:
for this churn project, prediction moment is 00:00 on the first day
of each scoring month before same-day CRM updates arrive
```

The global Concept defines reusable meaning. The project Definition records the project's concrete semantics.

---

## 5. Knowledge granularity has three levels

A binary choice between full asset and anonymous embedded facet is insufficient.

The representation should support:

```text
KnowledgeAsset
    independently retrievable/reusable/governed unit

KnowledgeComponent
    typed, stably identifiable component owned by an asset
    can carry provenance, revision, and relation semantics
    without independent global retrieval by default

NarrativeFacet
    explanatory or descriptive content without independent identity
```

### Why KnowledgeComponent is necessary

Some knowledge needs stable identity for:

```text
provenance
challenge/review
relation targeting
revision history
component-level reuse within an asset
```

but does not deserve a top-level catalog object.

Examples include:

```text
Histogram bin-width interpretation
one Random Forest hyperparameter semantic
one Missing Data branch rule
one validation-framework limitation
```

This middle layer reduces both asset explosion and loss of important internal structure.

### Promotion rule

A component should be considered for promotion to an independent asset when independent identity materially improves:

```text
cross-context reuse
independent retrieval
independent governance/review
independent versioning
project instantiation/reference
relationship semantics
dependency or validity handling
```

Promotion remains a governance judgment rather than a mechanical object-count rule.

---

## 6. Static semantic relations and conditional methodological rules are different

Checkpoint 102 initially placed substantial meaning in typed relations.

The Missing Data reconstruction showed that two different structures are needed.

### KnowledgeRelation

A `KnowledgeRelation` expresses a relatively stable semantic relationship between identifiable knowledge units.

Examples include families such as:

```text
IS_A
PART_OF
ALTERNATIVE_TO
COMPLEMENTS
GOVERNED_BY
REQUIRES_CONCEPT
CAN_SATISFY
```

Relations may carry:

```text
scope / conditions
rationale
provenance
revision or governance state
```

where those materially affect interpretation.

### Conditional KnowledgeRule

A conditional rule expresses guarded methodological reasoning.

Conceptually:

```text
WHEN
    project/knowledge conditions

THEN
    activate / require / recommend / deprioritize /
    constrain / interpret / request clarification /
    require revalidation

FORCE
    hard validity
    strong guidance
    heuristic guidance
    informational

UNKNOWN BEHAVIOR
    ask
    defer
    block dependent claim/action
    make no inference

RATIONALE / SCOPE / PROVENANCE
```

A rule may be an independent `RULE` asset when independently reusable or a rule component inside a Framework when local to that framework.

The internal representation should not encode an entire data-science process as one giant rule tree.

---

## 7. Conditional rules guide reasoning rather than silently execute analytical decisions

The rule layer exists to support methodological navigation, not to turn the system into a rigid expert-system pipeline.

Preferred behavior is:

```text
rule becomes applicable
    -> activate concern/question/method/strategy
    -> surface a validity requirement or warning
    -> change relevance/prioritization inputs
    -> constrain a claim where required
    -> request clarification where necessary
```

rather than:

```text
rule becomes applicable
    -> silently choose preprocessing/model/reporting action
```

Project actions still pass through the project object model, for example:

```text
Proposal
Investigation
Run
Finding
Decision
```

according to configured human involvement and system autonomy.

### Soft-rule conflicts

Multiple non-hard rules may point in different directions.

They should contribute inspectable reasoning factors rather than being resolved by hidden rule priority.

The methodological relevance layer may weigh:

```text
validity importance
information value
downstream impact
risk
cost
redundancy
project intent
human preferences
```

Hard constraints can dominate incompatible soft recommendations within their declared scope.

---

## 8. Minimal explicit condition structure should remain deliberately small

The system needs enough structure to express deterministic dependencies without inventing a full methodology programming language.

The stress tests required only conceptual support for:

```text
predicate reference
ALL
ANY
NOT
unknown
```

A predicate may refer to:

```text
a mechanically known project fact/property
an answered Question
a current Definition/Finding
a semantic check resolved by flexible reasoning
```

Nuanced applicability should not be forced into a brittle DSL merely because it matters.

The representation should formalize dependencies when formalization creates reliability or efficiency, and retain semantic reasoning where interpretation is genuinely contextual.

---

## 9. Retrieval, applicability, required context, and relevance are separate stages

The first candidate `RetrievalApplicabilityProfile` was too broad.

The refined architecture separates conceptually:

```text
RetrievalProfile
    high-recall signals for entering the methodological horizon

ApplicabilitySpec
    explicit prerequisites/exclusions where reliably expressible

ContextRequirements
    project facts/definitions needed to decide or apply the knowledge

SemanticChecks
    applicability questions requiring interpretation

Project relevance assessment
    project-specific judgment of importance/recommendation/requirement
```

Example:

```text
timestamp present
    -> retrieval signal for temporal-validation knowledge

prediction moment unknown
    -> missing context that may create a Question

intended use is genuinely temporal future prediction
    -> project-specific applicability/relevance evidence
```

Unknown context should not automatically mean `not applicable`.

It may instead require clarification, defer judgment, or block a dependent validity claim.

This architecture remains consistent with Foundation 019's staged relevance model:

```text
KNOWN
    -> APPLICABLE
    -> RELEVANT
    -> RECOMMENDED
    -> REQUIRED / BLOCKING
```

---

## 10. Global knowledge influences project objects in several ways

There should be no universal project-side `KnowledgeInstance` object.

Different reusable assets interact with Foundation 018 project objects differently.

Examples:

```text
QUESTION_TEMPLATE
    -> may instantiate a project Question

METHOD
    -> may be referenced by a Proposal, Investigation, or Run

FRAMEWORK
    -> may become active in project reasoning and organize
       Questions, Proposals, Constraints, and Decisions
       without requiring a FrameworkInstance object

RULE
    -> may generate a Question, project Constraint, warning,
       recommendation, criterion Finding, or revalidation obligation

INTERPRETIVE reasoning function
    -> may influence a Finding or constrain a Claim

HUMAN-ESCALATION reasoning function
    -> may generate a Proposal for clarification/review and later
       a HumanClarification event
```

The system should distinguish:

```text
instantiate
reference
generate
constrain
interpret
trigger
```

rather than flattening all of these into one mapping.

---

## 11. Criterion assessments should use the existing project epistemic chain

The stress tests do not justify adding a universal top-level `Assessment` object.

A reusable criterion applied to a specific project subject can be represented through the existing Foundation 018 epistemic structure.

Example:

```text
Question
    Is feature X available under the prediction contract?

Evidence
    lineage / documentation / timestamps

Finding
    field becomes available after the prediction moment

Criterion Finding facet
    subject = feature X
    criterion = Prediction-Time Feature Eligibility revision R
    verdict = INELIGIBLE

Claim, when needed
    feature X is not eligible for the intended deployment claim

Decision
    exclude / lag / reconstruct feature X
```

A structured criterion-Finding form may include:

```text
subject
criterion knowledge revision
verdict
conditions
supporting evidence
rationale
```

Unresolved state remains a Question.

A user-facing `AssessmentView` may be derived from the Question, Evidence, criterion Finding, related Constraint, and Decision without requiring another durable object family.

---

## 12. Human-facing decision trees and workflows are derived views

The original `Missing_Data.md` tree demonstrated that a useful human workflow can mix:

```text
questions
facts
goals
hard safeguards
strategy alternatives
method options
interpretation cautions
reporting guidance
```

That mixture is appropriate for navigation but not necessarily for canonical internal storage.

A human-facing tree can be derived from:

```text
active Framework
current project facts/Definitions/Findings
unresolved Questions
applicable conditional rules
candidate Strategies/Methods
cross-cutting Constraints
current Decisions
```

Conceptually:

```text
project state changes
    -> evaluate affected rules/applicability
    -> update methodological horizon
    -> activate/deactivate Questions and options
    -> render current path
```

The internal representation therefore remains composable while the user can still receive a clear decision-tree experience.

---

## 13. Worked examples establish the representation boundary

### Histogram

```text
METHOD asset
    + components for binning, normalization, interpretation limits
    + narrative examples
    + relations to ECDF and summary statistics
```

The evidence requirement "understand the empirical distribution" remains separate from Histogram itself.

### Missing Data

```text
FRAMEWORK asset
    + question templates
    + conditional rule components
    + strategy/method references
    + cross-cutting Information Legitimacy rules
    + derived decision-tree view
```

The Framework does not itself become one monolithic executable workflow.

### Temporal Validation

```text
CONCEPT assets
    prediction moment / target horizon / retraining cadence / availability time

FRAMEWORK asset
    temporal-validation strategy reasoning

RULE assets
    evaluation must represent intended temporal generalization
    no unavailable future information in simulated prediction

METHOD assets
    chronological holdout / rolling origin / expanding / sliding windows
```

### Random Forest

```text
METHOD asset
    + mechanism/capability/configuration components
    + relation to Bagging CONCEPT
    + interpretation-rule component
    + separate execution implementations
```

### Prediction-Time Feature Eligibility

```text
RULE asset
    + hard validity / eligibility / claim-constraint functions

Project:
Question -> Evidence -> criterion Finding -> Claim/Decision
```

### Class Imbalance

The new example supports a substantive cross-cutting Framework rather than one method:

```text
FRAMEWORK
    class-imbalance reasoning

CONCEPTS
    prevalence / threshold / error costs / calibration

QUESTIONS
    prevalence stability / decision objective / error costs

METHOD references
    weighting / resampling / class-sensitive metrics /
    threshold tuning / calibration

RULES
    constrain interpretation when majority-dominated metrics
    obscure minority-class performance
```

The same Framework can appear in several human `KnowledgeCollection`s such as EDA, Evaluation, Models, and Thresholding without those collections becoming methodological authority.

---

## 14. Structured-versus-semantic boundary

The representation should remain hybrid.

### Strong candidates for structure

```text
stable identity and revision identity
intrinsic asset kind
operationally meaningful reasoning functions
component identity when independently referenced/governed
provenance references
typed relations
relation scope/conditions where material
retrieval cues
explicit applicability predicates/exclusions
context dependencies
conditional rule guards
rule consequence category
rule force
unknown behavior
project references to knowledge revisions
criterion-Finding subject / criterion / verdict
```

### Strong candidates for semantic prose or semi-structured content

```text
purpose
nuanced scope explanation
mechanism explanation
trade-off reasoning
interpretation narrative
known limitations and counterexamples
examples
human-facing rationale
```

Some knowledge should have both structured dependency semantics and prose rationale.

Maximum formalization is not a goal.

---

## 15. Conflict, supersession, and provenance

Knowledge evolution should be explicit.

Potential conflict may occur at the level of:

```text
asset revision
component
relation
conditional rule
scope boundary
```

Two apparently conflicting rules should first be checked for different scopes rather than assuming one must overwrite the other.

Where a later revision genuinely supersedes earlier knowledge:

```text
historical project references remain intact
new reasoning prefers the accepted current revision
material active dependencies may require re-evaluation
```

Candidate relation concepts such as:

```text
CONTRADICTS
SUPERSEDES
NARROWS_SCOPE_OF
```

may be useful, but the exact taxonomy remains open.

The important requirement is recoverable historical interpretation and inspectable current governance.

---

## 16. The representation must remain open-world

Explicit knowledge structures are a defense against repeated omission, not a closed definition of data science.

The system should still support open-ended reasoning such as:

```text
Given the current project state and methodological horizon,
is an important concern, method, failure mode, or question missing?
```

Repeated useful discoveries can become candidate knowledge gaps and later be promoted into reusable assets/components after review.

This keeps structured knowledge and general reasoning complementary rather than competing.

---

## 17. What this foundation does not decide

This foundation deliberately does not select:

```text
database
relational schema
graph database
vector store
retrieval engine
embedding model
rules engine
ontology framework
schema language
agent framework
backend stack
implementation language
final asset-kind enum
final reasoning-function enum
final relation taxonomy
final condition syntax
final rule consequence vocabulary
```

The next architecture work should derive implementation requirements from this conceptual model rather than choosing technology first.

---

## 18. Durable design conclusions

The representation architecture is now:

```text
KnowledgeAsset
    stable identity + revision
    intrinsic kind
    optional reasoning functions
    optional retrieval/applicability/context structures

KnowledgeComponent
    stably identifiable sub-knowledge when needed

NarrativeFacet
    non-addressable explanatory content

KnowledgeRelation
    stable semantic relationship

Conditional KnowledgeRule
    guarded methodological implication
    standalone or component

KnowledgeCollection
    organizational/navigation grouping

Project object model
    references / instantiates / is constrained or informed by
    global knowledge revisions without one KnowledgeInstance type

Criterion Finding
    structured project Finding form for subject-specific verdicts

ExecutionCapability
    separate implementation bridge

Views
    derived navigation and explanation over knowledge + project state
```

The system should formalize what improves dependency integrity, validity, retrieval, provenance, and repeatability while leaving genuinely contextual interpretation to flexible reasoning.

---

## 19. Next design question

With the conceptual methodological-knowledge representation now promoted, the project can move from **what the knowledge must mean** toward **what capabilities an implementation must provide**.

The next step should still avoid premature technology selection.

First derive implementation requirements from Foundation 020, including:

```text
identity/revision requirements
component addressing
relation traversal needs
conditional-rule evaluation needs
semantic retrieval needs
project-state lookup needs
provenance/history needs
horizon construction needs
LLM context assembly needs
human navigation/query needs
mutation/review/governance needs
```

Only after those requirements are explicit should the project compare persistence, indexing, retrieval, and orchestration architecture options.