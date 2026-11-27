# Quantum Magic Burst Routing

**Can a 15-to-1 magic-state factory detect correlated source failures by changing only which input slots the sources feed?** When five sources must each supply three raw $`T`$ states, their output bundles can be assigned to the existing injection slots so that the four standard checks distinguish every whole-bundle fault pattern up to its complement.

For independent sources that each flip their entire bundle with probability $`p`$, the factory accepts only when no source fails or all five fail. The latter event flips the output state. The acceptance probability and the conditional infidelity are

```math
A=(1-p)^5+p^5,\qquad \epsilon=\frac{p^5}{A}.
```

| Result | What the assignment achieves |
|---|---|
| Whole-bundle faults | Fifth-order suppression at zero syndrome. A bundle placed on a zero-syndrome triple can give a first-order error. |
| Syndrome-dependent acceptance | The four checks retain the maximum information attainable by any placement of the five bundles. Each syndrome determines a pair of complementary source histories. |
| Partial bundles | Every fault confined to one source is detected. Among fifth-order placements, the assignment minimizes the number of undetected events consisting of one whole bundle and two states from another source. |
| Independent per-input faults | A closed form gives the acceptance and output error when independent local flips are added. Mixed terms can dominate the fifth-order term. |

The result uses 15 raw states and the usual checks per attempted output. Rejected attempts count toward cost. Slot assignment can leave the logical check circuit fixed, but physical delivery, waiting and faulty checks require their own accounting. The [schedule analysis](science/scheduling.md) makes that accounting explicit for a serial injection port.

## Sister project

[Quantum Common-Mode Magic Distillation](https://github.com/GoGoKo699/Quantum-Common-Mode-Magic-Distillation) extracts a T state by preserving coherence between two strings with the same unknown phase. The [phase-tied receiver](science/phase-tied-receivers.md) uses that projection to measure the same complementary burst histories as the routed factory when the 15 inputs also carry continuous phase drift. Four phase ties suffice for fifth-order suppression, and a fifth improves the displayed yield by a factor of 16.

## Read the science

Start with the [circuit, fault model and claims](science/model.md). The [routing theorem](science/routing.md) gives the five bundles and derives the reliability–yield tradeoff. The [noise analysis](science/noise.md) proves the partial-burst optimum and evaluates independent local errors. The [larger Reed–Muller construction](science/scaling.md) extends the mechanism to more sources with an explicit raw-state budget. The [science index](science/README.md) connects these results to the [prior work](references/RELATED_WORK.md).

## Learn the project

The [30-milestone map](learning/MILESTONES.md) traces the argument from binary Pauli syndromes to source-aware input assignment, phase-tied extraction and resource accounting. The single educational anchor is Daniel Gottesman's *An Introduction to Quantum Error Correction and Fault-Tolerant Quantum Computation*. The [Gottesman bridge](learning/GOTTESMAN_BRIDGE.md) maps its stabilizer, transversal-gate and injection sections to the proofs.

Use the [learning entry point](learning/README.md) for a self-directed route or the [LLM reading guide](llms.txt) to locate a claim or derivation.

## Reproduce the finite checks

```bash
python3 verification/run_all.py
python3 verification/check_phase_ties.py
```

The [verification guide](verification/README.md) identifies the enumerated fault histories, exact probability comparisons, phase-tied receivers and larger constructions. The written proofs supply the general statements.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
