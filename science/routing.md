# Routing and decisions

## An assignment for five sources

Let $`s_j=\bigoplus_{v\in B_j}v`$ be the syndrome of a whole burst from source $j$.

| Source $j$ | Slots $`B_j`$ | Syndrome $`s_j`$ |
| --- | --- | --- |
| 1 | 1, 2, 4 | 7 |
| 2 | 3, 5, 7 | 1 |
| 3 | 6, 8, 10 | 4 |
| 4 | 9, 12, 15 | 10 |
| 5 | 11, 13, 14 | 8 |

The whole-burst syndrome of a history $`b\in\mathbb F_2^5`$ is $`Mb=\bigoplus_{j:b_j=1}s_j`$, where the columns of $M$ are the $`s_j`$. Each source fills an odd number of slots, so the logical fault bit is the parity of $b$. The five $`s_j`$ are nonzero and distinct and sum to zero. If a nonempty proper subset sums to zero, its complement does too. The smaller set has size at most two, which would give a zero or a repeated syndrome. Thus the only nonzero kernel vector is $`\mathbf 1=(1,1,1,1,1)`$, and the 16 syndromes label the 16 complementary pairs $`\{b,b+\mathbf 1\}`$ exactly.

## Maximal information from the existing checks

For every placement its syndrome map $`M'`$ kills $`\mathbf 1`$, since the XOR of all nonzero labels is zero. Consequently $`M'=LM`$ for a linear map $L$. The receiver can reproduce any other layout's syndrome by applying $L$ before its correction and acceptance decisions. The actual fault parity of a whole-burst history is the same in every layout, so the chosen assignment can match every achievable yield and infidelity pair under any fixed joint history law, including heterogeneous burst probabilities and correlated sources. This comparison keeps the physical source noise law fixed when the assignment changes. With observed side information or past records, it can be applied to the conditional history law whenever the additional records and their joint law are common to the layouts.

Syndrome-only processing cannot distinguish complementary histories in this model, and their fault parities are opposite. Given masses $`w(b),w(b+\mathbf1)`$, the minimum conditional fault probability on that syndrome is the smaller mass divided by the sum. Its attaining correction is the parity of the more probable history. At a specified yield, sort the syndromes by increasing conditional fault probability and retain them in that order, randomizing at the boundary if needed. This follows by exchanging equal amounts of accepted probability from a larger-risk class to a smaller-risk class.

## Exact yield and infidelity

Suppose the source bursts are independent with equal probability $`0<p<1/2`$. Every complementary pair has a unique representative of smaller weight $`i\in\{0,1,2\}`$. The maximum-posterior correction is its parity. The size-$i$ class contains $`\binom{5}{i}`$ syndromes. Each one has total mass $`a_i`$ and contributes unconditional error mass $`e_i`$ when accepted.

```math
a_i=p^i(1-p)^{5-i}+p^{5-i}(1-p)^i,\qquad
e_i=p^{5-i}(1-p)^i .
```

The conditional error odds $`e_i/(a_i-e_i)=[p/(1-p)]^{5-2i}`$ increase with $i$. Accepting all classes up to $k$ gives

```math
A_k=\sum_{i=0}^{k}\binom 5i a_i,\qquad
F_k=\frac{\sum_{i=0}^{k}\binom 5i e_i}{A_k}.
```

| Classes kept | Syndromes kept | Leading infidelity as $`p\to0`$ |
| --- | ---: | ---: |
| 0 | 1 | $p^5$ |
| 0 and 1 | 6 | $5p^4$ |
| 0, 1 and 2 | 16 | $10p^3$ |

The intermediate values of yield follow by partial acceptance in one class. At full yield, $`F_2=10p^3(1-p)^2+5p^4(1-p)+p^5`$. At zero syndrome, the correction is identity and the only fault is the all-source burst, which gives the following exact rates.

```math
A_0=(1-p)^5+p^5,\qquad F_0=\frac{p^5}{(1-p)^5+p^5}.
```

For the usual zero-syndrome test with its identity correction, this infidelity is the minimum over layouts. To see this, pair each accepted history with its complement. The no-fault/all-fault pair always contributes. For every other accepted pair the smaller weight is one or two, and the odd member of the pair has conditional probability strictly larger than the odd member of the no-fault/all-fault pair. Every extra pair therefore increases conditional infidelity. A layout with a collinear group has a weight-one accepted fault and incurs first-order infidelity. A zero-syndrome layout with no zero column and a repeated column has a weight-three accepted fault, since the repeated pair and its three-element complement both have zero syndrome. Thus fifth-order zero-syndrome suppression is equivalent to all five columns being distinct and nonzero.

[Model](model.md) · [Partial bursts and local faults](noise.md) · [Verification](../verification/README.md)
