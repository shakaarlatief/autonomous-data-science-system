# R8-C Assurance Decision Probe Harness

Temporary research/qualification machinery for the decision-relevant R8-C probes preregistered in Research 277.

This directory is evidence infrastructure only. It has no target-architecture preservation right.

## P-D6

p_d6_executor_capability.py tests executor-capability versus trust separation.

## P-D3

p_d3_boundary_independence.py implements the preregistered two-layer Product/JW1 boundary-independence probe with explicit import scans, target-shaped isolated execution, and forbidden-dependency controls.

## P-D5

p_d5_adapter_fidelity.py tests consumer-side normalization of a native pytest JUnit XML result path and the JW1 project-knowledge CLI JSON result contract across pass/fail/error/zero/skipped/truncated/unmatched cases, with intentionally faulty adapters as witnesses.

## P-D1

p_d1_claims.json contains the twelve claims selected and frozen in Research 291 before warrant authoring. p_d1_warrant_proportionality.py validates selective claim grain, executes sensitivity/specificity witnesses for all four invariant claims, and runs sampled mutation adequacy against the Product reasoning suite.

## P-D2

p_d2_history_labels.json contains the ten real historical changes and independent semantic labels frozen in Research 294 before classifier authoring. p_d2_ratchet_history.py verifies exact Git patch bindings, classifies only normalized policy deltas, exercises witness-removal and patch-drift negative controls, and proves exact owner-batch policy-diff digest binding.

## P-D4

p_d4_oracle_corpus.json freezes the real current-routing oracle corpus before successor design. p_d4_successor_contract_v02.json freezes the representation-independent successor claims and controls before implementation. p_d4_oracle_successor.py replays the frozen old oracle, translates compatibility inputs into ROUTING_ASSURANCE_SUBJECT_V1, evaluates the independent successor classifier, and exercises direct translated-representation and semantic-completeness controls.

Every concrete probe harness must be committed and Git-blob-hash frozen before execution.
