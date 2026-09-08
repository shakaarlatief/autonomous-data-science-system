# GitHub Connector Preimplementation Evidence Gaps

**Date:** 2026-09-08
**Status:** FINAL SCHEMA RECONCILIATION COMPLETE / G0 PRIVATE CANDIDATE QUALIFIED / ACTION-SPECIFIC GAPS REMAIN EVIDENCE-GATED
**Research:** Research 123
**Purpose:** Convert the final 89-action native-schema reconciliation into a bounded evidence plan that closes only gaps material to practical GitHub parity, without attempting to clone host-internal wrapper details that were never projected.

## Final reconciliation

```text
projected actions                         89
captured exact action names               89
missing actions                            0
extra actions                              0
host-visible request contracts captured   89 / 89
GitHub actions invoked during capture      0
machine-readable output schemas exposed    0 / 89
structured error schemas exposed           0 / 89
separate action-title fields exposed        0 / 89
GITHUB_89_SCHEMA_CAPTURE=INCOMPLETE
```

`INCOMPLETE` is an exact-contract classification, not a failure of the 89-action discovery. Everything the host projected was captured; the projection itself omits enough information that exact native-wrapper wire compatibility cannot be reconstructed from discovery alone.

## Evidence layers

Research 123 targets practical capability parity rather than undocumented host-wrapper cloning. Preserve three evidence layers:

```text
L1 native host-visible contract
   action names, request fields, required/optional status, defaults,
   visible enums/constraints/pagination, read-vs-mutation classification

L2 GitHub platform contract
   REST/GraphQL request and response semantics, permissions, statuses,
   pagination, Git object shapes and Actions/download behavior

L3 native wrapper-only behavior
   normalized issue/PR/review models, hidden continuation envelopes,
   reusable file-reference representation and wrapper-specific envelopes
```

L1 is complete at 89/89. Resolve L2 from authoritative GitHub platform documentation and later live Runtime Bridge qualification. Investigate L3 only where wrapper behavior materially affects practical capability or ChatGPT usability.

## Material request-contract gaps

### `create_tree`

The host projects `tree_elements` only as `{ [key: string]: any }[]`. Before `github.create_tree` is frozen, authoritative GitHub Git Tree evidence must establish supported entry fields, modes/types, required combinations, deletion/null semantics and validation behavior.

### Cross-field semantics

The following are descriptive or incomplete rather than fully structural:

```text
create_branch         exactly one of sha / base_ref
fetch_issue/get_repo  exactly one repository selector
add_review_to_pr      review required for COMMENT / REQUEST_CHANGES
create_pull_request   title unless issue; head/base alias and valid-combination rules incomplete
search_repositories   topn aliases per_page but precedence is unspecified
```

Resolve GitHub-native behavior from platform authority. If ambiguity is wrapper-specific, define and document a deliberate Runtime Bridge rule rather than guessing hidden native-wrapper precedence.

### Pagination and continuation

Many exact behaviors are already captured and must remain action-specific. Remaining gaps include collections whose descriptions do not state whether all pages are consumed and cursor/token actions whose returned continuation property is hidden by `any`. Do not impose one global pagination abstraction.

### Download/resource handoff

`download_workflow_artifact` and `download_user_content` describe file results while hiding the native file-reference schema. Practical parity requires reliable ChatGPT handoff, not byte-for-byte reproduction of an undocumented wrapper object. Reuse the already-qualified Codexless MCP resource/file-handoff architecture and qualify user-visible materialization directly.

## G0 is not blocked by action-specific projection gaps

The missing normalized outputs, wrapper error envelopes, hidden continuation property names, `create_tree` entry details and individual alias rules do not prevent implementation of the server-owned GitHub authority/API substrate.

```text
G0
    dedicated GitHub App identity/configuration contract
    device-flow user authorization
    protected server-owned access/refresh token lifecycle
    installation-derived repository authority
    internal REST/GraphQL transport
    bounded GitHub host/API routing
    structured transport-level error normalization
    API transport test doubles / fixtures
```

G0 may begin after this reconciliation because it freezes no public action-specific parity contract. This is not a parity waiver: no `github.*` action becomes parity-qualified merely because G0 exists.

## Output-shape strategy

All 89 native actions return `any`. Invoking every action merely to sample outputs would be expensive, mutation-heavy and still incomplete for optional/error variants. Preferred strategy:

```text
1. define explicit stable Runtime Bridge result contracts from semantic objectives + GitHub API evidence;
2. preserve native descriptive guarantees where visible;
3. use representative read-only native qualifications only when wrapper behavior affects usability/continuation;
4. use disposable mutation fixtures only where a material behavior cannot be established otherwise;
5. never claim exact hidden native-wrapper wire equivalence where the host never exposed it.
```

Potential representative wrapper archetypes, only if needed, are normalized issue, PR, review/thread, repository/installation, search continuation, Git object, Actions, resource handoff and simple success-only mutation results.

## Error strategy

The native host exposes no structured error schema for any action. Runtime Bridge should therefore own one stable semantic error envelope while preserving action-specific GitHub status/cause data internally. The design should distinguish stable machine code, human message, HTTP/GraphQL source, retryability, mutation uncertainty and action identity, and must never expose credentials or sensitive headers.

Already-proven specific semantics, such as `fetch_pr_file_patch` valid-empty versus 404 and merge `expected_head_sha` mismatch, remain stronger than a generic policy.

## Enterprise scope

`fetch_issue.repository_url` and `get_repo.repository_url` explicitly mention GitHub Enterprise Server custom hostnames and GHE.com API hosts. This is endpoint-specific evidence, not proof of universal Enterprise support. G0 should avoid an architecture that precludes future Enterprise routing, while initial github.com/GitHub App qualification may remain the bounded first target. Enterprise parity must be declared separately.

## Official GitHub platform pass

Validation 138 / Checkpoint 381 close the initial platform-level gaps using current official GitHub documentation. `create_tree` nested entry semantics, create-PR normalized head/base requirements, GitHub App user-token/device-flow authority, installation-derived user scope, github.com REST versioning/headers and same-path Contents serialization are now implementation-grade.

The remaining hidden native wrapper outputs/errors do not reopen those platform contracts. They remain per-action result/qualification concerns.

## G0 implementation result

Validation 139 / Checkpoint 382 move G0 from design to a privately preserved candidate. Twelve focused tests cover protected-store serialization, device flow, refresh, fixed REST routing, semantic errors, GraphQL registry and installation-derived scope. No native-wrapper result-shape claim is added by this work. The Windows OS-keyring adapter remains a concrete runtime qualification gate before integration.

## Implementation gate

```text
HOST_VISIBLE_SCHEMA_CAPTURE             COMPLETE 89 / 89
EXACT_NATIVE_WRAPPER_WIRE_CONTRACT      INCOMPLETE
PRACTICAL_ACTION_MAPPING                READY
G0_AUTH_TRANSPORT_KERNEL                PRIVATE CANDIDATE QUALIFIED
ACTION_SPECIFIC PARITY PUBLICATION      BLOCKED UNTIL RELEVANT GAP DISPOSITION
BROAD 89-ACTION NATIVE REPLAY           NOT JUSTIFIED
```

The next substantive work is Windows keyring adapter import and synthetic credential round-trip qualification, followed by main-runtime G0 integration if that gate passes. Authoritative GitHub API mapping continues per action bundle, while targeted native-wrapper qualification remains reserved for concrete material gaps that survive platform mapping.
