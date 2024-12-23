from itertools import pairwise
from more_itertools import windowed
from collections import defaultdict


def mix(a, b):
    return a ^ b


def prune(a):
    return a % 16777216


def next_num(n):
    n = prune(mix(n * 64, n))
    n = prune(mix(n // 32, n))
    n = prune(mix(n * 2048, n))
    return n


def generate_sequence(n, length=2000):
    return [n] + [n := next_num(n) for _ in range(length)]


with open('inputs/22.txt') as f:
    nums = [int(x) for x in f.readlines()]

sequences = [generate_sequence(num) for num in nums]
prices = [[x % 10 for x in seq] for seq in sequences]
diffs = [[y % 10 - x % 10 for x, y in pairwise(seq)] for seq in sequences]

windows_and_prices = []
for diff_list, price_list in zip(diffs, prices):
    windowlist = tuple(windowed(diff_list, 4))
    windows_and_prices.append(tuple(zip(windowlist, price_list[4:], strict=True)))

bananas = defaultdict(int)
for buyer in windows_and_prices:
    seen = set()
    for window, price in buyer:
        if window not in seen:
            bananas[window] += price
            seen.add(window)

print(f'Part 1: {sum(sequence[-1] for sequence in sequences)}')
print(f'Part 2: {max(bananas.values())}')
