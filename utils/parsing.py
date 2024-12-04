import re


def parse_grid(lines, character="#"):
    d = set()
    for i, line in enumerate(lines):
        for j, num in enumerate(line.strip()):
            if num == character:
                d.add((i, j))
    return d


def parse_ints(lines, negative=False):
    pattern = r'-?\d+' if negative else r'\d+'
    return [list(map(int, re.findall(pattern, line))) for line in lines]
