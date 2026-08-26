# Checkpoint 194: Source Universe and Evidence Substrate Architecture Frozen

**Date:** 2026-08-25  
**Status:** Source-substrate conceptual architecture frozen; implementation not yet begun  
**Checkpoint class:** Architecture / stage-boundary checkpoint  
**Project stage:** V1 methodological knowledge-universe construction  
**Scope:** Durable source universe, original artifact preservation, source registry, derived-source lineage, ChatGPT/Git/cloud-drive boundary, and first-corpus validation direction  
**Authority:** Current checkpoint for the source-substrate transition. Foundation 021 is promoted conceptual authority for this scope; exact storage schema and implementation remain unfrozen.  
**Design session:** 06  
**ChatGPT project:** Autonomous Data Science System  
**Session title:** 06 - Methodological Knowledge Universe Construction

## 1. Why this checkpoint exists

Checkpoint 193 established the serious methodological knowledge-universe construction framework and identified source registration/provenance as the next design boundary.

The user then began supplying a broad educational corpus, starting with the VU Amsterdam Machine Learning course, and correctly challenged whether simply uploading hundreds of PDFs into ChatGPT was a sufficiently professional long-term source architecture.

That exposed a deeper prerequisite:

```text
source intake convenience
    !=
durable ADS source/evidence substrate
```

The project therefore stopped further bulk uploads and designed the source substrate first.

---

## 2. Newly accepted conceptual boundary

Research 034 and Foundation 021 now preserve the distinction:

```text
SOURCE UNIVERSE
    exact evidence artifacts + source identity + versions + collections
    + rights/access context + ingestion history + processing lineage

METHODOLOGICAL KNOWLEDGE UNIVERSE
    governed reusable reasoning knowledge
```

A source may support candidate or accepted knowledge, but source availability does not itself create methodological authority.

---

## 3. Core identity distinctions

The source architecture now distinguishes:

```text
Source
    logical publication/document/reference identity

SourceArtifact
    exact byte representation

SourceCollection
    contextual grouping such as a university course or source bundle

SourceMembership
    role/certainty of association with a collection

DerivedArtifact
    rebuildable representation produced from an exact artifact

SourceSpan
    source location used for evidence provenance
```

The exact schema and enum vocabulary are deliberately not frozen yet.

---

## 4. Exact-byte integrity direction

The preferred V1 artifact-integrity/content-addressing digest is SHA-256.

The architecture preserves:

```text
logical source identity
    !=
artifact digest identity
```

Exact duplicate files should converge on one artifact identity even when observed under different filenames or intake events.

Different byte artifacts may still be related semantically, for example annotated/cropped/alternate-format/version variants, and should not be merged automatically.

---

## 5. Original artifact store direction

The preferred first implementation is:

```text
ADS-owned SourceArtifactStore port
        ->
local filesystem content-addressed immutable source store
```

This is a local-first implementation choice, not a permanent provider commitment.

Future adapters may target object storage or managed institutional storage without changing source semantics.

No exact local vault path is frozen.

---

## 6. Registry direction

Source identity/metadata should live in a first-class Source Registry rather than in folder names.

The initial implementation should align with the existing relational/local-first persistence architecture.

The registry should eventually preserve at least:

```text
logical source identity
exact artifact identity/digest
source metadata and canonical locators
source type
versions/variants
collections and membership uncertainty
ingestion events
rights/access/redistribution context
derived-artifact lineage
integrity state
evidence/source-location links
```

---

## 7. Git boundary

The public Git repository remains architectural/preservation authority for:

```text
source-domain code
schemas/migrations
storage ports/adapters
policies
safe metadata/interchange fixtures
processing definitions
integrity/recovery tests
knowledge/source provenance semantics
history and decisions
```

It is not the default vault for:

```text
copyrighted books
restricted lecture material
private source PDFs
large binary archives
machine-local paths
credentials
```

Git LFS is not selected as the source-vault architecture.

---

## 8. ChatGPT boundary

ChatGPT Library and Project Sources remain useful development surfaces but are explicitly non-authoritative for ADS source preservation.

```text
ChatGPT Library
    convenience / cross-chat reuse / intake aid

Project Sources
    small active working context / bounded source bundle

ADS Source Registry + SourceArtifactStore
    durable system-owned source substrate
```

The system must remain recoverable and correct if ChatGPT-side file organization changes or is unavailable.

---

## 9. Cloud-drive boundary

Google Drive, OneDrive, or similar services may later provide:

```text
personal archive
backup/synchronization
intake adapter
human organization
ChatGPT-accessible bridge
```

They do not become the semantic source registry.

A cloud sync location is not assumed to be sufficient backup until recovery/versioning behavior is verified.

---

## 10. Backup/recovery boundary

The source substrate must not become dependent on one local disk.

Before broad educational-corpus intake depends on the new vault, the implementation should demonstrate:

```text
working local source store
    +
independent recoverable backup
    +
verified restore/integrity path
```

The backup provider is not yet selected.

---

## 11. Derived-source lineage

Original artifacts remain immutable evidence.

Operations such as text extraction, OCR, page rendering, chunking, summarization, or embedding create derived artifacts with explicit parent/pipeline lineage.

The design borrows the useful entity/activity/agent distinction from W3C PROV without requiring the internal ADS model to use RDF or the full PROV serialization.

BagIt/RFC 8493 and RO-Crate are preserved as future archival/interchange candidates at their natural boundaries, not selected as internal ontology.

---

## 12. Source-span / knowledge provenance direction

The eventual evidence link should be able to connect a knowledge revision/component to exact source locations such as:

```text
artifact digest + page/page range
section/heading
paragraph/block
figure/table/region
versioned extracted text span
```

Whole-document bibliographies alone are insufficient for consequential reusable claims when finer support can be preserved.

Evidence linkage does not bypass knowledge governance.

---

## 13. Rights/access direction

The source system must preserve enough rights/access context to avoid accidental public redistribution.

The architecture separates:

```text
can ADS access it?
does ADS preserve a copy?
may it be redistributed?
what license/rights statement is known?
is a public canonical locator available?
is it appropriate authority for this proposition?
```

No final enums are frozen.

---

## 14. D-015 status

D-015 remains operationally active for now.

The conceptual source architecture that D-015 deferred has now been resolved, but no governed source store has yet been implemented or validated.

Therefore the current uploaded educational files are still development/intake material rather than an accepted ADS source-vault corpus.

D-015 should be superseded in scope only after the minimal source substrate passes its real-corpus and recovery gates.

---

## 15. First real corpus acceptance test

The already supplied VU Amsterdam Machine Learning batch becomes the first source-substrate validation corpus.

The implemented source subsystem should demonstrate at least:

```text
exact duplicate detection
artifact integrity verification
course collection registration
uncertain association preservation
multiple source types
observed filename history
safe rights/access defaults
deterministic registry export
retrieval of exact source bytes
independent backup and recovery
no accidental Git inclusion of source binaries
```

The user should not upload the next broad course batch until this intake path is available and validated.

---

## 16. Development sequence now

The active sequence becomes:

```text
Checkpoint 193 knowledge-universe framework
        ->
Research 034 + Foundation 021 source-universe architecture
        ->
Checkpoint 194
        ->
Specification 023 minimal source-substrate contract
        ->
local content-addressed SourceArtifactStore
        ->
relational Source Registry
        ->
integrity + deterministic export + bounded lineage
        ->
VU Machine Learning first-corpus ingestion
        ->
backup/recovery + duplicate/variant pressure test
        ->
source-span/evidence integration
        ->
resume six-slice methodological knowledge pressure test
```

This is a prerequisite for professional knowledge construction, not a change away from the methodological knowledge-universe strategy.

---

## 17. Explicit non-decisions

Still open:

```text
exact source database schema/table names
exact source-vault filesystem layout
exact storage root path
final source/collection/right/access enums
backup provider
cloud storage provider
parser/OCR stack
chunking/embedding pipeline
source-span persistence representation
evidence-link relation vocabulary
full provenance serialization
BagIt/RO-Crate adoption level
source-authoring/import UI
remote-source refresh policy
website snapshot policy
retention/deletion policy for source artifacts
```

These should be resolved prospectively in Specification 023 or later pressure tests rather than inferred from this checkpoint.

---

## 18. Promotion audit

### Promoted

A new foundational architecture is warranted because the distinction is cross-cutting, long-lived, and necessary for both knowledge construction and eventual product behavior:

```text
docs/foundations/021_source_universe_artifact_integrity_and_evidence_provenance_architecture.md
```

### Preserved as research rationale

The detailed alternatives, requirements, standards comparison, and phased implementation reasoning are preserved in:

```text
docs/research/034_durable_source_universe_and_evidence_substrate_architecture.md
```

### Not yet promoted to explicit implementation decision

D-015 is not yet superseded. The project has selected the conceptual direction but has not yet demonstrated the operational source substrate.

### No change to knowledge representation authority

Foundation 020 remains the current reusable methodological knowledge-representation foundation. Foundation 021 adds the distinct source/evidence substrate and does not replace Foundation 020.

---

## 19. Exact continuation point

Next:

> **Draft and freeze Specification 023 for the smallest V1 source-registry/artifact-store implementation that can safely ingest, verify, export, back up, restore, and retrieve the existing VU Machine Learning source batch without putting private/copyrighted binaries in Git.**

Do not bulk-upload additional courses before this path is validated.
