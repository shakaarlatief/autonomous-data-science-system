# Research 089: Cockpit Implementation Provenance Recovery Completion and Exact-History Gate

**Date:** 2026-08-28  
**Status:** Completed Phase-C recovery evidence; controlled holistic reintegration may now resume  
**Scope:** Closes the implementation-provenance recovery opened by Research 088 / Checkpoint 250 by proving that the recovered manifest is structurally complete and that every declared historical source path exists at its exact integration target.  
**Authority:** Recovery/integration-process evidence. It does not promote a new visual design and does not weaken any source decision, foundation or specification.  
**Interaction environment:** ChatGPT  
**Project / workspace:** Autonomous Data Science System  
**Interaction session:** `chatgpt-09`  
**Conversation title:** `09 - Project Cockpit Design Exploration`  
**Companion collaboration thread:** `MC-0004`

---

## 1. Recovery objective

Research 088 diagnosed the first holistic Cockpit failure as an integration-fidelity failure rather than a repository-preservation failure.

The required repair was:

```text
recover complete Phase-C decision history
    +
distinguish selected / provisional / deferred / rejected / diagnostic evidence
    +
bind implementation obligations to exact historical source artifacts
    +
define deterministic validation
    +
prove the historical bindings actually resolve
```

That recovery substrate now exists.

## 2. Durable recovery artifacts

The repository now contains:

```text
docs/cockpit/PHASE_C_DECISION_LEDGER.md
    exhaustive Research 037-088 disposition ledger

docs/cockpit/ACCEPTED_IMPLEMENTATION_MANIFEST.md
    human-readable source/invariant/adaptation contract

docs/cockpit/accepted_implementation_manifest.json
    machine-readable implementation manifest

scripts/check_cockpit_implementation_manifest.py
    deterministic structural and exact-history validator

.github/workflows/cockpit-implementation-provenance.yml
    full-history CI gate
```

The decision ledger preserves the full design history while preventing the opposite error of treating every explored candidate as an implementation obligation.

## 3. Manifest coverage

The machine-readable manifest contains:

```text
23 total entries
19 required entries
    MUST_PORT or MUST_PRESERVE

4 deliberately non-promotable entries
    PROVISIONAL_ONLY
    DO_NOT_SELECT_DURING_INTEGRATION
    EXCLUDED_SOURCE
```

The required set spans the complete currently held Cockpit integration surface, including Specification 008 capabilities, G4/H4, WorkUnit semantic channels, connector semantics, X5, Z7, Quiet Graphite, Conversation scope/anchor/access, and the source-state restoration model.

The non-promotable set explicitly protects provisional L0/S0, unselected Conversation transition candidates, and the failed holistic browser.

## 4. Exact historical source verification

A durable GitHub Actions gate was added at:

```text
.github/workflows/cockpit-implementation-provenance.yml
```

The workflow performs a full-history checkout:

```text
actions/checkout
fetch-depth: 0
```

and runs:

```text
python scripts/check_cockpit_implementation_manifest.py --verify-git-history
```

The validator uses Git object resolution for every declared binding:

```text
<integration SHA>^{commit}
<integration SHA>:<source path>
```

This means the gate proves that the manifest is not merely syntactically plausible. Every declared exact source file must actually exist at the declared historical target.

## 5. First exact-history CI result

Workflow creation commit:

```text
2127563c0ed980f7bf6fad36e36b11e76500c59b
```

GitHub Actions run:

```text
33156357834
```

Result:

```text
Cockpit implementation manifest: PASS
entries=23 required=19 non_promotable=4
exact historical source verification: PASS
```

Therefore the complete current manifest resolves against repository history.

No historical-path failure remains at this gate.

## 6. Recovery error caught before closure

The recovery process already demonstrated why exact verification is necessary.

An early reconstruction incorrectly named a nonexistent JavaScript refinement file for the selected Z7 deep-focus target. Direct historical inspection showed that the accepted bundle actually contains:

```text
work-unit-deep-focus-spatial-zoom.html
work-unit-deep-focus-spatial-zoom.css
work-unit-deep-focus-spatial-zoom-refinement.css
work-unit-deep-focus-spatial-zoom.js
```

at:

```text
04616a52df5cceff6c59223bbd6f07448d027510
```

The manifest was corrected before the exact-history CI gate was frozen.

This is positive evidence that the new architecture detects reconstruction mistakes rather than allowing plausible-looking provenance to become durable truth.

## 7. What this closes

The Checkpoint 250 recovery requirements are now satisfied at the provenance layer:

```text
complete Phase-C disposition recovered
exact implementation manifest constructed
implementation obligations separated from non-decisions
exact target/source bindings recorded
allowed adaptation boundaries recorded
fixture caveats recorded
verification requirements recorded
deterministic validator added
full-history exact source resolution proven in CI
```

The repository no longer depends on a future integrator remembering which historical HTML/CSS/JS files implement labels such as G4, H4, SEL2, X5, Quiet Graphite or A6.

## 8. What this does NOT close

This result does not mean a replacement holistic Cockpit has passed fidelity review.

There are two distinct gates:

```text
PROVENANCE GATE
    are the accepted sources and boundaries recovered exactly?
    -> PASS

INTEGRATED FIDELITY GATE
    after composition/porting, does the replacement browser actually preserve them?
    -> NOT YET RUN
```

The first gate is now complete. The second becomes the governing gate for the replacement integration.

## 9. Reintegration authorization

The project may now resume holistic Cockpit implementation under a stricter rule:

```text
accepted source exists
    -> reuse or port exact source implementation
    -> preserve invariant geometry / behavior / visual hierarchy
    -> adapt only inside the manifest boundary

provisional default exists
    -> carry only as provisional

candidate is deferred/rejected/evidence-only
    -> do not select through implementation accident

whole-product glue is unresolved
    -> introduce minimum glue
    -> label it provisional
    -> record it separately
```

The failed browser at `8e554d847bb3b6318db432abcb5dff742f0fa523` remains excluded from the source graph.

## 10. Next integration boundary

The next phase is not a fresh design exercise.

It is a controlled source-faithful reintegration:

```text
1. compose/port exact accepted mechanisms
2. keep unresolved shell glue explicitly provisional
3. preserve M01-M23 maturity boundaries
4. run deterministic provenance validation continuously
5. establish component-by-component fidelity checks against exact targets
6. only after those checks pass, present the replacement holistic browser for human product review
```

Production `/cockpit` remains untouched until the design/integration boundary is explicitly promoted later.
