# Research 128: Authority Activation and Temporal/Supersession Deep Dive

**Date:** 2026-09-13
**Status:** D5-D6 EVIDENCE DEEP DIVE COMPLETE / ACTION-SHAPED AUTHORITY RESOLUTION AND TEMPORAL-SEMANTIC CONSTRAINTS ESTABLISHED / TARGET ARCHITECTURE NOT SELECTED
**Scope:** Deepen Research 125 discriminators D5 (authority-aware retrieval and pre-action activation) and D6 (temporal/supersession semantics). Examine mature policy-decision/enforcement systems, pre-action admission controls, attribute-based decision models, temporal database semantics, standards supersession, provenance invalidation/revision and evolving-knowledge models. Establish architecture-neutral constraints for resolving which knowledge governs a concrete action at a concrete time without selecting a rule engine, policy language, graph store, database, metadata schema or target implementation.
**Authority:** Supporting external-evidence research under Research 124. This record constrains later requirements/evidentiary-provenance reconciliation but does not create a new reasoning-control implementation, change current ADS authority, or select the successor architecture.
**Declared references:** `research:124`, `research:125`, `research:126`, `research:127`, `checkpoint:466`, `path:docs/CONTINUITY.md`, `path:docs/DEVELOPMENT_METHOD.md`, `path:docs/local_execution/OPERATIONS.md`

## 1. Questions under investigation

D5 asks:

> **Given an intended project action, how should the architecture resolve and activate the knowledge that governs that action before consequential reasoning or mutation proceeds?**

D6 asks:

> **How should the architecture represent when knowledge applies, when the project learned/recorded it, and how updates, replacements, historical validity and known-wrong material differ?**

They are coupled because a source can be highly relevant yet still be the wrong authority for the current task, scope or time.

The failure to avoid is:

```text
retrieve semantically similar source
    -> assume it governs
        -> ignore action/scope/time/supersession context
            -> reason confidently from stale, partial or conflicting authority
```

The deep dive therefore treats **relevance retrieval** and **authority resolution** as distinct operations.

## 2. Evidence families

The main evidence families are:

```text
NIST SP 800-162 ABAC
    authorization decisions depend on subject, object, requested operation
    and environment attributes evaluated against policy/rules/relationships

OASIS XACML 3.0
    Policy Decision Point / Policy Enforcement Point separation,
    applicability, Permit/Deny/NotApplicable/Indeterminate outcomes,
    explicit policy-combining semantics

Open Policy Agent (OPA)
    decoupled policy decision-making from enforcement,
    policy evaluation against structured runtime context,
    policy distribution and decision logs

Kubernetes Admission Control / ValidatingAdmissionPolicy
    request-specific checks after authentication/authorization but before persistence,
    match conditions, Deny/Warn/Audit actions, Fail/Ignore error policy

Temporal database literature + IBM temporal tables
    valid/business time versus transaction/system time,
    bitemporal representation and historical queries

RFC Editor relationships
    Updates versus Obsoletes, permanent archive plus explicit metadata
    needed to reconstruct current specification/practice

Wikidata evolving-knowledge model
    validity periods + preferred current values + historical normal values
    + deprecated known-wrong/dismissed values

W3C PROV-O
    revision, generation, invalidation and explicit provenance times
```

The security-policy sources are analogies for **decision architecture**, not evidence that project knowledge should be treated as access-control policy or that ADS should adopt their languages.

## 3. NIST ABAC: authority depends on the requested action and context

**Primary source:** NIST SP 800-162, *Guide to Attribute Based Access Control (ABAC) Definition and Considerations*, updated August 2019.

URL: https://csrc.nist.gov/pubs/sp/800/162/upd2/final

NIST defines ABAC as authorization where permission to perform operations is determined by evaluating attributes of the subject, object, requested operation and sometimes environment against policy, rules or relationships.

The important transfer is structural:

```text
who / what actor is involved?
what exact operation is intended?
what object/scope is affected?
what environment/current state matters?
which governing rules are applicable to that request?
```

### Research 124 transfer

The correct governing knowledge for ADS should not be resolved only from a broad topic label such as `development-governance` or semantic similarity to the user's wording. A task such as:

```text
explain current project state
restart Runtime Bridge
change branch protection
publish a scientific conclusion
promote a knowledge artifact
```

may involve overlapping subject matter but different governing sources and consequence classes.

A later candidate should therefore demonstrate **action-shaped authority resolution** using enough task/scope/environment context to distinguish these situations.

### Transfer limit

ABAC answers permission questions. ADS authority resolution additionally asks what evidence/procedure must be read and how reasoning should proceed. The transferable idea is contextual policy applicability, not access-control semantics.

## 4. XACML: decision and enforcement are distinct, and ambiguity is a first-class result

**Primary source:** OASIS, *eXtensible Access Control Markup Language (XACML) Version 3.0*.

URL: https://docs.oasis-open.org/xacml/3.0/xacml-3.0-core-spec-cs02-en.html

XACML separates:

```text
PAP  Policy Administration Point
     creates/manages policies

PDP  Policy Decision Point
     evaluates applicable policies and renders a decision

PEP  Policy Enforcement Point
     requests the decision and enforces it
```

XACML also preserves decision states beyond a simple success path. `NotApplicable` means no applicable rule/policy produced a governing answer. `Indeterminate` represents evaluation/error ambiguity. Its `only-one-applicable` policy-combining algorithm returns `Indeterminate` when more than one policy is applicable where exactly one was expected.

### Research 124 transfer

This provides unusually strong evidence for separating:

```text
knowledge/policy administration
    !=
authority-resolution decision
    !=
enforcement / action gating
```

It also supports fail-visible resolution states such as:

```text
RESOLVED
NO_GOVERNING_AUTHORITY_APPLICABLE
AMBIGUOUS_OR_CONFLICTING_AUTHORITY
REQUIRED_AUTHORITY_UNAVAILABLE_OR_UNREADABLE
```

rather than blending multiple plausible sources into one model-generated answer.

### Combining semantics matter

XACML demonstrates that when several policies apply, the way they combine must itself be governed: deny-overrides, permit-overrides, first-applicable and only-one-applicable produce different results.

For ADS, this means a future authority resolver cannot merely collect all “relevant governing files.” It must know whether sources:

```text
replace one another
supplement one another
have hierarchical scope/precedence
all must be consumed together
or represent an unresolved conflict
```

The exact combining rules remain an ADS design question.

## 5. OPA: policy decision-making can be externalized from the acting component

**Primary source:** Open Policy Agent documentation.

URLs:
- https://www.openpolicyagent.org/docs
- https://www.openpolicyagent.org/docs/deploy

OPA explicitly decouples policy decision-making from enforcement. An application supplies structured context to OPA; OPA evaluates that context against policy/data and returns a decision. OPA deployments can also distribute policy and retain decision logs.

### Transfer

The actor doing substantive work need not be the only place where the rule “remember to inspect the governing source before this action” lives.

This independently supports the Research 124 working concept of project-controlled dispatch/control logic around a transient reasoning model:

```text
intent/task observed
    -> project-controlled authority/activation decision
        -> required sources/obligations returned
            -> acting collaborator consumes them
                -> action proceeds or fails visibly
```

### Transfer limit

A reasoning model still needs to understand source content and perform substantive judgment. OPA-style policy evaluation cannot replace scientific/design reasoning; it only demonstrates a mature separation between policy decision and policy enforcement/application logic.

## 6. Kubernetes admission control: critical checks can sit directly in the pre-action path

**Primary sources:** Kubernetes documentation.

URLs:
- https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers/
- https://kubernetes.io/docs/reference/access-authn-authz/validating-admission-policy/

Kubernetes admission controllers intercept create/delete/modify requests after authentication and authorization but before resource persistence. ValidatingAdmissionPolicy can match specific operations/resources and then Deny, Warn or Audit validation failures. Its `failurePolicy` can be `Fail` or `Ignore`; `Fail` rejects the request when policy evaluation itself errors.

### Research 124 transfer

This strongly supports **situation-specific activation at the action boundary** rather than relying only on cold-start orientation or model memory.

A mature ADS successor should be evaluated on whether consequential actions can expose a bounded pre-action gate such as:

```text
intended action classified
    -> applicable governing-source obligations resolved
        -> required source freshness/availability checked
            -> source consumption evidenced
                -> proceed / warn / refuse / escalate
```

### Consequence-sensitive enforcement

Kubernetes also gives a useful counterweight to universal blocking. Some validation failures can warn or audit instead of deny; policy-evaluation failure can be configured fail-closed or fail-open depending on context.

For ADS, high-consequence authority requirements may need fail-closed behavior, while low-consequence exploratory work may merely surface a warning or reconstruction receipt.

This prevents “activation” from becoming a global system that blocks all reasoning whenever any optional knowledge is unresolved.

## 7. D5: retrieval and authority resolution are different contracts

The cross-domain evidence now supports a sharper distinction:

```text
RELEVANCE RETRIEVAL
    What knowledge is likely useful for understanding this task?

AUTHORITY RESOLUTION
    What knowledge is allowed/required to govern this exact action,
    target, scope, state and time?
```

Relevance retrieval can be probabilistic and recall-oriented. Authority resolution requires governed applicability/precedence semantics and explicit uncertainty.

A semantically similar result may be useful evidence while being:

```text
historical rather than current
supporting rather than governing
superseded
outside the action's scope
valid only under another branch/environment
an update that must be combined with an older base source
an alternative/rejected design
```

This is stronger than a generic “rank authoritative files higher” approach.

## 8. An architecture-neutral authority-resolution request shape

Research 128 does not select a schema, but external evidence now justifies requiring candidates to show how they resolve at least the semantic equivalent of:

```text
action / requested operation
    what is about to be reasoned, recommended or mutated?

target / object / scope
    which repository area, tool, workstream, system or knowledge object?

actor / collaborator context
    which role/capability is acting, where relevant?

current environment/state
    branch, runtime state, lifecycle state, private/public availability,
    consequence class or other governing context

time query
    current authority now, or authority/history at a past/future point?
```

The resolver result should be able to return:

```text
governing source set
resolution status
why those sources apply
how they combine / supersede
required consumption or checks
unresolved conflicts / missing evidence
```

This is a comparison contract, not a selected control-plane API.

## 9. Activation should bind to the concrete intended action

The BL-001 result showed that finding and reading the correct operations runbook did not guarantee that the exact ordered task contract was then followed. D5 therefore needs more than source discovery.

The policy/admission-control evidence suggests a stronger concept:

> **Activation is complete only when governing knowledge is bound to the concrete action contract closely enough that the action can be checked against it.**

For an ordered restart, consuming `OPERATIONS.md` is necessary but the system should also preserve/check the relevant ordered procedure before instructions are emitted.

For a repository mutation, the gate may need expected branch, expected state, allowed action family or validation result.

This remains architecture-neutral and does not imply deterministic automation of every reasoning task.

## 10. Authority resolution needs an explicit uncertainty/failure policy

XACML and Kubernetes both make failure handling part of the policy design rather than an accidental model behavior.

Research 124 should therefore require later candidates to distinguish at least:

```text
no special governing authority exists
    ordinary reasoning may continue under default project rules

required authority exists and resolves cleanly
    activate/consume it, then continue

several apparently governing sources conflict or combine ambiguously
    fail visibly / escalate rather than blend silently

required authority is known but unavailable/stale/unreadable
    fail visibly for consequential work

optional/supporting knowledge is missing
    continue with calibrated uncertainty where allowed
```

A blanket “fail closed on any retrieval miss” would be unnecessarily brittle; a blanket “continue if the model can infer something plausible” would recreate the historical risk.

## 11. Temporal databases: when a fact applies and when it is recorded are separate dimensions

**Primary/established sources:**
- Jensen, Clifford, Elmasri, Gadia, Hayes, Jajodia et al., *A Glossary of Temporal Database Concepts*, SIGMOD Record.
- IBM temporal-data documentation.

URLs:
- https://sigmodrecord.org/
- https://www.ibm.com/docs/en/ida/9.1.1?topic=modeling-temporal-data

Temporal database terminology distinguishes:

```text
VALID / BUSINESS TIME
    when the fact is valid in the modeled world/domain

TRANSACTION / SYSTEM TIME
    when the fact is recorded/known in the database system
```

A bitemporal representation preserves both.

### Research 124 transfer

For some project knowledge, these questions differ:

```text
When did this rule/decision/procedure become applicable?
When did ADS record or learn that it was applicable?
What did the repository believe at an earlier point?
What do we now know was actually applicable at that earlier point?
```

Example:

```text
External procedure changed on 10 September.
ADS learned and recorded the change on 12 September.

"What applies now?"
    needs current applicability.

"What did ADS know on 11 September?"
    needs repository/transaction history.

"What should have governed work performed on 11 September?"
    may need the external/applicability time even though ADS learned it later.
```

This is a real semantic distinction, not merely a timestamp-format issue.

### Transfer limit

Most ADS knowledge may not require full bitemporal modeling. The evidence justifies preserving the distinction where it affects authority, audit or historical reconstruction, not adding two time intervals to every artifact.

## 12. “Current” is not one universal property

The temporal evidence implies several different meanings that prose often collapses:

```text
currently recorded
currently believed/accepted by ADS
currently applicable to the task/domain
currently authoritative after supersession/updates
latest by commit timestamp
latest by artifact publication
```

These are not guaranteed to coincide.

A future architecture should therefore avoid treating “most recent file/commit” as a sufficient authority algorithm.

## 13. RFC Editor: update and replacement are different supersession relations

**Primary sources:** RFC Editor, *What Is an RFC?* and RFC Series conventions.

URLs:
- https://www.rfc-editor.org/series/rfc/
- https://www.rfc-editor.org/rfc/rfc7322.html

Published RFC text is immutable; changes appear in later RFCs. The RFC Series records relationships in metadata:

```text
Updates
    newer RFC makes substantive changes but does not replace the older RFC;
    current understanding may require both

Obsoletes
    newer RFC replaces the older RFC;
    the old RFC remains in the permanent archive but the newer RFC should
    generally be used for current specification/practice
```

### Research 124 transfer

A generic `supersedes` flag can be too weak.

The project may need to distinguish at least the semantics of:

```text
REPLACES / OBSOLETES
    old source remains history but no longer supplies current governing content

UPDATES / SUPPLEMENTS
    old source remains partly governing and must be interpreted with the update

REFINES / SPECIALIZES
    newer source governs only a narrower scope

CORRECTS
    prior statement was wrong rather than merely historical
```

The exact relation vocabulary must remain minimal and earned by real project cases.

### Current-authority traversal

The RFC model also demonstrates why “open the newest document” is insufficient. To understand current specification/practice, a reader may need to follow `Updated By` relationships and distinguish them from `Obsoleted By` relationships.

Later ADS candidates should therefore be tested on graph/relationship traversal for current authority, not chronology alone.

## 14. Wikidata: historical truth is not the same as deprecated/known-wrong knowledge

**Source:** Wikidata, *Help:Evolving knowledge* and *Help:Ranking*.

URLs:
- https://www.wikidata.org/wiki/Help:Evolving_knowledge
- https://www.wikidata.org/wiki/Help:Ranking

Wikidata combines time qualifiers with rank. Historical values can retain normal rank with start/end validity periods, while currently valid values may be preferred. Known mistakes or dismissed beliefs can remain stored but be marked deprecated so they are not normally returned as current answers.

### Research 124 transfer

This provides strong evidence that several states should remain distinct:

```text
historically true / formerly applicable
    not current, but not wrong

superseded/replaced as project authority
    old source remains provenance/history

rejected/known wrong
    preserved to prevent rediscovery, but should not be treated as valid evidence

current preferred/accepted
    default for ordinary current reconstruction
```

A single `historical=true` or `active=false` flag would conflate materially different epistemic meanings.

### Transfer limit

Wikidata ranks are community conventions for an open knowledge base, not ADS governance. The transferable distinction is between historical validity and epistemic deprecation, not its exact rank mechanism.

## 15. PROV-O: revision and invalidation can be explicit provenance events

**Primary source:** W3C, *PROV-O: The PROV Ontology*.

URL: https://www.w3.org/TR/prov-o/

PROV-O includes `wasRevisionOf`, `wasInvalidatedBy`, `generatedAtTime` and `invalidatedAtTime` in addition to derivation/primary-source relations.

### Transfer

If later architecture candidates represent authority transitions explicitly, provenance can record not just that A and B are related, but that a particular entity/version was generated, revised or invalidated at a particular project time.

This can support historical reconstruction without overwriting the old knowledge object.

### Transfer limit

PROV invalidation does not itself define ADS authority, correctness or temporal applicability. It supplies provenance vocabulary, not the governing semantics.

## 16. D6: applicability time, repository knowledge time and authority time should not be silently collapsed

Research 128 now distinguishes three conceptual questions, while deliberately not requiring three stored timelines everywhere:

```text
DOMAIN / APPLICABILITY TIME
    when was the fact/rule/decision actually applicable?

REPOSITORY KNOWLEDGE TIME
    when did ADS record/know this representation?

AUTHORITY TRANSITION TIME
    when did ADS accept/promote/supersede this knowledge as governing project state?
```

Often the latter two will coincide. Sometimes applicability and repository knowledge will coincide as well. The architecture should permit them to diverge when a real case requires it.

This is especially important for:

```text
retroactive corrections
late-discovered external changes
backfilled evidence
historical experiment interpretation
migration/authority switches
private/public synchronization lag
```

No tritemporal database is selected or implied.

## 17. A current-authority answer can be a set, not always one document

RFC `Updates` semantics and policy combining systems both demonstrate that current governing authority may consist of several sources that must be interpreted together.

Therefore later candidates should not assume:

```text
one action -> exactly one governing file
```

The possible result is:

```text
one action
    -> one governing source
or
one action
    -> governing source + mandatory supplements/updates
or
one action
    -> no special source beyond default project rules
or
one action
    -> unresolved conflict / unavailable required authority
```

The project should prefer the smallest governing source set that completely covers the task.

## 18. Temporal and authority semantics interact with derived views

Research 127 established that generated current-state or routing views are derived. D6 adds a further requirement: those views can be structurally fresh while still representing the wrong **applicability/authority state** if their generator does not traverse supersession/update/validity semantics.

A derived “current procedures” index is therefore only correct if its derivation understands what “current” means for those procedures.

This reinforces that freshness is not merely:

```text
built from latest Git commit
```

It is also:

```text
resolved against the authority/temporal semantics required by the view's contract
```

## 19. D5-D6 architecture-neutral constraints

The evidence is strong enough to freeze the following for later requirements reconciliation and candidate comparison:

```text
D5-C1  Relevance retrieval and governing-authority resolution are different contracts.

D5-C2  Authority resolution must be shaped by the concrete intended action, affected scope,
       current environment/state and, when relevant, actor/role and time query.

D5-C3  A governing result may be a source set, not necessarily one artifact, because updates
       and supplements can remain jointly authoritative.

D5-C4  Authority selection/combination semantics must be explicit enough to distinguish
       replacement, supplementation, precedence and unresolved conflict.

D5-C5  No-applicable-authority, ambiguous/conflicting-authority and unavailable-required-
       authority must be representable as distinct fail-visible outcomes.

D5-C6  Consequential action paths must be able to bind resolved governing knowledge to the
       concrete action before execution/advice is finalized; source discovery alone is insufficient.

D5-C7  Enforcement strength should be consequence-sensitive. High-consequence required
       authority may fail closed; low-risk exploratory gaps may warn/audit/continue with uncertainty.

D5-C8  Governing-policy administration, authority decision and action enforcement/consumption
       are separable concerns even if one implementation component performs several roles.

D5-C9  Probabilistic retrieval may nominate candidate sources but may not silently resolve
       consequential authority when deterministic/explicit applicability semantics are available.

D6-C1  Applicability time and repository-recording/knowledge time are conceptually distinct
       and must be representable separately where the distinction affects project reasoning.

D6-C2  Authority-transition time is a distinct project concept from domain applicability;
       a candidate may collapse them only where project semantics make them identical.

D6-C3  Historical/formerly-applicable knowledge must remain distinguishable from rejected,
       erroneous or epistemically deprecated knowledge.

D6-C4  Replacement/obsolescence and supplementation/update are different supersession
       relations and cannot be safely collapsed when current authority depends on the difference.

D6-C5  Current authority cannot be determined from recency alone. Scope, status, temporal
       applicability and supersession/update relations must participate where relevant.

D6-C6  Historical authoritative objects should remain identifiable after they cease to be current;
       current reconstruction may hide them by default without deleting provenance.

D6-C7  Derived current-state/routing views must resolve the temporal/supersession semantics
       promised by their view contract, not merely rebuild from the latest repository revision.

D6-C8  Strong temporal modeling should be selective. Full bitemporal/tritemporal structure
       is justified only for knowledge classes where divergent time dimensions affect authority,
       audit, reconstruction or correction semantics.
```

## 20. Consequence classes become a serious candidate discriminator

D5 evidence suggests that one universal activation behavior is likely wrong.

Later candidates should show a small, governed consequence model capable of distinguishing, for example:

```text
EXPLORATORY / LOW CONSEQUENCE
    broad reasoning may continue despite optional retrieval gaps;
    uncertainty is reported

GOVERNED GUIDANCE
    task-specific governing sources must resolve and be consumed

MUTATING / HIGH CONSEQUENCE
    governing authority + action preconditions must resolve before dispatch

AUTHORITY / SCIENTIFIC PROMOTION
    source evidence, conflict state and acceptance basis must resolve before promotion
```

This is not a frozen four-level taxonomy. It is a requirement that the candidate explain why one failure/enforcement policy is appropriate across heterogeneous tasks.

## 21. D5-D6 thought experiments for later qualification

The evidence suggests concrete tests that later candidates should face.

### 21.1 Similar but non-governing source

A semantic search returns an old operations checkpoint before the current runbook. The candidate must not treat similarity or recency alone as authority.

### 21.2 Update without replacement

Procedure B updates only one step of Procedure A. Current execution requires A + B. A resolver that returns only the newest source fails.

### 21.3 Replacement with preserved history

Specification C obsoletes B. B remains discoverable for historical reconstruction but should not enter ordinary current execution as governing content.

### 21.4 Late-discovered applicability

An external constraint became effective yesterday but was recorded by ADS today. Historical reconstruction must distinguish what actually applied yesterday from what ADS knew yesterday.

### 21.5 Conflicting governing candidates

Two current-looking artifacts both claim authority over the same exact action and no governed precedence resolves them. The candidate must surface ambiguity rather than blend them.

### 21.6 Governing source unavailable

The resolver knows that a required private or operational source exists but cannot access/freshness-check it. Consequential action must stop or escalate according to policy rather than infer from memory.

### 21.7 Source consumed but action contract violated

The right procedure is read, but the generated instructions reorder mandatory steps. The pre-action/response gate must detect that source consumption was not sufficient for action fidelity.

## 22. What D5-D6 still does not select

No decision has been made on:

```text
whether authority rules live in metadata, code, a graph, policy files or generated indexes
whether authority resolution is deterministic code, model-assisted or hybrid
whether action classification is rule-based, model-based or both
which exact consequence classes ADS needs
whether governing-source consumption is proven by receipts, structured extraction or validation
how procedure conformance is checked for free-form model output
whether temporal semantics are stored per entity, relation or event
whether valid/transaction/authority times are explicit fields or derivable from events/Git
which supersession relation vocabulary is minimal but sufficient
whether current-authority closure is precomputed or traversed on demand
```

These remain target-design questions.

## 23. Stop rule and next boundary

D5-D6 now have strong cross-domain convergence around:

```text
action/context-shaped authority applicability
separation of decision from enforcement
pre-action admission/forcing functions
fail-visible ambiguity/unavailability
consequence-sensitive enforcement
distinct applicability and repository-knowledge time
replacement versus update/supplement semantics
historical-valid versus known-wrong distinction
current authority as relationship traversal, not recency
```

Additional broad policy or temporal examples are unlikely to change these conclusions before the final targeted discriminators are researched.

The next paired deep dive is:

```text
D7  consolidation fidelity and provenance
D8  maintenance economics at 5x / 10x scale
```

These should be researched together because stronger consolidation/semantic machinery is only worthwhile if it preserves meaning and remains economical to operate as the repository grows.

After D7-D8, Research 124 should perform the planned requirements/evidentiary-provenance reconciliation before architecture synthesis.

The owner-provided paper/video remains intentionally withheld.

```text
RESEARCH128_D5_D6=COMPLETE
RELEVANCE_RETRIEVAL_NE_AUTHORITY_RESOLUTION=true
AUTHORITY_RESOLUTION_IS_ACTION_CONTEXT_SHAPED=true
PRE_ACTION_ACTIVATION_IS_EVIDENCE_BACKED=true
AMBIGUITY_AND_UNAVAILABILITY_FAIL_VISIBLE=true
TEMPORAL_APPLICABILITY_NE_RECORDING_TIME=true
REPLACEMENT_NE_SUPPLEMENTATION=true
HISTORICAL_VALIDITY_NE_DEPRECATION=true
TARGET_ARCHITECTURE=NOT_SELECTED
NEXT=D7_D8_CONSOLIDATION_FIDELITY_MAINTENANCE_ECONOMICS_DEEP_DIVE
WITHHELD_OWNER_SOURCE=STILL_WITHHELD
```