# Research 127: Capture, Consolidation, Promotion, and Source-Derived State Deep Dive

**Date:** 2026-09-13
**Status:** D3-D4 EVIDENCE DEEP DIVE COMPLETE / LIFECYCLE AND DERIVED-STATE CONSTRAINTS ESTABLISHED / TARGET ARCHITECTURE NOT SELECTED
**Scope:** Deepen Research 125 discriminators D3 (conversation-born capture -> consolidation -> promotion) and D4 (canonical source versus rebuildable derived state). Examine mature archival ingest/dissemination models, provenance standards, preservation-event models, software proposal lifecycles, query/read-model patterns, reproducible-build provenance and modern LLM memory consolidation. Establish architecture-neutral constraints for later candidate comparison without selecting a file family, database, graph, event store, memory product or target lifecycle implementation.
**Authority:** Supporting external-evidence research under Research 124. This record constrains later requirements/evidentiary-provenance reconciliation but does not create a new project-development authority, promote generated synthesis automatically, or select the successor architecture.
**Declared references:** `research:124`, `research:125`, `research:126`, `checkpoint:464`, `checkpoint:465`, `path:docs/DEVELOPMENT_METHOD.md`

## 1. Questions under investigation

D3 and D4 are intentionally researched together.

D3 asks:

> **How can important reasoning born in conversations, investigations, tool work or partial evidence become durable project understanding without forcing every transient thought directly into authoritative project state?**

D4 asks:

> **How can the project derive summaries, indexes, graphs, routing views and task-shaped reconstruction packets from durable knowledge without those convenient outputs becoming an accidental second source of truth?**

The coupled failure to avoid is:

```text
transient reasoning
    -> generated summary
        -> repeatedly reused because convenient
            -> silently treated as authority
                -> source basis / uncertainty / rejected alternatives lost
```

The deep dive therefore focuses on lifecycle roles, promotion boundaries, transformation provenance, rebuildability, freshness and selective retention.

## 2. Evidence families

The evidence set emphasizes mature systems that distinguish input, governed durable state and consumer-facing projections:

```text
OAIS Issue 3 (CCSDS 650.0-M-3, 2024)
    SIP / AIP / DIP roles, ingest quality assurance, preserved package versus dissemination

PREMIS 3.0
    preservation Events, event details/outcomes, linked Objects and Agents,
    selective event recording

W3C PROV-O
    Entity / Activity / Agent, derivation, generation, revision, primary source,
    qualified provenance

Python PEP 1
    idea -> draft -> review/resolution -> accepted/final/rejected/etc.,
    historical rationale versus current formal documentation

IETF RFC 6410 / BCP 9
    maturity progression plus explicit simplification of status levels

Azure Materialized View and CQRS patterns
    source/write model versus read-optimized projections, rebuildability,
    read-only views, staleness and complexity

SLSA provenance
    generated artifact bound to transformation/build type, inputs/dependencies,
    parameters and producing system

Nix reproducible-build practice
    explicit dependencies help reproducibility but hidden nondeterminism remains

DRed / IBIS design-rationale research
    low-friction capture of issues/options/arguments during ongoing work

Generative Agents / MemGPT
    recent LLM evidence for detailed-memory capture, reflection/consolidation,
    retrieval and tiering, without authority guarantees
```

No single source is treated as an ADS design template. The significance lies in cross-domain convergence and counterexamples.

## 3. OAIS provides a powerful three-role separation

**Primary source:** CCSDS 650.0-M-3, *Reference Model for an Open Archival Information System (OAIS)*, Issue 3, December 2024.

URL: https://ccsds.org/Pubs/650x0m3.pdf

OAIS distinguishes three Information Package roles:

```text
SIP  Submission Information Package
     information submitted by a Producer for ingest

AIP  Archival Information Package
     information prepared to satisfy the archive's long-term preservation obligations

DIP  Dissemination Information Package
     all or part of preserved information delivered for a Consumer's request
```

The distinction is functional rather than cosmetic. OAIS states that the three package types have different information requirements. A SIP may be partial; several SIPs may be needed. The ingest process performs quality assurance and transforms one or more SIPs into one or more AIPs conforming to archive data/documentation standards. The AIP has more stringent preservation-information requirements. A DIP may contain all or part of an AIP, or collections of AIPs, shaped to consumer requirements.

### Transfer to Research 124

The strongest transfer is not the package format. It is the **role separation**:

```text
captured / submitted material
    need not already satisfy durable-authority requirements

governed durable knowledge
    may require stronger completeness, context, provenance and validation

consumer / reconstruction representation
    may be task-shaped, partial or transformed without becoming the source
```

For conversation-born project knowledge this suggests that “worth capturing,” “worthy of durable authoritative preservation,” and “useful to present in this task context” are three different judgments.

### Transfer limit

OAIS is an archival reference model, not a software-project governance model. An ADS knowledge lifecycle should not inherit archival package names, storage assumptions or preservation bureaucracy merely because the separation is useful.

## 4. Ingest can transform and validate rather than merely copy

OAIS's Generate AIP function transforms submissions into preservation packages that satisfy the archive's standards. The process can reorganize content, gather additional representation information and produce descriptive information. It can also send material for audit and request more information if necessary.

This provides an important counterexample to a naive capture model:

```text
conversation transcript
    -> copied verbatim into permanent knowledge
```

Durable preservation may instead involve **controlled transformation** provided that the transformation preserves the intended information and provenance.

For ADS, plausible transformations include distillation, classification, relationship declaration, explicit uncertainty, conflict identification or promotion into a stronger knowledge unit. Research 127 does not decide which are automated or model-assisted.

The crucial constraint is that transformation must not erase the ability to reconstruct where the durable knowledge came from.

## 5. PREMIS: transformations deserve event provenance, but not every action deserves an event object

**Primary source:** Library of Congress, *PREMIS Data Dictionary for Preservation Metadata, Version 3.0*.

URLs:
- https://www.loc.gov/standards/premis/v3/
- https://www.loc.gov/standards/premis/v3/premis-3-0-datadictionary-only.pdf

PREMIS's Event entity records an action involving one or more Objects. Event metadata includes identifier, type, date/time, optional event details, optional outcome information, linked Agents and linked Objects. PREMIS explicitly states that actions modifying objects should always be recorded, while less consequential actions may remain in logs/audit trails rather than becoming first-class Event entities.

### Transfer

A knowledge architecture should be able to record consequential transformations such as:

```text
capture accepted for durable processing
consolidation / synthesis
human or model review
promotion to authority
supersession
migration
regeneration of a derived representation
repair after detected drift
```

But it does not follow that every retrieval, read, summarization attempt or chat message deserves a permanent lifecycle event. Event granularity should track preservation/authority significance.

This is valuable for D3 because it supports **selective lifecycle provenance** rather than complete operational telemetry as project knowledge.

## 6. W3C PROV-O: derived knowledge should point through the transformation to its sources

**Primary source:** W3C, *PROV-O: The PROV Ontology*.

URL: https://www.w3.org/TR/prov-o/

PROV-O distinguishes Entity, Activity and Agent and supplies relations such as:

```text
wasGeneratedBy
wasDerivedFrom
used
wasAttributedTo
wasRevisionOf
hadPrimarySource
```

PROV's qualified relations can add detail about the derivation activity, usage and generation instead of representing provenance only as a simple source-to-output edge.

### Transfer

A generated ADS synthesis should be able, where required, to answer:

```text
which durable source entities were used?
which transformation/activity produced this output?
which model/tool/human agent materially participated?
which version/configuration of the transformation mattered?
is this a derivation, revision, quotation or promoted human/model synthesis?
```

The exact schema remains open. The evidence establishes only that **source lineage and transformation lineage are separable first-class concerns**.

## 7. SLSA adds a practical provenance envelope for generated artifacts

**Primary source:** SLSA, *Provenance* and *Build Provenance*, current approved specification.

URLs:
- https://slsa.dev/spec/v1.2/provenance
- https://slsa.dev/spec/v1.2/build-provenance

SLSA provenance describes where, when and how an artifact was produced. Build provenance identifies the producing builder/platform, a build type, external parameters and resolved dependencies/inputs.

### Transfer

For a deterministic generated knowledge view, a useful analogous provenance envelope may need to bind:

```text
output identity
source identities + exact source revisions
transformation type/version
material parameters/configuration
producing tool/runtime identity
execution time / generation boundary
```

For an LLM-derived synthesis, additional inputs that materially affect semantics may include model identity/version, prompt/template version and declared human review/promotion outcome.

This is not a requirement to implement SLSA or in-toto. It is evidence that “generated from repository state” is too weak a provenance claim when the exact generator and inputs affect trust.

## 8. Nix: explicit inputs are necessary but do not eliminate nondeterminism

**Primary source:** NixOS, *Reproducible Builds*.

URL: https://reproducible.nixos.org/

Nix derivations have deterministic references to dependencies and use sandboxing, but Nix explicitly notes that timestamps and other nondeterministic inputs can still prevent bit-for-bit reproduction.

### Transfer

Research 124 should distinguish at least two meanings of rebuildability:

```text
structural/deterministic derived state
    same source revision + same generator/config
    should normally regenerate equivalent or exact machine structure

probabilistic semantic synthesis
    exact byte reproduction may be unrealistic
    but all source inputs, transformation/model context and promotion basis
    must be recoverable enough to audit or regenerate a fresh candidate
```

A derived state whose output depends materially on hidden conversation context, unrecorded prompts, unavailable model state or unknown external data is not strongly rebuildable merely because a script can be run again.

## 9. Materialized View: derived read state can be explicitly disposable

**Primary source:** Microsoft Azure Architecture Center, *Materialized View pattern*.

URL: https://learn.microsoft.com/en-us/azure/architecture/patterns/materialized-view

The pattern precomputes query-shaped representations over source data. Microsoft states that a materialized view is completely disposable because it can be rebuilt from source stores, and that applications do not update it directly. The guidance also emphasizes that views can become inconsistent with changing source data and therefore need update/regeneration policy.

### Transfer

This supplies a strong D4 discriminator:

```text
derived reconstruction/index/view state
    should normally be read-only from the perspective of project truth
    should be disposable if all unique truth lives elsewhere
    should expose freshness/source binding
    should have a defined regeneration path
```

If a human or model discovers unique valuable understanding while using a derived view, that new understanding must cross an explicit promotion/capture boundary rather than being written back into the view as hidden authority.

## 10. CQRS: write authority and read projections can be separate models

**Primary source:** Microsoft Azure Architecture Center, *CQRS pattern*.

URL: https://learn.microsoft.com/en-us/azure/architecture/patterns/cqrs

CQRS separates command/write and query/read models. Read models may use materialized views optimized for retrieval. When combined with event sourcing, the event store can be the single source of truth and read views can be regenerated. The same guidance explicitly warns about eventual consistency, view-generation cost and increased complexity.

### Transfer

The useful architecture question is:

> **Should authority-bearing project mutations and reconstruction/read views have different interfaces and contracts even if they share underlying data?**

This does not require CQRS. It strengthens the principle that a search index, graph projection or context packet should not automatically expose mutation semantics merely because it is convenient to query.

## 11. Software proposal processes separate discussion, draft, acceptance and current formal documentation

### 11.1 Python PEP 1

**Primary source:** Python, *PEP 1 - PEP Purpose and Guidelines*.

URL: https://peps.python.org/pep-0001/

PEPs are used to propose significant changes, collect input and document design decisions. An idea begins in discussion before becoming a draft PEP. A PEP can move through Draft, Accepted, Provisional, Deferred, Rejected, Withdrawn, Final or Superseded states. Rejected ideas are deliberately recorded with rationale. After resolution, most PEPs become historical design records rather than the living formal documentation of expected behavior, which is maintained elsewhere.

### Transfer

This is strong evidence for several D3 distinctions:

```text
discussed idea                 != formal proposal
formal proposal                != accepted project knowledge
accepted design                != implemented/final state
resolved rationale/history     != current operational specification
rejected knowledge             may remain valuable provenance
```

The same record can remain durable after it ceases to be current authority.

### 11.2 IETF BCP 9 / RFC 6410 is a counterweight against status proliferation

**Primary source:** RFC 6410, *Reducing the Standards Track to Two Maturity Levels*.

URL: https://www.rfc-editor.org/info/rfc6410/

The IETF deliberately reduced the standards-track maturity ladder because advancement through the prior levels had become difficult. It preserved the important benefits of maturity progression while simplifying the mechanism.

### Transfer

If ADS introduces capture/promotion states, the lifecycle should use the **smallest number of semantically necessary states**. Rich lifecycle semantics do not justify a large status taxonomy by default.

## 12. Design-rationale research: capture must stay near the work and low-friction

**Source:** Bracewell, Wallace, Moss and Knott, *Capturing design rationale*, Computer-Aided Design 41(3), 2009.

DOI: https://doi.org/10.1016/j.cad.2008.10.005

DRed is described as a simple and unobtrusive tool for recording issues, options and supporting/opposing arguments while design proceeds. It was developed and tested with a large aerospace organization.

### Transfer

Conversation-born insight will be lost if durable capture requires the collaborator or project owner to stop substantive work and manually author a heavyweight canonical artifact for every useful thought.

However, “low-friction capture” is not equivalent to “automatic authority.” The evidence supports a lightweight intake/candidate mechanism followed by stronger consolidation/promotion gates where warranted.

## 13. Modern LLM memory shows consolidation utility but not governance safety

### 13.1 Generative Agents

**Source:** Park et al., *Generative Agents: Interactive Simulacra of Human Behavior*, UIST 2023.

URL: https://research.google/pubs/generative-agents-interactive-simulacra-of-human-behavior/

The architecture stores a natural-language record of experiences, synthesizes those memories into higher-level reflections over time and retrieves relevant memories for planning.

### 13.2 MemGPT

**Source:** Packer et al., *MemGPT: Towards LLMs as Operating Systems*.

URL: https://arxiv.org/abs/2310.08560

MemGPT manages multiple memory tiers to move information between limited active context and larger external memory.

### Transfer

These systems support the feasibility of:

```text
detailed/episodic capture
    -> higher-level consolidation
        -> selective later activation
```

But neither supplies the project-governance semantics required here. An LLM reflection can be useful while still being wrong, incomplete, stale or unsupported. Therefore generated reflection is best treated as **candidate/derived understanding until separately promoted**.

## 14. The central D3-D4 lifecycle distinction

Cross-disciplinary convergence now supports an architecture-neutral four-role model:

```text
1. INTAKE / CAPTURE
   potentially incomplete observations, dialogue, evidence or reasoning
   worth retaining long enough for evaluation

2. CONSOLIDATED CANDIDATE
   transformed/distilled understanding with source lineage
   useful for review but not automatically current authority

3. PROMOTED DURABLE KNOWLEDGE
   explicitly accepted knowledge whose authority/status is governed
   and whose provenance remains traversable

4. DERIVED CONSUMPTION VIEW
   task-shaped summary/index/graph/context packet generated from durable sources
   optimized for retrieval/reconstruction, normally not a write authority
```

These are **semantic roles for later candidate comparison**, not selected artifact families, database tables or mandatory persistent states.

One candidate may collapse roles 1 and 2 for simple knowledge. Another may generate role 4 dynamically. The architecture must preserve the distinctions when conflating them would create authority or provenance ambiguity.

## 15. Promotion is an authority transition, not just a copy operation

OAIS ingest, PEP resolution and PREMIS event provenance independently support the idea that durable promotion can involve validation, transformation, completion and explicit status change.

For Research 124, a meaningful promotion should be able to establish at least:

```text
what is being promoted
from which source/candidate basis
who or what is authorized to promote it
what authority / epistemic status results
what important uncertainty remains
what prior knowledge it supersedes or complements
where the source/provenance trail remains available
```

The exact level of automation remains open. A project-owner decision, bounded model-assisted reconciliation, deterministic validator or combination may play roles depending on knowledge class and consequence.

## 16. Promotion should be selective

Neither PEP practice nor PREMIS treats every observed action as a high-level governed artifact. PEP 1 explicitly says ordinary enhancements/bug fixes do not need a PEP. PREMIS allows less important actions to remain in logs rather than first-class Events.

This provides a useful anti-explosion principle:

> **Durable capture may be broader than durable promotion, and durable promotion should be proportional to the knowledge's future value, authority significance, uniqueness and reconstruction need.**

The evidence does not justify storing every model token, every intermediate thought or every retrieval result forever.

## 17. Rejected and superseded knowledge should remain durable when it prevents rediscovery

PEP 1 explicitly preserves rejected ideas and their rationale so future participants do not repeat already-settled discussions. This aligns with Research 124's requirement to distinguish rejected, superseded and historical knowledge from current authority.

The lifecycle therefore should not equate:

```text
not promoted / no longer current
    ==
worthless / deletable
```

The correct retention depth is still a design and maintenance-economics question.

## 18. Derived views need freshness semantics

Materialized View and CQRS guidance make stale read models a normal systems concern. A project-derived index or reconstruction packet can be structurally valid yet semantically stale relative to changed sources.

Later candidates should therefore demonstrate how a derived representation exposes or enables determination of:

```text
source revision boundary
transformation/generator identity
creation/refreshed time or generation identity
staleness / freshness status
rebuild/refresh trigger
failure behavior when freshness cannot be established
```

Freshness need not mean “rebuild on every commit.” The acceptable lag depends on the view's use and authority risk.

## 19. Rebuildability has levels

Research 127 refines KA-R21's generic rebuildable-derived-state requirement into three comparison classes:

```text
R0  SOURCE-BOUND
    source identities and transformation provenance are known,
    but repeat generation is not promised

R1  REGENERABLE
    the same authoritative inputs and versioned transformation can generate
    a fresh semantically equivalent derived representation

R2  DETERMINISTICALLY REPRODUCIBLE
    the same authoritative inputs and transformation are expected to produce
    the same machine-significant result, subject to declared normalization
```

These are candidate-evaluation classes, not frozen implementation labels.

Structural indexes, manifests and routing projections should usually aspire to R2. LLM-generated synthesis may realistically qualify only for R1 unless the model/runtime is fully pinned and deterministic, and even then semantic review may matter more than byte identity.

R0 may be acceptable for disposable exploratory outputs but is weak for any view that materially affects routine reconstruction.

## 20. Promotion of derived insight must create authoritative state deliberately

A derived view can expose a genuinely new conclusion not yet present in source knowledge. For example, an LLM may synthesize several research records and identify a novel architecture principle.

The safe transition is not:

```text
generated summary happens to contain useful new insight
    -> summary cache silently becomes source truth
```

It is:

```text
generated/derived insight
    -> captured as candidate with provenance
        -> reviewed / validated proportionately
            -> explicitly promoted onto the authoritative knowledge substrate
                -> future views derive from the promoted knowledge
```

This preserves the distinction between **discovery through derivation** and **authority through promotion**.

## 21. Read views should not be ordinary mutation surfaces

Materialized View and CQRS patterns provide mature precedent for separating query-optimized projections from the write model.

Research 124 should therefore compare candidates where reconstruction/search/graph/context views are read-only by default. Mutations discovered through those interfaces can be routed to the authoritative knowledge-management path rather than directly editing a generated view.

This is a candidate discriminator, not a requirement to use separate databases.

## 22. Derived-state loss should be survivable

A strong D4 design must pass this thought experiment:

```text
delete the semantic index / vector database / generated graph /
materialized current-state view / reconstruction cache

Can the project rebuild enough of it from durable authoritative state
without losing unique accepted project understanding?
```

If the answer is no because unique accepted knowledge exists only in the derived store, the store is no longer merely derived. It either needs promotion into explicit authority or must be governed as an authoritative source itself.

This is the operational meaning of “no accidental second source of truth.”

## 23. Hidden-context derivation is a special risk for LLM-generated views

Traditional build/view systems often know their source inputs. LLM outputs can be influenced by:

```text
prior conversation state
system/developer instructions
model version
retrieval ordering
prompt/template version
sampling/runtime behavior
connected/private context
unrecorded tool results
```

Not all of these need permanent preservation for every low-risk summary. But a derived view cannot claim strong regeneration/audit properties if material hidden inputs are unknown.

Candidate architectures should therefore define **provenance sufficiency by consequence class** rather than pretending all generated text is equally reproducible.

## 24. Consolidation quality remains a separate problem

D3-D4 answers how consolidation should relate to authority and source lineage; it does not prove that a consolidation is semantically faithful.

A synthesis can be perfectly traceable and still omit a crucial exception or flatten uncertainty. Research 124 therefore correctly keeps D7, consolidation fidelity and provenance, as a later deep dive.

Similarly, an architecturally clean lifecycle can still be too expensive to maintain. D8 remains necessary.

## 25. D3-D4 architecture-neutral conclusions

The evidence is strong enough to freeze the following for later reconciliation and candidate comparison:

```text
D3-C1  Captured material must not automatically inherit project authority.

D3-C2  Capture, consolidation, validation/review and authority promotion are
       distinguishable lifecycle functions even if a candidate sometimes collapses them.

D3-C3  Promotion of unique durable understanding must be explicit, source-traceable
       and proportional to consequence.

D3-C4  Capture should remain low-friction enough to occur during real work; heavyweight
       canonical authoring cannot be the only intake path for important reasoning.

D3-C5  Rejected, deferred and superseded reasoning may remain durable when its rationale
       prevents rediscovery or explains current state, without remaining current authority.

D3-C6  Lifecycle status vocabularies should be minimal; every additional promotion state
       must earn its operational value.

D3-C7  Full indefinite capture of every message/token/intermediate result is not justified
       by the current evidence. Retention depth should be proportional to uniqueness,
       authority significance, audit value and future reconstruction need.

D4-C1  Query/reconstruction/index views should normally be treated as derived read state,
       not ordinary write-authority surfaces.

D4-C2  Derived state that matters to reconstruction must have sufficient source binding,
       transformation identity and freshness information to detect staleness and enable repair.

D4-C3  Loss of a genuinely derived store must not destroy unique accepted project truth.

D4-C4  Structural derived state should normally be deterministically reproducible where
       practical; probabilistic semantic synthesis may instead require provenance-complete
       regeneration plus semantic review rather than byte identity.

D4-C5  If generated insight becomes unique accepted project knowledge, it must cross an
       explicit promotion boundary onto an authoritative durable surface.

D4-C6  Task-shaped consumer/reconstruction representations may select, summarize or
       reorganize authoritative knowledge without becoming the authority they represent.

D4-C7  Hidden material inputs weaken rebuildability. Provenance sufficiency must scale with
       the consequence of relying on the generated representation.

D4-C8  Freshness/lag is an explicit property of derived views; inability to establish required
       freshness must fail visibly for uses whose correctness depends on current state.
```

## 26. What D3-D4 still does not select

No decision has been made on:

```text
whether raw conversation capture is automatic, model-triggered or explicit
how long unpromoted candidate capture is retained
whether capture lives in Git, a database, conversation export or another substrate
whether consolidation is incremental, batch, event-driven or checkpoint-triggered
which promotion decisions require the project owner
whether source truth is event-oriented or state-oriented
whether derived views use SQL, static generation, search indexes, graphs or vectors
whether provenance records are embedded with sources or stored as separate relations/events
exact freshness thresholds
exact model/prompt provenance required for each generated output class
```

Those are later candidate-design and qualification questions.

## 27. Stop rule and next boundary

The D3-D4 evidence now has strong cross-domain convergence:

```text
input/capture != preserved authoritative knowledge != consumer projection
proposal != accepted authority
transformation requires provenance when it matters
read views can be disposable and rebuildable
probabilistic synthesis can aid consolidation without becoming authority
promotion and retention must be selective
```

Additional broad examples are unlikely to materially alter these conclusions before the remaining discriminators are researched.

The next deep dive should move to:

```text
D5  authority-aware retrieval and pre-action activation
D6  temporal / supersession semantics
```

These should be paired because authority resolution depends on current-versus-historical applicability, supersession and temporal validity.

D7 consolidation fidelity/provenance and D8 maintenance economics remain after that.

The owner-provided paper/video remains intentionally withheld.

```text
RESEARCH127_D3_D4=COMPLETE
CAPTURE_DOES_NOT_IMPLY_AUTHORITY=true
PROMOTION_IS_EXPLICIT_AUTHORITY_TRANSITION=true
DERIVED_VIEWS_DEFAULT_TO_READ_ONLY_DISPOSABLE=true
DERIVED_UNIQUE_TRUTH=NOT_ALLOWED_WITHOUT_PROMOTION
REBUILDABILITY_LEVELS=REFINED_FOR_COMPARISON
TARGET_ARCHITECTURE=NOT_SELECTED
NEXT=D5_D6_AUTHORITY_ACTIVATION_TEMPORAL_SUPERSESSION_DEEP_DIVE
WITHHELD_OWNER_SOURCE=STILL_WITHHELD
```