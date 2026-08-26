# MC-0001 Resolution

**Thread:** MC-0001  
**Status:** RESOLVED  
**Resolution date:** 2026-08-25  
**Topic:** Governed multi-model development collaboration architecture  
**Authority:** Collaboration-resolution provenance. Canonical development-method authority changes only through the normal promotion audit.

## Outcome

The first ChatGPT-Claude collaboration trial resolved the conceptual architecture sufficiently to stop open-ended debate and move to a bounded mechanical prototype.

The durable message chain is:

```text
001 ChatGPT review request
002 Claude Phase-A counter-design
003 Claude comparative review
004 ChatGPT comparative response
005 Claude bounded Phase-D challenge
006 ChatGPT Phase-D resolution
```

## Resolved architecture

The models converged, after explicit challenge and several revisions on both sides, on the following candidate design:

```text
repository remains project authority
collaboration remains selective rather than mandatory
SOLO ChatGPT and SOLO Claude work remain first-class modes
one bounded task owner exists for collaborative tasks
roles are per-task and do not imply write authority
write scope is explicit and separate from role
one collaborator owns target-state writes at a time
reviewers may simultaneously write only declared secondary surfaces
collaboration state should become machine-checkable
that state is a coherence guard, not a true distributed lock
GitHub issues/PR comments are transport, not authority
repository message files are durable collaboration provenance
pointer-first issue transport has a disclosed full-content fallback
independent-first review uses an accepted pre-proposal ref when practical
independence contamination is disclosed and classified, never erased
provider-local session numbering uses self-describing IDs
human involvement is reserved for genuine project-intent or consequential decisions
API orchestration remains deferred until evidence justifies it
```

## Review-integrity finding

MC-0001 did not produce a fully blind Phase A.

Claude avoided Research 035 and ChatGPT message 001, but the current routing documents already summarized candidate architecture content.

Therefore:

```text
independent from full candidate memo     yes
blind to all candidate content           no
classification                           partially independent
```

Future deliberately blind review should normally use an accepted pre-proposal base/ref plus a neutral problem packet. Framing bias remains a second-order risk and should be audited proportionately for unusually consequential reviews.

## Disagreement routing conclusions

```text
FACT
    inspect source / repository / deterministic evidence

INTERPRETATION
    expose shared evidence and differing inference; seek discriminating evidence

REQUIREMENT
    inspect canonical authority first; human decides only when requirement must be chosen/changed/extended

ARCHITECTURE
    compare against accepted requirements; prototype/falsify where useful

RISK
    no blanket conservative-wins rule; use proportional lightweight or fuller risk characterization

EVIDENCE_SUFFICIENCY
    define stronger evidence/gate or preserve unresolved status

NORMATIVE_PROJECT_INTENT
    human decision

SCOPE
    inspect task authority first; no blanket narrow-scope-wins rule
```

## Human role

The human is not a routine transport clerk or approval gate for every collaboration transition.

Routine thread opening and uncontested ownership handoffs can proceed under the governed process.

Human arbitration remains required when the issue is genuinely about project intent, desired requirement changes, consequential risk acceptance, resource commitment, or an unresolved choice for which technical evidence cannot determine the desired direction.

## Provenance and naming

Candidate convention:

```text
ChatGPT project/workspace   Autonomous Data Science System
ChatGPT session ID          chatgpt-NN
Claude project/workspace    Autonomous Data Science System
Claude session ID           claude-NN
visible chat title          NN - Main Topic / Stage
collaboration thread        MC-NNNN
```

Model/configuration, interaction surface, and effort/reasoning mode may be useful optional provenance. Fields that the model cannot reliably introspect should preserve the source of the value when known rather than being guessed.

## Mechanical follow-up

One load-bearing item remains before routine multi-model canonical development:

> Implement and validate a scoped machine-readable collaboration-state coherence guard.

That follow-up is frozen prospectively in Specification 024 and will be exercised by MC-0002 using a direct-review mode.

## No automatic canonization

This resolution does not by itself amend:

```text
docs/DEVELOPMENT_METHOD.md
docs/CONTINUITY.md
docs/checkpoints/README.md
docs/DECISIONS.md
```

Those changes are candidates for promotion only after the collaboration-state prototype has passed its frozen gates and survived direct cross-model review.
