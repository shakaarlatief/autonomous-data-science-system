# Research 172: Q1 + Q2 Cross-Provider Authority Hard-Case Fixture Freeze

**Date:** 2026-09-14
**Status:** CONTROLLED NON-OPENAI PROVIDER FIXTURE + ORACLE FROZEN / MANUAL EXTERNAL RUN NEXT / TARGET ARCHITECTURE NOT SELECTED
**Candidate:** `PKA-CANDIDATE-01`
**Qualification clusters:** Q1 provider/tool portability + Q2 authority hard cases
**Exact real base:** `a685ef48c4c4853babff9295f03f198c7b3dcd1d`
**Scope:** Freeze the final pre-Q10 challenge: a fresh non-OpenAI provider must reconstruct Candidate 01 authority semantics from one bounded project-controlled packet, refuse to treat probabilistic retrieval rank as authority, resolve one scoped replacement, fail visibly on an under-specified authority scope, and preserve one partially superseded decision's retained outcome.
**Authority:** Experimental protocol only. Current continuity remains operational authority; the portable packet is a derived consumption view and not project authority.
**Declared references:** `research:171`, `research:170`, `research:168`, `research:144`, `checkpoint:516`, `path:docs/DECISIONS.md`

## 1. Why this is the final pre-Q10 test

Research 171 leaves exactly three non-Q10 items without real Candidate 01 evidence:

```text
KA-R36  provider and tool portability
KA-R14  supersession / supplementation / conflict visibility
KA-R24  probabilistic retrieval is not sole governing authority
```

They are tested together because the critical portability question is not merely whether another model can read Markdown. It is whether a different provider can reconstruct the same governing result when probabilistic ranking points toward a plausible but non-governing source and explicit lifecycle/scope semantics must control the decision.

## 2. Frozen artifacts

```text
Q1_Q2_CROSS_PROVIDER_FIXTURE_V01.json
    SHA-256  abb4ccc8d7e5915d231a44f359cd9aab7f1b0029d1cd8708ec05e3105c746211

Q1_Q2_CROSS_PROVIDER_ORACLE_V01.json
    SHA-256  9b6a6cae95bad6a6f5a0295d05988e808b46d6c9f4af9de44b6ec69f1abd39be

PORTABLE_PROVIDER_PACKET_V01.md
    SHA-256  dc24924a828da7ea4d2421e70c35d7d65a0b42decf83cb3d03c888a461a351b8

EXTERNAL_PROVIDER_REQUEST_V01.txt
    SHA-256  97237d154bdb93384c03d800b7aff16f392152bc9e2c0c0d532d07dbd0e7e610

RETRIEVAL_NOMINATIONS_V01.json
    SHA-256  76e5da10ab1ec2ff8bae6d91837e1ff1162b8998c27e9fa5044dfe9af0b3d1db
```

The oracle is separate from the portable packet and must not be available to the external collaborator.

## 3. Provider boundary

This experiment requires:

```text
fresh external-provider session     yes
OpenAI provider                      forbidden
prior ADS conversation context       forbidden
web browsing                         forbidden
outside packet evidence              forbidden
exact provider + model provenance    required
```

A fresh Claude-family run is the intended manual path because it supplies a capable non-OpenAI provider without changing the repository-controlled semantics under test.

## 4. Task A: scoped replacement versus retrieval rank

The derived retrieval layer deliberately ranks `D-011` above `D-028` for the question:

> Which decision governs the V1 persistence/retrieval architecture?

Candidate 01's explicit source-local relation says `D-011 REPLACE -> D-028` for scope `v1_persistence_retrieval_architecture`. Therefore a portable implementation must resolve the governing source from explicit authority semantics rather than similarity rank.

## 5. Task B: fail-visible under-specified scope

The question:

> Which implementation architecture decision governs?

intentionally omits the implementation subsystem. `D-011` has different scoped successors for persistence/retrieval, persistence tooling, Python tooling, interchange, reasoning runtime and source-universe substrate, plus residual applicability elsewhere.

The external provider must not invent a subsystem or choose the top retrieved candidate. The safe result is visibly unresolved until scope is supplied.

## 6. Task C: partial supersession with retained outcome

For external learning-source architecture, `D-015` is partially superseded by `D-033` in the architecture-uncertainty scope while retaining the durable outcome that source binaries do not belong in public Git merely because ADS consumes them.

The portable collaborator must distinguish:

```text
current governing architecture  D-033
retained outcome                 public_git_source_binary_exclusion
```

This tests that supersession does not erase explicitly retained semantics.

## 7. Probabilistic retrieval challenge

`RETRIEVAL_NOMINATIONS_V01.json` intentionally puts semantically plausible but sometimes non-governing sources at rank 1. It is marked `authority_class=derived` and explicitly warns that scores nominate evidence only.

A pass requires all three tasks to record `retrieval_used_as_authority=false`.

## 8. Portable packet design

`PORTABLE_PROVIDER_PACKET_V01.md` is self-contained and project-controlled. It includes:

```text
exact real-base source bindings
Candidate 01 relation semantics
canonical D-011 / D-015 / D-028 / D-033 excerpts
derived retrieval nominations
three bounded tasks
strict JSON result schema
```

The packet itself is a derived consumption view. It does not create a new authority source.

## 9. Freeze preflight

```text
Q1_Q2_CROSS_PROVIDER_V01_FREEZE_PREFLIGHT=PASS
fixture/oracle identity             PASS
real source hashes                  exact base match
portable artifact hashes            exact
OpenAI provider                      forbidden
prior ADS context                    forbidden
web browsing                         forbidden
oracle access                        forbidden
exact provider/model provenance      required
current project authority            unchanged
```

## 10. Execution rule

The project owner must run the exact external request in a completely fresh non-OpenAI provider session with the portable packet attached. The returned JSON must be copied verbatim into `EXTERNAL_PROVIDER_RESULT_V01.json` and preserved before the oracle is evaluated.

```text
RESEARCH172=CROSS_PROVIDER_FIXTURE_FROZEN
REAL_BASE=a685ef48c4c4853babff9295f03f198c7b3dcd1d
FIXTURE_SHA256=abb4ccc8d7e5915d231a44f359cd9aab7f1b0029d1cd8708ec05e3105c746211
ORACLE_SHA256=9b6a6cae95bad6a6f5a0295d05988e808b46d6c9f4af9de44b6ec69f1abd39be
CURRENT_ARCHITECTURE=STILL_AUTHORITY
TARGET_ARCHITECTURE=NOT_SELECTED
NEXT=RUN_FRESH_NON_OPENAI_PROVIDER
```
