# MC-0014 Brief: Adversarial Interpretation of H1/H2 Probe Evidence

**Thread:** MC-0014
**Date opened:** 2026-09-13
**Review mode:** ADVERSARIAL_REVIEW
**Coordination branch:** `v1-source-vault-bootstrap-resume`
**Exact review target:** `85ade407b2f1957f5a3980aca92c09500db430b8`
**Claude interaction:** `claude-03`
**Claude conversation title:** `03 - Project Knowledge Architecture Foundations and Design Method`
**Authority:** Collaboration evidence only. Requirements V0.2 remain the frozen candidate-acceptance authority. This thread cannot select a target architecture, amend requirements or authorize migration.
**Purpose:** Adversarially interpret the now-complete V0.1 and V0.2 H1/H2 mechanism probes before Research 124 narrows toward a target architecture. Search for construct-validity defects, candidate-boundary leakage, self-fulfilling assumptions, stronger untested candidate forms and unjustified extrapolation rather than rewarding agreement.

## 1. Why this review is now timely

Research 134 explicitly deferred another Claude turn until mechanism-probe evidence existed. Two probe rounds now exist:

```text
Common Fixture V0.1
    H1 and H2 both semantically pass
    generic cross-objectness does not establish separate authority
    broad H2 physical boundedness supported, semantic boundedness unresolved

Relation-Lifecycle Discriminator V0.2
    H1 and narrowed H2 both semantically pass
    strongest allowed H1 uses a source-owned sidecar
    H1 relation placement is deliberately deterministic but semantically arbitrary
    narrowed H2 gives qualifying relations first-class ownership
    H2 rejects ordinary directional relations under its admission rule
```

The project now needs a skeptical second-model interpretation more than another internally generated synthetic probe.

This is **not** an independence-sensitive design round. You are intentionally allowed to see ChatGPT's interpretations and should attack them directly.

## 2. Exact-target discipline

Use the coordination branch only to find this MC-0014 obligation. For substantive review, bind your analysis to exact commit:

```text
85ade407b2f1957f5a3980aca92c09500db430b8
```

At minimum inspect the exact-target versions of:

```text
docs/research/PROJECT_KNOWLEDGE_ARCHITECTURE_REQUIREMENTS_V02.md
docs/research/134_comparative_architecture_reconciliation_and_common_fixture_probe_protocol.md
docs/research/135_common_fixture_v01_machine_freeze_before_hypothesis_implementation.md
docs/research/136_common_fixture_v01_h1_h2_empirical_mechanism_probe.md
docs/research/project_knowledge_architecture_probe_v01/COMMON_FIXTURE_V01.json
docs/research/project_knowledge_architecture_probe_v01/RESULTS_V01.json
scripts/research/project_knowledge_architecture_probe_v01.py

docs/research/137_relation_lifecycle_discriminator_v02_machine_freeze.md
docs/research/138_relation_lifecycle_discriminator_v02_h1_h2_empirical_result.md
docs/research/project_knowledge_architecture_probe_v02/RELATION_LIFECYCLE_FIXTURE_V02.json
docs/research/project_knowledge_architecture_probe_v02/RESULTS_V02.json
scripts/research/project_knowledge_architecture_probe_v02.py
tests/unit/test_project_knowledge_architecture_probe_v02.py
```

Read Research 124 and earlier evidence only as needed to test interpretation. Do not restart broad web research.

## 3. Review stance

Act as an adversarial architecture/evidence reviewer, not as a second author.

Agreement is not a success criterion. Disagreement is not a success criterion either. The goal is to identify the strongest real defects or confirm which claims survive attack.

Distinguish carefully among:

```text
FACT / IMPLEMENTATION DEFECT
MEASUREMENT DEFECT
CONSTRUCT-VALIDITY DEFECT
INTERPRETATION OVERREACH
ARCHITECTURE BOUNDARY PROBLEM
EVIDENCE INSUFFICIENCY
REAL SUPPORT
```

## 4. Questions that must be attacked directly

### A. Does V0.1 really strengthen H1?

Test the claim that directional source ownership plus deterministic closure handles the V0.1 hard cases without hidden duplicate truth or an undeclared relation registry. Look for places where H1 merely pushes complexity into generated closure or source-local metadata.

### B. Is strongest-H1 V0.2 still honestly H1?

The final H1 uses `sidecar:S-A:relations` because Research 137 allows tightly source-owned sidecars. The relation inside that sidecar has stable ID, revision, lifecycle, provenance and timeline independent of `S-A`'s intrinsic semantics.

Ask:

```text
is that genuinely source-local relation metadata?
or is it already a first-class relation object physically namespaced under S-A?
if the latter, has V0.2 collapsed H1/H2 into a placement/namespace distinction?
what exact semantic boundary would distinguish them?
```

Do not accept ChatGPT's labels as proof of family identity.

### C. Is the V0.2 discriminator circular or self-fulfilling?

The fixture explicitly declares that `R-ABC-1/2` have:

```text
stable relation identity
independent lifecycle
relation-specific provenance
no natural endpoint owner
```

and H2's admission rule uses those same properties.

Assess whether:

```text
the fixture genuinely tests an architecture consequence
or merely encodes the conclusion that the relation should be first-class
```

If partly self-fulfilling, identify what additional evidence would make the mechanism claim non-circular.

### D. Does H2 actually need a “spine”?

Separate:

```text
first-class relation identity / authority
from
centralized relation/control substrate
```

Could qualifying relation objects be repository-native, distributed, typed artifacts or another non-central form while preserving the semantic benefit? If yes, say whether “minimal spine” is now the wrong architectural abstraction.

### E. Are the maintenance measurements fair?

V0.2's final strongest-H1 result shows:

```text
H1 independent-relation authority sites  1
H2 independent-relation authority sites  2
H1 authoritative location touches         4
H2 authoritative location touches         5
H1 arbitrary owners                       2
H2 arbitrary owners                       0
```

Challenge whether those metrics are meaningful, representation-dependent, incomplete or differently weighted. Identify missing cost dimensions before any target decision.

### F. Does the H2 10/50/100 scale result prove selectivity?

The scaled ordinary relations are synthetically labeled so the admission rule clearly rejects them. Assess how much evidence this really provides. What real-corpus or ambiguous-case test is needed to estimate false-positive/false-negative admission behavior rather than merely confirm that the implementation follows the frozen rule?

### G. Should H3 or another family reopen?

Research 136 deferred H3 because H1/H2 stayed lightweight. V0.2 now introduces first-class relation objects. Determine whether that materially strengthens an object-primary alternative, a typed-object/document hybrid, or another architecture family enough to reopen it.

### H. What does the evidence actually justify now?

Attack Research 138's strongest integrated hypothesis:

> Source-local by default, with separately authoritative first-class semantic/control objects only when the thing itself earns independent identity/lifecycle/provenance and cannot be naturally owned by one source; broader navigation, closure, search and context views remain derived/rebuildable.

Classify each part as:

```text
SUPPORTED
PLAUSIBLE_BUT_UNPROVEN
TOO_STRONG
WRONG / CONTRADICTED
```

## 5. Required conclusion

End with a concrete disposition containing:

1. **Strongest defect found**, if any.
2. **Strongest result that survives adversarial review.**
3. Whether H1 and H2 remain meaningfully distinct after the strong H1 sidecar form.
4. Whether the project should keep the term `bounded spine`, replace it with a more precise mechanism abstraction, or reopen a different family.
5. The **minimum next empirical step** required before target narrowing. Prefer a real-repository or behavioral discriminator if synthetic fixtures have reached diminishing returns.
6. Whether another Claude round is needed after ChatGPT disposition, or whether this one review should close MC-0014.

Do not select the target architecture.

## 6. Required output

Write exactly one response at:

```text
docs/model_collaboration/threads/MC-0014/messages/001_claude_adversarial_probe_interpretation.md
```

Include normal collaboration provenance and the exact reviewed commit.

## 7. Write scope

Claude may write only:

```text
docs/model_collaboration/threads/MC-0014/messages/**
```

Do not modify Research 124, Requirements V0.2, routing, checkpoints, fixtures, probe implementation, raw results or canonical governance.

```text
MC0014=OPEN
MODE=ADVERSARIAL_REVIEW
EXACT_REVIEW_TARGET=85ade407b2f1957f5a3980aca92c09500db430b8
MESSAGE_001=CLAUDE_NEXT
REQUIREMENTS_V02=FROZEN_UNCHANGED
TARGET_ARCHITECTURE=NOT_SELECTED
```
