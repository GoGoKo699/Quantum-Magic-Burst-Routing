# Partial bursts and local faults

This page uses the slot and syndrome notation in [Model](model.md) and [Routing and decisions](routing.md). All postselection results below use the usual zero-syndrome test with its identity correction. The final section also considers accepting every syndrome with a posterior correction.

## A sharp count for partial bursts

In any fifth-order layout each source triple is noncollinear, meaning its three labels do not XOR to zero. A single affected source can therefore flip any nonempty subset of its triple and will always trigger the checks. Singletons are nonzero, distinct labels cannot XOR to zero in pairs, and the triple syndrome is nonzero by construction.

Consider a whole burst at source $i$ and a two-state burst at a distinct source $j$. Their union has odd cardinality, so an accepted event produces logical Z. Both faults have the same syndrome exactly when the omitted label of $`B_j`$ is $`s_i\oplus s_j`$. In that case the labels of the two-state burst are fixed by $i,j$. Define $D$ as the number of ordered pairs $(i,j)$ permitting such an accepted fault.

**The minimum of $D$ among fifth-order layouts is one.** To prove the lower bound, label every nonzero four-bit vector either as one of the five $`s_i`$ or as one of their ten unordered pair XORs. These 15 labels are distinct. An equality between two different expressions would give a proper zero-sum subset of the five syndromes.

For each $j$, let $`f_j`$ be the binary linear functional that takes 0 on $`s_j`$ and 1 on each $`s_i`$ for $`i\ne j`$. It exists because the only relation between the five syndromes is that they sum to zero, and the proposed function values satisfy that relation. The functional is 1 on precisely four singleton syndromes $`s_i`$ and four pair XORs $`s_i\oplus s_j`$ with $`i\ne j`$. Evaluating $`f_j`$ on the XOR of all labels of $`B_j`$ gives $`f_j(s_j)=0`$. The count of those eight labels in $`B_j`$ is therefore even.

No $`B_j`$ contains its own syndrome $`s_j`$, since the other two labels would then have to XOR to zero. Across the five source triples, the singleton syndromes in the preceding count each appear exactly once. Summing the even counts gives $`D+5`$ even, so $D$ is odd and at least one. The explicit layout has one event. Source 3 flips its entire triple, and source 2 flips slots 3 and 7. Both syndromes are 4.

If each source independently has probability $p$ of a whole burst and probability $r$ of a uniformly chosen two-state burst, with those choices mutually exclusive within a source, the coefficient of $`pr`$ in the low-rate expansion of accepted logical error probability is $`D/3`$. The same coefficient holds for conditional infidelity because there are no terms of degree one in the accepted logical error probability. A fixed heterogeneous distribution can weight individual pairs differently.

## Two sources with arbitrary partial bursts

Every noncollinear layout has a two-source partial-burst failure. Pick two labels from one triple. Their XOR is a third label outside that triple, since a label within the triple would make it collinear. Flipping those two slots and the external slot gives an accepted logical error. This construction identifies exactly 15 distinct weight-three fault sets that occupy two sources, one for each of the three internal pairs of the five triples. A two-source line has a unique internal pair. Thus rejecting every single-source subset is possible, and rejecting every arbitrary two-source subset is impossible at zero syndrome with this fault model and gadget.

## Exact law with independent per-slot faults

On top of independent whole-source bursts of rate $p$, add an independent Z fault of probability $q$ at each of the 15 slots. A local fault at a slot already flipped by a whole burst cancels that slot's fault. The probabilities below use $`x=1-2q`$ and $`y=1-2p`$. Let $A$ denote yield, and let $C$ denote the signed accepted logical parity, the probability of accepted correct output minus the probability of accepted wrong output. For the explicit five-source layout,

```math
A=\frac{1+x^8(10y^2+5y^4)}{16},\qquad
C=\frac{x^{15}y^5+x^7(10y^3+5y)}{16},\qquad
F=\frac{A-C}{2A}.
```

The indicator of zero syndrome is the average over its 16 binary characters. The zero character contributes 1 to the acceptance numerator. Every nonzero functional on $`\mathbb F_2^4`$ is 1 on eight slot labels. The map from a character to its evaluations at the five source syndromes is a bijection onto the even five-bit words, because the syndromes have rank four and sum to zero. The 15 nonzero characters thus give ten source weights 2 and five source weights 4. A Bernoulli bit of rate $q$ contributes $x$ to a character that depends on it, and a rate-$p$ source bit contributes $y$. The logical parity sign complements both supports since all source bundles have odd size. The zero character then contributes support sizes 15 and 5. The nonzero characters contribute size 7 along with size 3 or 1. This gives $C$.

The first mixed terms at small nonnegative $p,q$ are

```math
F(p,q)=F(p,0)+35q^3+35pq^2+10p^2q+O\!\left(q(p+q)^3\right).
```

There are 35 unordered zero-syndrome triples of local faults. Each of the $`\binom{15}{2}`$ pairs determines its third label, and each triple has three pairs. One whole burst and two local faults require a pair with XOR $`s_i`$, giving seven pairs for each of the five sources. Two whole bursts and one local fault require the one slot with label $`s_i\oplus s_j`$, giving ten possibilities. With fewer than three occurrences no pattern passes with odd parity. These are all degree-three terms involving $q$. The remainder follows by analyticity at $`(p,q)=(0,0)`$ after subtracting the exact pure-burst result. For $`q=O(p^3)`$ the fifth-order behavior in $p$ is retained. When $p$ and $q$ are comparable and tend to zero, the mixed-noise law is cubic.

## Full-rank equivalence and a limit of syndrome dominance

For fixed $q$, the local-fault syndrome and parity law is invariant under invertible relabeling of the four syndrome bits. Such a transformation permutes the 15 slot labels and preserves local error parity. All rank-four whole-source layouts are therefore equivalent under independent per-slot faults. A singular syndrome map used to simulate a lower-rank placement in the pure-burst model need not preserve this local noise law. In fact a lower-rank layout can improve the optimal fidelity at full yield in this model.

For a layout with whole-source syndrome map $M$, write $`W_M(s)=\mathbb E[(-1)^{\sum_i b_i}\mathbf 1_{Mb=s}]`$ for its signed whole-source syndrome mass. The signed mass of the final syndrome $s$, including the raw-slot faults, is

```math
D_M(s)=x^7 W_M(s)-\frac{x^7(1-x^8)y^5}{16} .
```

This follows by the same character sum. The signed mass for a local syndrome $u$ is $`x^7\mathbf 1_{u=0}-(x^7-x^{15})/16`$. Convolution with the source signed masses gives $`D_M`$, using $`\sum_s W_M(s)=y^5`$. Accepting every syndrome and choosing its more likely logical parity gives error $`[1-\sum_s |D_M(s)|]/2`$.

For an explicit comparison take bundles $(1,2,4)$, $(3,5,7)$, $(6,8,9)$, $(10,11,12)$, $(13,14,15)$. The syndrome list $(7,1,7,13,12)$ has rank three and merges exactly two complementary-history classes at each attained syndrome. At zero it combines the no-burst class with the class of the two bursts at sources 1 and 3. For $`p=q=t`$ and $`0<t\le 0.01`$, the zero signed mass is positive and all other signed masses are negative for both this layout and the rank-four layout. Indeed a nonzero syndrome combines at most two positive weight-two class masses, each at most $t^2$, while the negative constant divided by $x^7$ is $`(1-x^8)x^5/16\ge t x^{12}>2t^2`$. At zero the no-burst class alone has signed mass $`(1-t)^5-t^5`$, which exceeds the magnitude of the same constant divided by $x^7$.

Both layouts have the same total signed mass $`x^{15}y^5`$. With the common sign pattern, the rank-three layout increases the absolute signed mass sum by twice the increase at zero. Its full-yield error improvement is exactly

```math
x^7\big[t^2(1-t)^3-t^3(1-t)^2\big]>0 .
```

At $`p=q=1/1000`$, the full-yield errors are approximately $`0.000181781255`$ for the rank-four layout and $`0.000180799110`$ for the rank-three layout. [Verification](../verification/README.md)

The fifth-order comparison holds for zero-syndrome postselection and whole-source noise. The all-syndrome example shows why the optimal layout under mixed noise can depend on the accepted yield.

[Routing and decisions](routing.md) · [Verification](../verification/README.md) · [Related work](../references/RELATED_WORK.md)
