# Research 458: OPERATIVE SP-6 detective-only null-baseline comparison result

**Date:** 2026-10-03
**Status:** SP-6 COMPLETE / OPERATIVE_INCREMENTAL_CONTROL_VALUE / NO PRODUCTION SELECTION
**Protocol:** Research 457
**Comparison artifact:** experiments/ao10_operative_sp6_v01/SP6_COMPARISON_V01.json
**Artifact SHA-256:** 1a05cefe93230bccc70a206758b8b1046a565004f2dfc65b3265e8e2b722b64d
**Historical snapshot:** 0a68787aee5f2c6332d6ee1fb6adbf0efe92a41d
**Scope:** Record the frozen desk comparison between detective-only null baseline N and the surviving OPERATIVE V0.2 mechanism.
**Authority:** Development evidence only. This result does not select a production architecture, amend Specification 028, authorize migration, resume dependent DRPs, expose hidden R2 material, or switch authority.

## 1. Main result

The detective-only baseline is stronger than a strawman.

On the three frozen public historical realization gaps:

    H1 Specification 028 package responsibilities  DETECTED
    H2 reconstruction planner                      DETECTED
    H3 AO-6 ROTATE completion                      DETECTED

On the three realized controls:

    identity responsibility                        NO_GAP
    authority responsibility                       NO_GAP
    workstream responsibility                      NO_GAP

Therefore:

    N positives = 3 / 3 correct
    N controls  = 3 / 3 correct

OPERATIVE's counterfactual structured replay is also correct on all six.

So the evidence does not support:

    OPERATIVE_REQUIRED_FOR_RELIABLE_DETECTION

Detective/audit practice can catch these known misses.

## 2. The material difference is timing and control, not raw detection

H1 and H2 were surfaced later through retrospective semantic/audit comparison.

H3 was exposed at the action boundary when the live ROTATE attempt could not complete local attach/switch and was later preserved by AO-9.

Thus N can discover and later preserve important misses, but two of three positive witnesses were discovered only through later audit.

## 3. What OPERATIVE adds

The OPERATIVE arm is explicitly counterfactual.

It was not active at the historical snapshot.

Using only the mechanism already supported by SP-2/SP-3, an accepted requirement identity plus governed lifecycle/deferral and realizer coverage can keep each realization obligation continuously machine-visible.

For future implementation-pending obligations, missing coverage need not be treated as an immediate violation. A governed deferral/lifecycle can preserve an accepted-but-open state and later make the relevant gate mechanically fail if qualified realization is still absent.

For ROTATE, selected action plus a completion requirement and no valid attach/switch receipt can mechanically preserve selected != completed without a later model reconstructing that relation from narrative history.

The unique incremental capabilities in this replay are:

    generic continuous coverage visibility
    exact requirement -> realizer/evidence -> operational-result lineage
    deterministic source-fact predicates
    eligibility for governed admission/block behavior
    no need for detector inference to become authority

These capabilities are already represented in admitted competency questions from SP-1.

## 4. Burden comparison

No weighted cost score is used.

### OPERATIVE fixed prototype burden

Observed in SP-3:

    coverage validator                    55 nonblank code lines
    predicate engine A                   56 nonblank code lines

Minimum observed mechanism prototype:

    111 nonblank code lines

Qualification-only development overhead:

    independent engine B                 40 nonblank code lines
    comparison runner                    29 nonblank code lines

Those 69 lines should not be mistaken for mandatory production runtime burden.

### OPERATIVE minimum marginal representation in this replay

    accepted requirement identities      6
    exact domain references              6
    integrated owner review events       2 assumed minimum
    valid realizer coverage declarations 3
    gap cases with no valid coverage     3
    new generic predicate definitions    0
    leak-review events                   0

The two-review assumption groups the Specification 028 family into one governing source/consequence review and the AO-6 family into one.

SP-2 remains the only observed owner-review burden evidence:

    LOW after task clarification.

### N marginal observed burden

    persistent cross-domain obligation records   0
    minimum positive-gap discovery judgments     3
    same-boundary discoveries                    1
    later retrospective discoveries              2

Later targeted regression examples include:

    AO-9 R7 for selected Specification 028 realization gaps
    AO-9 R11 for selected ROTATE != completed rotation

The full AO-1/AO-9 program is not charged to these gaps.

## 5. Frozen decision-rule evaluation

N_LOWER_COST_COMPARABLE_CONTROL is not satisfied.

Although N handled all six cases, it does not provide the same generic deterministic lineage and governed consequence power as the structured arm without adding machinery that would move it away from the frozen detective-only definition.

OPERATIVE_REQUIRED_FOR_RELIABLE_DETECTION is not satisfied.

N detected all three historical misses.

NO_ECONOMIC_DOMINANCE is not the best description because the comparison does identify a named incremental control outcome already required by admitted competency questions.

Therefore:

    SP6 = OPERATIVE_INCREMENTAL_CONTROL_VALUE

Meaning:

    detective-only N is a credible and cheaper-looking detection baseline;

    OPERATIVE adds a qualitatively different generic control capability:
    continuously tracked accepted requirement -> realization -> operational consequence;

    the extra control has bounded micro-probe burden so far;

    this supports continued development but does not by itself justify production adoption.

## 6. Important limitations

The three positive witnesses were selected because they are known historical misses.

That favors N because its actual historical discovery is already known.

The OPERATIVE side is counterfactual and therefore cannot claim observed prevention.

The six-case replay is too small for production economics.

The fixed-code-line counts are prototype measurements, not engineering estimates.

The owner-review count is an explicit minimal assumption.

The comparison says nothing about long-run maintenance burden across hundreds of governing acts.

## 7. Architectural implication

The null baseline remains valuable even if OPERATIVE continues.

A mature system should not assume structured authoring is perfect.

Detective mechanisms can remain as recital-leak detection, realization-gap audit, policy/claim checks, and periodic repository integrity review.

The architectural question is therefore potentially:

    thin accepted machine consequences
    + deterministic realization/control
    + independent detective safety net

versus:

    detective-only
    + targeted claims/checks.

## 8. Interaction with the reopened rich-owner-approved option

The owner's recent observation changes the next design question.

R2 ruled against relying on later inferred rich semantics as authoritative truth.

It did not prove that a richer semantic representation could not work when the model drafts it, the governing human sees source meaning beside it, the human accepts/amends it, and the accepted structure becomes authority.

That is materially different from the failed inference-heavy architecture.

SP-6 does not compare that candidate against thin OPERATIVE.

Therefore no larger pilot or production selection should assume that thin OPERATIVE has already beaten:

    RICH_ACCEPTED = richer structured semantics + explicit owner acceptance

The next discriminating step should compare whether the extra rich fields answer admitted competency questions or deliver control value not already obtained by thin OPERATIVE, and what additional owner/maintenance burden they impose.

## 9. Current disposition

    SP6=COMPLETE
    SP6_RESULT=OPERATIVE_INCREMENTAL_CONTROL_VALUE

    N_POSITIVES=3/3
    N_CONTROLS=3/3
    N_IS_CREDIBLE_BASELINE=true

    OPERATIVE_GENERIC_LINEAGE=true
    OPERATIVE_GOVERNED_CONTROL=true
    OPERATIVE_PRODUCTION_SELECTED=false

    SP5=RETIRED_AS_NON_DISCRIMINATING

    RICH_ACCEPTED_CANDIDATE=REOPEN_FOR_COMPARISON
    OLD_INFERENCE_AUTHORITATIVE_ARCHITECTURE=NOT_REOPENED

    HIDDEN_R2_DETAILS=SEALED

    NEXT=FREEZE_THIN_VS_RICH_ACCEPTED_COMPARISON
