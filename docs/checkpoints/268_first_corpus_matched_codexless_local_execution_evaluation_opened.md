# Checkpoint 268: First Permanent Corpus Matched, Codexless Local Execution Evaluation Opened

**Date:** 2026-08-31  
**Branch:** `v1-source-vault-bootstrap-resume`  
**Status:** ACTIVE CONTINUATION BOUNDARY

## What is frozen at this checkpoint

The first permanent Source Universe bootstrap has advanced through clean registry creation and prospective corpus comparison without beginning source ingestion.

Verified state:

```text
permanent Source Registry           CREATED / MIGRATED / VERIFIED
Alembic head                        0003_source_universe
SQLite table count                  33
first permanent corpus              VU Amsterdam Machine Learning
prospective comparison outcomes     20
MATCH                               20
DIFFERENT_ARTIFACT                  0
MISSING_LOCAL_SOURCE                0
ADDITIONAL_LOCAL_SOURCE             0
source ingestion                    NOT STARTED
independent encrypted backup        NOT YET VERIFIED
clean recovery proof                NOT YET COMPLETED
Course 2                            BLOCKED
Cockpit                             PAUSED at frozen frontend state
```

The 20/20 byte-level comparison does not rewrite or upgrade the manifest's existing `CONFIRMED`, `POSSIBLE`, or `UNVERIFIED` association judgments. Those provenance semantics remain preserved exactly.

The public-safe comparison evidence is:

```text
docs/source_universe/validation/004_permanent_first_corpus_prospective_compare_all_match.md
```

## Why Source Vault ingestion is temporarily paused here

The remaining Source Vault workflow is increasingly machine-local. The current collaboration loop requires ChatGPT to emit commands, the project owner to run them locally, and the resulting output to be relayed back into the conversation.

A candidate open-source bridge, Codexless, may allow the active ChatGPT collaboration surface to perform bounded local project inspection, command execution, guarded edits and verification directly while continuing to use Codex only when agent-level work is actually needed.

Because the permanent corpus has not yet been ingested, this is a clean and reversible point to evaluate that execution mechanism without placing the already-verified Source Registry or original educational corpus at unnecessary risk.

The governing evaluation record is:

```text
docs/research/098_codexless_local_execution_bridge_evaluation.md
```

## Candidate status

Codexless is **not accepted** at this checkpoint.

Current classification:

```text
CANDIDATE / EVALUATION OPENED
```

Upstream is an independent Technical Preview. Its documented security model and Plus/Pro real-machine testing are useful evidence but do not replace ADS's own bounded evaluation.

The first evaluation intentionally excludes browser automation.

## Evaluation boundary

The intended sequence is:

```text
1. verify Node.js >= 22
2. verify working local Codex installation/runtime
3. review selected Codexless release/tag and installer/security boundary
4. verify current ChatGPT account exposes the required Developer Mode / App connection path
5. select authenticated tunnel mechanism
6. install only after the above checks pass
7. run Codexless doctor against ADS
8. prove harmless read-only local operations
9. prove one controlled disposable write/cleanup operation
10. classify Codexless as accepted, read-only-only, deferred, or rejected
11. only then resume permanent Source Vault ingestion or explicitly return to the prior manual/agent execution path
```

No secret, tunnel token, local credential, browser profile or source binary belongs in public Git.

## Authority principle

If adopted, Codexless is an execution bridge, not a new ADS authority layer.

```text
public repository              project-development authority
private companion              durable private continuity complement
.ads-private                   machine-local operational configuration
Source Registry / Vault        canonical source substrate
Codexless                      replaceable local execution transport only
```

Local Codex authority remains the ceiling for borrowed execution capabilities. ADS should narrow authority further where possible rather than granting generic machine control.

## Resume rule if the evaluation fails

The Source Vault bootstrap remains fully resumable without Codexless.

Return to:

```text
permanent registry migrated / verified
20 / 20 prospective corpus MATCH
source ingestion NOT STARTED
```

Then run the already-governed ingestion, working-store audit, encrypted independent backup round trip, clean restore and restored audit through the existing manual / Codex / Claude Code execution paths.

## Exact next action

Do not ingest yet.

Proceed with the bounded prerequisite review for Research 098, starting with local Node.js and Codex runtime verification and the current ChatGPT Developer Mode / App availability check.
