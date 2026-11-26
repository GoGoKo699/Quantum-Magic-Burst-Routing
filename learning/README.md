# Learning Quantum Magic Burst Routing

A 15-to-1 factory has four syndrome checks and fifteen input slots. This project asks how much those checks can tell us when each of five sources supplies three inputs and faults can strike a whole source bundle. The learning route starts with gate teleportation and parity checks, then follows the input assignment through exact error rates, partial faults, and scheduling.

| Resource | Use it to |
|---|---|
| [30-milestone map](MILESTONES.md) | Follow the argument from physical inputs to the conditions under which routing helps. |
| [Gottesman bridge](GOTTESMAN_BRIDGE.md) | Connect stabilizer checks, logical Paulis, and ancilla preparation to the factory notation. |
| [Scientific account](../science/README.md) | Read exact assumptions, constructions, and proofs. |
| [Verification](../verification/README.md) | Reproduce the finite pattern checks and compare them with the analytical formulas. |

Start at [M01](MILESTONES.md#m01-the-t-state) for the full route. Readers comfortable with stabilizers and gate teleportation can check their understanding at [M12](MILESTONES.md#m12-the-single-block-design-question), then follow the routing argument from [M13](MILESTONES.md#m13-a-bundle-induces-one-check-column).
