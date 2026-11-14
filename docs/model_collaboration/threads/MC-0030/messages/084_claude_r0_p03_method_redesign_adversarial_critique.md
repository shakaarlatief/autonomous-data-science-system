# MC-0030 Message 084: Claude adversarial critique of the R0-P03 bottleneck diagnosis and method redesign

```text
Thread              MC-0030
Message             084
Request             MC-0030 Message 083 (whole-program reorientation and method redesign critique)
Author / role       Claude / claude-04 (MC-0030 Messages 001, 003, 062, 064). Exposed comparative
                    methodology critic. Not a fresh scored evaluator, gold author, arm author or custodian.
Repository          shakaarlatief/autonomous-data-science-system
Branch / base       v1-source-vault-bootstrap-resume @ c418d62fe63fdbad6079be0571409949016183b5 (verified remote head)
Primary subject     docs/research/669_r0_p03_bottleneck_and_prospective_comparison_redesign_assessment.md
Verdict             PROPOSE_PROSPECTIVE_AMENDMENT
Authority           Collaboration challenge only. No protocol amendment, owner decision, score, gold,
                    source admission, implementation, migration or physical-target selection.
```

## 0. Exposure, method and limits

**Exposure.**
- I wrote Message 001, the independent LEDGER-KERNEL design.
- I wrote Message 003. Its findings F-08 (one natural J2 carrier) and F-09 (substrate selected, navigation open) were accepted into Research 512 §§9–10, so they define the P03 common substrate and arm list.
- I wrote Message 062. Its F1–F11 were reconciled in Research 559.
- I wrote Message 064. It was reconciled in Research 649 and seeded the T2 experiments in Research 650–653.

So I am partly responsible for the procedure I now criticise. I address that directly in §3.9.

**Read in full at `c418d62f`:**
- `docs/ARCHITECTURE_PROGRAM_OVERVIEW.md`;
- Research 502, 503, 507, 309, 310, 313, 512;
- Research 513 (all sections), 555, 559, 576;
- Research 635, 636, 639, 641, 654, 655, 656, 657, 658, 660, 661, 666, 667, 668, 669;
- Checkpoint 931 and `docs/current_routing.json`.

**Read earlier in this same conversation:** Research 642–648 (for Message 064). In this session I re-checked only their result tables and statements, not their full text.

**Spot-checked for material claims:**
- the status and result tables of Research 650–653;
- `experiments/r0_p03_navigation_probe/route_b_primary_b0_baseline_execution_v01.py` (the `INDEX_CHAR_LIMIT = 12000` constant, and B0 is FTS-only);
- the V03 qualification fixtures `experiments/ao10_hybrid_d1_replay_v01/{accepted_j1.json,source_facts.json}` and `experiments/ao10_hybrid_d2_lineage_v01/reviewer_fixtures.json`;
- the Research 491 header;
- commit dates of the three historical source pins;
- a whole-tree search for V03 J1 carriers.

**Not read:**
- Research 504, 508, 511, 517 and 556–634, apart from their titles and headers. Older results are therefore cited from the documents that report them; for example, the R0-P02 PASS comes from Research 555 §4.
- No protected C01/C02 material, private reviewer report, hidden gold, owner credential or external web source.
- Research 560–634 except titles. Claims about that span are limited to title-level classification and are marked as such.

**Labelling.** "Observed" means I read it in a source or ran it. "Hypothesis" means a reasoned conjecture that still needs a test.

## 1. Whole-program reorientation and current R0 status

### 1.1 What is being built

**The program's purpose.** The program is building the **Project System**: the system that designs, governs, researches, builds, qualifies, preserves, migrates and evolves the Autonomous Data Science System (ADS) Product. It sits in a Product/Project split (G-DUAL). Inside it, separate planes interlock:
- **Activation/Orchestration (AO):** what is happening and what happens next. **AO-4** governs architecture evolution.
- **Knowledge / state / authority:** now the selected V03 kernel.
- **Assurance and admission:** WARRANT-F.
- **Execution and delivery.**
- **Observation, recovery and evolution.**

The whole is one Project Operating Architecture (Research 309 §3, 310 §3). It is meant to be self-improving but never self-modifying (310 §2), with the owner keeping normative authority. The Project-Sovereign Materialized Framework (PSMF) and generic-framework extraction are deliberately postponed until ADS has been implemented, migrated and operated (309 §2).

**History.**
- **D-035 / Specification 028.** The original Project Knowledge Architecture (PKA-CANDIDATE-01). It was built through W0–W4. Its W5 navigation work produced the Research 217 controlled subject system.
- **Research 313.** Removed any preservation right from that subject system and from every semantic mechanism. Only the empirical lessons are kept.
- **Research 502 (D-036).** After the AO-10, R2, C1–C9 and D1–D3 work, D-036 selected **THIN_CENTRED_HYBRID_V03** as the logical semantic/control kernel. It has three layers:
  - **J1:** accepted governing meaning.
  - **J2:** natural-owner realization facts.
  - **J3:** mechanically derived operational truth.

  D-036 keeps Specification 028 as current operational authority (502 §§1, 6). It deliberately freezes no physical choice: not the files, storage, workflow, CI/CD or J1 package syntax (502 §4).
- **R0.** Research 503 opened R0 as first-principles physical/software realization under 44 requirements. Research 507 added R0-R45…R62, which cover semantic organization and the executor boundary.
- **Independent designs.** The independent ChatGPT design (504 + 508) and Claude design (Message 001) were reconciled into GOVERNED_LEDGER_KERNEL_V01 (Research 511). After Message 003 they became **V02** (Research 512). V02 is the leading physical candidate, not a selected one.
- **The three probes.** Research 513 preregistered P01 (owner authenticity), P02 (admission and ordering) and P03 (navigation).
- **R1–R7 after selection.** R1 is the physical contract. R2 is implementation. R3–R7 are semantic inventory, shadow operation, reversible migration, untouched confirmation and authority switch (502 §7; overview §16).

### 1.2 Corrections to the stale overview (overview §§1, 17, 22, dated 13 October, Checkpoint 896)

| Overview statement | Status at `c418d62f` |
|---|---|
| "R0-P03 CURRENT… Checkpoint 896 source-role frame… gold/scoring not yet frozen" | Routing is now at **Checkpoint 932**, `latest_experiment_outcome=INCOMPLETE`, boundary `p-three-method-redesign-claude-critique-pending` (`docs/current_routing.json`). |
| Option A legacy gold accepted, not executed | **Still not executed.** Research 636 §2 lists the neutral nine-case adjudication as "not completed". |
| (absent) | **Research 576**: owner-accepted Level B execution method (no OS sandbox mandate; Level C allowed only unscored). |
| (absent) | **C01**: 6 provisional closures and 6 material HOLDs (Research 635). **C02**: 8 distinct, 2 duplicate, 2 uncertain; 0/10 full-scope closures after a review of 37 original files (Research 639, 641). |
| (absent) | **Exploratory execution.** Every arm has a working prototype that has been run, all under exposure and unscored:<br>• legacy B0-like versus B1-like (Research 642);<br>• fusion and routing (645);<br>• directed relations (646);<br>• 719 paraphrases (647);<br>• T2 currentness and false-authority work (650–653);<br>• Route B on 12 exposed tasks with B0, B1, B2, B3 and classical-LSA B4 (655–657);<br>• extractive answers (658);<br>• masked Claude reviews (660);<br>• the four-need pilot (661–666);<br>• source frontier and documentary chain (667–668). |
| R0-P01 / P02 | Unchanged: P02 PASS within its synthetic and live-host scope. P01 Attempt 001 is AMEND, and further P01 work is deferred (Research 555 §§3–4). |
| Physical target | Not selected. V02 is the leading candidate. Specification 028 remains operational authority. |

**Scale of the P03 effort (observed from file headers and titles).**
- **114** research documents (556–669), dated 12 October to 14 November 2026.
- **39** checkpoints (894–932).
- Messages 061–083.
- **Zero** formal B0–B4 scores.

About 30 of the 114 titles, concentrated in Research 562–616, concern custody, sandboxing, recipient keys and CMS envelopes, host and ACL isolation, fictional or fake custody rehearsals, and reviewer handoff routes. This is a title-level classification; I did not read those documents.

### 1.3 Classes of design freedom (Message 083 §1)

1. **Physical mechanisms** (files, folders, storage, schemas, CI/CD, branch/merge/review workflow, collaboration procedures, navigation machinery): no preservation right (503 §2, 507, 555 §1).
2. **Selected logical V03 obligations** (503 §3 invariants): in force until a governed AMEND/SUPERSEDE/REOPEN, and still open to evidence (502 §8).
3. **Current operational contracts**, including Research 513/559/576 as the P03 contract: in force until an owner-approved prospective amendment (513 §2.1, L46; 555 §1).
4. **Historical results** (C01/C02 HOLDs, Route-B outputs, Research 217): immutable.

My recommendation changes only class 3, and only prospectively.

## 2. Independent diagnosis of the blocking dependencies

### 2.1 Source-to-claim trace

| Path | What was required | What failed | Source |
|---|---|---|---|
| **C01** (12 fresh-author needs) | "Complete source/authority closure before build inclusion" (576 §2.1, L26) | Six HOLDs. Their gaps: endpoint authority (6), integrated workflow event (5), independent executed validation receipts (6), owner approval audit (3), and failures/rollback (6). | 635 "What improved" |
| **C02** (12 new needs) | The same closure, "at complete original question scope" | 0/10 closures after 37 original files were reviewed. No case "with sufficient source evidence for its complete original question scope". | 641 §2, L36 |
| **Four-need pilot** | Full-scope reviewer support | 1/4 supported. Wide demands ("every route", "all indirect dependencies") exceeded the budget. | 661 §§2, 4 |
| **Common substrate** | J1 effects, lineage, J2 coverage, receipts and authority labels equal for all arms (513 §6.2, L447) | 0/80 sources adjudicated for authority. 0 accepted J1 effects and 0 J2 REALIZES relations in a 10-carrier chain. | 667 §2; 668 §3 |
| **Route-B B0** | The 513 B0: substrate plus lexical | Implemented as body FTS5 only, with a 12,000-character cap and no relations. The runner itself says so (route_b_…b0…py L43, L329). | 655 §3 |
| **Route-B B2** | Editorial links beyond the substrate | Native `Declared references`/`Authority`/`Parent` headers were excluded *because they belong to the substrate*. But no arm received them, so typed source relations were dropped from all arms. | 656 §3, L30 |

### 2.2 Ranked causal blockers

**1. Structural world mismatch (observed; I treat it as proof, not hypothesis).**
- Research 513 asks which additions improve on the **V03-native** substrate (513 L25, §6.2).
- That substrate does not exist in any real ADS history, and cannot be honestly derived from it:
  - V03 was selected on 2026-10-04 (502 header), but its J1 package representation is itself an R0/R1 deliverable (502 L167) and R2 has not started.
  - The only tracked `accepted_j1` file in the whole tree is the D1 experiment fixture `experiments/ao10_hybrid_d1_replay_v01/accepted_j1.json` (observed with `git ls-tree`).
  - Research 512 §9 (L298) forbids inferring RELATIONAL J2 "from similarity, naming, model judgment, or heuristic code reading".
  - Every P03 source pin predates any V03 carrier. For example, `4b94ffe1` is dated 2026-09-20, before D-036 itself; `c57556a8` is 2026-10-13 and `47ed6344` is 2026-11-12.
- So any real-history P03 must either drop B0 to lexical-only (as Route B did) or label a synthetic substrate. **The 513 question cannot be tested as stated in any pre-V03 world.** Research 669 §3 calls this "a credible, independently testable prerequisite mismatch, not yet proof". I think it is already established by definition.

**2. Gold standard conflated with world truth (observed).**
- The reference standard grew from "source closure" (513 §6.5 asks only for tasks plus gold) into **complete as-stated historical truth**. The gaps that blocked C01 and C02 (executed CI, owner approval audit, rollback and endpoint authority; 635, 641, 654 §5) are facts about *what happened in the world*.
- Navigation gold only needs to be relative to the source and the substrate: which carriers answer the question, what they assert, with which authority class, and where the evidence stops.
- The independent authors naturally asked about operative reality. In V03 those are exactly J1/J2/J3 questions, and legacy prose was never designed to answer them; that is why V03 was selected (overview §5, "R2 underdetermination").
- **Reinterpretation:** the C01/C02 HOLDs are evidence *for* V03's premise, not navigation evidence.

**3. Independence achieved through custody infrastructure, not through design (observed at title level; impact is a hypothesis).**
- Hidden-gold custody, encryption envelopes and sandbox qualification took roughly 30 research units (Research 562–616 titles).
- The requirement to hold full gold "outside every author-visible source/tool/context/account surface" (576 §2.2) exists only because tasks and gold were created **before** arms were authored.
- Message 062's commit-then-draw principle was applied to the held-out set but never to the tasks themselves.

**4. Comparison framing (observed).**
- P03 is treated as one pre-selection gate (513 §7). It was never decomposed into:
  - what must be known **before R1**: family sufficiency and physical lock-in;
  - what can be chosen later through a bounded interface (R0-R54, 507 L108–114).
- §4 of 669 lists "Option D" as a gate change but does not test whether the B0–B4 choice changes the physical target at all.

**5. Process loop (observed).**
- Research 636 already set out the critical path (L55) and warned against "gate-building" projects.
- Afterwards, 30+ research units extended peripheral evidence (654, 662–668) without producing an eligible reference packet.
- There was no decision-value budget and no time-boxed stop rule until 666 §5.

**6. Contributing but not binding.**
- Question sampling breadth: the wide needs in 661.
- Source access: off-index originals (635).
- Actor availability. Fresh Claude sessions were obtained repeatedly and quickly (Messages 067–082), so availability of independent actors is **not** the current binding constraint.

### 2.3 Competing explanations (Message 083 §3)

| Explanation | Verdict |
|---|---|
| Intrinsic protocol/world mismatch | **Main cause** (blocker 1). |
| Badly sampled questions | **Partial cause.** It explains C02's duplicates and the four-need breadth failures, but not the zero closures on focused needs. |
| Correct safety behaviour under incomplete evidence | **Yes for the HOLDs themselves.** They were right to refuse. The protocol's error was to require them. |
| Insufficient source access | **Minor.** |
| Missing independent actors | **Formerly binding** (the custody era). Not binding now. |
| Unnecessary gate coupling | **Yes** (blocker 4). |

## 3. Strongest objections to Research 669

### 3.1 It understates the decisive fact
669 §3 (L52–65) presents the substrate mismatch as a hypothesis. As §2.2-1 shows, it is true by construction. Option A (669 §5, L81) is described as "cannot be declared impossible categorically". For the 513 question as stated, it can: real pre-V03 history has no V03-native substrate to share across arms. What Option A *can* test is navigation over **legacy prose**, which is a different and narrower question; see §3.5.

### 3.2 It misattributes the historical-truth demand to Research 513
669 §3's graph (L46–50) says the comparison requires "complete historical owner/effect/implementation/test/CI/authority truth". Research 513 never says this. §6.5 asks for tasks from a fresh author or a mechanical rule; §6.8 asks for source citations and false-authority scoring.

The demand came in through later reference standards:
- "complete source/authority closure" (576 L26);
- "complete original question scope" (641 L36);
- independent authors choosing operative questions.

**Consequence.** The repair belongs in the **reference semantics** — gold that is relative to sources and the substrate, with UNKNOWN as a valid answer — not in making the history more complete.

### 3.3 Option B's controlled world is the right instinct but the wrong construction
An independently authored, fully synthetic project history (669 L84) has three problems:
1. It is expensive.
2. It reproduces the custody problem: someone must hide the scenario truth.
3. It risks the "synthetic notation" bias that 669 §7 itself names.

**A better precedent already exists in this repository.** D1 (Research 490/491) encoded a **real ADS event** into V03 J1 effects with owner ACCEPT ("Development replay acceptance only", 491 header) and real J2 source facts (`accepted_j1.json`: 4 effects of types REQUIRE/PROHIBIT/AUTHORIZE/LIFECYCLE; `source_facts.json` binds real commits `73f54c6a`/`cd0cf087`). D2 holds REPLACE/REPARTITION/REINSTATE/CARRY_FORWARD lineage fixtures.

A **real-content V03 micro-migration slice** gives real document noise and real decisions together with authentic V03 truth semantics. It also rehearses R3/R4 (§5).

### 3.4 The real-history world in Option B tests a different question
Real history scored "only [on] propositions independently established by the permitted source evidence" (669 L85) would be navigation over **legacy-unreconciled** prose. That matters — it is the R3 inventory and transition problem, and V03 explicitly keeps a legacy-unreconciled boundary (502 §3). But it cannot discriminate additions *over the V03 substrate*. Placing it as a co-equal world with separate viability conditions would double the cost while answering a question the physical-target decision does not hinge on.

### 3.5 No decision-value analysis (Message 083 question A)
669 D0 (L96) asks for a decision table but never asks whether **any** B0–B4 outcome changes GOVERNED_LEDGER_KERNEL_V02.

**My hypothesis, testable in §6:**
- Every compared arm is additive and non-authoritative by contract (513 §6.10 forbids registries and authority leakage; 512 §10 places navigation in the derived plane).
- So the selection among B1–B4 is mostly an R1 extension-point question, of the same kind as the items 512 §21 (L693) deferred because they "have bounded adaptation points inside V0.2".
- What *must* be settled before R1 is the 512 §24 falsifier (L822): whether "relation-first substrate plus candidate navigation additions cannot match the best Research 217 behavior fairly". That is a sufficiency and safety question about the substrate.

### 3.6 Parity defects 669 does not name
- **Typed source relations dropped from every arm.** Route-B removed native typed references from B2 because they "belong to the substrate", yet B0 never received them (656 L30; B0 runner L262, L329). Every Route-B comparison therefore omits the repository's own governed reference grammars: Specification 025 `Declared references`, Specification 028 structured declarations, and header relationship fields (Message 064 S1, accepted in 649).
- **The cap was not neutral.** 669 does mention the 12,000-character cap (D3, L102). But it did not apply evenly:
  - B2 link extraction read full bodies (656 L40, which notes edge extraction "beyond B0's first-12,000-character search cap");
  - B1/B3 annotations were written from full-document knowledge.

  The cap therefore handicapped B0 relative to every metadata arm.

### 3.7 Twelve tasks cannot discriminate the 513 selection rule
**Arithmetic (reasoning, not a test result).** For a binomial pass count with n = 12 and p ≈ 0.8, the standard deviation is about 1.4 tasks. So 513's "+2 PASS" material-advantage rule (§6.11) sits about 1.4 SD from noise for a single run.

669 keeps n = 12 but never addresses power. A redesign should keep the 12 independent tasks as the formal gate and add a larger, **mechanically generated** suite to give the comparison statistical power. That is additive, not a relaxation.

### 3.8 The custody mechanism should be removed, not requalified
669 D5 (L106) keeps "a reference custodian accessible to reviewers but not arm authors". If **arms are frozen before tasks exist** — tasks generated or originated afterwards from a seeded generator or a fresh originator — then arm-side leakage is structurally impossible and no custodian is needed during arm authoring. Only a lightweight evaluator-side commitment remains: gold is hash-committed and published after outputs are committed.

This is 513's own purpose (no tuning to tasks) achieved by ordering instead of secrecy. It does change §6.5's literal order ("Before constructing/scoring B1-B4… freeze 12 primary tasks", L509–524), so it needs an owner amendment (§5.9).

### 3.9 Self-critique: Message 062 contributed to the loop
Research 559 adopted several of my F1–F11 recommendations as prerequisites:
- role-aware whole-system frames that include J2 realizers;
- task closure before build;
- independent annotators;
- closed per-arm worlds;
- run repetition.

Each was defensible on its own. Together, and without a decision-value budget, they compounded into the pre-score stall. In particular, F2 (include realizers and structured state) and F4 (use the source-declared substrate) assumed that a V03-native substrate could be extracted from real history. §2.2-1 shows it cannot. I withdraw that part of F4 as applied to pre-V03 history.

## 4. Comparative assessment of continuation designs

| Design | Tests the 513 question? | Independence / custody burden | Main bias risk | Value before R1 | Loop risk |
|---|---|---|---|---|---|
| **A** — repair the single historical world | **No** (no V03 substrate; §3.1) | High (custody, closure) | B0 degenerates to lexical-only | Low | **High** (C01/C02 evidence) |
| **B** — synthetic world + real world, separate viability | Yes in the synthetic world | High (scenario truth must be hidden; two worlds) | Synthetic notation favours a typed graph | Medium | Medium–high |
| **C** — real sources only, graded, plus invariant spot-checks | No (legacy prose) | Medium | Abstention can be gamed; no substrate | Low | Medium |
| **D** — exploratory only, bounded unresolved choice | n/a | None | Silent inheritance; never revisited | Depends on lock-in, which is untested | Low, but risks a hollow decision |
| **E** (new, recommended) — X1 lock-in/invariant probe first, then X2: a formal P03 on a real-content V03 micro-migration slice, with legacy periphery and commit-then-originate tasks | **Yes** (§5) | **Low** (no custody during arm authoring) | Encoding bias, mitigated by native-grammar extraction, a fresh audit and owner ratification of load-bearing effects | **High**: X1 decides lock-in; X2 decides family sufficiency and selection | **Low** (finite stops, §6) |
| **F** (complement) — prospective live-use sampling during R4 shadow | Yes, on the actual migrated system | Low | Late; possible sunk-cost bias toward B0 | None before R1 | Low |

**Why E beats B.**
- E keeps real content and real decisions, with V03 truth defined by the architecture's own semantics: owner-ratified J1 and natural-owner J2 from Git and CI receipts (the Research 654 method).
- E removes custody by ordering.
- E turns the legacy problem into a scored **zone** of one world rather than a second world.
- E produces R3/R4 rehearsal evidence as a by-product: encoding cost per effect is a direct data point for the 512 §24 falsifier "J2 RELATIONAL declarations create unsustainable authoring burden" and for the 512 §18 acceptance-volume input.

**Why E is not just D.** D defers selection without first establishing that deferral is safe. E's first step (X1) falsifies or confirms that premise. And X2 still runs the full 513 comparison, with its PASS / multiple-viable outcome semantics (513 §6.12, L624), so no outcome is waived.

## 5. Preferred experiment design ("P03-V2", a prospective proposal)

### 5.1 Decision decomposition
- **P03-F (family sufficiency and safety; required before R1).** Can the V03-native substrate plus lexical retrieval and derived orientation support whole-system tasks with:
  - zero false authority;
  - exact source and revision on authority answers;
  - no path-as-identity;
  - no index-as-truth;
  - no central membership registry;
  - safe deletion of the index (513 §6.10 invariants)?
  - **REOPEN** only if no arm can, without changing authority or substrate assumptions (513 §6.12).
- **P03-S (choice of additive navigation layers).** The 513 §6.11 selection among B1–B4.
  - It is decided by X2 if X2 yields PASS_WITH_SELECTION.
  - Otherwise it goes to the owner as the bounded choice 513 already provides for (PASS, MULTIPLE_VIABLE_ARMS).
  - The physical target ships the extension interface that X1 validates (R0-R54).

### 5.2 Scientific unit
One **task run**: (arm, task, run index), executed by a fresh agent inside that arm's closed snapshot under an identical tool and context budget. Each run yields:
- a cited answer;
- an assertion set, each item labelled ASSERTED / NOT_FOUND_IN_COVERED_SCOPE / UNKNOWN_IN_WORLD;
- a resource trace.

Pre-register three runs per task, with majority aggregation (as Research 559 F11 already anticipated).

### 5.3 World
A **real-content V03 micro-migration slice** with two zones.

**Core zone.** A bounded, coherent real program encoded into V03 J1/J2/J3.
- **Recommended candidate:** the Specification 028 / D-035 PKA implementation slice at a pinned revision. It has normative requirements, real code (`tools/project_knowledge/…`), real tests (Research 668 ran 103/103 authority tests), provider CI runs (Research 654 method), generated views, the D-036 successor selection while Specification 028 stays operational, and a real unaccepted proposal (Research 254).
- **Why this slice:** it spans all four 513 task families, including cross-plane realizers and authority/recovery. It also overlaps Research 668's verified chain, which can be reused as an encoding seed.
- **J1 encoding:**
  - Only from source-declared facts, using the repository's own grammars (DECISIONS status and supersession, Specification 025 typed references, Specification 028 declarations, header relationship fields).
  - Every effect is labelled `MIGRATION_CANDIDATE_J1`.
  - The owner ratifies the load-bearing effects (on the order of ≤ 30) by chat confirmation under Research 555 §2A, as D1/491 did. The ratification count and time are themselves data.
- **J2:** OBSERVABLE facts from Git objects and provider run, job and step records (Research 654's evidence ladder), plus explicit natural-owner REALIZES declarations written as experiment carriers and labelled `SYNTHETIC_V03_ANALOGUE`. Nothing is inferred (512 L298).

**Legacy periphery zone.** Real unencoded prose carriers from the same period, labelled LEGACY_UNRECONCILED (502 §3). Here UNKNOWN is the correct gold for operative claims.

**Size.** Toward the 513 target of 60 build plus 20 held-out carriers (§6.7). Held-out carriers are drawn by commit-then-draw from the slice frontier after arms freeze.

**Exclusions.** The P03 design lineage (Research 556+, Messages 061+), as already accepted in Research 559 F5/F7.

### 5.4 Common substrate (all arms, identical digest)
Per Research 513 §6.2:
- encoded J1 effects and identities;
- lineage and currentness;
- completion and J2 coverage;
- evidence/receipt relations;
- authority-class labels;
- documentary declared relations from native grammars, as a separate non-J1 class (correcting the §3.6 parity defect);
- the derived connector-readable orientation (512 §11).

**Strong shared lexical baseline, fixed before any task exists:**
- full-text passage-chunked BM25 with standard k1/b defaults and a fixed chunk and overlap size;
- heading boosting;
- exact identifier lookup (`D-036`, `Research 512`, effect IDs);
- no 12,000-character body cap.

### 5.5 Arm differences (513 §6.3 retained)
- **B1:** the Research 217 vocabulary, allowed controlled prospective evolution under an equal authoring budget (Research 559 F9), with source-owned memberships.
- **B2:** carrier-declared editorial `about` links beyond the substrate's documentary relations. If none survive the collapse rule, that is a finding.
- **B3:** selective concern declarations, with a pre-frozen distinctness rule against B1.
- **B4:** semantic retrieval over the structured parent chosen by a pre-score rule: the X1-conformant structured arm with the lowest measured authoring cost.
  - It needs a pinned neural model whose availability is **verified in the actual execution environment before freeze**; Research 657 recorded egress denial for PyPI.
  - If it is unavailable, B4 is omitted before any score with a disclosed family-coverage limitation (513 L482).

Authoring cost is measured in minutes and bytes, and is recorded per arm.

### 5.6 Task and reference origination, in this order
1. Freeze the slice and substrate.
2. Arm authors (exposure allowed) write and freeze all arm metadata. The freeze commit is C_arm.
3. **Tasks are created after C_arm.** Two streams:
   - **(a) Formal 12** (3 per 513 family). A fresh session sees only the slice's topic index, not the arm files, and originates needs. Wide "enumerate everything" needs are allowed, but gold may be partial or UNKNOWN.
   - **(b) Generated power suite** (e.g. 48–96 tasks). A deterministic generator over the encoded graph, seeded by `SHA-256(C_arm ‖ coordinator ack commit)`. Families: what governs X now, what changed when Y superseded, what realizes Z and is its evidence fresh, what is impacted if E is amended, plus negative and contradictory-ID controls (the Research 651/652 templates). Wording is produced by a fresh session from fact cards.
4. **Gold:**
   - for (b), mechanical from the encoded world;
   - for (a), relative to sources and substrate, written by a separate fresh reviewer blind to the arms, with claim-level support (Research 666 method) and UNKNOWN as legitimate gold.
   - Gold is hash-committed before runs and published after outputs are committed.
5. **Legacy 9:** Research 559 Option A, unchanged, in the historical 65-carrier world as a separate regression packet, adjudicated by a fresh session (≤ 9 needs, ≤ 65 documents).

### 5.7 Evaluation and held-out handling
- Two scorers where judgment is needed, preferably from **two model families**, because Research 660 noted the same-family limitation.
- Mechanical scoring takes precedence for citations, revisions and authority classes.
- Held-out maintenance F1 uses the arm's frozen rules applied by a maintainer, scored against a fresh reference annotator.
- Churn is measured mechanically.

### 5.8 Quantitative rules
- **Retained unchanged** (513 §6.10–6.12):
  - ≥ 10/12 formal tasks;
  - ≥ 8/9 neutral legacy, or N/A frozen in advance;
  - zero false authority across **all** runs, both streams and both zones;
  - held-out F1 ≥ 0.80;
  - churn ≤ 10%;
  - safety on index deletion;
  - the complexity-preference rule.
- **Added (reporting only, no new pass gate except false authority):**
  - per-zone coverage, defined as the fraction of gold propositions answered correctly;
  - abstention appropriateness, defined as abstaining exactly where gold is UNKNOWN;
  - power-suite top-k and answer accuracy with confidence intervals.

  Trivial abstention therefore scores badly on coverage and cannot pass.

### 5.9 Prospective governing changes needed (owner decision; nothing implied)
1. Redefine the P03 world as the real-content V03 micro-migration slice with a legacy zone (amends 513 §6.7 corpus semantics).
2. Commit-then-originate task order (amends the §6.5 sequence; purpose preserved).
3. Gold relative to sources and substrate, with UNKNOWN as valid. This supersedes the "complete original question scope" reference standard (Research 641) and 576 §2.1's "complete source/authority closure" for P03-V2.
4. Add the generated power suite (additive).
5. Treat X1's invariant results as pre-score structural findings: an arm that intrinsically violates a 513 §6.10 invariant is eliminated before scoring, with the reason recorded.
6. Explicit fallback to an R0-R54 bounded unresolved interface if X2 cannot be admitted within its bound (§6.3).

### 5.10 Physical, logical and process evolution (Message 083 question I)
- **V03 logical substrate:** no P03 evidence falsifies it, and the HOLDs fit its premise. Keep.
- **V02 physical candidate — candidate items for AMEND/CLARIFY:**
  - an explicit navigation extension interface (namespaced optional source declarations, a validator plug-in port, a derived-index provider port; R0-R54);
  - references bound to identity, including fragments (`DECISION:D-035`; Message 064 S3);
  - a mapping of native declared-reference grammars into the substrate as a documentary relation class;
  - CLARIFY whether scoped governance delegation needs a consequence form. Specification 028's REPLACE/SUPPLEMENT/SPECIALIZE/CORRECT cannot express `CONTINUITY.md` L377 (Message 064 S7).
  - The 331-checkpoint generated-view lag in Research 668 supports keeping 512 §11's freshness service level.
- **Experiment process (an AO-4 evolution input, not a target change):** every pre-score prerequisite carries a decision-value statement and a time-boxed stop rule. The P03 history (§1.2, §2.2-5) is the triggering evidence.

## 6. First finite step and stop conditions

### 6.1 X1: navigation-extension conformance and lock-in probe
**Purpose.** Falsify my central premise that B1–B4 are additive extensions whose selection does not change the V02 family. At the same time, mechanically execute the 513 §6.10 invariant gates that need no task gold.

**Inputs (exact provenance).**
- `c418d62f`.
- Contract: Research 512 §§9–11, 17, 23 and 513 §6.10.
- V03-native mini-world:
  - `experiments/ao10_hybrid_d1_replay_v01/{accepted_j1.json,source_facts.json,definitions.json}`;
  - `experiments/ao10_hybrid_d2_lineage_v01/reviewer_fixtures.json` (REPLACE ×6, REPARTITION ×5, REINSTATE ×2, CARRY_FORWARD ×1; observed);
  - at most 20 added synthetic carriers labelled as such.
- Arm prototypes: the existing Route-B code, reused as mechanisms only. Exposed Route-B metadata and results are not imported:
  - B1/B2/B3 from `route_b_distinct_b1_b2_b3_navigation_comparison_v01.py`;
  - for B4, any dense provider (classical LSA suffices to test the interface, not quality).

**Checks per arm (all mechanical, no gold):**
1. **Kernel non-interference:** the J3 and orientation digest is identical with and without the arm's metadata and plug-in.
2. **Authority isolation:** injection of authority, currentness or effect fields is rejected (reusing the Research 667 negative controls).
3. **Deletion and rebuild:** deleting the derived index degrades discovery only, and the rebuilt digest is equal.
4. **Identity:** renaming or relocating a carrier preserves arm metadata bound to identity; any path binding fails.
5. **Lineage coupling:** after SPLIT/MERGE/REPLACE/RETIRE/REINSTATE of a target effect, links and memberships are either rebound through the kernel's lineage API or surfaced as REVIEW_REQUIRED. They are never silently stale.
6. **Vocabulary governance:** does evolving B1/B3 vocabulary need a new J1 consequence type or a new governance path, or does it fit existing AO-4/J1 governance?
7. **Growth churn:** add 10 carriers under the frozen authoring rule and measure the share of pre-existing authored metadata that changes.

**Output.** Each arm is classified as one of:
- `ADDITIVE_EXTENSION`;
- `REQUIRES_R1_HOOK` (with the named hook);
- `REQUIRES_KERNEL_OR_J1_CHANGE`;
- `INTRINSIC_INVARIANT_VIOLATION`.

Plus the R1 hook list, a JSON result and a source-free report.

**Isolation and authority.** Unscored Level C engineering under Research 576. No tasks, gold, protected material or private files. Results are architecture-conformance facts that any party can reproduce. They are not scores.

### 6.2 How X1 changes the decision, and its stop rule
| X1 outcome | Consequence |
|---|---|
| All arms are ADDITIVE or REQUIRES_R1_HOOK | My premise survives. The hooks become R1 obligations. Proceed to X2 (P03-V2) under the §5.9 amendments. |
| Any arm is REQUIRES_KERNEL_OR_J1_CHANGE | **My premise is falsified for that arm.** Its merit becomes pre-R1-critical, and X2 must score it against B0 before any target package. Flag a V02 AMEND candidate. |
| Any arm shows an INTRINSIC_INVARIANT_VIOLATION | That arm is a structural REOPEN/eliminate candidate, decided by the owner. If every arm including B0 fails an invariant, P03-F is REOPEN-relevant. |
| X1 is inconclusive (the fixtures cannot express a check) | Stop. Report which check, and do not extend X1 beyond its fixed scope (one pass, at most about two working sessions). |

### 6.3 X2 admission bound
- X2 gets **one** admission attempt for slice encoding, owner ratification, fresh originator and reviewer, and two-family scorers. Bound: **at most 10 working sessions** before any run.
- If admission fails, return a specific HOLD and the R0-R54 fallback for P03-S: a bounded unresolved interface validated by X1, with selection deferred to option F (R4 shadow), under explicit owner disposition. P03-F's invariant results from X1 stay as the minimum pre-R1 evidence.
- No new cohort is started automatically, and no gate is relaxed.

## 7. Verdict

**PROPOSE_PROSPECTIVE_AMENDMENT.**

**Conditions.**
- Keep the 513 §6.10 invariants, the arm definitions, the ≥ 10/12, ≥ 8/9, zero-false-authority, F1 and churn gates, and the complexity rule.
- Keep Research 559 Option A and the Research 576 Level B roles.
- Amend only world semantics, task order, gold semantics and an additive power suite (§5.9). Each needs explicit owner acceptance.
- Run X1 first; it can falsify the basis of the amendment.

**Why not the other verdicts.**
- **Not KEEP_513_WITH_BOUNDED_REPAIR:** the stated question cannot be tested in any pre-V03 world (§2.2-1).
- **Not REOPEN_P03_EXPERIMENT_DESIGN:** the arms, gates and decision classes stay valid; only the world and its ordering are defective.
- **Not DEFER_P03:** deferral without X1 would leave the lock-in question untested, and would let exposed exploratory results gain de facto weight.

**Risks of redesign, taken seriously.**
- It can look like moving the goalposts after repeated failure. Mitigation: no exploratory score is imported, every gate is kept, and the amendment is justified by pre-score structural evidence.
- Encoding bias toward typed relations. Mitigation: native-grammar-only encoding, a fresh audit, a legacy zone and owner ratification.
- Owner ratification burden.
- A generated suite can overweight graph-shaped questions. Mitigation: the formal 12 come from a fresh originator, not the generator.
- Hooks may be underspecified, and B1's historical strengths could be lost if B1 is under-resourced. Mitigation: B1 gets an equal budget and controlled evolution.

**Risks of continuing the old design.** Indefinite HOLD cycles (C01, C02, the four-need pilot), custody engineering, decision by exhaustion, and exposed Route-B results drifting into informal preference.

**Remaining uncertainty.** Whether a meaningful slice can be encoded at acceptable cost (unmeasured). Whether a neural B4 can actually run in the execution environment. Whether fresh two-family scorers can be arranged. Whether the owner accepts ratifying about 30 effects.

**What would reverse my conclusion.**
- X1 finds any arm REQUIRES_KERNEL_OR_J1_CHANGE. Then P03-S is pre-R1-critical, and I would shift toward a fuller B0–B4 scoring before target selection, accepting higher cost.
- Slice encoding proves infeasible without inference forbidden by 512 L298. Then the V03 substrate itself has an authoring-burden problem, which is a 512 §24 falsifier and should trigger V02 AMEND before P03.
- A pilot of the legacy zone shows that navigation outcomes there diverge sharply from the core. Then the legacy-heavy R4/R5 transition period should drive the selection, and option C-style real-history evaluation deserves co-equal weight.

```text
REQUEST=MC0030_MESSAGE083
REPLY=MC0030_MESSAGE084
REVIEW=EXPOSED_ADVERSARIAL_METHODOLOGY_NOT_SCORED
VERDICT=PROPOSE_PROSPECTIVE_AMENDMENT
PRIMARY_BLOCKER=V03_NATIVE_SUBSTRATE_ABSENT_FROM_ALL_PRE_V03_WORLDS
SECONDARY_BLOCKER=REFERENCE_GOLD_DEFINED_AS_HISTORICAL_WORLD_TRUTH
PROCESS_DEFECT=PRE_SCORE_PREREQUISITE_ACCRETION_WITHOUT_DECISION_VALUE_BUDGET
RESEARCH_669=DIRECTIONALLY_RIGHT_UNDERSTATES_MISMATCH_OPTION_B_CONSTRUCTION_REJECTED
PREFERRED=E_X1_LOCKIN_PROBE_THEN_P03V2_REAL_CONTENT_V03_SLICE_COMMIT_THEN_ORIGINATE
FIRST_STEP=X1_NAVIGATION_EXTENSION_CONFORMANCE_NO_GOLD_LEVEL_C
513_GATES=RETAINED
OWNER_DECISION_REQUIRED=WORLD_TASK_ORDER_GOLD_SEMANTICS_POWER_SUITE
SELF_CRITIQUE=MESSAGE062_F4_WITHDRAWN_FOR_PRE_V03_HISTORY
V03_LOGICAL=KEEP
V02_PHYSICAL=CANDIDATE_AMEND_NAVIGATION_EXTENSION_INTERFACE_IDENTITY_REFERENCES
PHYSICAL_TARGET_SELECTED=false
FORMAL_P03_COMPLETE=false
PROTOCOL_CHANGE_AUTHORIZED=false
```
