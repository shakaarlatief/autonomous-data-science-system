# Research 187: W0 Capture Validation G011 Result

**Date:** 2026-09-18
**Status:** PKA-G011 ACCEPTED / CAPTURE NON-AUTHORITY AND PROSPECTIVE PROMOTION PLAN VERIFIED / W0 REMAINS IN PROGRESS / CURRENT CONTINUITY STILL AUTHORITY
**Selected architecture:** `PKA-CANDIDATE-01`
**Governing contract:** Specification 028
**Implementation design:** Research 179, with Research 185 remaining the prospective G010 field-level refinement
**Prior accepted boundary:** Checkpoint 535 / Research 186 / `bd7a511d7b35e85e86588b5ebbf477e2d6a9ffd6`
**Scope:** Record the accepted G011 capture scanner, non-authority boundary, pure prospective `PromotionPlan`, semantic-unit disposition completeness, and complete post-implementation qualification.
**Authority:** Implementation evidence subordinate to Specification 028 and Research 179. This record accepts PKA-G011 only. It does not accept PKA-G012+, execute a real canonical promotion, start W1/W4 migration, publish successor views, overwrite compatibility authority, or switch operational authority.

## 1. Accepted G011 boundary

G011 completes the W0 capture-validation gate without adding any path that can promote capture material into authority automatically.

The accepted implementation adds:

```text
tools/project_knowledge/capture.py
    pure capture projection
    prospective PromotionPlan construction
    exact natural-target resolution
    no discovery, filesystem I/O, writes, adapters, services or authority imports

tools/project_knowledge/model.py
    CaptureRecord
    PromotionDisposition
    PromotionUnitDisposition
    PromotionPlan
    designated open/historical capture roots

tools/project_knowledge/services/discovery.py
    open capture area
    historical capture area
    parent capture paths outside those areas are DISALLOWED

tools/project_knowledge/services/validation.py
    validated captures returned separately from canonical sources
    captures never enter ValidationResult.sources

tests/unit/test_project_knowledge_capture.py
    focused G011 capture/promotion qualification
```

No canonical source is actually mutated by G011.

## 2. Capture storage and admission

The designated capture homes are exactly:

```text
docs/project_knowledge/captures/open/
docs/project_knowledge/captures/historical/
```

`capture.v1` remains schema-fixed to:

```text
authority_class = capture
```

A `CaptureRecord` additionally requires:

```text
profile = capture.v1
authority_class = capture
carrier inside open/ or historical/
optional summary nonblank when present
provenance/source-reference entries nonblank and duplicate-free
```

A capture declaration outside the designated open/historical areas fails repository admission. The capture parent tree is not a generic queue namespace.

Open and historical capture declarations are schema-validated, but validation exposes them through a separate `captures` tuple. They do not enter `sources`, so ordinary canonical discovery, authority resolution and the G009/G010 canonical view input corpus remain structurally separate from capture material.

## 3. Capture provenance

`CaptureRecord` preserves both capture schema provenance surfaces:

```text
provenance
source_references
```

The deterministic `provenance_chain` is their sorted de-duplicated union. An unreviewed capture may legitimately have no provenance yet, but such a capture cannot produce an accepted promotion plan.

Historical captures remain valid non-authoritative records but cannot re-enter promotion planning. Only a capture still under the open-capture area is eligible for a prospective promotion plan.

## 4. Prospective promotion only

Research 179 explicitly limits W0 to constructing and validating `PromotionPlan`; real W1/W4 canonical promotion is not performed.

`build_promotion_plan(...)` is therefore a pure operation over explicit values. It performs no I/O and exposes no write API.

A valid plan requires:

```text
validated open CaptureRecord
explicit review_disposition = ACCEPTED_FOR_PROMOTION
explicit nonblank accepted_understanding
exactly one natural current canonical target
exact current committed target SourceRevision
nonempty capture provenance chain
nonempty unique required semantic-unit IDs
exactly one typed disposition for every required semantic unit
at least one MATERIALIZED_IN_CANONICAL_SOURCE unit
```

The target may be selected by authored semantic identity, exact carrier path, or both. Exact carrier selection is permitted for canonical sources that intentionally have no durable `semantic_id`; this preserves Specification 028 / Research 179 selective identity rather than minting an identifier from a path.

If both target selectors are supplied they must resolve to the same single canonical owner. Carrier order and lexical order never select the target.

The plan binds the target's exact `SourceRevision`, including its carrier path. A stale revision or revision bound to a different carrier fails visibly.

## 5. Semantic-unit preservation contract

The accepted dispositions are exactly:

```text
MATERIALIZED_IN_CANONICAL_SOURCE
INTENTIONALLY_LATENT_WITH_RECOVERABLE_SOURCE
REJECTED_WITH_REVIEWED_RATIONALE
```

Mechanical qualification proves disposition completeness, not semantic equivalence.

Rules:

```text
required semantic-unit IDs are explicitly authored SemanticId values
required IDs are unique
unit dispositions are typed and unique by semantic-unit ID
sorted representation is presentation only
latent units require at least one recoverable source reference
rejected units require a nonblank reviewed rationale
accepted promotion must materialize at least one unit
no required unit may be missing or silently added
```

Human/model review remains responsible for judging whether canonical prose genuinely realizes accepted meaning where that cannot be deterministically verified, exactly as frozen in Research 179.

## 6. Structural non-authority

G011 now has several independent barriers against authority leakage:

```text
capture.v1 schema cannot claim canonical authority
GovernedSource rejects capture profile + canonical authority
CaptureRecord accepts only capture authority
DiscoveryPolicy excludes capture areas from canonical source discovery
ValidationResult stores captures separately from sources
Authority resolver ignores noncanonical inputs
capture.py imports no authority/services/adapters layer
actual authority.py imports no capture module
PromotionPlan cannot turn the capture carrier into the canonical target
historical captures cannot re-enter promotion planning
no mutation/write/promotion command exists in G011
```

A direct adversarial authority-resolution test supplies a capture as a candidate and receives `MISSING_REQUIRED_AUTHORITY / NO_CANONICAL_CANDIDATES`.

## 7. Selective identity and natural target ownership

G011 does not require every canonical source to have semantic identity.

Qualification proves both target modes:

```text
semantic identity target
    exactly one canonical source with that authored SemanticId

identity-free target
    exact explicitly supplied carrier path + exact committed SourceRevision
```

No target identity is generated from filename, path, title, digest or input position. The existing global architecture guard continues to enumerate every production `SemanticId(...)` construction site, and G011 adds no automatic minting site.

## 8. Adversarial qualification

The focused G011 suite passes 27/27 and covers:

```text
capture provenance preservation and order independence
capture immutability
designated-area enforcement
unreviewed capture valid but not promotable
historical capture cannot be replanned
capture cannot satisfy authority resolution
valid reviewed plan with all three disposition classes
identity-free canonical target via exact carrier
missing/invalid target selector
identity/carrier selector mismatch
explicit accepted review required
explicit accepted understanding required
zero/multiple target owner rejection
stale target revision rejection
revision/carrier mismatch rejection
complete disposition coverage
required-unit duplicate rejection
untyped unit rejection
latent source-reference requirement
rejected rationale requirement
at least one materialized unit
representation-order independence
capture and canonical target remain immutable/non-mutated
```

The substrate snapshot suite additionally proves open/historical captures validate separately in both snapshot modes, remain absent from canonical sources, and captures placed elsewhere are rejected.

The architecture guard proves the capture planner and authority resolver remain structurally disconnected.

## 9. G009 TCB regression caught during final review

A cleanup attempt during independent review tried to replace the literal capture-area defaults in `DiscoveryPolicy` with imported L0 constants. That is semantically equivalent ordinary Python, but G009's frozen trusted-computing-base initialization grammar correctly rejected the class-body imported-name dependency with:

```text
TCB_INITIALIZATION_FORBIDDEN
```

The full G009 execution suite therefore caught the change before acceptance. The attempted cleanup was reverted. The production defaults remain literal deterministic data and the G011 architecture guard asserts they equal the L0 capture-root constants, preventing silent drift without broadening the G009 TCB grammar.

This incident is evidence that G009's execution-attestation boundary remains active after later gates rather than being treated as historical-only tests.

## 10. Final verification evidence

After the final G011 path invariant and TCB-safe discovery repair, the complete unit inventory was requalified through bounded non-overlapping partitions:

```text
G011 capture/promotion                    27 / 27 PASS
G010 current-state core                   76 / 76 PASS
G009 view framework                       53 / 53 PASS
G009 execution/adversarial                76 / 76 PASS
G006 identity                             63 / 63 PASS
G007 authority                           103 / 103 PASS
G008 workstreams                          89 / 89 PASS
substrate schemas                         86 / 86 PASS
substrate declarations                    70 / 70 PASS
substrate snapshots                       50 / 50 PASS
architecture guards                       20 / 20 PASS
inherited unit inventory                 309 / 309 PASS
----------------------------------------------------
complete unit inventory                1,022 / 1,022 PASS
```

Additional pre-acceptance gates:

```text
compileall                              PASS
final WORKTREE validation              PASS / 1,413 candidates / zero diagnostics / NON_COMMITTED
accepted-HEAD COMMIT validation        PASS / 1,411 candidates / zero diagnostics / COMMITTED
accepted implementation base           bd7a511d7b35e85e86588b5ebbf477e2d6a9ffd6
PUBLIC_REPOSITORY_INTEGRITY            PASS
git diff --check                       PASS
```

All task-created `g011-*` temporary directories were removed. The two pre-existing access-restricted historical `.tmp/pytest-checkpoint-275/` and `.tmp/pytest-publication-276/` directories remain intentionally untouched.

## 11. Gate disposition

```text
PKA-G001..PKA-G011   PASS
PKA-G012..PKA-G017   PENDING
W0                    IN PROGRESS
W1                    NOT STARTED
REAL_CANONICAL_PROMOTION=false
CURRENT_OPERATIONAL_AUTHORITY=CURRENT_CONTINUITY_ARCHITECTURE
AUTHORITY_SWITCH_ALLOWED=false
SPECIFICATION_028=UNCHANGED
```

## 12. Next W0 work

The next bounded gate is PKA-G012:

```text
public/private validation rejects synthetic leakage and preserves consequence-sensitive unavailable state
```

G012 must build on the accepted public-safe substrate without re-opening G011 capture authority or beginning W1 migration.

```text
RESEARCH187=PKA_G011_ACCEPTED
PKA_G001_G011=PASS
PKA_G012_G017=PENDING
NEXT=PKA_G012_PUBLIC_PRIVATE_VALIDATION
CURRENT_OPERATIONAL_AUTHORITY=CURRENT_CONTINUITY_ARCHITECTURE
AUTHORITY_SWITCH_ALLOWED=false
```
