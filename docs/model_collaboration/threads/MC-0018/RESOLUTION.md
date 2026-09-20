# MC-0018 Resolution: W5 Information Architecture Co-Design Closed

**Thread:** MC-0018
**Date resolved:** 2026-09-20
**Status:** RESOLVED / PHYSICAL-AUTHORING V0.2 FROZEN / EMPIRICAL GATES NEXT
**Coordination branch:** `v1-source-vault-bootstrap-resume`
**Task owner:** ChatGPT / `chatgpt-27`
**Claude collaborator:** Claude / `claude-03`
**Claude conversation title:** `03 - Project Knowledge Architecture Foundations and Design Method`
**Exact design target:** `ac45bc7078cd23af85f243cb61ba6a8b499f284d`
**Authority:** Collaboration evidence only. Research 208 records the reconciled W5 design result. Specification 028 and the accepted W0-W4 boundaries remain stronger within their scopes.

## Result

MC-0018 successfully re-engaged the persistent Claude architecture collaborator after W0-W4 implementation and used real successor artifacts to challenge W5's proposed future file/folder/subject architecture.

The thread resolved four main areas:

```text
physical / authoring architecture
    -> V0.2 frozen

semantic-subject architecture
    -> not frozen; empirical T1 required

item-registry identity/carrier architecture
    -> converged direction, empirical T3 required

historical navigation preservation
    -> evidence lifecycle selected, empirical T4 required
```

The collaboration also found one implementation-maintenance defect that should be repaired before production navigation work:

```text
C1
    all eight persistent views currently share one maximal implementation_files
    closure, causing every generator/schema byte change to invalidate all views
```

## Message sequence

```text
001  Claude W5 information-architecture review and counter-design
002  ChatGPT verification, disposition and V0.2 direction
003  Claude V0.2 challenge + bounded W0-W4 implementation-conformance pass
004  ChatGPT final reconciliation + empirical-gate handoff
```

## Accepted architectural outcomes

```text
physical location = primary natural responsibility, not semantic parentage
no generic docs/domains/ wrapper
epistemic/lifecycle families remain justified
top-level natural domain homes remain justified
docs/project_knowledge remains narrow infrastructure
new ordinary names default to lowercase_snake_case
no cosmetic mass rename
update existing natural owner by default
first-class identity + independent lifecycle can justify a separate carrier
no mass historical retrofit
scope:* remains resolver vocabulary, not semantic-subject vocabulary
subject vocabulary must be controlled and membership must not live centrally
one declaration per carrier remains
path-target typed relations remain rejected
project_boundary.v1 is retained
```

## Empirical next steps

```text
C1
    narrow per-view implementation closures

T1
    non-authoritative controlled-subject vocabulary corpus

T3
    item-registry identity/carrier prototype
    D-011 primary case
    AB-032 secondary case

T4
    cold historical-navigation reconstruction with live Knowledge Map withheld
```

Only after these gates should the remaining W5 information-architecture contract be frozen and broad semantic migration begin.

## W0-W4 review disposition

The thread intentionally did **not** duplicate the full W0-W4 qualification program.

Instead, Claude performed one bounded post-implementation architecture-conformance pass. That pass strengthened the major Candidate 01 bets around source-local ownership, selective identity, snapshot discipline, deterministic generated views, capture non-authority and the narrow project-knowledge boundary, while exposing the subject-vocabulary, registry-identity and generator-invalidation issues now carried into W5.

No W0-W4 acceptance is reopened.

## Close

```text
MC0018=RESOLVED
RESEARCH208=GOVERNING_W5_DESIGN_RESULT
PHYSICAL_AUTHORING_V02=FROZEN
BROAD_W5_MIGRATION=PAUSED
NEXT=C1_THEN_T1_T3_T4
```
