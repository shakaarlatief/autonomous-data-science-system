# Research 125: Cross-Disciplinary External Evidence for Project Knowledge Architecture

**Date:** 2026-09-13
**Status:** PHASE-1 CROSS-DISCIPLINARY EVIDENCE ESTABLISHED / TARGETED EVIDENCE DEEP DIVES NEXT / TARGET ARCHITECTURE NOT SELECTED
**Scope:** Build an independent external evidence field for Research 124 by examining information science, digital preservation, organizational memory, design rationale, human factors, software architecture, reproducible derived state, temporal data, and modern LLM memory/retrieval research. The goal is to expand the project-development knowledge-architecture design space rather than search for one ready-made solution.
**Authority:** Supporting evidence research under Research 124. This record does not select the target architecture, does not replace current project-development knowledge authority, and does not make external frameworks authoritative over ADS.
**Declared references:** `research:124`, `checkpoint:463`, `foundation:014`, `path:docs/KNOWLEDGE_MAP.md`, `path:docs/DEVELOPMENT_METHOD.md`

## 1. Why this research exists

Research 124 has now completed its internal failure corpus, historical ChatGPT baseline, and owner clarification that the redesign is a whole-architecture inquiry rather than a defect-patching exercise.

The next question is not:

```text
which external product looks most like our current repository?
```

It is:

> **What mature ideas from multiple disciplines should change how we think about durable project understanding, semantic organization, provenance, consolidation, activation, temporal truth, derived views, and task-shaped reconstruction?**

The evidence search therefore deliberately spans both AI and non-AI fields. At least one major evidence stream had to come from disciplines that solved long-lived knowledge, records, safety, or architecture-description problems before current LLM systems existed.

## 2. Evidence discipline

Every source below is treated as an analogy or transferable design principle only to the extent justified by its original domain.

```text
external framework observed
    !=
ADS successor architecture selected

useful vocabulary or mechanism
    !=
requirement to adopt its implementation technology

empirical result in another domain
    !=
direct proof for LLM project-development behavior
```

The research distinguishes:

```text
PRIMARY STANDARD / OFFICIAL MODEL
    normative or institutional reference material

PEER-REVIEWED RESEARCH
    empirical or conceptual work published in established venues

OFFICIAL ENGINEERING GUIDANCE
    practitioner architecture guidance from a responsible platform/vendor

RECENT AI RESEARCH
    relevant modern memory/retrieval work whose authority and stability are weaker than mature standards
```

## 3. Knowledge identity, semantic organization, and multiple views

### 3.1 W3C SKOS: concepts can have identity independent of labels

**Source:** W3C, *SKOS Simple Knowledge Organization System Reference*.

URL: https://www.w3.org/TR/skos-reference/

**Evidence class:** PRIMARY STANDARD / W3C Recommendation.

SKOS defines a `Concept` as an idea or notion, a unit of thought. Concepts can have preferred, alternative, and hidden labels, while semantic relationships such as broader, narrower, and related connect concepts independently of any one textual label.

**Plausible transfer to Research 124:** Important project knowledge may benefit from identity that is not identical to the filename or current title of the artifact containing it. The same durable concept can plausibly survive renaming, representation change, or multiple views while preserving a stable semantic identity.

**Transfer limit:** This does not imply that ADS should use RDF, SKOS, or a formal ontology. SKOS is evidence for separating conceptual identity from labels and for explicit semantic relations, not a target implementation decision.

### 3.2 IFLA Library Reference Model: organize information around user tasks and relationships

**Source:** IFLA, *IFLA Library Reference Model*, current repository edition surfaced in 2024.

URL: https://repository.ifla.org/rest/api/core/bitstreams/7d23aa55-1f85-490f-b500-6170285585a6/content

**Evidence class:** PRIMARY DOMAIN REFERENCE MODEL.

IFLA LRM distinguishes user tasks including Find, Identify, Select, Obtain, and Explore. Explore is explicitly relationship-driven and contextual: users may browse, make unexpected connections, and become familiar with a collection for future use.

**Plausible transfer:** Project-knowledge architecture should be evaluated by the different tasks collaborators perform, not by whether one structure is elegant in isolation. Broad orientation, exact evidence retrieval, authority resolution, historical reconstruction, and exploratory discovery are different task classes and may deserve different routes or views.

**Transfer limit:** Bibliographic entities and library users are not project-development knowledge. LRM contributes task-centered modeling and relationship-aware exploration, not a project ontology to copy.

### 3.3 Flamenco: faceted navigation allows several organizational axes at once

**Source:** UC Berkeley, *Flamenco Search Interface Project*.

URL: https://flamenco.berkeley.edu/

**Evidence class:** RESEARCH SYSTEM / INFORMATION RETRIEVAL AND HCI.

Flamenco combines hierarchical faceted metadata with free-text search so users can refine and expand queries while maintaining context in a large information space.

**Plausible transfer:** The successor should not assume that one hierarchy must simultaneously carry subject, chronology, authority, workstream, evidence depth, and artifact type. Multiple orthogonal facets may be more robust than forcing every knowledge item into one tree.

**Transfer limit:** Flamenco is primarily a navigation/interface result. It does not solve project authority, provenance, supersession, or required-source activation.

### 3.4 Furnas et al.: vocabulary mismatch is fundamental

**Source:** Furnas, Landauer, Gomez, and Dumais, *The Vocabulary Problem in Human-System Communication*, Communications of the ACM, 1987.

DOI: https://doi.org/10.1145/32206.32212

**Evidence class:** PEER-REVIEWED CLASSIC HCI/IR RESEARCH.

The study found surprisingly large variability in spontaneous word choice for the same targets. Systems that require users to guess one exact term are therefore fragile.

**Plausible transfer:** Exact filenames, one canonical subject label, or a single controlled vocabulary should not be the only route to project knowledge. Aliases, lexical search, semantic relationships, structured metadata, and possibly embeddings can complement one another.

**Transfer limit:** Human naming variability is not the same as LLM retrieval behavior. The result supports multiple lexical access paths, not any specific retrieval stack.

### 3.5 ISO/IEC/IEEE 42010 and SEI Views & Beyond: one underlying thing can require multiple concern-shaped views

**Sources:**
- ISO/IEC/IEEE 42010:2022, *Software, systems and enterprise - Architecture description*. https://www.iso.org/standard/74393.html
- Software Engineering Institute, *Views and Beyond Collection*. https://www.sei.cmu.edu/library/views-and-beyond-collection/

**Evidence class:** INTERNATIONAL STANDARD + ESTABLISHED SOFTWARE-ARCHITECTURE GUIDANCE.

ISO 42010 distinguishes an architecture from its architecture description and formalizes viewpoints/model kinds used to address different concerns. SEI's Views & Beyond treats views as a fundamental organization principle and emphasizes choosing relevant views based on anticipated use.

**Plausible transfer:** A project-knowledge substrate may support several task-shaped projections rather than one monolithic universal document. A current-state view, semantic-domain view, provenance view, workstream view, and evidence view could all be projections over overlapping underlying knowledge.

**Transfer limit:** Architecture-description practice concerns documenting software/system architectures, not maintaining all project-development knowledge. The transferable principle is concern-shaped representation, not its exact documentation templates.

## 4. Provenance, preservation, and future interpretability

### 4.1 W3C PROV-O: provenance is a relationship model, not a footnote

**Source:** W3C, *PROV-O: The PROV Ontology*.

URL: https://www.w3.org/TR/prov-o/

**Evidence class:** PRIMARY STANDARD / W3C Recommendation.

PROV-O models Entity, Activity, and Agent plus explicit relationships such as `wasGeneratedBy`, `wasDerivedFrom`, `used`, `wasAttributedTo`, `wasRevisionOf`, and `hadPrimarySource`.

**Plausible transfer:** Research 124 should consider provenance, derivation, revision, responsibility, and primary-source relationships as first-class machine-readable relations rather than relying only on narrative references between files.

**Transfer limit:** PROV-O does not define ADS authority levels, promotion rules, task routing, or canonical-source policy. It supplies vocabulary and a modeling precedent.

### 4.2 OAIS: preserving bytes is not preserving meaning

**Source:** CCSDS 650.0-M-3, *Reference Model for an Open Archival Information System (OAIS)*, Issue 3, December 2024.

URL: https://ccsds.org/Pubs/650x0m3.pdf

**Evidence class:** PRIMARY INTERNATIONAL PRESERVATION REFERENCE MODEL.

OAIS distinguishes a content object from the Representation Information required to make it understandable. Representation Information can include structural, semantic, software, algorithmic, and instructional material. OAIS also requires Preservation Description Information around reference, context, provenance, fixity, and access rights. Separately, Descriptive Information can act as an index/access aid and is generally derived from deeper preserved information.

**Plausible transfer:** Durable project knowledge must preserve enough context and semantics for a future collaborator to interpret it, not merely keep Markdown bytes alive. The separation between deeply preserved information and derived descriptive access aids is especially relevant to source-authoritative plus rebuildable-view designs.

**Transfer limit:** OAIS is designed for long-term archival preservation, not an actively changing software/research project. Its categories should inform requirements, not be imported wholesale.

### 4.3 PREMIS: preservation events and responsibility can be explicit

**Source:** Library of Congress, *PREMIS Data Dictionary for Preservation Metadata, Version 3.0*.

URL: https://www.loc.gov/standards/premis/v3/

**Evidence class:** PRIMARY PRESERVATION METADATA STANDARD.

PREMIS models Objects, Events, Rights, and Agents, including identifiers, event outcomes, links between events and objects, and agent roles. Version 3 also supports intellectual-entity-level representation within the object model.

**Plausible transfer:** Important transformations of project knowledge, such as consolidation, migration, promotion, supersession, regeneration, or repair, could have explicit event/provenance records instead of being inferable only from Git diffs or prose.

**Transfer limit:** PREMIS optimizes preservation metadata, not active reasoning or project navigation.

### 4.4 Records Continuum: current use and preservation need not be separate life phases

**Sources:**
- Society of American Archivists, *records continuum*. https://dictionary.archivists.org/entry/records-continuum.html
- Frings-Hessami, Archival Science work on the Records Continuum Model and its Create, Capture, Organise, Pluralise dimensions.

**Evidence class:** ESTABLISHED ARCHIVAL THEORY / PEER-REVIEWED SYNTHESIS.

The records-continuum perspective treats creation, capture, organization, and broader reuse as overlapping dimensions rather than a simple linear transition from active record to archive.

**Plausible transfer:** Project history does not need to become semantically dead once immediate work closes. Knowledge can simultaneously serve current work, provenance, accountability, and later reinterpretation. Preservation requirements can be designed at capture time rather than added only after work finishes.

**Transfer limit:** This is archival/recordkeeping theory. It should widen our reasoning about lifecycle and reuse, not prescribe repository mechanics.

## 5. Organizational memory and conversation-born rationale

### 5.1 Ackerman and Halverson: organizational memory is both object and process

**Source:** Ackerman and Halverson, *Considering an Organization's Memory*, CSCW 1998.

URL: https://web.eecs.umich.edu/~ackerm/pub/98b24/cscw98.om.html

**Evidence class:** PEER-REVIEWED CSCW RESEARCH.

Their ethnographic analysis argues that organizational memory is better understood through both stored artifacts and the work processes through which memory is created, interpreted, and used.

**Plausible transfer:** Research 124 should avoid reducing project memory to a storage repository. Capture, consolidation, routing, activation, interpretation, and escalation are part of the memory architecture.

**Transfer limit:** Organizational work groups differ from LLM-mediated software projects, but the object-plus-process distinction transfers cleanly at the conceptual level.

### 5.2 Answer Garden: stored knowledge can escalate to a knowledgeable actor

**Source:** Ackerman and Malone, *Answer Garden: A Tool for Growing Organizational Memory*, ACM COIS 1990, plus later field-study work.

DOI: https://doi.org/10.1145/91474.91485

**Evidence class:** PEER-REVIEWED CSCW / ORGANIZATIONAL MEMORY.

Answer Garden combined retrieval of recorded answers with routing to people when the repository could not answer the question.

**Plausible transfer:** Fail-visible escalation is a legitimate memory-system behavior. The project-development knowledge architecture should be allowed to say that required knowledge is absent, ambiguous, or needs owner/domain input rather than forcing every gap through probabilistic synthesis.

**Transfer limit:** Human expert routing is not identical to ADS escalation. The useful idea is graceful escalation when memory is incomplete.

### 5.3 Design-rationale research: capture reasoning with low disruption

**Sources:**
- Conklin and Yakemovic, *A Process-Oriented Approach to Design Rationale*, Human-Computer Interaction 6, 1991. https://doi.org/10.1080/07370024.1991.9667172
- Bracewell, Wallace, Moss, and Knott, *Capturing design rationale*, Computer-Aided Design 41(3), 2009. https://doi.org/10.1016/j.cad.2008.10.005

**Evidence class:** PEER-REVIEWED DESIGN-RATIONALE RESEARCH.

IBIS-style work captures issues, options, arguments, and decisions as reasoning unfolds. Conklin and Yakemovic report an industrial trial capturing more than 2,300 requirements/design decisions; DRed was designed as a simple, unobtrusive graph of issues, options, and pro/con arguments in aerospace engineering.

**Plausible transfer:** Important conceptual discussion does not need to wait until it naturally fits a final Research, Foundation, or Specification artifact. A successor may need a low-friction capture layer followed by deliberate distillation/promotion into durable synthesis.

**Transfer limit:** Structured rationale capture creates maintenance and interaction cost. If capture is burdensome, people and models will bypass it. Raw dialogue structure should not automatically become project authority.

## 6. Activation, forcing functions, and resume reliability

### 6.1 NASA checklist research: availability is weaker than workflow integration

**Source:** Degani and Wiener, *Human Factors of Flight-Deck Checklists: The Normal Checklist*, NASA Contractor Report 177549, 1990/1991.

URL: https://ntrs.nasa.gov/archive/nasa/casi.ntrs.nasa.gov/19910017830.pdf

**Evidence class:** GOVERNMENT HUMAN-FACTORS RESEARCH.

The report examines checklist functions, format, design, length, usage, human limitations, organizational culture, and production pressure, noting that improper use or non-use can contribute to accidents.

**Plausible transfer:** Merely storing a correct procedure is weaker than embedding required checks in the workflow and designing them for actual use conditions. This directly supports treating governing-source activation as a sociotechnical/control problem, not only a retrieval problem.

**Transfer limit:** Aviation safety behavior is not evidence about LLM cognition. The transfer is about process design and forcing functions.

### 6.2 FDA human factors: design should reduce dependence on manuals and retraining

**Source:** U.S. FDA, *Human Factors and Medical Devices*.

URL: https://www.fda.gov/medical-devices/device-advice-comprehensive-regulatory-assistance/human-factors-and-medical-devices

**Evidence class:** OFFICIAL SAFETY/USABILITY GUIDANCE.

FDA frames human-factors engineering around minimizing use-related risk and explicitly lists reduced reliance on manuals, reduced training/retraining, and reduced use error among beneficial outcomes.

**Plausible transfer:** A robust project-development environment should make correct behavior easier through system/interface structure rather than depending on the collaborator remembering that documentation exists.

**Transfer limit:** Medical-device regulation is not project-knowledge design. The relevant transfer is the design philosophy of reducing reliance on memory/manual lookup for critical behavior.

### 6.3 Goal-memory and interruption research: resume cues matter

**Sources:**
- Altmann and Trafton, *Memory for goals: an activation-based model*, Cognitive Science 26(1), 2002. https://doi.org/10.1207/s15516709cog2601_2
- Dodhia and Dismukes, *Interruptions create prospective memory tasks*, Applied Cognitive Psychology 23(1), 2009. https://doi.org/10.1002/acp.1441

**Evidence class:** PEER-REVIEWED COGNITIVE SCIENCE / HUMAN FACTORS.

Altmann and Trafton model goal retrieval in terms of activation and associative priming, including the importance of cues. Dodhia and Dismukes show how interruption can impair encoding of an intention to resume and later interpretation of resumption cues.

**Plausible transfer:** Explicit resume targets, return conditions, parent relationships, and distinctive resumption cues are better design primitives than expecting an interrupted collaborator to reconstruct latent intent from prose history.

**Transfer limit:** These are human cognitive models. They justify explicit externalized cues for human/project workflows but do not prove equivalent internal mechanisms in LLMs.

## 7. Derived state, reproducibility, and history/current separation

### 7.1 Materialized views: query-shaped representations can remain subordinate to source

**Source:** Microsoft Azure Architecture Center, *Materialized View pattern*.

URL: https://learn.microsoft.com/en-us/azure/architecture/patterns/materialized-view

**Evidence class:** OFFICIAL ENGINEERING GUIDANCE.

A materialized view precomputes data in a representation suited to a particular query. The guidance explicitly treats the view as disposable because it can be rebuilt from source data, and says applications should not update the view directly.

**Plausible transfer:** The project-development knowledge architecture can plausibly separate durable source knowledge from generated current-state, routing, broad-orientation, or task-specific views, provided those views are mechanically rebuildable and visibly subordinate to source authority.

**Transfer limit:** A knowledge view is not a database materialized view in the strict sense. The transferable principle is source-authoritative plus rebuildable query-shaped projection, not a database product choice.

### 7.2 Event sourcing: complete history and current projections can be separate, but complexity is real

**Source:** Microsoft Azure Architecture Center, *Event Sourcing pattern*.

URL: https://learn.microsoft.com/en-us/azure/architecture/patterns/event-sourcing

**Evidence class:** OFFICIAL ENGINEERING GUIDANCE.

Event sourcing stores a sequence of changes in an append-only system of record and commonly derives query-optimized materialized views by replaying that history. The same guidance strongly warns that event sourcing changes storage, concurrency, schema evolution, querying, testing, and migration, and states that traditional data management is sufficient for most systems and most parts of systems.

**Plausible transfer:** Research 124 should compare the benefits of immutable/history-rich provenance plus current projections without presuming that the entire repository should become event-sourced. The pattern is useful precisely because it exposes both the power and cost of separating historical truth from read-optimized current state.

**Transfer limit:** Git history, project knowledge, and domain events are not interchangeable. Event sourcing is an analogy and candidate mechanism only where its audit/reconstruction benefits justify its complexity.

### 7.3 Build Systems Ã  la Carte: decompose architecture choices rather than copy a monolith

**Source:** Mokhov, Mitchell, and Peyton Jones, *Build Systems Ã  la Carte*, ICFP 2018 / Journal of Functional Programming 2020.

URL: https://www.microsoft.com/en-us/research/publication/build-systems-la-carte/

**Evidence class:** PEER-REVIEWED SOFTWARE-SYSTEMS RESEARCH.

The work studies build systems as points in a design landscape by separating components and orthogonal design choices, then recombining them to prototype systems with desired properties.

**Plausible transfer:** Research 124 should compare independent architecture dimensions such as canonical knowledge identity, history representation, derivation, retrieval, activation, consolidation, views, and validation instead of searching for one external system to copy wholesale.

**Transfer limit:** Build systems solve dependency/recomputation problems, not organizational memory. The transferable lesson is design-space decomposition.

### 7.4 Nix reproducibility: declared inputs help, but hidden nondeterminism still matters

**Source:** NixOS, *Reproducible Builds*.

URL: https://reproducible.nixos.org/

**Evidence class:** OFFICIAL ENGINEERING PRACTICE.

Nix derivations make dependencies explicit and sandbox builds, which creates a strong basis for reproducibility, while the project explicitly notes that nondeterministic inputs such as timestamps can still prevent bit-for-bit reproduction.

**Plausible transfer:** Generated knowledge views should have explicit source inputs, transformation identity, and regeneration rules. A claimed rebuildable view is not truly safe if hidden context, model version, prompts, timestamps, or unavailable external state materially affect its output without being recorded.

**Transfer limit:** Knowledge synthesis is often intentionally probabilistic, so reproducibility may mean provenance-complete regeneration or deterministic structural regeneration rather than byte-identical text.

## 8. Temporal semantics: when true and when known are different questions

**Source:** Jensen and Snodgrass et al., *A Glossary of Temporal Database Concepts*, SIGMOD Record.

URL: https://sigmodrecord.org/?download_id=9853&smd_process_download=1

**Evidence class:** PEER-REVIEWED / COMMUNITY TEMPORAL-DATABASE REFERENCE.

Temporal database terminology distinguishes **valid time**, when a fact is true in the modeled reality, from **transaction time**, when the fact is stored in the database.

**Plausible transfer:** Project knowledge may need to distinguish several temporal questions that are currently easy to collapse in prose:

```text
when did the underlying project fact or decision apply?
when did the project learn or record it?
when was an earlier representation superseded?
when did the successor become authoritative?
```

For example, a correction written today may describe a state that became true yesterday, while the repository only learned it today. Current-state reconstruction and historical audit have different semantics in that case.

**Transfer limit:** This does not select a bitemporal database. The evidence only establishes that multiple time dimensions are a mature modeling concept worth testing against ADS needs.

## 9. Modern LLM memory and retrieval research

### 9.1 Generative Agents: detailed experience plus reflection plus retrieval

**Source:** Park et al., *Generative Agents: Interactive Simulacra of Human Behavior*, UIST 2023.

URL: https://research.google/pubs/generative-agents-interactive-simulacra-of-human-behavior/

**Evidence class:** PEER-REVIEWED AI/HCI RESEARCH.

The architecture stores a complete natural-language record of agent experiences, synthesizes those memories into higher-level reflections, and retrieves memories dynamically to support planning.

**Plausible transfer:** This supports the broad pattern:

```text
capture detailed experience
    -> consolidate into higher-level understanding
    -> retrieve task-relevant material later
```

That pattern is highly relevant to conversation-born project insights that should not remain trapped in one chat.

**Transfer limit:** LLM-generated reflection can be lossy or wrong. The paper does not provide the authority, provenance, supersession, or source-strength guarantees required by Research 124.

### 9.2 RAPTOR: retrieval can operate over several abstraction levels

**Source:** Sarthi et al., *RAPTOR: Recursive Abstractive Processing for Tree-Organized Retrieval*, ICLR 2024.

URL: https://proceedings.iclr.cc/paper_files/paper/2024/hash/8a2acd174940dbca361a6398a4f9df91-Abstract-Conference.html

**Evidence class:** PEER-REVIEWED AI/IR RESEARCH.

RAPTOR recursively embeds, clusters, and summarizes text into a tree whose nodes represent differing abstraction levels, then retrieves across that hierarchy.

**Plausible transfer:** Broad project orientation and exact local evidence do not have to use the same retrieval granularity. Hierarchical synthesis with drill-down is technically plausible and empirically useful in long-document retrieval.

**Transfer limit:** Recursive summaries are generated abstractions, not project authority. A Research 124 successor would need stronger provenance and fidelity controls than ordinary RAG.

### 9.3 GraphRAG: global sensemaking and local retrieval are different query classes

**Source:** Edge et al., *From Local to Global: A Graph RAG Approach to Query-Focused Summarization*, Microsoft Research, 2024.

URL: https://www.microsoft.com/en-us/research/publication/from-local-to-global-a-graph-rag-approach-to-query-focused-summarization/

**Evidence class:** RECENT AI RESEARCH.

The paper argues that conventional RAG performs poorly on global questions about a whole corpus, such as identifying major themes, and introduces graph/community summaries for global query-focused summarization. Microsoft later distinguishes global, local, and hybrid/DRIFT-style query modes.

**Plausible transfer:** Project-level orientation, domain-level synthesis, and exact artifact lookup are materially different retrieval tasks. A mature reconstruction system may need an explicit query/reconstruction planner rather than one universal retriever.

**Transfer limit:** GraphRAG's graph and summaries are LLM-generated derived state. They cannot automatically become authority-bearing project truth.

### 9.4 LongMemEval: long-term memory has separable stages and failure modes

**Source:** Wu et al., *LongMemEval: Benchmarking Chat Assistants on Long-Term Interactive Memory*, ICLR 2025.

URL: https://proceedings.iclr.cc/paper_files/paper/2025/hash/d813d324dbf0598bbdc9c8e79740ed01-Abstract-Conference.html

**Evidence class:** PEER-REVIEWED RECENT AI MEMORY RESEARCH.

LongMemEval evaluates information extraction, multi-session reasoning, temporal reasoning, knowledge updates, and abstention. It reports a substantial accuracy drop for commercial assistants and long-context models across sustained interactions and decomposes long-term memory design into indexing, retrieval, and reading.

**Plausible transfer:** Putting more history into context is not equivalent to robust project memory. Capture/indexing, retrieval, evidence consumption, temporal/update handling, and abstention are separable capabilities that can fail independently.

**Transfer limit:** The benchmark studies conversational memory, not authority-governed project repositories. Its stages should inform evaluation decomposition, not define the target architecture.

## 10. Counterweights against overengineering

The external evidence does not uniformly point toward more structure.

### 10.1 Ontology evolution is itself an ongoing maintenance process

**Source:** Zablith et al., *Ontology evolution: a process-centric survey*, The Knowledge Engineering Review 30(1), 2015.

URL: https://oro.open.ac.uk/39267/

**Evidence class:** PEER-REVIEWED KNOWLEDGE-ENGINEERING SURVEY.

The survey treats ontology evolution as a multi-stage process required to keep an ontology aligned with changes in its modeled domain and system requirements.

**Implication:** A formal semantic layer can itself become a substantial governed system with migration, repair, validation, and evolution cost. Research 124 should not choose a knowledge graph or ontology merely because explicit semantics are attractive.

### 10.2 Materialized views multiply consistency and maintenance surfaces

The Materialized View guidance notes update and consistency concerns, especially when source data changes while views are generated. Many task-specific views therefore create regeneration and validation obligations even if they are derived.

**Implication:** Generated views reduce read cost only if their refresh, provenance, staleness, and rebuild contracts remain cheap enough to manage.

### 10.3 Event sourcing demonstrates that maximum historical fidelity can be operationally expensive

The Azure Event Sourcing guidance explicitly recommends using the pattern only where auditability and historical reconstruction justify the complexity.

**Implication:** "Preserve every transition as a first-class domain event" is not automatically superior to Git plus selected structured provenance. Granularity must earn its cost.

### 10.4 Design-rationale capture succeeds only when capture friction stays low

DRed's industrial rationale-capture work emphasizes simplicity and unobtrusiveness. Earlier design-rationale systems often failed to become routine tools when the recording burden was too high.

**Implication:** A theoretically elegant knowledge schema can be worse than a simpler architecture if models or humans routinely bypass it. Capture economics is a first-class design constraint.
## 11. Cross-disciplinary synthesis: what the evidence changes

The phase-1 evidence field does not select a successor, but it materially expands and sharpens the design space.

### 11.1 Conceptual knowledge identity should be investigated independently of document identity

SKOS and library/reference-model practice show mature precedents for intellectual or conceptual identity that survives labels and manifestations. Research 124 should therefore test whether important ADS concepts, decisions, questions, claims, risks, or workstreams need stable identities independent of the current Markdown file containing them.

This is directly relevant to the owner's example of the human versus human-plus-LLM versus ADS distinction. That concept currently has historical, canonical, and routing representations. The evidence suggests that those may be understood as several manifestations/views of one durable conceptual subject rather than merely unrelated files linked by convention.

### 11.2 One primary hierarchy is unlikely to be enough

Faceted navigation, software architecture viewpoints, provenance models, library user tasks, and temporal models all independently suggest that several axes can be simultaneously valid:

```text
semantic subject / concept
artifact or representation type
authority / maturity / epistemic state
chronology / temporal validity
workstream / dependency / control flow
provenance / derivation
evidence depth
privacy / access boundary
stakeholder / task viewpoint
```

A successor should therefore be evaluated on whether it supports multiple orthogonal traversal axes without manually duplicating project truth.

### 11.3 Capture, consolidation, and authority promotion are different lifecycle functions

Organizational-memory and design-rationale work support low-friction capture of reasoning as it occurs. Generative Agents and hierarchical retrieval research support later consolidation into higher-level representations. OAIS, PREMIS, and PROV-O emphasize retaining enough context and provenance to understand where derived knowledge came from.

A promising research abstraction is therefore:

```text
capture
    -> distill / consolidate
        -> review / validate
            -> promote durable synthesis where justified
                -> retain provenance to original evidence and reasoning
```

This is not yet a file layout or workflow specification.

### 11.4 Current understanding and historical provenance need not be the same representation

OAIS, preservation metadata, temporal modeling, event-sourced projections, and materialized views all provide independent precedents for separating authoritative history/source information from query-shaped current representations.

This strengthens a Research 124 question that goes beyond the current `CURRENT_STATE`/checkpoint split: can one durable substrate support historical audit, current synthesis, semantic exploration, and task-specific reconstruction as distinct projections with explicit lineage?

### 11.5 Reconstruction should be task-shaped

IFLA user tasks, ISO viewpoints, GraphRAG global/local modes, RAPTOR abstraction levels, and materialized views all converge on the idea that different questions need different information shapes.

A stable bootstrap mechanism should probably determine what reconstruction task is being attempted before selecting depth and breadth. This supports a reconstruction planner concept but does not yet determine whether that planner is deterministic code, structured metadata plus an LLM, generated indexes, or another mechanism.

### 11.6 Activation is not merely retrieval

NASA/FDA human-factors evidence and the project's own BL-001/BL-002 history agree on a systems principle: making correct information available is weaker than integrating required checks into the workflow at the moment they matter.

For Research 124, the transferable target is **reliable pre-action activation**, not an assumption that an LLM has the same cognitive mechanisms as a pilot or medical-device user.

### 11.7 Vocabulary mismatch makes single-label routing structurally brittle

Furnas, SKOS labels, faceted search, and modern semantic retrieval all support multiple access paths. Exact paths and controlled terms remain useful for precision, but aliases, relationships, lexical search, semantic search, and task context should be compared as complementary rather than mutually exclusive mechanisms.

### 11.8 Derived intelligence should remain traceable and rebuildable

Materialized-view practice, reproducible-build thinking, OAIS descriptive information, and generated LLM indexes all suggest a useful boundary:

```text
canonical durable source knowledge
    -> declared transformation/indexing/consolidation process
        -> rebuildable derived view/index/synthesis
```

Where a derived synthesis becomes unique project truth, it should require explicit promotion into authority rather than silently inheriting authority from repeated use.

### 11.9 Temporal semantics deserve explicit treatment

The project currently distinguishes current, historical, superseded, rejected, and unresolved knowledge, but the external temporal literature suggests a deeper question: whether "when true/applicable" and "when recorded/known" need separate semantics for some knowledge classes.

This should be tested against concrete ADS cases before selecting a representation.

### 11.10 The strongest external pattern is architectural pluralism under explicit contracts

Across these disciplines, the most consistent signal is not one technology. It is separation of concerns:

```text
concept identity != label
source truth != query view
history != current projection
capture != consolidation
consolidation != authority promotion
retrieval != activation
broad orientation != exact evidence lookup
fact applicability time != recording time
human-readable view != machine-readable relationship structure
```

Research 124 should preserve those distinctions while still minimizing operational complexity.

## 12. Architecture discriminators that now deserve deeper research

The next external-evidence work should not yet synthesize a target. It should deepen the questions where architecture choice remains genuinely open.

### D1. Knowledge identity

```text
What deserves a stable identity?
file / artifact
concept / subject
decision
claim
question
risk
workstream
source/evidence object
or a small typed set of these?
```

### D2. Multi-axis organization

Can semantic, temporal, authority, provenance, workstream, evidence-depth, and artifact-type views be generated from one coherent substrate without creating several manually synchronized truths?

### D3. Capture and promotion

What is the cheapest reliable mechanism for turning conversation-born insight into durable knowledge without forcing every thought directly into a canonical artifact family?

### D4. Source versus derived state

Which representations must be authoritative source, which can be rebuildable derived state, and what exact lineage/rebuildability contract is required for generated summaries, graphs, indexes, routes, and current-state views?

### D5. Authority-aware retrieval and activation

How should the architecture distinguish ordinary relevance retrieval from mandatory governing-source resolution, and how can pre-action gates remain reliable without becoming noisy or over-constraining?

### D6. Temporal and supersession semantics

Which project facts require applicability time, recording time, supersession time, or explicit version lineage? Can simpler status fields cover most cases while stronger temporal modeling is reserved for the minority that needs it?

### D7. Consolidation quality

How should detailed history be compressed into durable synthesis while detecting omission, distortion, stale claims, authority leakage, and provenance loss?

### D8. Maintenance economics

At 5x and 10x scale, what is the marginal cost of adding, updating, consolidating, regenerating, validating, and retiring knowledge? A candidate that retrieves beautifully but requires excessive metadata/schema maintenance should fail this discriminator.

## 13. Phase-1 evidence disposition

Phase 1 establishes a sufficiently broad independent evidence field to move beyond internal intuition without yet exposing the project-owner withheld paper/video.

The most consequential result is that several Research 124 ideas now have independent cross-disciplinary support while also gaining important counterweights:

```text
concept identity independent of filename        plausible and well precedented
multiple task-shaped / concern-shaped views     strongly precedented
provenance as explicit relationships            strongly precedented
source + rebuildable derived projections        strongly precedented
capture -> consolidate -> retrieve              supported, but authority safety absent in AI work
workflow-integrated activation                   supported as systems principle
explicit resume cues                             supported in human-factors literature
hierarchical/global/local retrieval              supported in modern AI retrieval
formal ontology/graph everywhere                 NOT justified
full event sourcing                              NOT justified
LLM-generated summary as authority               NOT justified
one universal reconstruction packet              increasingly difficult to justify
```

The next Research 124 step should therefore be **targeted evidence deep dives on the discriminators above**, followed by requirements/evidentiary-provenance reconciliation. Target-architecture synthesis remains intentionally later.

The owner-provided paper/video remains withheld until those independent deep dives have established the broader evidence field strongly enough to evaluate its incremental contribution rather than anchor on it.

```text
RESEARCH125_PHASE1=CROSS_DISCIPLINARY_EVIDENCE_ESTABLISHED
TARGET_ARCHITECTURE=NOT_SELECTED
EXTERNAL_EVIDENCE=EXPANDS_WHOLE_ARCHITECTURE_DESIGN_SPACE
NON_AI_EVIDENCE_STREAMS=SUBSTANTIAL
NEXT=TARGETED_EVIDENCE_DEEP_DIVES
WITHHELD_OWNER_SOURCE=STILL_WITHHELD
```