# Validation 183: GitHub Native-Parity Gap Reconciliation, Extended Capabilities Next

**Date:** 2026-09-09
**Status:** PASS / 89 OF 89 ACTION NAMES IMPLEMENTED / 84 OF 89 POSITIVE-LIVE / RESIDUAL GAPS CLASSIFIED / EXACT WRAPPER PARITY EVIDENCE-GATED / EXTENDED CAPABILITIES NEXT
**Research:** Research 123

## 1. Purpose

Checkpoint 425 closes the last immediately isolatable native write positive-live actions and leaves the project at a natural reconciliation boundary. The purpose of this validation is to classify every remaining native-parity gap without forcing unrelated environment changes, inventing hidden wrapper semantics, or broad-replaying the provider-owned connector.

No GitHub mutation is performed in this reconciliation. Three safe read-only/fail-closed probes reconfirm current Runtime Bridge behavior for known option/host gaps.

## 2. Native action implementation and host-schema coverage

The captured provider GitHub connector inventory contains exactly 89 action names:

```text
reads   48
writes  41
total   89
```

Runtime Bridge preview.38 exposes exactly 89 `github.*` tools corresponding to all 89 captured native names. All 48 reads have fresh-host schema qualification. All 41 writes have local wire qualification plus fresh-host schema/guard qualification across their four families.

Therefore:

```text
NATIVE_ACTION_NAMES_IMPLEMENTED=89_OF_89
NATIVE_READ_ACTIONS_IMPLEMENTED=48_OF_48
NATIVE_WRITE_ACTIONS_IMPLEMENTED=41_OF_41
FRESH_HOST_SCHEMA_COVERAGE=89_OF_89
```

This is complete practical action-name/request-surface implementation coverage. It is deliberately distinct from exact hidden wrapper parity.

## 3. Positive-live action coverage

Successful positive-live action coverage is:

```text
reads                         47 / 48
repository Git/content writes  8 /  8
issue writes                  12 / 12
PR/review writes              15 / 19
Actions rerun writes           2 /  2
---------------------------------------
total                         84 / 89
```

Exactly five action-level positive-live gaps remain. All are fixture/environment-gated rather than implementation gaps:

```text
github.download_user_content
    PRIVATE_USER_IMAGES_FIXTURE_GATED

github.dismiss_pull_request_review
    GENUINE_DISMISSIBLE_SECOND_REVIEWER_FIXTURE_GATED

github.enable_auto_merge
    REPOSITORY_AUTO_MERGE_CONFIGURATION_GATED

github.request_pull_request_reviewers
    KNOWN_SECOND_REVIEWER_OR_TEAM_FIXTURE_GATED

github.remove_pull_request_reviewers
    KNOWN_SECOND_REVIEWER_OR_TEAM_FIXTURE_GATED
```

The project does not create unrelated third-party reviewer relationships, alter repository configuration outside the captured parity surface, or fabricate a private-user-images URL merely to turn those five rows green.

## 4. Option-level residual gaps

Three option/host semantics remain intentionally fail-closed or separately scoped inside otherwise implemented read actions. Live preview.38 probes reconfirm each boundary.

### `github.list_installations(manageable_only=true)`

Live result:

```text
errorCode = GITHUB_PARITY_OPTION_NOT_QUALIFIED
error = manageable_only=true is not yet qualified for the first read-only parity bundle
```

The provider wrapper describes a managed-account filter but does not expose exact account-type/filter semantics. A single live sample would not establish the general hidden wrapper rule, so Runtime Bridge continues to fail closed rather than guess.

### `github.list_repositories(include_search_index_status=true)`

Live result:

```text
errorCode = GITHUB_PARITY_OPTION_NOT_QUALIFIED
error = include_search_index_status=true is not yet qualified because the native search-index enrichment contract is not projected
```

The native enrichment output contract remains hidden. Runtime Bridge therefore does not invent enrichment fields.

### Enterprise `repository_url` routing

A fake Enterprise-style URL was supplied to the read-only `github.get_repo` selector path. Runtime Bridge rejected it before Enterprise routing:

```text
errorCode = GITHUB_ENTERPRISE_NOT_QUALIFIED
error = Initial Runtime Bridge repository_url support is bounded to https://github.com; Enterprise host parity remains separate
```

This matches the product boundary established earlier: the current App/runtime targets github.com and the selected GitHub App profile enables no enterprise permissions. Enterprise behavior remains a future target only if a real enterprise environment is introduced.

## 5. Exact native-wrapper wire parity remains evidence-gated

The provider host projection still does not expose enough information to claim byte-for-byte/native-wrapper parity for any action. The unresolved evidence classes are structural rather than implementation omissions:

```text
all native machine-readable output schemas  hidden behind `any`
all structured native error schemas         not projected
separate native title metadata              not projected
create_tree nested entry schema              genericized in host discovery
several cross-field / alias precedence rules hidden or descriptive only
several pagination/result continuation rules hidden or descriptive only
normalized native result envelopes           hidden
```

Official GitHub platform contracts and live behavior were sufficient to implement safe practical actions, but they cannot prove provider-wrapper-only hidden normalization or precedence semantics. Runtime Bridge intentionally uses explicit conservative narrowings where those semantics are not evidenced.

Consequently:

```text
EXACT_NATIVE_WRAPPER_PARITY_ROWS_CLOSED=0_OF_89
```

That metric is preserved as an evidence statement. It must not be reinterpreted as 0/89 implementation coverage.

## 6. Reconciliation disposition

The native-parity implementation phase is now structurally complete for the current evidence and environment:

```text
action names implemented                 89 / 89
fresh-host schema coverage               89 / 89
positive-live action coverage            84 / 89
action-level fixture/environment gaps     5
option/host semantic gaps                  3
unimplemented native actions               0
```

The remaining gaps should stay explicit and dormant until their real prerequisite appears. They do not justify blocking the broader Research 123 product goal.

Research 123 was deliberately expanded at Checkpoint 393 from native parity alone to native parity plus selected GitHub capabilities that the project-owned GitHub App can expose beyond the provider connector. The next stage should therefore return to that extension track. Repository Administration(write) was already selected as the strongest first extension family because the owner explicitly wants repository creation/administration and the App permission profile was configured to support it.

Before exposing any administration mutation, the next step is read-only design/research of a bounded semantic administration foundation, including concrete use cases, exact GitHub REST permission requirements, confirmation classes, destructive-operation handling and a minimal first action slice.

```text
VALIDATION183=PASS
NATIVE_ACTION_NAMES_IMPLEMENTED=89_OF_89
FRESH_HOST_SCHEMA_COVERAGE=89_OF_89
POSITIVE_LIVE_ACTIONS=84_OF_89
POSITIVE_LIVE_ACTION_GAPS=5
NATIVE_OPTION_HOST_GAPS=3
NATIVE_ACTIONS_UNIMPLEMENTED=0
EXACT_NATIVE_WRAPPER_PARITY_ROWS_CLOSED=0_OF_89
MANAGEABLE_ONLY_TRUE=FAIL_CLOSED_HIDDEN_WRAPPER_SEMANTICS
SEARCH_INDEX_ENRICHMENT_TRUE=FAIL_CLOSED_HIDDEN_WRAPPER_SEMANTICS
ENTERPRISE_REPOSITORY_URL=SEPARATE_UNQUALIFIED_TARGET
RESEARCH123_NATIVE_PARITY_IMPLEMENTATION=STRUCTURALLY_COMPLETE_WITH_RESIDUAL_EVIDENCE_GATES
NEXT=EXTENDED_GITHUB_REPOSITORY_ADMINISTRATION_FOUNDATION_DESIGN
```
