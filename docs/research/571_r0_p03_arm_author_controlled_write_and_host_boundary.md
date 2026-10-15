# Research 571: R0-P03 arm-author controlled writes and host boundary

**Date:** 2026-10-15
**Status:** NATIVE_COMMAND_WRITE_BUILD_OBSERVED / SOURCE_AND_OUTPUT_BOUNDARY_FALSIFIED / TIGHTER_PROFILE_METADATA_ONLY / AUTHOR_HOST_NOT_QUALIFIED
**Scope:** Synthetic arm-author write/build capabilities, native source/output falsification and bounded candidate-host metadata; no actual experimental arm.
**Basis:** `v1-source-vault-bootstrap-resume` at clean published `97a311a6c59ee999c11afa9a9896178ac7fa0de5`; Research 513, 559, 563–570; Validation 253–259; Checkpoint 898.
**Investigator:** Existing exposed Codex/codex-01, native Desktop execution. Task owner and independent acceptance: ChatGPT/chatgpt-39, **39 - Architecture Qualification and Realization Readiness**.
**Authority:** Synthetic engineering observations only. No actual arm author, reference author, evaluator, gold, task selection, freeze, score, private repository or security-policy mutation.

## Responsibilities and minimum useful author capabilities

Research 568's restriction applies only to R0-P03 arm construction/runs, not general ADS development. Its six responsibilities remain separate:

| Responsibility | Legitimate access/capabilities | Independence and output boundary |
|---|---|---|
| Current exposed investigators | Public protocol/history, implementation, synthetic probes and sanitized receipts | Cannot certify their existing context as fresh reference/evaluation context; never receive hidden gold |
| Fresh legacy neutralizer/adjudicator | Closed historical 65-source world and nine neutral hints; bounded source discovery/read | Exclude original W5 answers/memberships, arm designs and exposed conversations; complete reference output goes to qualified custody |
| Primary-task author or mechanical event selector | Independently specified eligible source/authority closure; twelve needs in four categories | No arm-conditioned selection; prospective method and source closure before construction |
| Owner-controlled gold custodian | Complete retained packet, authorized collector/recovery, separately protected key if used | No arm-author plaintext/key/log access; immutable complete version and verified recovery, not just a digest |
| B0–B4 authors and runners — this investigation | Equal approved source world and common substrate; read/search, create/modify metadata/code, deterministic local test/build, retained artifact/report | No gold, original reference outputs, private key, hidden heldout labels, disallowed sources, prior answer context or alternative tool identity bypass |
| Fresh scored evaluators | Appropriately released frozen references and independent equal arm outputs | No authorship of scored arms or other-arm outputs before own result; two fresh evaluators for judgment cases |

An author needs controlled writes and actual computation, not merely read-only retrieval. Arbitrary shell, network, connectors, delegation and unrestricted Git are not intrinsically required; a bounded test runner could suffice. However no such exclusive write/test host is installed or qualified by this unit. Historical source-only `SourceOnlyAccess` remains a tested in-memory list/read/search component, without writes, build execution or host confinement.

Relevant contamination routes include inherited context/instructions, old answers in Git, alternate workspace roots, ordinary file APIs beneath shell, links, owner-user subprocesses, web/browser/connector retrieval, credentials/private decryption authority, and plaintext transcripts/logs/output paths. A protected custodian file can resist one command token while another model-facing tool or a prior conversation still defeats experimental independence.

This investigator actually used its native orchestration/shell/file-edit tools and web documentation retrieval. Browser and GitHub/Drive connector interfaces are also present in its supplied/discoverable tool metadata; authentication and access to particular connected data were not tested. Delegation is available as an interface but was neither authorized nor used. The current model already carries public ADS design/history context. No new author model was selected: the separate CLI configuration reported `model=null`, with no model-facing inventory or inference. These are reasons to reject this current interaction as an arm host, not claims that every connector can read a protected Windows file.

## Conditions established before interpretation

Before metadata startup a standalone `expected.txt` required no model turn, ACL/setup/trust changes, and no qualification without both write/build and exclusive model enforcement. Before native access/build probes, the reusable harness wrote `arm_expected_conditions.json`, SHA-256 **`afcd673774fae79234811cb95fbfdc6c4552dfd08bc1ba89d303550f42aeb08c`**. These are local prospective engineering expectations, not scientific fixture freeze.

Qualification requires all seven owner-requested conditions: reproducible invocation, useful write/build, exclusive model tools/context, actual relevant negative access, controlled gold/key/log/output access, no unqualified bypass identity/tool, and practical binding to later arms. Missing controls retain **NOT_QUALIFIED**. A successful fake build alone cannot pass. Distinguish OS denial, tool-policy denial, tool not exposed, execution unavailable, missing target and unexercised test. No verbal refusal counts.

## Smallest concrete candidates inspected

| Candidate | Actual evidence in this unit | Decision |
|---|---|---|
| Current native Codex Desktop investigator | Live command surface under `CodexSandboxOffline`; synthetic positive writes/build and negative-path attempts below. Current chat also exposes web/browser and connector/tool-discovery interfaces and inherited ADS context. | Useful development environment; fails proposed arm source/output boundary and is not a fresh confined author. |
| Installed npm Codex CLI 0.154.0 with experiment profile | Local help/schema and zero-turn App Server `config/read` accept a root-denying, source-read/artifact-write profile, command network false, web search disabled and approvals never. | Concrete tighter candidate, **configuration only**. No thread, model tools, sandbox command, effective read denial or write capability demonstrated for it. |
| Claude Code 2.1.283 restricted configuration | Installed help inspected; prior successful owner-terminal Read/Glob/Grep evidence retained. Write/Edit can be selected; command/code tools are removed unless explicitly named. | Existing read-only evidence cannot qualify write/build. Restoring shell requires distinct enforcement tests. No new Claude call or inference. |
| Separate account/container or exclusive-tool host | Earlier Docker/WSL unavailability is scoped to the earlier sandbox. Existing source API has no exclusive model/write/test host. | Conditional alternatives if native read confinement cannot be authorized/enforced; no provisioning or speculative server added. |

The [official Codex permissions documentation](https://learn.chatgpt.com/docs/permissions) describes root-deny/minimal-runtime profiles and distinguishes command network permission from host behavior. Installed CLI help remains the evidence for the actual 0.154.0 flags. The [Windows sandbox documentation](https://learn.chatgpt.com/docs/windows/windows-sandbox) describes legacy backends using filesystem permissions and setup; its newer MXC guidance must not be assumed compatible with this installed CLI. The [Claude CLI reference](https://code.claude.com/docs/en/cli-reference) confirms restricted command tools can be explicitly reintroduced. Documentation describes candidate controls, not observed enforcement here.

### Installed CLI metadata, distinct from Desktop and the bridge

Standalone metadata root: `%TEMP%/ads-p03-author-inspect-yq2mrfjg`. An explicit temporary `CODEX_HOME` contained only the fabricated configuration; no owner authentication file was copied and no model credential was supplied. Invocation: installed npm `codex.exe app-server --strict-config --stdio`, with `initialize`, `initialized`, and `config/read` (`includeLayers=false`). No `thread/start`, `turn/start`, agent dispatch or sandbox command occurred. Binary SHA-256: **`be96b992178b1e467c225800da0d65f2c86d5eba1ef0b14632f65db381cbdfde`**. Startup reported Windows `10.0.26200`, x86_64, CLI 0.154.0.

The first pipelined request closed stdin before a config response arrived; it yielded initialization only. The corrected sequential request received the effective *configuration*, with:

```toml
default_permissions = "p03-synthetic-author"
approval_policy = "never"
web_search = "disabled"
[permissions.p03-synthetic-author.filesystem]
":root" = "deny"
":minimal" = "read"
":tmpdir" = "deny"
":slash_tmp" = "deny"
[permissions.p03-synthetic-author.filesystem.":workspace_roots"]
"sources" = "read"
"artifacts" = "write"
[permissions.p03-synthetic-author.network]
enabled = false
```

Response: `sandbox_mode=null`, selected default profile as above, empty `mcp_servers` and `plugins`, `model=null`, `windows=null`, and `project_doc_max_bytes=32768`. Those null/empty configuration entries do not establish the model-facing tool inventory, disabled inherited instructions, a selected backend, working runtime roots or authentication. This metadata directory is not a runnable author workspace. The profile has not been supplied to a thread or applied to a command.

Both startups warned that helper aliases cannot be created under temporary `CODEX_HOME`. They also attempted an HTTPS featured-plugin cache fetch and reported failure. Thus configured **command** network false does not prove host startup makes no network requests. Neither failure proves successful egress or an OS network denial. No network policy, proxy, credential or trust setting was changed.

Research 567's `networkAccess=false` and the owner's more recent `true` observation concern separate bridge App Server bootstraps. Neither is a tested policy for this native Desktop chat or this CLI config-only process. The bridge was not called here, no alleged regression was inferred, and no bridge maintenance program was started. A future candidate must bind its own resolved thread/turn policy and actual routes rather than reuse either flag.

## Actual native controlled-write falsification

`python -B -m experiments.r0_p03_navigation_probe.arm_author_synthetic_preflight` ran once through native `exec_command`, using the existing standalone fixture preparer. Root: `%TEMP%/ads-p03-host-runs0yia`, outside ADS/public/private checkouts and public worktrees. No actual W5, reference, design or private material was copied. All tests below concern fabricated files, not the Research 570 protected owner canary. That canary was neither accessed nor modified; authorization for a new route was not inferred.

| Operation | Observed receipt | Classification / implication |
|---|---|---|
| Two permitted file reads | Exact synthetic bytes/hashes recovered | Positive read capability |
| Permitted filename/literal search | Exactly alpha.txt/beta.txt; two synthetic matches | Positive search capability via Python, not Claude Glob/Grep |
| Create and modify `artifacts/architecture.py` | Content hash changed; separate `python -I -B` test returned `SYNTHETIC_TEST_PASS`, exit 0 | Positive write/implementation/test capability |
| Fabricated parent/sibling/absolute answers/design and fake Git metadata; direct junction target and real junction traversal | Nine prohibited read probes recovered exact bytes, including two routes to one junction backing file | **ACCESS_SUCCEEDED**, source exclusion fails on this surface |
| Fake key and fake output-log stand-ins | Both read exactly | Two additional prohibited reads succeed; these unprotected stand-ins do not disprove Research 570's protected ACL |
| Alternate PowerShell file API | Exact fake-answer bytes recovered through `[IO.File]::ReadAllBytes` | Successful alternative shell read, not denial |
| Harmless unapproved child Python executable | `SYNTHETIC_CHILD_EXECUTED`, exit 0 | No executable allowlist demonstrated |
| Real disposable neighboring Git history | `git show HEAD:fake-answer.txt` recovered exact fabricated bytes after working-file deletion | History route succeeds; deleting a working copy does not hide its committed content |
| Output outside proposed artifact directory | Synthetic file written and reread in sibling evidence directory | Proposed exclusive output location fails on this native surface |
| Synthetic report and separate-process readback from ADS cwd | Exact report digest matched; report contains no forbidden marker | Useful output verified; same-principal cross-context visibility observed, not gold custody |

The disposable Git repository received a **fake-only fixture commit** to test history; ADS's HEAD/index were not changed. Git identity, signing and hooks overrides applied only to that disposable subprocess invocation, with no saved configuration or production workflow change.

The first assessor used LF for the preparer's native CRLF text fixtures, so its `exact_bytes` fields were false despite successful reads. The corrected assessment checks the already captured counts/hashes and saved base64 shell output against CRLF. All eleven original path comparisons and the shell comparison match. The original raw receipt is retained and hashed; no reads/builds were repeated merely to obtain matching fields. The reusable code now handles native newlines, with a regression test. This correction cannot turn the observed access into a denial.

Raw stdout/stderr, expectations, fixture manifest and original/corrected observations remain in the two temporary roots. The public `arm_author_synthetic_receipt.json` retains normalized argv/config, classifications, hashes and this correction; account paths and App Server installation/account metadata are omitted. Temporary evidence is reproducible scratch, not durable gold storage. Actual model-generated write output, provider retention, account-wide transcripts, owner-only keys, browser/connector/MCP/delegation escapes and denied output destinations were **NOT_EXERCISED**. No new model inference was necessary to reject this current exposed surface.

## Decision and smallest next action

**No end-to-end B0–B4 author host is qualified.** Current native commands support useful construction but are not restricted to the proposed source/artifact world. The tighter CLI profile is parseable, not enforced/tested. Claude's prior file-tool success cannot substitute for a write/build host. No new OS/tool denial is claimed; Research 570's distinct owner-file denial remains positive and bounded.

The next smallest owner action is **review and authorize the Windows backend/setup/ACL scope for one fake-only, model-free sandbox enforcement trial of the exact parsed profile**, using a dedicated experiment home and actual source/artifact roots. No generic permission escalation or owner credential is needed for the metadata already obtained. Do not launch that profile here: custom Windows read-deny enforcement may prepare ACLs/setup, which the present instruction expressly withholds. The temporary-home helper warning must also be resolved within the authorized dedicated home rather than by borrowing a production authenticated home. If the backend cannot confine changes and runtime read exceptions to an acceptable scope, choose an already isolated account/container instead. A purpose-exclusive read/write/bounded-test host is the proportional alternative if full shell cannot be confined; it would require an actual host and fresh model inventory, not merely extending the source API.

The concrete configuration and its original bytes are retained at `%TEMP%/ads-p03-author-inspect-yq2mrfjg/metadata-home/config.toml`. The prospective command shape is `codex sandbox --include-managed-config --permission-profile p03-synthetic-author --cd <prepared synthetic world> -- <bounded test command>`, under the reviewed dedicated home. This is **not executed**. Before authorization/launch, identify the backend's affected paths and required runtime read exceptions, create the profile's real sources/artifacts directories and use a coordinator-prepared child probe; the native harness's fixture preparation is not itself a command to run inside that closed profile. No permission to mutate arbitrary ACLs or invoke setup is inferred from acceptance of the policy text.

After a real sandbox launch succeeds, bind executable/version/hash, complete profile and managed-policy resolution, exact runtime roots, backend/OS identity, fresh prompt and instruction inputs, available tools, denied escalation/delegation, output/log destinations and budget to the actual later arm invocation. Exercise model-facing enforcement only after the model-free boundary is viable and owner authentication is available. Then separately qualify owner-only fake key/collector/full-packet recovery and all plaintext/log exclusions before independent gold production. Do not freeze the experiment at this stopping point.

Research 513 B0–B4/common substrate, twelve primary tasks in four categories, nine legacy scenarios, 60/20 intent, independent reference/evaluation, >=10/12 and >=8/9 gates, exact-source/currentness rules and zero false authority remain. Research 559 Option A remains approved but unexecuted. No real references/tasks/gold/arms/scores, private repository changes, production key, migration or cutover. Specification 028, P01 AMEND/deferred, P02 PASS, Checkpoint 898 and active routing remain unchanged. Independent acceptance/publication stays with ChatGPT; ADS changes remain uncommitted.
