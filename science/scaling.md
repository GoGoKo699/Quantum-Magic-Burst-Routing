# Larger Reed–Muller gadgets

## Gadget and source syndromes

For $`m\ge4`$, take the first-order punctured quantum Reed–Muller distiller of length $`N=2^m-1`$. Its X-check rows are coordinate evaluations on the nonzero labels of $`\mathbb F_2^m`$. The binary row span consists of the zero word and linear words of weight $`2^{m-1}`$, a multiple of eight. The CSS logical zero is the uniform sum over the row span, and logical one is the uniform sum over its all-ones translate. All words in the translate have weight $`-1\bmod8`$. Thus physical transversal T acts as logical $`T^\dagger`$, with its fixed ideal Clifford conversion if the T-state convention is used. Input Z faults flip the m X-check signs by the XOR of their labels and, in a zero-syndrome branch, act by logical Z to the fault parity. See the inherited code constructions in [Related work](../references/RELATED_WORK.md).

Choose an odd number of sources $`5\le k\le m+1`$ supplying bundles of odd size. Reserve the labels $`s_i=e_i`$ for $`1\le i<k`$ and $`s_k=\bigoplus_{i<k}e_i`$. Give one reserved label to each bundle. The syndromes have a single relation, the XOR of all k. The remaining labels have zero total XOR and even cardinality, since the XOR of all N slot labels and the XOR of all k reserved labels are both zero. Giving the remainder to one bundle preserves those source syndromes and odd sizes. This already constructs rank $`k-1`$ at the same N slots and m checks.

The whole-source record distinguishes histories up to complement, so it can reproduce the decisions of any other placement with the same odd source sizes and the same history distribution. For independent equal whole-source burst rate $p$, zero-syndrome postselection accepts only the histories of weight zero and k. Its exact rates are

```math
A=(1-p)^k+p^k,\qquad
F=\frac{p^k}{(1-p)^k+p^k} .
```

The same posterior correction and increasing-risk acceptance order as in [Routing and decisions](routing.md) apply, with classes indexed by the smaller of a history's weight and its complement's weight. At each accepted yield the common source law and the permitted measurements determine the comparison.

## Controlling bundle sizes

For a general balancing procedure, fix a two-dimensional subspace $K$ of $`\mathbb F_2^m`$. Remove the cosets of $K$ that avoid zero and the reserved labels. Each removed coset has four labels and XOR zero. The unreserved nonzero labels in all remaining cosets number at most $`3(k+1)`$ and have even cardinality and XOR zero. Place this residue in one bundle and then assign each four-label coset to the currently smallest bundle. The source syndromes and odd sizes are preserved. If $`N/k>1+3(k+1)`$, the final largest bundle exceeds the initial largest size. It reached its maximum at an addition of four to a smallest bundle, so the final bundle sizes differ by at most four.

## Exactly equal sizes for odd prime source counts

Take any odd prime $`k\ge5`$ and $`m=k-1`$. Identify $`\mathbb F_2^m`$ with the even-parity subspace of $`\mathbb F_2^k`$. Cyclic shifts partition its nonzero vectors into orbits of size $k$, because a shorter orbit would consist of a constant vector and the all-ones vector has odd parity. The XOR of an entire orbit is zero, since each coordinate sees the same even number of ones.

Choose one representative from each orbit so their XOR is $`\mathbf 1+e_0`$. The k cyclic shifts of that set, including the identity, give all k bundles. Each bundle contains $`(2^{k-1}-1)/k`$ labels, an odd integer. Its syndrome is $`\mathbf 1+e_j`$ for its shift index $j$. These vectors span the even subspace and sum to zero. More explicitly, the linear map taking coefficients to their syndrome is $`b\mapsto b+\mathbf 1\sum_j b_j`$, whose kernel is the span of $`\mathbf 1`$.

For $`k=5`$, the integer labels $(12,5,23)$ meet all three orbits and XOR to $`30=\mathbf 1+e_0`$. For $`k=7`$, the labels $(3,5,9,15,23,27,58,53,125)$ meet all nine orbits and XOR to $`126=\mathbf 1+e_0`$. In both examples bit 0 is the least significant bit. The five-source assignment in [Routing and decisions](routing.md) also optimizes the partial-burst count.

For prime $`k\ge11`$, choose representatives independently and uniformly in their orbits. Every nontrivial binary linear functional on the even subspace is 1 on $`2^{k-2}`$ labels. In each orbit the number of such labels is even because the orbit XOR is zero, so it is at most $`k-1`$. At least $`2^{k-2}/(k-1)`$ orbits are nonconstant under this functional. For each such orbit the magnitude of the character average is at most $`1-2/k`$. By independence, the sum of the magnitudes of all nontrivial Fourier coefficients of the XOR distribution is bounded by

```math
(2^{k-1}-1)(1-2/k)^{2^{k-2}/(k-1)}<1.
```

To verify the strict inequality, use $`\log(1-2/k)\le-2/k`$ and $`2^{k-1}/[k(k-1)]>(k-1)\log 2`$. The latter holds at $`k=11`$, and $`2^{k-1}/[k(k-1)^2]`$ increases for integers $`k\ge11`$. Fourier inversion then gives positive probability for every target XOR, including $`\mathbf 1+e_0`$. A deterministic procedure tracks, after each orbit, the attainable XORs and one predecessor for each. Once all orbits have been processed, follow the predecessors from the requested target XOR to recover the representatives.

Each enlarged attempt uses $`2^m-1`$ raw states and m check bits. At independent retries its expected raw-state cost is $`(2^m-1)/A`$. The representative search treats each orbit member once per attainable XOR per layer and therefore takes at most $`N(N+1)`$ binary-vector updates, with up to $`(N/k+1)(N+1)`$ predecessor records. This is an offline construction cost measured against an already exponential raw-state count. Practical value depends on the available source bundles, spatial layout, and the time and error costs of realizing the permutation.

[Model](model.md) · [Verification](../verification/README.md)
