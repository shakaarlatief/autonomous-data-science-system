# R0-P01 owner decision: simplify accidental interruption and replacement authorization

**Date:** 2026-10-11
**Status:** EXPLICIT_HUMAN_APPROVAL / PROSPECTIVE PROCEDURAL SUPERSESSION / NO OWNER EXECUTION AUTHORIZED
**Scope:** Authority for separately owner-authorized replacement research executions after accidental operator mistakes or technical interruptions, preserving original observations. Not authority to execute Attempt 002.
**Parent:** Owner conversation following the explanation of Ctrl+C and the proportionality of the R0-P01 review campaign; Research 513; historical B01/B02 decisions; Claude Message 059.
**Authority:** Human project owner decision about research procedure, recorded by ChatGPT. Does not by itself constitute cryptographic acceptance or authorization to perform a new credential ceremony.

## Decision actually made

ChatGPT offered: **replace the rigid B02 retry restrictions with an explicit owner-authorized replacement procedure**, allowing a new execution after a documented accident or technical interruption even where the original B02 exception conditions would prohibit it, without automatically repeating, discarding or rewriting earlier executions. The owner responded:

> Yes I approve. and you can also save the knowledge about these things in the repo If you want as you will etc and you can also explain to claude etc if you want

This approval follows the owner's repeated explanation that, when something goes wrong accidentally, the owner can say so and exercise project-owner authority to decide that another test should be run, rather than requiring an elaborate engineering/scoring policy to unlock a retry. The owner explicitly distinguished the importance of high-quality ADS architecture work from unnecessary work on a temporary experiment.

## Effective prospective procedural rule

1. **Owner-declared incident is sufficient for the research-governance decision.** For an accidental terminal interruption, mistaken operator input, environment/tool failure or similar practical disruption, the owner may describe what happened in ordinary language and explicitly authorize a **fresh** research execution. The owner declaration is accepted for deciding to proceed; an independent cryptographic proof that the mistake was accidental is **not** a condition of that replacement permission. This is project-owner governance authority, **not** a cryptographic owner-acceptance proof of an ADS action.
2. **No automatic replacement or fixed two-claim budget for this category.** The old B02 cap of two new claimed runs and the `ALL_REQUIRED` exceptional-retry gate no longer constrain **owner-authorized replacements for declared accidents/technical interruptions**. They are prospectively superseded for that limited purpose. Each fresh execution still requires a distinct explicit human authorization and unique trial identity; authorization of this policy is not authorization of Attempt 002 or any future run.
3. **Preserve history and disclose all observations.** Retain the interrupted attempt, raw evidence, timeline, stated cause, original classification (where applicable), owner declaration, disposition and replacement relationship. Do not edit or retrospectively re-score Attempt 001, erase failed controls, invent owner proof, hide inconvenient data, or select only favorable attempts for an architectural conclusion. Invalid/incomplete executions may be excluded from a completed-run comparison only with an explicit, disclosed reason; their incidence remains usability/reliability evidence.
4. **Keep genuine security failures consequential.** A forged proof, altered statement, broken signature verification, contaminated evidence or substantive mechanism failure is never converted into PASS on the strength of an owner's explanation. A diagnosed engineering defect may be repaired prospectively and retested with a fresh owner authorization and new evidence, but the preceding failure remains recorded. Retesting cannot overwrite a negative architectural finding or relax predefined security/measurement thresholds to obtain a preferred outcome.
5. **Do not overengineer the right to restart.** A simple human declaration plus explicit fresh authorization is sufficient as *procedural* permission. Fine-grained Ctrl+C/Node races, Windows process-termination provenance and proof budget semantics should be engineered/tested only insofar as needed for safe cleanup, faithful evidence, meaningful usability measurements, security controls or reproducible actual scoring. They should not be multiplied solely to decide whether an owner may authorize a clean replacement.
6. **Separate actual future execution consent.** Before a real successor run, qualify the relevant nonsecret harness, cryptographic negative tests, isolation and evidence-handling essentials; then request fresh owner authorization for that run. This decision does not allow owner key creation, passphrase handling, WebAuthn ceremony, attempt start marker or other owner-sensitive execution now.
7. **Completed observations remain observations.** A wholly completed, non-accidental negative result is not an “accidental replacement” merely because it is disappointing. The owner may authorize separate prospective engineering or follow-up research, but the original observation continues to count. A PASS does not automatically entitle a fresh comparative claim to change a winner; genuinely new comparisons must be disclosed and preregistered as such.

## Relationship to earlier approved authority

- **Research 513:** Retain scientific preregistration, sign-what-you-see, all 13 security controls, independent proof verification, burden metrics, no post-result tuning-to-green and truthful reporting of repeated testing. Its research goal is not a fixed accident-retry limit.
- **B01 (approved October 10):** Historical acceptance and primary results/arm-evidence semantics remain intact. A prior claimed attempt's event can still be scored under its applicable version. Owner procedural replacement approval is independent of whether that original result was `INVALID_INCOMPLETE`, `INVALID_INSTRUMENT` or another subtype.
- **B02 (approved October 10):** Preserve its exact SHA-bound JSON and historical owner acceptance as evidence of what was approved then. **Prospectively supersede the restart restriction**, including the fixed two-new-claims limit, the exceptional-attempt cap and the “new falsifiable hypothesis” requirement for a declared accidental or technical interruption. Do not falsely edit the old file to make it appear that the original owner decision had different terms. Remaining B02 score/evidence rules continue only where consistent with this later human procedural decision. A later, simplified implementation protocol must explicitly record this precedence.
- **Attempt 001:** Its observed AMEND result, evidence, existing signatures and permanent historical identity remain unchanged.
- **Attempt 002:** Not authorized; F1/F2 remain unfrozen. This owner decision is **only** approval of prospective procedure.

## Minimal operating example

Owner presses Ctrl+C by accident during a native SSH prompt. We preserve what the program observed, record the owner's ordinary-language statement, and stop the original execution safely. The owner can then explicitly approve a **new** run after any required practical repair, without an artificial attempt-cap or independent proof that the keypress was accidental. The original event never becomes a successful signature and is never silently removed from research reporting.

## Consequence for work prioritization

Pause the repetitive Message 059 -> decision-table amendment -> independent review cycle as the default next action. Critically re-evaluate every remaining F1/F2 blocker against **actual cryptographic safety, faithfully recorded measurements, fair comparison, safe execution and reproducibility**. A finding solely about winning an exceptional claim under the now-superseded B02 procedure is no longer a reason to spend days on review. Genuine crypto false positives, wrong owner-proof attribution, missing critical evidence and unsafe Windows handling remain meaningful engineering/test tasks. Use short, independent reviews when they resolve concrete risk, not as an automatic sequence of document approvals.

```text
OWNER_REPLACEMENT_PROCEDURE=APPROVED_PROSPECTIVELY
OLD_B02_TWO_CLAIM_CAP=SUPERSEDED_FOR_OWNER_DECLARED_ACCIDENT_OR_TECHNICAL_REPLACEMENT
OWNER_DECLARATION=SUFFICIENT_FOR_PROCEDURAL_AUTHORITY_NOT_CRYPTOGRAPHIC_PROOF
HISTORICAL_B01_B02_BYTES=UNCHANGED
ATTEMPT_001=IMMUTABLE_AMEND
F1_F2=UNFROZEN
ATTEMPT_002=NOT_AUTHORIZED
```
