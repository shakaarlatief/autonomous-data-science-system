# Research 162: Q7 Real Public / Private Boundary Fixture Freeze

**Date:** 2026-09-14
**Status:** Q7 REAL CROSS-REPOSITORY FIXTURE + ORACLE FROZEN BEFORE IMPLEMENTATION / PRIVATE VALUES NOT PUBLISHED / TARGET ARCHITECTURE NOT SELECTED
**Candidate:** `PKA-CANDIDATE-01`
**Qualification cluster:** Q7 public/private boundary / degraded mode
**Exact public base:** `c4bc46a954a577ee697d5ae2bb62740af17e8900`
**Bound private repository head:** `f5fe565da1cdb6c0daedbf8b9b0aea7586abf350`
**Scope:** Freeze a real cross-repository Candidate 01 test of delegated private authority, `RESOLVED_PRIVATE` preservation, private-continuity PASS/FAIL/NOT_VERIFIED semantics, public non-leakage, bounded private dependency and consequence-sensitive degraded behavior without publishing private-only paths or values.
**Authority:** Experimental protocol only. Public ADS remains sole project-development authority. No private companion mutation is authorized by this freeze.
**Declared references:** `research:161`, `research:159`, `research:144`, `specification:025`, `specification:026`, `path:docs/CONTINUITY.md`, `path:docs/private_companion/README.md`, `checkpoint:506`

## 1. Why Q7 is next

Research 159 identified Q7 as synthetic-only. Research 161 then added real subsystem evidence to Q3 without firing the Object-Primary reopening rule. The next highest-value uncertainty is therefore the constitutional public/private boundary.

This test intentionally uses the real accessible private companion as evidence while ensuring no exact private path, storage coordinate, account identifier, remote destination or other private-only value is written into the public fixture or result.

## 2. Frozen artifacts

```text
Q7_REAL_FIXTURE_V01.json
    SHA-256  a8e0872aa8c1ffab421d86924185c48642a075f872aa64847ebac7df34037bef

Q7_REAL_ORACLE_V01.json
    SHA-256  f85ec95c45b31c4ab9d643737f23bb55c9c269a0fc9915b0c009252aac7b82f4

SHADOW_PRIVATE_BOUNDARY.md
    SHA-256  4839deec38c015f091b31a20c6bf3b130f7245f9425411e674260e527034e745
```

The fixture stores only public repository paths plus cryptographic bindings for the private evidence. The private workspace root and the private sensitive-payload path are runtime inputs and are not serialized into the fixture.

## 3. Real public authority evidence

The fixture binds exact public-base blobs for:

```text
docs/CURRENT_STATE.md
docs/CONTINUITY.md
docs/private_companion/README.md
Specification 025
Specification 026
scripts/check_private_continuity.py
```

Together they establish:

```text
public ADS repository = sole project-development authority
private companion = delegated private continuity complement only
RESOLVED_PRIVATE remains resolved when exact private value is unavailable
private freshness has independent PASS / FAIL / NOT_VERIFIED status
public PASS must not fabricate private PASS
required private NOT_VERIFIED -> stronger transition/action must not claim success
accessible private anchor mismatch -> FAIL
private-only material must not leak through public representations
```

## 4. Real private evidence binding

The private companion is directly accessible through its already-qualified `ads-private` workspace. The freeze binds:

```text
private repository exact HEAD
exact CURRENT_PRIVATE_STATE bytes by SHA-256
one real private Source Vault topology/evidence payload by SHA-256
```

Only the two public-safe anchor fields may be emitted from `CURRENT_PRIVATE_STATE.md`:

```text
Public continuity checkpoint
Public continuity commit
```

At the frozen boundary, those fields still point to an older public boundary. That stale anchor is useful real evidence: the candidate must classify it as `FAIL` against Checkpoint 506 without changing public `RESOLVED_PRIVATE` facts to unresolved and without treating public repository integrity as failed.

## 5. Frozen scenarios

### Q7-S01: ordinary public continuation, private inaccessible

Expected architecture behavior:

```text
private continuity = NOT_VERIFIED
public RESOLVED_PRIVATE state preserved
public continuation remains usable
no private value requested or invented
```

### Q7-S02: private-required transition, private inaccessible

Expected architecture behavior:

```text
private continuity = NOT_VERIFIED
required private dependency surfaced
action/transition blocked or held visibly
public state remains resolved
```

### Q7-S03: private-required transition, real private surface accessible but stale

The existing checker must observe a real anchor mismatch against the frozen public target.

Expected architecture behavior:

```text
private continuity = FAIL
required action blocked
public project-development authority unchanged
public RESOLVED_PRIVATE conclusion preserved
```

### Q7-S04: public-safe projection over real private sensitive payload

The implementation may read the bound private payload internally but must emit only a whitelisted public-safe projection. Exact private-only strings are scanned in memory and must not occur in the serialized result.

Expected architecture behavior:

```text
private value leak count = 0
private path serialization count = 0
```

### Q7-S05: optional retrieval unavailable for low-risk public exploration

Expected architecture behavior:

```text
degraded optional capability
no governing-authority bypass
no false success claim based on missing optional retrieval
```

## 6. Candidate 01 shadow policy under test

The single profile-specific shadow source states only the constitutional/control semantics needed for Q7:

```text
public development authority
private companion delegated role
public RESOLVED_PRIVATE state
private unavailable = NOT_VERIFIED
public-only fallback rule
private-required fail/hold rules
optional-retrieval degraded rule
public projection redaction rule
```

It does not copy private facts and does not introduce a second development authority.

## 7. Leakage discipline

The public fixture is prospectively checked to contain none of:

```text
private workspace root
private sensitive-payload relative path
exact local Source Vault coordinates
private account identifiers
private remote-folder identifiers or URLs
```

The eventual result must likewise avoid serializing any runtime-supplied private root/path or private-only exact values.

## 8. Freeze preflight

Two independent model-free preflights passed before implementation:

```text
Q7_REAL_V01_PUBLIC_FREEZE_PREFLIGHT=PASS
    fixture/oracle contract valid
    6 exact public-base blobs hash-match
    shadow policy parses
    5 scenarios frozen
    prohibited private path/value tokens absent from fixture

Q7_REAL_V01_PRIVATE_BINDING_PREFLIGHT=PASS
    private HEAD exact
    private state SHA exact
    private sensitive payload SHA exact
    public-safe continuity anchor present
    private working tree clean
```

```text
RESEARCH162=Q7_REAL_FIXTURE_FROZEN
FIXTURE_SHA256=a8e0872aa8c1ffab421d86924185c48642a075f872aa64847ebac7df34037bef
ORACLE_SHA256=f85ec95c45b31c4ab9d643737f23bb55c9c269a0fc9915b0c009252aac7b82f4
REAL_SCENARIOS=5
PRIVATE_VALUES_PUBLISHED=0
IMPLEMENTATION=NOT_YET_WRITTEN
CURRENT_ARCHITECTURE=STILL_AUTHORITY
TARGET_ARCHITECTURE=NOT_SELECTED
NEXT=IMPLEMENT_Q7_REAL_V01
```
