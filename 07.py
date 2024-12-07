from utils.parsing import parse_ints
from itertools import product


def fixable(answer, components, ops):
    options = ["".join(comb) for comb in product(ops, repeat=len(components) - 1)]
    for option in options:
        total = components[0]
        for num, func in zip(components[1:], option, strict=True):
            if func == "*":
                total *= num
            if func == "+":
                total += num
            if func == "|":
                total = int(str(total) + str(num))
        if total == answer:
            return True
    return False


with open('inputs/07.txt') as f:
    values = parse_ints(f.readlines())

print(sum(v[0] for v in values if fixable(v[0], v[1:], "*+")))
print(sum(v[0] for v in values if fixable(v[0], v[1:], "*+|")))
