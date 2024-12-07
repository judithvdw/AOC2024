from utils.parsing import parse_ints
from itertools import product
from operator import mul, add


def concat(a, b):
    return int(str(a) + str(b))


def fixable(answer, components, ops):
    options = product(ops, repeat=len(components) - 1)
    for option in options:
        total = components[0]
        for num, func in zip(components[1:], option, strict=True):
            total = func(total, num)
        if total == answer:
            return True
    return False


with open('inputs/07.txt') as f:
    values = parse_ints(f.readlines())

print(sum(v[0] for v in values if fixable(v[0], v[1:], (add, mul))))
print(sum(v[0] for v in values if fixable(v[0], v[1:], (add, mul, concat))))
