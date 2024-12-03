import re
from bisect import bisect
from math import prod


def mul(s):
    return prod((map(int, s.split(","))))


with open("inputs/03.txt") as f:
    code = f.read()

pattern = r'mul\((\d+,\d+)\)'
muls = [(int(m.span()[0]), mul(m.group(1))) for m in re.finditer(pattern, code)]
dos = [0] + [do.span()[0] for do in re.finditer(r'do\(\)', code)]
donts = [dont.span()[0] for dont in re.finditer(r'don\'t\(\)', code)]

print(sum(a[1] for a in muls))
print(sum(mul for loc, mul in muls if dos[bisect(dos, loc) - 1] > donts[bisect(donts, loc) - 1]))
