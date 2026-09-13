# Research 139: Cross-Model Probe Reconciliation and Real-Corpus Discriminator Protocol

**Date:** 2026-09-13
**Status:** MC-0014 ADVERSARIAL REVIEW RECONCILED / SYNTHETIC ADMISSION CLAIM DOWNGRADED / REAL-CORPUS DISCRIMINATOR PROTOCOL FROZEN / TARGET ARCHITECTURE NOT SELECTED
**Scope:** Reconcile Claude's adversarial review of Common Fixture V0.1 and Relation-Lifecycle V0.2, correct overstated probe interpretations, retire mechanism vocabulary not actually supported by the evidence, and freeze the next real-repository behavioral discriminator before case judgments begin.
**Authority:** Supporting Research 124 architecture evidence and experiment protocol. Requirements V0.2 remain the frozen candidate-acceptance authority. This record does not select a target architecture, storage technology or migration plan.
**Declared references:** `research:124`, `research:134`, `research:136`, `research:137`, `research:138`, `path:docs/model_collaboration/threads/MC-0014/messages/001_claude_adversarial_probe_interpretation.md`, `path:docs/model_collaboration/threads/MC-0014/messages/002_chatgpt_adversarial_review_disposition_and_close.md`, `path:docs/research/PROJECT_KNOWLEDGE_ARCHITECTURE_REQUIREMENTS_V02.md`, `checkpoint:482`

## 1. Why the adversarial review changes the evidence boundary

MC-0014 achieved exactly the purpose reserved for it in Research 134. Claude read not only the prose interpretations but both fixtures, result JSONs and probe implementations. That code-level review exposed two defects that materially change what may be claimed from V0.2:

```text
1. final H1 and H2 both reify the difficult relation as an independently
   identifiable lifecycle-bearing object;

2. the H2 admission/selectivity test reads hand-authored fixture booleans that
   already encode the classification outcome the rule is then praised for recovering.
```

These are not cosmetic wording issues. They change the architecture question.

The project therefore corrects the interpretation before designing the next probe rather than preserving a stronger claim merely because it was already published.

## 2. V0.1 survives adversarial review strongly

The strongest clean evidence from the synthetic phase remains Common Fixture V0.1.

The executable H1 showed that:

```text
directional supplement/conflict relations can be declared once by the asserting source
identity transition history can be owned by the durable subject
workstream state can be owned by first-class workstream sources
joint governing-source closure can be derived deterministically
no duplicate authoritative fact owner is required merely because a relation crosses artifacts
```

Claude independently verified the normalized ownership construction and raw result:

```text
duplicate_authoritative_fact_owners = {}
```

for both candidates.

The important architecture lesson remains:

> **Cross-objectness alone is not a sufficient admission criterion for separate authoritative relation/control ownership.**

One cost should be made more explicit than Research 136 did. If governing sets or similar closures remain derived, the resolver/compiler that computes them becomes a durable correctness-critical architecture component. Avoiding a second authority store does not eliminate semantic machinery; it moves some responsibility into deterministic derivation logic.

## 3. V0.2 family-boundary correction

Research 138 originally treated the strongest H1 and minimal H2 as different relation-ownership families.

The implementation shows a narrower reality.

Both candidates store the difficult relation with:

```text
stable relation id
revision
status
members
relation-specific evidence
timeline
recording/authority/effective temporal fields
supersession state
```

The physical shapes differ mainly in address/namespace:

```text
H1
    source_sidecars[S-A][relations][R-ABC-*]

H2
    relation_spine[R-ABC-*]
```

Therefore:

> **The final V0.2 H1 already performs relation reification.**

It does so inside an endpoint-owned namespace, whereas H2 addresses the relation directly by its own identity.

The experiment remains useful for lifecycle, concurrency, temporal and physical-placement behavior, but it is not a clean test of:

```text
source-local non-reified relation semantics
versus
first-class relation semantics
```

because both sides instantiate the latter for the difficult case.

This also reveals an ambiguity in the V0.2 H1 boundary. Research 137 allowed a tightly source-owned sidecar but prohibited a dedicated authoritative relation object whose lifecycle is independent of the endpoint. The final H1 satisfied the physical source-owned-sidecar condition while functionally giving the nested relation its own independent lifecycle. That is a real boundary leak, not something to hide through terminology.

## 4. V0.2 admission/selectivity correction

The V0.2 fixture explicitly supplies:

```text
stable_relation_identity_required
independent_lifecycle
relation_specific_provenance
natural_endpoint_owner
```

H2's admission function tests those same fields directly.

Consequently:

```text
false-positive admissions = 0
false-negative admissions = 0
```

proves that the implementation follows the predeclared boolean rule. It does not estimate whether that rule can classify real, unlabeled ADS relationships reliably.

The 10/50/100 scale result has the same limitation because every added relation is produced from the same clearly non-qualifying pre-labeled template.

The following claim from Research 138 is therefore withdrawn as empirical classification evidence:

> `H2_ADMISSION_SELECTIVITY=SUPPORTED_IN_V02`

What remains valid is narrower:

```text
H2_RULE_EXECUTION=CORRECT_AGAINST_FROZEN_FLAGS
H2_SYNTHETIC_NONQUALIFYING_RELATIONS=NOT_ADMITTED
REAL_CASE_ADMISSION_PRECISION=UNTESTED
REAL_CASE_ADMISSION_RECALL=UNTESTED
REVIEWER_CLASSIFICATION_AGREEMENT=UNTESTED
```

The rest of V0.2's computed mechanics remain useful. Temporal state resolution, stale-revision rejection, missing-evidence failure and deterministic derived-view rebuild do not reduce to reading the admission flags.

## 5. Vocabulary correction: from bounded spine to selective semantic reification

The probe program has not established that first-class semantic objects need a physically centralized substrate.

A relation with independent identity/lifecycle/provenance could be represented as:

```text
an individually addressable repository-native typed artifact
a source-adjacent but independently identified structured record
a relational row
a graph node/edge object
a compact shared structured store
another inspectable project-controlled representation
```

Nothing in V0.2 discriminates among these.

Therefore the leading representation-neutral mechanism concept becomes:

> **selective semantic reification**

with the broader formulation:

> **selectively first-class semantic/control objects**

The word `spine` remains useful only as the name of one possible physical/ownership arrangement. It is no longer treated as the semantic conclusion of Research 124.

## 6. Maintenance-measurement correction

Claude identified a concrete measurement redundancy in V0.1:

```text
authoritative_location_count
    = len(docs) + len(capture) + spine_record_count

full_rebuild_source_scan_count
    = len(docs) + len(capture) + spine_record_count
```

Those are aliases, not two independent observations.

Likewise, H2's:

```text
manual_global_entries == spine_records
```

by construction.

The raw result file remains immutable evidence of what was run, but future synthesis must not count those pairs as independent support.

The serialized-JSON byte comparison is also weak architecture evidence because field names/nesting are implementation-specific.

The V0.2 authoritative-location-touch count is more meaningful, but it still measures one representation choice, not a universal law.

A cost dimension absent from both probe rounds is now first-class in the next protocol:

> **authoring-time ownership/classification cost**

The project needs to observe how consistently capable reviewers decide where a real relationship belongs before seeing an answer key or another reviewer's judgment.

## 7. H3 disposition after the correction

Research 134 said H3 becomes serious if both conditions hold:

```text
H1/H2 require comparable object/schema machinery anyway
AND
object-primary representation materially simplifies the hard cases
```

V0.2 partially moves the first condition toward true for the difficult relation: both strong implementations use relation-object machinery.

The second condition remains unsupported. V0.1 still shows a clear economy from leaving ordinary relations source-local and deriving closure.

Therefore:

```text
H3_REFERENCE_POLE=RETAINED
H3_REOPENING_TRIGGER_FIRST_HALF=PARTIALLY_OBSERVED
H3_REOPENING_TRIGGER_SECOND_HALF=NOT_OBSERVED
H3_IMPLEMENTATION_NOW=NO
```

## 8. Corrected working hypothesis

After MC-0014, the strongest working hypothesis is deliberately representation-neutral:

> **Keep ordinary facts and directional relations source-local where one source can own them naturally. Permit selective first-class semantic objects where independent identity, lifecycle, provenance, temporal state or conflict/concurrency semantics materially justify addressable continuity. Keep broad navigation, authority closure, search and context views derived/rebuildable unless evidence demonstrates that a specific view must itself become authority. Do not infer physical centralization from first-class identity.**

Two clauses remain explicitly unproven:

```text
how to decide reliably that one source is a natural owner
how to decide reliably that a relationship has earned first-class identity
```

Those are now the primary empirical target.

## 9. Real-corpus discriminator objective

The next stage asks a different question from V0.1/V0.2:

> **Given real ADS relationships with no predeclared architecture label, can independent capable reviewers identify the same semantic ownership/reification class, and can a later mechanized rule reproduce that judgment without having been handed the answer as fixture flags?**

The test is behavioral and corpus-grounded rather than another hand-labeled mechanics fixture.

## 10. Unit of evaluation

One evaluation case is a **relationship evidence packet** drawn from the real public ADS repository at a frozen commit.

A packet may include:

```text
relationship case id
exact repository commit
exact source paths / source hashes
bounded excerpts or structured facts sufficient to understand the relation
relation participants as named in the sources
relevant lifecycle/history evidence when already present in the repository
query/task explaining what ownership decision is being judged
```

A packet must not contain:

```text
H1/H2/H3 labels
`natural_owner` flags
`independent_lifecycle` flags
`should_reify` or equivalent answer fields
reviewer labels
mechanized admission output
```

The packet should preserve enough actual context that reviewers are not classifying from a one-line paraphrase divorced from repository evidence.

## 11. Judgment taxonomy

Each reviewer must choose exactly one primary class:

```text
SOURCE_LOCAL
    one existing/source-like semantic owner can state the authoritative fact fully
    without independently maintained competing truth

FIRST_CLASS_SEMANTIC_OBJECT
    the relationship/activity/identity itself appears to need durable addressable
    continuity distinct from any one participant/source

DERIVED_ONLY
    the queried relationship is best treated as deterministic/rebuildable closure or
    view over authoritative inputs rather than unique authoritative truth

UNRESOLVED
    evidence is insufficient, the case is genuinely ambiguous, or different ownership
    classes remain materially plausible
```

For every case the reviewer must also provide:

```text
proposed natural owner, if SOURCE_LOCAL
what makes the relation/object independently continuous, if FIRST_CLASS
what authoritative inputs generate it, if DERIVED_ONLY
missing evidence / ambiguity, if UNRESOLVED
confidence: HIGH / MEDIUM / LOW
short rationale tied to the packet evidence
```

The taxonomy describes semantic ownership/reification only. It does not ask the reviewer to choose files versus SQL versus graph storage.

## 12. Independent-review discipline

At least two reviewers must judge the same frozen corpus without seeing one another's labels.

The first planned pair is:

```text
ChatGPT
Claude
```

The independence sought is **judgment independence**, not architecture-evidence blindness. Both models may know Requirements V0.2 and the previous probe lessons. They must not see the other reviewer's case labels before their own set is frozen.

The repository sequence should preserve that property mechanically:

```text
A. freeze corpus at immutable commit X
B. ChatGPT produces its complete judgment set from X
C. Claude is routed to exact X, while ChatGPT judgments remain descendant-only and excluded
D. Claude freezes its complete judgment set
E. only then compare labels
```

The ordering may be reversed in a future replication; the critical property is mutual label non-exposure.

## 13. Case-selection discipline

Case selection must not depend on the desired ownership answer.

The initial corpus should intentionally cover several real relationship classes already present in ADS, for example:

```text
supersession / scope replacement
source -> evidence / provenance relation
workstream parent/dependency/resume relation
governing-procedure or specification relation
semantic identity / carrier continuity relation
source-local applicability relation
generated/current-view relation
model-collaboration target/state relation
known-risk / reopen-trigger relation
```

Selection must record **why the case is in the corpus** using category/coverage criteria, not an expected label.

The first corpus should remain small enough for exact-source reading by both reviewers, approximately 12-20 cases. More cases are useful only after the review protocol itself is shown to work.

## 14. Comparison metrics

The comparison stage must report at least:

```text
exact agreement count / rate
agreement by case category
SOURCE_LOCAL / FIRST_CLASS / DERIVED_ONLY / UNRESOLVED marginal counts
high-confidence disagreements
whether both reviewers propose the same natural owner when SOURCE_LOCAL
whether disagreement is label-level or only rationale/confidence-level
cases both reviewers call UNRESOLVED
```

Because the classes are semantic categories and the sample is small, no single scalar score decides architecture quality.

If appropriate, Cohen's kappa may be reported as a descriptive statistic, but it must not replace case-level analysis and may be unstable with skewed class marginals.

## 15. Mechanized-rule stage comes only after judgments freeze

The previous V0.2 error was allowing the fixture to supply the same semantic flags the classifier used.

The real-corpus protocol therefore forbids mechanized admission output before the independent labels are frozen.

Only afterward may Research 124 define candidate observable features, such as evidence of:

```text
independent recorded state transitions while participants remain semantically stable
relation-specific provenance/evidence
stable references to the relationship across artifacts/time
multi-party edits or conflict boundary
one source explicitly asserting the full directional relation
lossy decomposition risk for n-ary semantics
query needs that address the relation itself rather than an endpoint
```

The rule should be evaluated against the frozen judgments, not used to generate them.

If reviewers materially disagree, that disagreement is itself evidence that the admission boundary may not be reliably mechanizable from current project knowledge.

## 16. What this protocol can and cannot establish

A successful result could support claims such as:

```text
capable reviewers can reproducibly distinguish ordinary source-local relations from
cases that appear to deserve first-class semantic identity

or

the boundary is too ambiguous to encode as a simple universal admission rule
```

It cannot by itself decide:

```text
physical storage technology
whole-project migration design
whether every first-class object uses one common schema
whether relation/workstream/identity objects share one substrate
whether retrieval architecture is adequate
whether the full successor satisfies all 50 requirements
```

## 17. Stop rule

Do not proceed directly from reviewer agreement to target selection.

After the real-corpus judgment comparison:

```text
if agreement is high and disagreements are explainable
    -> test a mechanized observable-feature rule against the frozen labels

if agreement is low or high-confidence disagreements remain
    -> analyze those cases before formalizing an admission rule

if most cases are SOURCE_LOCAL/DERIVED_ONLY
    -> keep reification narrow and do not invent a general registry

if many unrelated real cases repeatedly require independent identity
    -> reconsider whether H3 or a broader typed-object layer has become materially simpler
```

## 18. Current disposition

```text
MC0014=RESOLVED
V01_SOURCE_LOCAL_RESULT=RETAINED
V02_LIFECYCLE_MECHANICS=RETAINED
V02_FAMILY_DISCRIMINATION=DOWNGRADED
V02_ADMISSION_SELECTIVITY=WITHDRAWN_AS_REAL_CLASSIFICATION_EVIDENCE
BOUNDED_SPINE_LEADING_LABEL=RETIRED
SELECTIVE_SEMANTIC_REIFICATION=WORKING_CONCEPT
REAL_CORPUS_DISCRIMINATOR_PROTOCOL=FROZEN
REQUIREMENTS_V02=UNCHANGED_FROZEN
TARGET_ARCHITECTURE=NOT_SELECTED
NEXT=FREEZE_UNLABELED_REAL_ADS_RELATIONSHIP_CORPUS
```
