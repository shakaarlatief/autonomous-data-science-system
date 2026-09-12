# Project-Development Knowledge Failure Corpus

**Date opened:** 2026-09-12
**Status:** RESEARCH 124 EMPIRICAL CORPUS V0.1 / REAL HISTORICAL CASES ONLY / NO REMEDIES ENCODED
**Research owner:** Research 124
**Scope:** Bounded evidence corpus of observed project-development knowledge failures, near-misses, recovery events and explicit structural gaps used to characterize failure mechanisms before testing successor mechanisms.
**Authority:** Research support evidence. This corpus does not define the target architecture, does not replace the source records it cites, and must not be read as a list of accepted remedies.

## 1. Purpose

Research 124 needs empirical cases before mechanism probes. The corpus exists to preserve **what went wrong or became unreliable**, with enough source evidence to reproduce the mechanism, without embedding the architecture expected to fix it.

The corpus therefore separates:

```text
OBSERVED_FAILURE
    an incorrect, stale, misleading or omitted result actually occurred

OBSERVED_NEAR_MISS
    a concrete inconsistency/unsafe condition was caught before downstream harm

OBSERVED_RECOVERY_EVENT
    an interruption or ambiguous state required explicit reconstruction to continue safely

OBSERVED_PATTERN_COMPOSITE
    multiple durable records support a recurring pattern, but no single event owns the whole claim

STRUCTURAL_GAP_NOT_FAILURE
    a real missing capability/state representation is observed, but no incorrect continuation
    outcome has yet been proven from it
```

A `STRUCTURAL_GAP_NOT_FAILURE` entry is deliberately **not** counted as an empirical failure when later evaluating prevalence.

## 2. Detection labels

```text
OWNER_CAUGHT
    project owner noticed/corrected the problem

COLLABORATOR_CAUGHT
    ChatGPT/Claude/audit reasoning detected it before owner intervention

VALIDATOR_CAUGHT
    deterministic validation exposed it

POST_HOC_AUDIT
    later repository audit reconstructed the defect

HUMAN_REVIEW
    product/review observation exposed the defect
```

Multiple detection labels may apply.

## 3. Corpus summary

Current V0.1 contains:

```text
retrieval / discoverability                         3 cases
stale convenience / derived / duplicated view       3 cases
situation dispatch / governing-procedure activation 3 cases
required authority / source selection               2 cases
semantic scope / identity conflation                3 cases
continuation / resume                               2 cases, only 1 observed recovery event
compression / synthesis / transcription             3 cases
public / private continuity boundary                2 cases
latent known-risk / reopen-trigger activation       1 composite pattern
```

The classes are intentionally uneven. Sparse classes remain sparse rather than being padded with invented examples.

## 4. Retrieval / discoverability

### KF-RD-01 — Global Knowledge Map drifted into current Cockpit continuation

```text
Evidence type       OBSERVED_FAILURE
Detection           OWNER_CAUGHT + POST_HOC_AUDIT
Primary evidence    docs/research/103_repository_knowledge_discoverability_and_risk_scaled_verification_audit.md
Related boundary    docs/checkpoints/265_development_method_v06_knowledge_routing_and_verification_reconciliation.md
Observed period     2026-08-29
```

Observed state:

- the intended project-wide `KNOWLEDGE_MAP.md` existed;
- underlying durable knowledge files remained present;
- the current branch's global map had gradually become dominated by the active Cockpit continuation and recent Research/Checkpoint state;
- a fresh collaborator could recover the immediate Cockpit boundary while having a weaker route to unrelated/older project knowledge unless it already knew what to search for.

Observed consequence: semantic project-wide discoverability regressed without substantive knowledge loss.

Do not encode from this case whether the correct response is tags, generated views, semantic search, hierarchy or another mechanism.

### KF-RD-02 — Continuity surface retained stale interaction identity

```text
Evidence type       OBSERVED_FAILURE
Detection           POST_HOC_AUDIT
Primary evidence    docs/research/103_repository_knowledge_discoverability_and_risk_scaled_verification_audit.md §14
Observed period     2026-08-29
```

Observed state:

- current routing had already moved to the newer persistent interaction;
- `docs/CONTINUITY.md` still named an older ChatGPT session;
- the continuation surface therefore mixed stable procedure with stale current-context data.

Observed consequence: a reconstruction document could point at obsolete live context even while the actual current route had advanced.

### KF-RD-03 — Handoff audit found multiple unrouted/stale continuity surfaces

```text
Evidence type       OBSERVED_NEAR_MISS
Detection           COLLABORATOR_CAUGHT + OWNER_REQUESTED_AUDIT
Primary evidence    docs/checkpoints/269_codexless_read_path_verified_continuity_reconciled_for_chatgpt_12_handoff.md
Observed period     2026-08-31
```

Before planned rotation the audit found, among other defects:

```text
CURRENT_STATE stale relative to current_routing
new Codexless research/checkpoint not yet routed in KNOWLEDGE_MAP
Checkpoint 268 missing required metadata/provenance
```

The substantive local-execution evidence was still durable. The problem was that normal continuation/navigation surfaces did not consistently expose the durable state.

The defects were caught before the planned persistent-session handoff proceeded.

## 5. Stale convenience / derived / duplicated view

### KF-SV-01 — Repeated current-routing/prose drift motivated machine guard

```text
Evidence type       OBSERVED_PATTERN_COMPOSITE
Detection           POST_HOC_AUDIT
Primary evidence    docs/checkpoints/172_machine_checkable_current_routing_consistency_guard_passed.md
Observed period     through 2026-08-24
```

Checkpoint 172 records the discriminator explicitly:

```text
substantive preservation failure    NO
routing/current-state drift         YES, repeatedly observed
```

The project had several prose surfaces representing overlapping current routing. The durable facts survived, but copies drifted enough to justify a narrow machine-readable routing contract and contradiction detector.

The corpus records the repeated drift pattern, not the later validator as the expected successor mechanism.

### KF-SV-02 — Human Subject index and machine topic structure formed an unverified duplicate view

```text
Evidence type       OBSERVED_NEAR_MISS
Detection           CLAUDE_REVIEW + COLLABORATOR_VERIFICATION
Primary evidence    docs/model_collaboration/threads/MC-0005/RESOLUTION.md §3 F1
Observed period     2026-08-29
```

The numbered human-facing Subject index and machine-checked `KM-TOPIC` sections summarized the same semantic structure but were independently editable. The review classified this as the same general convenience-index-versus-authoritative-structure drift seam observed elsewhere.

This entry is a near-miss rather than proof that the two lists had already produced a user-visible wrong route at that exact boundary.

### KF-SV-03 — Promoted research summary contained wrong inventory counts

```text
Evidence type       OBSERVED_FAILURE
Detection           POST_HOC_AUDIT
Primary evidence    docs/research/107_post_outage_repository_integrity_recovery_audit.md §7
Underlying evidence workflow run 33415541195 / job 99565171066
Observed period     2026-08-31 to 2026-09-01
```

The raw metadata-inventory workflow was authoritative, but Research 106 transcribed materially incorrect family counts and the closed MC-0008 Message 004 contained a smaller count mismatch.

Observed consequence: a higher-level durable summary did not faithfully represent the raw evidence it summarized, although the substantive conclusion about family heterogeneity remained valid.

Cross-label: `COMPRESSION_SYNTHESIS_TRANSCRIPTION`.

## 6. Situation dispatch / governing-procedure activation

### KF-SD-01 — Exact restart runbook existed but wrong restart order was given

```text
Evidence type       OBSERVED_FAILURE
Detection           OWNER_CAUGHT
Primary evidence    docs/OPEN_ARCHITECTURE_BACKLOG.md AB-022, lines/section "Reconstruction-to-operational-authority routing"
Session             chatgpt-17
```

A fresh session performed the canonical public bootstrap and reconstructed the current checkpoint/research, but did not consume `docs/local_execution/OPERATIONS.md` before giving ordered restart instructions.

The collaborator instructed the owner to stop Codexless before the tunnel. The authoritative runbook required the reverse initial order. The owner noticed the mismatch and forced a runbook check before acting.

Critical discriminator:

```text
correct knowledge existed
correct authority was linked from live state
new-session reconstruction broadly succeeded
required governing procedure did not enter the reasoning path before exact guidance
```

Cross-label: `REQUIRED_AUTHORITY_SOURCE_SELECTION`.

### KF-SD-02 — Exact developer-MCP refresh procedure existed but generic fallback wording was produced

```text
Evidence type       OBSERVED_FAILURE
Detection           OWNER_CAUGHT / SAME BROADER CHATGPT-17 EPISODE
Primary evidence    docs/OPEN_ARCHITECTURE_BACKLOG.md AB-023 continuation note
Session             chatgpt-17
```

After publication, the collaborator suggested generic wording equivalent to "refresh the connector/app if that surface supports it" even though the repository already preserved the exact ChatGPT developer-MCP refresh path and readiness preconditions in `OPERATIONS.md`.

This is retained as a separate output-level exemplar but **not counted as an independent session-level incident** from KF-SD-01.

### KF-SD-03 — Established repository-native Claude collaboration process did not activate

```text
Evidence type       OBSERVED_FAILURE
Detection           OWNER_CAUGHT
Primary evidence    docs/checkpoints/453_project_knowledge_architecture_scope_activation_weaknesses_claude_dialogue_opened.md
Session             chatgpt-23
```

When the owner asked ChatGPT to discuss Research 124 with Claude, ChatGPT drafted a large manual relay prompt rather than activating the already-established repository-native `MC-*` / `REVIEW_INBOX` collaboration protocol. The owner had to remind ChatGPT how the process works.

Critical discriminator:

```text
governing process knowledge existed durably
current task clearly matched that process
repository access was available
no retrieval/process check was initiated before a generic workflow was proposed
```

## 7. Required authority / source selection

### KF-AS-01 — Cockpit integration used textual summaries instead of exact accepted implementation sources

```text
Evidence type       OBSERVED_FAILURE
Detection           HUMAN_REVIEW + POST_HOC_AUDIT
Primary evidence    docs/research/088_integrated_cockpit_fidelity_failure_and_source_of_truth_recovery_audit.md
Boundary evidence   docs/checkpoints/250_integrated_cockpit_fidelity_failure_recovery_audit_opened.md
Observed target     8e554d847bb3b6318db432abcb5dff742f0fa523
```

Exact accepted target SHAs and executable HTML/CSS/JS artifacts existed for major Phase-C choices. The holistic integration instead created a new monolithic implementation using textual decision summaries as guidance.

Observed consequence: accepted geometry, visual grammar and behavior were materially reinterpreted even though the stronger implementation evidence was preserved.

Primary class here is source selection/authority: the integration process stopped at a weaker semantic summary instead of consuming the exact implementation provenance required for fidelity.

Cross-label: `COMPRESSION_SYNTHESIS_TRANSCRIPTION`.

### KF-AS-02 — Accepted integrity architecture was narrowed during specification promotion

```text
Evidence type       OBSERVED_NEAR_MISS
Detection           POST_HOC_AUDIT
Primary evidence    docs/research/107_post_outage_repository_integrity_recovery_audit.md §§9-11
Observed period     2026-08-31 to 2026-09-01
```

After MC-0008 accepted a governed-document integrity architecture, Specification 025 omitted or narrowed several accepted pieces, including compatibility handling for existing explicit relationship fields, the private-side public continuity pointer, and explicit H1/filename identity agreement.

The omissions were caught before implementation proceeded.

Observed consequence: promotion from collaboration/research architecture into a formal specification lost parts of the accepted source contract.

This is a near-miss rather than evidence that the missing rules had already caused downstream repository corruption.

## 8. Semantic scope / identity conflation

### KF-SC-01 — Project-development knowledge architecture was conflated with ADS product architecture

```text
Evidence type       OBSERVED_FAILURE
Detection           OWNER_CAUGHT
Primary evidence    docs/checkpoints/453_project_knowledge_architecture_scope_activation_weaknesses_claude_dialogue_opened.md
Session             chatgpt-23
```

ChatGPT referred to the project-development knowledge architecture under redesign as though it were "ADS" itself. The owner corrected the distinction.

Observed consequence: reasoning language collapsed two architectural scopes that have different authority, purpose and evolution.

### KF-SC-02 — Collaboration role and write scope were conflated during multi-model architecture design

```text
Evidence type       OBSERVED_NEAR_MISS
Detection           CHATGPT_REVIEW + CLAUDE_ACKNOWLEDGEMENT
Primary evidence    docs/checkpoints/202_mc_0001_resolved_specification_024_frozen_mc_0002_opened.md
Observed period     2026-08-26
```

During MC-0001, a single-active-writer proposal conflated collaborator role with write authority/scope. ChatGPT identified the defect and Claude acknowledged/corrected it before promotion.

This is an adjacent semantic-conflation exemplar rather than the same project-domain conflation as KF-SC-01.

### KF-SC-03 — Disposable diagnostic chat was misclassified as canonical persistent interaction

```text
Evidence type       OBSERVED_FAILURE
Detection           LATER COLLABORATION REVIEW + POST_HOC_AUDIT
Primary evidence    docs/checkpoints/269_codexless_read_path_verified_continuity_reconciled_for_chatgpt_12_handoff.md
Supporting evidence docs/research/107_post_outage_repository_integrity_recovery_audit.md §12
```

A fresh Codexless plug-in validation chat was initially promoted into the persistent interaction-session sequence as canonical `chatgpt-12`. Later review established that it was a disposable test interaction and that the canonical persistent conversation had remained `chatgpt-11` at the checkpoint boundary.

The technical read-path result stayed valid; the **identity/scope classification** of the interaction was wrong.

## 9. Continuation / resume

### KF-CR-01 — Abnormal interruption left intended-versus-completed transition ambiguous

```text
Evidence type       OBSERVED_RECOVERY_EVENT
Detection           OWNER_REQUESTED_AUDIT + POST_HOC_AUDIT
Primary evidence    docs/research/107_post_outage_repository_integrity_recovery_audit.md
Observed period     2026-08-31 to 2026-09-01
```

A prolonged ChatGPT incident interrupted a multi-step repository task after Research 106 and Specification 025 were committed but before implementation, verification and canonical reconciliation.

The recovery process could not safely infer completion from conversational intent. It had to reconstruct:

```text
last trusted durable boundary
what commits/files actually completed
what the staged plan intended next
which inconsistencies were expected/deferred vs. new defects
```

No wrong resume action is preserved because the owner stopped and required the audit first. The event still demonstrates that continuation state can become ambiguous after abnormal interruption unless durable completed-vs-intended state is reconstructed.

### KF-CR-02 — Nested route / return target remains prose-heavy and machine-flat

```text
Evidence type       STRUCTURAL_GAP_NOT_FAILURE
Detection           OWNER/CHATGPT ARCHITECTURE AUDIT
Primary evidence    docs/OPEN_ARCHITECTURE_BACKLOG.md AB-025
Current example     Source Vault -> Research 113 -> Research 117 -> nested document/image work
```

`docs/current_routing.json` carries one current boundary but not the complete parent route, pause reason, return condition or exact resume target for nested work.

The repository preserves these relationships in prose/checkpoints well enough that no independently verified wrong return decision is recorded in this corpus yet.

**Do not count this entry as an observed resume failure.** It is retained because the structural gap is real and should shape baseline tests without inflating historical failure prevalence.

## 10. Compression / synthesis / transcription

### KF-CS-01 — Semantic summaries preserved decisions but lost implementation fidelity during integration

```text
Evidence type       OBSERVED_FAILURE
Detection           HUMAN_REVIEW + POST_HOC_AUDIT
Primary evidence    docs/research/088_integrated_cockpit_fidelity_failure_and_source_of_truth_recovery_audit.md
```

The semantic summaries were broadly correct about selected Cockpit concepts, yet were not sufficient to reproduce exact implementation-level visual/behavioral fidelity. The integrator re-authored accepted components from prose and produced a product that the owner immediately judged inconsistent with the previously designed Cockpit.

The corpus records the compression boundary failure, not the later accepted recovery manifest as a prescribed solution.

Cross-label: `REQUIRED_AUTHORITY_SOURCE_SELECTION`.

### KF-CS-02 — Raw metadata inventory was distorted in durable summary transcription

```text
Evidence type       OBSERVED_FAILURE
Detection           POST_HOC_AUDIT
Primary evidence    docs/research/107_post_outage_repository_integrity_recovery_audit.md §7
```

The authoritative raw workflow output reported one set of metadata counts. Research 106 contained materially different counts, and the closed MC-0008 summary had a smaller mismatch.

The summary error did not overturn the high-level conclusion, but it proves that durable synthesis can preserve interpretation while corrupting supporting quantitative details.

Cross-label: `STALE_CONVENIENCE_DERIVED_VIEW`.

### KF-CS-03 — "Full" verification label did not match tests actually executed

```text
Evidence type       OBSERVED_FAILURE
Detection           POST_HOC_AUDIT
Primary evidence    docs/research/104_repository_information_architecture_and_exhaustive_knowledge_routing_refinement.md §12
Boundary evidence   docs/checkpoints/266_repository_information_architecture_and_exhaustive_knowledge_routing.md §10
```

A workflow intended and reported as a full Cockpit V3 gate executed only 16 tests instead of the expected 78 because a quoted glob was passed literally.

Observed consequence:

```text
workflow/status said full
    !=
full verification evidence actually produced
```

This is an evidence-summary/claim-fidelity case rather than a retrieval miss.

## 11. Public / private continuity boundary

### KF-PP-01 — Private continuity state lagged later public Codexless evidence

```text
Evidence type       OBSERVED_FAILURE
Detection           HANDOFF/RECOVERY AUDIT
Primary evidence    docs/checkpoints/269_codexless_read_path_verified_continuity_reconciled_for_chatgpt_12_handoff.md
Supporting evidence docs/research/107_post_outage_repository_integrity_recovery_audit.md §6
```

The public project had advanced through later Codexless setup/read-path evidence while private `CURRENT_PRIVATE_STATE` still described older tunnel/plugin state.

Observed consequence: public and private continuity surfaces no longer represented the same synchronization boundary.

The corpus does not infer that private freshness should be copied into public state or that public state was substantively wrong.

### KF-PP-02 — Private synchronization-pointer requirement was dropped during specification promotion

```text
Evidence type       OBSERVED_NEAR_MISS
Detection           POST_HOC_AUDIT
Primary evidence    docs/research/107_post_outage_repository_integrity_recovery_audit.md §10
Source architecture docs/model_collaboration/threads/MC-0008/RESOLUTION.md
```

MC-0008 accepted a minimal private-side pointer recording the public boundary last reconciled against. Specification 025 preserved private integrity statuses but omitted the synchronization pointer itself.

The omission was detected before the integrity implementation completed. It is therefore a cross-boundary contract-loss near-miss, not a proven later stale-state event independent of KF-PP-01.

## 12. Latent known-risk / reopen-trigger activation

### KF-KR-01 — Previously documented escalation triggers were rediscovered only after live pressure appeared

```text
Evidence type       OBSERVED_PATTERN_COMPOSITE
Detection           OWNER_PATTERN_RECOGNITION + REPOSITORY AUDIT
Primary evidence    docs/OPEN_ARCHITECTURE_BACKLOG.md AB-027
Supporting evidence docs/foundations/014_knowledge_preservation_architecture_and_evolution.md
                    docs/research/064_rapid_iteration_repository_preservation_audit_and_checkpoint_hygiene.md
                    docs/research/103_repository_knowledge_discoverability_and_risk_scaled_verification_audit.md
                    docs/research/104_repository_information_architecture_and_exhaustive_knowledge_routing_refinement.md
```

Earlier project records explicitly deferred stronger knowledge machinery while naming triggers such as unreliable map maintenance, discoverability failures, prose dependency pressure, costly reconciliation and multi-contributor coordination pressure.

Later Research 103 observed concrete discoverability pressure after the owner raised the problem. AB-027 records the broader recurring pattern: foresight existed, but escalation conditions were scattered and often rediscovered only after a live symptom was independently noticed.

This is a composite pattern. It should not be interpreted as one experimentally isolated failure event.

## 13. Cross-case observations from V0.1

The corpus already supports several distinctions that should survive into blind baseline design:

```text
durable knowledge loss
    is uncommon in these cases

knowledge exists but routing/view is stale
    repeatedly observed

knowledge exists and is linked but governing procedure is not activated
    observed in at least two distinct task families

semantic summary is correct at a high level but insufficient for exact fidelity
    observed

promotion/synthesis can lose parts of source evidence or contract
    observed

some important architecture concerns remain structural gaps without a proven wrong outcome
    especially deterministic nested resume
```

A future baseline must therefore avoid scoring all failures as "could the model find the file?".

## 14. Evidence-strength limits

This V0.1 corpus is intentionally not balanced and should not be treated as a statistical sample of all project work.

Important limitations:

```text
owner-caught incidents are overrepresented because they are more likely to become durable records
successful silent retrieval/dispatch events are not sampled here
some cases share the same broader incident and are explicitly marked as such
several classes have only one clean real exemplar
no prevalence/frequency claim follows from the number of corpus rows
no architecture effectiveness claim follows from a historical fix being present in the source record
```

The next baseline design should preserve these limits.

## 15. Freeze rule before blind baselines

Before creating test prompts or mechanism-specific variants, this V0.1 corpus should be treated as the source-case freeze.

Any later constructed adjacent case must:

```text
name its parent corpus case
preserve the failure mechanism while changing surface wording/context
remain marked CONSTRUCTED rather than historical
avoid naming or implying the preferred remedy in the task prompt
```

The evaluator may know the source evidence. The tested fresh collaborator should receive only the task/reconstruction surface appropriate to that scenario, not this entire evaluator corpus by default.

```text
FAILURE_CORPUS_VERSION=0.1
HISTORICAL_CASE_ROWS=21
STRUCTURAL_GAP_ROWS=1
TARGET_ARCHITECTURE_REMEDIES_ENCODED=false
WITHHELD_OWNER_SOURCE_USED=false
NEXT=BLIND_BASELINE_PROTOCOL_AND_SCENARIO_SELECTION
```