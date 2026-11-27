# Verify the routing results

Run from the repository root with Python 3.10 or newer.

```bash
python3 verification/run_all.py
python3 verification/check_phase_ties.py
```

The scripts use the standard library. They enumerate fault patterns and assignments for the ideal syndrome model, with rational arithmetic for probabilities.

| Check | Reproduces |
|---|---|
| Whole-source faults | All 32 histories, 16 complementary history pairs, the zero-syndrome yield and error, and the error when accepting every syndrome and correcting the more probable history. A layout with a collinear triple has a single-source undetected fault. |
| Independent local faults | All 32,768 raw-slot fault masks, combined with all 32 source histories by syndrome and Hamming weight. Direct acceptance and logical-error masses match the Walsh formulas at six rational parameter pairs, including cases with either noise component absent. |
| Mixed-noise decoding | At whole-source and local flip rates of 0.001, accepting every syndrome and correcting the likelier parity gives logical error 0.000181781255 for the rank-four layout and 0.000180799110 for a rank-three layout. Whole-source syndrome dominance applies when local flips are absent. |
| Partial bursts | One accepted whole-plus-pair event in the explicit assignment. Among rank-four layouts containing the fixed triple `(1, 2, 4)`, 840 layouts have one such event, 2,160 have three, and 2,136 have five. Any noncollinear triple is equivalent to the fixed triple under an invertible binary relabeling, which preserves these event counts. |
| Larger codes | The coset allocation partitions 511 slots into nine odd bundles of size 55–57 and 1,023 slots into 11 bundles of size 93. The cyclic construction partitions 15 and 63 slots into five and seven equal bundles, respectively. Exhaustion in each case finds only the empty and all-source histories at zero syndrome. |
| Phase-tied receivers | Exact integer charge differences and rational span tests for all four receivers, disjoint carrier supports, all 32 burst histories per receiver, exact yields, and the mismatch exponent test for all 16 syndromes. |

The checks implement the [syndrome and parity model](../science/model.md) and [phase-tied receiver](../science/phase-tied-receivers.md). See the [assignment and syndrome proof](../science/routing.md), [noise calculations](../science/noise.md), and [larger-code construction](../science/scaling.md) for the general arguments. The scripts model ideal Clifford operations and syndrome measurements.
