# Validation 180: GitHub PR/Review Remaining-Six Resolution Design Qualified

**Date:** 2026-09-09
**Status:** PASS / SIX REMAINING PR-REVIEW ACTIONS CLASSIFIED / TWO ISOLATABLE / FOUR ENVIRONMENT-GATED / RUNTIME HARDENING REQUIRED BEFORE FURTHER DISMISS-AUTO-MERGE TESTING
**Research:** Research 123

## 1. Starting boundary

Validation 179 / Checkpoint 422 closes the Actions rerun family positive-live 2/2 and leaves exactly six native write actions without successful positive-live qualification, all in the PR/review family:

```text
github.dismiss_pull_request_review
github.enable_auto_merge
github.request_pull_request_reviewers
github.remove_pull_request_reviewers
github.update_pull_request
github.merge_pull_request
```

The owner then authorized continuation from the six-action resolution-design boundary. This validation is read-only with respect to GitHub PR/review state. It does not resume PR #84 mutations and does not replay the previous dismissal attempt.

## 2. Repository-wide environment survey

The installed GitHub App repository surface contains twelve repositories, all owned by `shakaarlatief`. Read-only repository metadata was inspected for all twelve. Every repository reports:

```text
allow_auto_merge = false
```

All twelve do permit at least one ordinary immediate merge method, but repository-level auto-merge is disabled everywhere. Therefore there is no currently installed repository on which `github.enable_auto_merge` can be positively exercised without first changing repository configuration through authority outside the captured 89-action parity surface.

Read-only pull-request discovery across all installed repositories found PR history only in four repositories. Every discovered pull request is authored by the same GitHub user `shakaarlatief`; no bot-authored or second-user PR fixture exists in the installed surface.

The bounded generic repository fetch allowlist intentionally rejects direct collaborator/assignee/team enumeration URL families. The live Runtime Bridge does expose `github.get_repo_collaborator_permission`, but that action validates a known username and is not a collaborator-discovery surface. No independent second reviewer identity can therefore be safely inferred or discovered from the current installed repository history.

## 3. Dismiss-review diagnosis

The failed positive dismissal in Validation 175 targeted a COMMENT review. GitHub's current GraphQL documentation states that `dismissPullRequestReview` dismisses an approved or rejected pull-request review. The ordinary GitHub review model distinguishes COMMENT, APPROVE and REQUEST_CHANGES decisions. GitHub REST documentation exposes a fixed dismissal endpoint and returns a normalized review with state `DISMISSED` on success.

This explains the live error returned against the COMMENTED review:

```text
Can not dismiss a commented pull request review
```

The current Runtime Bridge implementation sends the dismissal through GraphQL after resolving only review scope. GraphQL errors on mutation operations are conservatively classified as `mutationUncertain=true`, so a known non-dismissible COMMENTED state became an uncertainty stop even though readback showed no state change.

A robustness correction is warranted before any further dismissal attempt:

1. include review `databaseId` and `state` in the fixed review-scope query;
2. fail closed before mutation unless state is `APPROVED` or `CHANGES_REQUESTED`;
3. use GitHub's fixed REST dismissal endpoint with the resolved database ID and body `{message, event: DISMISS}`;
4. preserve the caller's existing GraphQL node-ID contract;
5. keep mutation-aware single-attempt transport.

A REST 422/other classified HTTP response is a known GitHub response and therefore remains `mutationUncertain=false`; only transport failure before a classifiable response remains uncertain.

Positive dismissal still requires a genuinely dismissible review, which in the current installed environment requires an independent reviewer/author relationship that does not exist.

## 4. Auto-merge diagnosis

GitHub documentation requires repository-level auto-merge to be enabled before a PR can have auto-merge configured. GitHub also exposes the option only on PRs that cannot merge immediately because some merge requirement remains outstanding.

The current Runtime Bridge implementation reads repository merge-method settings but does not first reject `allow_auto_merge=false`; it would reach the GraphQL mutation and receive an avoidable semantic failure. A robustness correction is therefore warranted:

```text
if repository allow_auto_merge !== true:
    fail before GraphQL mutation with deterministic Runtime Bridge error
```

Because all twelve currently installed repositories have auto-merge disabled, positive-live qualification remains configuration-gated unless the owner separately chooses to change repository settings outside the captured 89-action surface. Research 123 should not silently mutate repository configuration merely to force one parity test green.

## 5. Reviewer request/removal diagnosis

`github.request_pull_request_reviewers` and `github.remove_pull_request_reviewers` require a real individual reviewer or team target for meaningful positive-live qualification. The current installed surface contains only user-authored PRs, no organization-owned installed repository/team fixture, and no safely discoverable second collaborator identity.

Requesting an invented username, unrelated account or guessed bot would create unnecessary third-party interaction and would not be a professional qualification fixture. These two actions remain fixture-gated until a known authorized second reviewer/team exists.

The current Runtime Bridge narrowing that requires at least one reviewer or team reviewer remains deliberate even though the captured native schema does not structurally require a non-empty array.

## 6. Update and merge are independently isolatable

`github.update_pull_request` and `github.merge_pull_request` do not require the blocked reviewer or auto-merge environment. They can be qualified without touching PR #84 by creating a fresh disposable base branch, fresh disposable head branch, one deterministic head-only fixture commit, and a new disposable PR between those two branches.

The safe order is:

```text
1. read current main SHA, but never use main as PR base/merge target
2. create disposable base branch from that SHA
3. create disposable head branch from that SHA
4. create one fixture file/commit on disposable head
5. create disposable PR head -> disposable base
6. derive exact PR number and exact head SHA from returned/read-back state
7. invoke github.update_pull_request once with bounded title/body metadata change
8. reread PR and exact head SHA
9. invoke github.merge_pull_request once with required expected_head_sha
10. verify disposable base advanced to returned merge SHA and main remained unchanged
```

Any `mutationUncertain=true` remains a hard stop with no replay.

This sequence requires separate explicit owner authorization because it performs new PR/repository mutations.

## 7. Resolution classification

```text
github.update_pull_request
    READY_FOR_ISOLATED_POSITIVE_FIXTURE

github.merge_pull_request
    READY_FOR_ISOLATED_POSITIVE_FIXTURE

github.dismiss_pull_request_review
    SECOND_REVIEWER_FIXTURE_GATED + RUNTIME_GUARD_HARDENING_REQUIRED

github.enable_auto_merge
    REPOSITORY_CONFIGURATION_GATED + RUNTIME_GUARD_HARDENING_REQUIRED

github.request_pull_request_reviewers
    SECOND_REVIEWER_OR_TEAM_FIXTURE_GATED

github.remove_pull_request_reviewers
    SECOND_REVIEWER_OR_TEAM_FIXTURE_GATED
```

Under the current account/repository environment, the maximum immediately achievable successful positive-live coverage is therefore 37/41 after isolated update+merge qualification. The remaining four should stay explicitly environment-gated rather than being forced through unrelated configuration/collaborator changes outside the parity surface.

## 8. Next boundary

Before any new positive PR/review mutation, first harden the two known semantic preflight gaps without changing public tool schemas:

- deterministic non-dismissible-review guard plus fixed REST dismissal transport;
- deterministic repository auto-merge-disabled guard.

Then publish/verify that runtime hardening with local no-write guard tests. Afterward, separately request owner authorization for the isolated update+merge disposable PR sequence.

```text
VALIDATION180=PASS
PR_REVIEW_REMAINING_SIX_DESIGN=PASS
PR_REVIEW_READY_FOR_ISOLATED_POSITIVE=2
PR_REVIEW_ENVIRONMENT_GATED=4
DISMISS_REVIEW_GATED=SECOND_REVIEWER_PLUS_HARDENING
AUTO_MERGE_GATED=REPOSITORY_CONFIGURATION_PLUS_HARDENING
REQUEST_REVIEWERS_GATED=SECOND_REVIEWER_OR_TEAM
REMOVE_REVIEWERS_GATED=SECOND_REVIEWER_OR_TEAM
UPDATE_PR_READY=true
MERGE_PR_READY=true
CURRENT_ENVIRONMENT_MAX_POSITIVE_LIVE=37_OF_41
PR84_MUTATION_REPLAY_AFTER_UNCERTAINTY=0
NEXT=PR_REVIEW_SEMANTIC_GUARD_HARDENING_PREVIEW38
```
