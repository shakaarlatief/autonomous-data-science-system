from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def append_once(path: Path, marker: str, block: str) -> None:
    text = path.read_text(encoding="utf-8")
    if marker in text:
        return
    path.write_text(text.rstrip() + "\n\n" + block.strip() + "\n", encoding="utf-8")


def replace_required(path: Path, old: str, new: str) -> None:
    text = path.read_text(encoding="utf-8")
    if old not in text:
        raise RuntimeError(f"Required text not found in {path}: {old!r}")
    path.write_text(text.replace(old, new, 1), encoding="utf-8")


def main() -> None:
    decisions = ROOT / "docs" / "DECISIONS.md"
    open_questions = ROOT / "docs" / "OPEN_QUESTIONS.md"
    major_changes = ROOT / "docs" / "MAJOR_CHANGES.md"

    append_once(
        decisions,
        "## D-034. Adopt governed provider-neutral multi-model development collaboration",
        r'''
---

## D-034. Adopt governed provider-neutral multi-model development collaboration

**Status:** Accepted  
**Date:** 2026-08-26

ADS development may use multiple strong AI collaborators under one provider-neutral repository-governed method rather than informal model switching.

The accepted architecture is:

```text
repository remains project authority
SOLO work remains first-class
collaboration is selective and task-scoped
one bounded task owner
ROLE != WRITE_SCOPE
one target-state write owner at a time
explicit secondary write surfaces
machine-readable collaboration-state coherence guard
GitHub issue / PR transport != authority
numbered repository messages preserve durable collaboration provenance
independent-first review uses accepted pre-proposal refs when independence matters
known contamination is disclosed rather than erased
deferred review preserves exact targets and named gate boundaries
human arbitration is reserved for genuine project-intent / consequential choices
provider-local interaction session IDs such as chatgpt-06 / claude-01
```

Specification 024 is accepted with final classification:

```text
COLLABORATION_STATE_GUARD_ACCEPTED
```

The guard is a coherence mechanism, not authenticated model identity or a distributed lock.

Review/collaboration modes include SOLO, REVIEWED, INDEPENDENT_THEN_COMPARATIVE, COORDINATED_HANDOFF, and ADVERSARIAL_REVIEW. Expensive independent/comparative review is selective rather than mandatory.

When one collaborator is temporarily unavailable, intended review may be deferred only until its explicit gate. The affected review target must be frozen to an exact immutable Git ref. Unrelated bounded work may continue. Review of ancestor X does not imply review of descendant Y.

Unattended scheduled model review and API orchestration are explicitly **not** part of the current accepted method. Both remain deferred until measured coordination burden, write isolation, product capabilities, or economics justify the extra machinery.

### Rationale

The decision was pressure-tested rather than accepted from a single proposal.

```text
MC-0001
    ChatGPT proposal + Claude independent/comparative challenge
    exposed candidate-content leakage and single-global-writer over-coarseness

MC-0002
    direct Claude implementation review of Specification 024
    all MC-G01 through MC-G16 satisfied

MC-0003
    real deferred-review backlog with two simultaneous Claude obligations
    processed later in priority order with separate exact targets/dispositions
```

The method produced real marginal value: each model identified substantive weaknesses in the other's initial design, both revised positions, and the first asynchronous catch-up workflow worked without user transcript relay.

Known future mechanization triggers are preserved without premature implementation:

```text
cross-thread dependency metadata / downstream impact discovery
review-inbox generation or consistency checking if real drift appears
secondary-vs-secondary write-surface overlap if simultaneous secondary writers appear
explicit review-obligation/gate fields if backlog scale justifies schema support
```

See:

```text
docs/DEVELOPMENT_METHOD.md version 0.5
docs/CONTINUITY.md
docs/model_collaboration/README.md
docs/model_collaboration/DEFERRED_REVIEW_AND_CATCHUP.md
docs/model_collaboration/INTERACTION_PROVENANCE_AND_NAMING.md
docs/model_collaboration/threads/MC-0001/RESOLUTION.md
docs/specifications/024_v1_model_collaboration_state_guard.md
docs/model_collaboration/threads/MC-0002/RESOLUTION.md
docs/model_collaboration/threads/MC-0003/RESOLUTION.md
docs/checkpoints/204_multimodel_collaboration_method_promoted.md
```
''',
    )

    open_text = open_questions.read_text(encoding="utf-8")
    if "**Last reconciled:** 2026-08-24" in open_text:
        open_text = open_text.replace(
            "**Last reconciled:** 2026-08-24",
            "**Last reconciled:** 2026-08-26",
            1,
        )
    open_questions.write_text(open_text, encoding="utf-8")

    append_once(
        open_questions,
        "### Q-054. How far should governed multi-model collaboration be mechanized?",
        r'''

---

## Multi-model development and collaboration

### Q-054. How far should governed multi-model collaboration be mechanized?

**Status:** Core collaboration method accepted; further mechanization deliberately open

Development Method v0.5, D-034, Specification 024, and MC-0001 through MC-0003 establish the current human-supervised provider-neutral collaboration method.

Current accepted boundary:

```text
repository-mediated collaboration
selective SOLO / REVIEWED / independent-comparative modes
one task owner + scoped write ownership
machine-readable per-thread coherence guard
manual or issue-assisted asynchronous transport
deferred review with exact immutable targets and explicit gates
human arbitration for genuine project-intent/consequential choices
```

The following remain open and should be implemented only when real use justifies them:

```text
cross-thread dependency metadata and downstream impact discovery
generated REVIEW_INBOX / inbox-state consistency validation
secondary-vs-secondary write-surface overlap protection
machine-readable review-obligation and gate-boundary fields
stale/superseded deferred-obligation validation
whether recurring backlog scale eventually justifies stronger orchestration
```

Unattended scheduled model review is currently deferred rather than accepted. It does not create additional weekly subscription capacity and currently adds unattended write/concurrency, clarification, and budget-consumption risk.

Programmatic OpenAI/Anthropic API orchestration is also deferred. Reopen only when measured manual coordination burden or automated-review value justifies separately metered usage, credentials, context duplication, retries, and orchestration infrastructure.

No Specification 025 is justified yet.
''',
    )

    replace_required(
        major_changes,
        "**Last reviewed:** 2026-08-25",
        "**Last reviewed:** 2026-08-26",
    )

    append_once(
        major_changes,
        "## 2026-08-25 to 2026-08-26: Governed multi-model development became canonical",
        r'''

---

## 2026-08-25 to 2026-08-26: Governed multi-model development became canonical

The ADS development method expanded from one ChatGPT-centered interaction process into provider-neutral governed collaboration among ChatGPT, Claude, the human project owner, and future collaborators.

The architecture was pressure-tested through three real threads rather than promoted from one model's proposal:

```text
MC-0001
    independent/comparative architecture review
    -> exposed candidate-content leakage and single-global-writer weakness

Specification 024 / MC-0002
    -> machine-readable per-thread coherence guard
    -> direct Claude implementation review
    -> COLLABORATION_STATE_GUARD_ACCEPTED

Research 036 / MC-0003
    -> explicit deferred review/catch-up
    -> two pending Claude obligations coexisted
    -> later processed in priority order with exact-target discipline
```

Development Method v0.5 now makes SOLO work first-class, collaboration selective, task ownership explicit, role separate from write scope, independent review contamination visible, disagreement routable, and provider-neutral interaction provenance mandatory for new checkpoints from Checkpoint 204 onward.

The source-vault deployment remains paused rather than cancelled.

Unattended scheduled model review and API orchestration remain deferred. Known future collaboration-mechanization triggers are preserved without opening Specification 025 prematurely.

Key sources:

```text
docs/DEVELOPMENT_METHOD.md
docs/CONTINUITY.md
docs/DECISIONS.md, D-034
docs/checkpoints/204_multimodel_collaboration_method_promoted.md
docs/model_collaboration/README.md
docs/model_collaboration/threads/MC-0001/RESOLUTION.md
docs/specifications/024_v1_model_collaboration_state_guard.md
docs/model_collaboration/threads/MC-0002/RESOLUTION.md
docs/model_collaboration/threads/MC-0003/RESOLUTION.md
```
''',
    )


if __name__ == "__main__":
    main()
