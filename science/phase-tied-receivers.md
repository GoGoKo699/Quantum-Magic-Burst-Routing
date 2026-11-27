# Burst suppression with phase-tied inputs

Five sources each deliver three equatorial states with unknown phase drift. Four exact phase ties suffice to recover the same complementary-history syndrome as the standard routed distiller, using a separate stabilizer receiver. A fifth tie permits shorter parity projections and improves the yield by a factor of 16 in the constructions below.

## Source and receiver

Source $`i`$ supplies carriers $`A_i,B_i,C_i`$ with respective phase offsets $`\theta_i,\phi_i,\theta_i+\phi_i`$ from the nominal phase $`\pi/4`$. Conditional on the offsets, the input is a product over all 15 carriers. A whole-source burst $`b_i=1`$ applies $`Z`$ to all three carriers from source $`i`$. The receiver knows the linear ties between the phase offsets but has no phase or burst record. It receives one block, uses ideal stabilizer operations in a stable frame, and has no separate nonstabilizer resource. The offsets range over a relatively open region of the subspace given by the ties.

Label the five candidate ties by their residuals. A tie holds when its residual vanishes.

```math
\begin{aligned}
e_1 &= \theta_2-\theta_1, & e_2 &= \phi_3-\phi_2,\\
e_3 &= \theta_4-\theta_3, & e_4 &= \phi_5-\phi_4,\\
e_5 &= \theta_5+\phi_1-\theta_3-\phi_3.
\end{aligned}
```

The exact conditional syndrome statement applies to each history $`b\in\mathbb F_2^5`$. Statements using a common rate $`p`$ assume independent Bernoulli bursts. Every attempt charges all 15 carriers, including those discarded or consumed on rejection.

## Two-string projections

For an entry `L / R` in the table, work on the union of the listed carriers. The first computational string has ones exactly on the left list and the second has ones exactly on the right. They are complementary on this support. Project onto their two-dimensional span by reading the signed $`Z`$ parity relating a pivot carrier to each of the other carriers. The computational projection on a support of size $`m`$ succeeds with probability $`2^{1-m}`$ for every phase and burst history. Each basis component had squared amplitude $`2^{-m}`$.

Bit flips and pivot CNOTs decode the selected strings to the two values of one qubit. If the sums of offsets on the two lists agree, their relative phase is the nominal weight difference times $`\pi/4`$, plus $`\pi`$ times the burst parity of the support. An even weight difference can be set to zero by a power of $`S`$. Then an $`X`$ measurement reads the burst parity. An odd weight difference can be set to $`\pi/4`$, yielding $`|T\rangle`$ up to a logical $`Z`$ given by the same parity. The [Common-Mode extraction theorem](https://github.com/GoGoKo699/Quantum-Common-Mode-Magic-Distillation/blob/b4175b3ddf2822bf1ffd3e43cccf544410f36473/science/exact-extraction.md) uses this odd-weight projection to produce the target from a single phase collision. Here four disjoint even-weight projections also report relative source failures.

| Ties imposed | Comparison 1 | Comparison 2 | Comparison 3 | Comparison 4 | Extraction |
| --- | --- | --- | --- | --- | --- |
| All five | `A2 / A1` | `B3 / B2` | `A4 / A3` | `B5 / B4` | `B1 A5 / C3` |
| All except 2 | `A2 / A1` | `A4 / A3` | `B5 / B4` | `B1 C5 / B3 C4` | `C1 B2 A5 / C2 C3` |
| All except 3 | `A2 / A1` | `B3 / B2` | `B5 / B4` | `C1 A5 / C2 A3` | `B1 A4 C5 / C3 C4` |
| All except 5 | `A2 / A1` | `B3 / B2` | `A4 / A3` | `B5 / B4` | `C1 C3 C5 / B1 C2 C4 A5` |

With tie 2 removed, the first three comparisons enforce $`b_1=b_2`$ and $`b_3=b_4=b_5`$ on positive outcomes. The fourth reads $`b_1+b_3+b_4+b_5`$, so its positive outcome enforces $`b_1=b_3`$. Its phase residual is $`e_5-e_3+e_4`$ and the extraction residual is $`e_5-e_1`$. Both vanish without imposing tie 2.

The source mask of a support records which bundles occur an odd number of times. Use integers to encode source masks, with source 1 at the least significant bit. For instance, mask 3 reports $`b_1+b_2`$. Let $`M`$ have the four comparison masks as rows and write $`k`$ for the extraction mask.

| Ties imposed | Comparison masks | Extraction mask | Active carriers | Joint projection probability |
| --- | --- | ---: | ---: | ---: |
| All five | 3, 6, 12, 24 | 21 | 11 | 1/64 |
| All except 2 | 3, 12, 24, 29 | 21 | 15 | 1/1024 |
| All except 3 | 3, 6, 24, 23 | 21 | 15 | 1/1024 |
| All except 5 | 3, 6, 12, 24 | 14 | 15 | 1/1024 |

## Observed syndrome and yield

Let $`D`$ be the joint probability of the five computational projections. Their supports are disjoint, so the probabilities multiply conditional on the phases and the history. In each row $`M`$ has rank four and kernel $`\{00000,11111\}`$. Its comparison outcomes therefore label all 16 complementary history pairs. The two members differ by an odd extraction parity since $`k\cdot \mathbf 1=1`$.

Keeping only the four positive comparison outcomes accepts the clean history and the all-source burst. The latter gives $`Z|T\rangle`$. Under independent bursts of rate $`p`$, the acceptance probability $`A`$ and accepted infidelity $`F`$ are

```math
A=D\big[(1-p)^5+p^5\big],\qquad F=\frac{p^5}{(1-p)^5+p^5}.
```

All 15 carriers are supplied before the test. Independent retries cost $`15/A`$ raw states on average for one accepted output.

The same four measured outcomes also transfer the full [routing decision frontier](routing.md#maximal-information-from-the-existing-checks). The routed Reed–Muller circuit and this receiver both report rank-four linear syndromes on five source bits with kernel spanned by $`\mathbf 1`$. Their records are related by an invertible linear recoding. The difference between the two output parities, $`k\cdot b`$ and $`\sum_i b_i`$, is an even linear form of the source bits and is determined by the syndrome. A known syndrome-dependent $`Z`$ correction accounts for that difference. Thus for any fixed joint law on the burst histories, the same syndrome-dependent acceptance and correction rules have the same conditional infidelities and yields scaled by $`D`$. This comparison concerns the observed record, the charged raw states, and the ideal conditional output. The [injection circuit](model.md) and the two-string receiver have different physical operations and scheduling requirements.

## Four ties within the disjoint receiver family

Consider receivers with one prescribed complementary pair per support, four even comparison supports, and one odd extraction support, all disjoint. The comparison masks must have rank four to label every complementary pair.

Reduce the integer charge map modulo two. On a source its coordinates are $`x_A+x_C`$ and $`x_B+x_C`$. Its kernel therefore consists of unions of complete three-carrier bundles. If the four signed comparison charge differences were dependent modulo two, some nonempty union of their disjoint supports would consist of all the carriers of a source set $`S`$. This set has even cardinality because the comparison supports are even. It is proper among five sources. Each selected comparison then has source mask supported in $`S`$ and each other comparison has source mask supported in its complement. All masks are even, so the total rank is at most $`(|S|-1)+(5-|S|-1)=3`$, a contradiction. Independence modulo two implies independence over the reals.

Thus the four comparison equalities already require four independent ties. At four ties the five charge differences, including the extractor, are dependent modulo two. The dependence includes the extractor, because the four comparison differences are independent. If the selected supports exhaust only a proper set of source bundles, the split-rank bound gives the same contradiction. Consequently all 15 carriers must occur in the selected supports, fixing $`D=2^{-10}`$ for this family. With the five specified ties, each even support still needs at least two carriers and the extractor needs at least three because every individual carrier has nonzero sensitivity. The displayed $`D=1/64`$ is then maximal within this family.

For the last row there is also an optimal extraction probability among receivers that first keep the four stated comparison projections and use only the seven remaining carriers for extraction. Those seven carriers have six independent charge coordinates subject to the four retained ties. Their sole signed charge relation uses all seven and is the last row's extraction equality. Only one charge sector contains both Hamming-weight parities, and it has two strings. The one-qubit extraction bound gives at most $`2^{1-7}=1/64`$ once the four comparison projections succeed.

The four-tie minimum concerns the stated receiver family. In the [independent-phase converse](https://github.com/GoGoKo699/Quantum-Common-Mode-Magic-Distillation/blob/cf36089ff7215b5f3044c06ffc0be79f96a53c43/science/burst-converse.md), arbitrary joint stabilizer receivers at nonvanishing yield cannot achieve fifth-order suppression when all inter-source ties are removed. That converse also explains why sixth order is impossible even with ties. Whether arbitrary joint receivers can omit either outer tie in the named family remains open.

## Finite deterministic mismatch

For each receiver, let $`\delta_j`$ be the residual phase of comparison $`j=1,2,3,4`$ and $`\delta_0`$ the residual phase of extraction. The signs of these residuals depend on basis order and do not affect the probabilities.

| Ties imposed in the exact circuit | Four comparison residuals, in order | Extraction residual |
| --- | --- | --- |
| All five | $`e_1,e_2,e_3,e_4`$ | $`e_5`$ |
| All except 2 | $`e_1,e_3,e_4,e_5-e_3+e_4`$ | $`e_5-e_1`$ |
| All except 3 | $`e_1,e_2,e_4,e_5-e_1+e_2`$ | $`e_5+e_4`$ |
| All except 5 | $`e_1,e_2,e_3,e_4`$ | $`-e_1+e_2-e_3+e_4`$ |

Set $`t_j=\sin^2(\delta_j/2)`$. After the computational projections, each comparison reports its ideal bit with probability $`1-t_j`$ and the flipped value with probability $`t_j`$. These comparison errors are independent conditional on the fixed phases and burst history. The extracted qubit still has coherent phase residual $`\delta_0`$. Its infidelity is $`t_0`$ for an even extraction parity and $`1-t_0`$ for an odd one.

Let $`f_j(0)=1-t_j`$, $`f_j(1)=t_j`$, $`g(0)=t_0`$, $`g(1)=1-t_0`$, and $`w_b=p^{|b|}(1-p)^{5-|b|}`$. The all-positive comparison rule has exact acceptance and accepted wrong mass

```math
\begin{aligned}
A &= D\sum_b w_b\prod_{j=1}^4 f_j\big((Mb)_j\big),\\
AF &= D\sum_b w_b\prod_{j=1}^4 f_j\big((Mb)_j\big)\,g(k\cdot b).
\end{aligned}
```

If the comparisons retain positive clean yield and the extraction residual is fixed, the infidelity tends to $`t_0`$ as $`p\to0`$. For residuals tending to zero, each nonzero syndrome $`s`$ has a unique history of odd extraction parity. Denote its weight by $`m_s`$. Since $`A\to D`$ and all wrong-mass terms are nonnegative, fifth order holds exactly when

```math
t_0=O(p^5),\qquad
\prod_{j:s_j=1}t_j=O\big(p^{5-m_s}\big)
\quad\text{for every nonzero }s.
```

For the four constructions, the inequalities for one nonzero syndrome bit already imply the remaining inequalities. The [finite check](../verification/check_phase_ties.py) verifies this by enumerating the histories. The weights for the four individual syndrome bits are

| Ties imposed | Wrong-history weights for individual comparison bits |
| --- | --- |
| All five | 1, 2, 2, 1 |
| All except 2 | 4, 2, 2, 2 |
| All except 3 | 2, 2, 4, 2 |
| All except 5 | 4, 2, 2, 4 |

For example, with all five ties, residuals of orders $`p^2,p^{3/2},p^{3/2},p^2`$ on the four comparisons and $`p^{5/2}`$ on extraction preserve fifth order. These statements model deterministic phase offsets and an otherwise ideal receiver. [Partial bursts](noise.md), storage noise and faulty checks require separate models.
