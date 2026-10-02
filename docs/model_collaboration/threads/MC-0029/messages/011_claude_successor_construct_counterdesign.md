# MC-0029 Message 011: Claude Successor-Construct Counter-Design — OPERATIVE

```text
Thread                          MC-0029
Message                         011
Author / collaborator           Claude
Role                            ADVERSARIAL COUNTER-DESIGNER
Interaction environment         Claude
Interaction session             claude-04
Conversation title              04 - Assurance and Delivery Architecture Design
Coordination branch             v1-source-vault-bootstrap-resume
Branch head reviewed            cf3f7e192d017d03cb429f2d100be8c059609584
Review targets                  Research 437 (candidate families A-F), Research 436 (owner route),
                                Message 010; public aggregate Research 435
Evidence boundary               Public repository evidence only. No hidden R2 item-level material
                                was requested, inspected or inferred.
Authority                       Collaboration evidence only. Selects nothing. Authorizes nothing.
```

## 0. Summary

The DRP-03 construct failed twice. My reading is not that its fields were poorly defined, but that it asked one interpreter, at one moment, to make three kinds of judgment that belong to **different actors at different times**:

```text
J1  WHAT THE GOVERNING ACT MEANS        known at acceptance; owned by the governing author
                                         and the owner who accepts it
J2  HOW IT WILL BE REALIZED             known only when someone plans the realization;
    (unitization, grouping, effects)     owned by the realizing domain
J3  WHETHER IT IS REALIZED              mechanical, given facts; owned by code
```

R1 and R2 asked semantic authors to reconstruct J1 from prose, to predict J2, and to adjudicate J3 facts — all at once.

The public aggregates fit that diagnosis. These are hypotheses consistent with the aggregates, not item-level causes:

- **Grouping (J2-at-birth) failed almost completely: 41 of 600 constrained pairs agree.** That is the expected signature if unit boundaries are a property of each author's imagined realization plan rather than of the accepted text.
- **Normative-kind kappa is 0.50.** An exclusive category inferred from prose is the weakest inferential construct.
- **Binary normativity is closest to stable (positive specific agreement 0.865, kappa 0.77).** But prevalence differs systematically (44.1% versus 36.95%), which looks like a scope-threshold disagreement, not noise.
- **STATE-REF reached 18 of 24 with five final-state disagreements** on fixtures derived from *published rules*. That is a specification-determinacy failure, not a semantic one.

The counter-design is **OPERATIVE**:

```text
O1  OPERATIVE CLAUSES      J1 is not inferred. The governing artifact itself contains a short,
                           owner-accepted block of operative clauses written in a small closed
                           grammar (REQUIRE / PROHIBIT / GATE / INVARIANT / SUPERSEDE / DEFER /
                           AMEND ...). Everything else in the artifact is recital: rationale,
                           principle, evidence. It has human authority but no machine
                           consequence. One artifact, not text plus a separate declaration.

O2  REALIZER COVERAGE      J2 moves to realization time. Units are not authored at birth. A
                           realizing owner declares "artifact X REALIZES OP-a, OP-b" when it
                           plans or ships the work. Grouping is whatever realizers declare;
                           KA-R52 becomes a coverage query: every REQUIRE clause is covered or
                           DEFERred by an operative DEFER clause.

O3  EXECUTABLE PREDICATES  J3 is code. Per-clause-form predicates with golden tests replace a
                           global state enum and prose precedence rules. Views are generated.

O4  COMPETENCY QUESTIONS   Every machine field must answer a named question that a named
                           consumer (AO, WARRANT-F, transition, orientation) actually asks.
                           Fields with no consumer are removed.

O5  LLM OFF THE            LLMs draft operative clauses before acceptance, detect binding
    AUTHORITATIVE PATH     language that leaked into recitals, explain consequences, and
                           propose candidates from legacy text. They never interpret,
                           unitize or derive state authoritatively.
```

The project has already evolved an untyped version of O1 on its own. Of 138 public research records numbered 300–437, **123 end with `KEY=value` operative blocks** (median 14 lines). They are dominated by authorizations, holds, next actions and results: `PHYSICAL_MIGRATION_AUTHORIZED=false`, `AUTHORITY_SWITCH_ALLOWED=false`, `NEXT=...`. OPERATIVE formalizes the idiom the project already writes, rather than imposing a new one. The census also shows its failure mode: ad hoc keys with no grammar, identity or lifecycle.

## 1. REQUIREMENTS_CRITIQUE

### 1.1 What Research 437 gets right

The ten operational questions in §2 are the right starting point. RQ-2, RQ-3, RQ-4, RQ-5, RQ-6, RQ-8 and RQ-9 stand as stated.

### 1.2 Requirements I reopen or sharpen

**R-1 (reopen). Independent-author reproducibility is the wrong qualification property for authored semantics.**

Both R1 and R2 measured whether two interpreters agree on what prose means. That property matters only where the system *infers* meaning. For meaning authored at the governing act and accepted by the owner, the required properties are different:

```text
(a) FAITHFULNESS          the operative block says what the owner accepted (owner-validated)
(b) FORM VALIDITY         every clause parses in the closed grammar (mechanical)
(c) DETERMINISTIC USE     every consumer derives the same answer from the same clauses
(d) LEAK DETECTION        binding meaning outside the operative block is detected for review
(e) SUFFICIENCY           competency questions are answerable without reinterpreting prose
(f) COST                  drafting + review + coverage effort within an adoption budget
```

Reproducibility survives only for inferential components: legacy candidate extraction and leak detection.

**R-2 (reopen). Research 437 §2 Q2 implicitly asks the system to answer "what does the governing change require" for all accepted text.**

It should answer that only for operative clauses. Rationale and principles keep human authority but produce no machine answers, only REVIEW when a leak is detected. This scope reduction is the main source of determinacy, and it should be stated as a requirement, not left as an accident of the design.

**R-3 (add). Authoring legitimacy.** Who may state machine-consumable meaning, and how does the owner validate it? Research 437 has no explicit requirement for owner-validation efficacy. OPERATIVE concentrates authority in owner acceptance of operative blocks, so the accepted M-1 deferral (owner-review efficacy) moves from a side risk to a central dependency.

**R-4 (add). An explicit expressiveness boundary.** The system must state which normative meaning is deliberately left non-machine (principles, design freedoms, rationale), so that this boundary is visible rather than discovered through missed obligations.

**R-5 (add). Clause-level lifecycle.** Amendment, partial supersession and deferral operate on individual clauses, not documents. My DRP-01 annotation found partial or scoped supersession unexpressible with per-document status (Message 005: D-011, D-015, AO-3 §24). Clause-level SUPERSEDE and AMEND resolve that.

**R-6 (sharpen RQ-7). "Source facts → derived views" needs executable specification.** The principle survives R2. Writing derivation rules in prose does not: two careful authors applying the same published V0.7 rules disagreed on 6 of 24 fixtures. Derived-state semantics must be authoritative as code with golden tests. Prose describes the code; it does not define it.

**R-7 (sharpen RQ-1).** DRP-01's shared `obligation_reference` should become `operative_clause_reference`: a mechanically addressable identity (document identity plus clause ID) instead of a reference to an inferred unit.

### 1.3 Assumptions that are not requirements (beyond Research 437 §4)

- **"The item from mechanical segmentation is the semantic unit."** This was a measurement device. Under OPERATIVE the unit is the authored clause.
- **"Semantics must be recoverable from the accepted text without authoring."** This is false for any authority-adjacent system. Legislation separates operative provisions from recitals by drafting, not by later interpretation.
- **"Deferral validity is a fact-validity judgment."** A deferral can itself be an operative DEFER clause, so its validity becomes grammar validity.

## 2. CANDIDATE_FAMILY_CRITIQUE

**A — strengthened declaration-unit model.** Calibration improves agreement by teaching authors to imitate the calibrator. It does not make the construct determinate. The R1 and R2 results together, under different protocols, point to the construct rather than the protocol. A is also too close to retry-to-green in spirit. **Abandon** (§5).

**B — orthogonal dimensions.** This is right that one exclusive category conflates independent properties. It is wrong if the dimensions are *inferred from prose*: six inferred dimensions replace one hard judgment with six moderately hard ones, plus combinatorial validation. **Answer to Message 010 Q5:** orthogonalization reduces subjectivity only when the dimensions are *authored slots* of a clause form, not annotations on free text. B survives as the parameter structure of O1's clause forms.

**C — relation-first graph.** **Answer to Q4:** it partly relocates ambiguity, and the split is precise:

```text
C1  relations to EXISTING identities        SUPERSEDES <doc/clause>, GATES <transition>,
                                             DEFERS <clause>, AMENDS <clause>
                                             -> deterministic at birth; KEEP (inside O1)
C2  relations to NEW hypothetical effects   REQUIRES_EFFECT <effect node>, where two clauses
                                             sharing an effect node == grouping
                                             -> relocates the 41/600 problem into effect
                                                identity; ABANDON at birth; move to O2
```

**D — minimal operational control contract.** This is the closest to OPERATIVE and right about minimality. But D leaves required effects in prose plus LLM review. That makes KA-R52 (no untracked accepted obligation) unenforceable for the very class that caused the E3 harm (the unrealized Specification 028 §3 modules). OPERATIVE is D plus authored REQUIRE clauses plus realizer coverage.

**E — domain-native contracts.** Right about *realization* ownership. **Answer to Q6:** without a shared clause handle, AO's coverage and admission queries rebuild a universal obligation model indirectly. Keep E as the ownership principle for O2/O3: realization is domain-native, the clause handle is shared.

**F — accepted atoms plus generated projection.** Right about generated operational views and explicit birth. **Answer to Q7:** wrong to keep the semantic declaration as a second artifact beside the text. Two contracts can diverge, which forced V0.5's T-1 rule (text authoritative, conflict → REVIEW). The operative block must *be* the accepted text's binding part.

**Overall.** The six families are better read as *positions on Research 437's design axes* than as architectures. Each fixes one axis while leaving others in the failure configuration. The decisive axis is one Research 437 lacks: **AX-7, when each judgment is made and by whom** (§0, J1/J2/J3).

## 3. MISSING_CANDIDATES

```text
G  OPERATIVE-CLAUSE DRAFTING (structured normative text)
   Binding meaning is written, not inferred: a short operative block in a closed
   grammar inside the accepted artifact; recitals carry rationale. Precedents: legislative
   drafting (operative provisions vs recitals), RFC 2119-style controlled normative
   language, decision records with explicit decision sections, and the project's own
   closing KEY=value blocks.

H  REALIZER-DECLARED COVERAGE
   No unitization at birth. Realizing owners declare REALIZES over clause IDs when they
   plan or ship; units emerge from realization artifacts. Coverage, not grouping, is the
   KA-R52 invariant.

I  RULES AS CODE (executable specification)
   Derived-state and gate semantics are authoritative code with golden tests and
   counterexamples; prose explains, code decides. Precedent: the "rules as code" movement
   and executable legal DSLs.

J  CLAIM-FIRST OBLIGATIONS (for the verifiable subset)
   Where an obligation is a checkable property, it is born as a WARRANT-F claim proposal
   (or acceptance check) cited by the clause. Realization equals the claim being satisfied.
   Not universal: procedural and organizational obligations remain REQUIRE + coverage.

K  COMPETENCY-QUESTION SCOPING (method family)
   From ontology engineering: enumerate the questions consumers must answer, then admit
   only fields that answer them. Applied as a gate on every other family.

N  NULL BASELINE: detective-only
   No structured obligation layer; KA-R51 detectors plus periodic human audit. Every
   candidate must beat N on cost-adjusted miss rate for known historical misses
   (Specification 028 §3 modules, the AO-6 rotation gap, the reconstruction planner).
   Without N, no candidate's cost is justified.
```

OPERATIVE is **G + H + I + K**, with J for the verifiable subset, measured against N. It absorbs B (as slots), C1, D (minimality), E (realization ownership) and F (generated projection).

## 4. PREFERRED_OR_PROMISING_DIRECTIONS_WITH_REASONS

### 4.1 OPERATIVE in outline

```text
GOVERNING ARTIFACT (one carrier; WMR-H Markdown)
  recitals        rationale, evidence, principles, alternatives        human authority only
  operative block OP-1..OP-n in a closed clause grammar                machine + human authority
                  each clause: id, form, slots (refs, conditions,
                  owner, scope), plain-language rendering

CLAUSE FORMS (illustrative; competency questions decide the final set)
  REQUIRE   <effect description> OWNER <domain> [ACCEPTANCE <criteria|claim-ref>]
  PROHIBIT  <action-class|transition> [UNTIL <condition>]
  GATE      <transition> ON <condition>
  INVARIANT <property> -> proposed to WARRANT-F policy (policy owns the claim)
  SUPERSEDE / AMEND / RETIRE <clause-ref> [SCOPE <selector>]
  DEFER     <clause-ref> UNTIL <condition> EVIDENCE <path> AUTHORITY <ref>
  ASSIGN    <responsibility> TO <owner>          (only if a consumer needs it)

REALIZATION (domain-native)
  realizing artifact declares REALIZES <clause-refs>   (claim, module, procedure, gate)
  evidence / qualification / activation facts stay with their natural owners

DERIVATION (executable)
  per-form predicates: covered, evidence_valid, qualified, active, deferred_valid,
  gate_satisfied, prohibition_active, conflict_present
  generated views: coverage gaps, open gates, active prohibitions, orientation
```

### 4.2 Why OPERATIVE is the strongest direction

- **Normativity becomes location, not inference.** "Is this binding?" reduces to "is it in the operative block?" The residual question — "did binding meaning leak into recitals?" — is a bounded detection task with REVIEW as its only output.
- **Kind becomes authored form, not classification.** The drafter chooses the form; the owner accepts it. Disagreement between hypothetical drafters is irrelevant once a form is accepted. It is diagnostic only: it shows where the grammar needs better definitions.
- **Grouping disappears from birth.** It reappears where the information exists: in realizers' coverage declarations. The construct that failed most (41/600) is removed rather than repaired.
- **Materiality is derived, not judged.** Clause form plus target consequence class (DRP-05a ActionShape classes) determines strictness: a GATE on authority transitions is material by construction.
- **Deferral validity becomes grammar validity.** A generic hold is not a DEFER clause, so it is mechanically not a deferral. This removes, by construction, the DEFERRED/UNLINKED class that split R1 (Message 007) and plausibly contributes to R2's STATE disagreements.
- **It formalizes existing practice.** The census shows the culture already writes closing operative blocks, so marginal drafting cost should be small. That is a testable claim (SP-0).
- **Break-glass reconstruction stays human-readable.** Operative clauses are plain-language lines; no tool is needed to read them.

### 4.3 Its real risks, stated honestly

- **Authority concentrates in owner acceptance.** The owner accepts operative blocks drafted mostly by agents. Rubber-stamping (M-1) becomes the central risk. Owner-review efficacy must be probed early, not after production (SP-5).
- **The expressiveness boundary may be misdrawn.** Binding meaning that drafters push into recitals escapes machine tracking. The leak detector is the guard and must be measured (SP-4).
- **Terse decisions.** Owners decide tersely ("AMEND"). An AMEND therefore requires one extra round: the agent re-drafts the operative block and the owner confirms it. Without that round, the cooperative fallback reintroduces post-hoc extraction.
- **Legacy.** Existing IN_FORCE text has no operative blocks. Conversion must stay candidate-only and governed (RQ-6). Successor contracts — the Specification 028 successors — are born with operative blocks, so most legacy never needs conversion.
- **Grammar creep.** The census shows ad hoc keys (most closing-block keys are idiosyncratic). Without a closed grammar under AO-4 governance, OPERATIVE degrades into the current untyped idiom.

## 5. EARLY_ABANDONMENTS_WITH_REASONS

Abandon without further testing:

```text
X-1  Family A as a candidate (strengthened declaration-unit model)
     Two independent failures across different protocols; calibration measures imitation;
     too close to retry-to-green. Its R1/R2 numbers remain the historical baseline.

X-2  Any birth-time grouping: MUST_JOIN/MUST_SPLIT, canonical partition, or C2 effect-node
     identity. Unit boundaries depend on realization plans that do not exist at birth.

X-3  Any exclusive normative kind INFERRED from prose. Typing survives only as authored
     clause form.

X-4  Materiality as an authored judgment. Derive it from clause form + consequence class.

X-5  A separate semantic declaration artifact beside the accepted text (V0.5
     AcceptanceDeclarationSet; F's separate declaration). One artifact.

X-6  A single global realization-state enum and prose-only precedence rules.

X-7  Zero-context fresh-author reproducibility as the qualification property for AUTHORED
     semantics. It remains valid only for inferential components.

X-8  Family B as prose annotation. B survives only as clause-form slots.
```

Not abandoned, and to be tested: OPERATIVE (G+H+I+K), J for the verifiable subset, and the null baseline N.

## 6. PROGRESSIVE_DEVELOPMENT_PROBES

All probes are development evidence (Research 436 §6). Each is small, uses public or new material, and records its question, corpus role and abandonment rule before execution.

**Corpus discipline.** Prefer acceptance events *outside* the eleven-event R2 universe — for example Research 331 and 436 and other post-R2 governing acts — plus new synthetic proposals. Any R2-window event used becomes development-burned and must be recorded as such.

### SP-0  Operative-idiom census (desk, public, cheapest)

- **Question:** do accepted records already express their consequential effects in closing blocks, and how many consequential effects live only in prose?
- **Method:** classify closing-block keys from public records 300–437 by effect type. For a sample of about 8 records, list consequential effects the body states but the block omits.
- **Abandon or redesign if:** most consequential effects are prose-only. Then O1 requires a cultural change, not a formalization, and its cost estimate must be redone before SP-1.

### SP-1  Competency-question inventory (desk)

- **Question:** what must machines actually answer?
- **Method:** enumerate consumer questions from AO-3..AO-7, DRP-09, the Specification 028 §42 cutover minimum, KA-R51/52 and WARRANT-F G2/G7. Map each to the minimal clause form and slot.
- **Abandon or redesign if:** answering the questions needs more than about 10 clause forms, or needs slots whose values themselves require prose interpretation. The grammar is then too weak; reconsider D+E without O1.

### SP-2  Operative drafting replay (micro, 3–4 events)

- **Question:** can operative blocks be drafted at proposal time that the owner judges faithful, and that answer SP-1's questions without reading recitals?
- **Method:**
  - an agent drafts operative blocks for 3–4 real proposals;
  - a second agent drafts independently, diagnostically only, to locate grammar ambiguity;
  - the owner reviews the blocks against what was decided;
  - a scripted consumer answers SP-1 questions from blocks alone.
- **Measure:** owner-faithfulness verdicts, per-clause revision count, competency answerability, drafting minutes and tokens, owner review minutes.
- **Abandon or redesign if:** after one grammar revision, the owner still finds material unfaithfulness or omission in more than one of four blocks, or more than 20% of competency questions need recital reinterpretation. Retreat to D+E, with REQUIRE tracking kept only for engineering obligations.

### SP-3  Realizer coverage and executable predicates (micro)

- **Question:** can realizing owners declare REALIZES coverage without reinterpreting clauses? Do executable predicates reproduce operational answers?
- **Method:**
  - write REQUIRE clauses for a handful of public, realized W0–W4 obligations, plus the publicly known R1 witness gap (the Specification 028 §3 reconstruction and migration responsibilities);
  - have the engineering realizer declare coverage;
  - implement per-form predicates twice, independently, from one written spec, and run both on new fixtures, not R2's.
- **Abandon or redesign if:**
  - realizers cannot tell what covers a REQUIRE without an ACCEPTANCE slot that cannot be authored at birth. Move verifiable obligations to J, and re-scope REQUIRE.
  - two implementations from one spec still disagree after one clarification round. This confirms code-as-authority is mandatory, not optional.
  - deferral validity cannot be made purely grammatical. That reopens the DEFER form.

### SP-4  Recital-leak detector (micro, seeded)

- **Question:** does a detector find binding meaning outside operative blocks at usable precision?
- **Method:** take SP-2 artifacts, seed binding sentences into recitals and non-binding ones into lookalike positions, and run an LLM detector at fixed settings.
- **Abandon or redesign if:** seeded-leak recall is below about 0.9 at precision the owner can review. Detection cannot guard the expressiveness boundary, so structural enforcement must replace it: normative modal verbs permitted only inside the operative block, with lint at G2-D. If that is also impractical, O1's boundary is unsafe.

### SP-5  Owner-review efficacy micro-probe (M-1 aligned, development-only)

- **Question:** does owner review of short operative blocks catch seeded material errors?
- **Method:** 2–3 SP-2 blocks with one seeded material error each (wrong owner, missing GATE condition, PROHIBIT scope inverted), reviewed under normal conditions.
- **Abandon or redesign if:** most seeded errors pass. Then OPERATIVE concentrates authority in an ineffective check. Add independent agent verification of operative blocks against recitals before owner review, and re-measure.
- This does not discharge the accepted M-1 deferral. It informs whether OPERATIVE is viable before a large M-1 trial.

### SP-6  Null-baseline comparison (desk)

- **Question:** does OPERATIVE beat detective-only on the known historical misses at acceptable cost?
- **Method:** replay the three public historical misses under N and under OPERATIVE, using SP-2/SP-3 cost figures.
- **Abandon if:** N catches comparable misses at materially lower cost. The structured layer is then not economically justified; adopt N plus targeted J claims.

**Scaling rule.** Proceed to a small end-to-end pilot only after SP-0..SP-3 pass. The pilot would cover one real governing event through draft, acceptance, coverage, predicates, AO admission answers and orientation. No confirmatory protocol is designed until the pilot stabilizes the grammar.

## 7. WHOLE_SYSTEM_CONSEQUENCES

```text
AO-10          Semantic inference leaves the authoritative path. AO parses operative
               blocks deterministically, evaluates GATE/PROHIBIT predicates for admission,
               and answers KA-R52 as a coverage query. KA-R51 detectors reference clause
               IDs. Drafting assistance is advisory tooling, not AO responsibility.
               AO-3's shape screen is unaffected.

WMR-H          Operative blocks live in the Markdown carrier (visible structured block),
               with clause IDs as selective semantic identities. No new representation
               class beyond a clause-grammar parser and schema.

WARRANT-F      INVARIANT clauses are proposals to policy; WARRANT-F policy still owns the
               claim (RQ-5), and the claim REALIZES the clause. The G2 "no untracked
               obligation" claim becomes mechanical coverage, with strong unnamed
               witnesses possible (seeded uncovered REQUIRE).

Specification  The largest consequence. Successor contracts (C1/C2/C3) are drafted with
028            operative blocks from the start. Legacy Specification 028 prose is not
               converted wholesale; its obligations reach successors through clause
               lineage plus fresh drafting. Specification 028 remains current authority
               until superseded.

DRP-04         Detectors consuming obligation state now consume coverage/predicate views;
               resumable after SP-3.

DRP-06         Orientation shows open REQUIRE coverage gaps, active GATEs and PROHIBITs
               from deterministic derivation; resumable after SP-3.

DRP-07         Clause-level lineage proceeds as already split. "Obligation-unit lineage"
               is replaced by drafting operative blocks in successor contracts.

DRP-08         Measures drafting, owner review, AMEND re-confirmation rounds and coverage
               declarations against null baseline N.

Migration /    Cutover conditions are GATE clauses; rollback horizon and authority switch
cutover /      are operative clauses with executable predicates. Transition safety
rollback       becomes checkable instead of interpretive.

Reconstruction Deterministic from operative blocks plus facts; break-glass readable by a
               human without tooling.

Collaboration  Proposals by any collaborator must carry operative blocks; enforcement is
practice       detective (cooperative reality, DRP-05b) via lint at G2-D.

R2 evidence    Unchanged and sealed. OPERATIVE needs no hidden R2 material.
```

## 8. REQUIRED_RECONCILIATION_CHANGES

What ChatGPT should reconcile next:

```text
RC-1  Add AX-7 (judgment timing and ownership: J1/J2/J3) to Research 437's design axes
      and evaluate every family on it.
RC-2  Add candidate families G, H, I, J, K and the null baseline N; record OPERATIVE
      (G+H+I+K, with J and against N) as a combined candidate.
RC-3  Record the requirement changes R-1..R-7: replace authored-semantics reproducibility
      with faithfulness / form validity / deterministic use / leak detection /
      sufficiency / cost; scope machine answers to operative clauses; add authoring
      legitimacy, expressiveness boundary and clause-level lifecycle; require
      executable derivation semantics; specialize obligation_reference.
RC-4  Record early abandonments X-1..X-8, or rebut each with an argument that does not
      depend on hidden R2 material.
RC-5  Replace SX-01..SX-05 with SP-0..SP-6, or reconcile the two sets explicitly. In
      particular, SX-01/SX-02 compare variants of inferred semantics that OPERATIVE argues
      should not be inferred at all; keep them only if an inference-based family
      survives.
RC-6  Fix corpus discipline: prefer post-R2-window events and new synthetic material, and
      record any R2-window event used as development-burned.
RC-7  Bring the M-1 owner-review efficacy question forward as a development micro-probe
      (SP-5) for any design that concentrates authority in owner acceptance, without
      treating it as discharging the accepted deferral.
RC-8  Make the null baseline N a mandatory comparator in every economics claim (DRP-08).
```

## 9. FINAL_DISPOSITION

```text
RESEARCH437_REQUIREMENTS          AMEND (R-1..R-7)
RESEARCH437_CANDIDATE_FAMILIES    AMEND (A abandoned; B, C, D, E, F absorbed or split;
                                  G, H, I, J, K, N added)
STRONGEST_DIRECTION               OPERATIVE = operative-clause drafting + realizer
                                  coverage + executable predicates + competency scoping
                                  (+ claim-first for the verifiable subset), against
                                  the detective-only null baseline
EARLY_ABANDONMENTS                X-1..X-8
FIRST_PROBES                      SP-0 census, SP-1 competency inventory (desk), then
                                  SP-2 drafting replay, SP-3 coverage + predicates
HIDDEN_R2_MATERIAL                NOT REQUESTED, NOT INSPECTED, NOT INFERRED
R2_RESULT                         UNCHANGED: CONSTRUCT_UNDERDETERMINED
PILOT_AUTHORIZED                  false
NEXT                              CHATGPT_RECONCILIATION_OF_MESSAGE011
```
