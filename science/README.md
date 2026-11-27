# Science

Five labeled sources each supply three raw T states to a 15-to-1 magic-state distiller. A failure at one source can flip several of its states together. The protocol assigns the three states from each source to specific injection slots so the distiller's four existing checks reveal as much as possible about those shared failures.

For independent whole-source bursts of equal probability $p$, zero-syndrome postselection accepts with probability $(1-p)^5+p^5$. The accepted state's infidelity is $p^5/[(1-p)^5+p^5]$. A layout containing a collinear source triple gives first-order infidelity under the same test. The chosen layout also minimizes the number of accepted logical faults caused by one whole-source burst and one distinct source's two-state burst, among layouts achieving fifth-order suppression.

| Page | What it establishes |
| --- | --- |
| [Model](model.md) | The ideal 15-to-1 gadget, the input fault model, and the charged resources. |
| [Routing and decisions](routing.md) | The explicit slot assignment, its maximal syndrome information, and the exact fidelity–yield tradeoff under whole-source noise. |
| [Phase-tied receivers](phase-tied-receivers.md) | Parity projections that recover the same burst syndrome under coherent phase drift, the four-tie yield tradeoff, and the deterministic mismatch law. |
| [Partial bursts and local faults](noise.md) | Sharp limits on partial bursts and exact performance when every slot independently adds a local fault. |
| [Larger Reed–Muller gadgets](scaling.md) | A general construction and an equally sized source assignment for an infinite family. |
| [Supply scheduling](scheduling.md) | A serialized feeder comparison that counts storage, waiting and rejected attempts. |

The fixed-gadget results count every raw input, including inputs to rejected attempts. A hardware comparison also needs the cost of moving and buffering states, the error rates of the checks and correction, and a source noise model that can be validated experimentally.

[Related work](../references/RELATED_WORK.md) · [Verification](../verification/README.md)
