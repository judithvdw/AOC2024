import re
from bisect import bisect
from math import prod


def clean_and_mul(s):
    return prod((map(int, s.split(","))))


with open("inputs/03.txt") as f:
    code = f.read()

muls = [(int(m.span()[0]), clean_and_mul(m.group(1))) for m in re.finditer(r'mul\((\d+,\d+)\)', code)]
dos = [0] + [do.span()[0] for do in re.finditer(r'do\(\)', code)]
donts = [-1] + [dont.span()[0] for dont in re.finditer(r'don\'t\(\)', code)]

print(sum(a[1] for a in muls))
print(sum(mul for loc, mul in muls if dos[bisect(dos, loc) - 1] > donts[bisect(donts, loc) - 1]))
