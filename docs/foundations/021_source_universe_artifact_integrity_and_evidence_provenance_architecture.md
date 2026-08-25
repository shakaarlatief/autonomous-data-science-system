# Foundation 021: Source Universe, Artifact Integrity, and Evidence Provenance Architecture

**Date:** 2026-08-25  
**Status:** Accepted conceptual foundation for the source/evidence substrate  
**Authority:** Current architectural foundation for source identity, original-artifact preservation, derived-source lineage, and evidence provenance. It is subordinate to current project-wide principles and does not freeze the exact V1 storage schema, physical provider, source-rights enums, parser stack, or knowledge-evidence vocabulary.  
**Origin:** Research 034 and the methodological knowledge-universe construction stage.

## 1. Purpose

A serious methodological knowledge universe requires more than reusable knowledge objects. It also requires a durable evidence substrate that preserves what the knowledge came from and allows exact source artifacts to be recovered, verified, reprocessed, and cited later.

This foundation establishes the conceptual source architecture before bulk source intake.

---

## 2. Source universe and methodological knowledge universe are separate systems

The project adopts the durable distinction:

```text
SOURCE UNIVERSE
    original evidence artifacts, source identities, versions,
    collections, locators, rights/access context, and processing lineage

METHODOLOGICAL KNOWLEDGE UNIVERSE
    governed reusable concepts, questions, methods, assumptions,
    failure modes, decision principles, relations, rules, and claim constraints
```

The source universe supplies evidence and context. It does not automatically become methodological authority.

Therefore:

```text
source available
    !=
source appropriate for a proposition
    !=
knowledge candidate accepted
    !=
knowledge eligible for enforcement
```

---

## 3. Logical source identity is separate from exact artifact identity

The project distinguishes:

```text
Source
    logical publication/document/reference identity

SourceArtifact
    one exact byte representation of a Source
```

Examples of separate artifacts for one logical source may include:

```text
publisher PDF
annotated PDF
cropped PDF
HTML snapshot
EPUB
scan
```

A cryptographic digest identifies exact bytes, not intellectual or semantic equivalence.

SHA-256 is the preferred V1 exact-artifact digest unless a later specification justifies an additional or replacement algorithm.

---

## 4. Original source artifacts are immutable evidence objects

When ADS preserves a source artifact, the original bytes should not be modified in place.

Transformations such as:

```text
text extraction
OCR
page rendering
layout parsing
chunking
summarization
embedding
indexing
```

produce derived artifacts rather than replacing the original.

This preserves the ability to verify what was actually used and to regenerate better derived representations later.

---

## 5. Content addressing is an operational storage property, not the entire domain model

The preferred initial artifact store is content-addressed by cryptographic digest.

This supports:

```text
exact duplicate detection
integrity verification
immutable storage
stable references across filename changes
storage-backend portability
```

However:

```text
artifact digest
    !=
Source identity
```

and:

```text
same semantics
    does not imply
same bytes
```

Near-duplicates, editions, annotations, alternate formats, and semantically equivalent copies remain explicit registry concerns.

---

## 6. Source collection context is first-class but non-owning

The source architecture must support collections such as:

```text
university course
reading list
book series
standards family
methodological source bundle
real-project evidence collection
```

A source may belong to multiple collections without copying the underlying artifact.

Membership must be able to preserve uncertainty. The system should not force a file into "belongs" or "does not belong" when the intake context only justifies "possibly associated".

Collection membership does not imply source authority or knowledge acceptance.

---

## 7. The Source Registry and Artifact Store are separate responsibilities

The architecture separates:

```text
Source Registry
    identity, metadata, relationships, rights/access context,
    collections, ingestion history, processing/evidence references

Source Artifact Store
    exact preserved bytes
```

The initial registry should align with the accepted local-first relational persistence architecture.

The artifact store should sit behind an ADS-owned storage port so that logical source identity does not depend on one filesystem path or one cloud provider.

---

## 8. Local-first is the initial storage implementation, not a permanent provider commitment

The preferred initial source-artifact backend is:

```text
local filesystem content-addressed store
```

behind an ADS-owned port.

Future backends may include object storage or managed institutional storage without redefining source identity or knowledge provenance.

The project does not introduce cloud object-store complexity merely for appearance or premature scale.

---

## 9. Local-first does not mean single-copy

One local disk is not sufficient preservation.

The operational source subsystem should require an independent recoverable backup path before the educational corpus becomes dependent on it.

Synchronization may contribute to this strategy but should not be treated as equivalent to verified backup/recovery automatically.

Recovery should be tested, not merely assumed.

---

## 10. Git is architectural authority, not the default binary source vault

The public repository should preserve:

```text
source architecture
source-domain code
schemas and migrations
storage interfaces/adapters
integrity and recovery tests
processing-pipeline definitions
public-safe source manifests/interchange fixtures
knowledge-to-source provenance semantics
history and decisions
```

The repository should not store restricted or private source binaries by default.

This includes copyrighted books, private lecture material, large source archives, private filesystem paths, and access credentials.

Git LFS is not selected as the default source-vault mechanism because large-file transport alone does not provide the source registry, rights, provenance, collection, lineage, and evidence semantics ADS requires.

---

## 11. Rights, access, redistribution, and authority are separate dimensions

The source substrate must be able to distinguish at least conceptually:

```text
whether ADS can access a source
whether ADS preserves a local copy
whether the source may be redistributed
what license/right statement is known
whether a canonical public locator exists
whether the source is appropriate evidence for a given proposition
```

A source may be valid private evidence inside a local ADS installation while being ineligible for publication or export.

Possessing a digest or a copy does not create redistribution rights.

---

## 12. Ingestion history is event-like provenance

The system should preserve how an exact artifact entered ADS separately from what the artifact is.

An intake event may preserve:

```text
time
channel
observed filename
observed locator
user-supplied course/source context
association uncertainty
artifact digest
result such as new / duplicate / rejected / unresolved
```

Repeated encounters with the same exact artifact should not require duplicate artifact identities.

---

## 13. Original filenames and local paths are not source identity

Filenames are useful human metadata but are not authoritative source identifiers.

Machine-specific local paths are adapter/configuration state and should not be committed as portable public source identity.

External identifiers such as DOI, ISBN, official URL, release/version identifier, or standard number should be represented separately where available.

---

## 14. Derived artifacts are rebuildable lineage products

A derived representation should identify:

```text
exact parent SourceArtifact
processing activity / pipeline
software version
configuration
output identity/digest where useful
creation time
```

This keeps parser behavior, OCR, chunking, summaries, and embeddings reproducible and replaceable.

The conceptual separation is compatible with W3C PROV's distinction among entities, activities, and agents, while ADS remains free to use a simpler internal relational representation.

---

## 15. Evidence provenance should support source locations finer than whole documents

Knowledge revisions should eventually be able to refer to specific source locations such as:

```text
page or page range
section/heading
paragraph/block
figure/table
region
character/token span in a versioned derived representation
```

For PDFs, the combination of exact artifact identity and page location provides a durable coarse anchor even when extraction tooling changes.

Derived text spans may add precision but should not erase the original artifact/page reference.

---

## 16. Evidence relationships are many-to-many and semantically typed

The future knowledge-provenance layer should support the fact that a source location may:

```text
support
define
motivate
challenge
limit
contextualize
implement
```

a knowledge proposition or component.

The exact vocabulary is deferred.

Evidence linkage does not bypass knowledge review. Source support is one input to governance, scope, freshness, and enforcement decisions.

---

## 17. Source acquisition may copy, reference, or do both

The architecture supports three broad modes:

```text
PRESERVED COPY
    exact bytes stored by ADS

EXTERNAL REFERENCE
    source metadata/locator preserved while bytes remain external

PRESERVED SNAPSHOT + CANONICAL REFERENCE
    exact used artifact preserved plus authoritative external locator/version
```

The correct mode depends on rights, reproducibility needs, source volatility, availability, and operational value.

Storage mode does not determine epistemic authority.

---

## 18. ChatGPT Library and Project Sources are development surfaces, not system authority

The project explicitly rejects reliance on ChatGPT file features as the canonical ADS source substrate.

ChatGPT Library may be useful for:

```text
cross-chat reuse
human convenience
development intake
```

Project Sources may be useful for:

```text
small active source bundles
current manifests
construction policies
```

But ADS integrity, recoverability, source identity, and provenance must remain independent of those product features.

---

## 19. Cloud drives are useful adapters and backup/intake surfaces, not the semantic registry

Google Drive, OneDrive, or similar systems may serve as:

```text
personal archive
intake source
backup/synchronization mechanism
human folder organization
ChatGPT-accessible bridge
```

The ADS source model should not depend on their folder hierarchy, object IDs, or availability as its fundamental identity model.

---

## 20. Interoperability standards should be used at their natural boundaries

The project may borrow from or interoperate with established standards without adopting them blindly as internal ontology.

Relevant candidates include:

```text
W3C PROV
    provenance/derivation concepts

BagIt / RFC 8493
    archival transfer/package manifests and checksums

RO-Crate
    research-object metadata/export interoperability
```

Internal ADS semantics remain governed by actual system requirements.

---

## 21. Source preservation quality is separate from proposition authority

The architecture keeps distinct:

```text
artifact integrity/preservation
source authority for a proposition
freshness sensitivity
rights/access state
knowledge governance state
scope confidence
enforcement eligibility
```

A single scalar source-quality or confidence score must not collapse these dimensions.

---

## 22. Educational source intake becomes a substrate validation exercise

The already supplied VU Amsterdam Machine Learning material should be the first real corpus used to validate the implemented source subsystem.

The system should demonstrate at least:

```text
exact duplicate detection
artifact verification
course collection registration
uncertain association preservation
multiple source types
original filename history
safe rights/access defaults
stable registry export
retrieval of exact original bytes
backup/recovery
no accidental Git publication of source binaries
```

Only after this boundary is demonstrated should bulk educational-corpus intake proceed.

---

## 23. Relationship to D-015

D-015 remains operationally in force until the source substrate is actually implemented and validated.

This foundation resolves the conceptual direction that D-015 deliberately left open, but it does not pretend that a durable source vault already exists.

A later implementation/promotion checkpoint may supersede D-015 in scope by establishing the accepted intake path.

---

## 24. Required next step

The next legitimate step is to freeze a bounded V1 source-substrate specification covering:

```text
minimal Source / SourceArtifact / SourceCollection / membership model
artifact-store port
content-addressed local backend behavior
integrity verification
source-registry persistence
rights/access minimum
intake event minimum
deterministic registry export/interchange
bounded derived-artifact lineage
backup/recovery acceptance test
VU Machine Learning first-corpus acceptance test
```

The implementation should remain minimal enough to learn from the real corpus before a larger source ontology or ingestion platform is built.

---

## 25. Core architectural statement

The durable source boundary is:

```text
Source
    !=
SourceArtifact
    !=
SourceCollection membership
    !=
DerivedArtifact
    !=
SourceSpan / evidence location
    !=
Methodological Knowledge
    !=
Knowledge acceptance or enforcement
```

The ADS source subsystem should preserve exact evidence while keeping every later interpretation, extraction, and methodological claim explicit, reviewable, and reversible.
