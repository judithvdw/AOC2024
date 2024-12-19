from functools import cache


@cache
def possibilities(design, towels):
    total = 0
    for towel in towels:
        if design == towel:
            total += 1
        if design[:len(towel)] == towel:
            total += possibilities(design[len(towel):], towels)
    return total


with open('inputs/20.txt') as f:
    a, b = f.read().split('\n\n')

designs = b.split()
towels = tuple(a.split(", "))

print(sum(bool(possibilities(design, towels)) for design in designs))
print(sum(possibilities(design, towels) for design in designs))
