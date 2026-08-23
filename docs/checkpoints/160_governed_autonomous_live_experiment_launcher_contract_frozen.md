# Checkpoint 160: Governed Autonomous Live Experiment Launcher Contract Frozen

**Date:** 2026-08-23  
**Status:** FROZEN CONTROL-PLANE CONTRACT  
**Checkpoint class:** EXPERIMENT-CONTROL CONTRACT / IMPLEMENTATION BOUNDARY  
**Project stage:** Post-V0 bounded V1 implementation and integration  
**Scope:** Freezes the first governed autonomous live-experiment launcher design before implementation and provider-free validation.  
**Authority:** Historical contract-freeze boundary. Specification 018 v0.1 is the frozen implementation authority for this bounded control-plane experiment until superseded by a later accepted result.  
**Design session:** 04  
**ChatGPT project:** Autonomous Data Science System  
**Session title:** 04 - Selective Context Promotion & Reasoning Vertical Slice  
**Development branch:** `v1-autonomous-live-experiment-launcher`  
**Base integration commit:** `4385b83b43582ff6466b519b4e96356d220c44bc`  

## 1. Why this checkpoint exists

Specification 017 is now historically closed through a preservation-only merge. PR #22 merged the frozen contract and incomplete live evidence into `v1-frontend-spike`, while PR #16 was closed without merging its unpromoted experiment implementation.

The next bounded project objective is the user's requested removal of the repeated manual GitHub Actions button press for already-authorized live experiments.

Research 025 and Specification 018 now freeze the first governed control-plane design before implementation.

## 2. Frozen design

The launcher architecture is:

```text
owner-created GitHub issue
    -> default-branch launcher workflow
    -> repository-controlled authorization registry
    -> exact actor / source-SHA / CI-run / duplicate checks
    -> exact allowlisted workflow_dispatch
    -> experiment-owned live workflow
```

The launcher itself has no provider credential and makes no model/provider call.

## 3. Frozen security and governance properties

The implementation must preserve all of the following:

```text
owner-only authorization
fixed repository registry
no arbitrary command execution
no issue-supplied workflow/ref/SHA/model/prompt/secret
exact source SHA verification
exact required CI run-ID verification
fail-closed duplicate policy
least-privilege launcher token
independent target-workflow SHA/confirmation check
accepted/rejected issue audit trail
```

## 4. External platform basis

Current GitHub documentation supports the selected transport mechanism:

- `workflow_dispatch` workflows must exist on the default branch;
- `workflow_dispatch` is an explicit exception to the usual recursive-workflow suppression for events created with `GITHUB_TOKEN`.

This permits a GitHub-native issue-event gate to dispatch an allowlisted live workflow without a repeated manual Actions UI step.

## 5. Provider-free validation requirement

No provider-backed launch is authorized by this checkpoint.

The next implementation must pass:

1. registry validation tests;
2. issue grammar and owner-rejection tests;
3. source-SHA and exact CI-run tests;
4. duplicate-launch tests;
5. exact dispatch-construction tests;
6. static workflow least-privilege tests;
7. full repository regression tests on Ubuntu and Windows where applicable;
8. one end-to-end provider-free issue-to-`workflow_dispatch` probe after the exact implementation head is green.

## 6. Promotion audit

### Promote now

Only the following are promoted as frozen implementation requirements:

- Research 025 as the design rationale for the launcher experiment-control slice;
- Specification 018 v0.1 as the frozen provider-free implementation contract;
- the architectural distinction between launch authorization and provider execution credentials;
- the requirement that issue text can select only an existing launch authorization and cannot define executable configuration.

### Do not promote now

The following are not yet accepted capabilities:

- the launcher implementation itself;
- autonomous provider-backed live execution;
- autonomous retries;
- arbitrary workflow dispatch;
- final production approval policy;
- a final control-plane transport beyond this bounded V1 mechanism.

## 7. Historical boundaries preserved

Specification 014 remains accepted bounded selective-context evidence.

Specification 015 remains immutable `FAIL` evidence.

Specification 016 remains bounded supported disposition-semantics evidence.

Specification 017 remains an incomplete live execution with no advancement classification. Its partial scores are not used to tune this launcher.

## 8. Exact continuation

```text
1. implement Specification 018 on v1-autonomous-live-experiment-launcher
2. add provider-free unit/static/integration tests
3. add ordinary pull-request CI
4. validate the exact branch head
5. expose only the launcher registry/workflow and harmless probe on main
6. create one owner launch issue through the connected GitHub interface
7. require autonomous workflow_dispatch of the probe with no provider call
8. checkpoint exact run IDs and result
9. only then preregister the next recommendation/action experiment with system-owned provenance
```

No new recommendation/action provider call is authorized at Checkpoint 160.
