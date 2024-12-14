from collections import defaultdict
from math import prod, inf

from utils.parsing import parse_ints
from utils.visualisations import print_map


def step(robot, w, h):
    px, py, vx, vy = robot
    new_x = (px + vx) % w
    new_y = (py + vy) % h
    return [new_x, new_y, vx, vy]


def get_quad_info(data, w, h):
    counts = defaultdict(int)
    for robot in data:
        x, y = robot[0], robot[1]
        if x < WIDTH // 2 and y < HEIGHT // 2:
            counts["A"] += 1
        if x > WIDTH // 2 and y < HEIGHT // 2:
            counts["B"] += 1
        if x < WIDTH // 2 and y > HEIGHT // 2:
            counts["C"] += 1
        if x > WIDTH // 2 and y > HEIGHT // 2:
            counts["D"] += 1
    return counts


with open('inputs/14.txt') as f:
    data = parse_ints(f.readlines(), negative=True)

# WIDTH, HEIGHT = 11, 7
WIDTH, HEIGHT = 101, 103

cycles = WIDTH * HEIGHT
smallest = (inf, 0)
for i in range(cycles):
    new_locs = []
    for robot in data:
        new_loc = step(robot, WIDTH, HEIGHT)
        new_locs.append(new_loc)
    data = new_locs
    quads = get_quad_info(data, WIDTH, HEIGHT)
    if (level := prod(quads.values())) < smallest[0]:
        smallest = level, i + 1
        grid = {(robot[0], robot[1]) for robot in data}
    if i == 100:
        print(f"Part 1: {prod(quads.values())}")

print(f"Part 2: {smallest[1]}")
print_map(grid, HEIGHT, WIDTH)
