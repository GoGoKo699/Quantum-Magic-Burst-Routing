# Related work

## The standard 15-to-1 factory

Bravyi and Kitaev established magic-state distillation with the 15-qubit Reed–Muller construction. Bravyi and Haah placed transversal $`T`$ gates and distillation in a triorthogonal-matrix framework. Litinski's phase-gadget circuit provides the concrete model used here. In its 15 injected rotations, the output Pauli support is common and the four check-wire Pauli supports range over the nonzero four-bit vectors. The project inherits this circuit and its binary fault propagation. See [Bravyi and Kitaev](https://doi.org/10.1103/PhysRevA.71.022316), [Bravyi and Haah](https://doi.org/10.1103/PhysRevA.86.052329) and [Litinski, Fig. 3 and §1](https://doi.org/10.22331/q-2019-12-02-205).

## Correlated faults and factory network design

O’Gorman and Campbell place correlated outputs of an earlier branch into different Bravyi–Haah blocks and use module checking to track errors across a factory. Their two-round analysis tracks the patterns that can pass simultaneous checks when two branches fail. The placement problem here fixes one block, a known partition of its inputs by source, and the number of inputs each source must supply. The optimized four-bit syndrome and the partial-burst count concern that within-block constraint. See [O’Gorman and Campbell, Fig. 2 and Appendix F](https://doi.org/10.1103/PhysRevA.95.032338).

Meier, Eastin and Knill likewise discuss routing outputs from a given distillation instance to different downstream instances when their errors can be correlated. This gives an important baseline if enough separate output batches and downstream blocks can be scheduled. The [scheduling analysis](../science/scheduling.md) accounts for those requirements in a finite benchmark. See [Meier, Eastin and Knill](https://arxiv.org/abs/1204.4221).

## Fault-pattern formulations

Balada Gaggioli and Mareček frame distillation in terms of fault patterns that a stabilizer protocol rejects or maps to the target, and give bounds on the minimum raw-state count for prescribed independent-input suppression orders. Their framework also treats prescribed sets of patterns and, in composite constructions, faults with different costs at different units. It supplies a general formulation for asking which source faults are harmless. The [routing theorem](../science/routing.md) solves the distinct assignment problem for a specific check circuit and gives the full syndrome comparison. The [partial-burst bound](../science/noise.md) fixes the circuit and optimizes the number of particular two-source failures. See [Balada Gaggioli and Mareček, Theorem 1 and §IV](https://arxiv.org/html/2610.31115v1).

## Coherent phase cancellation

Debroy and colleagues choose stabilizer signs so coherent idling errors cancel in encoded Shor memories. The [phase-tied receiver](../science/phase-tied-receivers.md) instead receives prepared equatorial product states. The signed parity projections use specified equalities among the accumulated phases to measure relative burst bits and extract one T state. The construction transfers the entire complementary-history decision frontier to that input model. [Debroy et al., *Physical Review Letters* **127**, 240501 (2021)](https://doi.org/10.1103/PhysRevLett.127.240501)

Wang and colleagues characterize a five-to-one distiller's polarization and acceptance in terms of moments after local Clifford twirling. The phase-tied receiver uses coherence between selected computational strings before measuring the burst comparisons. Its deterministic mismatch law gives the error probability of each comparison separately. [Wang et al., arXiv:2610.36963](https://arxiv.org/abs/2610.36963)

## Physical correlations and educational source

Correlated device faults can arise from mechanisms such as bursts of quasiparticles. Such observations motivate examining correlated inputs and do not identify the five-source model with the noise of a particular device. The pure whole-bundle model and mixed partial-fault law have separate assumptions. See [McEwen et al.](https://doi.org/10.1038/s41567-021-01432-8).

The [Gottesman bridge](../learning/GOTTESMAN_BRIDGE.md) uses §§2–4 of Gottesman's introduction for the stabilizer and fault-tolerance background. Gottesman provides the vocabulary and propagation rules. The present routing assignment and its proofs are developed in the science pages. See [Gottesman](https://arxiv.org/abs/0904.2557v1).
