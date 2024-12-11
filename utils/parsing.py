import re
from collections import defaultdict


def parse_grid(lines, character="#"):
    d = set()
    for i, line in enumerate(lines):
        for j, num in enumerate(line.strip()):
            if num == character:
                d.add((j, i))
    return d


def parse_ints(lines, negative=False):
    pattern = r'-?\d+' if negative else r'\d+'
    return [list(map(int, re.findall(pattern, line))) for line in lines]


def parse_grid_v2(lines, skip="", nums=False):
    d = defaultdict(set)
    for y, line in enumerate(lines):
        for x, c in enumerate(line.strip()):
            if c not in skip:
                if nums:
                    d[int(c)].add((x, y))
                else:
                    d[c].add((x, y))

    return d