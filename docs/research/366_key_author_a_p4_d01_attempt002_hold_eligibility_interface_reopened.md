# Research 366: Key Author A P4 D01 Attempt 002 HOLD and Grouping-Eligibility Architecture Reconsideration

**Date:** 2026-09-27
**Status:** P4 D01 ATTEMPT 002 HOLD / REPEATED HIDDEN ELIGIBILITY FAILURE / NO THIRD RETRY RELEASED / OWNER AMENDMENT DECISION REQUIRED
**Parent:** Research 365 / owner-run local D01 attempt-002 postflight
**Scope:** Record the second D01 grouping attempt's task-owner postflight, distinguish execution success from hidden eligibility inconsistency, stop blind retries, and surface the need to reconsider the P4 grouping/classification interface before any third D01 attempt or D02 exposure.
**Authority:** Empirical HOLD and design-reconsideration boundary only. This record does not authorize a new P4 grouping protocol, D01 attempt 003, D02, held-out grouping, classification repair, LEGACY, canonical key assembly, migration, implementation, or authority switching.

## 1. Attempt 002 postflight

The owner-run deterministic postflight reported:

    artifact schema                     PASS
    rejected-attempt provenance         PASS
    replacement artifact write-once     PASS
    bounded grouping-catalog reads      PASS
    endpoint distinctness               PASS
    endpoint event scope                PASS
    quarantine erratum ordering         PASS
    quarantine erratum structure        PASS
    event cardinality                   PASS
    join/split disjointness             PASS
    lexical endpoint order              PASS
    local settings absent               PASS
    compaction absent                   PASS
    duplicate-pair absence              PASS
    forbidden-source absence            PASS
    forbidden-tool/shell absence        PASS
    pair reasons                        PASS
    pair object shape                   PASS
    deterministic pair order            PASS
    PRECEDENTS unchanged                PASS
    progress accepted-set unchanged     PASS
    progress authorization              PASS
    progress errata count               PASS
    event closed                        PASS
    progress phase                      PASS
    restart accounting                  PASS
    transcript existence                PASS
    transcript model                    PASS
    transcript permission mode          PASS
    transcript session identity         PASS

The sole failed acceptance condition was:

    hidden endpoint consistency         FAIL

Therefore:

    D01_ATTEMPT_002
        HOLD

    D02
        NOT RELEASED

No hidden endpoint identity, pair identity, count, label, reason, or attention mapping is published.

## 2. Interpretation

Attempt 001 exposed that the original D01 executor prompt did not explicitly require grouping-time realization-required eligibility.

Research 365 corrected that omission and attempt 002 executed under the corrected instruction.

Because attempt 002 still fails the same hidden acceptance condition while all observable execution controls pass, the problem can no longer be treated as merely a missing prompt sentence.

The current P4 design asks the grouping author to:

    remain blind to frozen P2/P3 classifications

while the acceptance gate requires:

    exact consistency with those frozen classifications

and the replacement instruction attempts to bridge this by:

    independently re-judging realization-required eligibility from current-event text

That bridge is now empirically shown to be unstable in development grouping.

A third blind retry with stronger wording would risk tuning the semantic author toward an unseen answer key rather than improving construct validity.

Therefore no third retry is released under the current design.

## 3. Design question reopened

The P4 grouping/classification interface is reopened for owner decision before further grouping.

The preferred amendment direction is a minimal downstream eligibility projection:

    frozen Key-A BIRTH classifications remain immutable

    task owner mechanically derives only the item IDs whose frozen primary
    classification has realization_required=true for the current event

    grouping author receives the event content plus an eligibility projection
    sufficient to know which semantic items are in grouping scope

    grouping author still does not read the prior classification artifact,
    attention mapping, classification rationale, normative kind, materiality,
    restatement status, decision-time delta, or any other frozen label

    grouping author makes MUST_JOIN / MUST_SPLIT / UNCONSTRAINED judgments only
    among the projected eligible items

    every stored pair still requires independent pairwise semantic review

    no pair outcome is mechanically inferred

    the hidden task-owner endpoint-consistency gate becomes tautological with
    the supplied eligibility projection rather than a second hidden
    reclassification test

This would make grouping explicitly conditional on the already-frozen classification stage instead of requiring the same logical author to reproduce frozen classification eligibility without seeing its own prior decision.

The same mechanism would be frozen before held-out grouping and later applied symmetrically to Key Author B using Key B's own frozen classifications.

This is a material amendment to Research 363 section 7 because the current design deliberately withholds all prior classification-derived eligibility information from the grouping author.

Owner authorization is therefore required before adopting it.

## 4. Alternatives not selected automatically

The task owner does not automatically:

    accept attempt 002 after deleting inconsistent pairs
    mutate frozen P2/P3 labels
    expose hidden failing endpoint identities
    disclose hidden pair counts
    weaken the endpoint-consistency gate
    continue blind retries until the hidden gate happens to pass
    start D02

Those options would either rewrite frozen semantics, leak hidden truth, or tune against the hidden key.

## 5. Deferred tooling/capability observation

A separate non-semantic observation from this review is preserved for later architecture work:

    the future Project Development System and tool/runtime architecture should
    explicitly support capability-scoped local workspace admission and bounded
    access to private project workspaces when authorized by the owner

Relevant design dimensions include:

    explicit owner authorization
    exact-root admission
    read versus write capability separation
    private/local versus repository authority
    provenance and auditability
    revocation
    safe failure when admission is unavailable
    no silent connector or authority fallback

This is deferred architecture input only.

It does not modify P4 and does not authorize present Runtime Bridge changes.

## 6. Current boundary

    P1_STATE=PASS
    P2_BIRTH_DEVELOPMENT=PASS
    P3_BIRTH_HELDOUT=PASS
    KEY_A_BIRTH_ATTENTION_QUALITY=PASS

    P4_AUTHORIZED=true

    P4_D01_ATTEMPT_001=HOLD
    P4_D01_ATTEMPT_002=HOLD
    P4_D01_REPEATED_FAILURE=HIDDEN_ENDPOINT_ELIGIBILITY

    THIRD_RETRY_RELEASED=false
    D02_RELEASED=false

    P4_GROUPING_CLASSIFICATION_INTERFACE=REOPENED_FOR_OWNER_AMENDMENT

    CLASSIFICATION_REPAIR_AUTHORIZED=false
    LEGACY_AUTHORIZED=false
    CANONICAL_KEY_A_ASSEMBLY_AUTHORIZED=false
    MIGRATION_AUTHORIZED=false

    NEXT=OWNER_P4_ELIGIBILITY_INTERFACE_AMENDMENT_DECISION
