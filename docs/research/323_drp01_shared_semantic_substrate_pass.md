# Research 323: DRP-01 Shared Semantic Substrate PASS

**Date:** 2026-09-25
**Status:** DRP-01 PASS / SIX SHARED PRIMITIVES SUPPORTED / ROLE MODEL SUPPORTED / STATUS VOCABULARY STILL PROVISIONAL / NEXT DRP-03
**Protocol:** Research 316 / AO10-DRP-V01
**Harness freeze:** Research 321
**Reviewer A freeze:** Research 322
**Reviewer B commit:** b6ba5d22239626b01097add55118b266aed1f633
**Durable evidence:** docs/research/project_knowledge_activation_orchestration/ao10/evidence/drp01_run001_result.json
**Result SHA-256:** ec805f52a30d70a2333934a59f6df58524d54352721d3ef8db937a5fb05c20da
**Scope:** Reconcile the two independent DRP-01 semantic annotations against the frozen comparison harness.
**Authority:** Research evidence only. This does not accept V0.3, finalize the successor specification, fix the exact lifecycle vocabulary, authorize implementation, or change current authority.

## 1. Independence and validation

Reviewer A:

    ChatGPT
    frozen before reviewer B existed
    Research 322
    annotation SHA-256
        08c67c42575ad3691c4646c3437d19ec595b07add063f9f361cf6a7491ac1890

Reviewer B:

    Claude interaction claude-04
    conversation 04 - Assurance and Delivery Architecture Design
    commit b6ba5d22239626b01097add55118b266aed1f633

Claude reports that it read the reviewer packet, schema, definitions and corpus from harness-freeze commit bbd9c370, which predates Annotation A, and read all thirty source carriers from exact base 870689734673e6e8c2212035afcdf27daf733c15.

The committed Annotation B passes the frozen annotation schema/order validation.

Its repository source references also resolve semantically at the frozen base. Three references use structured field paths rather than literal line substrings:

    SOURCE_VAULT_BOOTSTRAP_WORKSTREAM.md::structured declaration.semantic_id
    MC-0029/STATE.json::target.base_ref
    MC-0029/STATE.json::independence.review_base_ref

The referenced fields exist. The frozen reviewer contract permits a stable heading or JSON/structured field reference, so this is not a harness defect.

No comparison threshold changed after either annotation existed.

## 2. Frozen comparison execution

Exact command:

    .\.venv\Scripts\python.exe experiments\ao10_drp01_shared_semantic_substrate_v01\probe.py \
        --annotation-a experiments\ao10_drp01_shared_semantic_substrate_v01\annotation_chatgpt_a.json \
        --annotation-b docs\model_collaboration\threads\MC-0029\messages\005_claude_drp01_annotation_b.json \
        --output experiments\ao10_drp01_shared_semantic_substrate_v01\results\run_001

Observed primary class:

    PASS

Admission-set agreement:

    Jaccard = 1.00

Both reviewers independently admitted the same six shared primitives and rejected all four negative controls.

## 3. Shared primitive result

Both reviewers independently admit:

    semantic_identity
    exact_subject_revision_binding
    provenance_descriptor
    governing_lifecycle_reference
    obligation_reference
    governed_relation_reference

No admitted primitive violates the preregistered two-seam minimum.

No reviewer marks a semantic conflict.

No negative control enters the shared substrate:

    workstream_state                REJECTED
    bridge_execution_mode           REJECTED
    warrant_claim_internal_state    REJECTED
    stochastic_campaign_statistic   REJECTED

This supports the V0.3 architectural shape:

    minimal shared semantic substrate
        +
    bounded domain models

It does not support a universal Project type system.

## 4. Role-model result

Reviewer A:

    carriers                         30
    semantic units                   36
    role representability            1.0000
    carriers > 4 units               0
    irreducibly multi-role units      0
    path misuse                       0

Reviewer B:

    carriers                         30
    semantic units                   45
    role representability            0.9667
    carriers > 4 units               1 / 30 = 0.0333
    irreducibly multi-role units      1 / 45 = 0.0222
    path misuse                       0

Both satisfy all Research 316 thresholds.

The difference in unit counts is useful evidence rather than a failure. The semantic-unit boundary has some reviewer discretion, but practical decomposition remains well below the burden thresholds.

Claude's one irreducibly mixed unit is in CURRENT_STATE.md, where one current-stage heading interleaves current CONTROL meaning with a long historical EVIDENCE narrative.

That finding supports the already-planned bounded-orientation and adoption-economics probes rather than requiring a new architecture change now.

## 5. Lifecycle vocabulary findings

The DRP-01 primary result is PASS, but the exact governing-status vocabulary remains intentionally unselected.

Claude identifies five useful refinement points:

1. **Partial-scope supersession**
   A single token cannot represent a decision that remains effective in one scope and is superseded in another. This should normally be represented by scope-qualified governed relations, not by multiplying status tokens.

2. **Proposal replaced by adopted amended successor**
   A proposal such as WMR-H V0.2 can be replaced before ever becoming effective. The final lifecycle semantics must decide whether SUPERSEDED includes replacement of never-effective proposals or whether a distinct relation/state is cleaner.

3. **Stale self-declared status**
   Research 258 and Research 276 retain historical pre-acceptance status text even though later owner records adopt their content. This strongly supports governing_lifecycle_reference as resolved project state rather than trusting carrier headers or recency.

4. **EFFECT_WITHHELD boundary**
   EFFECT_WITHHELD must mean a deliberate scoped hold on governing effect. It must not become a synonym for "accepted but not yet implemented". Unrealized implementation belongs to obligation/realization state.

5. **Discharged one-time governing items**
   RETIRED appears capable of representing completed/discharged one-time governing items, potentially with a retirement reason rather than another status token.

These are design inputs for the successor semantic contract.

They do not make DRP-01 an AMEND because V0.3 explicitly left the exact role/status enum pending DRP-01 and the frozen PASS criteria concern practical representability, substrate boundedness and semantic separation.

## 6. Canonical-boundary observations

The two reviewers agree on admission but not every wording boundary.

Claude usefully narrows:

    provenance_descriptor
        derivation/semantic lineage at the shared layer
        executor/build provenance remains assurance-owned

    obligation_reference
        accepted normative Project obligations
        collaboration next-actor duties are a homonymous domain concept,
        not automatically the same shared primitive

These narrower boundaries are consistent with the anti-over-unification goal.

The final successor contract should normalize exact definitions using the seam evidence, rather than concatenating both reviewers' wording.

## 7. Architecture consequence

Primary evidence class:

    TARGET_ARCHITECTURE_EVIDENCE

V0.3 core disposition:

    MINIMAL_SHARED_SEMANTIC_SUBSTRATE    RETAIN
    SIX_CANDIDATE_PRIMITIVES             SUPPORTED FOR DOWNSTREAM DESIGN
    DOMAIN_NEGATIVE_CONTROLS             KEEP DOMAIN-OWNED
    SEMANTIC_UNIT ROLE MODEL              RETAIN
    PATH AS IDENTITY/AUTHORITY            REJECT
    EXACT STATUS VOCABULARY               STILL PROVISIONAL

Standing falsifiers:

    F-C role-granularity failure     RESOLVED FOR FROZEN CORPUS
    F-E substrate creep              RESOLVED FOR CANDIDATE/CONTROL SET

This does not prove future primitives may be admitted casually. Every later shared primitive still requires the seam-admission rule.

## 8. Current state

    DRP09=PASS
    DRP05A=PASS
    DRP05B=PASS_DETECTIVE_FIRST
    DRP01=PASS

    DRP01_ADMISSION_JACCARD=1.00
    DRP01_SHARED_PRIMITIVES=6
    DRP01_NEGATIVE_CONTROLS_ADMITTED=0

    DRP_RESULT_COUNT=4
    UNRESOLVED_AMEND_RESULTS=0
    ACTIVE_HARNESS_INVALID_RESULTS=0

    EXACT_ROLE_STATUS_ENUM=NOT_FINAL
    OWNER_DECISION=NOT_READY

    AO10_PRODUCTION_IMPLEMENTATION_AUTHORIZED=false
    AO10_SHADOW_ACTIVATION_AUTHORIZED=false
    CURRENT_STATE_COMPACTION_AUTHORIZED=false
    PHYSICAL_MIGRATION_AUTHORIZED=false
    CURRENT_ORACLE_RETIREMENT_AUTHORIZED=false
    AUTHORITY_SWITCH_ALLOWED=false

    NEXT=DRP03_OBLIGATION_UNIT_HARNESS_FREEZE
