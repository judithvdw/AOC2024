from utils.parsing import parse_ints
from itertools import pairwise


def diffs(report):
    return [a - b for a, b in pairwise(report)]


def is_valid(diff):
    return (min(diff) >= -3 and max(diff) < 0) or (min(diff) > 0 and max(diff) <= 3)


def dampening(report):
    for i in range(len(report)):
        if is_valid(diffs(report[:i] + report[i + 1:])):
            return True
    return False


with open('inputs/02.txt') as f:
    reports = parse_ints(f.readlines())

print(f"Part 1: {sum([is_valid(diffs(report)) for report in reports])}")
print(f"Part 2: {sum([dampening(report) for report in reports])}")
