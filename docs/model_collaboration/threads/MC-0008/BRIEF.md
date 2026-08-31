# MC-0008 Brief: Repository Governed-Document Metadata and Reference-Integrity Architecture

**Thread:** MC-0008  
**Date opened:** 2026-08-31  
**Review mode:** INDEPENDENT_THEN_COMPARATIVE  
**Coordination branch:** `v1-source-vault-bootstrap-resume`  
**Exact pre-proposal review target:** `7794951cbedd16f2fd1a27170946aa59b952e27a`  
**Intended reviewer environment:** fresh normal Claude Project interaction with repository access  
**Intended interaction session:** `claude-02`  
**Intended conversation title:** `02 - Repository Metadata Integrity Review`  
**Authority:** Neutral pre-proposal collaboration brief. It frames the observed repository-maintenance problem and constraints but does not freeze a solution or make the reviewer authoritative.  
**Purpose:** Obtain a genuinely independent second-model architecture proposal for repository-wide document metadata, provenance, reference integrity, live-state consistency and scalable enforcement before ChatGPT freezes or implements a candidate redesign.

## Why this review exists

ADS deliberately evolves its own development and preservation architecture when actual use exposes a new scaling failure mode.

Foundation 014 intentionally adopted lightweight, family-sensitive document metadata rather than one universal schema and explicitly deferred stronger machine-readable metadata, contradiction/staleness detection, dependency modeling and authority/supersession checks until observed maintenance pressure justified them.

That pressure now appears real. Recent repository work has exposed multiple continuity and metadata defects while the underlying substantive knowledge remained durable. Checkpoint 269 records examples including stale current-state material, a duplicate Research identity, missing Knowledge Map routing and incomplete checkpoint metadata. Research 103 and Research 104 already strengthened semantic routing, current-state ownership and narrow deterministic validation, but the repository still has several artifact families whose metadata and cross-document relationships are primarily convention-governed rather than mechanically checked.

The project owner has asked for this to be handled as the project has handled earlier scaling discoveries: reflect on the architecture, improve the method where justified, and avoid another isolated repair that merely fixes today's visible symptom.

Before ChatGPT freezes a candidate solution, the project owner explicitly requested Claude's independent ideas and criticism. This first MC-0008 phase therefore exists to reduce anchoring.

## Independence boundary

Claude's substantive architectural evidence base is the repository exactly as it existed at:

```text
7794951cbedd16f2fd1a27170946aa59b952e27a
```

Read this `BRIEF.md`, `THREAD.md`, `STATE.json` and the current collaboration inbox from the coordination branch only to locate and understand the request. For substantive repository evidence, inspect the exact frozen target above.

Do not inspect later ChatGPT candidate-design, implementation, specification or resolution artifacts before freezing the independent position. No ChatGPT implementation contract or metadata schema has been frozen for MC-0008 at opening.

Known exposure is limited to the problem/evidence summarized here and the accepted architecture already present in the frozen repository. This is intended as `BLIND_TO_CANDIDATE`, not blind to the existing system.

## Minimum governing read set

Begin from the exact frozen target and read at least:

```text
docs/foundations/014_knowledge_preservation_architecture_and_evolution.md
docs/research/103_repository_knowledge_discoverability_and_risk_scaled_verification_audit.md
docs/research/104_repository_information_architecture_and_exhaustive_knowledge_routing_refinement.md
docs/checkpoints/269_codexless_read_path_verified_continuity_reconciled_for_chatgpt_12_handoff.md
docs/README.md
docs/DEVELOPMENT_METHOD.md
docs/CONTINUITY.md
docs/CURRENT_STATE.md
docs/current_routing.json
docs/KNOWLEDGE_MAP.md
docs/checkpoints/README.md
docs/model_collaboration/README.md
docs/specifications/024_v1_model_collaboration_state_guard.md
```

Then inspect representative examples from the major artifact families and the actual validators/workflows/scripts needed to test claims. Do not trust summaries where the implementation can be inspected directly.

## Existing facts and constraints, not proposed solutions

Treat the following as problem constraints rather than a candidate design:

```text
Git + repository artifacts remain project authority.
Different artifact families legitimately serve different semantic roles.
Checkpoint metadata already has dedicated mechanical protection.
Model-collaboration state already has a schema/validator/workflow.
Current routing and Knowledge Map have narrower deterministic guards.
Several other important document families use conventions without one repository-wide integrity contract.
Historical artifacts should not be rewritten merely for cosmetic uniformity.
Current/high-authority/live-routing artifacts deserve stronger protection than low-risk historical prose.
Semantic judgment should not be automated merely because syntax can be checked.
The solution should remain proportionate to observed failures and should scale with repository growth.
```

Do not assume that the answer must be universal front matter, family-specific front matter, sidecars, a central manifest, a generated catalog, one validator, multiple validators or any particular storage format. Compare the strongest options.

## Architecture questions to answer independently

Assess at least the following.

1. **What is the actual failure model?**
   - Which metadata/provenance/reference failures are now demonstrated rather than hypothetical?
   - Which are dangerous enough to mechanize now, and which should remain human review?

2. **Artifact-family taxonomy**
   - Which repository artifact families should be governed by an explicit metadata contract?
   - Which files should remain outside that mechanism?
   - Are numbered Foundations, Specifications, Research, Checkpoints, validation/evidence records, canonical global documents, specialized ledgers/indexes and collaboration records meaningfully different classes for this purpose?

3. **Common versus family-specific semantics**
   - Is there a small common metadata kernel worth enforcing across governed documents?
   - Which fields must be family-specific?
   - How should status, authority, scope, maturity, provenance, dates, identity, supersession and change constraints be represented without creating meaningless boilerplate?

4. **Representation architecture**
   - Compare Markdown headers/front matter, sidecar metadata, central registries/manifests, generated indexes and hybrid designs.
   - Which representation best preserves human readability, Git reviewability, deterministic validation and low maintenance tax for ADS now?

5. **Reference integrity**
   - What kinds of cross-document references should be mechanically checked?
   - Consider numbered identity, filename/header identity agreement, repository paths, supersedes/superseded-by relations, governing-artifact references, exact commit refs, Knowledge Map routes and canonical current pointers.
   - How should rename/renumber/history cases be handled without erasing provenance?

6. **Dynamic canonical-state consistency**
   - `CURRENT_STATE.md` and `current_routing.json` intentionally own live state in human- and machine-readable forms.
   - What synchronization assertions are justified?
   - Should other canonical files be prohibited from duplicating volatile fields, checked for stale pointers, or handled differently?

7. **Legacy migration**
   - How should hundreds of existing documents be treated?
   - Compare immediate strict migration, active/high-authority-first migration, warning mode, migrate-on-touch and other staged approaches.
   - Define when warnings should become errors.

8. **Validator and CI architecture**
   - Should ADS have one family-aware governed-document checker, several focused validators behind an aggregate gate, generated schemas, declarative contracts or another architecture?
   - How should existing checkpoint, Knowledge Map, current-routing and collaboration-state guards compose with it?
   - How do we avoid duplicate logic and contradictory validators?

9. **Semantic limits**
   - Which properties can be proven deterministically and which cannot?
   - How should the system avoid claiming that a syntactically valid `Authority` or `Status` value is semantically true?

10. **Operational ergonomics**
    - What authoring workflow keeps new documents correct by construction?
    - Are templates/generators useful, or would they add unnecessary machinery?
    - What diagnostics should a model or human receive when a contract fails?

11. **Scaling and dependency evolution**
    - At roughly 10x the current repository size, what fails first?
    - Does this work justify a first explicit dependency graph now, or should graph semantics remain deferred?
    - What measurable trigger should cause the next architectural step?

12. **Security and trust**
    - Are there path traversal, malformed-link, untrusted-content or CI abuse considerations relevant to parsing repository metadata?
    - Keep controls proportional to the public repository threat model.

13. **Simplest strong alternative**
    - What is the strongest materially simpler architecture than your preferred design?
    - Why should ADS choose or reject it?

## Required first-phase output

Write one durable independent proposal at:

```text
docs/model_collaboration/threads/MC-0008/messages/001_claude_independent_governed_document_integrity_proposal.md
```

The message should preserve the normal collaboration provenance fields and include:

```text
exact SHA reviewed
independence statement and exposures
problem diagnosis
recommended architecture
artifact-family taxonomy
common versus family-specific metadata model
reference-integrity model
current-state consistency model
legacy migration strategy
validator/CI composition
semantic/non-automatable boundary
authoring ergonomics
rollout phases and gates
strongest failure mode of your own proposal
strongest simpler alternative
10x scaling assessment
what evidence would change your recommendation
explicit list of MUST_DO_NOW / SHOULD_DO_LATER / DO_NOT_DO items
```

Do not optimize for agreement with ChatGPT. No ChatGPT candidate has been provided for this phase.

## Comparative second phase

After Claude's independent position is durably frozen, ChatGPT will independently disposition the findings and may freeze a concrete candidate architecture. If a candidate is frozen, MC-0008 may then enter the comparative phase so Claude can see the proposal and identify convergence, disagreement, omissions and any must-fix issue before implementation acceptance.

The first message must remain unchanged as the independent record.

## Write scope

Claude may write only:

```text
docs/model_collaboration/threads/MC-0008/messages/**
```

Do not modify repository target state, canonical documentation, validators, workflows, schemas, current routing or the collaboration contract itself.

## Blocking semantics

MC-0008 blocks implementation/freeze of the new repository-wide metadata/reference-integrity architecture until the independent first-phase proposal is preserved and dispositioned.

It is not a newly discovered Source Universe data-integrity defect. The project owner has nevertheless chosen to complete this repository-preservation reflection before returning to permanent source ingestion.