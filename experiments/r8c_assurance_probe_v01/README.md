# R8-C Assurance Decision Probe Harness

Temporary research/qualification machinery for the decision-relevant R8-C probes preregistered in Research 277.

This directory is evidence infrastructure only. It has no target-architecture preservation right.

## P-D6

p_d6_executor_capability.py tests executor-capability versus trust separation.

## P-D3

p_d3_boundary_independence.py implements the preregistered two-layer Product/JW1 boundary-independence probe with explicit import scans, target-shaped isolated execution, and forbidden-dependency controls.

## P-D5

p_d5_adapter_fidelity.py tests consumer-side normalization of a native pytest JUnit XML result path and the JW1 project-knowledge CLI JSON result contract across pass/fail/error/zero/skipped/truncated/unmatched cases, with intentionally faulty adapters as witnesses.

Every concrete probe harness must be committed and Git-blob-hash frozen before execution.
