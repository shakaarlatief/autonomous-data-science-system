# Foundation 022: Source Universe, Artifact Integrity, and Evidence Provenance Architecture

**Date:** 2026-08-25  
**Status:** Accepted conceptual foundation for the source/evidence substrate  
**Authority:** Current architectural foundation for source identity, original-artifact preservation, derived-source lineage, and evidence provenance. It is subordinate to current project-wide principles and does not freeze the final storage provider, complete source ontology, parser stack, or knowledge-evidence vocabulary.  
**Origin:** Research 034 and the methodological knowledge-universe construction stage.  
**Numbering note:** This foundation is the canonical renumbering of the source-universe foundation originally drafted as Foundation 021. Foundation 021 was already occupied by the professional product/interface foundation. The renumbering is administrative only and does not change the accepted source architecture.

## 1. Purpose

A serious methodological knowledge universe requires a durable evidence substrate that preserves what knowledge came from and allows exact source artifacts to be recovered, verified, reprocessed, and cited later.

The Source Universe is therefore a first-class ADS subsystem rather than an informal folder of PDFs or a ChatGPT attachment convention.

---

## 2. Source Universe and Methodological Knowledge Universe are separate

The project adopts:

```text
SOURCE UNIVERSE
    source identities
    exact source artifacts
    versions / variants
    collections
    locators
    rights / access context
    ingestion provenance
    derived processing lineage

        !=

METHODOLOGICAL KNOWLEDGE UNIVERSE
    governed reusable methodological reasoning
    questions
    evidence requirements
    assumptions
    diagnostics
    alternatives
    failure modes
    claim constraints
    relations
    conditional guidance
```

A source artifact is evidence. It does not become accepted reusable methodological knowledge merely because ADS possesses or parses it.

Conversely, reusable methodological knowledge should be able to retain fine-grained provenance to the evidence supporting it.

---

## 3. Logical source identity is separate from exact artifact identity

ADS distinguishes at least:

```text
SourceRecord
    logical intellectual/source identity

SourceArtifact
    exact byte stream for one concrete representation
```

Examples:

```text
same PDF bytes under two filenames
    -> one SourceArtifact
    -> multiple encounter/name provenance records

same book/work represented by two byte-distinct PDFs
    -> distinct SourceArtifact values
    -> possible reviewed relationship at the logical Source level
```

Filename, local path, and folder membership are observations, not authoritative artifact identity.

Exact artifact identity is based on a cryptographic content digest over unmodified bytes.

---

## 4. Collections preserve context without forcing certainty

Courses, reading lists, evidence bundles, standards families, and similar groupings are represented as source collections rather than physical folders becoming semantic truth.

Collection membership must preserve uncertainty explicitly. A file found in a course folder may be:

```text
CONFIRMED
LIKELY
POSSIBLE
UNVERIFIED
```

or an equivalent future governed state.

Intake must not silently strengthen uncertain association merely because files are colocated.

---

## 5. Original artifacts are immutable evidence

The original exact source artifact is the authoritative preserved evidence object.

Processing may produce rebuildable derivatives such as:

```text
extracted text
page renders
document structure
tables / figures
chunks
embeddings
summaries
concept candidates
```

Those derived representations do not replace the original artifact.

If parsers or extraction methods improve later, new derived artifacts should be reproducible from the same preserved original and retain lineage to it.

---

## 6. ADS owns a storage abstraction, not one provider

The application uses an ADS-owned source-artifact storage boundary. The initial accepted backend is local content-addressed filesystem storage, but source semantics must not depend on that layout.

Conceptually:

```text
SourceArtifactStore
    put / stage
    commit
    open
    exists
    verify
    enumerate for audit
```

A future S3-compatible, Azure Blob, Google Cloud Storage, institutional, or other backend may implement the same semantic boundary if requirements justify it.

Cloud infrastructure is not adopted merely to appear more professional.

---

## 7. Content addressing and integrity

Exact artifact preservation uses SHA-256 over the exact unmodified byte stream for the accepted V1 substrate.

Consequences:

```text
same digest + verified byte size
    -> same exact byte artifact for ADS purposes

different digest
    -> distinct exact artifact
```

No semantic same-work conclusion follows automatically from either case.

The artifact store must support integrity verification and orphan/missing/corrupt detection against the Source Registry.

---

## 8. Registry authority is separate from binary storage

The Source Registry owns durable source metadata and relationships such as:

```text
logical source identity
artifact identity and digest
collection membership
association uncertainty
locators
rights / access classification
ingestion encounters
derived-artifact lineage
verification state
```

The artifact store owns exact bytes.

Neither layer silently fabricates the other. A stored orphan object is not a successful registry record, and a registry row pointing to missing/corrupt bytes is an integrity failure.

---

## 9. Rights, privacy, and redistribution are explicit

Possession of a source does not imply redistribution permission.

Public course affiliation, a public web page, or a familiar title also does not automatically imply that every associated PDF may be redistributed.

User-supplied educational material therefore begins conservatively unless reviewed otherwise:

```text
private access
unknown redistribution status
private metadata by default where needed
```

Public Git must not contain private source bytes or private machine paths merely because ADS uses those sources internally.

---

## 10. Portable public metadata and private restore state are different views

The source subsystem may expose different deterministic representations for different purposes.

At minimum the accepted V1 direction distinguishes:

```text
PRIVATE_SNAPSHOT
    trusted backup / restore / migration representation

PUBLIC_SAFE_CATALOG
    safe metadata suitable for review or optional Git preservation
```

A public-safe catalog must exclude private paths, credentials, internal artifact-store locations, private notes, and source binary bytes.

---

## 11. Recovery is part of preservation

A source is not durably preserved merely because it exists on one local disk.

Acceptance of a source-storage deployment requires recoverability evidence:

```text
clean integrity audit
    -> verified independent backup
    -> clean-target restore
    -> restored registry verification
    -> restored exact-byte integrity audit
```

The initial backup implementation may use a second filesystem destination. Provider selection remains independent from the preservation semantics.

---

## 12. Evidence provenance should become fine-grained

The long-term provenance target is not merely:

```text
knowledge item -> PDF
```

It should support evidence locations such as:

```text
knowledge component / proposition revision
    -> exact SourceArtifact
    -> page / section / figure / table / span where appropriate
```

This allows ADS to explain not only what it recommends but why, and to reopen or re-evaluate knowledge when supporting evidence changes.

The final evidence-link vocabulary is intentionally not frozen here.

---

## 13. ChatGPT and external file managers are integration surfaces, not authority

ChatGPT Library, ChatGPT Project Sources, Google Drive, OneDrive, and similar systems can be useful for human organization, development access, intake, synchronization, or backup.

They do not become ADS semantic source authority simply because a file is present there.

The authoritative source model remains ADS-owned and portable across those surfaces.

---

## 14. Relationship to methodological knowledge construction

The intended sequence is:

```text
durable source corpus
    -> governed source registration
    -> derived source representations
    -> candidate methodological extraction / decomposition
    -> source-backed review
    -> governed methodological knowledge
    -> behavioral and project-level validation
```

LLMs may assist with extraction, decomposition, relation proposals, duplicate candidates, and review support. Model output is not independent evidence for its own claims and cannot silently create accepted methodological authority.

---

## 15. Accepted V1 implementation evidence

Specification 023 implemented and validated the first bounded realization of this foundation.

The first VU Amsterdam Machine Learning corpus exercise demonstrated exact-byte preservation, duplicate encounter handling, explicit association uncertainty, deterministic export, integrity audit, verified backup, clean restore, and cross-platform behavior.

Checkpoint 196 classifies that bounded implementation:

```text
SOURCE_SUBSTRATE_ACCEPTED
```

The implementation acceptance does not imply that the permanent user-controlled vault has already been deployed.

---

## 16. Reopen conditions

Revisit or extend this foundation when evidence demonstrates that the current distinctions fail for material source classes or workflows, including for example:

```text
complex source versioning / editions
multi-file compound publications
video/audio or interactive sources
remote mutable web content
licensed institutional repositories
shared multi-user source governance
fine-grained evidence-span requirements
large-scale object-store operations
source withdrawal / legal restrictions
provenance graphs that exceed the current relational model
```

Changes should preserve exact-artifact integrity and historical provenance unless an explicitly stronger replacement is justified.
