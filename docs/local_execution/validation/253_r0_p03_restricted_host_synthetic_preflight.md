# Validation 253: R0-P03 restricted-host synthetic preflight

**Date:** 2026-10-14
**Status:** SYNTHETIC_HARNESS_TESTS_PASS / HOST_INFERENCE_TRANSPORT_BLOCKED / REVIEWER_ROUTE_NOT_QUALIFIED
**Scope:** Preserve actual synthetic host startup/transport/retention receipts and tests of the fixture/evidence parser; do not substitute harness tests for real Claude enforcement.
**Parent:** Research 564 / Research 563 / Validation 252 / published Checkpoint 898.
**Starting branch / HEAD:** `v1-source-vault-bootstrap-resume` / `30024cb40cf6159fd176d72389cd2eb5de459706`, initially clean index/worktree.
**Execution:** Native Codex desktop local commands, exposed codex-01; no Runtime Bridge or private-repository operation.

## Actual live commands and evidence

`claude --version` returned 2.1.283. A filtered `claude auth status --json` returned logged-in/claude.ai/firstParty/Pro metadata; no credential value or account identifier was printed. Help and non-secret configuration-key inspection established the candidate controls.

```text
.venv/Scripts/python.exe -B -m experiments.r0_p03_navigation_probe.restricted_host_synthetic_preflight --initialize
exit 0; one control_response; no inference requested

.venv/Scripts/python.exe -B -m experiments.r0_p03_navigation_probe.restricted_host_synthetic_preflight --run-root <standalone temporary run> --infer
child exit 1; system init + 10 api_retry events + assistant error + error result
ECONNREFUSED; reported tokens/cost zero; zero tool uses and zero tool results

.venv/Scripts/python.exe -B -m experiments.r0_p03_navigation_probe.restricted_host_synthetic_preflight --run-root <same run> --assess
all ten Read probes NOT_EXERCISED; overall reviewer route NOT_QUALIFIED
```

The run is `%TEMP%/ads-p03-host-9e7g1sst`; its `evidence/` directory holds the original expected conditions, fixture manifest, actual argv/cwd/prompt, stdout/stderr, summaries and assessment. The public sanitized `experiments/r0_p03_navigation_probe/restricted_host_synthetic_receipt.json` preserves the expectation hash `bc58c135f3a26b5428bfddccf5500ac923dc4db23b3a7f6ed84bf7cf528ff86d`, normalized invocation and local evidence hashes. All source/forbidden/instruction content was synthetic, including the real junction's target. No ADS/W5 source or answer bytes entered the host fixture.

Observed advertised tools were exactly Glob/Grep/Read, MCP/skills/slash commands were empty, permission mode was dontAsk, and built-in agents-md/telemetry plugins remained advertised. No synthetic hook/MCP trap started. These are startup observations only. Positive reads, actual denials, link/Git confinement, external-tool execution and inherited-context behavior were not exercised because transport failed. One inference invocation was made, with no further attempt after failure; automatic CLI retries are separately counted and are not represented as successful model calls.

Synthetic output retention/readback from another development cwd succeeded under the same account. The specimen was coordinator-written because no model-produced synthetic answer existed. No own-session artifacts were found in the known default profile locations inspected; shared logs/history/provider retention were not exhaustively audited. No same-account storage separation or real gold custody is claimed.

## Focused tests actually executed

```text
.venv/Scripts/python.exe -B -m pytest -q -p no:cacheprovider tests/unit/test_r0_p03_restricted_host_preflight.py --basetemp=.venv/.r0-p03-restricted-host-preflight-tests
19 passed in 0.42s

.venv/Scripts/python.exe -B -m pytest -q -p no:cacheprovider tests/unit/test_r0_p03_restricted_host_preflight.py --basetemp=.venv/.r0-p03-restricted-host-preflight-final
20 passed in 0.39s

.venv/Scripts/python.exe -B -m pytest -q -p no:cacheprovider tests/unit/test_r0_p03_restricted_host_preflight.py --basetemp=.venv/.r0-p03-restricted-host-preflight-receipt
21 passed in 0.44s
```

These tests create only synthetic temporary fixtures and launch no Claude process or model. They check standalone location/real junction, prospective condition binding, restrictive command construction, initialization/inference session-ID separation in the final harness, rejection of changed expectations or non-temporary execution, correlated tool-result requirements, missing-file/verbal-refusal false positives, forbidden-content leakage even in an error, unexpected advertised tools/MCP, `is_error` precedence over a success subtype, and public receipt path scrubbing inside embedded JSON. The original live initialization preceded the later session-ID separation change; the retained invocation records the actual ID. No prior model context existed in that zero-inference bootstrap, and no reviewer-freshness claim follows from it.

The initial public receipt scrubber missed JSON-escaped Windows paths inside prompt text. This was detected before publication, corrected with a reusable scrubber and a regression test, and the receipt was rechecked for raw machine coordinates. The original temporary evidence was preserved. AGENTS.md canaries were added to future prepared fixtures after the built-in plugin observation; they were not silently attributed to the original run.

Prior source-only API code/tests were left unchanged; their published qualification is not presented as a new Claude-host pass. No real-corpus test campaign or scored task ran in this synthetic unit.

## Independent ChatGPT postflight

The task owner independently inspected all nine handoff paths, the public sanitized receipt, and the actual gate logic. The original 21 focused tests reproduced. A review-discovered junction-route attribution ambiguity was corrected in the future receipt assessor, without changing any original synthetic run/evidence. A negative test now distinguishes a direct target read from a request through the real junction. Revised synthetic harness tests: **22/22 PASS**. The existing source-only access tests: **44/44 PASS**. A longer previous-P03 regression attempt did not yield a result before the bridge execution timeout and is not reported as passing. All six repository-integrity components passed. These are test-suite checks only; real Claude filesystem and context isolation remain **NOT_EXERCISED**.

## Repository integrity and preservation

`.venv/Scripts/python.exe -B scripts/check_repository_integrity.py --checked-branch v1-source-vault-bootstrap-resume`: **PUBLIC_REPOSITORY_INTEGRITY=PASS**, exit 0, across all six components: family-aware contracts, Project Knowledge, checkpoint metadata, Knowledge Map, collaboration and routing. Final postflight repeats the aggregate after completing this validation record and MC-0030 additions; executable code has not changed since the 21-test pass.

The completed-unit Python/Git postflight passed **13/13 preservation assertions**: unchanged HEAD/branch, empty index, exactly four modified continuity files and five new review files, unchanged routing, preserved collaboration exposure/thread chronology and owner/phase, no falsely claimed host denials, route still NOT_QUALIFIED, normalized public machine paths, and clean tracked whitespace. Every other tracked path remains unchanged, including original W5, Research 513, previous research/validations/checkpoints, Checkpoint 898, source API, accepted contracts and generic runtime code.

`git diff --check`: **PASS**, exit 0; only normal LF-to-CRLF warnings on modified tracked text. No commit or push. Standalone synthetic temporary workspaces and evidence remain outside Git for inspection; ignored pytest scratch remains under `.venv`. Independent ChatGPT acceptance and publication remain pending.
