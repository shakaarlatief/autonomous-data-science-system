# Validation 278: Runtime Bridge guarded Git recovery and R0-P03 S1 A2 evidence publication

**Date:** 2026-10-28
**Status:** PASS / MANAGED PREVIEW.83 V2 VERIFIED AND ACTIVATED / REAL GUARDED COMMIT AND PUSH RESTORED
**Scope:** Record the observed recurring semantic Git transaction timeouts, exact source-level diagnosis, failed first managed-release candidate, corrected immutable V2 release, controlled activation, first live rollback witness and full public Research 609–611 commit/push acceptance.
**Authority:** Infrastructure and publication evidence only. This validates neither independent non-arm reviewer/challenger identity nor source-adjudication authority, protected report custody, future blind-author access exclusion, any historical source admission, S3 author-world freeze, reference gold or B0–B4 scoring. The original Checkpoint 898 and Specification 028 remain unchanged.
**Prior evidence:** Validation 127, 158, 210, 251, 263 and 275–277; Research 606–611; `docs/local_execution/OPERATIONS.md`.

## 1. Prior incident, current reproduction and actual causal scope

Research 609–611 remained locally validated but uncommitted after multiple guarded `codex.git_commit_paths` calls failed with internal errors and/or command/exec deadline expiry. Each uncertain attempt was reconciled before further mutation: before recovery, local public HEAD was `36fd56cf3dd0e0cf06902c8affd16928926395bd`, GitHub agreed, staging was empty, and all intended source-free work remained as uncommitted files. Reducing commit size and an ordinary managed restart did not cure the failure.

The repository's earlier Validation 263 described a similar 2026-10-18 semantic Git preflight timeout corrected by a managed preview.82 release that increased the read-only preflight budget. The **new** problem differs: the installed `SemanticGitService.commitPaths` made many separate read-only Git calls through the Codex App Server command sandbox. Individual trivial Git observations were successful but Runtime Bridge command round trips were observed at approximately 18–25 seconds. Seven such Git checks executed inside **one** Python process in approximately 0.42 seconds, whereas one enclosing Codex command round trip was approximately 20 seconds. This supports the repeated sandbox initialization/transport overhead as the immediate transaction timeout mechanism; it does **not** establish an underlying Codex provider/process root cause.

An attempted sandboxed `git add -n` was separately denied at `.git/index.lock`. That is an intended prohibition and is not the repair mechanism. No global Git permission, filesystem ACL, sandbox profile, tunnel identity, credential or repository trust policy was weakened.

## 2. Purpose-specific source repair and security constraints

The previous installed server was `0.1.1-preview.82-semantic-git-readonly-preflight-budget`. The repair was packaged as a separate, fixed release candidate rather than overwriting live source. Its functional change is narrow:

- **Only** inside `commitPaths`, route an explicit allowlist of the transaction's fixed, read-only Git observations through the existing server-owned bounded host-Git process substrate. This avoids repeated Codex command sandbox launches for each preflight.
- Retain exact registered workspace authority, `expectedHead`, current branch/upstream/remote validation, protected-path rejection, no transient Git state, empty initial staging index, declared-path change checks, exact staging, staged whitespace/diff check, postcommit parent/equality verification and failure-atomic index rollback.
- Reject an unrecognized, injected or malformed host-read command rather than broadening the allowlist. Keep all other semantic Git operations and the ordinary Codex command lane on their existing paths; no caller-selected cwd, executable, Git refspec or host process is added.
- Preserve the existing rule that a failed transaction may not erase or reset an undeclared staged path merely to make automatic rollback appear successful.

A focused simulation exercised successful commit, protected-path refusal, unexpected staged-path hold, declared-scope rollback, injected branch rejection and uncertain commit. The installed runtime was not changed by this simulation.

## 3. Immutable V1 candidate and managed regression rejection

The initial release bundle was saved and published in the separately authorized private runtime source repository as:

```text
PRIVATE_V1_SOURCE_COMMIT=47d9e4a79159dc8a00f591ccac5cf12cbc310eed
PRIVATE_V1_PARENT=a489e81535f1ec5b94b8122f91c86ca5ea155ba4
PRIVATE_V1_RELEASE_ID=semantic-git-host-readonly-commit-v1
```

After the owner performed a source-preserving `git pull --ff-only origin main`, the bundle's four payload hashes and private repository synchronization were verified. `codex.runtime_release prepare` returned `prepared`; `publish` returned durable `failed` with `errorCode=RUNTIME_RELEASE_REGRESSION_FAILED`. The release gate did **not** activate V1.

An isolated staged-copy reproduction identified that an existing `commit-index-recovery-release-smoke.mjs` assertion expected the host process log to contain **only** the index-restoration mutation. The new design intentionally includes additional host read-only preflights in that log. The test's expectation was too broad. An independent source-level reproduction also confirmed the flexible-authority test depended on the complete staged source tree, rather than only a minimal file subset.

The correction retained the security checks and revised the regression to assert **only the exact authorized mutating commands**. The local source-free focused commit test, index-recovery smoke and 13-case flexible-authority regression then passed. This did not legitimize any arbitrary host command.

## 4. Immutable V2 release, source synchronization and activation

A separate V2 bundle was prepared, with a corrected release identity/manifest and the revised index-recovery regression. Its private Git-object publication used an exact-parent, non-force ref update, not an unguarded local Git commit:

```text
PRIVATE_V2_SOURCE_COMMIT=43742ae8250c0dd748719bd0027a25e892d7d784
PRIVATE_V2_PARENT=47d9e4a79159dc8a00f591ccac5cf12cbc310eed
PRIVATE_V2_RELEASE_ID=semantic-git-host-readonly-commit-v2
TARGET_VERSION=0.1.1-preview.83-semantic-git-host-readonly-commit-v2
TARGET_SURFACE=codexless-public-preview-v2
TARGET_TOOL_COUNT=179
PAYLOAD_FILE_COUNT=4
MANIFEST_SHA256=21136c506d33dfa5d0c0ab76b5671f3c726c2e1e156460fdd683a3156e1f97c4
```

The owner's first V2 `git pull --ff-only` was safely aborted by Git because the six bundle files already existed as untracked local copies from authoring. The coordinator verified **all six** against exact expected SHA-256 hashes, copied them to an independently checked temporary backup, removed only those duplicate untracked copies and verified the original private Git HEAD and an empty clean index/worktree. The owner then performed the exact ordinary fast-forward pull successfully to `43742ae8`.

The bridge independently verified local HEAD/origin parity, clean private checkout and all release payload hashes. The managed release events were:

```text
PREPARE=prepared
PUBLISH_OPERATION_ID=rm_5de1311cfc08fa7f81a07200229764ec
PUBLISH_STATUS=succeeded
POSTPUBLICATION_VERIFY=verified
POSTPUBLICATION_MISMATCH_COUNT=0
ACTIVATION_OPERATION_ID=rm_832ca27adc9a0e08935792fc7e7509f4
ACTIVATION_STATUS=succeeded
ACTIVATION_RECOVERY_ATTEMPTED=false
LIVE_PUBLIC_SERVER_VERSION=0.1.1-preview.83-semantic-git-host-readonly-commit-v2
LIVE_SEMANTIC_GIT_SHA256=9e9e856774c873900f174f3e7a5904bbd758f2898dcef69d3236b52720fa5f2a
LIVE_SURFACE_CONTRACT_SHA256=b173972233495f15a364757c47cf170511570c25192ddbdd442117e59eededd3
```

The target version and exact source hashes were read back from the **live installed runtime** after the managed restart. No manual executable replacement or arbitrary process termination was used.

## 5. Live guarded Git rollback and successful publication

The ADS public checkout began at `36fd56cf3dd0e0cf06902c8affd16928926395bd`, with exactly 16 intended pending Research 609–611/Validation 275–277 files or changes and an empty Git index. The live repaired `codex.git_commit_paths` call successfully passed the prior timing bottleneck, staged the declared files, and reached `git diff --cached --check`.

The staged diff correctly rejected the source-free 193-byte intentional CRLF text fixture as apparent trailing whitespace under its existing `-text` attribute. The guarded commit **returned `GIT_COMMIT_PATHS_DIFF_CHECK_FAILED` and `indexRestored=true`**, proving that the index rollback path operates after real staging. A strictly file-scoped `.gitattributes` correction made the fixture rule `-text whitespace=cr-at-eol`; the original SHA-256 `8af9f2f5ea35071e1e8db50e0f467188a63b0a2ad390e5a3eba3853b109603fb` and size 193 were reverified unchanged. All other whitespace checks remained in force.

The final precommit checks passed:

```text
FOCUSED_REGRESSION_TESTS=42_PASS
PUBLIC_REPOSITORY_INTEGRITY=PASS
INDEX_BEFORE_COMMIT=EMPTY
SOURCE_FREE_TEXT_PNG_FIXTURE_HASHES=UNCHANGED
CRLF_ATTRIBUTE=TEXT_UNSET_WHITESPACE_CR_AT_EOL
```

The repaired guarded commit then succeeded with the exact **16** declared paths:

```text
PUBLIC_COMMIT_PARENT=36fd56cf3dd0e0cf06902c8affd16928926395bd
PUBLIC_COMMIT_SHA=13f02e64d4ef9cfa36701502e93212924635d3c9
GIT_COMMIT_PATHS_EXIT_CODE=0
GIT_COMMIT_PATHS_POSTFLIGHT_OK=true
GIT_COMMIT_PATHS_INDEX_CLEAN_AFTER=true
```

The guarded `codex.git_push_ff_only` subsequently returned `exitCode=0`, `retried=false`, `PUBLIC_REPOSITORY_INTEGRITY=PASS`, `trackedWorkingTreeCleanAfter=true`, `postflightOk=true`, and matched local HEAD and remote-tracking HEAD at the exact new commit. An **independent GitHub API read** confirmed `refs/heads/v1-source-vault-bootstrap-resume` pointed to `13f02e64d4ef9cfa36701502e93212924635d3c9`.

## 6. Operational lesson and scoped scientific holds

Do not respond to a guarded commit timeout with repeated uncertain mutations, larger arbitrary deadlines, raw sandboxed `git add`, permission broadening, or a claim that prior research failed. First reconcile HEAD/index/remote; inspect the installed source and prior release records, measure inner Git time separately from outer Codex command-lane latency, and repair the smallest purpose-specific boundary that the evidence supports. Maintain exact hash-bound release bundles, stage/live regressions, managed activation, failure recovery and real exact-path postflight before declaring the infrastructure restored.

Research 609–611 and Validation 275–277 are now **published**; prior 'publication pending' statements in their historical records describe the state when those records were authored, not the current state. The public project does **not** automatically gain scientific actor independence from this repair.

```text
VALIDATION_278=MANAGED_RUNTIME_PREVIEW83_AND_REAL_GUARDED_GIT_PUBLISH_PASS
PUBLIC_COMMIT=13f02e64d4ef9cfa36701502e93212924635d3c9
PUBLIC_GITHUB_REF=CONFIRMED_EQUAL
RESEARCH_609_610_611=COMMITTED_AND_PUBLISHED
REAL_HISTORICAL_SOURCE_DELIVERY=ZERO
REAL_REVIEWER=NOT_ADMITTED
REAL_CHALLENGER=NOT_ADMITTED
A2_R05_REAL_CONFIDENTIAL_CUSTODY=NOT_QUALIFIED
A2_R07_AUTHOR_ACCESS_DENIAL=NOT_TESTED
S3_AUTHOR_WORLD=WORLD_UNFROZEN
S4_HIDDEN_GOLD=NONE
S4_B0_B4_SCORING=NOT_STARTED
CHECKPOINT=898_UNCHANGED
SPECIFICATION_028=UNCHANGED
```
