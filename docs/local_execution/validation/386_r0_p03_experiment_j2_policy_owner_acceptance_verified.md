# Validation 386: Exact recorded-chat acceptance of P03 REV01 assurance policy

**Date:** 2026-11-15
**Status:** SOURCE_BOUND_POLICY_ACCEPTANCE_PASS / ORIGINAL_SOURCE_GIT_VERIFIED / 83_FOCUSED_TESTS_PASS / J2_S1_J3_UNQUALIFIED
**Research:** 689. **Checkpoint:** 950. **MC-0030:** Message 103.
**Scope:** Verify exact independent-from-source-file conversational owner decision binding for the previously published one-event experimental natural-owner policy.
**Authority:** Developer research-workflow acceptance evidence only, not independently authenticated human or model identity, J2 coverage, new source execution, J3 or formal B0–B4 selection.

Inputs:

    Proposal Git: 3dc76841973e75af201c4036007e95f06d10545d
    Proposal raw SHA-256: f0217d8c24aba8aa5a5d493d6c816f9e439de4e32f32c00d56665b075ead798f
    Exact user message: ACCEPT
    Binding SHA-256: beabc995359f79fe8d4f659efa76ff912b8ec02de74397d3656c29438215672d
    Accepted-policy receipt SHA-256: 2ae70ec2fabbc7dbe541811a9468ae2285e1461ef223a3eef4dbcdd02c8782ff

Executed:

```powershell
.venv\Scripts\python.exe -m experiments.r0_p03_navigation_probe.v03_real_pk_j2_experiment_assurance_accepted_policy_rev01
.venv\Scripts\python.exe -m pytest -q --tb=short -p no:cacheprovider tests/unit/test_r0_p03_v03_real_pk_j2_accepted_policy_rev01.py tests/unit/test_r0_p03_v03_real_pk_j2_experiment_assurance_preflight_rev01.py
```

Observed: **83 passed in 3.20s**. Original proposal was verified directly from Git; original predecision source and receipt remain unchanged and valid. The frozen policy is now owner-accepted for its narrow research-development purpose, but the source-author principal remains only recorded-chat/exposed-session assurance, not cryptographic model authentication.

The receipt states that this acceptance cannot be used before publication, cannot apply retrospectively to Checkpoint 948 and does not itself admit any current or future J2. New composite realizer and source scope need independent preaction freeze, then a new exact event and genuinely fresh G006/G013 execution, postexecution COVERS and separate J3. J2=0, S1 not activated, J3 HOLD.

Repository-integrity, publication, working tree and GitHub checks are evaluated at the eventual preserved head, not inferred from the focused pytest result.
