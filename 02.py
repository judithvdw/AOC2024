from utils.parsing import parse_ints
from itertools import pairwise


def diffs(report):
    return [a - b for a, b in pairwise(report)]


def is_valid(report):
    return (min(report) >= -3 and max(report) < 0) or (min(report) > 0 and max(report) <= 3)


with open('inputs/02.txt') as f:
    reports = parse_ints(f.readlines())

print(sum([is_valid(diffs(report)) for report in reports]))
