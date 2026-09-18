# Research 188: W0 Public / Private Validation G012 Result

**Date:** 2026-09-18
**Status:** PKA-G012 ACCEPTED / PUBLIC-PRIVATE NON-LEAKAGE AND DEGRADED-MODE CONTRACT VERIFIED / W0 REMAINS IN PROGRESS / CURRENT CONTINUITY STILL AUTHORITY
**Selected architecture:** `PKA-CANDIDATE-01`
**Governing contract:** Specification 028
**Implementation design:** Research 179, with Research 185 retaining its G010 field-level refinement
**Prior accepted boundary:** Checkpoint 536 / Research 187 / `64a4fdc1ac8aa263990c01e4d8e4f5c910e4fa76`
**Scope:** Accept the production public/private validation boundary required by PKA-G012: public-safe abstract private dependency tokens, consequence-sensitive private-state availability semantics, repository and generated-output non-leakage validation, frozen Q7 evidence preservation, and qualification that known private probes remain validation-only rather than generation inputs.
**Authority:** Implementation evidence subordinate to Specification 028 and Research 179. This record accepts PKA-G012 only. It does not accept PKA-G013+, inspect or migrate live private state, start W1, publish successor views, overwrite compatibility authority, or switch operational authority.

## 1. Accepted G012 boundary

G012 builds on the accepted G007 authority engine and G009 generation architecture rather than creating a second public/private subsystem.

The accepted production changes are bounded to:

```text
tools/project_knowledge/model.py
    validate_private_dependency_token(...)
    AuthorityQuery private-dependency validation
    PrivateStateEvidence private-dependency + availability validation

tools/project_knowledge/services/validation.py
    validate_public_projection(...)
    repository declaration/content non-leakage validation

tools/project_knowledge/services/generation.py
    mandatory public view/manifest non-leakage checks
    optional known-private qualification probes at host boundary only

tests/unit/test_project_knowledge_privacy.py
    focused G012 + frozen-Q7 production-semantic qualification

tests/unit/test_project_knowledge_substrate_architecture.py
    structural non-leakage gate placement and worker-boundary guard
```

No private repository path, private root, secret payload or private-only value is introduced into public canonical project knowledge.

## 2. Public-safe private dependency identity

`AuthorityQuery.required_private_dependencies` and `PrivateStateEvidence.dependency` remain strings rather than canonical project semantic IDs, but G012 constrains them to a public-safe abstract-token grammar.

Accepted examples are abstract dependencies such as:

```text
PRIVATE:CONTINUITY
```

Rejected forms include:

```text
Windows absolute paths
Windows drive-relative locators
UNC paths
/home/... or /Users/... paths
file:// locators
../ traversal-like references
URL/path-shaped locators
whitespace-bearing prose
```

The constraint preserves Research 179's bounded public pointer model: public authority may state that a private dependency is required without storing the private source-store root, local path or payload.

## 3. PrivateStateEvidence remains a public-safe verification receipt

The production surface remains exactly:

```text
dependency
available
freshness
```

`available` is `bool | None`; freshness remains the existing typed freshness state. No private path, root, payload, account identifier, secret or arbitrary metadata field was added.

For consequential actions requiring private evidence:

```text
missing evidence           -> REQUIRED_PRIVATE_STATE_UNAVAILABLE
available = false          -> REQUIRED_PRIVATE_STATE_UNAVAILABLE
available = unknown        -> REQUIRED_PRIVATE_STATE_UNAVAILABLE
freshness != FRESH         -> REQUIRED_PRIVATE_STATE_UNAVAILABLE
fresh + available          -> ordinary authority resolution may proceed
```

The existing G007 semantics remain authoritative for this decision.

## 4. RESOLVED_PRIVATE is not collapsed into current verification

G012 preserves the Q7 distinction:

```text
RESOLVED_PRIVATE / public resolved-private conclusion
    semantic fact already known by the public project authority

FRESH / STALE / UNKNOWN + available/unavailable
    current verification state of a delegated private dependency
```

Optional or unavailable private inspection does not invalidate an already public-resolved fact or ordinary public-only continuation.

Required private state, by contrast, fails visibly when it is unavailable or stale. Public authority is never bypassed because optional retrieval is absent.

## 5. Public non-leakage validator

`validate_public_projection(...)` is a fail-visible validator over immutable public UTF-8 bytes.

It provides two complementary controls:

```text
fixture-backed exact-value detection
    caller-supplied known private str/bytes values
    raw UTF-8 and JSON-escaped spellings
    ASCII-escaped Unicode JSON spellings

defense-in-depth locator detection
    Windows absolute paths
    UNC paths
    file:// paths
    /home/<user>/... paths
    /Users/<user>/... paths
```

Diagnostics expose only stable error codes and generic descriptions. They never echo the matched private value or path.

The path detector is deliberately conservative and does not claim universal private-data detection. Public-safe repository-relative references such as `docs/private_companion/README.md`, abstract tokens such as `PRIVATE:CONTINUITY`, and public schema URLs remain legal.

## 6. Repository validation boundary

For a governed declaration admitted by production discovery, repository validation checks the complete declaration carrier bytes after schema parsing succeeds.

Therefore private material hidden in surrounding Markdown prose cannot evade the check merely because the structured declaration itself is public-safe.

Synthetic qualification proves that a governed public declaration containing either:

```text
an absolute/private filesystem locator
an exact known private fixture value
```

fails repository validation without echoing the sensitive value in diagnostics.

This gate does not pretend to scan arbitrary non-governed historical repository prose for secrets. Its production responsibility is the successor project-knowledge publication surface defined by Specification 028.

## 7. Generated-view publication boundary

The ordinary bound G009 generation worker validates generated view and manifest bytes with the generic public-output validator before returning a successful build.

The public host entry point validates those bytes again and may additionally receive known private fixture values for adversarial qualification.

Critically:

```text
known_private_values
    are never sent through _execute_bound(...)
    never enter the isolated worker
    never enter canonical inputs
    never enter the compute unit
    never enter the manifest
    never affect semantic generation
```

They are host-side validation probes only.

A synthetic private capture is also proven unable to influence `source_inventory`: capture material remains noncanonical under G011, so its private payload does not enter generated public bytes even when the host probe knows that value.

## 8. Frozen Q7 evidence is preserved and connected to production semantics

G012 leaves the Research 162/163 Q7 fixture and oracle byte-identical:

```text
Q7_REAL_FIXTURE_V01.json
SHA-256  a8e0872aa8c1ffab421d86924185c48642a075f872aa64847ebac7df34037bef

Q7_REAL_ORACLE_V01.json
SHA-256  f85ec95c45b31c4ab9d643737f23bb55c9c269a0fc9915b0c009252aac7b82f4
```

The focused production suite explicitly maps the frozen scenario classes onto accepted production semantics:

```text
Q7-S01 public-only + private unavailable
    public authority remains RESOLVED

Q7-S02 required private + unavailable
    REQUIRED_PRIVATE_STATE_UNAVAILABLE

Q7-S03 required private + stale
    REQUIRED_PRIVATE_STATE_UNAVAILABLE

Q7-S04 public-safe projection
    covered by exact-value/path non-leakage validation

Q7-S05 optional retrieval unavailable
    retrieval nominations cannot become governing authority
```

The historical Q7 implementation/oracle tests remain separately passing in the inherited suite. G012 does not import the old research script into production.

## 9. Adversarial findings during implementation

Two bounded defects were caught before acceptance.

First, the UNC-path regular expression did not initially detect the JSON-escaped UNC representation used by the public byte validator. The detector was corrected and the adversarial case now passes.

Second, the first private-dependency token grammar would have admitted a Windows drive-relative spelling such as `C:private-state` because it contains no slash. The grammar now rejects any leading single-letter drive designator while preserving authored abstract namespaces such as `PRIVATE:CONTINUITY`.

The exact-value detector was also strengthened to inspect both UTF-8/non-ASCII and ASCII-escaped JSON spellings of known Unicode private fixture values.

## 10. Final verification evidence

The complete unit inventory is 1,057 tests and was requalified through bounded non-overlapping partitions:

```text
G012 public/private                         34 / 34 PASS
G011 capture/promotion                     27 / 27 PASS
G010 current-state core                    76 / 76 PASS
G009 view framework                        53 / 53 PASS
G009 execution/adversarial                 76 / 76 PASS
G006 identity                              63 / 63 PASS
G007 authority                            103 / 103 PASS
G008 workstreams                           89 / 89 PASS
substrate schemas                          86 / 86 PASS
substrate declarations                     70 / 70 PASS
substrate snapshots                        50 / 50 PASS
architecture guards                        21 / 21 PASS
inherited unit inventory                  309 / 309 PASS
-----------------------------------------------------
complete unit inventory                  1,057 / 1,057 PASS
```

One combined G010 regression invocation exceeded the Runtime Bridge 30-second command ceiling. It was split into smaller non-overlapping partitions; the complete 76-test G010 inventory passed. No timeout was treated as a semantic pass.

Additional pre-documentation gates:

```text
compileall                              PASS
final WORKTREE validation              PASS / 1,415 candidates / zero diagnostics / NON_COMMITTED
accepted-HEAD COMMIT validation        PASS / 1,413 candidates / zero diagnostics / COMMITTED
accepted implementation base           64a4fdc1ac8aa263990c01e4d8e4f5c910e4fa76
PUBLIC_REPOSITORY_INTEGRITY            PASS
git diff --check                       PASS
```

All task-created `g012-*` temporary directories were removed. The two pre-existing access-restricted historical `.tmp/pytest-checkpoint-275/` and `.tmp/pytest-publication-276/` directories remain intentionally untouched.

## 11. Gate disposition

```text
PKA-G001..PKA-G012   PASS
PKA-G013..PKA-G017   PENDING
W0                    IN PROGRESS
W1                    NOT STARTED
PRIVATE_LIVE_INSPECTION_REQUIRED=false
CURRENT_OPERATIONAL_AUTHORITY=CURRENT_CONTINUITY_ARCHITECTURE
AUTHORITY_SWITCH_ALLOWED=false
SPECIFICATION_028=UNCHANGED
```

## 12. Next W0 work

The next bounded gate is PKA-G013:

```text
full rebuild and incremental refresh are semantically equivalent on the frozen W0 fixture corpus
```

G013 must build on the accepted G009-G012 substrate without starting W1 or changing authority.

```text
RESEARCH188=PKA_G012_ACCEPTED
PKA_G001_G012=PASS
PKA_G013_G017=PENDING
NEXT=PKA_G013_FULL_INCREMENTAL_EQUIVALENCE
CURRENT_OPERATIONAL_AUTHORITY=CURRENT_CONTINUITY_ARCHITECTURE
AUTHORITY_SWITCH_ALLOWED=false
```
