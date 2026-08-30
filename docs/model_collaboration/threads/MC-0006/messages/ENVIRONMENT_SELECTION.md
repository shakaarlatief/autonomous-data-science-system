# MC-0006 Reviewer Environment Selection

**Date:** 2026-08-30  
**Status:** Historical routing note  
**Authority:** Records why the reviewer environment was changed before the substantive MC-0006 review began. It does not alter the frozen review target.

The initial MC-0006 routing named Claude Code because the review spans architecture plus implementation and the permanent deployment will later require local execution.

Before the review began, the project owner clarified that the normal Claude Project already has full repository access through a custom connector. The project owner then asked normal Claude to compare the two environments for this exact task before any routing change was made.

Claude's environment-selection assessment recommended a split:

```text
normal Claude + repository connector
    perform the read-only adversarial architecture/repository review

Claude Code
    use later for narrow execution-based verification and local Windows deployment work
    when the evidence question genuinely requires command/filesystem execution
```

The rationale was that most MC-0006 questions are architectural and repository-inspection questions, while backup/restore behavior, crash/partial-failure behavior and Windows-specific filesystem semantics may benefit from targeted execution evidence. The normal Claude environment also enforces the no-deployment boundary structurally because it has repository access but not the same direct local-machine execution surface.

The project therefore keeps the exact frozen review target unchanged and routes the substantive MC-0006 review to the existing normal Claude collaboration session. If the review identifies execution-dependent evidence gaps, those should be verified later through a separately scoped execution task rather than silently widening the review itself.
