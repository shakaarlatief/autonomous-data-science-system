# MC-0016 Brief: Adversarial Review of Whole-Architecture Candidate 01

**Thread:** MC-0016
**Date opened:** 2026-09-14
**Review mode:** ADVERSARIAL_REVIEW
**Coordination branch:** `v1-source-vault-bootstrap-resume`
**Exact review target:** `69aed186a0d63b3c395a133cd920099d5fa8e000`
**Claude interaction:** `claude-03`
**Claude conversation title:** `03 - Project Knowledge Architecture Foundations and Design Method`
**Authority:** Collaboration evidence only. Requirements V0.2 remain the frozen candidate-acceptance authority. This thread cannot select the target architecture, migrate current authority or amend requirements.
**Purpose:** Attack the first post-MC-0015 whole-architecture candidate and its 50 KA-R / 17 KA-I design mapping before any substantial shadow implementation begins. Search for hidden duplication, semantic contradictions, under-specified mechanisms, requirement coverage gaps, overfitting to the current repository and simpler or stronger competing forms.

## 1. Exact-target discipline

Use the coordination branch only to locate this obligation. Bind substantive review to exact commit:

```text
69aed186a0d63b3c395a133cd920099d5fa8e000
```

At minimum inspect the exact-target versions of:

```text
docs/research/PROJECT_KNOWLEDGE_ARCHITECTURE_REQUIREMENTS_V02.md
docs/research/143_real_corpus_construct_reconciliation_and_candidate_synthesis_readiness.md
docs/research/144_whole_architecture_candidate_repository_native_semantic_sources.md
docs/research/145_candidate_01_requirements_v02_design_coverage_and_qualification_plan.md
docs/research/project_knowledge_candidate_01/QUALIFICATION_MATRIX_V01.json
```

Read older Research 124 evidence only when needed to test a concrete claim. Do not restart broad web research.

## 2. Review stance

This is an adversarial architecture review, not a co-authoring exercise. The candidate's statement that all 50 requirements and 17 invariants are design-mapped is a claim to test, not a premise to accept.

Distinguish:

```text
ACTUAL DESIGN GAP
UNDER-SPECIFIED MECHANISM
INTERNAL CONTRADICTION
HIDDEN DUPLICATE TRUTH / DRIFT SURFACE
SCALING OR MAINTENANCE RISK
MIGRATION RISK
QUALIFICATION-ONLY UNCERTAINTY
IMPLEMENTATION CHOICE THAT CAN SAFELY REMAIN OPEN
REAL SUPPORT / SURVIVING STRENGTH
```

## 3. Questions that must be attacked directly

### A. Candidate architecture coherence

Does the candidate form a coherent whole, or is it an accumulation of mechanisms that individually sound reasonable but create hidden interactions or duplicated semantics?

### B. Rich source versus structured declaration drift

Candidate 01 keeps rich prose authoritative while also introducing structured declarations and action contracts adjacent to the same source. Test:

```text
what exactly is authoritative if prose and structure disagree?
how is duplicate statement of the same rule avoided?
can action-contract constraints be maintained without creating a second truth inside the source?
what is generated versus authored?
```

If the candidate needs a sharper one-home-per-fact rule inside a source, state it.

### C. Selective durable identity and tombstones

Attack rename/move/merge/split/redirect semantics. Does a selective identity-transition record remain bounded, or is it the start of a hand-maintained global registry? How are historical references resolved without requiring universal identity metadata?

### D. SINGLE_SOURCE default and JOINT_AUTHORITY exception

Is the distinction precise enough to satisfy KA-R13/R14 without circular human judgment? Does a joint-authority declaration merely recreate a mini-spine? Can base+supplement cases normally remain directional source-owned + derived closure, and when exactly must a separate authority-set source exist?

### E. Derived current state and current routing

Candidate 01 proposes eventually making `current_routing.json`, `CURRENT_STATE.md` and `KNOWLEDGE_MAP.md` derived. Challenge whether `CURRENT_STATE.md` currently contains unique synthesis that cannot be deterministically regenerated. Is the proposed rule “promote unique insight first, then derive the view” operationally realistic, or does it just move the hard consolidation problem elsewhere?

### F. Workstream object versus canonical source

Does the workstream profile correctly embody the MC-0015 conclusion that durable identity and single-source authority can coexist? Does putting state in one workstream source scale to nested/parallel workstreams, or does it recreate central control records elsewhere?

### G. Authority resolver and action-contract fidelity

This is the most safety-critical new mechanism. Attack:

```text
task/action classification
applicability/scope semantics
supersession closure
structured action contracts
free-form conformance checking
source-consumption evidence
fail-visible ambiguity
```

State whether Research 144 is concrete enough to prototype BL-001-style protection or whether a design gap remains before implementation.

### H. Capture/promotion and consolidation

Does the candidate make low-friction capture realistic without turning capture into a second knowledge swamp? Are promotion and consolidation semantics sufficient to preserve omitted limitations, uncertainty, rejected rationale and provenance?

### I. Scale and maintenance economics

Challenge the assumption that local declarations plus generated views necessarily yield dependency-local cost. Identify which dependencies still have to be discovered/maintained and whether global full rebuilds or semantic review can dominate at 5x/10x scale.

### J. Public/private and migration

Attack the abstract-private-dependency mechanism, non-leakage story, shadow migration, compatibility-view parity and rollback. Identify any missing mechanism that blocks safe migration.

### K. 50 + 17 design-coverage audit

Independently inspect the frozen Requirements V0.2 boundary. Report every KA-R or KA-I for which Candidate 01 is:

```text
NOT ACTUALLY DESIGN-COVERED
ONLY PARTIALLY DESIGN-COVERED
COVERED BUT HIGH-RISK / QUALIFICATION-DEPENDENT
```

Do not mechanically reproduce Research 145's mapping. If all are genuinely covered at design level, say so only after checking.

### L. Alternative-family reopening

Does Candidate 01 now contain enough identity/relation/schema machinery that H3/Object-Primary or another simpler family should be reopened before implementation? Or does the source-local/derived-view evidence still justify the hybrid?

## 4. Required conclusion

End with:

1. strongest design defect, if any;
2. strongest candidate property that survives attack;
3. corrected count/list of any design-coverage gaps or partial gaps;
4. whether Candidate 01 is coherent enough for a shadow prototype;
5. the **smallest falsification-first prototype slice** to build next, in priority order;
6. explicit conditions that would reopen H3 or another family;
7. whether another Claude round is needed before implementation.

Do not select the target architecture.

## 5. Required output

Write exactly one response at:

```text
docs/model_collaboration/threads/MC-0016/messages/001_claude_adversarial_candidate_01_review.md
```

Include normal collaboration provenance and the exact reviewed commit.

## 6. Write scope

Claude may write only:

```text
docs/model_collaboration/threads/MC-0016/messages/**
```

Do not modify Research 144/145, Requirements V0.2, routing, checkpoints, current state or candidate artifacts.

```text
MC0016=OPEN
MODE=ADVERSARIAL_REVIEW
EXACT_REVIEW_TARGET=69aed186a0d63b3c395a133cd920099d5fa8e000
CANDIDATE=PKA-CANDIDATE-01
MESSAGE_001=CLAUDE_NEXT
TARGET_ARCHITECTURE=NOT_SELECTED
```
