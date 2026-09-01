# Current State

**Checkpoint:** 269  
**Date:** 2026-09-01  
**Active development branch:** `v1-source-vault-bootstrap-resume`  
**Active PR:** none  
**Promoted V1 integration branch:** `v1-frontend-spike` at `2480109fadeee1e480ef03b82e335aacdf9adf91`  
**Latest specification:** Specification 027 extends Specifications 025/026 with governed historical-intermediate checkpoint integrity and discoverability.  
**Latest scientific experiment:** Specification 022 remains `INCOMPLETE / EXECUTION INTEGRITY FAILED`; no GENERIC / ADS_HORIZON / ORACLE_HORIZON comparison may be inferred from that run.

## Active interaction context

```text
Interaction environment  ChatGPT
Project / workspace      Autonomous Data Science System
Interaction session      chatgpt-13
Conversation title       13 - Repository Integrity / Canonical Reconciliation
Primary collaborator     ChatGPT
```

Repository artifacts remain authoritative across chats and models.

---

## Current active stage: governed repository integrity hardening

The v0.8 repository-integrity architecture is implemented and its reconciled public target at commit `284c99e094a44750404fa197da127bfaf6d9b93a` passed the full Repository Integrity workflow on Ubuntu and Windows. The private companion was separately reconciled against that public target.

A later audit of the repaired duplicate Checkpoint 252 case identified one bounded edge case: the useful source-faithful reintegration milestone whose numeric identity was retired remained outside both numbered-checkpoint metadata enumeration and numbered Knowledge Map range coverage.

Research 108 and Specification 027 close that gap without changing numbered chronology.

The current integrity architecture now distinguishes:

```text
numbered checkpoints
    numbered identity
    checkpoint-era metadata validation
    active-branch freshness participation
    compact Knowledge Map range coverage

historical intermediate checkpoint milestones
    non-numbered intermediate_YYYY-MM-DD_<slug>.md identity
    Original recorded identity retained as provenance only
    Identity disposition required
    checkpoint-era metadata validation
    direct Knowledge Map routing
    no participation in numbered freshness or checkpoint ranges
```

The existing aggregate public integrity gate remains the authority for exact-target acceptance. A public branch mutation is accepted only when the Repository Integrity workflow passes on that exact HEAD; prior green runs are not inherited automatically.

---

## Checkpoint 252 identity repair remains canonical

Canonical numbered Checkpoint 252 remains:

```text
docs/checkpoints/252_advanced_integrated_cockpit_spatial_rail_study_opened.md
```

The earlier source-faithful reintegration milestone remains preserved as:

```text
docs/checkpoints/intermediate_2026-08-28_source_faithful_reintegration_interaction_integrity_gate.md
```

That intermediate record is still useful historical continuity and repair provenance. It receives no replacement checkpoint number.

Specification 027 now makes its status mechanically explicit:

```text
metadata/provenance validation      REQUIRED
direct semantic Knowledge Map route REQUIRED
numbered checkpoint range           NOT APPLICABLE
current_checkpoint freshness        NOT APPLICABLE
```

No renumbering of Checkpoint 253 onward occurs.

---

## Current canonical integrity route

The governing route for the present repository-integrity boundary is:

```text
docs/research/103_repository_knowledge_discoverability_and_risk_scaled_verification_audit.md
docs/research/104_repository_information_architecture_and_exhaustive_knowledge_routing_refinement.md
docs/research/105_codexless_local_execution_bridge_evaluation.md
docs/research/106_governed_repository_integrity_and_continuity_bootstrap_hardening.md
docs/research/107_post_outage_repository_integrity_recovery_audit.md
docs/research/108_historical_intermediate_checkpoint_integrity_and_discoverability_audit.md
docs/specifications/024_v1_model_collaboration_state_guard.md
docs/specifications/025_v1_governed_repository_integrity_and_continuity_hardening.md
docs/specifications/026_v1_repository_integrity_recovery_amendment.md
docs/specifications/027_v1_historical_intermediate_checkpoint_integrity_extension.md
docs/checkpoints/README.md
docs/checkpoints/268_first_corpus_matched_codexless_local_execution_evaluation_opened.md
docs/checkpoints/269_codexless_read_path_verified_continuity_reconciled_for_chatgpt_12_handoff.md
docs/CONTINUITY.md
docs/DEVELOPMENT_METHOD.md
docs/current_routing.json
docs/KNOWLEDGE_MAP.md
```

Development Method v0.9 is the current operational method for this refinement.

SOLO execution is proportionate here. The method keeps SOLO as the default for routine bounded work and requires multi-model collaboration when independent review or counter-design value justifies the coordination cost. Research 108 records why another Claude round was not required for this narrow edge case.

---

## Source Vault remains paused and unchanged

Repository-integrity hardening does not authorize Source Vault ingestion.

The permanent Source Universe remains frozen at:

```text
permanent Source Registry           MIGRATED / VERIFIED
Alembic head                        0003_source_universe
SQLite tables                       33
first permanent corpus compare      20 / 20 MATCH
DIFFERENT_ARTIFACT                  0
MISSING_LOCAL_SOURCE                0
ADDITIONAL_LOCAL_SOURCE             0
source ingestion                    NOT STARTED
working-store integrity audit       PENDING
independent encrypted backup proof  PENDING
clean restore + restored audit      PENDING
Course 2                            BLOCKED
```

The original source root and other machine-specific operational coordinates remain `RESOLVED_PRIVATE`. Their exact values do not belong in public Git.

The next-generation Project Cockpit frontend exploration remains paused at its previously frozen state. This integrity refinement changes only repository governance around the preserved intermediate milestone; it does not alter accepted Cockpit design or implementation evidence.

---

## Research 105 remains open at the controlled-write boundary

The Codexless local-execution evaluation remains:

```text
OPEN / READ-ONLY PATH VERIFIED / WRITE VALIDATION PENDING
```

The controlled disposable write/read/delete proof has not been run and must not be inferred from GitHub-side repository mutations.

That proof must test the actual local Codexless bridge against the actual local checkout, remain outside authoritative Source Universe state, and leave protected state unchanged.

---

## Public/private/preflight claims remain separate

The integrity architecture distinguishes:

```text
PUBLIC_REPOSITORY_INTEGRITY
    PASS | FAIL

PRIVATE_CONTINUITY_INTEGRITY
    PASS | FAIL | NOT_VERIFIED

CHAT_ROTATION_PREFLIGHT
    PASS | HOLD | FAIL
```

A public PASS never proves private freshness. After any new public continuity commit, the private public-safe synchronization anchor must be reconciled separately before a new private PASS is claimed.

Even when public and private integrity are both green, the open Research 105 local-execution obligation keeps chat-rotation preflight at HOLD until that transition obligation is resolved or explicitly reclassified.

---

## Exact continuation order

For the current branch HEAD:

```text
1. require the complete Repository Integrity workflow to pass on the exact public commit
2. if private continuity is required, reconcile its public-safe anchor to that exact public commit and verify it separately
3. keep CHAT_ROTATION_PREFLIGHT at HOLD while Research 105 remains an open transition obligation
4. resume the controlled disposable Codexless local write/read/delete proof only through the actual local execution bridge
5. classify the local-execution bridge explicitly
6. only after prerequisite gates permit it, resume permanent Source Vault bootstrap/ingestion
```

If the public gate exposes an unexpected defect, diagnose the exact contract before further mutation. Do not weaken validators to obtain a green result.

No new checkpoint is created merely because Research 108, Specification 027 or Development Method v0.9 exists. A checkpoint after 269 still requires a meaningful verified transition.

---

## Minimum reading for continuation

Bootstrap-critical first reads:

```text
README.md
docs/README.md
docs/CONTINUITY.md
docs/current_routing.json
docs/CURRENT_STATE.md
docs/KNOWLEDGE_MAP.md
```

Then read the governing current boundary:

```text
docs/research/105_codexless_local_execution_bridge_evaluation.md
docs/research/106_governed_repository_integrity_and_continuity_bootstrap_hardening.md
docs/research/107_post_outage_repository_integrity_recovery_audit.md
docs/research/108_historical_intermediate_checkpoint_integrity_and_discoverability_audit.md
docs/specifications/025_v1_governed_repository_integrity_and_continuity_hardening.md
docs/specifications/026_v1_repository_integrity_recovery_amendment.md
docs/specifications/027_v1_historical_intermediate_checkpoint_integrity_extension.md
docs/checkpoints/README.md
docs/checkpoints/intermediate_2026-08-28_source_faithful_reintegration_interaction_integrity_gate.md
docs/checkpoints/268_first_corpus_matched_codexless_local_execution_evaluation_opened.md
docs/checkpoints/269_codexless_read_path_verified_continuity_reconciled_for_chatgpt_12_handoff.md
docs/DEVELOPMENT_METHOD.md
```

When relevant and accessible, retrieve the private companion only after the public reconstruction.

The public repository remains the sole project-development authority.
