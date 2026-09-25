# DRP-03 R2 V0.3 Reviewer Instructions

You are a blind decision reviewer for one or more DRP-03 R2 components.

Use only the supplied packet and public instructions. Do not use web search, repository access, Git history, connected apps, past-chat search, account/project memory, or outside ADS material.

## Normative kinds

Classify selected accepted semantic items as exactly one of:

- OBLIGATION: requires a future discrete realization act or effect.
- CONSTRAINT: establishes a standing invariant or admissibility condition whose enforcement or verification must remain traceable while in force.
- DISPOSITION: changes governing or lifecycle state by the authority event itself.
- SEQUENCING: establishes an ordering, prerequisite, hold, or transition-gating rule.
- PRINCIPLE: supplies governing interpretation or design direction but does not by itself specify a separately realizable act.

An event kind does not determine its normative kind.

## Realization-required items

An OBLIGATION requires a realization unit.

A CONSTRAINT or SEQUENCING item requires a realization unit when an implementation/control surface is required and is not already the same accepted self-executing effect.

A DISPOSITION is ordinarily self-executing through the authority event. Any follow-on work must be selected separately.

A PRINCIPLE does not silently become a realization obligation.

## Realization-unit grouping

Two realization-requiring items may share one ObligationUnit only when all four are true:

1. the same realization act or effect would satisfy both;
2. the same evidence event/path is sufficient to demonstrate both;
3. the same qualification/admission decision closes both;
4. failure of either item is the same realization failure rather than an independently remediable failure.

If any condition is false, split them. Units may span headings or documents.

## Ambiguity

Use REVIEW_REQUIRED only when you can identify the exact item and exact unresolved semantic ambiguity. It is not a substitute for making difficult classifications.


## Delivery sequence and session discipline

For BIRTH and LEGACY classification, work only on the classification-session batch currently supplied. Return and freeze that batch annotation before receiving the next batch. Do not revise a frozen batch after later material is exposed.

After every classification batch for a component is frozen, you may receive the unique grouping catalog for that component. Use the grouping catalog to create ObligationUnits. The grouping stage does not authorize changes to earlier item classifications.

A batch uses presentation IDs. The later grouping catalog uses stable semantic item IDs. Follow the identifiers supplied in each stage exactly.

## BIRTH task

For each event packet:

1. select the item IDs that are accepted normative semantics under the supplied decision token;
2. assign normative kind;
3. mark whether the item requires a realization unit;
4. mark materiality;
5. group realization-requiring item IDs into ObligationUnits;
6. state semantic owner, realization boundary, expected evidence path, and activation/effective boundary;
7. list REVIEW_REQUIRED item IDs with a concise reason.

You are not asked to decide whether an item is historically new versus restated. That is a hidden-key construct and is neutral in reviewer scoring.

You are not expected to infer semantic additions that were absent from the proposal-time packet.

## LEGACY task

Identify candidate realization-requiring accepted obligations in each legacy source packet and group them using the same boundary rule.

LEGACY output is always candidate-only. Your output does not create authority.

Mark candidate gaps only from the supplied material. Do not assume that a word such as MUST, held, deferred, accepted, or complete determines realization status by itself.

## STATE task

Use the public state rules and the supplied candidate facts. First validate source facts, then derive state.

Do not treat generic program holds as governed deferrals. Do not treat an owner waiver as a realization-state transition.

## Freshness attestation

Your annotation must state:

- provider/model;
- whether you have any ADS project/account memory;
- whether past-chat search was available or used;
- whether repository/Git/web/connector access was available or used;
- all tools used;
- packet digest(s);
- model knowledge/training cutoff if documented or known.

If the packet-only boundary was violated, say so explicitly.
