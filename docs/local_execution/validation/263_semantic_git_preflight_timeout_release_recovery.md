# Validation 263: Semantic Git preflight timeout and managed release recovery

**Date:** 2026-10-18
**Status:** PASS / MANAGED V2 RELEASE VERIFIED / PUBLIC SEMANTIC COMMIT AND PUSH RESTORED
**Scope:** Preserve the observed preflight timeout, source-level diagnosis, V1 activation failure with automatic recovery, corrected V2 managed release and exact-path public ADS publication.
**Authority:** Operational evidence only. This does not select a physical architecture, qualify an independent R0-P03 reviewer, admit sources or gold, launch B0–B4 scoring, advance Checkpoint 898 or replace Specification 028.
**Prior evidence:** Research 430/519/520/580/581, Validations 127/158/206/251 and `docs/local_execution/OPERATIONS.md`.

## Reproduced failure and bounded diagnosis

The public ADS branch `v1-source-vault-bootstrap-resume` began at `27c84fdf50e4a588b82e761ff8a97fa6e269542f` with exactly three pending Research 592 paths and an empty index. The purpose-specific `codex.git_commit_paths` returned `command/exec timed out after 15000ms` on repeated calls; exact read-only postflight proved no commit, unchanged HEAD and preserved working files. In contrast, ordinary `codex.command_exec` read-only Git succeeded using explicit `timeoutMs=30000`. Ordinary sandboxed `git add` was denied at `.git/index.lock`, confirming that direct command execution is not a legitimate substitute for bounded host-backed Git mutation.

The active installed `src/semantic-git.mjs` was byte-identical to the qualified prior private runtime release payload (SHA-256 `20cdb089f9e4fa4f2d7097b28f1233f06326c0c7d665b45a925f1151db67bab9`). Its semantic Git read-only preflights defaulted to 10,000 ms and the authority executor supplied a separate 5,000 ms watchdog. The observed error therefore corresponds to a 15-second preflight boundary. Historical Research 430/580 recorded model-free command round trips near 13 seconds. This supports a locally insufficient preflight budget, without claiming a proved tunnel, Codex installation or sandbox-helper root cause.

## V1 release and failed activation

The first candidate changed exactly that read-only preflight default from 10,000 to 30,000 ms. Its synthetic test verified 4/4 entry points (fetch, pull, commit, push) without performing any mutation. The same preflight timeout prevented the private runtime semantic Git tool from committing its own repair. Following Research 520's previously qualified self-hosting precedent, the constrained Runtime Bridge GitHub Git-object actions published an exact three-file candidate tree as a non-force fast-forward of the private runtime repository:

```text
V1 private source commit  80fdd092c4fb742b65c73c7b2787dba32e858361
V1 parent                 f296fa029cf523fad55237dbd42b821392355f11
```

After the owner performed an ordinary `git pull --ff-only origin main`, Windows `core.autocrlf=true` checked two source payloads out with CRLF despite the release manifest hashing LF bytes. Exact LF normalization reproduced both declared SHA-256 hashes and original Git blob identities. The owner then performed a bounded `git add` to reconcile index metadata: `git diff --cached --name-status` was empty and the working tree clean. No content rewrite was committed, and no Git configuration/ACL was changed.

V1 managed `prepare` and `publish` passed. Its first restart **failed** with `RUNTIME_REPLACEMENT_CONTRACT_MISMATCH` because the target release version was `0.1.1-preview.82-semantic-git-readonly-preflight-budget` but the payload did not update `PUBLIC_SERVER_VERSION` in `src/surface-contracts.mjs`. The managed restart receipt recorded `status=failed`, `recoveryAttempted=true`, `recoverySucceeded=true`; live health returned the restored prior version `0.1.1-preview.81-runtime-secret-scanner-fix`. V1 verification correctly returned `verification_failed` with two mismatches. The V1 failure was not silently relabeled success or retried.

## Corrected V2 source and release qualification

V2 includes the exact `PUBLIC_SERVER_VERSION` declaration and a matching focused test assertion. It adds an immutable bundle-local `.gitattributes` rule (`payload/** -text`, `release.json -text`) so LF payload bytes survive Windows checkout exactly; there is no global Git configuration change. It retains the host-backed semantic Git mutation path and all original authority, protected-path, exact-parent, branch, index and integrity guards.

V2 was published through the same bounded Git-object self-hosting route with an exact-parent, non-force ref update. Comparison confirmed exactly five added release-bundle files. The owner fast-forwarded the clean private checkout, and read-only bridge postflight verified HEAD/origin parity and byte-for-byte manifest hashes.

```text
V2 private source HEAD    a489e81535f1ec5b94b8122f91c86ca5ea155ba4
V2 parent                 80fdd092c4fb742b65c73c7b2787dba32e858361
Release ID                semantic-git-readonly-preflight-budget-v2
Target version            0.1.1-preview.82-semantic-git-readonly-preflight-budget
Surface                   codexless-public-preview-v2
Tool count                179
Payload file count        3
Runtime dependency count  1 (github-keyring-win32-x64)
Manifest SHA-256          cc91738f899c9481bd691997504170340ac5f46c2cdadd028397441029da6925
Focused test              PASS 4/4, 30000 ms, no mutation
Prepare                   prepared
Publish                   succeeded (rm_5c9fd7a054254ff208ec0b15316195d0)
Activation                succeeded (rm_d9effa280055edc9dc7a3a6c3f73cadf)
Postactivation verify     verified, mismatchCount=0
```

The controlled activation required no recovery attempt. Live `/healthz` independently returned `ok=true`, exactly the expected preview.82 version, surface `codexless-public-preview-v2` and 179 tools. The registered workspace's model-free read-only Git call and bounded GitHub repository-read action both worked. No deliberate tunnel restart, credential export, permission broadening or forbidden direct `.git` mutation occurred.

## Real repaired-operation acceptance

The public ADS Research 592 candidate was rechecked: `scripts/check_knowledge_map.py` PASS, `scripts/check_repository_integrity.py --checked-branch v1-source-vault-bootstrap-resume` reported `PUBLIC_REPOSITORY_INTEGRITY=PASS`, and `git diff --check` and exact HEAD/index/upstream preconditions passed.

The repaired **purpose-specific** `codex.git_commit_paths` committed exactly `docs/CURRENT_STATE.md`, `docs/KNOWLEDGE_MAP.md` and `docs/research/592_r0_p03_prospective_source_status_contamination_review_method.md`, with an exact single parent, empty index and `postflightOk=true`. One `codex.git_push_ff_only` succeeded with public integrity PASS, `retried=false`, clean tracked tree and refreshed remote equality.

```text
Public Research 592 HEAD   97472de90de438b700226531e4a5516c7f956924
Public parent              27c84fdf50e4a588b82e761ff8a97fa6e269542f
Local = origin HEAD        true
Git commit index clean    true
Push postflight           PASS
```

This verifies the repaired current operation end-to-end. It does not prove all future environmental latency, helper-resolution or tunnel failures eliminated. The next scientific action remains an independently challenged non-arm source-status/contamination method under Research 592, not a source freeze or scored experiment.

```text
RUNTIME_RELEASE_V1=ACTIVATION_FAILED_AND_RECOVERED
RUNTIME_RELEASE_V2=PREPARED_PUBLISHED_ACTIVATED_VERIFIED
V2_MISMATCHES=0
SEMANTIC_GIT_REAL_PUBLIC_COMMIT_AND_PUSH=PASS
R0_P03_SOURCE_REVIEW=NOT_EXECUTED
R0_P03_SCORE=NOT_RUN
CHECKPOINT=898_UNCHANGED
```
