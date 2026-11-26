# Model

## The 15-to-1 distiller

Use the standard 15-to-1 T-state distiller with four binary X checks. Its raw-state injection slots have the fifteen nonzero labels of $`\mathbb F_2^4`$. We represent a label by the integer whose four binary digits give its coordinates. For example, the three labels 1, 2, 3 XOR to zero. The ideal raw state is $`|T\rangle=T|+\rangle`$, and an input fault replaces it with the orthogonal state $`Z|T\rangle`$.

In the phase-gadget description, the injection at slot $v$ implements a $`\pi/8`$ Pauli rotation. The Pauli is Z on the output wire and on each of the four check wires for which the corresponding bit of $v$ is 1. A fault in an injected T state adds that Pauli, up to an irrelevant phase after the usual injection feed-forward. Multiplying the Pauli faults of a physical fault set $F$ gives its check syndrome $`s(F)`$ and output fault bit $`\ell(F)`$.

```math
s(F)=\bigoplus_{v\in F}v,\qquad
\ell(F)=|F|\bmod 2 .
```

The check wires are measured in X. The output differs from the ideal T state by $`Z^{\ell(F)}`$ after the fixed ideal output convention is applied. The raw states themselves are consumed by injection. See the circuit references in [Related work](../references/RELATED_WORK.md).

## Source bundles and fault models

A layout partitions the 15 slot labels into five disjoint sets $`B_1,\ldots,B_5`$, each of size three. Source $j$ supplies the states assigned to $`B_j`$. The assignment is made before the fault history is known. The receiver observes the four syndrome bits and knows the assignment and the assumed noise distribution.

In the whole-burst model, source $j$ contributes $`B_j`$ to $F$ when its fault bit $`b_j`$ is 1. The five-bit history may follow any joint law. The exact expressions in terms of a single rate $p$ assume that the five bits are independent Bernoulli variables with that common rate. Simultaneous whole bursts multiply their Pauli Z faults. Partial source bursts and independent extra per-slot faults are introduced separately in [Partial bursts and local faults](noise.md).

## Outputs and cost

After measuring a syndrome the receiver may reject the attempt or keep the state with a logical Z correction of its choice. Yield $A$ is the probability of keeping the output. Output infidelity is the probability of a residual logical Z conditional on keeping the output. The model makes the output a mixture of the intended pure state and its orthogonal Z partner, so these definitions agree with the usual pure-target state fidelity.

Each attempt uses 15 raw states and the original four checks. When retries are independently drawn and use the same decision rule, the expected raw-state cost of an accepted output is $`15/A`$. For correlated rounds the one-attempt rates still hold with their stated marginal distribution, and the waiting-time cost depends on the temporal law. Physical permutation, storage, routing and imperfect check costs require an architecture model.

[Routing and decisions](routing.md) · [Verification](../verification/README.md)
