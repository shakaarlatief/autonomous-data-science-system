# Validation 266: Fictional S1 role-boundary and public-receipt policy adversarial trial

**Date:** 2026-10-20
**Status:** SYNTHETIC_POLICY_MECHANICS_PASS / IDENTITY_ALIAS_NEGATIVE_CONTROL_OBSERVED / REAL_SECURITY_HOLD
**Scope:** Test mock reviewer/challenger/authorizer permissions, caller-declared role spoofing, role continuity across fictional sessions, public-receipt leakage constraints, typed release witnesses and actual-inspection-vs-self-assertion boundaries. Preserve the earlier source-free journal/transport regressions.
**Basis:** Research 597–598, Validation 264–265, R0-P03 prospective V0.4 review method, and existing retained scientific gates.
**Authority:** Fictional engineering results only. This is **not** a real reviewer admission, verified ACL, secure reviewer ledger, source-status adjudication, author-world freeze, hidden gold, scoring or production deployment.

## 1. Exact trial components and content boundary

```text
Implementation:
  experiments/r0_p03_navigation_probe/s1_role_boundary_synthetic.py

New unit tests:
  tests/unit/test_r0_p03_s1_role_boundary_synthetic.py

Regression modules:
  tests/unit/test_r0_p03_s1_transport_custody_synthetic.py
  tests/unit/test_r0_p03_synthetic_custody_evidence_candidate.py

Source marker:
  S1_SYNTHETIC_ROLE_BOUNDARY_NO_PRIVATE_CONTENT

Input:
  invented mock principal/session identifiers, known role labels,
  caller-declared booleans, fake disclosure and metadata flags

No actual:
  historical source batches, Research 217/W5 private gold,
  real reviewer ledger, Runtime API keys, Windows ACL modifications,
  new user accounts, private destination, external app/provider
  connection, service deployment or scored experiment
```

The new module is a **pure, local fictional policy simulator** with no production author-release operation. Its role checks trust a simulated assignment directory created by test code, not authenticated operating-system, cloud, tunnel or LLM principals.

## 2. Performed test run

An initial run of the new role-boundary tests with the earlier S1 and fictional custody regressions returned:

```text
52 passed in 0.42s
```

A negative-control test was then added to demonstrate **identity-alias defeat**: an actor exposed to mock restricted material could register a fresh, unlinked fake principal and thereby pass the simulated blind-author role check. That intentionally permitted result is evidence of a missing identity-link mechanism, **not** evidence that independence was achieved:

```text
53 passed in 0.27s
```

A further source review found two potential false-PASS routes in Python's permissive truth/equality semantics. Without type validation a nonempty string could satisfy a boolean release witness, while integer zero can compare equal to `False`. Exact-boolean input validation and three adversarial regression tests were added. The first run revealed a source-edit syntax error at test collection, which was corrected and retested before acceptance. The final completed run:

```text
.venv/Scripts/python.exe -B -m pytest -q -p no:cacheprovider
  --basetemp=.venv/.s1_role_boundary_20261020d
  tests/unit/test_r0_p03_s1_role_boundary_synthetic.py
  tests/unit/test_r0_p03_s1_transport_custody_synthetic.py
  tests/unit/test_r0_p03_synthetic_custody_evidence_candidate.py

56 passed in 0.27s
```

All runs occurred through the registered, purpose-bounded Codexless Runtime Bridge's authorized `codex.command_exec` path. New tests and code were authored in the public ADS workspace without touching historical experiment files. The temporary pytest artifacts are outside the committed source set.

## 3. Actual verified behavior versus unqualified security property

| Tested scenario | Observed source-free outcome | Not proven |
| --- | --- | --- |
| Fixed mock role/action policy | Five synthetic roles have distinct operation sets and role requests cannot override the in-memory assignment | Real authenticated API policy, privilege isolation or secret access |
| Unknown session or attempted reassignment | Rejected by the fake registry | Attested person-level identity, unforgeable session identifiers |
| Known reviewer opens another same-principal session | Retained mock role/exposure history prevents role switch | Cross-app/model-context identity or memory continuity |
| **Unlinked alias for same actor** | **Permitted by mock registry**; explicit negative-control reveals the gap | **Real identity collision prevention; not qualified** |
| Public coordinator and blind author | Mock direct reviewer-ledger access denied | OS ACL, service authorization, filesystem/connector reachability or telemetry isolation |
| Incomplete candidate/release evidence | Returns `RELEASE_HOLD_UNQUALIFIED_WITNESS` | Independent review, actual custody readback, author-render capture |
| All fictional release witnesses | Returns `SIMULATED_READY_ONLY_NO_RELEASE_CAPABILITY` | Real release authorization or owner approval |
| Variable public receipt, including singleton count or source-path mapping | Held; only a constant nonanswer-bearing fake marker accepted in this exact mock model | Security of a useful dynamic aggregate or real cumulative publication history |
| Malformed witness and receipt types | Nonboolean truthy release claims and numeric substitutes for `False` rejected | Validity of the caller's real evidence |
| Earlier journal/transport checks | Existing S1 exact fake delivery, simulated event integrity, dependency invalidation and fake custody tests still pass | Confidentiality, OS ACL isolation, independent external journal anchoring |

This validation does **not** claim that the permitted fictional role decisions could be trusted if an attacker controlled the process, registration table, caller's session identifier, mock observations or test harness itself.

## 4. Architecture qualification decision

**Positive:** the policy can clearly distinguish source proposal, independent challenge, simulated authorization, public-safe summaries and blind author read scope; fail-closed typing prevents simple Python coercion-based false readiness. The negative test demonstrates exactly why an externally verified principal/session/role mapping is an **essential independent requirement**, not an optional refinement.

**Unqualified:** real reviewer/challenger identity, actual separate trust principals, access to protected source material, confidential event storage, independent journal anchor custody, restart recovery under a real identity, secure author viewer, cross-provider memory exclusion and safe cumulative public reporting.

The next owner-approved actual-boundary exercise should test a real trust substrate using only fictional content, ideally comparing (i) owner-controlled Windows principal/ACL isolation; (ii) narrow authenticated review service; and (iii) hybrid content transport, independent anchor store and separate author-view gateway. Their security, complexity and operational feasibility must be measured rather than presumed. Do not register any new principals, modify ACLs, create credentials, connect a new provider or deliver protected records without an explicit qualified design and owner authorization.

Read-only architecture exploration and source-free simulation remain permitted, but pass/fail reports must distinguish security control **absence**, **lack of testing**, **platform refusal** and **observed operating-system or service enforcement**.

## 5. Scientific state

V0.4 remains a prospective, exposed-coordinator method contract awaiting a bounded independent challenge. Validation 266 does not supersede Research 513/559/576, restructure the protected source population, reinterpret old Research 217 gold, select a target physical architecture or move Checkpoint 898. No R0-P03 scored arm has run.

```text
VALIDATION_266=SYNTHETIC_ROLE_POLICY_MECHANICS_PASS
COMBINED_FOCUSED_TESTS=56_PASS
IDENTITY_ALIAS_NEGATIVE_CONTROL=DEMONSTRATES_UNQUALIFIED_BOUNDARY
STRICT_BOOLEAN_WITNESS_AND_RECEIPT_CHECKS=PASS
REAL_REVIEWER_IDENTITY_AUTHENTICATION=NOT_TESTED
REAL_REVIEWER_CUSTODY=NOT_SELECTED
REAL_CONFIDENTIALITY_OR_ACL_DENIAL=NOT_TESTED
SOURCE_ADMISSION=NONE
GOLD=NONE
SCORING_B0_B4=NOT_STARTED
CHECKPOINT=898_UNCHANGED
SPECIFICATION_028=UNCHANGED
```
