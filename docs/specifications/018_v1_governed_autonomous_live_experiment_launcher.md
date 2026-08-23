# Specification 018: V1 Governed Autonomous Live Experiment Launcher

**Version:** 1.0 bounded accepted control-plane contract  
**Status:** ACCEPTED FOR BOUNDED V1 USE  
**Date:** 2026-08-23  

## 1. Purpose

Specification 018 defines the first bounded control-plane capability that may replace the repeated manual GitHub Actions button press after a live experiment is already preregistered and its exact implementation head has passed the required provider-free gates.

The capability is intentionally narrow:

```text
owner-created governed launch request
    -> fail-closed repository-controlled authorization gate
    -> exact allowlisted workflow_dispatch
```

The launcher does not design experiments and does not itself call a provider.

## 2. Normative safety boundary

The launcher MUST satisfy all of the following:

1. execute from a workflow that exists on the default branch;
2. trigger only on newly opened GitHub issues;
3. accept requests only from the frozen repository owner login;
4. load launch behavior only from a repository-controlled registry;
5. treat issue text only as a launch identifier and exact confirmation token;
6. reject issue-supplied workflow paths, refs, SHAs, commands, models, prompts, secrets, or arbitrary arguments;
7. verify the exact source branch currently resolves to the registry source SHA;
8. verify every required frozen CI run ID against the exact source SHA and success conclusion;
9. reject duplicate launches under the bounded V1 duplicate policy;
10. dispatch only the exact registry workflow file/ref with exact registry-derived inputs;
11. expose no provider API secret to the launcher job;
12. record acceptance or rejection on the triggering issue;
13. leave independent exact-SHA and confirmation checks in the target live workflow;
14. fail closed on malformed registry data, malformed issue requests, missing API data, API errors, or ambiguous state.

## 3. Repository artifacts

The implementation SHALL introduce:

```text
.github/ads_live_experiments.json
.github/workflows/v1-autonomous-live-experiment-launcher.yml
.github/workflows/v1-live-launcher-probe.yml
scripts/ads_live_experiment_launcher.py
tests/unit/test_ads_live_experiment_launcher.py
```

The default-branch exposure of the two workflows and registry is a later deployment step after provider-free branch validation. The implementation branch itself is the source for review and tests.

## 4. Registry schema

Top-level object:

```json
{
  "schema_version": 1,
  "authorizations": []
}
```

Each authorization MUST contain exactly the governed launch information required by the launcher:

```json
{
  "launch_id": "string",
  "enabled": true,
  "owner_login": "string",
  "workflow_file": "string.yml",
  "ref": "branch-or-tag",
  "expected_source_sha": "40-hex commit SHA",
  "confirmation": "string",
  "required_ci_runs": [
    {
      "run_id": 123456789,
      "workflow_name": "Exact workflow name"
    }
  ]
}
```

### 4.1 Registry invariants

- `schema_version` MUST equal `1`.
- `launch_id` MUST be unique.
- `launch_id` MUST match `^[a-z0-9][a-z0-9._-]{2,79}$`.
- `owner_login` MUST match the configured repository owner for the initial V1 implementation.
- `workflow_file` MUST be a basename ending in `.yml` or `.yaml`; path separators are forbidden.
- `ref` MUST be a non-empty branch/tag string without whitespace or shell metacharacters.
- `expected_source_sha` MUST be exactly 40 lowercase hexadecimal characters.
- `confirmation` MUST match `^[A-Z0-9_]{8,120}$`.
- `required_ci_runs` MUST be non-empty for any enabled provider-backed authorization.
- every `run_id` MUST be a positive integer and unique inside the authorization.
- every `workflow_name` MUST be non-empty.

A provider-free probe authorization MAY use the same requirements and MUST still carry at least one exact successful CI run before launch.

## 5. Issue grammar

Accepted title grammar:

```text
[ADS LIVE] <launch_id>
```

Accepted body grammar:

```text
authorization: <confirmation>
```

The body MAY contain surrounding ASCII whitespace but MUST contain no additional non-whitespace content.

The launcher MUST NOT interpret Markdown links, code blocks, JSON, YAML, shell fragments, or additional key/value pairs from the issue.

## 6. Actor checks

Initial V1 authorized owner:

```text
shakaarlatief
```

The following MUST all equal the authorization `owner_login`:

```text
github.actor
github.event.sender.login
github.event.issue.user.login
repository owner
```

If any identity is absent or unequal, the request MUST reject before any workflow dispatch.

## 7. Source-head verification

Immediately before dispatch, the launcher MUST resolve:

```text
GET /repos/{repo}/git/ref/heads/{ref}
```

for a branch authorization and require its object SHA to equal `expected_source_sha`.

If the ref is not resolvable exactly, the launcher MUST reject.

The target workflow MUST independently require:

```text
github.sha == inputs.expected_source_sha
```

before any provider call or external side effect beyond bounded reporting.

## 8. Required-CI verification

For every registry `required_ci_runs` entry, the launcher MUST fetch the exact Actions run by ID and require:

```text
repository.full_name == current repository
name                 == registry workflow_name
head_sha             == expected_source_sha
status               == completed
conclusion           == success
```

No substitution with a different run ID is permitted at launch time.

## 9. Duplicate-launch policy

For V1, the launcher MUST reject if it can establish that the exact target workflow already has a queued, in-progress, or completed `workflow_dispatch` run whose `head_sha` equals the authorization `expected_source_sha`.

This intentionally treats replacement attempts conservatively. A deliberate new attempt requires a new frozen authorization record and a new `launch_id`.

If duplicate state cannot be determined reliably, fail closed.

## 10. Dispatch contract

The launcher MUST invoke only:

```text
POST /repos/{repo}/actions/workflows/{workflow_file}/dispatches
```

using the registry-controlled workflow file and registry-controlled ref.

Inputs MUST be exactly:

```json
{
  "launch_id": "<registry launch_id>",
  "expected_source_sha": "<registry expected_source_sha>",
  "confirmation": "<registry confirmation>"
}
```

No issue-derived field other than the already validated `launch_id` and exact confirmation equality may influence the dispatch payload.

## 11. Workflow permissions

Launcher workflow permissions MUST be no broader than:

```yaml
permissions:
  actions: write
  contents: read
  issues: write
```

The launcher workflow MUST NOT receive `OPENAI_API_KEY` or another provider credential.

The provider-free probe MUST not receive provider credentials.

## 12. Probe workflow

The first end-to-end validation target MUST be provider-free.

The probe workflow MUST:

- use `workflow_dispatch` only;
- accept exactly `launch_id`, `expected_source_sha`, and `confirmation` inputs;
- verify exact frozen probe values;
- verify `github.sha == expected_source_sha`;
- print a bounded success marker;
- perform no model/provider call;
- use no repository write permission;
- upload no secret-bearing artifact.

## 13. Python launcher module

`scripts/ads_live_experiment_launcher.py` SHALL provide testable logic separated from transport.

Required conceptual interfaces:

```text
load_registry(...)
parse_issue_request(...)
validate_authorization(...)
validate_ci_runs(...)
validate_duplicate_state(...)
build_dispatch_request(...)
```

The module MAY use standard-library-only Python for the pure validation layer.

Network transport MAY be performed by the workflow through GitHub CLI/API calls, but the data passed to those calls MUST come from validated registry-derived output.

## 14. Provider-free test matrix

At minimum, automated tests MUST cover:

### Registry acceptance/rejection

- valid registry;
- wrong schema version;
- duplicate launch ID;
- malformed SHA;
- workflow path traversal;
- shell-like ref;
- malformed confirmation;
- empty CI run set on enabled authorization.

### Issue parsing

- exact valid request;
- wrong title prefix;
- unknown launch ID;
- wrong confirmation;
- additional body content;
- issue-supplied fake workflow/ref/SHA text;
- non-owner actor;
- non-owner sender;
- non-owner issue author;
- repository-owner mismatch.

### Source and CI checks

- exact branch SHA success;
- moved branch rejection;
- CI run wrong SHA;
- CI run wrong workflow name;
- CI run not completed;
- CI run failed;
- missing CI run/API error.

### Duplicate checks

- no prior run accepted;
- queued duplicate rejected;
- in-progress duplicate rejected;
- completed duplicate rejected;
- unrelated SHA ignored;
- ambiguous duplicate lookup rejected.

### Dispatch construction

- exact workflow/ref/three-input payload;
- no arbitrary issue fields propagated.

## 15. Static workflow tests

Tests MUST verify the launcher workflow text does not contain:

- provider secret references;
- `eval`;
- issue-body interpolation into a shell command;
- issue-derived workflow/ref/SHA dispatch configuration.

Tests MUST verify launcher permissions are exactly the bounded set in Section 11.

## 16. End-to-end provider-free gate

After branch CI passes, the control plane MAY be exposed narrowly on `main` for one probe authorization.

The probe gate passes only if:

```text
owner issue created through connected GitHub interface
    -> launcher issue-event workflow starts
    -> launcher validates exact authorization
    -> launcher dispatches probe workflow without manual UI action
    -> probe run starts through workflow_dispatch
    -> probe exact SHA/confirmation checks pass
    -> no provider call occurs
```

The run IDs and exact source SHA MUST be recorded in the next checkpoint.

## 17. Failure interpretation

A launcher/probe failure is control-plane evidence, not recommendation/action scientific evidence.

Do not modify a frozen recommendation/action experiment contract to repair this launcher.

## 18. Promotion rule

The bounded launcher capability MAY be promoted only after:

1. the exact implementation head passes provider-free CI;
2. the exact default-branch launcher/probe exposure is reviewed against this specification;
3. one end-to-end provider-free issue-to-dispatch probe passes;
4. the result is checkpointed with exact run IDs and source SHAs.

## 19. Non-selections preserved

Specification 018 does not select:

- final production approval policy;
- autonomous experiment design;
- automatic provider retries;
- arbitrary workflow dispatch;
- arbitrary issue-driven commands;
- final provider/model;
- final recommendation/action policy;
- multi-agent architecture;
- deployment/cloud architecture.

## 20. Next step after promotion

After this bounded launcher is accepted, preregister the next recommendation/action-value experiment using system-owned exact context provenance. Only after that experiment's contract is frozen and its exact implementation head is green may a provider-backed authorization be added to the launcher registry.

## 21. Accepted end-to-end result

Checkpoint 161 records the successful bounded provider-free gate.

```text
implementation source   27e7bc84b5f63d65d43de9a5bd27d1fdc0677071
cross-platform CI       32660168566
launcher run            32660333663
probe run               32660340429
probe job               97245432893
observer run            32660375449
result                   GOVERNED_LAUNCHER_SUPPORTED
```

The owner-created issue was transport only. The repository-controlled registry supplied the executable workflow/ref/SHA/CI/confirmation authorization. The launcher dispatched the allowlisted provider-free probe without a manual Actions UI click and without a provider credential. The target probe independently verified its exact source SHA, ref, launch ID, and confirmation and completed successfully.

This acceptance is bounded to explicitly registered frozen experiments. It does not authorize autonomous experiment design, arbitrary workflow execution, arbitrary issue-driven commands, or automatic provider use.
