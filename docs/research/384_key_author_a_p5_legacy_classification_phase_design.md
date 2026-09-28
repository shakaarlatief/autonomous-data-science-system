# Research 384: Key Author A P5 LEGACY Classification Phase Design and Authorization Boundary

**Date:** 2026-09-28
**Status:** P5 PHASE DEFINED / LEGACY CLASSIFICATION ONLY / 18 FRESH PER-BATCH SESSIONS / OWNER AUTHORIZATION REQUIRED / NO P5 SEMANTIC WORK STARTED
**Parent:** Research 383
**Scope:** Define the next Key Author A phase after P4 BIRTH grouping PASS, preserve the frozen LEGACY classification-order and attention-control contract, separate semantic classification from later candidate-gap/evidence/grouping work, fix the batch exposure and session lifecycle, and return to an explicit owner authorization boundary before any LEGACY semantic source is exposed to the executor.
**Authority:** Operational phase design only. This record does not authorize P5 semantic execution or any later phase and does not modify the Research 332 public R2 V0.3 freeze, Research 334 execution addendum, Research 363 P4 result, or any hidden semantic artifact.

## 1. Why the next phase is LEGACY classification

The frozen R2 protocol has three semantic components:

    STATE
    BIRTH
    LEGACY

Key Author A has now completed:

    P1 STATE
        PASS

    P2 BIRTH development classification
        PASS

    P3 BIRTH held-out classification
        PASS

    BIRTH attention quality
        PASS

    P4 BIRTH grouping
        PASS

No LEGACY semantic execution has yet been authorized.

The frozen public delivery rule says that LEGACY classification batches are exposed sequentially and that the unique LEGACY grouping catalog is exposed only after every LEGACY classification batch is frozen.

The Research 334 execution addendum also requires component-level attention consistency to be computed only after all classification batches for that component are frozen.

Therefore the smallest coherent next semantic phase is:

    P5 = LEGACY CLASSIFICATION

P5 intentionally excludes:

    LEGACY candidate_gap decisions
    LEGACY evidence_refs
    LEGACY witness/control selection
    LEGACY grouping
    LEGACY attention-provenance exposure
    canonical Key A assembly
    commitment generation

Those later operations consume information that must remain hidden until classification freezes.

## 2. Frozen P5 workload

Frozen classification source:

    inputs/r2_v03/packets/legacy_classification_sessions.json

Equivalent public-freeze carrier:

    experiments/ao10_drp03_obligation_units_r2_v03/packets/legacy_classification_sessions.json

The frozen workload is:

    LEGACY sources
        17

    unique semantic items
        3088

    classification batches
        18

    classification presentations
        3210

    maximum presentations in one batch
        392

The eighteenth-batch structure exists because one packet source is split into two classification batches under the frozen <= 400 presentation rule.

The public source catalog itself remains:

    packets/legacy.json

and is not exposed during P5 because it is the later unique-item grouping surface.

## 3. Exact P5 batch order

P5 follows the exact frozen order in legacy_classification_sessions.json.

| Batch | batch_id | packet_source_id | part | presentations | frozen line range |
| ---: | --- | --- | ---: | ---: | --- |
| 1 | LBAT-93e997b85fbc | LSP-157dfb537436 | 1 | 297 | 1-2984 |
| 2 | LBAT-9186ac12caec | LSP-4f1bc6ce3068 | 1 | 156 | 2985-4551 |
| 3 | LBAT-c8da030cfb5d | LSP-8b58f8ed9f58 | 1 | 279 | 4552-7348 |
| 4 | LBAT-2a2a2c500d59 | LSP-816d7caf56ea | 1 | 63 | 7349-7985 |
| 5 | LBAT-8e5543368c9c | LSP-56ca7c39ec1f | 1 | 31 | 7986-8302 |
| 6 | LBAT-cbcee4be4d9b | LSP-31bd3b0b93e0 | 1 | 287 | 8303-11179 |
| 7 | LBAT-3a8ad9962488 | LSP-b413978959e6 | 1 | 128 | 11180-12466 |
| 8 | LBAT-d84497e1538b | LSP-50e46578ac33 | 1 | 45 | 12467-12923 |
| 9 | LBAT-08e16cc81391 | LSP-297f8addd5b0 | 1 | 357 | 12924-16500 |
| 10 | LBAT-c0e5a21d1114 | LSP-ff70bc5bdc8e | 1 | 392 | 16501-20427 |
| 11 | LBAT-858bbaa320f9 | LSP-ff70bc5bdc8e | 2 | 80 | 20428-21234 |
| 12 | LBAT-ce292c613f55 | LSP-2e843c73931a | 1 | 124 | 21235-22481 |
| 13 | LBAT-443067dd58fc | LSP-576a5c4f15b5 | 1 | 120 | 22482-23688 |
| 14 | LBAT-398c47770844 | LSP-19f2c71d43cf | 1 | 306 | 23689-26755 |
| 15 | LBAT-b19942c29622 | LSP-937da553d9a7 | 1 | 78 | 26756-27542 |
| 16 | LBAT-4da53a103ad0 | LSP-1186bc1ed0f6 | 1 | 77 | 27543-28319 |
| 17 | LBAT-70dc99bbdff2 | LSP-8fad31d410da | 1 | 122 | 28320-29546 |
| 18 | LBAT-68f304a3388d | LSP-5d0a24d52fe4 | 1 | 268 | 29547-32235 |

These line ranges are operational exposure guards over the already-frozen bytes. They do not change the protocol.

The executor may read only the current batch range.

An unrestricted read, search, count, grep or other query over the complete multi-batch classification file is prohibited during P5 semantic work.

## 4. Why candidate_gap and evidence are not part of P5

The canonical LEGACY item schema ultimately contains:

    item_id
    normative
    normative_kind
    material
    realization_required
    candidate_gap
    evidence_refs

But P5 operates on hidden-attention presentation IDs, not the unique semantic item catalog.

The semantic author must not inspect the presentation-to-item attention mapping while classifying.

candidate_gap and evidence_refs also require source-level provenance and repository realization/non-realization evidence at the frozen LEGACY horizon.

Therefore P5 freezes only the presentation-level semantic fields that can be judged from the classification presentation itself:

    presentation_id
    normative
    normative_kind
    material
    realization_required

No candidate_gap value is authored in P5.

No evidence reference is authored in P5.

No witness/control identity is selected in P5.

After all P5 batches freeze and the attention quality gate passes, a separately designed later phase may expose the unique LEGACY catalog and the bounded frozen-horizon provenance/evidence surfaces required to author:

    candidate_gap
    evidence_refs
    hidden material-gap witness truth
    already-realized false-gap control truth
    within-source grouping constraints

This separation prevents repository implementation status from feeding back into first-pass semantic classification.

## 5. Negative-control blindness during classification

The public freeze contains two source-level negative controls.

Their identities are mechanically encoded outside the reviewer-facing classification surface.

P5 does not expose:

    legacy_corpus_manifest.json
    packets/legacy_provenance.json
    packets/legacy_attention_provenance.json
    packets/legacy.json

to the semantic author.

This keeps source role, provenance, unique-item identity and duplicate mapping unavailable during classification.

The later evidence/grouping phase may use the frozen provenance and manifest under its own prospectively defined boundary.

## 6. Allowed common P5 sources

Every P5 session may read only the common private working state required to preserve one logical author:

    work/PROGRESS.json
    work/CODEBOOK.md
    work/PRECEDENTS.md
    work/ERRATA.jsonl if present

and the frozen common instructions:

    inputs/r2_v03/KEY_AUTHOR_INSTRUCTIONS.md
    inputs/r2_v03/key_author_schema.json
    inputs/addendum/DRP03_R2_KEY_AUTHOR_EXECUTION_ADDENDUM_V01.md

The only batch-specific semantic source is the currently released line range from:

    inputs/r2_v03/packets/legacy_classification_sessions.json

P5 must not read:

    prior P1 STATE semantic output
    frozen P2/P3 BIRTH classification artifacts
    P4 BIRTH grouping artifacts
    BIRTH attention provenance
    LEGACY attention provenance
    LEGACY unique grouping catalog
    LEGACY provenance
    LEGACY corpus manifest
    frozen LEGACY evidence checkout
    any live ADS repository checkout
    another key author's material
    reviewer annotations
    scoring artifacts
    unrelated local files
    web or connector sources

## 7. Private P5 batch artifact shape

Each batch freezes into one separate private artifact under the private key-author workspace.

Logical working shape:

    {
      "schema_version": 1,
      "protocol_id": "AO10-DRP03-R2-V03",
      "component": "LEGACY",
      "phase": "classification",
      "batch_id": "...",
      "packet_source_id": "...",
      "part_index": 1,
      "presentations": [
        {
          "presentation_id": "...",
          "normative": true | false,
          "normative_kind": "OBLIGATION" | "CONSTRAINT" | "DISPOSITION" | "SEQUENCING" | "PRINCIPLE" | null,
          "material": true | false,
          "realization_required": true | false
        }
      ]
    }

For batch 11:

    part_index = 2

The batch artifact is a private working representation.

It is not the final canonical Key A LEGACY source object.

Later mechanical assembly may use the frozen attention mapping only after the component classification is closed.

## 8. Fresh per-batch session policy

P5 contains 3210 presentations across 18 batches and is substantially larger than any earlier single semantic phase.

The project has already observed that long-lived semantic sessions create compaction and verifier-scope risk.

P5 therefore prospectively selects the stronger lifecycle:

    one fresh standalone Claude Code session per batch

Each fresh batch session must use the same:

    exact model selection
        claude-opus-5-5

    semantic codebook
    frozen protocol/addendum
    append-only precedent record
    append-only errata record
    private workspace
    no-other-key boundary

Fresh sessions do not create new logical key authors.

They are sequential executions of the same Key Author A slot.

The current batch session may not learn or read later batch content.

The next batch is not released until the current artifact has passed task-owner postflight and is accepted/frozen.

This policy is deliberately stronger than the minimum Research 334 allowance for multiple sequential sessions and is selected before P5 begins.

## 9. Batch stop gate

For every batch N:

    task owner releases only batch N
    executor opens a fresh standalone session
    executor reads common allowed sources
    executor reads only the exact batch-N classification range
    executor classifies every presentation independently
    executor writes the one batch-N artifact
    executor updates only authorized private progress
    executor may append precedents or errata under the existing append-only rules
    executor freezes the batch
    executor stops
    executor returns only a bounded non-secret report
    task owner performs mechanical/transcript postflight
    only accepted batch N permits release of batch N+1

The executor report must not reveal:

    presentation labels
    normative-kind counts
    material counts
    realization-required counts
    duplicate/attention identities
    negative-control identities
    precedent content
    semantic rationales
    candidate-gap identities
    evidence results

## 10. Tool and environment boundary

P5 classification requires no shell, Git, repository query, web, connector, MCP or IDE assistance.

Therefore semantic execution remains:

    terminal
        standalone external Windows Terminal / PowerShell

    IDE context
        absent

    permission mode
        default / interactive approval

    web
        denied

    MCP
        disabled

    shell use by semantic executor
        prohibited

    Git use by semantic executor
        prohibited

    repository access by semantic executor
        prohibited

    subagents / parallel semantic workers
        prohibited

If the semantic executor believes a shell or repository query is necessary for classification:

    STOP / HOLD

Repository evidence is intentionally deferred to the later candidate-gap/evidence phase.

## 11. P5 task-owner verification contract

A P5 batch is accepted only if task-owner verification establishes mechanically that:

    current phase and authorization are correct
    all required predecessor phases remain frozen
    only the currently released batch was exposed
    output top-level fields are exact
    protocol/component/phase/batch/source/part metadata are exact
    presentation count matches frozen batch count
    presentation ID set and order exactly match the frozen batch
    no duplicate presentation IDs exist
    every required boolean has boolean type
    normative_kind is in the frozen enum
    normative=false implies normative_kind=null
    normative=true implies normative_kind is non-null
    no forbidden semantic field was added
    no forbidden source/tool was used
    no later batch was exposed
    artifact was written only under the authorized path
    shared precedent/errata state is append-only
    transcript model/session/environment satisfy the phase contract
    no compaction occurred inside the fresh batch session

Semantic correctness is not re-adjudicated by the task owner.

The task owner checks contract compliance, not hidden label content.

## 12. P5 completion and attention gate

P5 classification completes only after all 18 batch artifacts are separately accepted and frozen.

Mechanical cumulative completion requires:

    batches accepted
        18 / 18

    presentations accepted
        3210 / 3210

    artifact batch set
        exact

    presentation-ID sequence per batch
        exact

Only after P5 classification freezes may the task owner expose the frozen LEGACY attention mapping to a mechanical quality evaluator.

The semantic author does not receive that mapping.

Research 330's preregistered key-author gates remain:

    binary normative consistency
        >= 0.95

    normative-kind consistency
        >= 0.90
        on duplicate pairs where the item is treated as normative

A quality failure:

    does not authorize label repair
    does not authorize selective rerun-to-green
    invokes the preregistered quality-failure/replacement semantics
    preserves the failed annotations as evidence

A PASS makes the unique LEGACY catalog eligible for later candidate-gap/evidence/grouping design.

Eligibility is not authorization.

## 13. Later LEGACY phase remains deliberately separate

After P5 classification and its attention gate, the later LEGACY phase must be designed prospectively.

That later phase is expected to bind the already-frozen requirements for:

    unique semantic item reconstruction
    candidate_gap
    evidence_refs
    frozen LEGACY evidence horizon
        0a68787aee5f2c6332d6ee1fb6adbf0efe92a41d
    independent repository evidence
    at least 6 hidden material-gap witnesses
    at least 10 already-realized false-gap controls
    the 2 frozen source-level negative controls
    within-source MUST_JOIN / MUST_SPLIT grouping
    individual confirmation of every stored constrained pair
    no cross-source grouping
    no pair padding

The exact execution mechanics of that later phase are not authorized or frozen here.

## 14. Private-operation control-plane requirement

The P4 experience showed that private task-owner verification should use a purpose-specific bounded Runtime Bridge capability rather than generic shell authority over the Key Author A workspace.

P5 adopts that architecture prospectively.

Before the first P5 batch is released, the project must qualify a bounded private-operation surface that can, at minimum:

    prepare exactly the next frozen LEGACY classification batch
    expose no hidden labels or attention mapping
    postflight exactly one batch attempt
    accept or reject exactly one attempt
    advance only in frozen batch order
    return mechanical booleans/metadata only
    never expose private semantic counts beyond public frozen workload counts
    never accept caller-selected paths, commands, semantic IDs or arbitrary private-root authority

The precise Runtime Bridge implementation may be new or may safely generalize the existing P4 mechanism.

The implementation choice is not itself semantic authority.

P5 semantic launch remains blocked until that capability is qualified and active.

## 15. Owner authorization boundary

Research 384 defines P5 but does not authorize it.

Explicit owner authorization is required because P5 creates new hidden semantic labels over the LEGACY corpus.

Until that explicit authorization:

    P5_AUTHORIZED=false
    LEGACY_LABELS=NONE
    LEGACY_EVIDENCE_WORK=NOT_STARTED
    LEGACY_GROUPING=NOT_STARTED

The owner may:

    ACCEPT
        authorize P5 exactly as defined

    AMEND
        revise the phase prospectively before any LEGACY semantic label exists

    HOLD
        keep all LEGACY work gated

No P5 Claude Code prompt is issued before explicit authorization and bounded private-operation readiness.

## 16. Current boundary

    KEY_A_P1_STATE=PASS
    KEY_A_P2_BIRTH_DEVELOPMENT=PASS
    KEY_A_P3_BIRTH_HELDOUT=PASS
    KEY_A_BIRTH_ATTENTION=PASS
    KEY_A_P4_BIRTH_GROUPING=PASS

    KEY_A_P5_SCOPE=LEGACY_CLASSIFICATION_ONLY
    KEY_A_P5_BATCHES=18
    KEY_A_P5_PRESENTATIONS=3210
    KEY_A_P5_UNIQUE_ITEMS=3088
    KEY_A_P5_FRESH_SESSION_PER_BATCH=true
    KEY_A_P5_AUTHORIZED=false
    KEY_A_P5_PRIVATE_OPS_READY=false

    LEGACY_CANDIDATE_GAP=NOT_STARTED
    LEGACY_EVIDENCE=NOT_STARTED
    LEGACY_GROUPING=NOT_STARTED
    CANONICAL_KEY_A_ASSEMBLY=NOT_AUTHORIZED
    COMMITMENT_GENERATION=NOT_AUTHORIZED
    KEY_AUTHOR_B=NOT_AUTHORIZED
    MIGRATION=NOT_AUTHORIZED

    NEXT=OWNER_DECISION_ON_P5_THEN_BOUNDED_PRIVATE_OPS_QUALIFICATION_BEFORE_SEMANTIC_LAUNCH
