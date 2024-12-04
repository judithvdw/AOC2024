from utils.parsing import parse_grid

with open('inputs/04.txt') as f:
    raw = f.readlines()

lettersets = {}
for letter in "XMAS":
    lettersets[letter] = parse_grid(raw, letter)

# part 1
total = 0
dx_dy = ((0, 1), (1, 0), (0, -1), (-1, 0), (-1, 1), (1, -1), (1, 1), (-1, -1))
for x, y in lettersets["X"]:
    for dx, dy in dx_dy:
        if (x + dx, y + dy) in lettersets["M"] and (x + (dx * 2), y + (dy * 2)) in lettersets["A"] and (
                x + (dx * 3), y + (dy * 3)) in lettersets["S"]:
            total += 1

print(f"Part 1: {total}")

# part 2
total = 0
for x, y in lettersets["A"]:
    dx_dy = ((-1, 1), (1, -1), (1, 1), (-1, -1))
    ms = []
    ss = []
    for dx, dy in dx_dy:
        if (x + dx, y + dy) in lettersets["M"]:
            ms.append((dx, dy))
        if (x + dx, y + dy) in lettersets["S"]:
            ss.append((dx, dy))
    # make sure we have 2 M's and 2 S's and that a letter does not form a diagonal with itself
    if len(ms) == 2 and len(ss) == 2 and not (ms[0][0] + ms[1][0] == 0 and ms[0][1] + ms[1][1] == 0):
        total += 1
print(f"Part 2: {total}")
