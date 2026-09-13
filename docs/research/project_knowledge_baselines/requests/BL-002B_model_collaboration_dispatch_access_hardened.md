# BL-002B Request: Bring Claude into Current Work / Access-Hardened Replacement

**Scenario:** BL-002B (replacement replicate for invalid BL-002-A)
**Frozen snapshot:** `1a422c79dc67384426ad10e28c2fc6845147f9e0`

## Trial integrity contract

Use only the exact frozen Git commit named below as project evidence for the task.

Do not use descendant/current repository content as evidence. In particular, do not read current Research 124, the failure corpus, baseline protocol, baseline result files or later diagnosis records. Do not use web/external sources or prior-chat/project memory as evidence.

If you cannot reliably constrain repository reads to the exact snapshot, stop with `SNAPSHOT_ACCESS_UNAVAILABLE` rather than using current HEAD.

For repository access, use **Codexless Runtime Bridge only**. Do not use the native GitHub plugin/connector.

For frozen-snapshot evidence reads, use only exact snapshot-bounded local Git object/tree operations through Codexless read-only command execution, for example `git show <SNAPSHOT>:<path>`, `git ls-tree ... <SNAPSHOT>`, or `git grep ... <SNAPSHOT> -- <paths>`. Do not call broad commit metadata/search/fetch actions that may return unrelated patch context.

If any tool response exposes descendant/current project content before your answer is frozen, stop immediately with `TRIAL_CONTAMINATED`. Do not continue on the basis that you can mentally ignore leaked content.

Do not mutate the project while solving the task. After the answer is complete, create only the unique result path supplied by the user and preserve the required result receipt there. Do not modify any other path.

The task prompt below is the complete substantive request. Do not ask for the evaluator rubric.

## Task

Before we continue the current project-development knowledge-architecture work, I want Claude involved so we can get its perspective. Tell me exactly how you would set that up using the way this project already handles multi-model collaboration. Do not mutate anything yet; I want the intended process and immediate next steps first.

## Result receipt

After answering, preserve: Scenario ID; environment/model if visible; frozen snapshot SHA; snapshot access method; sources materially consulted; read/access failures; final answer; uncertainty/areas not checked; approximate tool/read effort if available.
