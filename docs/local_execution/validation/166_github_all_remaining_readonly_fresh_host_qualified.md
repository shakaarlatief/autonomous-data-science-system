# Validation 166: Final 26 GitHub Read-Only Actions Fresh-Host Qualified

**Date:** 2026-09-09
**Status:** PASS / FINAL READ-ONLY HOST GATE CLOSED / 48 OF 48 READ ACTIONS HOST-QUALIFIED / MUTATION PHASE NEXT
**Research:** Research 123
**Scope:** Preserve fresh-host projection, bounded schema inspection and exactly-once live qualification of the final 26 preview.33 GitHub read-only actions.

## 1. Starting boundary

Validation 165 / Checkpoint 408 had already established live Runtime Bridge preview.33 with 112 public tools, all 48 captured native GitHub read action names, 25 of 26 new actions positively live-qualified locally, and `github.download_user_content` intentionally positive-live-fixture-gated. The remaining gate was fresh ChatGPT host projection plus live use of the final 26-action batch.

## 2. Owner-supplied fresh-host result

The owner supplied the completed disposable-chat qualification with final marker:

```text
GITHUB_ALL_REMAINING_READONLY_FRESH_HOST=PASS
```

All 26 exact actions projected simultaneously in the fresh host. Every visible caller contract remained bounded and no schema was genericized/truncated enough to prevent establishing the input authority. The host did not separately render a literal `additionalProperties: false` keyword, so this validation does not overclaim that exact host-visible JSON-Schema keyword; local MCP wire evidence remains the authority for strict extra-field rejection. The host also exposed no separate titles or annotations for these 26 actions.

No projected action exposed caller-selected GitHub credentials, access/refresh tokens, client secrets, Authorization headers, GitHub hosts, arbitrary HTTP methods/headers, arbitrary REST endpoints, arbitrary GraphQL documents, permission profiles or non-GitHub transport authority.

## 3. Exact 26-action live result

All 26 authorized calls were made exactly once in the required order. No retry occurred.

The first call intentionally qualified the host allowlist guard rather than positive content retrieval:

```text
github.download_user_content
    https://example.com/not-allowed.png
    -> expected bounded hostname rejection
    -> positive live behavior remains FIXTURE_GATED
```

This expected semantic rejection is a PASS for the bounded-host qualification and is not counted as a failed application route. No private repository search or invented `private-user-images.githubusercontent.com` URL was used to manufacture a positive fixture.

Calls 2-26 all returned successful application results:

```text
github.download_workflow_artifact            PASS
github.fetch_commit_workflow_runs            PASS
github.fetch_issue                           PASS
github.fetch_issue_comments                  PASS
github.fetch_pr                              PASS
github.fetch_pr_comments                     PASS
github.fetch_pr_file_patch                   PASS
github.fetch_pr_patch                        PASS
github.fetch_workflow_job_logs               PASS
github.fetch_workflow_job_steps              PASS
github.fetch_workflow_run_artifacts          PASS
github.fetch_workflow_run_jobs               PASS
github.get_commit_combined_status            PASS
github.get_issue_comment_reactions           PASS
github.get_pr_diff                           PASS
github.get_pr_info                           PASS
github.get_pr_reactions                      PASS
github.get_pr_review_comment_reactions       PASS
github.get_users_recent_prs_in_repo          PASS
github.list_pr_changed_filenames             PASS
github.list_pull_request_review_threads      PASS
github.list_pull_request_reviews             PASS
github.list_recent_issues                    PASS
github.search_issues                         PASS
github.search_prs                            PASS
```

## 4. Canonical issue / PR / workflow fixture evidence

The canonical Research 123 fixtures resolved successfully:

```text
issue                         #82
issue comments                1 / ID 5580007938
PR                            #81
PR changed files              1
known changed filename        github-connector-capability-qualification.md
PR merged discussion entries  6
PR reviews                     3 / all COMMENTED
PR review threads              1 / unresolved / not outdated
workflow run                  32815726116
workflow job                  97703468768
workflow artifact             9553693015
```

`github.fetch_commit_workflow_runs` returned eight first-page PR-triggered runs for the selected commit, all reported completed/success. Workflow run `32815726116` exposed job `97703468768` and artifact `9553693015`. The job logs were non-empty and the job-step action reported eleven completed/success steps.

Combined commit status was successfully readable and returned `pending` with zero individual status contexts. Valid zero-reaction collections from issue-comment, PR and review-comment reaction readers were preserved as successful reads.

Issue search returned canonical issue #82 and PR search returned canonical PR #81. Recent-issue and authenticated-user recent-PR retrieval also succeeded with bounded result counts.

## 5. Workflow artifact resource handoff

`github.download_workflow_artifact` returned the canonical non-expired artifact with:

```text
filename     qualification-artifact.zip
media type   application/zip
size         322,868 bytes
SHA-256      8d271d9db840ae4f43ddd8c36766198dbb528118656c567f5d3fcf8ecbb02b2e
```

The structured tool result contained compact metadata rather than ZIP bytes/base64. The fresh ChatGPT host also received/materialized the reusable file/resource from the MCP resource-link handoff. This closes the host-side discriminator that remained after the preview.33 local resource-link qualification.

## 6. Secret, mutation and scale boundary

No credential secret appeared. Workflow logs contained only normal GitHub Actions redaction markers such as `***`, not underlying secret values.

No GitHub mutation occurred. No native GitHub connector, Browser, shell/command, semantic Git, runtime-maintenance, runtime-release or authorization-control action was used in the disposable qualification.

Nothing in this fresh-host test indicates that the 112-tool Runtime Bridge / 48-GitHub-read surface is too large for ChatGPT. All 26 newly added actions projected simultaneously with bounded schemas and were callable in one fresh host.

## 7. Read-phase disposition

All captured native GitHub read action names are now live on Runtime Bridge and fresh-host qualified:

```text
native read actions                         48
live Runtime Bridge github.* read actions   48
fresh-host projected / bounded              48 / 48
positive-live read actions                   47 / 48
fixture-gated positive read                  github.download_user_content
```

`github.download_user_content` is still not claimed as positive-live because an authorized `private-user-images.githubusercontent.com` fixture has not existed in the canonical qualification material. Its fresh-host bounded rejection plus synthetic positive resource-link regression are sufficient to move Research 123 into mutations without fabricating evidence.

Known `manageable_only=true`, search-index enrichment, Enterprise repository-URL routing and hidden native output-envelope gaps remain explicit. Exact native-wrapper parity therefore remains conservatively `0 / 89`.

The remaining captured native inventory is exactly 41 write actions. The preferred mutation cadence is now four larger risk/fixture families rather than tiny batches:

```text
repository Git / content mutations    8
issue mutations                      12
PR / review mutations                19
Actions rerun mutations               2
                                     --
remaining writes                     41
```

Repository Git/content mutations are next because they can be qualified on a disposable branch with explicit stale-SHA/non-force safeguards while leaving issue/PR/Actions fixtures untouched.

```text
VALIDATION166=PASS
GITHUB_ALL_REMAINING_READONLY_FRESH_HOST=PASS
FINAL_READ_BATCH_FRESH_HOST_PROJECTION=PASS_26_OF_26
FINAL_READ_BATCH_SCHEMA_BOUNDEDNESS=PASS_26_OF_26
FINAL_READ_BATCH_CALLS_2_TO_26=PASS_25_OF_25
DOWNLOAD_USER_CONTENT_HOST_ALLOWLIST=PASS_EXPECTED_REJECTION
DOWNLOAD_USER_CONTENT_POSITIVE_LIVE=FIXTURE_GATED
DOWNLOAD_WORKFLOW_ARTIFACT_RESOURCE_LINK_HOST=PASS
FRESH_HOST_QUALIFIED_READ_ACTIONS=48_OF_48
POSITIVE_LIVE_READ_ACTIONS=47_OF_48
LIVE_RUNTIME_VERSION=0.1.1-preview.33-github-all-readonly-resource-links
LIVE_PUBLIC_TOOL_COUNT=112
LIVE_GITHUB_READONLY_TOOL_COUNT=48
SECRETS_EXPOSED=false
GITHUB_MUTATION_OCCURRED=false
HOST_SURFACE_SCALE_112_TOOLS=PASS
NATIVE_WRITE_ACTIONS_REMAINING=41
EXACT_NATIVE_PARITY_ROWS_CLOSED=0
NEXT=GITHUB_REPOSITORY_GIT_MUTATION_IMPLEMENTATION
```
