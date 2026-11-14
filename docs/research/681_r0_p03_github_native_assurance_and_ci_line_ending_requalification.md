# Research 681: GitHub-native source assurance, provider check-run evidence and cross-platform CI qualification

**Date:** 2026-11-14
**Status:** GITHUB_NATIVE_COMMIT_AND_CHECK_API_EVIDENCE_OBSERVED / ORIGINAL_UNSIGNED_COMMITS / PREEXISTING_WINDOWS_CI_FAILURE_DIAGNOSED_AND_REPAIRED / FOUR_CROSS_PLATFORM_CHECKS_GREEN / AGENT_IDENTITY_AND_ORIGINAL_CONNECTOR_TRANSPORT_UNQUALIFIED
**Scope:** Investigate whether the actually connected GitHub/Runtime Bridge surfaces can independently prove original actor identity, actual connector transport and external provider-run execution. Act on an unexpected CI failure disclosed by the native API, preserve historical byte-pinned source identity, restore cross-platform CI and identify the precise J2 source and assurance implications.
**Authority:** Exposed and unscored architecture/custody evidence under Research 512 section 9, Research 673, the four owner-accepted experiment-only J1 inputs in Research 676, and Research 678-680. No new accepted J1, new qualified RELATIONAL J2, provider-verified original D1 connector transport, governing J3 completion, formal Research 513 comparison, production branch governance or physical target selection.
**Repository:** shakaarlatief/autonomous-data-science-system
**Branch:** v1-source-vault-bootstrap-resume
**Starting current head:** 511224a037bf63031ead0eda61754702361eebd7
**LF-preservation repair:** 66076d3d889645ca43f25d892dbf75a2f8355474
**CI coverage repair:** 36ab6cd33a31d579c68b6b814ca70b1fae59fc40
**Validation:** 378. **Checkpoint:** 942. **Collaboration:** MC-0030 Message 095.

## 1. Direct provider-authored data actually inspected

The investigator used the connected, read-only Codexless GitHub App REST adapter, not generic Git text or a self-authored claim, for:

- GET /repos/shakaarlatief/autonomous-data-science-system/git/commits/{sha}: GitHub's native Git commit and verification field.
- GitHub-native check-runs-for-ref, check-run details, annotations and workflow-run GET operations, including provider-generated run and check IDs.
- GitHub-native branch protection read for the exact registered development branch.
- GitHub Actions job logs through the connected GitHub job-log reader for failed Windows checks.

The API responses come through an authenticated GitHub App integration and have returned provider resource identities. This is an **online, source-provider API observation**, not a detached signed data packet that remains independently authenticated when copied into an ordinary Markdown document. The URLs/IDs can be queried again while GitHub still retains their resources. This document and any model-authored summary are DERIVED evidence carriers, not replacement natural-owner or GitHub-provider records.

The following original Git commit IDs were queried through GitHub's native Git commit endpoint:

| Event | Exact Git SHA | GitHub verification |
| --- | --- | --- |
| Historical original D1 Message 018 action | cd0cf087a4d0ddb30920a8c753e478da8f92295c | verified=false; reason=unsigned; signature=null |
| Claude's historical natural-owner response Message 091 | 90dc870cd059fa555299505b7c7f8110dadb47f4 | verified=false; reason=unsigned; signature=null |
| ChatGPT's genuine forward at-action source record | 131c54a4aec9f8733af35b1c90e8b16a7c9919a5 | verified=false; reason=unsigned; signature=null |
| Previous typed J2 port Checkpoint 941 | 511224a037bf63031ead0eda61754702361eebd7 | verified=false; reason=unsigned; signature=null |
| CI repair workflow update | 36ab6cd33a31d579c68b6b814ca70b1fae59fc40 | verified=false; reason=unsigned; signature=null |

These are **specific observed unsigned commits**, not a claim that every Git commit is unsigned or that GitHub lacks signing support. GitHub's author and committer metadata and normalized GitHub user association indicate an account associated with the commit, but do NOT distinguish Claude from ChatGPT or establish the actual tool/connector that performed the write. A Git commit being unsigned does not imply its contents or parent are invalid; it means GitHub's verified commit-signature mechanism did not attest this commit.

The development branch's live provider-governance read reported protected=false, codexlessSafetyBaseline=false, profileId=null, policy=null at HEAD 66076d3d. These facts mean the presently observed branch is not protected by that branch-protection endpoint. Do not infer all other GitHub ruleset settings or legal/project authority from this single endpoint. CI outcomes are observed verification facts, not demonstrated mandatory pre-push policy enforcement.

## 2. A live counterexample to local-pass -> external CI-pass inference

The source-bound Checkpoint 941 work finished with local tests and a successful Git push. GitHub's native check-runs-for-ref response subsequently revealed **eight completed checks**, of which **two were failures**:

    commit 511224a037bf63031ead0eda61754702361eebd7
    failure A: validate-collaboration-state (windows-latest)
               GitHub check run 132549849947
               workflow run 43628566028
    failure B: repository-integrity (windows-latest)
               GitHub check run 132549849558
               workflow run 43628566327

The other six GitHub checks on that commit succeeded, including the corresponding Ubuntu collaboration-state and repository-integrity checks.

GitHub Actions job logs show that the Windows collaboration-state validator exited 1 because it classified the two preserved MC-0030 Message 063 historical files as an unexempt duplicated durable message number. The Windows aggregate repository-integrity job ran its 40 local regression tests successfully, then failed in the model-collaboration-state component with precisely the same historical Message 063 mismatch. These are verified job-log observations, not inferred causes from a red icon.

The message-identity guard pins the two historical MC-0030 Message 063 original SHA-256 values and accepts exactly this preexisting two-file collision. The files are intentionally not renamed, rewritten or expanded into a broad exemption. GitHub Windows checkout can materialize LF Git text blobs with CRLF bytes when no explicit per-file checkout rule is defined. The guard hashed raw worktree bytes, so checkout line-ending conversion changed the worktree SHA even when the original committed text was identical.

An actual source-specific reproduction was performed in a sandboxed, temporary repository-local directory:

    Original LF files in existing worktree: collision guard PASS
    Identical content represented as CRLF in temporary checkout: duplicate identity FAIL

This demonstrates the relevant failure mode. Both immutable Git source blob SHA-256 values remained identical to the historical original pins; no genuine new duplicate or historical content corruption was found.

## 3. Targeted repair without weakening the source identity rule

First commit 66076d3d889645ca43f25d892dbf75a2f8355474 changed only:

- .gitattributes: explicitly assign -text to the two exact original MC-0030 Message 063 paths, preserving literal Git source bytes across Windows/POSIX checkouts.
- tests/unit/test_model_collaboration_message_identity.py: add a regression verifying both -text attributes, actual worktree/source blob byte equality, original SHA-256 identities and absence of CRLF conversion.

The validator's original exact byte hash, two-file exception scope and duplicate rejection were **not modified**. The original historical source files themselves were **not modified**. Test cases still reject a third Message 063 claimant and any substantive modified original content.

Running the test file with pytest's default Windows host TEMP under the constrained Runtime Bridge produced five temporary-directory PermissionError setup errors. A bounded rerun with --basetemp inside the trusted repository passed **7/7** tests, after which that temporary material was removed. The host-temp exception was environment access, not a message-validator assertion failure.

The initial two-file repair commit did not trigger relevant GitHub checks because the path-filtered workflows did not watch .gitattributes or this test file. This is an independent CI-coverage omission, not evidence that the repair passed CI.

Second commit 36ab6cd33a31d579c68b6b814ca70b1fae59fc40 changed only:

- .github/workflows/model-collaboration-state.yml
- .github/workflows/repository-integrity.yml

Both workflows now trigger on .gitattributes and tests/unit/test_model_collaboration_message_identity.py in push and pull_request path filters, and execute that exact regression in their existing Ubuntu/Windows validation steps. Their operating-system matrices, existing checks and permission declarations were not removed.

A focused combined local test run of model collaboration, message identity and repository-integrity suites passed **73 tests**, with repository-local bounded pytest temp. The pushed second commit independently triggered the following four GitHub-native check runs:

| GitHub check | Check ID | Result |
| --- | ---: | --- |
| validate-collaboration-state (ubuntu-latest) | 132554259150 | completed, success |
| validate-collaboration-state (windows-latest) | 132554258967 | completed, success |
| repository-integrity (ubuntu-latest) | 132554258768 | completed, success |
| repository-integrity (windows-latest) | 132554258516 | completed, success |

Workflow run 43629997613 (Model collaboration state) and workflow run 43629997620 (Repository integrity), both for head 36ab6cd3, reported event=push, status=completed, conclusion=success, runAttempt=1. Both Windows check-run details were separately reread: conclusion=success, annotationsCount=0, app slug=github-actions, app ID=15368, with exact recorded head SHA matching the repair commit.

Provider resource links:

    https://github.com/shakaarlatief/autonomous-data-science-system/actions/runs/43629997613
    https://github.com/shakaarlatief/autonomous-data-science-system/actions/runs/43629997620

This is actual provider-native evidence that the two workflows executed and passed on both operating systems. It does not identify or authenticate the agent that authored the commit.

## 4. J2 assurance: what is verified and what is not

Four important source facts must not be collapsed:

**A. Git object existence, content and ancestry.** Exact Git source objects and GitHub commit resources establish commit SHA, parent, paths and content. The natural owner of those OBSERVABLE facts is the Git object store/host provider. No additional model-written COVERS declaration is needed for those exact facts themselves.

**B. An agent's source-authored statement.** The source record can preserve an actor's stated intent and claimed COVERS at action time, with an exact Git carrier and provenance, but Git author fields and the resulting source tree do not independently authenticate the actual model session or connector operation. This remains a RELATIONAL candidate requiring governing effect and source-owner qualification.

**C. GitHub-native workflow execution.** GitHub Actions run and check-run APIs independently report particular CI jobs, Git commit association, conclusion, provider app identity and timestamps. They can support a J2 EPHEMERAL fact that a named GitHub Actions check executed with a stated conclusion. The API responses are dynamically re-queryable and mutable over time (e.g. reruns), so evidence needs exact run/check ID, attempt, ref, retrieval time/provenance and source-relative freshness policy. A copied model-authored Markdown statement is not independently signed provider evidence.

**D. Underlying commit writer/connector identity.** These exact commit and CI API records do not identify which model session or client used a specific transport to perform the original GitHub write. The historical source text's Claude-side connector attestation remains a single source claim family; the original D1 provider transport is still UNKNOWN. No new E01 natural-owner COVERS relation, independent agent credential or detached provider-specific transport receipt was obtained.

A provider's GitHub Actions check conclusion must never be substituted for the original E01 TRANSPORT_ATTESTED_GITHUB_CONNECTOR or used to promote the old historical source owner's CANNOT_ATTEST to a PASS.

## 5. Engineering design consequences, not a locked physical selection

The evidence supports a typed J2 source interface with independently source-verifiable Git observations; independently queryable provider-execution check receipts for specific events; explicit RELATIONAL natural-owner provenance bound to exact accepted effects; separate source-owner identity, assurance and freshness policies; and bounded UNKNOWN where an adequate trust root or provider native record does not exist.

For future action transport and owner authentication, feasible design candidates include repo-local signed commits/declarations, provider-owned API/audit events tied to an authenticated client or app, signature-verifiable execution receipts, a dedicated actor-to-effect admission service, or a policy-scoped combination. None has been demonstrated in this source world as an authenticated Claude-vs-ChatGPT action verifier. They must be assessed against actual provider availability, threat model, trust roots, recovery, authorization and cost before selection.

The same applies to branch governance. The observed development branch is unprotected; enabling mandatory CI checks/rulesets or changing branch and merge procedures may be valuable, but is a separate consequential governance and working-method decision, not automatically authorized by this research. No level of the architecture is frozen.

This discovery also creates a generalized testing principle: claims about CI and external actions require *provider-source checks*, not just local test counts and push success. Source-relative external status may reveal contradictions and should trigger investigation rather than silently adopting the previous local PASS.

## 6. Decision and next boundary

The historical original D1 effect set remains the four exact owner-accepted experiment-only J1 inputs. Original D1_AMEND remains unchanged, Message 091 CANNOT_ATTEST remains the terminal first-hand historical response, newly qualified RELATIONAL J2 remains zero, and original E01 J3 stays HOLD. Formal R0-P03 remains INCOMPLETE and no physical target has been selected.

The next useful boundary is to specify and test an actual trust-root and provider-receipt admission protocol for accepted effects, including whether stronger actor attribution is physically available or whether honest UNKNOWN and appropriately scoped alternative source worlds are required. This requires no automatic re-asking of Claude, no unapproved acceptance of a new effect and no artificial requirement that every provider use Git.

    RESEARCH=681
    NATIVE_COMMIT_SIGNATURE_SAMPLES=5_UNSIGNED
    ORIGINAL_CI_CHECKPOINT941=2_WINDOWS_FAILURES
    CI_REPAIR_COMMITS=66076d3d,36ab6cd3
    REPAIR_CI_CHECKS=4_COMPLETED_SUCCESS
    GITHUB_ACTIONS_NATIVE_CHECK_RECEIPTS=AVAILABLE_FOR_CI_OUTCOMES
    ORIGINAL_D1_CONNECTOR_TRANSPORT_PROOF=UNAVAILABLE
    INDEPENDENT_ACTOR_IDENTITY=UNAVAILABLE_FROM_INSPECTED_EVIDENCE
    P03_EXPERIMENT_ONLY_ACCEPTED_J1=4
    NEW_RELATIONAL_J2_QUALIFIED=0
    ORIGINAL_E01_J3=HOLD
    FORMAL_R0_P03=INCOMPLETE
    PHYSICAL_TARGET_SELECTED=false
    NEXT=TRUST_ROOT_AND_PROVIDER_EXECUTION_RECEIPT_ADMISSION_PROTOCOL_DESIGN
