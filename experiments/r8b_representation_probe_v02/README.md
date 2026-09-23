# P-R8B-01-R2 Corrected Representation Probe

This directory contains the corrected successor harness required by Research 266 after the MC-0027 adversarial audit.

The original `experiments/r8b_representation_probe_v01/` harness is preserved unchanged.

The corrected harness:

- reruns all original Research 263 blocking gates;
- replaces the seven invalid gate implementations identified by Claude;
- strengthens the four weak-but-directional gates where bounded;
- adds amendment gates for WMR-H V0.3 A-M1 and A-M2;
- binds results to exact Git-blob hashes at a named harness commit;
- treats the current harness as temporary research/qualification machinery, not future assurance architecture.

Execution must occur only after the harness commit and a separate freeze record have been created and pushed.
