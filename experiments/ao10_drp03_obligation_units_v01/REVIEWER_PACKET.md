# DRP-03 Obligation-Unit Reviewer Packet V0.1

Use the exact source base `870689734673e6e8c2212035afcdf27daf733c15`.

## Goal

Independently identify accepted normative propositions and group them into
ObligationUnits using the frozen rule:

> smallest semantic group of accepted normative propositions sharing one
> realization boundary and one evidence path.

Do not create units merely because text says MUST. Do not omit obligations
merely because text does not say MUST.

## Source roles

- ACCEPTANCE_EVENT: accepted owner/governance event. Delimit the obligations
  actually created or adopted by the event.
- GOVERNING_TRACE: existing governing contract used to test granularity and
  realization mapping. For Specification 028, review only the headings allowed
  by review_scope.json.
- SUPPLEMENTAL_KNOWN_WITNESS: review only the allowed witness heading.
- NEGATIVE_CONTROL: candidate/research evidence, not an accepted governing
  transition. It should normally create no obligation units merely by
  discussing proposed requirements.

## Proposition rules

Each proposition must:

- use the exact source heading as source_anchor;
- express one normative proposition close to the source wording while
  preserving actor/modality/object/consequence;
- avoid merging clauses that can have different realization/evidence paths.

Then group propositions into units only when they share one realization
boundary and one evidence path.

## Realization facts

Do not author a RealizationState label. Supply source-owned facts only:

- realization_relation_refs
- deferral_refs
- evidence_refs
- qualification_refs
- activation_refs

The harness derives state.

A governed deferral outranks other facts for the current state and derives
DEFERRED.

Use the five support acceptance records in review_scope.json as evidence for
already-realized W0-W4 obligations.

## Known sensitivity witnesses

The protocol requires you to surface these if supported by the frozen evidence:

- W_SPEC028_SECTION3_NAMED_RESPONSIBILITY_GAP
- W_AO6_BRANCH_ROTATION_ATTACH_GAP
- W_R311_ENGINEERING_NO_MUST

Attach the tag to the relevant unit. The tag does not dictate the unit's
derived state.

## Negative controls

Research 308 and Research 314 discuss candidates/readiness but are not accepted
governing transitions. If you find no accepted obligation birth event in one,
set creates_no_obligation_units=true and leave obligation_units empty.

## Independence

Two reviewers annotate independently before comparison. Do not inspect the
other reviewer's annotation.

## Output

Follow annotation_schema.json exactly and preserve review_scope.json source
order.

Source references should be compact repository locators, not copied passages.
