# Checkpoint 168: RECOMMENDED vs BLOCKING_REQUIRED Provider-Free Implementation Gate Passed

**Date:** 2026-08-24  
**Design session:** 04  
**ChatGPT project:** Autonomous Data Science System  
**Session title:** 04 - Selective Context Promotion & Reasoning Vertical Slice  
**Branch:** `v1-blocking-calibration-diagnostic`  
**PR:** #44 draft  
**Classification:** provider-free implementation gate passed  
**Scientific authority:** Specification 020 v0.1 remains frozen by Checkpoint 167

## Why this checkpoint exists

Checkpoint 167 froze Specification 020 before implementation. This checkpoint records the first exact provider-free implementation boundary that satisfies the frozen construct, execution, blinding, and cross-platform requirements.

This is an audit/promotion boundary for implementation only. It does not modify the frozen benchmark, semantics, thresholds, model treatment, call budget, randomization seed, or allowed scientific outcomes.

---

## Starting integration boundary

Specification 020 branch creation began exactly from the reconciled V1 integration head:

```text
b9c9c3a38935983075a9ca88632177980bb20ede
```

The frozen scientific sources remain:

```text
docs/research/027_recommended_vs_blocking_required_calibration_design.md
docs/specifications/020_v1_recommended_vs_blocking_required_calibration_diagnostic.md
tests/fixtures/reasoning/blocking_calibration_v1.json
docs/checkpoints/167_recommended_vs_blocking_required_calibration_contract_frozen.md
```

---

## Corrected provider-free implementation boundary

The exact corrected implementation head validated by the first complete cross-platform gate was:

```text
fb8327aae859f53bbb0c4d7bba70b32b6033343e
```

The implementation includes:

```text
experiments/blocking_calibration/__init__.py
experiments/blocking_calibration/harness.py
experiments/blocking_calibration/runner.py
tests/unit/test_blocking_calibration_harness.py
tests/unit/test_blocking_calibration_runner.py
tests/integration/test_blocking_calibration_vertical_slice.py
.github/workflows/v1-blocking-calibration.yml
```

The provider-free runner requires an injected `ReasoningRuntime`. It has no live runtime default and no command-line path that instantiates a provider runtime.

---

## Implemented frozen behavior

The provider-free implementation preserves the exact Specification 020 construct:

```text
BLOCKING_REQUIRED
    exact unresolved supplied requirement
    + exact active defended supplied downstream scope
    + explicit scope DEPENDS_ON requirement relation
    + candidate action resolves that requirement
    + exact requirement and scope pointers

RECOMMENDED
    materially worthwhile action
    + no exact active supplied downstream scope blocked on it
    + both pointers null
```

Implemented boundaries include:

```text
experiment-only BlockingCalibrationResult
strict disposition enum validation
strict supplied requirement-ID validation
strict supplied downstream-scope-ID validation
RECOMMENDED requires both blocking pointers null
truth-blinded model-visible requests
no reusable methodological context
no tools
no cross-call state
no project mutation
deterministic globally randomized 36-call plan
canonical plan serialization and SHA-256
complete attempt ledger
frozen retry categories only
deterministic gate recomputation from hidden fixture truth
fake-runtime end-to-end execution
```

---

## Attempt-ceiling repair before gate acceptance

During provider-free implementation, an edge case was found in the global provider-attempt budget path: exhausting the frozen 45-attempt ceiling could escape as an implementation exception before a normalized incomplete experiment result was preserved.

This was repaired before accepting the implementation boundary.

The corrected behavior is:

```text
45-attempt ceiling reached
    -> preserve every attempt already made
    -> stop further planned execution
    -> evaluate with execution_complete = false
    -> emit INCOMPLETE
    -> preserve result.json and RESULT.md
```

A provider-free regression test exhausts the complete 45-attempt ceiling and verifies the normalized `INCOMPLETE` outcome.

This repair changes execution robustness only. It does not change any frozen scientific truth or success threshold.

---

## Exact cross-platform evidence

Dedicated Specification 020 provider-free workflow:

```text
run 32697487230
```

Ubuntu:

```text
frozen dedicated tests       16 passed
full V1 Python regression    115 passed, 2 skipped
OPENAI_API_KEY               absent
```

Windows:

```text
frozen dedicated tests       16 passed
full V1 Python regression    115 passed, 2 skipped
OPENAI_API_KEY               absent
```

The two skipped tests are the existing PostgreSQL-environment tests when `ADS_TEST_POSTGRES_URL` is not configured. They are not Specification 020 failures.

Same-head surrounding regression evidence:

```text
V1 reasoning context value                 run 32697487202   success
V1 disposition semantics diagnostic        run 32697487256   success
V1 autonomous live experiment launcher CI  run 32697487239   success
Checkpoint metadata                        run 32697487221   success
```

No provider credential was supplied to ordinary CI.

---

## Provider boundary

At this checkpoint the branch contains no authorized Specification 020 provider path.

Explicitly absent:

```text
no live runtime default
no live CLI
no Specification 020 live workflow
no Specification 020 launch authorization
no provider-backed result
```

Therefore:

```text
provider calls authorized by Checkpoint 168 = 0
```

---

## Promotion audit

### Supported for continued implementation

The following implementation mechanisms are accepted as adequate for constructing a later live-capable boundary:

```text
frozen six-pair fixture loader and structural audit
truth-blinded provider-neutral request construction
experiment-only structured output
strict supplied-ID pointer validation
deterministic randomized plan and hash
attempt ledger and bounded retry accounting
normalized INCOMPLETE handling at attempt exhaustion
deterministic frozen gate evaluation
provider-free fake-runtime integration
cross-platform ordinary CI with provider credential absent
```

### Not promoted as scientific result

Checkpoint 168 does not establish:

```text
BLOCKING_BOUNDARY_SUPPORTED
production BLOCKING_REQUIRED semantics
production recommendation taxonomy
recommendation/action value of selective methodology
automatic project mutation or execution
final provider/model policy
```

No live reasoner observation exists yet for Specification 020.

---

## Later reconciliation evidence

After the provider-free implementation gate, Research 028 was added as a research-only architectural synthesis and canonical routing was reconciled. That later documentation work does not modify Specification 020's frozen scientific contract.

The exact fully reconciled branch head must be validated separately before a pre-live checkpoint is frozen.

---

## Exact continuation

```text
1. reconcile CURRENT_STATE / README / KNOWLEDGE_MAP / OPEN_QUESTIONS to the provider-free-green boundary
2. validate the exact reconciled branch head with the Specification 020 and inherited provider-free gates
3. freeze that exact pre-live boundary in a new checkpoint
4. only after that checkpoint, implement a separate live-capable runner/workflow without changing scientific content
5. provider-free validate the exact live-capable head
6. freeze an exact live-source checkpoint before any launch authorization
7. authorize at most one frozen live run through Specification 018
8. preserve raw live evidence before interpretation or tuning
```
