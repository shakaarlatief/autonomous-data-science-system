# Research 214: W5 T4 Historical Navigation Preservation Result

**Date:** 2026-09-20
**Status:** T4 ACCEPTED / HISTORICAL NAVIGATION EVIDENCE CONTRACT FROZEN
**Selected architecture:** `PKA-CANDIDATE-01`
**Governing W5 design:** Research 208
**Fixture freeze:** Research 213
**Fixture commit:** `619344bd284d70e47bad80c57d537ff1f50dee3f`
**Source boundary:** `4b94ffe183ff7af72cef6ee7492b4ba2f30c11ef`
**Legacy Knowledge Map SHA-256:** `a212bb2bf5ba2fa7f9e19e573932c3663dc83b02d980373dcd8f811d03b2d291`
**Scope:** Interpret the frozen T4 cold-navigation experiment and freeze what routing evidence must be captured before eventual legacy Knowledge Map retirement.
**Authority:** W5 design result only. This result does not retire the live Knowledge Map, create successor navigation authority, begin broad W5 semantic migration, or switch operational authority.

## 1. Mechanical result

The routing-only evidence candidate reproduces the frozen legacy map's navigational structure exactly:

```text
subject structures                         exact parity / 19
checkpoint-number ranges                   exact parity / 31
specialized domain index routes            exact parity / 5
cold subject queries with live map withheld 8 / 8
cold checkpoint queries with live map withheld 7 / 7
source digest                              exact
```

A flat path inventory contains 656 unique routed/index paths but has neither subject membership nor checkpoint-topic range semantics. It therefore cannot deterministically answer the same historical-navigation queries.

## 2. What the evidence candidate preserves

The accepted minimum **semantic content** for the historical routing evidence is:

```text
exact source boundary
exact source SHA-256
legacy subject topic ID
human subject label
short subject description / use-for text
explicit artifact paths per legacy subject
checkpoint-number ranges -> one or more legacy subjects
specialized domain index paths
```

General Knowledge Map maintenance prose, current-state prose and substantive project truth are not part of the historical-routing evidence contract.

## 3. Byte-size observation

The pretty-printed experiment JSON is 82,375 bytes versus 74,887 bytes for the source Markdown, a ratio of 1.100.

This does **not** indicate semantic over-preservation. The JSON repeats field names/indentation and explicit path strings. The same exact candidate object serialized deterministically without pretty whitespace is 71,389 bytes, a ratio of 0.953 to the source map.

Therefore T4 does not freeze pretty-print byte layout as part of the architecture. The contract concerns the minimum routing relations and provenance fields above. Production serialization may normalize repeated paths or use deterministic compact JSON if that materially improves storage/transport without reducing reviewability or meaning.

## 4. Lifecycle contract

Before the live legacy Knowledge Map can be retired, the successor migration process must:

```text
1. bind the final qualified live Knowledge Map to an exact immutable source ref;
2. compute and record the exact source digest;
3. extract the accepted historical-routing evidence shape;
4. verify exact route parity against that final source;
5. persist the evidence under the successor project-knowledge migration-evidence area;
6. only then allow the live compatibility/navigation role to retire.
```

The persisted artifact is classified as:

```text
authority class     evidence
substantive truth   none
purpose             historical / migration navigation
rebuildability      not claimed after the retired legacy source disappears
mutation policy     immutable evidence for that exact legacy boundary
```

If later corrections are needed, they must be explicit successor navigation knowledge or a new evidence version; the original boundary evidence is not silently rewritten.

## 5. Prospective physical home

The frozen future home is:

```text
docs/project_knowledge/migration_evidence/
    legacy_knowledge_map_routing_v1.json
```

This does not turn `docs/project_knowledge/` into a content registry. The artifact belongs there because it is project-knowledge migration infrastructure and evidence about the retired continuity architecture.

The exact production schema/serializer is deferred to the final W5 navigation realization after T1 closes, but it must enforce the semantic content and provenance contract above.

## 6. How successor navigation may use it

Successor navigation may consult this evidence to route into deep legacy history.

It may **not** use the artifact to:

```text
establish current semantic authority
override current natural owners
create current lifecycle state
replace Git/source provenance
pretend that legacy topic membership is the new production subject taxonomy
```

The legacy topic layer and the new semantic-subject layer therefore remain distinguishable even when both participate in one navigation experience.

## 7. Why T4 is sufficient

The experiment tests the exact failure mode identified in MC-0018: losing curated historical routing when the live Knowledge Map retires.

The routing-only evidence preserves all 19 subject structures, all 31 checkpoint range assignments and all five specialized-index routes while cold retrieval operates without the live map. A flat inventory cannot represent those relations.

No additional architecture dialogue is required before the final W5 navigation contract.

## 8. Result

```text
T4=ACCEPTED
HISTORICAL_NAVIGATION_CONTRACT=ROUTING_EVIDENCE
FINAL_PRE_RETIREMENT_PARITY_PROOF=REQUIRED
AUTHORITY_CLASS=EVIDENCE
POST_RETIREMENT_REBUILDABILITY=NOT_CLAIMED
LEGACY_TOPIC_TAXONOMY=HISTORICAL_ONLY
PROSPECTIVE_HOME=docs/project_knowledge/migration_evidence/legacy_knowledge_map_routing_v1.json
FLAT_ARTIFACT_INVENTORY=INSUFFICIENT
LEGACY_KNOWLEDGE_MAP=STILL_LIVE
BROAD_W5_MIGRATION=PAUSED
CURRENT_OPERATIONAL_AUTHORITY=CURRENT_CONTINUITY_ARCHITECTURE
AUTHORITY_SWITCH_ALLOWED=false
NEXT=COMPLETE_T1_INDEPENDENT_CALIBRATION_THEN_FINAL_W5_INFORMATION_ARCHITECTURE_FREEZE
```
