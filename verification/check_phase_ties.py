"""Check phase equalities, syndrome classes and deterministic mismatch."""

from collections import defaultdict
from fractions import Fraction
from itertools import product

LABELS = tuple(f"{kind}{bundle}" for bundle in range(1, 6) for kind in "ABC")
TIES = ("A2/A1", "B3/B2", "A4/A3", "B5/B4", "B1 A5/C3")
LAYOUTS = {
    "all ties": (None, (*TIES[:4], TIES[4]), 64, (1, 2, 2, 1)),
    "drop tie 2": (
        2, (TIES[0], TIES[2], TIES[3], "B1 C5/B3 C4", "C1 B2 A5/C2 C3"),
        1024, (4, 2, 2, 2),
    ),
    "drop tie 3": (
        3, (TIES[0], TIES[1], TIES[3], "C1 A5/C2 A3", "B1 A4 C5/C3 C4"),
        1024, (2, 2, 4, 2),
    ),
    "drop tie 5": (5, (*TIES[:4], "C1 C3 C5/B1 C2 C4 A5"), 1024, (4, 2, 2, 4)),
}
HISTORIES = tuple(product((0, 1), repeat=5))


def vector_difference(group):
    left, right = (word.split() for word in group.split("/"))
    result = [0] * 10
    for labels, sign in ((left, 1), (right, -1)):
        for kind, bundle in labels:
            pair = 2 * (int(bundle) - 1)
            if kind != "B":
                result[pair] += sign
            if kind != "A":
                result[pair+1] += sign
    return result


def in_span(vector, rows):
    target = list(map(Fraction, vector))
    echelon = []
    for row in rows:
        row = list(map(Fraction, row))
        for pivot, basis in echelon:
            row = [x - row[pivot] * y for x, y in zip(row, basis)]
        pivot = next((i for i, value in enumerate(row) if value), None)
        if pivot is not None:
            echelon.append((pivot, [x / row[pivot] for x in row]))
    for pivot, basis in echelon:
        target = [x - target[pivot] * y for x, y in zip(target, basis)]
    return not any(target)


def metadata(groups, kept):
    seen = set()
    masks = []
    denominator = 1
    for group in groups:
        left, right = (word.split() for word in group.split("/"))
        support = left + right
        assert len(support) == len(set(support))
        assert not seen.intersection(support)
        assert set(support) <= set(LABELS)
        seen.update(support)
        assert in_span(vector_difference(group), kept)
        masks.append(tuple(
            sum(label[1] == str(i) for label in support) % 2
            for i in range(1, 6)
        ))
        denominator *= 2 ** (len(support) - 1)
    return masks, denominator


def dot(u, v):
    return sum(a * b for a, b in zip(u, v)) % 2


def verify_layout(name, omitted, groups, expected_denominator, expected_weights):
    kept = [vector_difference(tie) for i, tie in enumerate(TIES, start=1)
            if i != omitted]
    masks, denominator = metadata(groups, kept)
    assert denominator == expected_denominator
    assert tuple(sum(mask) % 2 for mask in masks) == (0, 0, 0, 0, 1)

    by_syndrome = defaultdict(list)
    for history in HISTORIES:
        syndrome = tuple(dot(mask, history) for mask in masks[:4])
        by_syndrome[syndrome].append((history, dot(masks[4], history)))
    assert len(by_syndrome) == 16
    assert by_syndrome[(0,) * 4] == [((0,) * 5, 0), ((1,) * 5, 1)]
    for entries in by_syndrome.values():
        assert len(entries) == 2
        assert sorted(bit for _, bit in entries) == [0, 1]
        assert all(a != b for a, b in zip(entries[0][0], entries[1][0]))
        # The parity recoding is the same for both histories in each pair.
        assert len({(sum(history) + bit) % 2 for history, bit in entries}) == 1

    def odd_weight(syndrome):
        return next(sum(history) for history, bit in by_syndrome[syndrome] if bit)

    single_weights = tuple(
        odd_weight(tuple(int(i == j) for i in range(4)))
        for j in range(4)
    )
    assert single_weights == expected_weights
    for syndrome in by_syndrome:
        if any(syndrome):
            # With t_j = O(p^(5-m_j)), every wrong-support contribution is O(p^5).
            check_exponent = sum(
                (5 - weight) * bit for weight, bit in zip(single_weights, syndrome)
            )
            assert odd_weight(syndrome) + check_exponent >= 5

    for p in (Fraction(1, 100), Fraction(1, 10), Fraction(2, 5)):
        correct, wrong = (Fraction(0), Fraction(0))
        burst_mass = [p**size * (1 - p)**(5 - size) for size in range(6)]
        for history, bit in by_syndrome[(0,) * 4]:
            mass = burst_mass[sum(history)] / denominator
            if bit:
                wrong += mass
            else:
                correct += mass
        assert correct + wrong == ((1 - p)**5 + p**5) / expected_denominator
        assert wrong / (correct + wrong) == p**5 / ((1 - p)**5 + p**5)
    print(f"{name}: 32 histories, projection 1/{denominator}, "
          f"one-comparison wrong-history weights {single_weights}.")


if __name__ == "__main__":
    for name, layout in LAYOUTS.items():
        verify_layout(name, *layout)
