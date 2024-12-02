from collections import Counter

with open("inputs/01.txt") as f:
    data = [map(int, line.split()) for line in f.read().splitlines()]
    transposed = [list(i) for i in zip(*data)]

left, right = transposed
counts = Counter(right)
print(f"Part 1: {sum(abs(l - r) for l, r in zip(sorted(left), sorted(right)))}")
print(f"Part 2: {sum(l * counts[l] for l in left)}")
