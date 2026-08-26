# Specification 023: V1 Source Universe Substrate

**Date:** 2026-08-25  
**Status:** Frozen prospective V1 implementation contract  
**Scope:** Minimal governed source registry, exact source-artifact preservation, deterministic registry export, integrity verification, bounded derived-artifact lineage, and first real-corpus recovery validation  
**Authority:** Frozen implementation contract for the first source-substrate vertical slice. Subordinate to Foundation 021 and existing V1 persistence/interchange decisions. Does not define final source ontology, final evidence-link vocabulary, final backup provider, final parser stack, or accepted methodological knowledge.  
**Design session:** 06  
**ChatGPT project:** Autonomous Data Science System  
**Session title:** 06 - Methodological Knowledge Universe Construction

## 1. Purpose

Foundation 021 establishes the source-universe architecture conceptually. This specification freezes the smallest implementation that can demonstrate the architecture against the real VU Amsterdam Machine Learning source batch before further bulk source intake.

The target is not a complete document-management platform.

The target is:

```text
exact source bytes
    +
source identity / collection / rights metadata
    +
integrity and duplicate guarantees
    +
deterministic portable registry evidence
    +
provider-neutral artifact storage
    +
recovery evidence
```

with enough lineage to support later source extraction and knowledge provenance.

---

## 2. Frozen system boundary

The first executable source path is:

```text
filesystem source input
    -> preflight
    -> stage + SHA-256 + byte count
    -> content-addressed original-artifact store
    -> relational Source Registry transaction
    -> deterministic registry export
    -> integrity audit
    -> backup package
    -> restore into clean target
    -> integrity audit after restore
```

No LLM call is required or permitted for correctness of this path.

LLM-assisted classification/extraction may be added later behind separate candidate-generation boundaries.

---

## 3. Frozen domain distinctions

V1.0 implements the following minimum identities.

### 3.1 SourceRecord

Logical source identity.

Required fields:

```text
source_id                 UUID
stable_key                bounded unique stable key
title                     non-empty text
source_type               bounded enum
canonical_locator         nullable text
external_identifier_type  nullable bounded enum
external_identifier_value nullable text
access_class               bounded enum
redistribution_status     bounded enum
rights_note                nullable text
metadata_visibility        bounded enum
created_at                 timestamp
updated_at                 timestamp
```

Frozen `source_type` values for V1.0:

```text
LECTURE_MATERIAL
BOOK
PAPER
STANDARD
SOFTWARE_DOCUMENTATION
WEB_DOCUMENT
USER_NOTE
DATASET_DOCUMENTATION
OTHER
```

Frozen `external_identifier_type` values:

```text
DOI
ISBN
URL
STANDARD_ID
OTHER
```

A canonical URL may be present directly through `canonical_locator`; `URL` remains available for externally identified records where the identifier itself is treated as the explicit external identifier.

Frozen `access_class` values:

```text
PUBLIC
PRIVATE_USER_SUPPLIED
ORGANIZATION_INTERNAL
UNKNOWN
```

Frozen `redistribution_status` values:

```text
PERMITTED
RESTRICTED
UNKNOWN
```

Frozen `metadata_visibility` values:

```text
PUBLIC_SAFE
PRIVATE
```

These values are intentionally small and may be revised prospectively after first-corpus pressure testing.

### 3.2 SourceArtifact

Exact byte identity.

Required fields:

```text
artifact_id          UUID
source_id            UUID FK -> SourceRecord
sha256               lowercase 64-hex, globally unique
byte_size            non-negative integer
media_type           non-empty text
artifact_state       bounded enum
first_seen_at         timestamp
last_verified_at     nullable timestamp
```

Frozen `artifact_state` values:

```text
PRESERVED
MISSING
CORRUPT
```

Normal ingestion creates `PRESERVED` only after the exact bytes have been finalized in the artifact store.

### 3.3 SourceCollection

Required fields:

```text
collection_id       UUID
stable_key          bounded unique stable key
title               non-empty text
collection_type     bounded enum
canonical_locator   nullable text
metadata_json       JSON object
created_at           timestamp
updated_at           timestamp
```

Frozen `collection_type` values:

```text
COURSE
READING_LIST
SOURCE_BUNDLE
STANDARD_FAMILY
PROJECT_EVIDENCE_SET
OTHER
```

### 3.4 SourceCollectionMembership

Required fields:

```text
collection_id       UUID FK
source_id           UUID FK
membership_role     bounded enum
association_status  bounded enum
note                 nullable text
```

Uniqueness:

```text
(collection_id, source_id, membership_role)
```

Frozen `membership_role` values:

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

Frozen `association_status` values:

```text
CONFIRMED
LIKELY
POSSIBLE
UNVERIFIED
```

This explicit uncertainty is mandatory. Ingestion must not coerce `POSSIBLE` or `UNVERIFIED` to `CONFIRMED` automatically.

### 3.5 SourceLocator

Required fields:

```text
locator_id       UUID
source_id        UUID FK
artifact_id      nullable UUID FK
locator_type     bounded enum
locator          non-empty text
is_canonical     boolean
visibility       bounded enum
created_at       timestamp
```

Frozen `locator_type` values:

```text
CANONICAL_URL
DOI
ISBN
STANDARD_ID
OBSERVED_PATH
OBSERVED_URL
OTHER
```

Frozen `visibility` values:

```text
PUBLIC_SAFE
PRIVATE
```

`OBSERVED_PATH` must default to `PRIVATE` and must never appear in public-safe export.

### 3.6 SourceIngestionEvent

Required fields:

```text
ingestion_event_id  UUID
source_id           UUID FK
artifact_id         nullable UUID FK
collection_id       nullable UUID FK
occurred_at          timestamp
intake_channel       bounded enum
observed_name        nullable text
observed_locator     nullable text
result               bounded enum
note                 nullable text
```

Frozen `intake_channel` values:

```text
FILESYSTEM
CHATGPT_UPLOAD
WEB_DOWNLOAD
CONNECTOR
MANUAL_REFERENCE
OTHER
```

Frozen `result` values:

```text
NEW_ARTIFACT
EXACT_DUPLICATE
EXTERNAL_REFERENCE_ONLY
REJECTED
UNRESOLVED
```

The event preserves intake provenance; it does not create a new artifact when exact bytes already exist.

### 3.7 DerivedSourceArtifact

The first implementation supports bounded lineage only.

Required fields:

```text
derived_artifact_id       UUID
parent_source_artifact_id UUID FK
kind                      bounded enum
pipeline_key              non-empty stable key
pipeline_version          non-empty text
configuration_sha256      lowercase 64-hex
output_sha256             lowercase 64-hex
byte_size                 non-negative integer
media_type                non-empty text
storage_key               non-empty internal text
created_at                timestamp
```

Frozen `kind` values:

```text
EXTRACTED_TEXT
PAGE_RENDER_SET
DOCUMENT_STRUCTURE
OTHER
```

This is lineage infrastructure only. Specification 023 does not require implementing a production PDF extraction pipeline.

---

## 4. Stable identity and UUID policy

Application/domain identities use UUID values consistent with existing V1 interchange conventions.

UUIDv7 remains the preferred generation strategy where the existing application identity utility supports it, but semantic meaning must not depend on UUID version.

`stable_key` is the human-facing stable lookup identity for SourceRecord and SourceCollection.

Stable keys must be unique, lowercase, and bounded to:

```text
[a-z0-9][a-z0-9._/-]{0,126}[a-z0-9]
```

or a one-character `[a-z0-9]` value.

Stable keys must never be derived as the sole identity from a filename.

---

## 5. Exact-artifact digest contract

V1 uses SHA-256 for exact artifact content identity and integrity.

Rules:

```text
algorithm       SHA-256
digest encoding lowercase hexadecimal
byte input      exact file bytes, unmodified
```

No newline normalization, PDF metadata normalization, decompression, parsing, or semantic canonicalization occurs before the digest.

Therefore:

```text
same SHA-256 -> same exact byte stream for ADS purposes
```

and:

```text
different SHA-256 -> distinct SourceArtifact
```

No semantic duplicate claim follows automatically from either result.

---

## 6. Artifact-store port

V1 introduces an ADS-owned application/storage boundary conceptually named:

```text
SourceArtifactStore
```

Required behavior:

```text
stage_from_path(path) -> staged artifact metadata
commit(staged) -> stored artifact handle
open(sha256) -> readable byte stream
exists(sha256) -> bool
verify(sha256, expected_size) -> integrity result
iter_objects() -> iterable object metadata for audit
```

The implementation may choose equivalent method names while preserving these semantics.

The domain/application layer must not require knowledge of the physical storage path layout.

---

## 7. Frozen local content-addressed backend behavior

The initial backend is a local filesystem store rooted at a user/configuration supplied location outside the public Git repository.

The root must not be hard-coded into domain state.

Frozen object layout:

```text
<root>/objects/sha256/<first-two-hex>/<remaining-62-hex>
```

Example:

```text
sha256 = 6a489b8b...
path   = <root>/objects/sha256/6a/489b8b...
```

The full digest remains recoverable from the directory + filename.

The backend must also reserve:

```text
<root>/staging/
<root>/derived/
```

No metadata database is stored inside the object path itself as source authority.

---

## 8. Atomic artifact ingestion semantics

For filesystem ingestion, the required sequence is:

```text
1. open source file read-only
2. create unique staging file under <root>/staging
3. stream-copy bytes while computing SHA-256 and byte count
4. flush staging output
5. if final object already exists:
       verify existing final object digest + size
       delete staging copy
       return EXACT_DUPLICATE artifact-store result
6. otherwise atomically rename/move staging file to final content-addressed path
7. verify final object digest + size
8. return durable artifact-store result
```

The implementation must not modify the source input file.

A partially written staging object must never be visible as a committed artifact.

A failed finalization must not create a `PRESERVED` registry row.

---

## 9. Registry transaction boundary

External filesystem copying and hashing must not occur inside the authoritative database transaction.

Required sequence:

```text
artifact-store stage/finalize
    ->
short database transaction
        resolve/create SourceRecord
        resolve/create SourceArtifact
        create/update collection membership
        create locators
        create SourceIngestionEvent
    ->
commit
```

If artifact storage succeeds but the registry transaction fails, the content-addressed object may remain as an orphan.

This is acceptable only because V1 requires an orphan-audit operation that can report:

```text
stored object with no registered SourceArtifact
registered SourceArtifact with missing object
registered SourceArtifact with digest/size mismatch
```

The system must never silently fabricate registry success from an orphan object.

---

## 10. Exact duplicate semantics

If an incoming file digest matches an existing `SourceArtifact.sha256`:

```text
no new SourceArtifact row
no second binary copy required
new SourceIngestionEvent allowed and required for the new encounter
additional SourceLocator / observed filename allowed
additional collection membership allowed
```

If the caller proposes a different logical Source for the same exact artifact, the application must not silently duplicate the artifact or silently merge source identities.

V1 behavior:

```text
return explicit logical-source conflict requiring review
```

unless the caller explicitly attaches the existing artifact to the already-resolved Source identity.

This conservative rule prevents accidental semantic merges in the first implementation.

---

## 11. Logical source creation policy

V1 does not use LLM inference to decide whether two artifacts represent the same logical Source.

For first-corpus ingestion, SourceRecord creation is driven by a reviewable intake manifest or explicit CLI/application arguments.

The manifest may create a provisional one-source-per-logical-item mapping.

Later merge/same-work/version workflows are separate governed operations and are not part of normal ingestion.

---

## 12. Rights/access defaults

For user-supplied local educational material, default values are:

```text
access_class           PRIVATE_USER_SUPPLIED
redistribution_status UNKNOWN
metadata_visibility   PUBLIC_SAFE only when explicitly marked safe;
                      otherwise PRIVATE
```

The system must not infer redistribution permission from:

```text
file possession
public course affiliation
existence of a public URL
file extension
source title
```

Public papers or official documentation may be registered with different values only when the intake manifest/user explicitly provides justified metadata.

---

## 13. Private path handling

Machine-local input paths are never portable source identity.

If persisted as SourceLocator:

```text
locator_type = OBSERVED_PATH
visibility   = PRIVATE
```

Public-safe export must exclude them.

Storage-root paths and internal content-addressed paths are configuration/internal adapter state and must not appear in public-safe export.

---

## 14. Deterministic private registry snapshot

V1 requires a deterministic JSON interchange document:

```text
SourceRegistrySnapshot
```

Minimum fields:

```text
format
schema_version
export_profile
sources[]
artifacts[]
collections[]
memberships[]
locators[]
ingestion_events[]
derived_artifacts[]
```

Frozen:

```text
format         ADS_SOURCE_REGISTRY
schema_version 1
export_profile PRIVATE_SNAPSHOT
```

Serialization rules:

```text
UTF-8
LF newlines
final newline
2-space indentation
object keys lexicographically sorted
Unicode emitted directly where safe
arrays sorted deterministically by stable semantic identity
```

Sorting:

```text
sources             stable_key, source_id
artifacts           sha256, artifact_id
collections         stable_key, collection_id
memberships         collection stable_key, source stable_key, membership_role
locators            source stable_key, locator_type, locator
 ingestion_events   occurred_at, ingestion_event_id
 derived_artifacts  parent artifact sha256, kind, pipeline_key, derived_artifact_id
```

The leading space before `ingestion_events` above is typographical only; the JSON key is exactly `ingestion_events`.

Private snapshot may contain private metadata but must not contain source binary bytes.

---

## 15. Deterministic public-safe catalog export

V1 also requires:

```text
export_profile PUBLIC_SAFE_CATALOG
```

This export contains only records whose `metadata_visibility = PUBLIC_SAFE` and only locator rows whose `visibility = PUBLIC_SAFE`.

It must exclude:

```text
OBSERVED_PATH locators
source-store root/internal storage keys
credentials/tokens
private notes explicitly marked non-exportable
source binary bytes
private derived-artifact storage keys
```

Artifact SHA-256, byte size, media type, logical source identity, public-safe collection membership, and public canonical locators may be included when the parent source metadata is public-safe.

The public-safe catalog is suitable for committing to Git when project policy chooses to do so.

The operational Source Registry remains authoritative runtime state.

---

## 16. Snapshot import safety

V1 `PRIVATE_SNAPSHOT` import is a trusted restore/bootstrap path, analogous to accepted snapshot restore in the reusable-knowledge interchange boundary.

Normal interactive source authoring/ingestion must not use private snapshot import as a shortcut around intake policy.

Import rules:

```text
same source_id + same semantic record
    -> idempotent

same source_id + conflicting semantic record
    -> hard conflict

same stable_key + different source_id
    -> hard identity conflict

same artifact sha256 + same byte_size
    -> same exact artifact identity candidate

same artifact sha256 + different byte_size
    -> hard integrity conflict

missing referenced source/collection/artifact
    -> reject snapshot
```

Snapshot import does not supply artifact bytes by itself. Restore must separately restore/verify the object payload.

---

## 17. Integrity audit

V1 requires an audit command/service that compares registry and artifact store.

For every registered `PRESERVED` artifact:

```text
object exists
byte size matches
SHA-256 matches
```

The audit must also detect content-addressed objects with no registered SourceArtifact.

Frozen status classes:

```text
OK
MISSING_OBJECT
SIZE_MISMATCH
DIGEST_MISMATCH
ORPHAN_OBJECT
```

The audit must return non-zero/failure when any status other than `OK` is present, while preserving the complete report.

A successful audit may update `last_verified_at` for registered artifacts in a separate short transaction.

---

## 18. Backup package

V1 requires a provider-neutral filesystem backup/export package that can be copied to an independent destination.

Frozen logical structure:

```text
backup-root/
    backup_manifest.json
    registry/
        source_registry_snapshot.json
    objects/
        sha256/...
```

`backup_manifest.json` must include:

```text
format = ADS_SOURCE_BACKUP
schema_version = 1
created_at
registry_snapshot_sha256
object_count
object_total_bytes
objects[] with sha256 + byte_size
```

The object payload must preserve the same content-addressed layout.

The manifest itself must be deterministic except for `created_at` and any explicit backup identity field.

V1 does not require BagIt compliance, but the checksum-manifest approach is intentionally compatible with later packaging interoperability.

---

## 19. Backup creation semantics

Backup creation must:

```text
1. require a clean integrity audit first
2. export deterministic PRIVATE_SNAPSHOT
3. copy exact object bytes to the backup target
4. hash/verify every copied object at destination
5. write backup_manifest.json only after payload verification
6. hash the registry snapshot and record its digest in the manifest
7. perform final backup verification
```

If any step fails, the backup must not be reported as complete.

The backup destination may be a local second drive/folder for the first implementation. Cloud-provider integration is out of scope.

---

## 20. Restore semantics

Restore must support a clean empty target registry and artifact store.

Required sequence:

```text
1. validate backup_manifest structure
2. verify registry snapshot digest
3. verify every backup object digest + size
4. restore object payload to clean SourceArtifactStore
5. import PRIVATE_SNAPSHOT into clean registry
6. run full restored integrity audit
```

A restore is successful only when the final audit contains only `OK` for all registered preserved artifacts and no unexpected orphan objects.

Restore must not overwrite an existing non-empty target by default.

---

## 21. Derived-artifact storage

Derived artifacts are stored under the source-store root but outside `objects/`:

```text
<root>/derived/<parent-sha256>/<derived-kind>/<output-sha256>
```

This physical path is implementation detail and not public provenance identity.

A derived artifact must be regenerated rather than mutated in place if pipeline version/configuration changes.

The `configuration_sha256` is computed over deterministic UTF-8 JSON of the pipeline configuration with sorted keys and compact separators.

---

## 22. No automatic parsing requirement in this specification

Specification 023 validates the source/evidence substrate, not document-understanding quality.

At least one synthetic or fixture `DerivedSourceArtifact` must be created in tests to prove lineage and rebuildable storage mechanics.

Real PDF extraction is deferred to a later specification/pressure test.

---

## 23. Initial VU Machine Learning collection contract

The first real corpus collection has stable key:

```text
vu-amsterdam-machine-learning
```

Frozen collection metadata:

```text
title            Machine Learning
collection_type  COURSE
canonical_locator https://mlvu.github.io/
institution       Vrije Universiteit Amsterdam
```

`institution` is stored inside `metadata_json` for V1.

The currently observed ChatGPT intake snapshot contains 20 files and is preserved in:

```text
docs/source_universe/intake_snapshots/001_vu_machine_learning_chat_intake.md
```

That snapshot is historical diagnostic evidence, not the source registry.

---

## 24. First-corpus source manifest

Before ingestion, the implementation must use a human-reviewable manifest that maps each local file to:

```text
source stable_key
title
source_type
collection stable_key
membership_role
association_status
access_class
redistribution_status
metadata_visibility
optional canonical locator / external identifier
optional note
```

The manifest must not contain binary bytes.

The exact authoring syntax may be JSON under the existing deterministic-validation preference.

For files whose course association remains uncertain, the manifest must preserve `POSSIBLE` or `UNVERIFIED` rather than forcing `CONFIRMED`.

---

## 25. Chat-intake comparison report

The first-corpus ingestion must produce a comparison report against Intake Snapshot 001 when names/digests can be matched.

Required classifications:

```text
MATCH
DIFFERENT_ARTIFACT
MISSING_LOCAL_SOURCE
ADDITIONAL_LOCAL_SOURCE
```

The comparison is diagnostic only and does not make the ChatGPT-observed bytes authoritative.

---

## 26. Real duplicate gate

Intake Snapshot 001 already records fourteen exact-byte duplicate pairs across earlier and `(1)`-suffixed chat uploads.

The implemented source store must demonstrate on an equivalent local test that ingesting the same exact file under two names produces:

```text
1 SourceArtifact binary object
1 SourceArtifact registry row
2 SourceIngestionEvent rows
both observed names preserved
no second binary copy
```

If course/Source identity is the same, the second event result must be:

```text
EXACT_DUPLICATE
```

---

## 27. Variant gate

The first corpus includes two byte-distinct artifacts that appear related to Peter Bloem's PCA book material:

```text
book-v1.2.0-cropped.pdf
unraveling-pca.pdf
```

The implementation must preserve them as two distinct SourceArtifact records because their SHA-256 values differ.

The substrate must not automatically merge them semantically.

Any later relation such as alternate format/version/variant must require explicit review outside normal exact-dedup ingestion.

---

## 28. Git-exclusion gate

The local source-store root must be outside the Git working tree for the first production-like acceptance run.

Tests must also verify that configured source-store paths are not accidentally added by repository fixture setup.

No current source PDF/book from the VU Machine Learning batch is permitted to be committed by Specification 023 implementation.

The repository may later contain public-safe source manifests/catalog exports only.

---

## 29. Cross-platform requirement

The minimal source substrate must pass on:

```text
Ubuntu
Windows
```

for:

```text
path handling
atomic finalization behavior
hashing
registry persistence
snapshot serialization
backup/restore
integrity audit
```

Platform-specific path strings must not leak into public-safe deterministic output.

---

## 30. Database compatibility requirement

The source registry implementation must work with the accepted V1 persistence architecture.

Required first acceptance:

```text
SQLite
```

Schema design must not knowingly preclude PostgreSQL support through the existing SQLAlchemy Core/Alembic architecture, but a live PostgreSQL source-substrate gate is not required before the first local corpus intake unless implementation evidence exposes backend-specific behavior.

---

## 31. Migration requirement

Source Registry persistence changes require an Alembic migration consistent with D-029.

The migration must not modify or reinterpret accepted reusable-knowledge rows.

Source tables must be a separate persistence concern from reusable knowledge tables even when provenance later links the two.

---

## 32. Application-service boundary

The first implementation should expose application operations equivalent to:

```text
create_source
create_collection
ingest_file
register_external_reference
add_collection_membership
list_sources
get_source
open_source_artifact
verify_source_artifact
audit_source_store
export_source_registry
create_source_backup
restore_source_backup
```

Exact Python class/function naming is not frozen.

No API/UI endpoint is required yet.

---

## 33. Failure semantics

The source subsystem must fail closed on integrity ambiguity.

Examples:

```text
existing content-addressed object does not hash to its path digest
    -> hard integrity failure

same artifact digest with conflicting byte size
    -> hard integrity failure

registry says PRESERVED but object missing
    -> audit failure

public-safe export encounters private locator
    -> exclude it deterministically, do not redact ambiguously

snapshot references missing identity
    -> reject import

backup payload verification fails
    -> backup incomplete, restore prohibited
```

No automatic repair of corrupted original bytes is allowed.

---

## 34. Security and privacy minimum

V1 must not persist secrets in source metadata.

URLs containing obvious credential-bearing query parameters or embedded credentials should be rejected from `PUBLIC_SAFE` locators and should not be logged verbatim in public reports.

The source store must open originals read-only through normal application access.

No source binary should be served to external clients because Specification 023 does not define a network API.

---

## 35. Provider/model boundary

No OpenAI or other model/provider call is required for:

```text
ingestion
deduplication
integrity verification
registry export/import
backup/restore
first-corpus preservation
```

This entire specification is provider-free.

Any later LLM-assisted source classification or extraction must operate on candidate metadata/derived representations and must not become a source-integrity dependency.

---

## 36. Frozen executable gates

The provider-free implementation must demonstrate:

```text
SU-G01  schema/migration creates source registry cleanly
SU-G02  source + collection identities round-trip through repository layer
SU-G03  ingest preserves exact bytes and SHA-256/size
SU-G04  duplicate ingest stores one binary and one artifact row
SU-G05  duplicate ingest preserves multiple ingestion events/names
SU-G06  byte-distinct variants remain distinct artifacts
SU-G07  collection membership preserves POSSIBLE/UNVERIFIED exactly
SU-G08  private paths never appear in PUBLIC_SAFE_CATALOG
SU-G09  deterministic PRIVATE_SNAPSHOT is byte-stable for same semantic state
SU-G10  deterministic PUBLIC_SAFE_CATALOG is byte-stable for same public-safe state
SU-G11  store audit detects missing/corrupt/orphan objects
SU-G12  clean store audit passes
SU-G13  backup refuses dirty source store
SU-G14  backup verifies copied objects + registry snapshot
SU-G15  restore into clean target reproduces registry semantic state
SU-G16  restored artifact bytes match original digests
SU-G17  restored full integrity audit passes
SU-G18  bounded DerivedSourceArtifact lineage round-trips
SU-G19  current VU ML manifest can ingest without binary Git changes
SU-G20  current VU ML intake comparison report preserves all mismatch classes
SU-G21  Windows implementation test matrix passes
SU-G22  Ubuntu implementation test matrix passes
SU-G23  inherited current-routing/checkpoint/knowledge-interchange tests remain green
```

No gate may be waived after seeing the first-corpus result without a new prospective specification revision.

---

## 37. First-corpus advancement outcomes

After SU-G01 through SU-G23 pass, the real VU Machine Learning intake is classified as one of:

```text
SOURCE_SUBSTRATE_ACCEPTED
SOURCE_SUBSTRATE_NEEDS_REVISION
SOURCE_SUBSTRATE_FAILED
```

### SOURCE_SUBSTRATE_ACCEPTED

Requires:

```text
all hard gates pass
all locally available intended files ingested or explicitly accounted for
no unexplained integrity mismatch
backup and clean restore pass
no source binary committed to Git
no uncertainty silently strengthened
```

### SOURCE_SUBSTRATE_NEEDS_REVISION

Used when integrity is preserved but real-corpus pressure exposes a representation/ergonomics deficiency that should be revised before broad corpus intake.

Examples:

```text
collection membership model insufficient
source/artifact distinction insufficient
rights metadata insufficient
variant handling unclear
portable export missing necessary metadata
```

### SOURCE_SUBSTRATE_FAILED

Used for integrity, recoverability, or authority-boundary failures.

Examples:

```text
bytes lost/corrupted
backup cannot restore
exact duplicates produce inconsistent artifacts
private paths leak into public-safe export
restricted binaries enter Git
registry cannot reconstruct artifact identity
```

---

## 38. Promotion boundary after acceptance

If `SOURCE_SUBSTRATE_ACCEPTED` is achieved:

```text
D-015 may be superseded in scope
```

with a new explicit decision stating that external source artifacts are preserved in the governed private ADS SourceArtifactStore/Registry rather than copied into Git or left dependent on chat attachments.

Acceptance does not promote any methodological knowledge from the corpus.

The next stage is source-span/evidence integration and the six-slice knowledge pressure test.

---

## 39. Explicit non-goals

Specification 023 does not select or implement:

```text
full provenance ontology
full citation manager
final evidence-link vocabulary
final source semantic duplicate/merge workflow
complete rights/licensing ontology
PDF text extraction quality
OCR model
layout parser
embedding model
vector database
website crawling
remote source refresh scheduler
cloud object storage
cloud backup provider
multi-user permissions
network API
source authoring UI
automatic source authority scoring
automatic source classification by LLM
automatic knowledge extraction/acceptance
```

---

## 40. Frozen continuation

Implementation begins only from this frozen contract.

The next sequence is:

```text
provider-free implementation
    ->
SU-G01..SU-G23 cross-platform validation
    ->
first real VU Machine Learning local-corpus intake
    ->
backup + clean restore
    ->
result checkpoint
    ->
only then additional course intake
```

The user should not need to upload the remaining educational corpus into ChatGPT as a preservation strategy.
