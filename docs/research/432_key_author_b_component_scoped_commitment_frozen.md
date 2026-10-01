# Research 432: Key Author B component-scoped commitment frozen

**Date:** 2026-10-01
**Status:** KEY B STATE+BIRTH COMMITMENT FROZEN / CONSTRUCT COMPARISON NEXT
**Parent:** Research 431 / Research 423
**Scope:** Record completion of the repaired Key Author B STATE+BIRTH run and freeze the component-scoped Key B commitment before any Key A/B construct-validity comparison.
**Authority:** Mechanical completion and commitment-freeze disposition only. This record does not expose Key B semantic bytes, expose Key A semantic bytes, perform construct comparison, adjudicate disagreement, create the final key, run decision reviewers, score DRP-03, implement the successor architecture, migrate repository state, retire the oracle, or switch authority.

## 1. Completion boundary

The single Research-429-authorized fresh resume_after_hold was used exactly once after the V6 grouping-contract repair was qualified and deployed.

The accepted prefix was preserved.

The resumed P8 run reached:

    STATE accepted                    true
    classification batches            15 / 15
    attention gate                    PASS
    grouping events                   13 / 13
    grouping floor                    PASS
    runner                            COMPLETE
    hidden semantic details exposed   false

No additional retry was used.

## 2. Key B component commitment

The purpose-specific P8 finalizer mechanically assembled and froze the Key B component commitment:

    key author slot       KEY_AUTHOR_B
    component scope       BIRTH + STATE
    LEGACY                excluded / INCONCLUSIVE
    P6C                   not run
    serialization         AO10-DRP03-R2-V03-COMPONENT-BUNDLE-V01-CANONICAL-JSON
    commitment SHA-256    fe12b806ff28d81171af87d435172495f51a6f45c2164f2eecbc8b58f2f23e84
    canonical bytes       548226
    BIRTH attention       PASS
    BIRTH grouping floor  PASS

Post-finalization status verifies:

    p8Complete                true
    commitmentFrozen          true
    runner                    IDLE
    grouping events           13 / 13
    grouping floor            PASS
    current phase             P8_KEY_B_COMPONENT_COMMITMENT_FROZEN_AWAITING_COMPARISON
    hidden details exposed    false

## 3. Independence preservation

The Key B semantic run remained under the frozen isolation contract:

    fresh Claude process/session per semantic job
    zero tools
    stdin-only semantic input
    no session persistence
    no Key A semantic material in Key B jobs

The task owner has not inspected hidden Key B semantic output.

The Key B commitment froze before any Key A/B comparison, preserving the Research 330 / Research 332 concealment order.

## 4. Historical LEGACY consequence

The component-scoped amendment remains unchanged:

    HISTORICAL_R2_LEGACY_COMPONENT = INCONCLUSIVE
    HISTORICAL_R2_LEGACY_CONSTRUCT_VALIDITY = NOT_ESTABLISHED
    P6C = NOT_RUN

No LEGACY agreement statistic may be treated as pass, missing-at-random, or zero disagreement.

## 5. Next boundary

Both qualifying component commitments now exist:

    Key A STATE+BIRTH commitment = b632dd680208eb0bba9f3a9c571266b094e640016ea8d635d5cf1606f65b37bb
    Key B STATE+BIRTH commitment = fe12b806ff28d81171af87d435172495f51a6f45c2164f2eecbc8b58f2f23e84

Research 330 requires construct-validity comparison before any decision reviewer runs. Research 420/421 narrow that comparison to STATE+BIRTH only.

The next work is to freeze, implement and qualify a purpose-specific construct-comparison control plane that can mechanically read the two private commitments, compute only the preregistered aggregate agreement metrics, preserve hidden semantic concealment, and stop before owner adjudication or final-key creation.

    NEXT = DESIGN_IMPLEMENT_QUALIFY_CONSTRUCT_COMPARISON_CONTROL_PLANE
