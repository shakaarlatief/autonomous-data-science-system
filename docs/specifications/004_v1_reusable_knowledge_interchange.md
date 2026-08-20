# Specification 004: V1 Reusable Knowledge Interchange Contract

**Date:** 2026-08-20  
**Status:** Candidate V1 technical specification v0.1 pending executable validation  
**Scope:** Human-readable, deterministic, storage-neutral interchange for reusable methodological knowledge revisions, components, rules, relations, provenance references, and representative benchmark fixtures  
**Authority:** Candidate implementation contract subordinate to Foundations 019-020 and Specifications 001-003. It must survive schema/round-trip/representative-corpus tests before promotion.  
**Design session:** 02  
**ChatGPT project:** Autonomous Data Science System  
**Session title:** 02 - Methodological Brain & Knowledge Units

## 1. Purpose

Checkpoint 114 established the first production persistence path. The next risk is different:

> the operational database may be technically sound while reusable methodological knowledge remains difficult to review, seed, migrate, diff, test, or retrieve reproducibly.

Specification 001 already requires deterministic human-readable export and explicitly separates authoritative operational state from rebuildable indexes.

This specification defines the first storage-neutral interchange boundary between:

```text
human-reviewable methodological knowledge
        <->
validated application representation
        <->
production knowledge/revision persistence
        <->
derived retrieval indexes
```

The interchange representation must not become a second runtime authority.

---

## 2. Governing distinctions

The contract preserves the existing conceptual boundaries:

```text
KnowledgeAsset != KnowledgeComponent != NarrativeFacet
KnowledgeRelation != Conditional KnowledgeRule
stable identity != revision identity != current pointer
intrinsic kind != reasoning functions
retrieval signal != applicability != required context != project relevance
methodological knowledge != execution implementation
operational authority != interchange representation != derived index
```

The interchange layer serializes these semantics. It does not redefine them.

---

## 3. Canonical V1 interchange syntax: JSON

The canonical V1 interchange syntax is standard JSON.

Rationale:

```text
unambiguous parser semantics
native Python support
mature cross-language support
straightforward deterministic serialization
formal validation through JSON Schema
recursive rule ASTs and heterogeneous nested structures fit naturally
no executable semantics
no comment/anchor/tag features that can alter parser behavior
```

### Alternatives considered

**YAML** offers excellent multiline prose ergonomics, but making YAML the canonical interchange would require an additional parser-semantics contract around implicit typing, aliases/tags, duplicate keys, safe loading, and deterministic emission. YAML may later be supported as an authoring convenience, but it is not the V1 canonical representation.

**TOML** is strong for human-maintained configuration but is less natural for recursive condition ASTs, heterogeneous knowledge components, relation collections, and nested provenance structures.

**Markdown/front-matter hybrids** are excellent presentation formats but would force the application to parse methodological semantics out of a prose-oriented document structure.

The long-term product should normally provide structured UI/editor support, so V1 should prioritize unambiguous interchange and deterministic review over optimizing raw hand-editing ergonomics.

---

## 4. Validation standard

The structural contract is expressed with **JSON Schema Draft 2020-12**.

The V1 schema should:

```text
reject unknown top-level/typed-object properties by default
validate UUID-shaped durable identities
validate stable-key/token patterns
validate rule condition recursion
constrain governance/force/unknown-behavior enums
require explicit schema/bundle versions
keep free-form extension payloads only where Foundation 020 deliberately permits typed payload flexibility
```

The Python implementation should use a Draft 2020-12 capable validator with format checking enabled for UUID fields.

The first tested implementation candidate is `jsonschema` 4.x.

JSON Schema is the interchange-structure contract, not the domain model.

---

## 5. Logical bundle model

V1 defines one logical bundle document:

```text
ReusableKnowledgeBundle
    format
    schema_version
    bundle_kind
    assets[]
    relations[]
    provenance_sources[]
    collections[]
```

Initial physical export may use one JSON file.

Physical sharding is intentionally separate from logical schema. If a future catalog becomes too large for convenient single-file diff/review, the same logical document types can be packaged behind a manifest without redefining methodological semantics.

### Bundle kinds

Initial values:

```text
CANDIDATE_SET
ACCEPTED_SNAPSHOT
BENCHMARK_FIXTURE
```

`BENCHMARK_FIXTURE` is test/evaluation material and must not be silently promoted into accepted operational knowledge.

---

## 6. Knowledge asset revision document

Each bundle asset represents one explicit asset revision and its owned content.

Conceptually:

```text
asset_id
stable_key
revision_id
revision_no
governance_status
intrinsic_kind
title
purpose
scope
limitations[]
reasoning_functions[]
retrieval_profile
context_requirements[]
applicability
semantic_checks[]
narrative_facets[]
components[]
rules[]
provenance_source_ids[]
```

### Identity rules

```text
asset_id
    durable globally unique identity

stable_key
    stable human-facing lookup key

revision_id
    identity of exact serialized knowledge revision

revision_no
    monotonic revision number within the stable asset identity
```

Interchange identities are application/domain identities, not SQLite rowids or database-local sequences.

V1 accepts RFC-compatible UUID values. UUIDv7 remains the preferred production generation strategy, but the interchange format does not make UUID version part of semantic meaning.

---

## 7. Governance and authoring safety

Normal authoring/import must not silently create accepted knowledge.

The intended lifecycle is:

```text
author / generator creates CANDIDATE revision
        -> structural validation
        -> methodological review / challenge
        -> explicit acceptance operation
        -> current accepted pointer advances
        -> prior accepted revision may become SUPERSEDED
```

`CANDIDATE_SET` imports therefore create candidate revisions without changing the current accepted revision.

`ACCEPTED_SNAPSHOT` is a trusted export/restore/migration representation. Normal interactive authoring should not use accepted-snapshot import as a shortcut around governance.

The production repository currently has a convenience `publish_asset_revision()` operation that creates and accepts in one transaction. Before normal interchange import is enabled, persistence APIs should gain explicit candidate-create and accept/publish operations so import cannot bypass the governance model.

---

## 8. Retrieval profile

The interchange contract must carry enough reusable retrieval information to construct high-recall candidate sets without conflating retrieval with applicability.

Initial profile:

```text
aliases[]
lexical_terms[]
semantic_cues[]
negative_cues[]
```

These are retrieval hints only.

Example:

```text
Temporal Validation

lexical terms:
    chronological split
    time split
    rolling origin

semantic cue:
    performance should estimate future deployment after training on earlier observations
```

A timestamp being present may retrieve the asset while applicability remains unresolved.

---

## 9. Applicability and context requirements

The interchange should preserve three separate structures.

### ContextRequirement

A named project semantic needed to decide/apply knowledge:

```text
key
required_for[]
description
```

Example:

```text
prediction_moment
required_for = [APPLICABILITY, RULE_EVALUATION]
```

### Applicability

Mechanical prerequisites/exclusions that can be represented reliably using the minimal condition AST.

### Semantic checks

Natural-language questions that require interpretation rather than forced formalization.

Unknown context must remain distinguishable from negative applicability.

---

## 10. Components and narrative facets

A component carries stable identity when component-level provenance/revision/relation semantics matter:

```text
component_id
component_key
component_kind
revision_id
revision_no
governance_status
body
payload
reasoning_functions[]
provenance_source_ids[]
```

A NarrativeFacet has no independent durable identity:

```text
facet_kind
position
body
```

This preserves Foundation 020's three-level granularity model.

---

## 11. Conditional rule representation

Rules use the already-promoted deliberately small condition language.

Condition nodes are exactly one of:

```text
Predicate
ALL
ANY
NOT
```

Predicate form:

```json
{
  "predicate": "project.task.is_supervised",
  "arguments": {}
}
```

Composite forms:

```json
{"all": [ ...conditions... ]}
{"any": [ ...conditions... ]}
{"not": { ...condition... }}
```

A rule also records:

```text
rule_spec_id
rule_key
condition
consequence_type
consequence_payload
force
unknown_behavior
rationale
provenance_source_ids[]
```

No raw SQL, Python, shell, JavaScript, or arbitrary evaluation expression is allowed.

---

## 12. Static relation representation

Relations remain distinct from rules.

A relation document records:

```text
relation_id
relation_revision_id
revision_no
governance_status
source_ref
target_ref
relation_type
scope
rationale
provenance_source_ids[]
```

For interchange readability and portability, endpoint references use stable semantic node references:

```text
asset_key
optional component_key
```

rather than requiring reviewers to resolve UUIDs manually.

The importer resolves these references to the durable asset/component identities and rejects missing or ambiguous targets.

This does not replace the durable UUID identity of the relation itself.

---

## 13. Provenance references

The bundle may contain lightweight provenance-source records:

```text
source_id
source_type
title
locator
version_or_fingerprint
notes
```

The source record references the source; it does not silently copy the full external source into the repository.

This is compatible with D-015, which continues to keep currently attached learning/source materials outside the repository until the broader external-source architecture is explicitly designed.

Initial provenance roles are intentionally references rather than a complete citation ontology.

---

## 14. Deterministic serialization

For the same validated logical bundle, the V1 exporter must emit byte-stable output under the same schema version.

Rules:

```text
UTF-8
LF newlines
final newline
2-space indentation
JSON object keys sorted lexicographically
Unicode emitted directly rather than ASCII escaping where safe
assets sorted by stable_key
components sorted by component_key
rules sorted by rule_key
relations sorted by source_ref / relation_type / target_ref / relation_id
provenance sources sorted by source_id
collections sorted by collection_key
semantically-set-like string lists sorted and deduplicated by the application
```

Arrays whose order is meaningful, such as NarrativeFacet presentation order, retain explicit order.

### Semantic hashes

Database semantic content hashes are computed from the parsed/validated semantic projection, not from raw file bytes.

Therefore formatting-only changes must not create a different semantic hash.

V1 does not require RFC 8785 JSON Canonicalization Scheme for the initial interchange because the application controls the constrained semantic projection and does not currently sign interchange documents cryptographically. RFC 8785 remains the preferred standards-based escalation path if cross-language cryptographic canonicalization/signing becomes a requirement.

---

## 15. Import semantics

Import must be transactional at the semantic unit level and must be idempotent where identity/content agree.

Required behavior includes:

```text
same revision_id + same semantic hash
    -> idempotent/no duplicate revision

same revision_id + different semantic content
    -> hard conflict

same stable_key + different asset_id
    -> hard identity conflict

unknown relation endpoint
    -> reject relation import

CANDIDATE_SET
    -> never advances accepted-current pointer implicitly

ACCEPTED_SNAPSHOT
    -> trusted restore/bootstrap path only
```

The import layer must validate the complete logical document before applying authoritative writes whenever feasible.

No external file/network/LLM call should occur inside the database write transaction.

---

## 16. Export semantics

The first required export is:

```text
CURRENT_ACCEPTED_SNAPSHOT
```

It contains current accepted reusable knowledge and enough stable identity/revision/provenance information for:

```text
human review
diffing
debugging
migration verification
reproducible retrieval fixtures
```

Historical database revision history remains authoritative in the operational store.

A later full-history archive format may be added if operational recovery/migration evidence demonstrates the need. The current interchange does not pretend that one snapshot replaces database backup/history.

---

## 17. Representative stress corpus

The first executable validation should encode the already-studied heterogeneous examples:

```text
Histogram
Missing Data
Temporal Validation
Random Forest
Prediction-Time Feature Eligibility
Class Imbalance
```

and several helper/distractor concepts/methods needed to exercise relations and retrieval, such as:

```text
Prediction Moment
Bagging
ECDF
Gradient-Boosted Trees
```

The corpus must be marked `BENCHMARK_FIXTURE` and `CANDIDATE`; it is not automatically accepted global knowledge.

This gives the interchange schema a real heterogeneity test without silently promoting test fixtures into production methodological authority.

---

## 18. Executable validation gate

Before promotion to v1.0, the candidate must demonstrate:

```text
KI-01  JSON Schema validates itself under Draft 2020-12
KI-02  representative heterogeneous bundle validates
KI-03  unknown typed properties are rejected
KI-04  malformed UUIDs and stable keys are rejected
KI-05  malformed recursive rule conditions are rejected
KI-06  deterministic dump -> load -> dump is byte-identical
KI-07  semantic digest is unaffected by insignificant input formatting
KI-08  relation endpoint references resolve uniquely in the representative corpus
KI-09  duplicate stable keys / IDs / component keys / rule keys are rejected by application validation
KI-10  bundle-kind/governance safety rejects candidate content masquerading as trusted accepted import
```

A later persistence round-trip gate should then prove candidate import, explicit acceptance, accepted export, and revision-history pinning through the production repository.

---

## 19. Explicit non-goals

Specification 004 v0.1 does not select:

```text
embedding model
reranker
retrieval fusion algorithm
ANN/vector backend
knowledge authoring UI
external source ingestion service
cryptographic signing
full-history portable archive
complete knowledge taxonomy
full relation ontology
full provenance ontology
```

The interchange format exists to make those later choices testable rather than to pre-decide them.

---

## 20. Promotion criterion

Promote this specification only if the executable interchange tests pass on the representative corpus without requiring a conceptual exception for any of the six core methodological examples.

If the corpus requires many format-specific escape hatches, revise the contract before building import/export and retrieval on top of it.

---

## External standards/research references

Current official references consulted during this design step:

```text
JSON Schema Draft 2020-12
https://json-schema.org/draft/2020-12

RFC 8785: JSON Canonicalization Scheme
https://www.rfc-editor.org/rfc/rfc8785.html

python-jsonschema documentation
https://python-jsonschema.readthedocs.io/
```

The project-specific architectural conclusions remain governed by Foundations 019-020 and Specifications 001-003 rather than by any single external tool or standard.
