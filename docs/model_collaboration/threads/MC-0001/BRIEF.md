# MC-0001 Neutral Brief: Multi-Model Development Collaboration

**Thread:** MC-0001  
**Purpose:** Neutral problem statement for an independent first-pass design  
**Important:** A reviewer performing Phase A should read this brief and the accepted governing project-method documents, but should **not** read Research 035 or the proposer's detailed architecture until the independent proposal has been durably recorded.

## Problem

The Autonomous Data Science System has so far been developed primarily through ChatGPT plus the human project owner, with Git/GitHub and structured repository artifacts acting as durable project memory.

The project owner now wants to use both ChatGPT and Claude as serious development collaborators.

The collaboration method should be professional, scalable, efficient, auditable, and genuinely epistemically useful rather than merely producing duplicated opinions.

## Existing conditions

The current project already has:

```text
repository-as-source-of-truth continuity
canonical documents
research/foundations/specifications/checkpoints
active branch and PR routing
a development method with proactive preservation
explicit promotion audits
Git history and CI
human project ownership
```

The current development process and checkpoint provenance are still partly ChatGPT-specific.

The user currently has interactive access to both ChatGPT and Claude through their product subscriptions. Fully automated API orchestration is technically possible later but would add separate metered usage and engineering complexity.

## Requirements

Design a collaboration method that addresses at least:

1. how both models reconstruct project state;
2. how task ownership is assigned;
3. how concurrent/conflicting writes are prevented;
4. how one model reviews or challenges another;
5. how genuine independence is preserved where valuable;
6. how agreement bias and performative disagreement are both controlled;
7. how material disagreement is represented and resolved;
8. when the human must decide;
9. how the models can communicate efficiently without the user constantly copy-pasting messages;
10. whether a dedicated model-to-model communication surface should exist;
11. what should be preserved from model-to-model exchanges;
12. how review connects to branches, PRs, checkpoints, and canonical promotion;
13. how the method avoids excessive bureaucracy;
14. how it remains provider-neutral enough to support future models/tools;
15. when, if ever, API orchestration should be introduced;
16. how to determine whether using a second model actually improves development quality.

## Constraints

- The repository remains the durable project source of truth.
- Raw model output is not automatically canonical authority.
- The human project owner must not become a permanent transport clerk.
- Two models should not independently corrupt canonical state.
- No design should assume model consensus equals truth.
- No design should require API orchestration at this stage unless it can justify that complexity.
- The process should be proportionate: high-impact architecture may deserve stronger review than trivial mechanical work.
- Existing project history and accepted specifications must remain auditable.

## Phase-A output requested from reviewer

Without reading Research 035, propose the collaboration architecture you would choose.

Please include:

```text
your preferred architecture
role/ownership model
communication mechanism
review/independence mechanism
disagreement protocol
human role
branch/PR coordination
preservation/authority model
efficiency safeguards
API-orchestration boundary
largest risks in your own proposal
what evidence would make you revise it
```

Do not optimize for agreement with ChatGPT. Do not optimize for disagreement either.

The goal is your best independent design from the requirements above.