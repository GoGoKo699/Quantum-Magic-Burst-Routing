# From Gottesman’s stabilizer tutorial to burst routing

The educational anchor is Daniel Gottesman, *An Introduction to Quantum Error Correction and Fault-Tolerant Quantum Computation*, [arXiv:0904.2557v1 (16 April 2009)](https://arxiv.org/abs/0904.2557v1). The [HTML](https://arxiv.org/html/0904.2557v1) and [PDF](https://arxiv.org/pdf/0904.2557v1) give the sections below.

## Read the parts that carry the argument

| Section in Gottesman | What to extract | Where it enters the project |
|---|---|---|
| §2.3, especially Theorem 5 | A generator measurement records whether an error commutes or anticommutes. Errors share a syndrome when their product has trivial syndrome. | [Check signs and output parity](../science/model.md) |
| §3.1, binary parity-check and seven-qubit examples | A matrix column gives the syndrome of one error. Adding columns gives the syndrome of several errors. | [Input labels and source-bundle columns](../science/routing.md) |
| §§3.4–3.5 | Logical Paulis act on encoded information. Clifford conjugation maps Paulis to Paulis. | [Which accepted faults flip the output](../science/model.md) |
| §§4.1 and 4.3 | Propagate errors through the operation that follows them. Treat preparation, measurement, and waiting as physical locations when modeling implementation. See how transversal gates constrain error spread. | [Physical injection and scheduling assumptions](../science/scheduling.md) |
| §4.5, Eqs. (70)–(71) and Fig. 6 | The $R_{\pi/8}$ phase gate can be implemented through an ancilla and a measurement-dependent Clifford correction. This gate is denoted $T$ here. | [The magic-state input model](../science/model.md) |
| §4.6 | A known ancilla can be prepared selectively. A rejected syndrome costs a full attempted preparation. | [Acceptance, output error, and retry cost](../science/routing.md) |

## Translate the code picture

| Stabilizer language | Factory language |
|---|---|
| Measurement of a generator returns $+1$ or $-1$. | Encode a sign as a bit, with $1$ marking a flip relative to the ideal check. The gadget supplies four such bits. |
| A binary matrix maps a Pauli error to its syndrome. | A raw $Z$-error mask selects columns labeled by the fifteen nonzero vectors of $\mathbb F_2^4$. The XOR of the selected labels is the observed syndrome. |
| A zero-syndrome error can implement a nontrivial logical Pauli. | If the XOR vanishes and the number of faulty injections is odd, the attempt passes the zero-syndrome filter and a $Z$ error remains on the output. |
| The same syndrome can be shared by multiple error patterns. | The source-burst vector and its complement always share a syndrome. The two histories have opposite output parity in the five-source model. |
| Syndrome-conditioned preparation filters erroneous outcomes. | The factory can accept only the zero record, or use a model-based parity correction and accept a larger set of records. Each choice has an acceptance rate and a conditional output error. |

## Cross from the tutorial to this factory

Gottesman supplies the syndrome and gate-teleportation framework. The 15-to-1 injection circuit comes from the magic-state distillation literature cited in [Related work](../references/RELATED_WORK.md). Its fault-propagation rule is the additional step needed here. Each faulty injection flips the output and toggles the subset of check bits named by its slot. With this rule, the quantum circuit induces a linear syndrome on raw error masks and a separate output parity.

The project changes the input assignment under a source-level noise model. Each source has a physical bundle of three states. The three slot columns of a bundle sum to its source-level syndrome column. Selecting those columns to give a rank-four source map leaves exactly two burst histories per record. The [routing proof](../science/routing.md) establishes the assignment and the decision rule. The [noise analysis](../science/noise.md) explains how partial bundles and independent slot faults change the guarantee.

The tutorial’s treatment of noisy physical locations also motivates the distinction between the ideal circuit and a deliverable schedule. Transport, waiting, imperfect checks, and any correlations introduced by shared hardware need their own model. The [scheduling analysis](../science/scheduling.md) states the cost assumptions used for the comparisons.

Use the [milestone map](MILESTONES.md) to follow the whole argument.
