# Specification 014 frozen live result manifest

This directory is the durable repository copy of the complete artifact produced by the frozen live run.

```text
GitHub Actions workflow: V1 reasoning context value live
workflow run:           32635061634
successful run attempt: 2
source head:            3592cc3bd91e0aae7e5c667fa0c762ae4acd5395
artifact id:            9492191878
artifact name:          v1-reasoning-context-value-3592cc3bd91e0aae7e5c667fa0c762ae4acd5395-2
artifact ZIP SHA-256:   e2fa6b70915b96b2978c4b2c78c5d16207b09cf7bd1e0bb79a2ea027bba5a30a
```

The first workflow attempt stopped before provider calls because the repository secret was absent. Attempt 2 passed the credential boundary and executed the unchanged frozen experiment. No treatment, rubric, threshold, repetition, or retry-policy change occurred between the preregistration and the successful live execution.

File SHA-256 values were checked before this preservation commit:

```text
RESULT.generated.md                 1ad50b0f48616a4196900ddfcc33956364147df79a7c328770f393f6eda1e988
judge_attempts.jsonl                4a6d89ba5ab4a82ae1be1e18d635e1f1c406701ffebef6973c80099401ccfebc
judge_plan.json                     b4c362d830d82db8f9f3becc63d2adf473df387f9293a3e2462d7279de2efb10
reasoner_attempts.jsonl             1b29b31528523593d96abbcf4a27b654788ce4ca981915a7e2390d4eaa5436bb
reasoning_context_value.sqlite3     41b5b99da1de980de451c0a392cfc50e503cd026639a3bad05e47a3e653adee5
reasoning_plan.json                 025ccc11268ef5b915f90aeaf32d28ee18d5f32a7834a32930a6cbeceaedb5e2
result.json                         84bebdecc9694062cec48ffe5b0cd0d399667b6dfcb17ea79989d3f67927df03
```

The JSON/JSONL files and generated report preserve the reasoning and judge outputs, exact context identities, provider usage, timing, model/runtime identity, plan hashes, and frozen gate evaluation. The SQLite file is the isolated experiment database captured by the runner and is not authoritative reusable-knowledge or project state.
