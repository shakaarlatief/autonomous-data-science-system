# MC-0001: Multi-Model Development Collaboration Architecture

**Status:** RESOLVED  
**Topic:** Design and pressure-test the collaboration architecture for ChatGPT + Claude + human development of ADS  
**Task owner:** ChatGPT  
**Independent reviewer / counter-designer:** Claude  
**Human decision authority:** Project owner  
**Review mode:** INDEPENDENT_THEN_COMPARATIVE  
**Active branch:** `v1-multimodel-development-collaboration`  
**Active PR:** #76  
**Stacked on:** `v1-source-vault-bootstrap` at `d9437a8ca07a444400a5eb44ac2c89e8108c91c2`  
**Live transport:** GitHub Issue #77  
**Target authority:** None directly. This thread is collaboration provenance; canonical promotion remains separate.  
**Current phase:** RESOLVED  
**Next expected participant:** None for MC-0001

## Resolution

The architecture review completed through:

```text
001 ChatGPT review request
002 Claude Phase-A counter-design
003 Claude comparative review
004 ChatGPT response
005 Claude bounded Phase-D challenge
006 ChatGPT Phase-D resolution
```

The durable resolution is:

```text
docs/model_collaboration/threads/MC-0001/RESOLUTION.md
```

The sole load-bearing follow-up is no longer conceptual debate. It is the bounded collaboration-state guard implementation frozen in Specification 024 and exercised through MC-0002.

## Review-integrity result

Phase A was independent from the full Research 035 memo and ChatGPT message 001, but not blind to all candidate content because routing/current-state documents already summarized parts of the candidate architecture.

That limitation remains preserved as evidence rather than rewritten away.

## Resolved direction

```text
repository remains project authority
SOLO work remains first-class
collaboration is selective
one bounded task owner
role and write scope are distinct
scoped target-state write ownership
allowed secondary review/provenance write surfaces
machine-readable collaboration state before routine scale-up
coherence guard, not true distributed lock
provider-local sessions such as chatgpt-06 / claude-01
pointer-first issue transport with disclosed fallback
accepted-base-ref independent review for future blind passes
proportional disagreement routing
human arbitration only for genuine project-intent/consequential decisions
API orchestration deferred
```

## Historical live transport

GitHub Issue #77 remains the transport record for MC-0001. It should not be treated as canonical authority.

## Follow-up

```text
Specification 024
    -> MC-0002 implementation
    -> direct Claude review
    -> classification
    -> promotion audit
```
