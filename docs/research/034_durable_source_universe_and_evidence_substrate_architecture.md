# Research 034: Durable Source Universe and Evidence Substrate Architecture

**Date:** 2026-08-25  
**Status:** Architectural research and implementation-direction memo  
**Authority:** Research guidance for the source-universe stage. This memo does not itself authorize bulk source intake, copy private/copyrighted source binaries into Git, freeze a final physical storage provider, or promote extracted source content into accepted methodological knowledge.  
**Origin:** Checkpoint 193 knowledge-universe construction boundary, D-015 deferred source-storage decision, Research 033 source/provenance requirements, and the Session 06 source-corpus discussion.

## Purpose

The first serious methodological knowledge-universe stage exposed a prerequisite that should be resolved before bulk source intake:

> **What is the durable source substrate that preserves exact original source artifacts, their identity, provenance, versions, collection context, derived representations, and links to governed methodological knowledge without making ChatGPT, Git, or one storage provider the accidental system authority?**

The source problem is not merely file organization. The eventual ADS should be able to answer:

```text
Which exact source artifact supports this knowledge component?
Which version or edition was used?
Where in the source does the support occur?
Was the source copied, linked, or externally referenced?
Is this source private, licensed, public, or redistribution-restricted?
Which extraction pipeline produced this text/chunk/table/figure representation?
Can the original bytes still be verified?
Can all rebuildable source representations be regenerated?
Can the source backend change without changing methodological semantics?
```

This memo designs that boundary before the current educational corpus is ingested in bulk.

---

## 1. Governing constraints already present in the repository

### 1.1 D-015 deliberately deferred this decision

D-015 keeps currently attached learning materials outside the GitHub repository because copying them would prematurely define an external-source architecture.

That decision was correct. The current stage now supplies enough requirements to design the missing substrate rather than continuing to rely on chat attachments implicitly.

### 1.2 Source material is not accepted methodological authority

Research 033 establishes:

```text
available source != accepted authority
lecture note != universal rule
LLM extraction != independent evidence
```

The source substrate must therefore preserve evidence without collapsing evidence into accepted knowledge.

### 1.3 Local-first remains an accepted system direction

D-028 selects a SQLite-centered local-first operational architecture for current V1 system state. The source subsystem should align with that direction where reasonable while avoiding hard coupling between logical source identity and one machine-specific filesystem path.

### 1.4 Persistent system memory is larger than model context

The source universe may eventually contain hundreds or thousands of documents. It is system memory, not a prompt attachment set.

ChatGPT Project Sources, chat attachments, or one giant model context are therefore not the target architecture.

---

## 2. Fundamental distinction: source universe versus methodological knowledge universe

The project should preserve a first-class separation:

```text
SOURCE UNIVERSE
    original evidence artifacts and their provenance

METHODOLOGICAL KNOWLEDGE UNIVERSE
    governed reusable reasoning knowledge derived from, supported by,
    challenged by, or contextualized by source evidence
```

The relationship is many-to-many.

One source may support many knowledge components. One knowledge component may require several sources. A source may be useful for discovery while not being strong enough to justify acceptance. A source may challenge or narrow an existing component rather than support it.

Conceptually:

```text
SourceArtifact / SourceSpan
        |
        | evidence relationship
        v
KnowledgeComponentRevision
```

The source universe should survive even if the knowledge representation changes later.

---

## 3. Source substrate requirements

The first source architecture should satisfy the following requirements.

### S-01 Exact-byte identity

The system must be able to identify and verify the exact bytes of an ingested artifact.

### S-02 Logical identity separate from byte identity

A publication, lecture, book, standard, documentation page, or other logical source may have multiple exact artifacts, editions, versions, formats, or annotated copies.

### S-03 Immutable original preservation

Ingested original bytes should not be modified in place.

### S-04 Duplicate-safe ingestion

Exact duplicates should be detected by content rather than filenames.

### S-05 Collection context

Sources must be able to belong to collections such as courses, reading lists, books, standards families, source bundles, or project evidence sets without physical duplication.

### S-06 Uncertain association

The system must be able to preserve uncertain membership such as "possibly associated with this course" without forcing a false yes/no classification.

### S-07 Rights and access metadata

Private possession, public availability, licensing, redistribution restrictions, and access sensitivity must not be conflated.

### S-08 Derived-artifact lineage

Extracted text, rendered pages, tables, figures, chunks, summaries, embeddings, and other derived representations must identify the exact parent artifact and processing pipeline.

### S-09 Source-location provenance

Knowledge should eventually be able to point to source locations such as pages, sections, paragraphs, table/figure regions, or machine-readable spans.

### S-10 Rebuildability

Derived source representations and retrieval indexes should be rebuildable from preserved originals plus versioned processing configuration.

### S-11 Backend portability

The domain model must not encode one local path, cloud vendor, ChatGPT feature, or object-store provider as source identity.

### S-12 Integrity verification

The system should be able to verify stored bytes against their recorded digest and detect missing/corrupted objects.

### S-13 Backup/recovery

A source corpus should not depend on one physical device or one synchronized folder without a tested recovery path.

### S-14 Public-repository safety

The public Git repository must not accidentally publish restricted source binaries, private local paths, credentials, or sensitive access locators.

### S-15 Scalable retrieval

The architecture must support later search over the corpus without turning the search index into source authority.

---

## 4. Architecture decision: registry plus artifact store plus derived store

The preferred architecture separates three operational concerns.

```text
SOURCE REGISTRY
    semantic identity, metadata, relationships, governance/access metadata

ORIGINAL ARTIFACT STORE
    immutable exact source bytes

DERIVED ARTIFACT / INDEX LAYER
    rebuildable representations and retrieval structures
```

### 4.1 Source Registry

The Source Registry should become authoritative operational state for source identity and provenance metadata.

The initial V1 implementation should fit the existing local-first persistence architecture, most likely as relational state in the ADS operational database.

It should not be a folder-name convention pretending to be a data model.

### 4.2 Original Artifact Store

The original store should preserve exact source bytes outside the public Git repository by default.

The preferred initial physical implementation is a local filesystem backend behind an ADS-owned storage port.

### 4.3 Derived Artifact / Index Layer

Derived outputs are not source authority. They should be reproducible products of a processing activity over a particular exact artifact.

Examples include:

```text
parsed text
page renderings
layout structure
OCR output when required
tables
figures
equation representations
section trees
chunks
summaries
embeddings
lexical indexes
vector indexes
```

If a parser, embedding model, or chunking strategy changes, those outputs may be regenerated without changing the identity of the preserved source artifact.

---

## 5. Identity model

A single hash is not sufficient for the whole source model.

### 5.1 Source

`Source` is the logical intellectual/document identity.

Examples:

```text
Goodfellow et al. "Generative Adversarial Nets"
Peter Bloem "Unraveling Principal Component Analysis"
VU Amsterdam Machine Learning lecture: Trees and Ensembles
scikit-learn feature-selection documentation
RFC 8493 BagIt specification
```

A Source may have stable metadata such as title, authors/organization, canonical locator, DOI/ISBN/standard identifier, source type, and publication/version context.

### 5.2 SourceArtifact

`SourceArtifact` is one exact byte representation.

Examples:

```text
publisher PDF
annotated PDF
cropped PDF
HTML snapshot
EPUB
local scan
```

Each artifact should carry a cryptographic digest. SHA-256 is the preferred V1 integrity/content-addressing digest because it is widely supported, deterministic, and already used elsewhere in the repository's evidence-preservation practice.

The digest identifies exact bytes, not semantic equivalence.

### 5.3 SourceVersion / edition relation

Versions/editions should be explicit relationships among logical sources/artifacts rather than destructive overwrites.

Possible relationships include conceptually:

```text
VERSION_OF
SUPERSEDES_SOURCE_VERSION
ALTERNATE_FORMAT_OF
ANNOTATED_VARIANT_OF
DERIVED_FROM
```

The exact production vocabulary remains open for Specification 023.

### 5.4 SourceCollection

Collections provide context without owning the source identity.

Examples:

```text
VU Amsterdam Machine Learning course
Econometrics course
Missing-data pressure-test source bundle
ISO standards used by the project
Current six-slice methodological source packet
```

One source may belong to multiple collections.

### 5.5 SourceMembership

Collection membership should support role and certainty.

For course intake, useful candidate semantics include:

```text
CONFIRMED
LIKELY
POSSIBLE
UNVERIFIED
```

and roles such as:

```text
LECTURE
REQUIRED_READING
SUPPLEMENTARY_READING
BOOK
PAPER
EXERCISE
SOLUTION
NOTES
REFERENCE
UNKNOWN
```

These are candidate concepts, not frozen enums.

---

## 6. Content-addressed storage without making the digest the domain identity

The original artifact store should be content-addressed operationally.

Conceptually:

```text
sha256:<digest>
    -> exact bytes
```

A filesystem implementation may shard objects by digest prefix to avoid large flat directories.

The domain should not expose that physical layout as semantic identity.

This gives several benefits:

```text
exact duplicate elimination
integrity verification
safe immutable originals
stable references across filename changes
portable storage backends
```

It does not solve near-duplicate or semantically equivalent documents automatically.

Two PDFs with different annotations or metadata may produce different hashes while representing closely related content. The registry should preserve both artifacts and record their relationship after review.

---

## 7. Ingestion events preserve how the artifact entered ADS

Artifact identity alone does not preserve intake history.

The source subsystem should retain an `IngestionEvent` or equivalent event record containing information such as:

```text
ingestion event identity
timestamp
intake channel
observed filename
observed locator
collection/context supplied by the user
association uncertainty
artifact digest
operator / process identity where relevant
result: new artifact / exact duplicate / rejected / unresolved
```

This allows the same exact artifact to be encountered multiple times without creating duplicate source objects while preserving the fact that it was supplied in different contexts.

Example:

```text
52.Trees.annotated.pdf
52.Trees.annotated(1).pdf
```

may prove to be the same exact artifact. In that case there should be one artifact identity and two observed intake names/events, not two independently authoritative files.

---

## 8. Original filenames and local paths are metadata, not identity

The source model must not rely on:

```text
C:\some\folder\lecture.pdf
```

or on one cloud-sync path.

Original filenames can be preserved as intake metadata because they are useful to humans.

Local paths should generally be adapter/configuration state rather than portable source identity and should not be committed to the public repository.

Canonical external locators such as DOI, official URL, ISBN, or standards identifiers should be stored separately from local artifact locations.

---

## 9. SourceStore port

The application should own a storage interface conceptually similar to:

```text
SourceArtifactStore
    put(bytes) -> digest / artifact handle
    get(artifact_identity) -> bytes/stream
    exists(artifact_identity)
    verify(artifact_identity)
    delete(...) only under explicit retention policy
```

The exact interface is deferred to Specification 023.

### Initial implementation

Preferred:

```text
local filesystem content-addressed store
```

### Future implementations

Possible later adapters:

```text
S3-compatible object storage
Azure Blob Storage
Google Cloud Storage
MinIO
managed institutional storage
```

The existence of these future options is a reason to define the port, not a reason to introduce cloud operational complexity now.

---

## 10. Local-first does not mean single-copy

A local source vault on one disk is not a professional preservation strategy by itself.

The initial operational target should be:

```text
working local source store
    +
independent recoverable backup copy
```

A synchronized cloud folder may help, but synchronization alone should not be assumed to equal backup because deletions/corruption can propagate. Recovery/version-history behavior should be understood and tested for whichever backup mechanism is chosen.

A later production deployment may use versioned object storage and independent backup/replication.

The exact backup provider is not selected here.

---

## 11. Git repository boundary

The public Git repository should own:

```text
source-domain code
storage ports/adapters
schemas
migrations
policies
public-safe deterministic registry/interchange fixtures
source-processing pipeline definitions
integrity/recovery tests
knowledge-to-source provenance semantics
architecture/history documentation
```

It should not own by default:

```text
copyrighted books
restricted lecture materials
private papers obtained under access restrictions
large binary source archives
machine-specific vault paths
cloud credentials
private access tokens
```

Some public-domain or permissively licensed source artifacts might later be committed intentionally when justified, but that is an explicit exception rather than the default storage model.

Git LFS therefore does not become the default source-vault architecture. It can solve large-file transport for a Git repository, but it does not by itself provide the source identity, rights, lineage, collection, derived-artifact, or evidence-link semantics ADS requires.

---

## 12. Rights, licensing, privacy, and redistribution

The source registry should preserve at least enough information to avoid accidental redistribution.

Useful conceptual dimensions include:

```text
access class
    PUBLIC
    PRIVATE_USER_SUPPLIED
    ORGANIZATION_INTERNAL
    UNKNOWN

redistribution status
    PERMITTED
    RESTRICTED
    UNKNOWN

license / rights statement
    explicit license identifier or human-readable note where known

canonical public locator
    if one exists
```

These are candidate semantics rather than frozen production enums.

Hash values and metadata do not grant redistribution rights.

The system should support a source being fully usable inside a private local ADS installation while remaining ineligible for publication in the public repository or exported source bundles.

---

## 13. Derived representation lineage

Every consequential derived representation should be attributable to:

```text
exact source artifact
processing activity / pipeline identity
software version(s)
configuration
creation timestamp
output digest where useful
```

This enables reproducibility and later reprocessing.

Conceptually:

```text
SourceArtifact
    -> ExtractionActivity(parser=vX, config=Y)
        -> DerivedArtifact(text/layout/pages/...)
```

The model resembles the entity/activity/agent separation used by W3C PROV. ADS does not need to adopt RDF or the full PROV serialization internally to benefit from the same provenance distinction.

---

## 14. Source spans and evidence links

The eventual provenance layer should support finer-grained evidence than whole-document citation where feasible.

Candidate source-location representation should be able to address:

```text
page number / page range
section or heading
character/token offsets in a derived text representation
figure/table identifier or region
paragraph/block identity
external locator fragment when the source format supports it
```

A knowledge revision should then be able to record an evidence relationship such as:

```text
SUPPORTS
DEFINES
MOTIVATES
CHALLENGES
LIMITS
CONTEXTUALIZES
IMPLEMENTS
```

The exact vocabulary remains open.

A source span is evidence location, not a copied methodological proposition. The extracted/reviewed knowledge component remains separately governed.

---

## 15. Evidence provenance should not depend on one parser

PDF extraction is imperfect. Page geometry, equations, tables, figures, and reading order can be lost or distorted.

Therefore:

```text
original artifact location
    should remain recoverable

machine-derived text span
    may supplement, not replace, original location
```

For a PDF, page number plus artifact digest provides a durable coarse anchor even if the text-extraction algorithm changes.

More precise derived spans can then be versioned against a particular extraction representation.

---

## 16. Interoperability standards to borrow from rather than copy blindly

Several established standards are relevant.

### W3C PROV

W3C PROV separates entities, activities, and agents and explicitly supports derivation, versioning, and reproducibility-oriented provenance.

ADS should reuse this conceptual discipline where it helps rather than inventing ambiguous lineage semantics.

Reference:

```text
https://www.w3.org/TR/prov-overview/
```

### BagIt, RFC 8493

BagIt defines a file-packaging format with payload manifests/checksums and is useful for reliable transfer and archival packaging.

Potential ADS role:

```text
backup/export/transfer package candidate
```

not:

```text
internal domain model
```

Reference:

```text
https://www.rfc-editor.org/rfc/rfc8493
```

### RO-Crate

RO-Crate provides a JSON-LD based packaging/metadata approach for research objects and contextual entities.

Potential ADS role:

```text
future metadata/export interoperability candidate
```

not:

```text
mandatory internal ontology
```

Reference:

```text
https://www.researchobject.org/ro-crate/specification.html
```

The project should adopt standards at boundaries where they reduce interoperability risk, not force the internal system into a standard whose scope is different from ADS.

---

## 17. ChatGPT Library and Project Sources

ChatGPT-side storage is useful during development but should have no authoritative role in ADS source identity.

### ChatGPT Library

Useful as:

```text
human convenience
cross-chat file reuse
development intake surface
```

Not suitable as:

```text
canonical ADS artifact store
source registry
backup authority
long-term evidence identifier
```

### ChatGPT Project Sources

Useful as:

```text
small active working context
current source manifest
current construction policy
small bounded source bundle under active review
```

Not suitable as the complete source universe because the platform feature is a context aid rather than ADS-owned source infrastructure and has project-file limits.

### Principle

```text
ChatGPT availability may accelerate development,
but ADS correctness and recoverability must not depend on it.
```

---

## 18. Cloud drives and connected folders

Google Drive, OneDrive, or another managed drive can be valuable as:

```text
personal archive
backup/synchronization layer
human organization layer
ChatGPT-accessible bridge
intake source
```

They should not become the semantic source registry.

An adapter may later ingest from a connected folder while preserving the external locator and copying exact bytes into the governed artifact store when policy permits.

A linked source that cannot legally or practically be copied may instead remain externally referenced, with availability and verification limitations recorded explicitly.

---

## 19. Copy, reference, or hybrid acquisition policy

Not every source must be handled identically.

The source subsystem should support at least three conceptual acquisition modes.

### PRESERVED COPY

ADS stores exact bytes in its artifact store.

Preferred for user-owned/private study material and sources where local preservation is allowed and useful.

### EXTERNAL REFERENCE

ADS stores metadata/locator but not the artifact bytes.

Useful where redistribution/copying is undesirable, where the source is an authoritative live service, or where access must remain external.

### PRESERVED SNAPSHOT + CANONICAL REFERENCE

ADS preserves the exact artifact used for reproducibility and also records the canonical external locator/version.

This is often the strongest mode for public papers, standards, documentation snapshots, and other evolving sources when rights permit.

The exact policy and enum names remain open.

---

## 20. Source authority is proposition-sensitive and independent of storage mode

A locally preserved PDF is not more authoritative merely because ADS owns a copy.

Likewise, an externally referenced official standard can be stronger evidence than a locally stored lecture deck.

The architecture therefore keeps separate:

```text
artifact preservation quality
source authority for a proposition
rights/access status
freshness sensitivity
knowledge governance state
```

No scalar "source quality" field should collapse these dimensions.

---

## 21. Proposed ingestion workflow

The long-term intake workflow should become approximately:

```text
USER / CONNECTOR / FILESYSTEM supplies source context
        ->
preflight policy and file discovery
        ->
stream bytes and compute SHA-256
        ->
verify / deduplicate exact artifact
        ->
preserve immutable original when acquisition policy permits
        ->
resolve/create logical Source
        ->
record collection membership and uncertainty
        ->
record rights/access/canonical locators
        ->
record IngestionEvent
        ->
produce source-intake report
        ->
optional derived-processing jobs
        ->
source becomes eligible for candidate knowledge extraction
```

The ingestion transaction should avoid external network/LLM work inside authoritative database writes, consistent with existing persistence design principles.

---

## 22. Educational corpus intake becomes a system acceptance test

The currently supplied VU Amsterdam Machine Learning batch is an unusually useful first real source-substrate test because it includes:

```text
lecture decks
annotated variants
book-like material
primary papers
possibly supplementary/uncertain files
different filenames that may duplicate earlier uploads
```

The first implemented source subsystem should be exercised against that real batch before the user uploads dozens of additional courses.

The acceptance exercise should verify at least:

```text
exact duplicate detection
artifact integrity verification
course collection registration
uncertain membership preservation
multiple source types
original filename preservation
rights/access defaults
stable registry export
retrieval of exact original bytes
backup/recovery of the corpus
no source binaries accidentally entering Git
```

This turns source intake into architecture evidence rather than clerical upload work.

---

## 23. Proposed V1 implementation sequence

```text
SU-0  conceptual source architecture                       THIS MEMO
SU-1  freeze minimal Source Registry + SourceStore contract NEXT
SU-2  implement local content-addressed artifact store
SU-3  implement relational source registry + deterministic interchange/export
SU-4  implement integrity verification and bounded derived-artifact lineage
SU-5  ingest VU Machine Learning batch as first real corpus
SU-6  execute backup/recovery and duplicate/variant pressure tests
SU-7  connect source spans/evidence links to candidate knowledge construction
SU-8  resume six-slice knowledge pressure test with governed source bundles
```

The source substrate is therefore a prerequisite to bulk source intake, not a detour from the methodological knowledge universe.

---

## 24. Explicit non-decisions

This memo does not yet select:

```text
exact local vault root path
final database table/schema names
final source/access/right enums
final relation vocabulary
final evidence-link vocabulary
final backup provider
final cloud object-store provider
final parser/OCR stack
final document/chunk representation
final embedding/index strategy
final metadata interoperability format
full W3C PROV adoption
BagIt as mandatory internal packaging
RO-Crate as mandatory internal metadata
Git LFS for source storage
automatic source-quality scoring
automatic knowledge acceptance from sources
```

Those choices should be frozen only when the minimal V1 source contract or implementation pressure requires them.

---

## 25. Architectural conclusion

The source substrate should be designed as an ADS-owned evidence system rather than a folder of attachments.

The core boundary is:

```text
logical Source identity
        !=
exact SourceArtifact bytes
        !=
collection membership
        !=
derived representation
        !=
methodological knowledge
        !=
knowledge acceptance
```

The preferred current direction is:

```text
ADS relational Source Registry
        +
ADS-owned SourceArtifactStore port
        +
local content-addressed immutable original store first
        +
independent recoverable backup
        +
rebuildable derived artifacts/indexes
        +
source-span/evidence lineage into governed knowledge
```

ChatGPT Library, Project Sources, cloud drives, Git, and future object stores may all participate as development, intake, backup, interchange, or storage mechanisms. None should become source authority merely because it is convenient today.
