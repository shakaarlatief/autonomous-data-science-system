# Research 025: Governed Autonomous Live Experiment Launcher Design

**Status:** design research  
**Date:** 2026-08-23  
**Scope:** control-plane automation for explicitly authorized live ADS experiments  

## 1. Problem

The V1 experiment loop currently contains a repeated human transport step after an experiment has already been designed, frozen, implemented, and provider-free validated:

```text
freeze experiment contract
    -> implement
    -> validate exact source head
    -> user manually presses Run workflow
    -> inspect result
```

The manual button press is not itself a methodological safeguard. The safeguards that matter are whether the experiment is preregistered, whether the exact implementation head is known, whether required provider-free gates passed, whether the intended live workflow is the only workflow that can be launched, and whether the launch is auditable.

The Specification 017 preservation work also produced direct control-plane evidence that an owner-created GitHub issue can trigger a default-branch Actions workflow without a manual Actions UI step. That proof used no new provider call.

The design question is therefore:

> Can ADS replace the repeated manual workflow-dispatch click with a narrow, auditable, owner-authorized launcher while preserving or strengthening the existing preregistration and exact-head gates?

## 2. External platform facts relevant to the design

Current GitHub Actions documentation establishes two important constraints.

1. A `workflow_dispatch` workflow must exist on the repository default branch to receive dispatches.
2. Events created with the repository `GITHUB_TOKEN` normally do not recursively start workflows, but `workflow_dispatch` and `repository_dispatch` are explicit exceptions and do create workflow runs.

References:

- https://docs.github.com/en/actions/concepts/security/github_token
- https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows
- https://docs.github.com/en/rest/actions/workflows#create-a-workflow-dispatch-event

These facts make a two-stage GitHub-native control plane feasible:

```text
owner-created issue event
    -> default-branch launch gate
    -> validated workflow_dispatch
    -> exact experiment branch/ref
    -> experiment-owned live workflow
```

## 3. Design goals

The launcher should remove only the repeated transport burden. It must not weaken the scientific or operational boundary around live provider calls.

Required properties:

- owner-only launch authority;
- a fixed repository-controlled experiment registry;
- no workflow path, shell command, branch, SHA, model, prompt, or secret supplied by issue text;
- exact source SHA verification immediately before dispatch;
- explicit required-CI evidence tied to that exact SHA;
- exact confirmation token identity;
- duplicate-launch rejection for the same frozen authorization;
- least-privilege launcher permissions;
- no provider secret in the launcher job;
- clear accepted/rejected issue comments;
- target live workflow remains independently responsible for checking its own frozen branch/SHA/confirmation boundary before provider execution.

## 4. Non-goals

This launcher is not:

- a generic remote shell;
- a general GitHub workflow runner;
- an experiment scheduler;
- an autonomous experiment designer;
- permission for ADS to run arbitrary live model calls;
- a replacement for experiment-specific preregistration;
- a replacement for provider-free CI;
- a replacement for target-workflow safety checks;
- a production deployment system.

## 5. Threat model

### 5.1 Public issue creation

The repository is public. An arbitrary GitHub user may be able to create an issue that resembles a launch request.

Mitigation:

```text
github.actor
issue.user.login
repository owner
    must all resolve to the frozen authorized owner
```

The launcher must reject before dispatch if any actor identity check fails.

### 5.2 Issue-text injection

A malicious issue could attempt to place a shell command, alternate workflow path, ref, or SHA into the title/body.

Mitigation:

- issue text is parsed only as a launch identifier plus an exact confirmation token;
- all executable launch configuration comes from the repository registry;
- no `eval`;
- no command interpolation from issue body;
- no issue-supplied workflow file, ref, SHA, command, model, or arguments.

### 5.3 Branch movement race

The launcher may verify a branch and then dispatch after the branch moves.

Mitigation is two-sided:

1. launcher checks the branch current SHA equals the registry `expected_source_sha` immediately before dispatch;
2. target live workflow receives the expected SHA and must reject before provider execution unless `github.sha` equals that exact SHA.

The second check is authoritative against a check-dispatch race.

### 5.4 Stale or unrelated CI

A green workflow from another commit must not authorize a live run.

Mitigation:

- the registry stores the exact required workflow-run IDs for the frozen source head;
- the launcher fetches each run and checks exact repository, expected workflow name, expected source SHA, completed status, and `success` conclusion.

This intentionally favors explicit evidence over heuristics such as "latest green run".

### 5.5 Duplicate launches

Opening multiple identical issues must not multiply provider runs.

Initial V1 policy:

- every authorization has an immutable `launch_id`;
- the launcher rejects if the target live workflow already has a queued, in-progress, or completed run for the exact expected source SHA after the authorization became active;
- any intentional replacement attempt requires a new registry authorization with a new `launch_id`.

This is conservative. Retry policy can become richer later if evidence justifies it.

### 5.6 Privilege concentration

The issue-facing launcher should not have the provider secret.

Mitigation:

```text
launcher workflow
    permissions: actions write, contents read, issues write
    provider secret: absent

experiment live workflow
    provider secret: available
    contents write: not required
```

This separates launch authority from provider execution credentials.

## 6. Proposed registry

A repository-owned JSON registry should define every launchable experiment. Issue text selects an existing `launch_id`; it cannot define launch behavior.

Candidate record:

```json
{
  "launch_id": "spec018-probe-001",
  "enabled": true,
  "owner_login": "shakaarlatief",
  "workflow_file": "v1-live-launcher-probe.yml",
  "ref": "v1-autonomous-live-experiment-launcher",
  "expected_source_sha": "<exact sha>",
  "confirmation": "RUN_SPEC018_PROBE_001",
  "required_ci_runs": [
    {
      "run_id": 123,
      "workflow_name": "V1 autonomous live experiment launcher"
    }
  ]
}
```

The first real provider-backed experiment should receive a separate authorization record only after its own contract and implementation are frozen.

## 7. Issue request contract

The issue should be deliberately boring and exact.

Title:

```text
[ADS LIVE] <launch_id>
```

Body:

```text
authorization: <exact registry confirmation token>
```

No other issue field participates in dispatch configuration.

## 8. Launch algorithm

```text
issue opened
    -> verify repository and owner actor
    -> parse exact title/body grammar
    -> load registry from trusted default-branch checkout
    -> require launch_id exists and enabled
    -> require registry owner matches actor and issue author
    -> verify branch current SHA == expected_source_sha
    -> verify each frozen CI run ID:
         head_sha == expected_source_sha
         workflow name == expected
         status == completed
         conclusion == success
    -> reject duplicate authorization if already launched
    -> POST workflow_dispatch for registry workflow/ref
       with exact launch_id, expected_source_sha, confirmation
    -> comment accepted dispatch metadata on issue
```

Every rejection must fail closed and comment a bounded reason without exposing secrets.

## 9. Target live workflow contract

The launcher is only one layer. A launchable provider workflow must independently validate:

```text
inputs.launch_id == frozen expected launch_id
inputs.confirmation == frozen confirmation
inputs.expected_source_sha == frozen source SHA
github.sha == inputs.expected_source_sha
current branch/ref == frozen branch
required provider secret exists
provider-free preflight passes
```

Only after those checks may provider execution begin.

For a provider-free probe workflow, the same checks apply except no provider secret or provider call exists.

## 10. Validation strategy

### Layer A: pure parser and registry tests

Test owner acceptance and all fail-closed cases without GitHub network calls.

### Layer B: mocked GitHub API launch tests

Exercise exact SHA, CI-run, duplicate, and dispatch behavior against a fake client.

### Layer C: workflow static checks

Assert minimum permissions and confirm that the issue body cannot provide workflow/ref/SHA/command values.

### Layer D: end-to-end provider-free probe

After exact branch CI is green:

1. expose the launcher and a harmless probe workflow on the default branch;
2. register one exact probe authorization;
3. create the launch issue through the connected GitHub interface;
4. require launcher acceptance;
5. require a `workflow_dispatch` probe run without manual UI interaction;
6. require the probe to verify exact SHA/confirmation and perform no provider call.

A successful probe is control-plane evidence only.

## 11. Promotion boundary

A successful launcher probe may promote the following bounded capability:

> ADS development can autonomously transport an already authorized frozen live experiment from an owner-created issue request into an exact allowlisted GitHub Actions dispatch without a repeated manual Actions UI click.

It must not promote:

- arbitrary autonomous live-model execution;
- autonomous experiment design;
- autonomous retries;
- arbitrary workflow execution;
- final production operations/deployment policy;
- final approval/escalation policy.

## 12. Recommended next step

Freeze a narrow technical Specification 018 around this control plane, implement it provider-free, validate the exact head in CI, then run exactly one provider-free end-to-end probe. Only after that should the next recommendation/action experiment be preregistered and authorized through the new mechanism.