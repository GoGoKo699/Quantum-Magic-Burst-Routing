"""Enumerate the ideal distiller's classical Z-fault patterns."""

from collections import Counter, defaultdict
from fractions import Fraction
from functools import reduce
from itertools import combinations
from operator import xor


SLOTS = tuple(range(1, 16))
GROUPS = (
    (1, 2, 4),
    (3, 5, 7),
    (6, 8, 10),
    (9, 12, 15),
    (11, 13, 14),
)
COLLINEAR_GROUPS = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9),
    (10, 11, 12),
    (13, 14, 15),
)
RANK_THREE_GROUPS = (
    (1, 2, 4),
    (3, 5, 7),
    (6, 8, 9),
    (10, 11, 12),
    (13, 14, 15),
)


def syndrome(labels):
    return reduce(xor, labels, 0)


def subsets(items):
    for size in range(len(items) + 1):
        yield from combinations(items, size)


def burst_classes(groups):
    """Map each syndrome to the histories with that syndrome."""
    classes = defaultdict(list)
    for history in subsets(tuple(range(len(groups)))):
        fault = [slot for source in history for slot in groups[source]]
        classes[syndrome(fault)].append(history)
    return classes


def verify_whole_bursts():
    assert tuple(sorted(slot for group in GROUPS for slot in group)) == SLOTS
    assert tuple(map(syndrome, GROUPS)) == (7, 1, 4, 10, 8)
    classes = burst_classes(GROUPS)
    all_sources = set(range(len(GROUPS)))
    assert len(classes) == 16
    assert classes[0] == [(), tuple(sorted(all_sources))]
    for first, second in classes.values():
        assert all_sources - set(first) == set(second)
        assert len(first) % 2 != len(second) % 2
    assert Counter(min(map(len, histories)) for histories in classes.values()) == {
        0: 1, 1: 5, 2: 10,
    }

    for p in (Fraction(1, 20), Fraction(1, 4), Fraction(1, 2)):
        weights = [p**size * (1 - p)**(5 - size) for size in range(6)]
        accepted = sum(weights[len(history)] for history in classes[0])
        wrong = sum(weights[len(history)] for history in classes[0] if len(history) % 2)
        assert accepted == (1 - p)**5 + p**5
        assert wrong / accepted == p**5 / ((1 - p)**5 + p**5)
        # For p <= 1/2, accepting all outcomes and correcting the lower
        # weight history fails exactly when the larger history occurred.
        map_error = sum(weights[max(map(len, histories))] for histories in classes.values())
        assert map_error == 10 * weights[3] + 5 * weights[4] + weights[5]

    baseline = burst_classes(COLLINEAR_GROUPS)
    assert sum(len(history) == 1 for history in baseline[0]) == 1
    print("Whole-bundle faults: 32 patterns, 16 complement classes, exact yield and error.")


def raw_pattern_counts():
    """Count raw masks by syndrome and size, before adding source bursts."""
    return Counter((syndrome(fault), len(fault)) for fault in subsets(SLOTS))


def direct_noise_weights(raw_counts):
    """Count pairs of raw and source masks that reach each accepted parity."""
    counts = Counter()
    for source_fault in subsets(tuple(range(len(GROUPS)))):
        burst_syndrome = syndrome(
            slot for source in source_fault for slot in GROUPS[source]
        )
        for (raw_syndrome, raw_size), count in raw_counts.items():
            if raw_syndrome == burst_syndrome:
                # Combining Z errors by symmetric difference adds parities.
                parity = (len(source_fault) + raw_size) % 2
                counts[len(source_fault), raw_size, parity] += count
    return counts


def verify_local_noise():
    raw_counts = raw_pattern_counts()
    assert sum(raw_counts.values()) == 2**15
    counts = direct_noise_weights(raw_counts)
    assert counts[0, 3, 1] == 35
    assert counts[1, 2, 1] == 35
    assert counts[2, 1, 1] == 10
    assert counts[5, 0, 1] == 1
    assert not any(
        parity and source_size + raw_size < 3
        for source_size, raw_size, parity in counts
    )

    points = [
        (Fraction(0), Fraction(0)),
        (Fraction(1, 10), Fraction(0)),
        (Fraction(0), Fraction(1, 10)),
        (Fraction(13, 100), Fraction(19, 1000)),
        (Fraction(1, 4), Fraction(1, 8)),
        (Fraction(1, 2), Fraction(1, 2)),
    ]
    for p, q in points:
        good = Fraction(0)
        bad = Fraction(0)
        for (source_size, raw_size, parity), count in counts.items():
            source_weight = p**source_size * (1 - p)**(5 - source_size)
            raw_weight = q**raw_size * (1 - q)**(15 - raw_size)
            if parity:
                bad += count * source_weight * raw_weight
            else:
                good += count * source_weight * raw_weight

        x, y = 1 - 2 * q, 1 - 2 * p
        acceptance = (1 + x**8 * (10 * y**2 + 5 * y**4)) / 16
        signed_acceptance = (x**15 * y**5 + x**7 * (10 * y**3 + 5 * y)) / 16
        assert good + bad == acceptance
        assert good - bad == signed_acceptance
        assert bad / (good + bad) == (acceptance - signed_acceptance) / (2 * acceptance)
    print("Local faults: 32,768 raw masks, exact Walsh agreement at six rational points.")
    verify_mixed_noise_map(raw_counts)


def unconditional_map_risk(groups, p, signed_raw):
    """Accept every syndrome and correct towards the more likely parity."""
    source_weights = [p**size * (1 - p)**(5 - size) for size in range(6)]
    signed_burst = {
        observed: sum((-1)**len(history) * source_weights[len(history)]
                      for history in histories)
        for observed, histories in burst_classes(groups).items()
    }
    signed_observations = [
        sum(weight * signed_raw[observed ^ burst]
            for burst, weight in signed_burst.items())
        for observed in range(16)
    ]
    # Each absolute value is the difference between the larger and
    # smaller parity masses for that observation.
    return (1 - sum(map(abs, signed_observations))) / 2


def verify_mixed_noise_map(raw_counts):
    p = q = Fraction(1, 1000)
    signed_raw = [Fraction(0) for _ in range(16)]
    for (observed, size), count in raw_counts.items():
        signed_raw[observed] += count * (-1)**size * q**size * (1 - q)**(15 - size)

    assert len(burst_classes(RANK_THREE_GROUPS)) == 8
    rank_four = unconditional_map_risk(GROUPS, p, signed_raw)
    rank_three = unconditional_map_risk(RANK_THREE_GROUPS, p, signed_raw)
    assert rank_three < rank_four
    print(f"Mixed-noise MAP risk at p = q = 0.001: rank four {float(rank_four):.12f}, "
          f"rank three {float(rank_three):.12f}.")


def noncollinear_partitions(labels):
    """Partition labels into noncollinear triples, ordering by least slot."""
    if not labels:
        yield ()
        return
    first, *rest = labels
    for second, third in combinations(rest, 2):
        group = (first, second, third)
        if syndrome(group):
            remaining = tuple(slot for slot in rest if slot not in (second, third))
            for partition in noncollinear_partitions(remaining):
                yield (group,) + partition


def full_plus_pair_faults(groups):
    """List accepted logical Z events as (full source, pair source, pair)."""
    for full_source, full in enumerate(groups, start=1):
        for pair_source, partial in enumerate(groups, start=1):
            if full_source == pair_source:
                continue
            for pair in combinations(partial, 2):
                if syndrome(full + pair) == 0:
                    yield full_source, pair_source, pair


def verify_partial_bursts():
    assert list(full_plus_pair_faults(GROUPS)) == [(3, 2, (3, 7))]
    counts = Counter()
    fixed_group = (1, 2, 4)
    remaining = tuple(slot for slot in SLOTS if slot not in fixed_group)
    for partition in noncollinear_partitions(remaining):
        groups = (fixed_group,) + partition
        sums = set(map(syndrome, groups))
        # Five nonzero, distinct sums with total XOR zero have no
        # proper zero-XOR subset. Any such subset or its complement
        # would have size at most two.
        if len(sums) != 5:
            continue
        count = sum(1 for _ in full_plus_pair_faults(groups))
        counts[count] += 1
        # Every pair in any source determines a distinct weight-three
        # line with two slots in that source and one in another.
        weight_three = {
            tuple(sorted((first, second, first ^ second)))
            for group in groups
            for first, second in combinations(group, 2)
        }
        assert len(weight_three) == 15
    assert counts == {1: 840, 3: 2160, 5: 2136}
    print("Partial faults: rank-four layout counts by accepted full-plus-pair events "
          "are 1→840, 3→2160, 5→2136.")


def scalable_groups(dimension, sources):
    """Keep seed syndromes while distributing zero-XOR affine cosets."""
    basis = [1 << bit for bit in range(sources - 1)]
    seeds = basis + [syndrome(basis)]
    groups = [[seed] for seed in seeds]
    reserved = {0, *seeds}
    free_cosets = []
    leftover = []
    # The four consecutive labels form cosets of span(1, 2).
    for start in range(0, 1 << dimension, 4):
        coset = tuple(range(start, start + 4))
        if reserved.isdisjoint(coset):
            free_cosets.append(coset)
        else:
            leftover.extend(label for label in coset if label not in reserved)
    assert len(leftover) % 2 == 0
    assert syndrome(leftover) == 0
    assert len(leftover) <= 3 * (sources + 1)
    groups[0].extend(leftover)
    for coset in free_cosets:
        min(groups, key=len).extend(coset)
    assert list(map(syndrome, groups)) == seeds
    return groups


def verify_scalable_examples():
    for dimension, sources in ((9, 9), (10, 11)):
        groups = scalable_groups(dimension, sources)
        lengths = list(map(len, groups))
        labels = sorted(label for group in groups for label in group)
        assert labels == list(range(1, 1 << dimension))
        assert all(length % 2 for length in lengths)
        assert max(lengths) - min(lengths) <= 4
        classes = burst_classes(groups)
        assert len(classes) == 2 ** (sources - 1)
        assert classes[0] == [(), tuple(range(sources))]
        print(f"Scaled example: {len(labels)} slots, {sources} sources, "
              f"bundle sizes {min(lengths)}–{max(lengths)}.")


def verify_cyclic_examples():
    examples = (
        (5, (12, 5, 23)),
        (7, (3, 5, 9, 15, 23, 27, 58, 53, 125)),
    )
    for sources, representatives in examples:
        mask = (1 << sources) - 1
        groups = [representatives]
        for _ in range(sources - 1):
            groups.append(tuple(
                ((label << 1) & mask) | (label >> (sources - 1))
                for label in groups[-1]
            ))
        labels = sorted(label for group in groups for label in group)
        assert labels == [
            label for label in range(1, mask) if label.bit_count() % 2 == 0
        ]
        assert list(map(syndrome, groups)) == [
            mask ^ (1 << index) for index in range(sources)
        ]
        assert burst_classes(groups)[0] == [(), tuple(range(sources))]
        print(f"Cyclic example: {sources} sources, {len(representatives)} slots each.")


def main():
    verify_whole_bursts()
    verify_local_noise()
    verify_partial_bursts()
    verify_scalable_examples()
    verify_cyclic_examples()


if __name__ == "__main__":
    main()
