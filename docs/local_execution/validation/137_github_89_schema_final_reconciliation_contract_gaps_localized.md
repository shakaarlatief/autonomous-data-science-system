# Validation 137: GitHub 89-Schema Final Reconciliation, Contract Gaps Localized

**Date:** 2026-09-08
**Status:** PASS / 89 OF 89 HOST-VISIBLE CONTRACTS RECONCILED / EXACT NATIVE WIRE CONTRACT INCOMPLETE / G0 READY
**Research:** Research 123
**Scope:** Preserve the final same-conversation reconciliation of all six native GitHub schema-capture batches, distinguish complete host-visible request mapping from unavailable native wrapper wire details, and define the smallest justified preimplementation evidence strategy.

## 1. Final GitHub-only reconciliation

The same fresh GitHub-only conversation that projected the corrected 89-action inventory and supplied all six discovery batches performed one final reconciliation without invoking any GitHub action.

```text
projected actions                       89
captured exact actions                  89
missing actions                          0
extra actions                            0
full host-visible schemas captured      89 / 89
GitHub actions invoked                   0
GITHUB_89_SCHEMA_CAPTURE=INCOMPLETE
```

The `INCOMPLETE` result is not a count/inventory failure. It means the host projection itself does not expose enough information to clone the complete native wrapper wire contract exactly.

## 2. Projection-wide missing contract classes

The reconciliation confirms:

```text
machine-readable output schemas missing       89 / 89
structured machine-readable error schemas     89 / 89 missing
separate action title fields                   89 / 89 missing
```

Descriptions expose partial semantic result/error behavior for some actions, but do not recover field types, nullability, nested structure, requiredness or full error envelopes.

## 3. Request-side genericization and ambiguity

`GitHub.create_tree.tree_elements` remains the strongest structural loss:

```text
{ [key: string]: any }[]
```

The projection therefore omits exact entry properties, required fields, enums, Git modes/types, path constraints and cross-field rules.

Other material ambiguities include descriptive-only cross-field requirements, incomplete `create_pull_request` head/base alias behavior, `search_repositories` topn/per_page precedence, hidden continuation result fields, unspecified pagination for some collections, `enable_auto_merge` inference details, hidden file-reference schemas, reviewer-array at-least-one ambiguity and plain-string example domains that are not enums.

## 4. Correct interpretation

The final evidence supports two different readiness claims:

```text
ACTION INVENTORY / NAMING                 READY 89 / 89
HOST-VISIBLE REQUEST CONTRACT MAPPING     READY 89 / 89
EXACT NATIVE WRAPPER WIRE CONTRACT        NOT READY
```

Research 123 targets practical GitHub capability parity. Exact cloning of undocumented host wrapper objects is not automatically required for practical parity and should not trigger an indiscriminate 89-action live replay.

## 5. Evidence-gap strategy

`docs/research/GITHUB_CONNECTOR_PREIMPLEMENTATION_EVIDENCE_GAPS.md` now separates:

```text
L1 native host-visible contract    complete
L2 GitHub platform contract        authoritative GitHub docs/live Runtime Bridge evidence next
L3 native wrapper-only behavior    targeted qualification only where materially relevant
```

The plan explicitly avoids inferring hidden native fields. It also avoids blocking all implementation on action-specific result gaps that do not affect the independent authentication/transport substrate.

## 6. G0 disposition

The action-specific projection gaps do not block the planned G0 kernel because G0 freezes no public `github.*` action-specific request/result contract.

G0 may therefore begin with:

```text
GitHub App/device-flow authority
protected server-owned token lifecycle
installation-derived repository scope
internal REST/GraphQL transport
bounded GitHub routing
transport-level semantic error normalization
API transport fixtures/tests
```

No action-specific parity publication is authorized merely by completing G0. Each action or implementation bundle must still satisfy its relevant GitHub platform/request/result/permission/error evidence before parity qualification.

## 7. Next boundary

The broad schema-capture loop is closed. The next work is **G0 plus authoritative GitHub API contract mapping**, with targeted native connector qualification only for surviving material wrapper gaps.

```text
VALIDATION137=PASS
HOST_VISIBLE_SCHEMA_CAPTURE=89_OF_89_COMPLETE
GITHUB_89_SCHEMA_CAPTURE=INCOMPLETE
INTERPRETATION=EXACT_NATIVE_WIRE_CONTRACT_INCOMPLETE
PRACTICAL_ACTION_MAPPING=READY
G0_AUTH_TRANSPORT_KERNEL=READY_TO_BEGIN
ACTION_SPECIFIC_PARITY_PUBLICATION=BLOCKED_PENDING_RELEVANT_GAP_DISPOSITION
BROAD_NATIVE_89_ACTION_REPLAY=NOT_JUSTIFIED
IMPLEMENTATION=NOT_STARTED_AT_THIS_VALIDATION
NEXT=G0_PLUS_AUTHORITATIVE_GITHUB_API_CONTRACT_MAPPING
```
