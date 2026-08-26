# Source Substrate Validation 001: VU Amsterdam Machine Learning

**Date:** 2026-08-25  
**Status:** PASS, provider-free implementation and first-corpus validation  
**Specification:** 023  
**Scope:** Exact-artifact preservation, source-registry behavior, duplicate handling, deterministic export, integrity audit, backup/restore, and first real VU Machine Learning corpus exercise  
**Authority:** Validation evidence for Specification 023. This result does not make the current ChatGPT/runtime filesystem the canonical long-term source vault, does not authorize redistribution of source binaries, and does not promote source content into accepted methodological knowledge.

## 1. Result

The bounded Specification 023 source substrate passes its provider-free implementation and first-corpus validation boundary.

Frozen advancement classification:

```text
SOURCE_SUBSTRATE_ACCEPTED
```

This classification accepts the V1 source-substrate architecture and implementation seam. It does **not** claim that the user's permanent private source vault has already been instantiated on user-controlled durable storage.

---

## 2. Exact implementation head exercised in repository CI

The provider-free implementation was committed on:

```text
v1-source-universe-substrate
9b7e42314dc1414499ec3422103e61795d9f81fe
```

The implementation includes:

```text
SourceArtifactStore port
local immutable content-addressed backend
relational Source Registry
Alembic migration 0003
reviewable intake manifest
exact duplicate / variant semantics
deterministic PRIVATE_SNAPSHOT
PUBLIC_SAFE_CATALOG filtering
integrity audit
provider-neutral backup package
clean restore
bounded DerivedSourceArtifact lineage
provider-free CLI
cross-platform CI
```

---

## 3. Cross-platform repository validation

GitHub Actions run:

```text
32860579873
V1 source universe substrate
```

completed successfully on both:

```text
ubuntu-latest   PASS
windows-latest  PASS
```

Both jobs successfully:

```text
verified provider credentials were absent
migrated a clean SQLite registry to Alembic head
ran the complete current V1 Python test suite
verified no source binary was tracked under docs/source_universe
```

The Ubuntu job recorded:

```text
124 passed
2 skipped
```

The two skips were the pre-existing PostgreSQL integration tests whose optional `ADS_TEST_POSTGRES_URL` was not configured in this workflow. They are not source-substrate test failures.

At the same implementation head, the applicable routing/checkpoint and inherited V1 retrieval/Horizon/selective-context workflows also completed successfully.

---

## 4. First real source corpus used

The first corpus was the 20-file VU Amsterdam Machine Learning batch already supplied during Design Session 06 and fingerprinted prospectively in:

```text
docs/source_universe/intake_snapshots/001_vu_machine_learning_chat_intake.md
```

The controlled intake manifest is:

```text
docs/source_universe/manifests/001_vu_machine_learning.json
```

The exact source bytes used for this validation were the uploaded artifacts exposed to the active development runtime. They were used only to exercise the source subsystem. The validation vault, database, backup, and restore target were disposable development locations outside Git.

No source PDF, private registry snapshot, private observed path, backup payload, or source-vault binary was committed to the repository.

---

## 5. Intake comparison against prospective fingerprints

Before ingestion, the controlled 20-file corpus was compared against the prospectively preserved exact-byte fingerprints.

Result:

```text
MATCH                    20
DIFFERENT_ARTIFACT         0
MISSING_LOCAL_SOURCE       0
ADDITIONAL_LOCAL_SOURCE    0
```

Therefore every selected first-corpus byte stream matched the diagnostic pre-implementation fingerprint exactly.

---

## 6. Initial exact-artifact ingestion

Initial ingestion result:

```text
NEW_ARTIFACT  20
```

After initial ingestion:

```text
logical sources       20
SourceArtifact rows   20
stored objects         20
```

All 20 stored objects passed exact SHA-256 and byte-size integrity verification.

The two PCA-book-like files that had different prospective SHA-256 values remained distinct exact artifacts, as required. No semantic same-work merge was inferred from similar titles/content.

---

## 7. Real duplicate re-encounter

Fourteen earlier unsuffixed lecture uploads were available in the development runtime in addition to the corresponding `(1)`-renamed files recorded in the current batch.

Each was re-ingested against the already resolved logical source identity.

Result:

```text
EXACT_DUPLICATE  14
```

After these real duplicate re-encounters:

```text
logical sources          20
SourceArtifact rows      20
stored objects            20
SourceIngestionEvent rows 34
```

This demonstrates the intended distinction:

```text
new encounter / filename
    !=
new exact artifact
```

The system retained encounter provenance without storing duplicate artifact bytes or creating duplicate artifact identities.

---

## 8. Collection uncertainty preservation

The intake manifest preserves the user's stated uncertainty about the three `Lecture9-*` files as:

```text
association_status = POSSIBLE
```

and does not silently strengthen that status to `CONFIRMED`.

The PCA references remain `UNVERIFIED` as course-membership assertions pending later source review.

---

## 9. Clean integrity audit

Before backup, the working registry/store audit produced only:

```text
OK  20
```

No registered artifact was missing, size-mismatched, digest-mismatched, or corrupt, and no unexpected content-addressed object was orphaned.

The executable test suite separately exercises detection of:

```text
MISSING_OBJECT
SIZE_MISMATCH / DIGEST_MISMATCH
ORPHAN_OBJECT
```

and verifies that backup refuses a dirty source store.

---

## 10. Backup and clean restore

The clean working state was exported to a provider-neutral backup package and restored into a separate clean source registry and clean artifact store.

Backup payload:

```text
object_count        20
object_total_bytes  490083291
```

Safe validation digests:

```text
private registry snapshot SHA-256
5d40280e41d1580e508a0b3d504e553231a2602e4603c68408a55cef98bc9169

backup registry snapshot SHA-256
5d40280e41d1580e508a0b3d504e553231a2602e4603c68408a55cef98bc9169

backup manifest SHA-256
9e43fc0fa1d642cd0095119226e93febc724d12967ca7fc73bdf0e7fe671d08a
```

The private snapshot itself is deliberately not committed because it contains private intake metadata such as observed local paths.

Clean restore result:

```text
restored registry semantic snapshot equals source snapshot  true
restored full integrity audit                              PASS
restored artifact objects                                 20 / 20 OK
```

Thus the source substrate demonstrated recovery rather than only successful ingestion.

---

## 11. Specification 023 gate disposition

The implementation/validation evidence supports the frozen gates as follows:

```text
SU-G01  PASS  clean schema/migration
SU-G02  PASS  source + collection round-trip
SU-G03  PASS  exact bytes / SHA-256 / size
SU-G04  PASS  duplicate -> one binary + one artifact row
SU-G05  PASS  duplicate encounters retained as separate ingestion events
SU-G06  PASS  byte-distinct variants remain distinct
SU-G07  PASS  POSSIBLE / UNVERIFIED preserved
SU-G08  PASS  private paths excluded from public-safe catalog
SU-G09  PASS  deterministic private snapshot
SU-G10  PASS  deterministic public-safe catalog
SU-G11  PASS  missing/corrupt/orphan detection exercised
SU-G12  PASS  clean store audit
SU-G13  PASS  dirty backup refusal exercised
SU-G14  PASS  backup payload + registry snapshot verification
SU-G15  PASS  clean restore reproduces registry semantic state
SU-G16  PASS  restored artifact bytes retain original digests
SU-G17  PASS  restored full integrity audit
SU-G18  PASS  bounded derived-artifact lineage round-trip
SU-G19  PASS  VU manifest exercises source intake without Git binaries
SU-G20  PASS  all comparison result classes preserved by executable tests
SU-G21  PASS  Windows CI matrix
SU-G22  PASS  Ubuntu CI matrix
SU-G23  PASS  inherited regression / checkpoint / routing behavior remains green
```

No frozen gate was weakened after observing the corpus.

---

## 12. Interpretation boundary

`SOURCE_SUBSTRATE_ACCEPTED` means:

```text
ADS now has an accepted V1 mechanism for preserving and governing source artifacts.
```

It does not mean:

```text
all educational sources are already ingested
ChatGPT Library is canonical storage
the disposable development vault is permanent storage
a cloud/object-store provider has been selected
a backup provider has been selected
the final source ontology is frozen
PDF extraction/chunking/embedding is selected
source content is accepted methodological knowledge
redistribution rights are known
```

The next operational step is to instantiate the accepted substrate on user-controlled durable storage, ingest the original local VU Machine Learning course folder, compare it with this first-corpus evidence, and create an independent recoverable backup. Only then should bulk educational-corpus intake proceed.
