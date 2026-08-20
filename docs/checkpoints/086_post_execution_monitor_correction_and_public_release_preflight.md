# Checkpoint 86: Post-Execution Monitor Correction and Public-Release Preflight

**Date:** 2026-08-19  
**Status:** Observer-only defect corrected after held-out execution; public-release audit has no blocking findings; local test confirmation pending  
**Checkpoint class:** EXPERIMENT_VERIFICATION  
**Project stage:** Prototype V0 held-out execution and evaluation  
**Scope:** Records the historical milestone described by this checkpoint: Post-Execution Monitor Correction and Public-Release Preflight.  
**Authority:** Historical provenance for the recorded experiment milestone; frozen experiment contracts and final experiment conclusions govern their declared scopes.  
**Design session:** 01  
**ChatGPT project:** Autonomous Data Science System  
**Session title:** 01 - Foundations & Checkpoint 0

## Purpose

This checkpoint records two post-execution maintenance findings that do not alter the completed Prototype V0 treatment evidence:

1. a read-only live-monitor counting/display defect discovered from the completed unattended run log; and
2. the first conservative repository/history audit performed in preparation for eventual public release.

Neither item changes B0, B1, P0, the frozen benchmark, the registered protocol, the completed attempt artifacts, the supervisor decisions, or the semantic rubric.

## Read-only monitor defect observed

During the final unattended run, the monitor repeatedly printed output of the form:

```text
verified=35 integrity_failures=index
```

while the authoritative final supervisor export reports:

```text
attempts_verified: 34
integrity_passed: 34
integrity_failed: 0
```

The discrepancy is therefore not an experiment-integrity failure.

## Root cause

`heldout_monitor.py` scanned every `*.json` file in the mechanical-verification directory as though it were an attempt-level verification report.

That directory also contains the aggregate metadata file:

```text
index.json
```

Because `index.json` has neither an attempt-level `attempt_id` nor an attempt-level `integrity_status`, the observer:

```text
counted it as one additional verification report;
and interpreted its missing integrity_status as a failure whose fallback name was "index".
```

This explains both visible symptoms:

```text
verified count was exactly one too high
integrity_failures=index appeared despite zero verifier integrity failures
```

The defect existed only in the optional read-only display layer. The validated supervisor and verifier did not use the monitor output to decide whether to run, replace, stop, or accept an attempt.

## Correction

`prototype_v0/src/ads_v0/heldout_monitor.py` now counts a JSON object as an attempt-level verification report only when:

```text
attempt_id is a string
integrity_status is exactly PASS or FAIL
```

Aggregate metadata such as `index.json` is ignored by the live report count.

`prototype_v0/tests/test_heldout_monitor.py` now explicitly places an `index.json` beside two attempt-level reports and asserts that:

```text
verification_reports == 2
only the genuine FAIL attempt is listed as an integrity failure
```

This is a post-execution observer correction. It does not retroactively modify any treatment trajectory or supervisor artifact.

## Public-release audit

A conservative public-release audit script and workflow were added before this checkpoint:

```text
scripts/public_release_audit.py
.github/workflows/public-release-audit.yml
```

The local audit was run against the full current repository plus reachable Git history.

Observed result:

```text
current_tracked_files: 158
historical_paths: 158
history_blobs_scanned: 321
history_blobs_skipped_large: 0
large_history_blobs: 0
blocking_findings: 0
warnings: 4
RESULT: PASS WITH WARNINGS
```

Warnings:

```text
1. one non-noreply commit email would become visible if the repository becomes public;
2. no LICENSE has yet been selected;
3. one current historical checkpoint contains an absolute Projects_Data path;
4. one older CURRENT_STATE blob in reachable history contains an absolute Projects_Data path.
```

No scanned credential/token/private-key finding was reported. No tracked generated/results runtime directory was reported.

The absolute path references are privacy/repository-cleanliness warnings rather than secret findings. The historical occurrence cannot be removed merely by editing the current file; doing so would require history rewriting, which is not justified at this stage.

## Publication boundary

The repository remains private.

This is still the preferred state until:

```text
blinded semantic judging is complete;
manual blinded adjudication is complete where required;
condition identity has been decoded only after consensus is frozen;
the final V0 interpretation is recorded;
a license decision is made;
and the release audit is rerun immediately before changing visibility.
```

## Validation still required

The monitor correction was made after the final held-out treatment execution. Before using the repository for semantic-judge execution, the local deterministic test suite should be run once after pulling this checkpoint's changes.

No treatment rerun is authorized or required.

## Promotion audit

The monitor correction is a scoped implementation-maintenance fact and this checkpoint is sufficient provenance. It does not warrant a new foundation or experimental protocol amendment.

The public-release preflight result should remain a current-state/release-preparation concern rather than a new system principle.
