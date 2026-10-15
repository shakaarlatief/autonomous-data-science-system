# Validation 260: R0-P03 arm-author controlled-write and host boundary

**Date:** 2026-10-15
**Status:** NATIVE_WRITE_BUILD_PASS / PROPOSED_SOURCE_OUTPUT_BOUNDARY_FAIL / TIGHTER_PROFILE_NOT_EXERCISED / COMPLETE_HOST_NOT_QUALIFIED
**Scope:** Validate the synthetic native command observation, conservative classifications, candidate metadata and preservation checks without certifying an author host.
**Parent:** Research 571; Research 513/559/568/570; Checkpoint 898.
**Baseline:** Clean `v1-source-vault-bootstrap-resume`, HEAD `97a311a6c59ee999c11afa9a9896178ac7fa0de5`, empty index. Native Desktop Codex/codex-01 investigates; ChatGPT/chatgpt-39 owns independent acceptance.

## Actual execution and receipts

1. Local metadata: `whoami` reported `CodexSandboxOffline`; installed PATH Codex 0.154.0 and Claude 2.1.283 help inspected. Read relevant scientific, role/custody, implementation and operational contracts. No bridge operation, private repo access, protected owner-canary access or account/ACL mutation.
2. Installed CLI generated its experimental protocol schema into standalone `%TEMP%/ads-p03-author-inspect-yq2mrfjg/schema`, exit 0. Temporary-home `app-server --strict-config --stdio` initialization and sequential `config/read` accepted the exact source-read/artifact-write/root-deny profile preserved in Research 571 and the public receipt. An earlier pipelined EOF returned only initialization, not a config result. No thread, model turn or sandbox command launched. Helper-alias refusal and failed plugin-cache HTTPS fetch are retained; neither is a file/network enforcement pass.
3. One native invocation: `.venv/Scripts/python.exe -B -m experiments.r0_p03_navigation_probe.arm_author_synthetic_preflight`. Reused the existing fixture preparer outside all public Git worktrees/private checkout roots. Actual scratch `%TEMP%/ads-p03-host-runs0yia`. Expectations saved before probes, SHA-256 `afcd673774fae79234811cb95fbfdc6c4552dfd08bc1ba89d303550f42aeb08c`.
4. Two exact permitted reads, exact two-name/literal search, create/modify architecture code, exit-0 separate-process test, forbidden-marker-free synthetic report and exact cross-context report readback all succeeded. **Eleven prohibited Python read probes** also succeeded (nine original forbidden paths, including direct/junction routes to the same target, plus fake key/log). Alternate PowerShell fake-answer read, deleted fake-answer Git-history read, child executable and outside-artifact output write succeeded. These are access/output **failures for the proposed boundary**, not OS/tool denials.
5. Native CRLF exact-byte comparison defect was corrected from existing saved counts/hashes/base64 output, without rerunning successful probes. Original raw receipt retained and bound by hash. Added native-newline regression coverage. All eleven original path comparisons and the alternate shell comparison match exact fabricated bytes after correction.

Reproduction of the command observation: run the module above; it creates only a new standalone synthetic fixture and returns **NOT_QUALIFIED**. It launches no model or permanent server and accepts no arbitrary target root. It creates a disposable fake Git-history commit; it does not commit in ADS. Raw evidence has exact subprocess argv/stdout/stderr and fixture/report hashes. Public `experiments/r0_p03_navigation_probe/arm_author_synthetic_receipt.json` normalizes home/run paths, carries config/binary/evidence commitments and distinguishes the correction. Original raw evidence is retained in Temp, not asserted to be a durable authority-bearing store.

## Focused verification

```text
.venv/Scripts/python.exe -B -m pytest -q
  tests/unit/test_r0_p03_arm_author_preflight.py
  tests/unit/test_r0_p03_restricted_host_preflight.py
  tests/unit/test_r0_p03_source_only_access.py
  tests/unit/test_r0_p03_source_only_capsule.py
  --basetemp=.venv/.p03-author-preflight-tests
```

**95 passed in 52.00s.** One pre-existing pytest-cache write `PermissionError` warning; no test failure. Eight new receipt/classification cases distinguish successful mismatched reads, missing target, OS permission errors, other I/O failure and the inability of command observations alone to certify a model host. Existing reviewer preflight, source API and capsule regression tests also passed. Mocked error tests do not establish a new actual OS denial. No tests or probes invoked Claude/model inference.

The deterministic six-component repository-integrity gate, scoped preservation assertions and whitespace results are recorded at final postflight below. They validate preservation and artifacts, not arm-host confinement.

Final postflight: `scripts/check_repository_integrity.py --checked-branch v1-source-vault-bootstrap-resume` **6/6 PASS**, `PUBLIC_REPOSITORY_INTEGRITY=PASS`. The initial run correctly rejected missing Scope metadata on both new documents; metadata was added and the full gate rerun successfully. **16 preservation assertions PASS**: unchanged HEAD/branch/index/routing/checkpoint, exact four modified plus five new files, retained phase/ownership/history, genuine codex-01 identity, owner provenance reconciled to chatgpt-39, scrubbed receipt and conservative qualification. `git diff --check` PASS and all five new files separately checked for whitespace. No ADS staging, commit or push.

## Qualification and stopping boundary

```text
CURRENT_NATIVE_COMMAND_USEFUL_WRITE_BUILD=OBSERVED
CURRENT_NATIVE_PROPOSED_SOURCE_AND_OUTPUT_EXCLUSION=FAIL
TIGHTER_CLI_PROFILE_CONFIG_PARSE=OBSERVED
TIGHTER_CLI_SANDBOX_ENFORCEMENT=NOT_EXERCISED
NEW_MODEL_INFERENCE_INVOCATIONS=0
NEW_ACTUAL_OS_OR_TOOL_DENIAL=NONE_CLAIMED
MODEL_TOOLS_CONTEXT_NETWORK_CONNECTOR_CUSTODY=NOT_QUALIFIED
COMPLETE_B0_B4_AUTHOR_HOST=NOT_QUALIFIED
REAL_GOLD_OR_ARMS_OR_SCORE=NONE
CHECKPOINT_AND_ROUTING=898_UNCHANGED
```

Installed help/config are not model tools. Same `CodexSandboxOffline` account name does not prove identical token/profile enforcement across Desktop, model-free bridge commands and App Server agents. No bridge bootstrap network flag is attributed to the tested native process. Existing protected owner-canary denial remains preserved; new unprotected fake stand-ins do not contradict it. Browser/network/MCP/connectors/delegation, fresh context, actual provider transcripts, owner key custody and complete packet recovery remain unexercised/unqualified.

Smallest owner dependency: review/authorize the exact Windows sandbox backend/setup/ACL scope for one synthetic model-free launch of the parsed experiment profile and an appropriate dedicated home; stop on effects outside the approved scope. No request to widen source access, change global ADS workflow, borrow production credentials or repeat the already successful owner-canary test. Only after the host boundary is viable should a fresh model-facing test and separate synthetic owner-key/output recovery proceed. No real task/reference/arm freeze is justified.
