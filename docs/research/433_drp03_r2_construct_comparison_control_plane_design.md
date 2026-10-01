# Research 433: DRP-03 R2 STATE+BIRTH construct-comparison control-plane design

**Date:** 2026-10-01
**Status:** PROSPECTIVE DESIGN FROZEN BEFORE COMPARISON / IMPLEMENTATION + QUALIFICATION AUTHORIZED / NO A-B COMPARISON YET
**Parent:** Research 432 / Research 421 / Research 330
**Scope:** Freeze the purpose-specific mechanical control plane that may compare the already-frozen Key Author A and Key Author B STATE+BIRTH commitments without exposing hidden semantic bytes to the task owner.
**Authority:** Prospective comparison-control design only. Both key commitments already exist and the Research 330 / Research 332 sequence requires construct comparison next. This record authorizes implementation and mechanical qualification of the bounded comparison control plane. It does not itself read the hidden key bundles, perform the live comparison, adjudicate disagreements, create a final key, run decision reviewers, score DRP-03, implement production AO-10, migrate repository state, retire an oracle, or switch authority.

## 1. Preconditions

The comparison control plane is permitted to activate only when it verifies both immutable component commitments:

    Key A
      commitment = b632dd680208eb0bba9f3a9c571266b094e640016ea8d635d5cf1606f65b37bb
      bytes      = 643247

    Key B
      commitment = fe12b806ff28d81171af87d435172495f51a6f45c2164f2eecbc8b58f2f23e84
      bytes      = 548226

Both must use:

    AO10-DRP03-R2-V03-COMPONENT-BUNDLE-V01-CANONICAL-JSON

Both must bind:

    included components = BIRTH + STATE
    BIRTH attention = PASS
    BIRTH grouping floor = PASS

LEGACY is excluded from construct comparison and remains:

    HISTORICAL_R2_LEGACY_COMPONENT = INCONCLUSIVE
    HISTORICAL_R2_LEGACY_CONSTRUCT_VALIDITY = NOT_ESTABLISHED
    P6C = NOT_RUN

The different excluded-component reason strings in A and B are historical provenance and must not be interpreted as a STATE/BIRTH disagreement.

## 2. Purpose-specific P9 boundary

Implement one purpose-specific Runtime Bridge tool:

    codex.p9_construct_comparison_operation

with an action-only caller surface:

    status
    run_comparison

The caller cannot select:

    Key A root
    Key B root
    comparison root
    bundle paths
    item IDs
    event IDs
    fixtures
    labels
    grouping pairs
    thresholds
    formulas
    output paths
    comparison scope

All roots and expected commitments are fixed server-side.

The comparison runs model-free. It invokes no Claude process, ChatGPT process, browser, web, GitHub, MCP subtool, or semantic agent.

## 3. Storage and concealment

Key A and Key B roots are read-only inputs to P9.

P9 writes only to a separate fixed machine-local comparison root:

    %LOCALAPPDATA%/ADS-R2-Construct-Comparison

No comparison artifact may be written into either key-author root.

The task-owner/public-safe surface may expose only preregistered aggregate metrics, threshold results, aggregate disagreement counts, bounded per-event ambiguity counts keyed by already-public packet event IDs, commitment identities, and control state.

It must never expose:

    item-level Key A labels
    item-level Key B labels
    item IDs associated with disagreement
    STATE fixture answers
    fact-validity partitions
    grouping pairs
    grouping reasons
    precedent text
    semantic transcripts
    private key paths
    private canonical bytes

A private comparison artifact may contain the exact disagreement material needed for later owner adjudication, but P9 status/run output must not reveal that material to the task-owner model.

## 4. Structural qualification before metrics

Before computing any semantic agreement statistic, P9 must verify:

    exact bundle hashes and byte lengths
    canonical serialization identity
    component scope = BIRTH + STATE
    public freeze binding equality
    key-author packet manifest binding equality
    owner-acceptance binding equality
    exact 13-event BIRTH event identity set
    exact item identity set within every aligned event
    exact 24 STATE fixture identity set
    exact required item fields
    exact required STATE structural fields
    exact grouping pair shape and canonical orientation
    no within-key grouping join/split collision

Any structural mismatch or commitment drift is a mechanical comparison failure. No semantic gate result may be inferred from a structurally invalid surface.

## 5. BIRTH construct metrics

P9 computes the frozen Research 330 pre-adjudication metrics over aligned BIRTH semantic items.

### 5.1 Normative prevalence

For each author:

    normative prevalence
      = normative item count / aligned BIRTH item count

This is reported descriptively and is not itself a gate.

### 5.2 Binary normativity Cohen kappa

On every aligned BIRTH item, compare the two boolean normative judgments.

Use ordinary two-rater Cohen kappa:

    kappa = (p_o - p_e) / (1 - p_e)

where p_o is observed agreement and p_e is agreement expected from the two marginal distributions.

Gate:

    binary normative kappa >= 0.80

If the denominator is zero, the metric is UNDEFINED and the construct gate fails closed rather than assigning an invented perfect value.

### 5.3 Normative positive specific agreement

Define:

    both_positive
    A_only_positive
    B_only_positive

from the normative booleans.

Compute exactly:

    2 * both_positive
    /
    (2 * both_positive + A_only_positive + B_only_positive)

Gate:

    normative positive specific agreement >= 0.80

A zero denominator is UNDEFINED and fails closed.

### 5.4 Normative-kind Cohen kappa

Compute multi-category Cohen kappa only on aligned items for which both authors mark normative=true.

Gate:

    normative-kind kappa >= 0.75

A zero/degenerate denominator is UNDEFINED and fails closed.

### 5.5 Material positive specific agreement

Apply the same positive-specific-agreement formula to the boolean material field over all aligned BIRTH items.

Gate:

    material positive specific agreement >= 0.90

A zero denominator is UNDEFINED and fails closed.

### 5.6 Grouping-constraint agreement

For each event, canonicalize an item pair to:

    min(item_id_a,item_id_b)
    max(item_id_a,item_id_b)

Each author maps a constrained pair to exactly one category:

    MUST_JOIN
    MUST_SPLIT

The comparison domain is the union of pairs constrained by either author, as frozen by Research 330.

A pair agrees only when both authors constrain it to the same category.

A one-sided constraint or opposite-category constraint is disagreement.

Compute:

    grouping constraint agreement
      = exact same-category constrained pairs
        /
        union constrained pairs

Gate:

    grouping constraint agreement >= 0.80

An empty union is UNDEFINED and fails closed.

## 6. Ambiguity accounting

Research 330 fixes the denominator and cap but does not separately name a numerator operator. P9 freezes the conservative mechanical interpretation before comparison:

For each event:

    denominator
      = union of items either author marks normative

    numerator
      = items in that denominator for which either author marks ambiguity=true

    fraction
      = numerator / denominator

The cap is:

    fraction <= 0.10

P9 reports numerator, denominator and fraction per event and overall.

A zero event denominator yields:

    numerator = 0
    fraction = 0

for that event because there is no normative item on which ambiguity can consume allowance.

This ambiguity accounting is descriptive/cap enforcement only. It never suppresses a material disagreement and never changes an author label.

## 7. Material disagreement accounting

P9 records only aggregate counts publicly.

For BIRTH, an aligned item is a material disagreement when the authors differ on any gating semantic field:

    normative
    normative_kind where applicable
    material

Grouping category disagreements are counted separately.

Differences in:

    realization_required
    restated
    decision_time_delta
    ambiguity

remain recorded privately for reconciliation provenance but are not silently converted into an agreement-gate PASS or FAIL beyond the explicitly frozen metrics/cap above.

No public-safe P9 response exposes which item disagreed.

If any pre-adjudication metric gate fails, outcome is:

    CONSTRUCT_UNDERDETERMINED

Owner adjudication cannot retroactively convert that failed construct gate into PASS.

If all metric gates pass but material disagreements remain, outcome is:

    CONSTRUCT_GATE_PASS_OWNER_ADJUDICATION_REQUIRED

No final key is created by P9.

If all metric gates pass and no material disagreement remains, outcome is:

    CONSTRUCT_GATE_PASS_NO_MATERIAL_ADJUDICATION_REQUIRED

Final-key construction remains a separately governed next stage.

## 8. STATE-REF comparison

STATE expected outputs are compared independently from BIRTH metrics.

For each of the 24 aligned fixtures, the material expected-output structure is:

    fixture_id
    sorted valid_fact_ids
    sorted invalid_fact_ids
    expected_state

The free-text reason is explanatory and is excluded from equality so stylistic explanation differences cannot create a semantic reference disagreement.

P9 reports only aggregate counts:

    fixture count
    exact structural agreement count
    fact-validity disagreement fixture count
    final-state disagreement fixture count

If any material structural STATE disagreement exists:

    STATE_REF = CONSTRUCT_UNDERDETERMINED

and the overall comparison cannot proceed to final-key reconciliation.

If all 24 material structures agree:

    STATE_REF_AUTHORS = AGREE

This does not yet claim the frozen reference implementation itself is correct. Research 330 separately requires the eventual STATE reference implementation to achieve 100% accuracy against the agreed frozen expected outputs; that implementation comparison is outside P9.

## 9. Overall comparison outcome

P9 returns one bounded overall state:

    CONSTRUCT_UNDERDETERMINED
    CONSTRUCT_GATE_PASS_OWNER_ADJUDICATION_REQUIRED
    CONSTRUCT_GATE_PASS_NO_MATERIAL_ADJUDICATION_REQUIRED

CONSTRUCT_UNDERDETERMINED is mandatory when:

    any required BIRTH gate metric is below threshold
    any required BIRTH gate metric is undefined
    STATE_REF has a material structural disagreement
    structural comparison preconditions fail in a way that makes semantic comparison invalid

Mechanical integrity failures use a specific P9 error code and do not masquerade as semantic disagreement.

## 10. Private comparison artifact

A successful mechanical run freezes a deterministic private comparison record bound to:

    Key A commitment SHA-256
    Key B commitment SHA-256
    public freeze SHA-256
    protocol ID
    comparison algorithm version

It stores:

    aggregate metric numerators/denominators
    exact aggregate metric values
    threshold results
    STATE aggregate comparison counts
    ambiguity aggregate counts
    private disagreement details needed for later owner adjudication
    overall outcome

The public-safe receipt exposes only the permitted aggregate projection plus the comparison-record SHA-256 and byte length.

A repeated run after freeze is idempotent: verify and return the existing public-safe receipt. It must not recompute against drifted inputs.

## 11. Qualification requirements

Before live A/B comparison:

    synthetic perfect-agreement fixture PASS
    synthetic threshold-boundary fixtures PASS
    binary-kappa known-answer fixture PASS
    multi-category normative-kind kappa known-answer fixture PASS
    positive-specific-agreement known-answer fixture PASS
    grouping union/category agreement known-answer fixture PASS
    one-sided grouping constraint disagreement fixture PASS
    opposite grouping category disagreement fixture PASS
    undefined-kappa fail-closed fixture PASS
    empty grouping-union fail-closed fixture PASS
    ambiguity numerator/denominator/cap fixture PASS
    STATE exact structural agreement fixture PASS
    STATE fact-validity disagreement fixture PASS
    STATE final-state disagreement fixture PASS
    STATE reason-only difference non-material fixture PASS
    commitment drift rejection PASS
    event/item/fixture alignment rejection PASS
    hidden-detail public-surface leak checks PASS
    comparison artifact immutability/idempotence PASS

Inherited regressions must also remain PASS:

    P8 regression
    P8 headless runner smoke
    P7 component-key regression
    P6 legacy regression
    P6 headless runner smoke
    P5 private-ops regression
    P4 private-ops regression
    Codex compatibility regression
    public surface registration
    flexible authority regression
    bounded Git regressions
    runtime release regressions

Managed publication, restart and exact verification must pass with:

    mismatchCount = 0

## 12. Execution authority after qualification

The Research 330 / Research 332 frozen sequence already requires construct comparison after both commitments and before decision reviewers.

Therefore, after this exact P9 design is implemented, qualified, published, activated and verified, the task owner may call:

    run_comparison

without another semantic authoring vote.

That call is mechanical only.

If the result requires owner adjudication, stop at that governed boundary and design the owner-only adjudication path without exposing hidden dispute content to the task-owner model.

If the result is CONSTRUCT_UNDERDETERMINED, stop. Do not retry, relabel, tune thresholds, or create a final key.

## 13. Current boundary

    KEY_A_COMPONENT_COMMITMENT = FROZEN
    KEY_B_COMPONENT_COMMITMENT = FROZEN
    HIDDEN_SEMANTIC_DETAILS_EXPOSED = false

    P9_CONSTRUCT_COMPARISON_DESIGN = FROZEN
    P9_IMPLEMENTATION = AUTHORIZED
    P9_QUALIFICATION = AUTHORIZED
    LIVE_CONSTRUCT_COMPARISON = NOT_RUN

    NEXT = IMPLEMENT_QUALIFY_DEPLOY_P9_CONSTRUCT_COMPARISON
