# Research 014: LangGraph 1.2.10 released durability comparator audit

**Date:** 2026-08-22  
**Status:** Current pre-implementation runtime-bakeoff evidence; no runtime selection  
**Scope:** Verifies the currently released LangGraph ecosystem and narrows the ADS durability comparator before implementation.  
**Design session:** 03  
**ChatGPT project:** Autonomous Data Science System  
**Session title:** 03 - Project Cockpit & V1 Integration

## 1. Why this audit exists

The OpenAI candidate exposed a concrete documentation/package mismatch during implementation. The LangGraph comparator therefore begins from released package evidence rather than assuming the current documentation and the installed distribution are identical.

The purpose is not to decide in favor of LangGraph from its documented feature list. It is to identify the exact released surfaces that must be exercised under the same ADS-owned Specification 005 workload.

## 2. Current released package family

Verified on 2026-08-22:

```text
langgraph                    1.2.10   PyPI release 2026-07-28
langgraph-checkpoint-sqlite  3.1.1    PyPI release 2026-07-30
langchain-mcp-adapters       0.3.1    PyPI release 2026-07-27
```

The LangGraph package currently declares Python >=3.10 and depends on the LangGraph checkpoint package family, LangChain Core, LangGraph SDK, and prebuilt support. SQLite checkpoint persistence remains a separate installable package.

Primary release/source evidence:

```text
https://pypi.org/project/langgraph/
https://github.com/langchain-ai/langgraph/blob/main/libs/langgraph/pyproject.toml
https://pypi.org/project/langgraph-checkpoint-sqlite/
https://pypi.org/project/langchain-mcp-adapters/
```

The comparator should pin these released versions in its experiment workflow rather than promote them into unconditional production dependencies.

## 3. Persistence boundary

Current LangGraph persistence documentation separates:

```text
Checkpointer
    thread-scoped graph state snapshots
    human-in-the-loop
    resume/replay/fault tolerance

Store
    application-defined cross-thread data
```

A stable `thread_id` is the cursor used to retrieve a persisted graph execution. In-memory checkpointers do not survive process restart. The current docs explicitly identify SQLite as a persistent local checkpointer option.

For the ADS comparator:

```text
LangGraph checkpointer
    candidate runtime execution state only

ADS operational/project database
    project/domain/methodological authority
```

This distinction is mandatory. LangGraph checkpoint state must not become the project source of truth.

## 4. Interrupt and replay semantics

The current official interrupt documentation states that when a node calls `interrupt()`:

```text
1. execution pauses
2. graph state is checkpointed
3. the caller receives the interrupt payload
4. resume uses Command(resume=...)
5. the interrupted node restarts from its beginning
6. code before interrupt() executes again
```

This is especially important for ADS because retry/replay semantics are not the same as domain exactly-once meaning.

Official guidance explicitly says side effects before `interrupt()` must be idempotent.

The comparator must prove this behavior experimentally rather than relying only on the documentation.

Primary source:

```text
https://docs.langchain.com/oss/python/langgraph/interrupts
```

## 5. Functional API durability option

The current Functional API exposes `@entrypoint` and `@task` over the same checkpoint/runtime substrate.

Documented behavior relevant to ADS:

```text
entrypoint
    can be checkpointed and interrupted

task
    task outputs are checkpointed
    completed task results can be reused during replay/resume
    side effects/non-deterministic work should be isolated into tasks
```

This may reduce the practical cost of entrypoint replay while retaining the runtime's durable execution model.

However, the first comparator should make replay semantics visible rather than hiding them completely. A small Graph API workload is therefore useful for directly testing node restart, while Functional API task isolation remains an architectural option to evaluate if the raw graph replay burden is material.

Primary source:

```text
https://docs.langchain.com/oss/python/langgraph/functional-api
```

## 6. Retry and timeout surface

LangGraph 1.2 documents retry and timeout policies at node/task level.

Relevant released/current API concepts include:

```text
RetryPolicy
    retry_on
    max_attempts
    initial_interval
    backoff_factor
    max_interval
    jitter

async node/task timeout
    hard run timeout / TimeoutPolicy
    NodeTimeoutError
```

The comparator should exercise retry/timeout on bounded async read-only work. Authoritative side effects remain protected at the ADS application boundary regardless of runtime retry behavior.

Primary sources:

```text
https://docs.langchain.com/oss/python/langgraph/fault-tolerance
https://reference.langchain.com/python/langgraph/types/RetryPolicy
```

## 7. MCP integration surface

Current LangChain MCP integration is provided by `langchain-mcp-adapters` rather than LangGraph core.

The released adapter supports local stdio subprocess connections through `MultiServerMCPClient`, which converts MCP tools into LangChain tools usable in workflows/agents.

For ADS this is a material dependency/coupling distinction:

```text
OpenAI candidate
    MCPServerStdio is in the OpenAI runtime package surface

LangGraph comparator
    current practical MCP path adds langchain-mcp-adapters
```

This does not disqualify LangGraph, but it belongs in complexity scoring.

Primary source:

```text
https://docs.langchain.com/oss/python/langchain/mcp
```

## 8. Known current ecosystem evidence to retain

Current public issue/release evidence shows the LangGraph ecosystem is actively evolving around checkpoint behavior and SDK compatibility. That is not itself a failure, but it reinforces the need to pin and test the released package set.

The comparator should not infer durability quality from the word "checkpoint" alone. It should mechanically test:

```text
process-boundary resume from SQLite
interrupt-node restart
read/tool replay behavior
side-effect placement
ADS idempotency under replay
retry and timeout behavior
normalized ADS provenance
```

## 9. Comparator design selected for implementation

The first executable LangGraph slice should use a small explicit Graph API workflow because it makes checkpoint/restart semantics inspectable.

Candidate shape:

```text
START
  -> principal_reasoner
       -> inspect_project_fact
       -> principal_reasoner
       -> lookup_methodological_reference
       -> principal_reasoner
       -> approval/proposal node
            interrupt before authoritative side effect
       -> principal_reasoner
       -> structured recommendation
       -> END
```

Properties:

```text
one principal reasoner
provider-neutral deterministic reasoner double
SQLite checkpoint file
stable thread_id
new runtime/checkpointer instance on resume
ADS ProposalLedger outside graph authority
normalized ADS RuntimeTrace
candidate types isolated below experiments/runtime_bakeoff/candidates/langgraph/
```

The approval node should deliberately record a harmless pre-interrupt execution counter so the test can prove that the node restarts on resume. The authoritative proposal must occur only after the interrupt and through `ProposalLedger.create_once(...)`.

## 10. Decision status

No runtime is selected.

The released audit keeps LangGraph decision-relevant because its durable checkpoint model is materially different from both the explicit direct-call token and OpenAI `RunState` paths.

The next step is executable evidence, beginning with durability/interrupt/replay behavior and then completing AR-01 through AR-12 if the candidate remains viable.
