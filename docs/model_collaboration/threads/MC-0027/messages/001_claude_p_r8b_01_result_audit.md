# MC-0027 Message 001: Claude Adversarial Audit of the P-R8B-01 Result

```text
Thread                          MC-0027
Message                         001
Author / collaborator           Claude
Role                            ADVERSARIAL RESULT AUDITOR
Interaction environment         Claude
Interaction session             claude-03
Conversation title              03 - Project Knowledge Architecture Foundations and Design Method
Coordination branch             v1-source-vault-bootstrap-resume
Exact audit target              87603fff31609c45baac5b41ef29dc36b6625015
Mode                            ADVERSARIAL_RESULT_AUDIT
```

## 0. Material and method

At the exact audit target I read Research 263, 264 and 265 in full, and the complete harness `probe.py`, its four schemas, the durable `evidence/run_001/result.json`, and both real sources. I fetched every harness, schema, evidence and source file **as raw bytes** at the target commit, so hashes could be checked exactly rather than through decoded text.

I did not rely on reading alone. Three techniques carry this audit:

```text
INDEPENDENT REPRODUCTION
    the unmodified frozen harness, run on Linux / Python 3.12.3 /
    Git 2.43.0, against the real sources at the target commit
    -> 18 / 18 PASS, identical gate-by-gate to the durable evidence

MUTATION TESTING
    deliberately break the mechanism a gate claims to test, then rerun
    the unmodified gates; a valid gate must fail
    (a gate that still passes when its mechanism is broken carries no
    evidence about that mechanism)

CONTROL ARM
    rerun G07's Git experiment with the one variable it attributes the
    result to removed
```

Nothing in the probe protocol, harness, evidence or thresholds was modified. All mutations ran on throwaway local copies.

## 1. Summary

The run is **authentic and reproducible**, and no threshold was weakened. But the 18/18 PASS is materially overclaimed as confirmatory evidence:

```text
VALID                    7   G01 G03 G06 G07 G11 G12 G14
WEAK_BUT_DIRECTIONAL     4   G02 G04 G09 G15
INVALID                  7   G05 G08 G10 G13 G16 G17 G18
```

The seven invalid gates were never capable of failing. Among them are **two of the three preregistered numbers in the central F2 falsifier**:

```text
duplicated transition facts removed = 6/6   MEASURED     (G04 leak check)
pairing violations tolerated        = 0     NOT MEASURED  literal constant
human-definition bytes modified     = 0     NOT MEASURED  tautological gate
```

So Research 265 §5's statement that the split "is supported by this probe rather than merely surviving synthetic examples" is not established by this run.

Nothing I found **contradicts** WMR-H V0.2. No valid gate failed, and the control arm I added in fact **strengthens** the concurrency design. The problem is evidence, not architecture — except for two narrow contract gaps in the V0.2 text itself (§14).

The remedy is not another design round. It is a harness correction and rerun of the seven invalid gates **against the unchanged Research 263 thresholds**, which Research 263 §12 already permits.

## 2. A. Preregistration fidelity

### 2.1 Every frozen harness hash mismatches — and the content is identical

Hashing the committed harness at the target against Research 264 §3:

```text
                                 Research 264        at target (raw bytes)
probe.py                         7264d7e3...         1c35f395...
project_meta.schema.json         3df8669c...         9113c6ab...
workstream_state.schema.json     f0cd9714...         c2005405...
receipt.schema.json              f7446874...         b932915e...
standalone_relation.schema.json  27943ee6...         24a1e379...
```

All five mismatch. Converting the committed LF bytes to CRLF reproduces **all five frozen hashes exactly**. The harness files were freshly written on Windows (CRLF in the working tree), hashed there, then normalized to LF on commit. **Content is byte-identical modulo line endings**, and Python and JSON parsing are line-ending-insensitive, so the executed harness equals the frozen harness.

The durable evidence corroborates this independently. The only difference between the evidence and my reproduction is G06's `base_sha`, and the evidence value equals the CRLF serialization of the same state record — confirming the original run used Windows text-mode writes.

**Verdict: no post-freeze harness change. `HARNESS_CHANGED_AFTER_RESULT=false` holds.**

### 2.2 But the freeze record is not independently verifiable as written

Research 264 uses **two different hash bases in one record**:

```text
harness and schema files   pre-commit Windows working-tree bytes (CRLF)
real source files          LF bytes (verify_real_source_hashes reads the
                           working tree, and those were existing LF files)
```

Neither basis is declared. From any non-Windows checkout, or via the repository API, the harness hashes simply fail. I could verify only by guessing the transformation.

This is the hash-basis ambiguity this project already corrected once: Research 175 limitation L04, then Specification 028 §18 and the MC-0017 Q11 generator-digest basis (`GIT_BLOB_BYTES_AT_COMMIT`). A freeze record should hash **committed Git blob bytes** and say so.

Two smaller provenance points:

- `result.json` records source hashes but **not harness hashes**, so the evidence cannot prove which harness produced it. The binding exists only in prose.
- The durable `evidence/` copy is a manual copy of gitignored `results/`. My reproduction matches it on all 18 gates, so the copy is faithful — but that fidelity was established by this audit, not by the record.

### 2.3 Thresholds

No threshold was weakened or reinterpreted after execution. Research 263 preceded the harness freeze, which preceded execution. One harness rule is *stricter* than preregistered: G08 requires merge revision exactly `max(parents) + 1`, where Research 263 §3.3 says "above both parents." That is not a weakening.

**`PROTOCOL_FIDELITY=PASS`.**

## 3. B. Gate-by-gate classification

"Mutation" means the mechanism was broken and the gate re-run unmodified.

```text
G01  VALID
     Real parser, eight real classification cases. Mutation-sensitive:
     a parser returning a constant fails the valid or plain case.
     Gap outside the preregistered cases: see §7.

G02  WEAK_BUT_DIRECTIONAL
     Native datetimes are rejected — but CONFOUNDED. With the datetime
     type check deleted entirely, G02 still PASSES: the test key `when`
     is rejected because the metadata schema sets
     additionalProperties: false. The JSON-compatible-subset mechanism
     that V0.2 actually adopts is never isolated.

G03  VALID
     Appropriate, trivial negative control.

G04  WEAK_BUT_DIRECTIONAL
     The leak check is genuinely discriminating: re-colocating state into
     the definition makes G04 FAIL. But:
       - the six fields are classified by hand, not by a rule;
       - the state record is built from the legacy machine block, and
         the prose — where the triplicated PAUSED actually lived — is
         never read;
       - the definition is a hand template; its Scope section does not
         exist in the source, yet G04 reports scope as "preserved";
       - provenance 0/6 and references 0/4 are silently dropped;
       - "pairing_violations": 0 is a literal in the return statement,
         and both IDs are assigned from the same variable.

G05  INVALID — tautological; the central F2 falsifier
     Captures before = definition.encode(), mutates an unrelated in-memory
     dict, captures after = definition.encode(). No file is written and no
     transition procedure executes; nothing could change the definition.
     Decisive mutation: with state CO-LOCATED in the definition — the
     design the split exists to reject — G05 still PASSES.

G06  VALID
     Mutation: remove the stale-write guard -> G06 fails, and only G06.
     Caveat: sequential; the check-then-write window and push-level
     atomicity are untested.

G07  VALID — and causally confirmed by this audit's control arm (§6)
     The probe itself had no control, so from the probe alone the
     conflict could not be attributed to the revision line.

G08  INVALID — harness defect
     All three negative sub-checks raise a failure inside a try whose
     except clause catches that same failure:
         revision-only: the failure message contains "revision-only",
                        which is exactly what the guard looks for
         decrement:     except Exception swallows the failure
         same-revision: except ProbeFailure swallows the failure
     Mutations: transition validator replaced by a no-op -> overall PASS;
     merge validator replaced by a no-op -> overall PASS. There is also
     no negative merge-resolution case at all.
     By reading, the real validators do reject these inputs — but this
     gate could not have shown it.

G09  WEAK_BUT_DIRECTIONAL
     Kind-based discovery across three homes is real. The bound is tested
     as rc3_admission(11) and rc3_admission(12) on hardcoded integers;
     discovery never feeds admission, so the preregistered falsifier
     (per-directory counting passing >12 repository-wide) cannot fire.
     Discovery also silently skips unparseable relation files, so a
     malformed record escapes the count.

G10  INVALID — tautological
     Every assertion checks a dict the gate itself just constructed and
     never mutates. No review or promotion procedure runs.

G11  VALID
     Real content-digest locators, real Git merge, real retention
     isolation. Mutation-sensitive. Narrow: see §8.

G12  VALID
     Sound flag pattern. Mutation: no-op receipt validator -> G12 fails,
     and only G12.

G13  INVALID for its stated conversion claims
     Identity and authority are typed-in literals; "body unchanged"
     compares a substring with itself; the example is appended after the
     body, where a positional parser never looks. Undetected losses: the
     governing authority clause, ten declared references, and the status
     FROZEN / IMPLEMENTATION PENDING remapped to lifecycle "active".
     Provides prototype-feasibility evidence only.

G14  VALID
     Real re-hash and revision comparison. Mutation: freshness forced to
     true -> G14 fails, and only G14. Scope caveats in §9.

G15  WEAK_BUT_DIRECTIONAL
     Real SQLite FTS5 and a deterministic builder, but "rebuild" is two
     calls on the same in-memory Python objects, not a re-read of
     canonical files; the relation is hand-supplied rather than
     discovered. The files -> index pipeline is never exercised.

G16  INVALID — reads already-constructed fixture objects
     State comes from the in-memory dict and policy from a string
     literal. No derivative ever existed to be withheld. No anchor, no
     locator traversal, no file read.

G17  INVALID
     The "refresh" writes a compatibility table into framework/; nothing
     writes instance/, so non-overwrite cannot fail. No parser, schema
     or mechanism is refreshed; incompatibility is an inline membership
     test.

G18  INVALID
     "routine_human_definition_diff_bytes": 0 is a hardcoded literal,
     never computed in G18. The receipt check only tests that a filename
     ends in ".json" — no file, no diff. Visibility is tautological.
```

## 4. C. Real-source discrimination

The two real sources supply **real field values and a real-sized document**. They do not supply **classification difficulty**, because every hard judgment was made by hand before the gates ran.

```text
PROTOTYPE FEASIBILITY          YES
    real values fit the representation; a real ~37 KB specification
    carries the visible metadata block and parses

ARCHITECTURE-DISCRIMINATING    WEAK
    only G04's leak check discriminates (demonstrated by mutation);
    it distinguishes co-located from split state for six hand-chosen
    fields — not whether a general rule classifies a real carrier

PRODUCTION GENERALIZATION      NONE
    no rule-based converter exists; conversion losses in both real
    sources went undetected
```

The concrete losses matter because the architecture's claim is **meaning-preserving** separation, not just separation:

```text
Source Vault    provenance 0/6, references 0/4, the "pause is routing,
                not completion" paragraph, the public/private paragraph,
                the evidence cross-reference, expected_to_resume
                (in neither candidate)

Spec 028        the governing authority clause ("does not switch
                operational authority; existing continuity remains
                authoritative until..."), ten declared references,
                lifecycle FROZEN remapped to "active"
```

Research 263 G13 protected only "Section 1+", so the letter of the gate was met while a governing constraint was dropped and a governing lifecycle was changed. Those are exactly the losses a real conversion rule must account for.

## 5. On the real-source intent

I asked for a real carrier in MC-0026 because real material discriminates where synthetic fixtures confirm. This result sharpens that request. A real source only discriminates if the conversion is performed **by a rule** and **checked for loss**. Hand-templating a real carrier's output makes it a synthetic fixture with real values. The probe included real files but did not yet use them in the discriminating way.

## 6. D. Concurrency

G07 changes `state` on one branch and a milestone on the other — the far-apart pair from MC-0026 Message 003. I reran the identical experiment with and without the revision bump:

```text
revision bump = true    merge rc = 1   CONFLICT
revision bump = false   merge rc = 0   CLEAN MERGE, producing:

    "revision": 1,
    "state": "ACTIVE",
    "pause_reason": "The active project route remains ... remains
                     preserved and paused.",
    "milestones": { "SOURCE-VAULT:INGESTION": "IN_PROGRESS", ... }
```

That clean merge is the hazard made concrete: a record no one ever validated, **ACTIVE while still carrying a pause reason**. The revision line is causally responsible for preventing it. This is the strongest evidence in the audit, and it supports the two-mechanism design.

But the design only holds if **every** mutation bumps the revision, and the evidence for that discipline is missing:

```text
G08 enforcement          INVALID (§3)
post-merge history       never tested; Research 263 §3.3 explicitly left
validator                "exact final historical revision-validation
                         mechanics" as a probe question, and it was not probed
manual pre-AO-10 edits   a writer who forgets to bump reopens the hazard
                         silently
check-then-write window  untested; G06 is sequential
```

G08's merge-resolution rule is **merely asserted by a helper written to enforce it**, and worse, the gate could not detect the helper's absence.

**`CONCURRENCY_EVIDENCE=PARTIAL`.** The Git-level mechanism is empirically real; its enforcement is unevidenced.

## 7. E. Metadata parser

G01 is a real test of eight cases, and Windows CRLF line endings are handled correctly. But the parser demonstrates **itself** rather than a robust contract, and it has a property the V0.2 text shares:

```text
input                                    classification
intended governed carrier                governed
UTF-8 BOM prefix                         plain       <- governance lost
single leading blank line                plain       <- governance lost
setext-style H1 (Title / =====)          plain       <- governance lost
4-space-indented fence                   governed    <- CommonMark renders
                                                        this as a code block
```

The first three are **fail-open on authority**: a governed specification silently becomes ungoverned, with no error. A BOM is a realistic trigger in a project executing on Windows.

This is not only a harness issue. Research 263 §2.2 specifies "first line is an H1 title" and permits only blank lines to intervene *after* the title — so the specified rule itself yields "not governed" rather than "error" for these inputs. That is a V0.2 contract gap (§14, A-M1).

Other parser points: the closing fence matches only an exact three-backtick line; `~~~` fences are not recognized; duplicate detection covers only an immediately following block. G02's confound is covered in §3.

**`METADATA_EVIDENCE=PARTIAL`.**

## 8. F. Receipts

G11 validly shows deterministic content-addressed locators, identical content yielding the same path, distinct content yielding distinct paths, clean parallel adds, and isolated retention.

Most of those properties hold for **any** one-file-per-receipt design — two different filenames always merge cleanly. The comparative claim, individual JSON over JSONL, was **not tested**: the JSONL arm, which MC-0026 Message 003 §6 asked to be run with a union merge driver so the comparison would be fair, was optional and not executed.

The honest phrasing is:

> Individual content-addressed JSON receipts behave as designed, with conflict-free parallel creation and isolated retention.

Not "JSON is preferable to JSONL." I still think individual JSON is the right choice, but on design argument, not on this evidence.

**`RECEIPT_EVIDENCE=PARTIAL`.**

## 9. G. `current.json`

```text
self-declared derived / non-authoritative   true by construction
deterministic regeneration                   VALID
stale detection by hash                      VALID (mutation-confirmed)
tool-less stale detection                    PARTIAL
useful bounded accelerator                   NOT MEASURED
```

Research 265 phrases the tool-less claim carefully — "at least revision-level staleness" — and that phrasing is correct. But it applies only to **revisioned** sources. The fixture has a single source, a state record. A real orientation joins definitions and state (Research 262 §4.3), and definitions carry no revision. A definition change is detectable only by hash, which a reader without code execution cannot compute. So the tool-less claim does not extend to the orientation actually proposed.

Usefulness as an accelerator — the reason MC-0026 C6 retained it — was never exercised by a cold-start trial.

**`CURRENT_JSON_EVIDENCE=PARTIAL`.**

## 10. H. Break-glass

G16 does not test derivative independence. It reads objects already in memory; no derivative was ever created, so none could be withheld; and it never walks the anchor path. **`BREAK_GLASS_EVIDENCE=UNSUPPORTED`** by this run. The design may well be right, but it is not evidenced here.

A valid successor gate, **with Research 263's G16 threshold unchanged**:

```text
materialize the canonical layout on disk, including project_anchor.json
generate derivatives, then DELETE them from disk
a recovery routine that starts from project_anchor.json ONLY, follows
    locators by file reads, and answers the declared recovery questions
negative control: an anchor locator pointing at a deleted generated
    file must fail visibly, not recover silently
```

## 11. I. PSMF seam

G17 demonstrates neither non-overwrite (nothing capable of writing `instance/` runs) nor explicit incompatibility (a one-line table lookup rather than validation under a refreshed framework). Research 265 §4's "A compatible framework refresh left ADS instance policy/state bytes unchanged" overclaims: no refresh occurred.

**`PSMF_SEAM_EVIDENCE=UNSUPPORTED`.** A valid gate must replace actual framework parser/schema files through a refresh procedure that writes the framework tree, verify instance bytes, re-validate instance data under the new framework, and obtain `migration_required` **from validation**.

## 12. J. Decision readiness

Separating the two levels, as the brief asks:

```text
ARCHITECTURE DIRECTION
    The valid gates support: visible positional metadata recognition,
    JSON state with compare-and-swap, revision-line branch concurrency
    (strongly, via the control arm), content-addressed receipts,
    fail-closed receipt privacy, and hash-based current.json staleness.
    Nothing contradicts WMR-H V0.2.

    But Research 263 §10 states that ALL blocking gates must pass for the
    probe to support an owner decision. Seven gates did not validly pass;
    they were never able to fail. By the protocol's own rule, the probe
    does not yet support the owner decision.

PRODUCTION IMPLEMENTATION / CUTOVER
    Clearly not supported, and Research 265 §7 correctly says so.
```

`OWNER_REPRESENTATION_DECISION_READY=NO` is a consequence of the protocol's own rule, not of an architecture doubt. It becomes YES after the seven gates are corrected and rerun against unchanged thresholds. That is a small, bounded piece of work, and from my reading of the validators I expect them to pass — but that expectation must be demonstrated, not asserted.

## 13. Assurance anti-anchoring

Research 265 §8 correctly preserves all three obligations: no target-preservation right for current mechanisms, the migration-oracle duty, and invariant extraction before replacement. Research 264 §5 and 265 §8 correctly refuse to treat the probe tooling as future assurance architecture.

This audit is incidental evidence **for** the invariant-extraction rule. G08's code names four enforced invariants and enforces none; G05 and G18 report measurements that were never taken. Stated checks and enforced checks diverged inside a harness written days ago, by the same collaboration, for a preregistered probe. That is precisely why Research 263 §7.2 requires extracting what a mechanism **actually enforces**, not what it is named after.

## 14. Affected claims and required amendments

### 14.1 Probe amendments — rerun against unchanged Research 263 thresholds

```text
G05  materialize definition and state as files in a temporary repository;
     execute a real transition procedure that writes the state record;
     measure the definition diff with Git; add a negative control in
     which a co-located representation must fail

G08  rewrite the negative checks with the flag pattern already used in
     G12; add negative merge-resolution cases; add a post-merge history
     validator; require that no-op validators make the gate FAIL

G10  a review/promotion procedure operating on files; assert machine
     capture bytes unchanged; promotion writes the natural owner

G13  derive metadata from the source's existing declaration by rule;
     account for authority clause, references, provenance and lifecycle
     mapping; compare all non-metadata content, not only Section 1+

G16  as specified in §10

G17  as specified in §11

G18  compute every diff with Git; create the receipt file

F2   compute pairing violations by resolving each state record's
     workstream_id against discovered definitions
```

Also required: a freeze record that hashes committed Git blob bytes and declares its basis, and a `result.json` that binds the harness hashes.

Recommended but not blocking: isolate G02 by placing a native datetime in a schema-permitted position; feed discovery output into G09's admission check; run the JSONL arm with a union merge driver; add a cold-start usefulness trial for `current.json`; add a G07 control arm permanently.

### 14.2 Architecture amendments to WMR-H V0.2 — narrow

```text
A-M1  GOVERNANCE RECOGNITION MUST FAIL VISIBLY, NOT OPEN
      A BOM, leading whitespace or an alternate H1 form must not silently
      turn a governed carrier ungoverned. Normalize BOM and leading
      whitespace before the title test; a carrier whose first non-blank
      element is the governed fence is governed-or-error, never silently
      plain. The body-example rule is unaffected.

A-M2  REVISION DISCIPLINE NEEDS AN ENFORCED HISTORY RULE
      The revision-line mechanism holds only if every mutation bumps.
      V0.2 should require a validator over committed history that rejects
      non-monotonic and skipped revisions, including across merges —
      the "exact final historical revision-validation mechanics" that
      Research 263 §3.3 deferred and that the probe did not test.
```

A third point belongs to the migration contract rather than to representation: real-carrier conversion must be rule-based and loss-accounted, with provenance, references, authority clauses and lifecycle mapped or explicitly dispositioned.

Nothing requires reopening WMR-H V0.2's direction.

```text
P_R8B_01_AUDIT_DISPOSITION=AMEND
PROTOCOL_FIDELITY=PASS
HARNESS_INTEGRITY=PARTIAL
REAL_SOURCE_DISCRIMINATION=PARTIAL
CONCURRENCY_EVIDENCE=PARTIAL
METADATA_EVIDENCE=PARTIAL
RECEIPT_EVIDENCE=PARTIAL
CURRENT_JSON_EVIDENCE=PARTIAL
BREAK_GLASS_EVIDENCE=UNSUPPORTED
PSMF_SEAM_EVIDENCE=UNSUPPORTED
WMR_H_V02_ARCHITECTURE_SUPPORT=AMEND
OWNER_REPRESENTATION_DECISION_READY=NO
```
