# Validation 393: Executed B0-B3 navigation channels on actual V03 experimental source world

**Date:** 2026-11-15
**Status:** FOUR_DISTINCT_CHANNELS_ACTUALLY_EXECUTED / FULL_GIT_SOURCE_CONTENT / 27_FOCUSED_TESTS_PASS / UNSCORED_AND_EXPOSED
**Research:** 696. **Checkpoint:** 957. **Collaboration:** MC-0030 Message 110.
**Scope:** Verify real B0/B1/B2/B3 ranking differences and evidence nonpromotion on the 24-source exact Checkpoint 954 original-Git experiment-only V03 pilot, never formal scored evaluation.

The executable and exposed coordinator-authored metadata are both strictly source-bound. Original source Git `17ea403ef64092f275e3c7d6492d99929804f8e5`; 24 source files, 459,438 UTF-8 bytes, 2,435 BM25 passages without the old 12,000-character source cap. Source metadata SHA-256 `e605d20259372e7583a1e7c52f22740279e09bc1435e22fbd741d53563295034`. Original W5 Research 217 subject vocabulary SHA-256 `53c5cb65caccd1a9123f5d6da2e5738f618b383339c5bcfcf1d58fb9f5399495`.

Program output is create-only and repeatable. SHA-256:

    bda8b2d64152d01f9e2b70487c275ab9c1ede8ceb833729fac6e88adbc18e309

Executed seven exposed engineering queries each through B0 full-source passage BM25, B1 catalog topic membership, B2 nonduplicate editorial source-link graph, and B3 distinct concerns. Rank ordering differed from B0 in 3/7 B1, 3/7 B2, 4/7 B3 cases. **This is actual behavioral differentiation, not a scored quality result.**

The new regression test suite passed **27 focused tests** including negative authority elevation, nonexistent B4, B1 unassignable subjects, B2 duplicate documentary path edges, B3 invalid concerns, full-source indexing, Git source identity, query budget and all-arm common semantics. Existing source-role/shared-runtime and J3 regressions remain independently required.

```powershell
.venv\Scripts\python.exe -m experiments.r0_p03_navigation_probe.v03_r0_p03_actual_navigation_channels_unscored_v01
.venv\Scripts\python.exe -m pytest -q --tb=short --maxfail=2 -p no:cacheprovider tests/unit/test_r0_p03_v03_actual_navigation_channels_unscored_v01.py
```

No formal 60/20 selected, no independent owner-authored source metadata, no protected source-relative gold, no new primary task or neutral 9-case legacy adjudication. The current Python venv lacks importable neural B4 packages; formal B4 inclusion remains a future prefreeze decision. Production acceptance and physical architecture remain unchanged.

GitHub publication and exact CI status must be verified separately at the final committed head.
