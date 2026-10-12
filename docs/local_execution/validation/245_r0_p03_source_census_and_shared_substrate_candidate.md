# Validation 245: R0-P03 source-census and shared-comparison-substrate candidate

**Date:** 2026-10-12
**Parent:** Research 557 / Checkpoint 893 / Research 513 and 556.
**Status:** 11_CANDIDATE_CENSUS_AND_CONTRACT_TESTS_PASS / PUBLIC_PREFLIGHT_PASS
**Scope:** Source-frame sampling-feasibility and semantic comparison-boundary design qualification; no navigation-arm construction, task authoring, owner signing, or scored result.

## Tested implementation

Added:
- `experiments/r0_p03_navigation_probe/source_census.py` as a read-only exact-Git-source-bound population audit, without any cohort/salt/gold allocation.
- `experiments/r0_p03_navigation_probe/common_substrate_contract_candidate.json` as an explicitly unfrozen shared V03 and B0-B4 comparison schema candidate.
- `tests/unit/test_r0_p03_source_census.py` as focused structural/corpus-provenance checks.

Executed:
```text
python -B -m pytest -q -p no:cacheprovider tests/unit/test_r0_p03_source_census.py --basetemp=.venv/.r0-p03-census-893B
11 passed in 0.56s
```

Ran the census over source ref `22a63604e382f73b7fe661937ed4852ecf7da672`:
- 10 source-family candidate strata, exact Git blobs, unique pool paths.
- Pool cardinalities: 12, 25, 28, 119, 56, 120, 200, 16, 693, 264.
- Sum **1533 distinct paths**; no overlap; each source frame offers at least 8 candidate paths.
- Proposed quotas **6 build + 2 held-out** per stratum; anchors are explicitly BUILD-only candidates; no exact cohort or hidden answers generated.

The tool's pool partition and test pass do not prove present authority, semantic relevance or equal task difficulty.

## Comparison consistency

- Common baseline is role/natural owner + exact effect governed subjects + lineage/currentness + completion + J2 coverage + evidence/receipts + authority status + lexical retrieval + connector-readable derived orientation.
- B1 topical subjects, B2 editorial/about links, B3 navigation concerns and B4 probabilistic retrieval are *additions*, not special baseline-only privileges.
- B2 extra links cannot silently duplicate already common J2 or lineage relation edges or claim new authority.
- All source facts must retain Git provenance, governing status source and unresolved status where necessary; future-V03 analogue data must be marked synthetic.
- Old Research 217 evidence and explicit owner R0-P01 deferral are unchanged.

## Public integrity and publication checks

Executed again after routing and source additions:
- `python -B -m pytest -q -p no:cacheprovider tests/unit/test_r0_p03_source_census.py --basetemp=.venv/.r0-p03-census-893-final`: **11/11 PASS in 0.44 seconds**.
- `python -B scripts/check_repository_integrity.py --checked-branch v1-source-vault-bootstrap-resume`: **PUBLIC_REPOSITORY_INTEGRITY=PASS** (family-aware repository, Project Knowledge, checkpoint metadata, Knowledge Map, model collaboration state and current routing all PASS).
- `git diff --check`: **PASS**, aside from platform LF/CRLF worktree normalization warnings.
- Changes are scoped to this candidate census/test/schema, Research 557, Validation 245, Checkpoint 893 and four ordinary route/current-state/knowledge-map/collaboration pointers.
- No observed P03 navigation score, arm-performance implementation, exact corpus freeze, hidden holdout fixture or result-dependent tuning occurred.

Commit/push and remote HEAD verification are separate guarded steps; this section records only actual precommit checks.

## Limitations

No independent Claude response, sealed independent cohort custodian, semantic/currentness gold oracle, P03 corpus freeze, fresh evaluators or navigation performance scores exist. No historical Research 513 threshold or previous results were altered, and no production authority or migration operation was performed.
