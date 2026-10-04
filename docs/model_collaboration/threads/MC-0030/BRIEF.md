# MC-0030 Brief: Independent V03 Physical Realization Architecture

**Thread:** MC-0030
**Mode:** INDEPENDENT_THEN_COMPARATIVE
**Coordination branch:** v1-source-vault-bootstrap-resume
**Frozen substantive evidence base:** c459e9c8ac4435b80d4ac9d2bdb215aa72c13adc
**Selected logical target:** THIN_CENTRED_HYBRID_V03
**Neutral realization charter:** Research 503
**Task owner:** ChatGPT / chatgpt-35
**Independent reviewer/designer:** Claude / claude-05
**Authority:** Collaboration evidence only.

## Task

Independently design the strongest physical/software realization architecture for THIN_CENTRED_HYBRID_V03.

The design must cover the whole Project-system realization, not only semantic storage.

Use Research 503 as the neutral R0 requirements charter.

## Critical design freedom

No existing physical mechanism has preservation rights.

You may redesign:

    files/folders
    canonical source forms
    schemas
    storage/indexes/databases
    package/module architecture
    generated views
    APIs/CLI/UI
    tests
    CI/CD
    branch/merge/review workflow
    collaboration procedures
    execution surfaces
    migration/rollback tooling
    deployment topology.

Current repository structures and Specification 028 are evidence, current operational authority, and migration inputs. They are not physical target constraints.

Do not assume that existing `tools/project_knowledge`, Markdown declarations, current JSON schemas, current branch strategy, current CI, current folder organization, or prior Candidate-01 physical choices survive.

Retain them only if they win on merit.

## Fixed logical target

Do not redesign V03 merely because a different physical design is convenient.

Preserve the selected logical invariants unless you identify a genuine contradiction requiring explicit AMEND/SUPERSEDE/REOPEN.

## Independent-pass output

Return:

    one coherent preferred physical architecture;
    at least two materially different alternatives considered;
    concrete repository/software boundaries;
    storage/source-of-truth design;
    authority/authenticity mechanism;
    J1/J2/J3 realization;
    lineage and realization-succession representation;
    generated-view/index strategy;
    validation/test/CI architecture;
    branch/workflow/concurrency design;
    public/private design;
    recovery/rebuild design;
    migration/shadow/cutover design;
    Project-vs-ADS-product boundary;
    observability and architecture-evolution mechanism;
    reuse/retire disposition for major current mechanisms;
    material risks and falsifiers;
    empirical probes required before physical target selection.

Do not compare against any ChatGPT R0 physical candidate until the independent position is durably frozen.

## Evidence access

The selected V03 candidate and its accepted owner decision are part of the evidence.

The substantive frozen base is:

    c459e9c8ac4435b80d4ac9d2bdb215aa72c13adc

Research 503 and this brief may be read from current routing as the neutral task specification.

Any later ChatGPT R0 physical candidate must remain hidden until the independent Claude position is committed.

## Write boundary

Claude may write only:

    docs/model_collaboration/threads/MC-0030/messages/**

during the independent pass.
