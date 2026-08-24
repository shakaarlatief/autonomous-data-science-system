# V1 Dependency-Backed Recommendation and Action Value Result

**Specification:** 021 v0.1  
**Date:** 2026-08-24  
**Frozen advancement outcome:** `FAIL`  
**Experiment source:** `575a3264ea39a10e35d769f9c54a2d1a13c28c08`  
**Source ref:** `v1-spec021-dependency-backed-recommendation-value-replacement-live-source`  
**Launch issue:** #60  
**Launcher run:** `32742406506`  
**Live workflow run:** `32742426787`  
**Live workflow job:** `97479810225`  
**Artifact ID:** `9525947445`  
**Artifact SHA-256:** `05724335763fdbeb7eecb456f9662a95dd8d25579d82d360d29d306755648fa8`  
**Raw preservation commit:** `5930a3c52f9580febb56f8e80d3d6eaf8d2cac66`

## Result in one sentence

Specification 021 completed the full repaired dependency-backed recommendation/action design with perfect deterministic disposition and pointer behavior in GENERIC, SELECTIVE, and FULL_HORIZON, but **failed the preregistered advancement contract** because SELECTIVE scored `0.800000` on DBRA-01's blinded semantic rubric, below the frozen per-case floor of `0.850000`; no positive SELECTIVE value signal passed.

The recommendation/action seam is therefore **not promoted**.

---

## Frozen execution integrity

The replacement run completed exactly within the frozen plan:

```text
reasoner outputs          36 / 36
judge outputs             36 / 36
scored observations       36 / 36
reasoner failed attempts   0
judge failed attempts      0
provider attempts         72 / 90
retries                    0
complete scored design     true
execution integrity        true
authoritative isolation    true
```

The live wrapper reported governed Specification 021 execution, and the exact source head was:

```text
575a3264ea39a10e35d769f9c54a2d1a13c28c08
```

All frozen technical invariants `DBRA-INV-01` through `DBRA-INV-24` evaluated true. The project state before and after the experiment remained empty and unchanged.

This also closes the mappingproxy-backed attempt-metadata defect preserved by the first incomplete run: real live-shaped provider usage was recorded successfully across the full 72-call replacement execution.

The first governed run `32727241852` remains immutable `INCOMPLETE` evidence and is not rescored or replaced historically.

---

## Aggregate frozen metrics

```text
                         GENERIC        SELECTIVE       FULL_HORIZON
exact disposition        1.000000       1.000000        1.000000
semantic score           0.958333       0.950000        0.950000
critical omissions       0              0               0
under-recommendations    0              0               0
over-recommendations     0              0               0
blocking false positives 0              0               0
blocking pointer errors  0              0               0
defer pointer errors     0              0               0
unnecessary cost         0              0               0
```

The explicit dependency-backed recommendation semantics therefore removed the over-blocking and pointer failures that dominated Specification 019 on the bounded cases. That is positive construct/instrumentation evidence, but the frozen Specification 021 advancement contract evaluates the complete recommendation seam, not disposition labels alone.

---

## Per-case frozen quality

Exact disposition accuracy:

```text
                         GENERIC        SELECTIVE       FULL_HORIZON
DBRA-01                  1.000000       1.000000        1.000000
DBRA-02                  1.000000       1.000000        1.000000
DBRA-03                  1.000000       1.000000        1.000000
DBRA-04                  1.000000       1.000000        1.000000
```

Blinded semantic score:

```text
                         GENERIC        SELECTIVE       FULL_HORIZON
DBRA-01                  0.833333       0.800000        0.800000
DBRA-02                  1.000000       1.000000        1.000000
DBRA-03                  1.000000       1.000000        1.000000
DBRA-04                  1.000000       1.000000        1.000000
```

The only weak case was DBRA-01, and the weakness was shared across all three conditions rather than being unique to SELECTIVE.

---

## Frozen gate result

The mechanically evaluated gate result was:

```text
absolute gates           FAIL
relative gates           PASS
expansion gates          PASS
positive value signals   0
advancement outcome      FAIL
```

Exactly one named gate failed:

```text
DBRA-G08  SELECTIVE every-case semantic score >= 0.85
```

Observed DBRA-01 SELECTIVE score:

```text
0.800000
```

Frozen floor:

```text
0.850000
```

All other frozen gates `DBRA-G01` through `DBRA-G23` passed.

Because Specification 021 explicitly defines any failed absolute, relative, or expansion gate in a complete integrity-valid design as `FAIL`, no post-hoc exemption is permitted for a treatment-invariant weakness.

---

## Failure anatomy: DBRA-01 semantic depth

DBRA-01 prospectively requires five semantic obligations. In addition to correct action disposition and relation pointers, the rubric requires the response to explain that:

```text
1. the exact prediction moment is unresolved and required before future-facing model selection can be defended;
2. post-outcome feature timing is a current validity concern and the feature audit is anchored to the represented requirement/scope relation;
3. a random-across-time split is inadequate for the stated future deployment and future-representative temporal validation blocks the defended model-selection scope;
4. both approved nonlinear comparisons wait exactly for prediction-validity-established;
5. the unrelated histogram action should not be elevated into current work.
```

The SELECTIVE reasoner outputs classified every action and pointer correctly in all three repetitions. Their rationales, however, were mostly relation-level statements such as an action resolving an unresolved requirement on which the defended scope depends. They did not consistently make the richer methodological explanation explicit, especially the significance of post-outcome feature timing and why random-across-time evaluation is not sufficient for future deployment.

That content pattern is consistent with the lower blinded semantic score. The preserved aggregate result does not retain per-obligation judge scores, so no stronger per-obligation attribution is claimed here.

The key treatment comparison is nevertheless clear from the frozen metrics:

```text
GENERIC DBRA-01 semantic       0.833333
SELECTIVE DBRA-01 semantic     0.800000
FULL_HORIZON DBRA-01 semantic  0.800000
```

SELECTIVE remained within the frozen relative non-inferiority margin and was identical to FULL_HORIZON on this case. The failed absolute floor is therefore not evidence that selective context uniquely caused the semantic weakness.

---

## No positive recommendation-value signal

No prospectively frozen positive value signal passed.

SELECTIVE did not exceed GENERIC by the required margin on aggregate exact accuracy or semantic quality, and no error-count or expansion signal could favor SELECTIVE because all three conditions already had zero deterministic recommendation errors and zero unnecessary expansion cost.

This means Specification 021 provides no evidence that the accepted SELECTIVE methodological context improves downstream recommendation/action quality beyond the strong GENERIC reasoner on this bounded ten-asset universe.

This statement is distinct from claiming that selective context is harmful. The result supports neither a positive recommendation-value claim nor a general negative claim about selective context.

---

## What Specification 021 establishes

The complete replacement run provides strong bounded evidence that the cleaned structural recommendation semantics are operationally usable in the full matched experiment:

```text
system-owned exact methodology provenance
explicit unresolved requirements
explicit active defended downstream scopes
scope DEPENDS_ON requirement relations
action RESOLVES requirement relations
explicit unresolved defer triggers
action WAITS_FOR trigger relations
model-owned dispositions and supplied-ID pointers
```

Across 36 reasoner outputs, every candidate action received the exact frozen disposition and every blocking/defer pointer was correct, with zero blocking false positives and zero expansion errors.

The run also establishes that the repaired JSON-safe `ReasoningUsage` attempt-recording path works under live provider usage for both reasoner and judge calls.

These are bounded construct and instrumentation results. They do not override the frozen scientific `FAIL` or promote the complete recommendation seam.

---

## What Specification 021 does not establish

The result does **not** justify:

```text
promotion of the dependency-backed recommendation/action seam
claim that SELECTIVE context improves recommendation quality
claim that SELECTIVE context is generally harmful
production recommendation/disposition enums
production REQUIRED/BLOCKING policy
production ranking or prioritization policy
open-world action generation
automatic project mutation or execution
final provider/model selection
multi-agent recommendation architecture
```

The observed result is bounded to the exact prospective benchmark, ten-asset knowledge universe, model/runtime configuration, and frozen gates.

---

## Architectural consequence

The known provenance, DEFER, BLOCKING_REQUIRED, and live usage-serialization confounds have now been separated from the recommendation-value question. The cleaned experiment still does not demonstrate a SELECTIVE advantage over a strong generic reasoner.

The next step should therefore **not** repeat or tune the same benchmark merely to seek a positive result.

A future design should instead ask whether the limiting factor is one of:

```text
knowledge novelty / coverage beyond what the strong generic model already knows
how much semantic explanatory content the compact methodology projection actually contributes
whether recommendation value appears only in harder heterogeneous project states
how explicit knowledge should influence reasoning without becoming redundant context
```

Those are future research questions. Specification 021 itself licenses no new provider-backed rerun.

---

## Durable evidence

Raw replacement bundle:

```text
experiments/dependency_backed_recommendation_action_value/results/
    spec021-live-20260824-run-32742426787/
```

The raw artifact was committed at `5930a3c52f9580febb56f8e80d3d6eaf8d2cac66` **before result interpretation**.

Contained-file hashes and complete launch/run/artifact provenance are recorded in:

```text
experiments/dependency_backed_recommendation_action_value/results/
    spec021-live-20260824-run-32742426787/ARTIFACT_MANIFEST.md
```

Historical incomplete evidence remains separately preserved at:

```text
experiments/dependency_backed_recommendation_action_value/results/
    spec021-live-20260824-run-32727241852/
```
