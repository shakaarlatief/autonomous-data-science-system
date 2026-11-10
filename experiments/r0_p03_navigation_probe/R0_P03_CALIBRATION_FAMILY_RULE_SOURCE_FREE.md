# Prospective source-family qualification rule — proposed, source-free

**Classification:** Publicly shareable methodological proposal. This document contains no case-specific findings and does not authorize admission or disclosure of any source.

```text
RULE = PROPOSED_NOT_FROZEN
SOURCE_ADMISSIONS = ZERO
AUTHOR_WORLD = WORLD_UNFROZEN
FALSIFICATION_HOLDOUT = NOT_ACCESSED
```

## 1. Purpose, unit of decision, and non-circularity

This rule determines whether evidence-bearing material can enter a specified future source world, and **for which purpose and temporal claim**. It must not decide which experimental treatment ought to win, create reference answers, or make an artifact authoritative by finding it relevant. It is an eligibility screen, not a scorer, reference annotator, or authority-promoting mechanism.

Qualify a **source family** defined prospectively by its *evidentiary function, claimed authority, lifecycle state, intended task use, temporal applicability, and disclosure risk*; filenames, locations, extensions, keywords, citation counts, and similarity to an expected answer are merely discovery signals. A family rule supplies a default evidentiary burden, not unconditional acceptance of every member. Each proposed member requires an identity-and-exception check, and a single material counterexample blocks unreviewed batch admission.

The qualification unit is the tuple:

`(source revision, family, proposition(s) supported, effective time, intended audience/use, permitted representation, dependency closure, exposure set)`.

A source can support a historical statement without supporting the corresponding *current* statement; can prove that a test ran without proving deployment; and can be relevant without being eligible for disclosure to task authors, reference annotators, treatment engineers, or evaluators.

## 2. Family-level authority and evidence matrix

Assign by **content and governing provenance**, not by path or asserted status. Multiple roles may coexist; apply the strictest material condition.

| Family / evidentiary role | Positive evidence required for proposed eligibility | Non-transferable boundary |
|---|---|---|
| **A. Governing decision or operational contract** | Identifiable competent decision-maker; explicit approval/adoption and scope; effective/version boundary; authoritative predecessor/successor chain; evidence the record is applicable to the intended claim and date | Approval of a plan is not implementation, actual control enforcement, or permission for a broader operation |
| **B. Implemented natural-owner or technical state** | Revision-bound real implementation/source or authoritative state; ownership of the asserted fact; dependencies and configuration; representative implementation or operational checks; absence of overriding later state | A design, generated model, synthetic fixture, or reported implementation is not itself proof of a deployed/current implementation |
| **C. Validation or experimental observation** | Frozen tested claim, test setup, inputs, execution record, actual outputs, negative/failure evidence, postconditions, provenance and scope limitations; ideally independently rerunnable artifacts | Passing a unit, synthetic, mock, descriptive, or static test does not prove an end-to-end live, human, security, production, or general result |
| **D. Research, proposal, comparison, or preregistration** | Exact revision, explicit proposal/freeze/authorization stage, alternatives and contradictions, linkage to any distinct later decision | A frozen proposal is not an adopted target; an unexecuted comparison has no measured winner |
| **E. Historical event, status, or checkpoint** | Dated, revision-bound event claim; supporting lower-level records; distinction between event time, record time, current state, and later reversal | Valid history is not present operational authority; a summary cannot expand the proof contained in its underlying record |
| **F. Task, evaluation, reference, or prior-result material** | Evidence of provenance and exposure, and proof that disclosure cannot reveal reference choices, answer structure, treatment features, prior outcomes, or scoring hints to an unauthorized recipient | If answer or design contamination is material, keep restricted regardless of historical accuracy or public provenance |
| **G. Derived, indexed, synthesized, or cited material** | Proven original inputs, transformation lineage, reproducible binding to source versions, complete limitations, and an applicable authority rule | Retrieval rank, citation edges, summaries and derived labels never confer authority on an underlying claim |
| **H. Opaque, inaccessible, or unsupported material** | Original reviewable bytes and a reliable parser/inspection path, with source identity and integrity established | Metadata, a filename, a neighboring citation, or an inaccessible compressed object cannot stand in for source-content examination |

Family membership is not exclusive. A document with a governing heading may primarily record a proposal or historical status. An executable artifact may still be test-only. If family classification depends on missing evidence, it is unresolved, not inferred from surface features.

## 3. Minimum positive evidence, applied before any admission proposal

A proposed qualification record must contain all applicable fields below, with direct citations to examined revision-bound evidence and explicit `UNKNOWN` where appropriate:

1. **Identity:** exact bytes or reproducible source revision, digest, readable format, evidence of origin, and any mismatch between manifest claims and inspected content. A cryptographic match to a provided manifest establishes internal consistency, not independent authenticity of that manifest.
2. **Proposition and scope:** precisely what statement this source can establish, including population, environment, action, time, conditions, and prohibited extrapolations.
3. **Authority:** the purported decision-maker/natural owner, evidence of authorization and acceptance, priority relative to applicable governing sources, and whether authority was effective at the queried time. A claimed `FROZEN`, `PASS`, `ACCEPTED`, or `CURRENT` label alone is insufficient.
4. **Temporal resolution:** creation/record time, operative/effective time, historical cutoff, amendments, later supersession or reactivation, and the difference between past truth and current applicability. Do not equate a newer file, later timestamp, or latest commit with governing status.
5. **Realization:** whether the source describes a proposal, executable implementation, observed invocation, deployed operation, owner-authorized action, or verified outcome. Require separate evidence for each promoted claim.
6. **Validation:** exact observations and independent or alternative corroboration; positive and negative controls; failed, timed-out, unexecuted and truncated steps; unknown environments, absent raw records, and possible self-report bias. Report the narrowest demonstrated result.
7. **Dependency and contradiction ledger:** declared references, cited predecessors/successors, competing authority, missing original artifacts and external dependencies. Investigate citation links as leads; never treat them as proof that a test, authorization, or decision exists. Absence of a citation is not proof of absence of relevant dependencies.
8. **Disclosure and contamination assessment:** whether the source alone or in combination with an admissible source, snippet, metadata, search result, or citation trail leaks prior answers, scoring rules, hidden selections, treatment design, expected outputs, or reference labels. Evaluate the *recipient's aggregate accessible set*, not merely lexical matches in one document.
9. **Strongest falsifier and next test:** a concrete observation that would overturn the proposed scope or disposition, the required original evidence to seek, and an independent review path.
10. **Custody and permitted representation:** full source, separately regenerated minimally sufficient excerpt, or restricted citation-only metadata, with an explicit audience and digest. Sanitization must be reviewed as a new artifact; redaction does not inherit admission from its parent.

Each field must be supported by evidence at a suitable level. A report saying a test passed cannot substitute for absent primary execution evidence when the proposed claim requires execution verification. Missing independent confirmation can support a *bounded historical-report* claim but not silently a broader current/operative claim.

## 4. Prospective dispositions and decision algorithm

All dispositions here are **recommendations pending a separate authorized freeze and per-source release**. None is an admission.

- **CANDIDATE_CURRENT_BOUNDED:** sufficiently verified, presently applicable, audience-safe for a narrowly named set of propositions; all material requirements above satisfied. Requires independent sign-off and a separate release action.
- **CANDIDATE_HISTORICAL_BOUNDED:** supports a dated state/event, with explicit cutoff and non-current warning; sufficient proof and safe permitted audience. Never auto-upgrades to current status.
- **CANDIDATE_SANITIZED_DERIVATIVE:** only a newly authored, hashed, independently checked excerpt/representation is eligible; the parent remains restricted. The derivative must preserve materially relevant uncertainty and falsifiers.
- **HOLD_MATERIAL:** a potentially eligible proposition exists, but one or more material inputs or conflicts is unresolved. No author/evaluator disclosure or eligibility while on hold.
- **EXCLUDE_FOR_INTENDED_WORLD:** demonstrably inappropriate, unneeded, unauthorized, contaminating, or incapable of truthfully supporting the intended use. Historical custody can remain appropriate; exclusion is not a claim that the historical record is false.
- **RESTRICTED_REVIEW_ONLY:** eligible to be studied by an authorized non-arm reviewer but not to enter author, gold, arm, or scorer worlds. This can coexist with HOLD or EXCLUDE for the intended world.

Decision procedure:

1. Freeze the **intended-use specification** independently of any proposed member's desired answer. Define audience, temporal question, required evidentiary strength, and allowed representations.
2. Inventory candidate revisions, family roles, provenance, content and context. Record unknowns; identify overlapping and missing semantic dependencies, including evidence not supplied.
3. Map claims to decision/implementation/validation/history layers, separating original observation from an authorial interpretation. Resolve contradictions by scope and competent authority, not document count or recency alone.
4. Apply disclosure and contamination tests **before** possible inclusion; test single-source and plausible combined-source disclosure. A clean lexical scan or citation graph never clears this gate.
5. Apply the appropriate family burden and run the material-HOLD tests. A failed hard safety/exposure condition results in exclusion for the intended audience; lack of evidence normally results in HOLD, not a permanent negative conclusion.
6. Draft the least expansive supportable disposition and falsifier. Independently review likely wrongful admissions and exclusions, document dissent, and only then submit a separate release request. No family-wide admission by analogy.

## 5. Mandatory material HOLD conditions

Use HOLD when any of the following could change eligibility, authority, truthful answerability, safety, or fairness:

- Original revision/bytes are absent, corrupted, compressed without a trustworthy inspection path, unsupported, or represented only by metadata or a neighboring source.
- A consequential reference, acceptance decision, owner authorization, implementation artifact, underlying log, fixture, raw measurement, or competing/superseding record is missing or unverifiable.
- Effective-time/record-time relationships, current versus historical authority, adoption versus implementation, or deployment scope cannot be resolved.
- Apparent results rely on draft, simulated, synthetic, self-reported or truncated evidence that does not establish the proposed operative claim.
- Citation/context closure is incomplete and an omitted dependency might materially alter interpretation; a bounded citation harvest is not semantic closure.
- A conflicting source is credible and cannot be adjudicated without making an experimental-design choice or inferring a missing decision.
- The audience/exposure ledger is incomplete, or combining the source with other accessible material may reveal reference answers, gold labels, historical solution paths, treatment designs, holdout composition or scoring cues.
- A required source representation or modality is inaccessible, or a transformed representation might drop material contraindications and caveats.
- A fair, arm-neutral positive witness cannot be constructed without inventing relationships, current state, adoption or validation.

A HOLD must identify the **specific missing discriminator**, expected evidence type, responsible independent decision authority, and possible later outcomes. If no safe way to resolve it exists, continue withholding. Do not rebrand uncertainty as rejection merely to reach a target corpus size; do not admit to meet a quota.

## 6. Safeguards against wrongful admission *and* wrongful exclusion

**Against wrongful admission:** fail closed on identity, provenance, applicability, competence, missing material dependencies and disclosure; require source-level negative claims to be checked for contradicting records; enforce the narrowest validated scope; preserve rejected and superseded historical evidence with correct timestamps; no generated state or citation edge promotes authority; no task-author/gold/arm/scorer access to restricted material; keep a separate release ledger from the reviewer recommendation.

**Against wrongful exclusion:** do not discard a source solely because it is old, a checkpoint, a draft, technical, unfamiliar media, uncited, lexically flagged, or not currently governing. It may still be valuable as scoped history, a negative control, a tested failure boundary, a design alternative, or a reproducible observation. Split mixed records into independently reviewed representations where safe. Preserve minority/contradictory evidence, explicit UNKNOWN, a reversible HOLD, and a documented positive pathway to qualification. Audit for both false positives and false negatives in each family.

**Against circularity and overfitting:** family burdens precede final source selection and must not be tuned using task outcomes or treatment performance. Do not select the corpus because it makes particular tasks answerable in a preferred manner. Do not repair labels after outputs. Apply the same authority, realization, validation, freshness and disclosure standards to every treatment. Hold out an independently controlled challenge set, unseen during rule drafting; the challenge reviewer, not the calibrator, conducts the later test.

## 7. Falsification protocol for an independent later reviewer

Before any later challenge, freeze this rule's definitions, thresholds, allowed exceptions and change-control method. The reviewer must operate without the rule author's access to challenge sources or answers and must record provenance of any prior exposure. Evaluate independently sampled positive and negative conditions across families, with adversarial cases involving temporal reversals, incomplete validation, misleading labels, missing original media, conflicting authority, undisclosed dependencies and combined-source leakage.

For each challenged decision, determine whether the exact **claimed proposition, temporal scope and audience** was actually justified. Report at least:

- **Wrongful admission:** material falsifier, missing original evidence, misassigned current authority, overstated validation/implementation, unsupported representation, or contamination that should have forced HOLD/EXCLUDE.
- **Wrongful exclusion:** original evidence actually satisfies the stated family burden and the source can be safely included in a narrower historical, bounded or sanitized role; identify which rule wrongly foreclosed that role.
- **Legitimate HOLD:** uncertainty remains material despite reasonable original-dependency examination; specify exactly what evidence could resolve it.
- **Indeterminate:** reviewer cannot access necessary evidence; never count as a correct acceptance or rejection.

Any verified wrongful admission is a stop condition for the affected family release and prompts a bounded rule revision, new version, independent re-review and retest. Wrongful exclusions prompt a less restrictive evidence-based pathway without relaxing authority and exposure guards. A single confirmed material counterexample falsifies an unconditional family admission claim. No numeric success rate can excuse a known safety- or reference-leakage failure.

## 8. Required audit record and freeze/release separation

For each proposed member, maintain a restricted audit row with: revision/digest; family and claims; temporal authority; governing decision; realization level; direct validation and failures; inspected adjacent files; omitted dependencies; contradictions; disclosure interactions; proposed disposition; strongest falsifier; necessary next action; independent reviewer and disagreement record; permitted representation; source-world version; final separately authorized admission decision (initially **NONE**).

For the family as a whole, publish only the reusable method and aggregate methodological limitations. Do **not** publish sensitive source identities, quotations, case dispositions, prior answers, hidden reference selections, or treatment-specific design details. The case ledger is owner-private, not a source of prompts or gold. Rule publication does not change source eligibility.

**Freeze criteria:** independently reviewed evidence thresholds; documented error taxonomy and disagreement procedure; no unresolved material contradictions inside the rule; prospective audience/claim definitions; independence and custody controls; exact version/hash; owner-authorized freeze. **Release criteria:** a *separate*, per-revision, per-audience decision with verified dependencies and sanitized-view review where applicable. Until those separate acts occur, this proposal grants no source admissions and does not freeze the future author world.
