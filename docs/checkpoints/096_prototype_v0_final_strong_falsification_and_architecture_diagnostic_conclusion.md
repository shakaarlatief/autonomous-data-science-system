# Checkpoint 96: Prototype V0 final strong-falsification and architecture-diagnostic conclusion

**Date:** 2026-08-19  
**Status:** Final V0 experimental checkpoint  
**Checkpoint class:** DESIGN  
**Project stage:** Prototype V0 final evaluation and closure  
**Scope:** Records the historical milestone described by this checkpoint: Prototype V0 final strong-falsification and architecture-diagnostic conclusion.  
**Authority:** Historical provenance; current canonical documents and promoted sources govern current interpretation.  
**Design session:** 01  
**ChatGPT project:** Autonomous Data Science System  
**Session title:** 01 - Foundations & Checkpoint 0

## Boundary reached

Prototype V0 is complete.

The sequence is now fully closed:

```text
30/30 treatment slots resolved
-> 34/34 persisted attempts mechanically verified PASS
-> 30 retained behavior-evaluable trajectories fixed
-> 60/60 blinded semantic judge passes completed
-> no manual adjudication required
-> blinded consensus frozen
-> frozen archive independently verified
-> condition mapping decoded deterministically
-> decoded semantic/mechanical results independently reviewed
-> retained P0 internal diagnostics exported and reviewed
-> preregistered continuation and strong-falsification rules applied
```

No further B0, B1, P0, or V0 semantic-judge inference is authorized.

## Uploaded architecture-diagnostic evidence

The final diagnostic archive was:

```text
p0_architecture_diagnostics_20260819T133210Z.zip
```

It contains:

```text
1 manifest
10 retained P0 trajectories
10 diagnostic files per trajectory
101 ZIP entries total
```

The manifest covers all 100 trajectory files with SHA-256 and byte size. Independent inspection found:

```text
missing covered files: 0
SHA-256 mismatches: 0
```

The export contains only retained P0 trajectories and no B0/B1 trajectory or semantic private decoder.

## Final common comparison

Pooled targeted architecture score:

```text
B0: 1.47
B1: 1.73
P0: 1.78
```

P0 versus B1:

```text
targeted mean difference: +0.05
strong targeted passes: 0 vs 0
critical failure runs: 0 vs 0
```

The registered material reliability alternative requires either at least two fewer critical failures or a targeted gain of at least `0.30` together with at least two additional strong-targeted passes. P0 satisfies neither.

Cross-variant targeted differences remain small and consistent:

```text
H1: +0.06
H2: +0.04
```

Paired P0 minus B1 targeted differences:

```text
H1: +0.10, 0.00, 0.00, 0.00, +0.20
H2:  0.00, +0.20, 0.00, 0.00, 0.00
```

Seven of ten paired blocks are exact ties.

## Resource and completion result

```text
B1 completed within budget: 10 / 10
P0 completed within budget:  3 / 10

B1 budget exhausted: 0 / 10
P0 budget exhausted: 7 / 10

B1 median tokens: 120,564.5
P0 median tokens: 260,370.0
P0/B1 token ratio: 2.160

B1 median calls: 16
P0 median calls: 13

B1 median Python: 6
P0 median Python: 5
```

The P0 problem is not a larger action count. It is repeated context cost.

Across P0 calls, median input tokens rose approximately from 2,793 on call 1 to 36,029 on call 12 and 40,975 on call 14. The current-state view itself grew to roughly 9,000-10,000 characters late in a run while prior provider context remained available.

## Architecture-specific diagnostic result

Across ten retained P0 runs:

```text
state objects: 506
relations: 483
invalidated transitions: 14
reopened transitions: 24
repair-priority objects: 32
support-reassessment objects: 30
knowledge reopens: 2
state-control errors: 0
blocked ACTION objects: 0
Python-budget blocks: 0
```

### False blocking

No architecture-induced action block occurred.

Every trace event marked `allowed=false` was one of the seven registered resource-budget exhaustion markers. There was no `P0_STATE_CONTROL_ERROR` and no blocked P0 ACTION object.

Result:

```text
critical false blocks: 0 / 10
noncritical false blocks: 0 / 10
```

### Invalidation and repair precision

The 14 invalidations were inspected individually. Every invalidated evidence/claim/assumption materially depended on the now-ineligible post-outcome feature or on model evidence produced using that feature.

No unrelated evidence was destroyed.

This agrees with blinded P0 repair precision:

```text
S6 repair completeness: 2.00
S7 repair precision:    2.00
```

No critical over-invalidation occurred.

### Reopening

Most reopens were correctly scoped to model-selection decisions, feature-eligibility questions, and dependent repair questions.

One H2 R4 internal generalization-regime question was reopened after a model-specific claim carrying a `validation_regime` tag was invalidated. The next accepted state patch immediately resolved the question by stating that the feature revision did not change the established temporal/entity validation regime.

This is a useful latent over-propagation example. It did not create a false block, destroy unrelated evidence, or trigger extra external analysis.

A few OPEN questions were also changed to REOPENED after a hard dependency break. Those are redundant status churn, not broad project invalidation.

Conservative result:

```text
behaviorally consequential broad reopening: 0 / 10
latent noncritical over-broad internal reopen artifact: at most 1 / 10
```

The registered friction threshold is not exceeded.

### Support-reassessment churn

Thirty support-reassessment obligations were created. Several targeted the top-level deliverable obligation and were immediately closed by controller support semantics as redundant.

This is not a registered false block, but it is avoidable internal state churn and should not survive unchanged.

### Knowledge-activation brittleness

Activation coverage:

```text
K-INFO-001: 10 / 10
K-INFO-002: 10 / 10
K-VAL-001:  10 / 10
K-INFO-003:  8 / 10
```

K-INFO-003 did not activate in two runs because the treatment learned the relevant table information through Python instead of the table-metadata path expected by the trigger.

The LLM still handled feature timing correctly. This shows that the current activation predicates can depend on tool path rather than semantic equivalence.

### Hard coding

No held-out-specific hard coding was found.

The P0 implementation is generic. Static inspection found no held-out trap names `lifecycle_flag` or `profile_code` in the P0 semantic implementation. It also does not encode the development trap name `account_state_code` or the held-out identifier `member_key`.

## Strong-falsification decision

Foundation 012 states that strong evidence against the current P0 design exists if any registered strong-falsification condition holds.

The architecture-specific failure clauses are not triggered:

```text
more P0 critical failures than B1: no
critical false block / over-invalidation: no
false blocking or unnecessary broad reopening in >=2/10: no
held-out-specific hard coding: no
```

The reliability-cost clause **is triggered**.

The registered reliability evidence shows:

```text
critical failure runs: B1 0, P0 0
strong targeted passes: B1 0, P0 0
P0 targeted mean advantage: +0.05
registered material targeted advantage: +0.30 plus strong-pass gain
```

Therefore B1 matches P0 at the preregistered material reliability level. P0 does not demonstrate a material reliability improvement.

The resource trigger is far exceeded:

```text
P0/B1 median tokens = 2.160
required for strong-falsification resource trigger: >=1.25
```

Completion is also materially worse:

```text
B1: 10/10 within budget
P0: 3/10 within budget
```

Final classification:

> **STRONG FALSIFICATION OF THE CURRENT P0 DESIGN.**

## Interpretation boundary

This does not falsify the broad Autonomous Data Science System vision.

It does not establish that explicit memory, dependencies, knowledge activation, or precise deterministic controls are never useful.

It establishes that the current always-on P0 combination does not earn its complexity on this benchmark when compared with a strong B1 workflow that receives the same methodological concepts statically.

## Mechanism-level lessons

```text
H1 typed state:
    rich audit state exists, but no material external reliability advantage

H2 knowledge activation:
    static B1 knowledge captured most benefit; current triggers are path-sensitive

H3 prospective safeguard:
    zero false blocks, but no invalid test proposal occurred, so positive benefit remains undiscriminated

H4 dependency repair:
    technically precise, but B1 repaired almost as well without the machinery

H5 frontier/action selection:
    fewer model calls and Python actions, but severe repeated-context cost dominates
```

## Promotion audit

This checkpoint contains material that must not remain checkpoint-only.

Promoted immediately:

```text
docs/experiments/prototype_v0/FINAL_RESULTS.md
    final authoritative V0 results and interpretation

docs/CURRENT_STATE.md
    V0 closed; strong falsification; post-V0 next stage
```

Additional stage-boundary reconciliation is still required for stale references in the knowledge map, open-question register, Prototype V0 README, major-changes ledger, and accepted project decisions.

No new production architecture is accepted in this checkpoint.

## Next step

Perform the post-V0 knowledge reconciliation, then design the smallest evidence-driven successor architecture.

The next experiment should target a failure mode where B1 is expected to struggle rather than tuning P0 against the already completed churn benchmark.
