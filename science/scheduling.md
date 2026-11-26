# Scheduling the same 15 injection slots

Five sources release three raw T states each per production epoch. A feeder that can select any available state for the next injection can exploit this batching inside one distillation attempt. Spreading each bundle across three attempts also fits the same injection slots, but it delays the first output and changes the number of live input states. This benchmark quantifies that difference for a single distiller with a specified feeder.

## Factory interface

[Litinski's factory](https://arxiv.org/abs/1905.06903) separates the 15 phase-gadget rotations and four X checks (Fig. 3) from their physical supply schedule. The two-level implementation uses intermediate storage spots and feeds rotations from upper and lower ancilla regions (Figs. 13–14, §4). The schedule below takes the 15 rotations and four checks as fixed and uses a **serialized** feeder. Its timing and capacity refer to this feeder abstraction. [O’Gorman and Campbell](https://arxiv.org/abs/1605.07197) split correlated branches across blocks and use module checks (§III and Fig. 2). The interleaved comparator here uses only the individual 15-to-1 blocks and their standard checks.

- A production epoch releases one three-state bundle per source, ready at the feeder. Fifteen states arrive at times $0,T,2T,\ldots$. Preparation and delivery up to the feeder are a common upstream cost.
- A feeder has a bank of individually selectable logical input cells. It delivers one state to the next injection in at most $g$ time units, with its transfer and injection both allotted within that slot. A slot's input leaves the bank at the beginning of the slot. Every attempt has the same 15 serial slots followed by a check, reset and output window of length $c\ge 0$, so $T=15g+c$. Rejected attempts still consume the full window and all 15 states.
- The distiller holds one attempt at a time, with a fixed order of slot labels $v_0,\ldots,v_{14}$. Each label is the four-bit check support of that slot's rotation, as in the [model](model.md). Neither the label order, the physical injection operations nor the feeder's maximum transfer time changes across comparators. The feeder needs enough capacity and connectivity for the storage counts below. Equal transfer time is a hardware interface assumption to check on an actual layout.

Register occupancy counts ready states before injection and excludes a state once it enters the common rotation circuit. If a delivery and an injection start coincide, the new arrivals count toward capacity first. The counts do not include the source devices, the distiller's working qubits, or the feeder transfer hardware. Those are common in a comparison with the same feeder built at its largest required capacity.

## Three schedules

**Routed.** At time $eT$, start the attempt for epoch $e$. Inject each state in the appropriate slot of the [five-source assignment](routing.md#an-assignment-for-five-sources). Within a source, any fixed ordering of the three bundle members suffices under whole-bundle noise. At most 15 input states are live. The total state waiting time before injection is $\sum_{j=0}^{14}jg=105g$ per attempt. The first check decision is available at time $T$.

**Collinear assignment.** Use the same schedule and assign the five sources the triples $(1,2,3)$, $(4,8,12)$, $(5,10,15)$, $(6,11,13)$, and $(7,9,14)$. These cover all 15 labels and each triple XORs to zero. The resources are the same as in the routed schedule. This is an explicit baseline for a syndrome-blind assignment. Other untuned assignments can have different reliability.

**Across-block interleaving.** For each successive frame of three production epochs, assign one member of every bundle to each of three attempts. In each attempt, feed the five states from the first epoch to ordered slots $0$–$4$, the five from the second to slots $5$–$9$, and the five from the third to slots $10$–$14$. The attempt starts, relative to the frame start, are $s$, $s+T$, and $s+2T$, where

```math
s=2T-10g .
```

The first attempt cannot start earlier and then run without interruption. It needs five distinct bundles from the third epoch, so at least five of its slots must start at or after $2T$. The latest possible first such slot is slot 10. In the schedule above, slot 5 begins at $s+5g\ge T$, and slot 10 begins at $2T$, so the attempt has all inputs on time. The first decision is available at $s+T$. After this startup delay, attempts run at the same cadence as the other schedules, including across frame boundaries.

The arrival at $2T$ brings the total number of supplied inputs to 45, of which the first ten have been consumed just before that arrival in the displayed schedule. A bank of 35 cells therefore suffices, including all later frames. Once the pipeline is full, each interval of length $T$ between arrivals consumes 15 states, so the post-arrival peak repeats and occupancy decreases between arrivals. This capacity is also necessary for a single distiller under interleaving. Before $2T$ its one in-progress attempt can consume at most ten inputs from the ten distinct bundles that have arrived. The remaining inputs for that attempt become available at $2T$. A common 35-cell feeder allows all three comparisons. With only 15 cells and the prescribed arrivals, the routed and collinear schedules fit.

The total waiting time in a frame is the sum of all 45 injection start times minus the sum of all 45 input arrival times. It is $315g$ for the first two schedules and $315g+45s$ for interleaving, or $105g+15s$ per attempted output on average. At $c=0$, the first interleaved decision comes after $35g$ and the average waiting exposure is $405g$ per attempt. These are occupied input-cell times. If the bank is provisioned statically, its reserved space-time must also be charged at its installed size, including empty cells.

## Yield and fidelity at the same attempt rate

Assume whole-bundle flips are independent across source–epoch pairs with probability $0<p<1/2$, and that storage, the feeder and the distiller introduce no additional faults. Use zero-syndrome acceptance for every schedule. Put $r=1-2p$ and let $A$ be the probability of acceptance and $F$ the infidelity conditional on acceptance. For interleaving, each attempt sees 15 distinct burst variables, so its single-attempt law is the independent input error case of the [local-noise formula](noise.md). Define $A_I=(1+15r^8)/16$ and $C_I=(r^{15}+15r^7)/16$.

| Schedule | $A$ | $F$ | First decision | Peak ready states |
| --- | --- | --- | --- | ---: |
| Collinear assignment | $1$ | $(1-r^5)/2$ | $T$ | 15 |
| Routed | $(1-p)^5+p^5$ | $p^5/A$ | $T$ | 15 |
| Interleaved | $A_I$ | $(A_I-C_I)/(2A_I)$ | $T+s$ | 35 |

Under these assumptions, routing costs the same 15 raw states and one fixed circuit window per attempt as the baselines. Its accepted infidelity is lower than interleaving's for the entire stated interval, and its accept rate is higher. For yield, use $16A_R=1+10r^2+5r^4$ and $16A_I=1+15r^8$. For the infidelity claim, write $16C_R=r^5+10r^3+5r$ so $F_R=(1-C_R/A_R)/2$. The difference of cross-products is

```math
256(C_R A_I-C_I A_R)
=r(1-r^2)^3(r^4+3r^2+1)(5r^8+10r^6+26r^4+10r^2+5)>0.
```

At $p=0.01$, the routed and interleaved marginal infidelities are about $1.05\times 10^{-10}$ and $3.61\times 10^{-5}$, with acceptance rates about $0.951$ and $0.860$, respectively. The collinear assignment accepts every time with marginal infidelity about $0.0480$.

In steady operation, expected output yield is $A/T$. The 45 inputs and three attempt windows per frame give $15/A$ raw states and $T/A$ distiller time per accepted output in the long-run average, including rejected shots. The corresponding input waiting exposure is $105g/A$ for routing and the collinear assignment, and $(105g+15s)/A$ for interleaving. The three interleaved attempts share bundle histories. In this schedule they put the same history in the same slot order, so their decisions and output error bits coincide in the pure whole-burst model. Their marginal fidelity and long-run yield do not give a product guarantee for a group of accepted outputs. More generally, relabeling interleaved blocks can change their joint output law.

## Charging additional faults

One conservative extension assigns a fault bound $\lambda_m$ per occupied buffer cell per time unit, $\lambda_f$ per transfer, and $b_d$ per fixed distiller window. For an attempt with input waiting exposure $W$, a union bound gives probability at most $b=\lambda_mW+15\lambda_f+b_d$ of any additional fault. These bounds are understood for the actual schedule, and may depend on the path or time if the corresponding individual probabilities are summed. In particular, an underestimated transfer path can invalidate a comparison even if it reaches the right logical slot.

Suppose the ideal and noisy experiments can be coupled so their results agree whenever no additional fault occurs, and the output is still evaluated against the same target. If $J=AF$ is the ideal accepted-error mass, then the actual acceptance differs from $A$ by at most $b$, and the actual accepted-error mass differs from $J$ by at most $b$. For $b<A$, a conditional infidelity upper bound is $(J+b)/(A-b)$. For interleaving the three attempt-specific exposures are $105g+15s+15(a-1)T$, where $a=0,1,2$. An averaged bound applies to the marginal of a uniformly chosen attempt in a frame. The bound is conservative because it counts even detected or logically harmless faults. Independent input Z storage faults can instead be propagated through the same checks as in the [noise analysis](noise.md), with rates that may vary by slot. Faults in the checks, time-correlated sources, or a feeder with constrained reachability need their own analysis. The numerical comparison above does not establish a surface-code implementation or a device-level advantage.

[Model](model.md) · [Routing and decisions](routing.md) · [Partial bursts and local faults](noise.md) · [Related work](../references/RELATED_WORK.md)
