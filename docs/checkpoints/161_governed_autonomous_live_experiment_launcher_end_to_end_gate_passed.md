# Checkpoint 161: Governed Autonomous Live Experiment Launcher End-to-End Gate Passed

**Date:** 2026-08-23  
**Status:** BOUNDED CONTROL-PLANE GATE PASSED / PROMOTION SUPPORTED  
**Checkpoint class:** CONTROL-PLANE EXPERIMENT RESULT / PROMOTION BOUNDARY  
**Project stage:** Post-V0 bounded V1 implementation and integration  
**Scope:** Records exact provider-free implementation, cross-platform CI, autonomous issue-to-dispatch probe evidence, bounded promotion, and the next authorized development boundary.  
**Authority:** Current bounded Specification 018 result boundary. Specification 018 v1.0 is accepted only within the scope stated here and does not authorize arbitrary workflow execution or autonomous experiment design.  
**Design session:** 04  
**ChatGPT project:** Autonomous Data Science System  
**Session title:** 04 - Selective Context Promotion & Reasoning Vertical Slice  
**Branch:** `v1-autonomous-live-experiment-launcher`  
**PR:** #23 -> `v1-frontend-spike`  
**Specification:** 018  
**Outcome:** `GOVERNED_LAUNCHER_SUPPORTED`

## Boundary reached

Specification 018 asked whether ADS development can replace the repeated manual GitHub Actions button press with a narrow repository-governed control plane that still preserves preregistration, exact-source validation, CI evidence, least privilege, and an auditable launch trail.

The bounded provider-free gate passed end to end.

```text
connected GitHub interface
    -> owner-created governed issue
    -> default-branch launcher workflow
    -> repository-controlled authorization registry
    -> exact actor / owner checks
    -> exact source-SHA check
    -> exact successful CI-run check
    -> duplicate-state check
    -> allowlisted workflow_dispatch
    -> provider-free probe workflow
    -> independent exact source / confirmation checks
    -> success
```

No manual Actions UI click was used for the probe launch and no provider credential or provider call participated in the test.

## Exact implementation evidence

Final provider-free implementation head used by the accepted probe authorization:

```text
27e7bc84b5f63d65d43de9a5bd27d1fdc0677071
```

Exact cross-platform provider-free CI run:

```text
run 32660168566
```

Observed on both Ubuntu and Windows:

```text
Specification 018 launcher tests   41 passed
full V1 Python suite               103 passed, 2 skipped
OPENAI_API_KEY                     absent
```

The two skips are the existing PostgreSQL-environment tests gated on `ADS_TEST_POSTGRES_URL`; they are not launcher failures.

## Exact autonomous probe

Governed request issue:

```text
issue 31
[ADS LIVE] spec018-probe-001
authorization: RUN_SPEC018_PROBE_001
```

Launcher workflow run:

```text
32660333663
```

The launcher recorded acceptance with:

```text
launch_id = spec018-probe-001
source    = 27e7bc84b5f63d65d43de9a5bd27d1fdc0677071
```

Exact target probe run:

```text
32660340429
```

Target workflow identity:

```text
name       ADS live spec018-probe-001
workflow   .github/workflows/v1-live-launcher-probe.yml
event      workflow_dispatch
head       v1-autonomous-live-experiment-launcher
head SHA   27e7bc84b5f63d65d43de9a5bd27d1fdc0677071
conclusion success
```

Probe job:

```text
job 97245432893
name probe
conclusion success
```

The probe independently verified:

```text
launch_id            == spec018-probe-001
confirmation         == RUN_SPEC018_PROBE_001
observed ref         == v1-autonomous-live-experiment-launcher
observed source SHA  == expected source SHA
```

and emitted:

```text
ADS_LIVE_LAUNCHER_PROBE_OK source=27e7bc84b5f63d65d43de9a5bd27d1fdc0677071
```

Read-only observer evidence was recorded through issue 32 and observer run `32660375449`.

## What this supports

The evidence supports a bounded V1 control-plane capability:

> An owner-created request may select an already repository-authorized live experiment and cause GitHub Actions to dispatch its exact allowlisted workflow without a manual Actions UI click, provided the launcher verifies the frozen owner identity, source SHA, CI evidence, registry authorization, confirmation, and duplicate state first.

The launcher is not an experiment designer and is not an arbitrary workflow runner.

The issue is transport, not authority. Executable launch behavior remains repository-controlled.

## Security boundary preserved

Specification 018's intended separations held in the provider-free gate:

```text
transport request
    !=
launch authorization

launcher authorization
    !=
provider credential

launcher validation
    !=
target-workflow validation
```

The launcher workflow receives only:

```text
actions: write
contents: read
issues: write
```

and receives no `OPENAI_API_KEY`.

Issue content cannot define workflow paths, refs, SHAs, shell commands, model configuration, prompts, secrets, or arbitrary dispatch inputs.

## Promotion audit

### Promote

1. Promote Specification 018 from frozen provider-free contract to bounded accepted V1 control-plane capability.
2. Promote the repository-controlled launch registry, ADS launcher script, default-branch issue-event launcher workflow, and independent target-workflow verification pattern as the accepted mechanism for future explicitly authorized experiments.
3. Promote the invariant that connected-interface issue creation is transport only; repository state remains the executable authorization source.
4. Promote exact required CI run IDs, exact source SHA, owner identity, confirmation identity, and duplicate-state checks as part of the bounded launch gate.
5. Route `README.md`, `docs/CURRENT_STATE.md`, `docs/KNOWLEDGE_MAP.md`, and `docs/OPEN_QUESTIONS.md` through this checkpoint.

### Do not promote

Do not infer or select any of the following from this control-plane result:

```text
autonomous experiment design
arbitrary GitHub workflow execution
arbitrary issue-driven commands
automatic provider retries
final provider/model
final recommendation/action policy
production human approval/escalation policy
multi-agent architecture
cloud/deployment architecture
automatic project mutation or execution policy
```

The one-shot probe authorization is test evidence, not a standing production authorization. It should be removed or disabled after the evidence is recorded.

## Final reconciled-head validation

Canonical reconciliation and conservative checkpoint-metadata repair were completed before merge.

Exact reconciled PR head:

```text
ea0441b29f18d056106b1c0ccbe9c4fba8c31883
```

Exact final provider-free runs on that head:

```text
Checkpoint metadata                         32661926851  success
V1 autonomous live experiment launcher CI  32661926840  success
V1 disposition semantics diagnostic         32661926806  success
V1 reasoning context value                  32661926796  success
```

The launcher CI passed on both Ubuntu and Windows, including the launcher-specific test suite, full V1 Python regression suite, and provider-credential absence check.

## Next justified boundary

The next scientific experiment remains separate from the launcher.

Before any new recommendation/action provider call:

```text
1. preregister a new recommendation/action-value contract
2. make exact supplied-context provenance system-owned
3. keep model-owned recommendation content separate from provenance
4. implement provider-free
5. validate the exact implementation head
6. add one exact repository-controlled launch authorization
7. use the governed launcher to dispatch the frozen live workflow
8. preserve and interpret the resulting evidence before any promotion
```

No recommendation/action scientific conclusion is changed by this checkpoint.

## Advancement decision

```text
GOVERNED_LAUNCHER_SUPPORTED
```

The bounded control-plane hypothesis earned promotion. The next project work should use this mechanism rather than returning to repeated manual `workflow_dispatch` button presses for explicitly authorized frozen experiments.
