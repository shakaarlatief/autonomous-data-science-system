from pathlib import Path
import json
import re


def read(path: str) -> str:
    return Path(path).read_text(encoding="utf-8")


def write(path: str, text: str) -> None:
    Path(path).write_text(text, encoding="utf-8")


def one(text: str, old: str, new: str, label: str) -> str:
    n = text.count(old)
    if n != 1:
        raise SystemExit(f"{label}: expected one literal anchor, found {n}")
    return text.replace(old, new, 1)


def sub1(text: str, pattern: str, replacement: str, label: str, flags: int = 0) -> str:
    out, n = re.subn(pattern, replacement, text, count=1, flags=flags)
    if n != 1:
        raise SystemExit(f"{label}: expected one regex anchor, found {n}")
    return out


# README
p = "README.md"
t = read(p)
old = """checkpoint            181
active branch         v1-dependency-backed-recommendation-value
active PR             #55 draft
promoted V1 head      a639cfc570290a2169425f43078bbb242fa398e9
current boundary      Specification 021 first live run remains INCOMPLETE;
                      final replacement live source frozen with fresh launch identity
latest experiment     Specification 021
outcome               INCOMPLETE
next                  validate this Checkpoint 181 routing head,
                      expose the identical final target on main,
                      then install one exact one-shot authorization for launch ...-002"""
new = """checkpoint            182
active branch         v1-dependency-backed-recommendation-value
active PR             #55 draft; complete result FAIL; do not merge implementation
promoted V1 head      a639cfc570290a2169425f43078bbb242fa398e9
current boundary      Specification 021 complete replacement run preserved;
                      frozen advancement outcome FAIL
latest experiment     Specification 021
outcome               FAIL
next                  validate the exact reconciled feature head,
                      preserve negative evidence without implementation promotion,
                      then close PR #55 without merge"""
t = one(t, old, new, "README current block")
old = """Specification 021  first governed live run preserved as INCOMPLETE after 72 uniform
                   usage-metadata serialization failures; defect reproduced and repaired
                   cross-platform at Checkpoint 179; repaired source frozen at 180;
                   fresh replacement launch identity frozen into final source at 181;
                   no scientific advancement result yet"""
new = """Specification 021  first governed live run preserved as INCOMPLETE; repaired replacement
                   run completed 36/36 reasoners + 36/36 judges with perfect deterministic
                   disposition/pointer behavior; DBRA-G08 failed on DBRA-01 semantic depth;
                   zero positive SELECTIVE value signals; frozen outcome FAIL"""
t = one(t, old, new, "README progression")
t = one(
    t,
    "docs/checkpoints/181_specification_021_replacement_launch_identity_and_final_live_source_frozen.md\n",
    "docs/checkpoints/181_specification_021_replacement_launch_identity_and_final_live_source_frozen.md\ndocs/checkpoints/182_specification_021_complete_live_result_failed.md\n",
    "README checkpoint route",
)
section = """## Specification 021: complete replacement result failed

Specification 021 completed the prospective dependency-backed recommendation-value experiment after the first live execution had been preserved as `INCOMPLETE` and its usage-metadata serialization defect was repaired without changing frozen science.

Final frozen provider source and governed execution:

```text
source                     575a3264ea39a10e35d769f9c54a2d1a13c28c08
source ref                 v1-spec021-dependency-backed-recommendation-value-replacement-live-source
launch issue               60
launcher run               32742406506
live run                   32742426787
live job                   97479810225
artifact                   9525947445
artifact SHA-256           05724335763fdbeb7eecb456f9662a95dd8d25579d82d360d29d306755648fa8
raw preservation commit    5930a3c52f9580febb56f8e80d3d6eaf8d2cac66
```

Raw evidence was committed before `result.json` was interpreted. The replacement run then completed the full frozen design:

```text
reasoner outputs          36 / 36
judge outputs             36 / 36
provider attempts         72 / 90
failed attempts           0
retries                   0
complete scored design    true
execution integrity       true
```

Frozen aggregate result:

```text
                         GENERIC        SELECTIVE       FULL_HORIZON
exact disposition        1.000000       1.000000        1.000000
semantic score           0.958333       0.950000        0.950000
blocking false positives 0              0               0
pointer errors            0              0               0
critical omissions       0              0               0
unnecessary cost         0              0               0
```

Every case and condition had exact disposition accuracy `1.000000`. The only failed frozen gate was:

```text
DBRA-G08  SELECTIVE every-case semantic score >= 0.85

DBRA-01 semantic:
GENERIC       0.833333
SELECTIVE     0.800000
FULL_HORIZON  0.800000
```

All relative and expansion gates passed, but no prospectively frozen positive SELECTIVE value signal passed. Under the immutable complete-design contract the advancement outcome is therefore:

```text
FAIL
```

The DBRA-01 semantic weakness is shared across conditions rather than selective-specific. The experiment nevertheless contains no post-hoc common-ceiling exemption. Specification 021 is not rescored.

Bounded positive evidence remains important: the explicit requirement/scope/resolver and defer-trigger relations eliminated the over-blocking and pointer failures seen in Specification 019 on these new cases, and the repaired live usage serializer completed all reasoner and judge attempt recording. Those results do not promote the complete recommendation seam.

The first run `32727241852` remains immutable `INCOMPLETE` historical evidence. The replacement authorization and temporary control-plane surfaces have been retired; the standing governed launcher is restored and the main authorization registry is empty.

Primary evidence:

```text
docs/checkpoints/182_specification_021_complete_live_result_failed.md
experiments/dependency_backed_recommendation_action_value/V1_DEPENDENCY_BACKED_RECOMMENDATION_ACTION_VALUE_RESULT.md
experiments/dependency_backed_recommendation_action_value/results/spec021-live-20260824-run-32742426787/
```
"""
t = sub1(
    t,
    r"## Specification 021:.*?\n---\n\n## Preservation and continuity hardening",
    section + "\n---\n\n## Preservation and continuity hardening",
    "README spec021 section",
    re.S,
)
continuation = """## Exact continuation

```text
1. keep both Specification 021 live runs immutable: the first INCOMPLETE, the replacement FAIL
2. validate the exact Checkpoint 182 feature head provider-free
3. create a preservation-only branch from v1-frontend-spike
4. preserve the frozen contract, benchmark fixture, checkpoints, canonical history, stable result, and raw evidence
5. exclude the rejected Specification 021 harness, runner, live workflow, and implementation tests from promotion
6. merge only the preservation evidence after exact green validation
7. close PR #55 without merge
8. reconcile v1-frontend-spike to the preserved Specification 021 FAIL boundary
9. do not repeat or tune Specification 021 merely to seek a positive result
10. authorize no new provider call until a genuinely new prospective question is frozen
```"""
t = sub1(
    t,
    r"## Exact continuation\n\n```text\n.*?\n```(?=\n\n---\n\n## Repository role)",
    continuation,
    "README continuation",
    re.S,
)
write(p, t)

# CURRENT_STATE
p = "docs/CURRENT_STATE.md"
t = read(p)
t = one(t, "**Checkpoint:** 181  ", "**Checkpoint:** 182  ", "CURRENT checkpoint")
t = sub1(
    t,
    r"\*\*Active PR:\*\* #55 draft,.*?  \n",
    "**Active PR:** #55 draft, complete Specification 021 result classified `FAIL`; implementation must not merge  \n",
    "CURRENT active PR",
)
t = sub1(
    t,
    r"\*\*Development stage:\*\* .*?  \n",
    "**Development stage:** Prototype V0 complete; bounded V1 retains the accepted project/object, persistence, methodological-knowledge, retrieval/Horizon/selective-context, real-reasoning, dependency-backed sequencing, Project Cockpit, runtime, governed live-launch, blocking-construct, and routing-consistency seams. Specification 021 completed after its first run was preserved as `INCOMPLETE`; the repaired replacement run is now frozen `FAIL` evidence with perfect deterministic recommendation semantics but insufficient DBRA-01 semantic depth and no positive SELECTIVE value signal.  \n",
    "CURRENT development stage",
)
t = one(t, "**Latest experiment status:** Specification 021 `INCOMPLETE`  ", "**Latest experiment status:** Specification 021 `FAIL`  ", "CURRENT outcome")
t = sub1(
    t,
    r"\*\*Immediate project priority:\*\* .*?\n",
    "**Immediate project priority:** validate the exact Checkpoint 182 feature head, preserve the failed experiment evidence without promoting its implementation, close PR #55 without merge, and only then define a genuinely new prospective research question.\n",
    "CURRENT priority",
)
t = sub1(
    t,
    r"Repository artifacts remain authoritative across chats\..*?\n\n---",
    "Repository artifacts remain authoritative across chats. `main` hosts the narrow governed live-launch control plane. The Specification 021 replacement authorization and temporary live/observer/preservation surfaces have been retired, the standing launcher is restored, and the main authorization registry is empty. No new provider call is authorized.\n\n---",
    "CURRENT control plane",
    re.S,
)
if "-> dependency-backed recommendation-value experiment 021 [INCOMPLETE; FINAL SOURCE FROZEN]" in t:
    t = one(
        t,
        "-> dependency-backed recommendation-value experiment 021 [INCOMPLETE; FINAL SOURCE FROZEN]",
        "-> dependency-backed recommendation-value experiment 021 [FAIL; COMPLETE EVIDENCE PRESERVED]",
        "CURRENT evidence chain",
    )
section = """## Specification 021 complete replacement result failed

Specification 021 kept the prospectively frozen four-case GENERIC/SELECTIVE/FULL_HORIZON comparison and explicit system-owned project relations unchanged throughout the repair cycle.

Historical first run:

```text
run                         32727241852
classification              INCOMPLETE
raw preservation commit     247314916fa028e2d27ea282ee030a26a30a84cc
```

Final replacement source and execution:

```text
source                      575a3264ea39a10e35d769f9c54a2d1a13c28c08
source ref                  v1-spec021-dependency-backed-recommendation-value-replacement-live-source
launch issue                60
launcher run                32742406506
live run                    32742426787
live job                    97479810225
artifact                    9525947445
artifact SHA-256            05724335763fdbeb7eecb456f9662a95dd8d25579d82d360d29d306755648fa8
raw preservation commit     5930a3c52f9580febb56f8e80d3d6eaf8d2cac66
```

The raw artifact was preserved before interpretation. The replacement execution completed 36/36 reasoner outputs and 36/36 blinded judge outputs using 72/90 provider attempts with zero retries and execution integrity true.

Frozen metrics:

```text
                         GENERIC        SELECTIVE       FULL_HORIZON
exact disposition        1.000000       1.000000        1.000000
semantic score           0.958333       0.950000        0.950000
blocking false positives 0              0               0
blocking pointer errors  0              0               0
defer pointer errors     0              0               0
critical omissions       0              0               0
unnecessary cost         0              0               0
```

Per-case exact accuracy was `1.000000` everywhere. DBRA-01 semantic quality was `0.833333` GENERIC and `0.800000` for SELECTIVE and FULL_HORIZON; all other cases scored `1.000000` in every condition.

Exactly one frozen gate failed:

```text
DBRA-G08  SELECTIVE every-case semantic score >= 0.85
```

Relative and expansion gates passed, but positive value signals were empty. The immutable complete-design classifier therefore returns:

```text
FAIL
```

The shared DBRA-01 semantic weakness is not evidence that SELECTIVE uniquely caused the failure, but the frozen absolute gate contains no post-hoc exemption. The result also provides no positive evidence that SELECTIVE improves recommendation quality beyond the strong generic reasoner on this bounded universe.

Bounded positive lessons remain: explicit requirement/scope/resolver and defer-trigger relations produced perfect disposition and pointer behavior across all conditions, and the repaired JSON-safe usage serialization completed under real provider usage. These lessons do not promote the full Specification 021 implementation.

Stable evidence:

```text
docs/checkpoints/182_specification_021_complete_live_result_failed.md
experiments/dependency_backed_recommendation_action_value/V1_DEPENDENCY_BACKED_RECOMMENDATION_ACTION_VALUE_RESULT.md
experiments/dependency_backed_recommendation_action_value/results/spec021-live-20260824-run-32742426787/
```
"""
t = sub1(
    t,
    r"## Specification 021 incomplete first live execution; final replacement live source frozen\n.*?\n---\n\n## Current non-selections",
    section + "\n---\n\n## Current non-selections",
    "CURRENT spec021 section",
    re.S,
)
continuation = """## Exact continuation

```text
1. keep the first Specification 021 run immutable as INCOMPLETE and the replacement as FAIL
2. validate the exact Checkpoint 182 feature head provider-free
3. construct a preservation-only branch from v1-frontend-spike
4. carry frozen contract, fixture, checkpoints, canonical history, stable result, and raw evidence only
5. exclude rejected Specification 021 implementation/harness/live workflow/tests
6. merge the preservation-only PR only after exact green validation
7. close PR #55 without merge
8. reconcile v1-frontend-spike to the preserved FAIL boundary
9. do not repeat/tune the same benchmark and authorize no new provider run without a new prospective contract
```"""
t = sub1(t, r"## Exact continuation\n\n```text\n.*?\n```\s*$", continuation + "\n", "CURRENT continuation", re.S)
write(p, t)

# KNOWLEDGE_MAP
p = "docs/KNOWLEDGE_MAP.md"
t = read(p)
t = one(t, "**Current checkpoint:** 181  ", "**Current checkpoint:** 182  ", "MAP checkpoint")
t = sub1(
    t,
    r"\*\*Active PR:\*\* #55 draft,.*?  \n",
    "**Active PR:** #55 draft, Specification 021 complete result `FAIL`; preservation-only integration next  \n",
    "MAP active PR",
)
t = one(t, "**Latest experiment:** Specification 021 `INCOMPLETE`", "**Latest experiment:** Specification 021 `FAIL`", "MAP outcome")
t = one(t, "main                           governed live-launch control plane; no replacement Spec021 authorization yet", "main                           governed live-launch control plane; Spec021 replacement authorization retired", "MAP main route")
t = sub1(
    t,
    r"Specification 021 / Checkpoints 174-181 / PR #55\n.*?final source 575a3264ea39a10e35d769f9c54a2d1a13c28c08 frozen with fresh launch identity \.\.\.-002 at Checkpoint 181",
    """Specification 021 / Checkpoints 174-182 / PR #55
    dependency-backed recommendation-value contract frozen prospectively;
    first governed live run 32727241852 preserved as scientifically INCOMPLETE;
    usage serialization defect reproduced and repaired without scientific changes;
    final replacement source 575a3264ea39a10e35d769f9c54a2d1a13c28c08 frozen at Checkpoint 181;
    replacement run 32742426787 completed 36/36 reasoners + 36/36 judges with integrity;
    exact dispositions/pointers perfect in all conditions, but DBRA-G08 failed;
    no positive SELECTIVE value signal; frozen outcome FAIL; implementation not promoted""",
    "MAP progression",
    re.S,
)
section = """### Specification 021, complete replacement result failed

Primary sources:

```text
docs/research/029_dependency_backed_recommendation_value_design.md
docs/specifications/021_v1_dependency_backed_recommendation_action_value_vertical_slice.md
tests/fixtures/reasoning/dependency_backed_recommendation_action_v1.json
docs/checkpoints/174_specification_021_dependency_backed_recommendation_value_contract_frozen.md
docs/checkpoints/175_specification_021_provider_free_implementation_gate_cross_platform_passed.md
docs/checkpoints/176_specification_021_pre_live_boundary_frozen.md
docs/checkpoints/177_specification_021_live_source_frozen.md
docs/checkpoints/178_specification_021_live_execution_incomplete_usage_serialization.md
docs/checkpoints/179_specification_021_usage_serialization_repair_cross_platform_passed.md
docs/checkpoints/180_specification_021_repaired_live_source_frozen.md
docs/checkpoints/181_specification_021_replacement_launch_identity_and_final_live_source_frozen.md
docs/checkpoints/182_specification_021_complete_live_result_failed.md
experiments/dependency_backed_recommendation_action_value/V1_DEPENDENCY_BACKED_RECOMMENDATION_ACTION_VALUE_RESULT.md
```

Frozen scientific status:

```text
FAIL
```

Final execution:

```text
source                   575a3264ea39a10e35d769f9c54a2d1a13c28c08
launch issue             60
launcher run             32742406506
live run                 32742426787
live job                 97479810225
artifact                 9525947445
artifact SHA-256         05724335763fdbeb7eecb456f9662a95dd8d25579d82d360d29d306755648fa8
raw preservation commit  5930a3c52f9580febb56f8e80d3d6eaf8d2cac66
reasoners                36 / 36
judges                   36 / 36
provider attempts        72 / 90
execution integrity      true
```

All three conditions had perfect exact disposition accuracy, zero blocking false positives, zero pointer errors, zero omissions, and zero unnecessary recommendation cost. Aggregate semantic scores were `0.958333` GENERIC, `0.950000` SELECTIVE, and `0.950000` FULL_HORIZON.

The only failed gate was `DBRA-G08`: DBRA-01 SELECTIVE semantic score was `0.800000` below the frozen `0.850000` per-case floor. GENERIC scored `0.833333` and FULL_HORIZON `0.800000` on the same case, so the semantic weakness was shared rather than selective-specific. Relative and expansion gates passed; no positive SELECTIVE value signal passed.

The explicit dependency-backed semantics are nevertheless strong bounded construct evidence because all action dispositions and relation pointers were exact across the complete matched design. The frozen scientific advancement result remains `FAIL`, and PR #55's implementation must not be promoted.

The first run `32727241852` remains separately preserved as `INCOMPLETE` historical evidence.
"""
t = sub1(
    t,
    r"### Specification 021, incomplete live result with final replacement source frozen\n.*?\n---\n\n## Governed autonomous live-launch route",
    section + "\n---\n\n## Governed autonomous live-launch route",
    "MAP spec021 section",
    re.S,
)
if "The consumed Specification 021 authorization is retired." in t:
    t = sub1(
        t,
        r"The consumed Specification 021 authorization is retired\..*?\n\n---",
        "Both Specification 021 one-shot authorizations are retired. The completed replacement result is frozen `FAIL`; no further Specification 021 provider run is authorized.\n\n---",
        "MAP launcher status",
        re.S,
    )
t = sub1(
    t,
    r"## Current exact continuation\n\n```text\n.*?\n```",
    """## Current exact continuation

```text
A. preserve the first Specification 021 run as INCOMPLETE and the replacement as FAIL
B. validate the exact Checkpoint 182 feature head
C. create and validate a preservation-only branch from v1-frontend-spike
D. preserve contract, fixture, checkpoints, canonical history, stable result, and raw evidence
E. exclude the rejected Specification 021 implementation/harness/live workflow/tests
F. merge only the preservation evidence
G. close PR #55 without merge
H. reconcile integration to the preserved FAIL boundary
I. do not repeat or tune Specification 021 merely to seek a positive result
J. authorize no new provider run until a genuinely new prospective contract is frozen
```""",
    "MAP continuation",
    re.S,
)
t = one(
    t,
    "181  Specification 021 final replacement live source frozen with fresh launch identity",
    "181  Specification 021 final replacement live source frozen with fresh launch identity\n182  Specification 021 complete replacement run classified FAIL; evidence preservation only",
    "MAP recent checkpoint",
)
write(p, t)

# OPEN_QUESTIONS
p = "docs/OPEN_QUESTIONS.md"
t = read(p)
t = sub1(
    t,
    r"\*\*Reconciliation context:\*\* .*?\n",
    "**Reconciliation context:** Prototype V0 is complete. Bounded V1 has established the project/object foundations, Project Cockpit, governed persistence/interchange, runtime boundary, retrieval/Horizon/selective-context chain, real reasoning-context evidence, dependency-backed sequencing, governed live-launch, and dependency-backed blocking construct validity. Specification 019 remained `FAIL`; Specification 020 returned `BLOCKING_BOUNDARY_SUPPORTED`. Specification 021 then completed its clean dependency-backed recommendation-value comparison after an initial preserved `INCOMPLETE` run and narrow instrumentation repair. The replacement run had perfect deterministic action dispositions and pointers in all conditions, but failed the frozen DBRA-01 semantic case floor and produced no positive SELECTIVE value signal. Specification 021 is therefore permanently `FAIL` under its frozen contract.\n",
    "OPEN context",
)
t = one(
    t,
    "**Status:** Selective reasoning-context seam supported; clean recommendation-value experiment attempted live but scientifically incomplete; final replacement source frozen but not authorized",
    "**Status:** Selective reasoning-context seam supported; complete clean recommendation-value experiment `FAIL`; selective downstream value remains unestablished",
    "OPEN Q005 status",
)
t = sub1(
    t,
    r"Specification 021 freezes a four-case GENERIC/SELECTIVE/FULL_HORIZON comparison.*?The live scientific result remains unknown\.",
    "Specification 021 completed its four-case GENERIC/SELECTIVE/FULL_HORIZON comparison after the first live run was preserved as `INCOMPLETE` and the usage-serialization defect was repaired without changing frozen science. The replacement run achieved perfect exact disposition and pointer behavior in all conditions. DBRA-01 semantic scores were `0.833333` GENERIC and `0.800000` for SELECTIVE and FULL_HORIZON, causing frozen absolute gate `DBRA-G08` to fail; all relative and expansion gates passed, but no positive SELECTIVE value signal passed. The immutable advancement outcome is `FAIL`. This does not show SELECTIVE is generally harmful, but it does mean the current bounded universe provides no demonstrated recommendation-quality advantage over the strong generic reasoner.",
    "OPEN Q005 result",
    re.S,
)
t = t.replace(
    "Its first governed live run was scientifically incomplete before any scored observation. Checkpoints 179-181 address only instrumentation and launch-source readiness.",
    "The completed replacement run produced perfect deterministic action dispositions and pointers across all conditions, strengthening the bounded construct evidence, while the full Specification 021 recommendation-value outcome remained `FAIL` because of the DBRA-01 semantic floor and zero positive value signals.",
)
t = t.replace(
    "Its incomplete first live execution and Checkpoints 179-181 do not alter those project-state semantics.",
    "Its completed replacement run preserved those project-state semantics and produced exact action/relation-pointer behavior, but does not define production dependency or claim-scope persistence.",
)
t = t.replace(
    "Its first live execution produced no scored scientific evidence; Checkpoints 179-181 establish only repair and launch readiness.",
    "Its repaired replacement execution completed with perfect deterministic dispositions and pointers but a frozen scientific outcome of `FAIL`; no SELECTIVE recommendation-value advantage was demonstrated.",
)
t = t.replace(
    "Its first live run is incomplete. Checkpoints 179-181 change only instrumentation and governed launch readiness, not the state-to-recommendation semantics.",
    "Its replacement run completed and preserved the state-to-recommendation relation semantics exactly, but the full recommendation-value contract classified `FAIL`.",
)
t = t.replace(
    "Specification 021's first live execution is incomplete with zero scored observations, so it still cannot establish that selective context adds downstream recommendation value. Checkpoint 179 repairs only the usage-metadata recording boundary, and Checkpoints 180-181 only freeze the repaired final source and fresh launch identity.",
    "Specification 021's repaired replacement execution completed, but it still does not establish that selective context adds downstream recommendation value: the frozen outcome is `FAIL`, the only failed gate is the DBRA-01 SELECTIVE semantic case floor, and no positive SELECTIVE value signal passed.",
)
t = t.replace(
    "Its first governed live run yielded zero scored observations because usage attempt-metadata serialization failed before successful outputs could be preserved. Checkpoint 179 reproduces and repairs that instrumentation issue provider-free without changing provenance ownership or the evaluation contract. Checkpoints 180-181 freeze the final replacement source and fresh launch identity. The live recommendation-value question remains open.",
    "Its first governed live run yielded zero scored observations and remains immutable `INCOMPLETE` evidence. The repaired replacement run then completed the full design with perfect deterministic action/pointer behavior, but the frozen recommendation-value result was `FAIL`: DBRA-G08 failed on DBRA-01 semantic depth and no positive SELECTIVE value signal passed. The broader question of when explicit knowledge adds value beyond strong generic reasoning remains open, but Specification 021 itself is closed.",
)
t = t.replace(
    "**Status:** Bounded V1 mechanism answered and supported; provider-backed use exercised for Specifications 019, 020, and 021; final Specification 021 replacement source frozen but not authorized",
    "**Status:** Bounded V1 mechanism answered and supported; provider-backed use exercised for Specifications 019, 020, and two governed Specification 021 runs; all one-shot authorizations retired",
)
t = sub1(
    t,
    r"Specification 021 then exercised the same control plane at frozen source `b589bad.*?none exists at the Checkpoint 181 boundary\.",
    "Specification 021 exercised the same control plane twice. The first frozen run at `b589bad975880b2d3cccc3596fc82539b1b96577` was preserved as `INCOMPLETE` after uniform usage-metadata serialization failure. After a prospectively tested narrow repair and fresh source freeze, launch `spec021-dependency-backed-recommendation-value-002` executed final source `575a3264ea39a10e35d769f9c54a2d1a13c28c08` as run `32742426787`. Its raw artifact was preserved before interpretation and the frozen scientific result classified `FAIL`. Both one-shot authorizations and temporary default-branch surfaces are retired; the standing launcher remains.",
    "OPEN Q053",
    re.S,
)
write(p, t)

# MAJOR_CHANGES
p = "docs/MAJOR_CHANGES.md"
t = read(p)
if "Specification 021 complete dependency-backed recommendation experiment failed" in t:
    raise SystemExit("MAJOR_CHANGES section already exists")
t = t.rstrip() + """

---

## 2026-08-24: Specification 021 complete dependency-backed recommendation experiment failed

Specification 021 prospectively combined the accepted system-owned provenance, dependency-backed DEFER, and explicit requirement/scope/resolver blocking constructions in a new four-case GENERIC/SELECTIVE/FULL_HORIZON recommendation-value experiment.

The first governed live execution was preserved as `INCOMPLETE` after a live-shaped `ReasoningUsage` serialization defect prevented scored observations. That defect was reproduced provider-free, repaired narrowly for both reasoner and judge attempt metadata, and revalidated cross-platform without changing the frozen scientific contract.

The repaired replacement run then completed the full frozen design:

```text
reasoner outputs          36 / 36
judge outputs             36 / 36
provider attempts         72 / 90
exact dispositions        1.000000 in all conditions
blocking/pointer errors   0 in all conditions
SELECTIVE semantic        0.950000 aggregate
DBRA-01 SELECTIVE         0.800000
DBRA-G08                  FAIL
positive value signals   0
outcome                   FAIL
```

The explicit dependency-backed relations eliminated the prior bounded over-blocking problem on the new cases, but the full recommendation seam did not earn promotion. DBRA-01 semantic depth missed the frozen per-case floor across SELECTIVE and FULL_HORIZON, and SELECTIVE showed no prospectively defined recommendation-quality advantage over the strong generic reasoner. The failed implementation is therefore preserved as evidence rather than promoted.

The next research direction should not repeat or tune the same benchmark merely to obtain a positive result. Higher-value questions concern knowledge novelty/coverage, semantic content carried by compact methodology projections, and harder heterogeneous project states where strong generic reasoning may actually lack relevant knowledge.

Key sources:

```text
docs/specifications/021_v1_dependency_backed_recommendation_action_value_vertical_slice.md
docs/checkpoints/182_specification_021_complete_live_result_failed.md
experiments/dependency_backed_recommendation_action_value/V1_DEPENDENCY_BACKED_RECOMMENDATION_ACTION_VALUE_RESULT.md
```
"""
write(p, t)

# current_routing.json
p = "docs/current_routing.json"
data = json.loads(read(p))
expected = {
    "schema_version": 1,
    "current_checkpoint": 181,
    "active_development_branch": "v1-dependency-backed-recommendation-value",
    "active_pr": 55,
    "promoted_integration_branch": "v1-frontend-spike",
    "promoted_integration_sha": "a639cfc570290a2169425f43078bbb242fa398e9",
    "latest_specification": "021",
    "latest_experiment_outcome": "INCOMPLETE",
    "current_boundary": "spec021-final-replacement-live-source-frozen-authorization-next",
}
if data != expected:
    raise SystemExit(f"unexpected routing manifest before reconciliation: {data}")
data["current_checkpoint"] = 182
data["latest_experiment_outcome"] = "FAIL"
data["current_boundary"] = "spec021-complete-live-result-fail-preservation-next"
write(p, json.dumps(data, indent=2) + "\n")
