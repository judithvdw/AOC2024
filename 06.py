from utils.parsing import parse_grid
from itertools import cycle


def run(start, obstacles, max_y, max_x, pt2=False):
    dx_dy = cycle(((0, -1), (1, 0), (0, 1), (-1, 0)))

    cur_loc = start
    cur_dir = next(dx_dy)
    visited = {((cur_loc), cur_dir)}

    while 0 < cur_loc[0] < max_x and 0 < cur_loc[1] < max_y:
        dx, dy = cur_dir
        next_loc = cur_loc[0] + dx, cur_loc[1] + dy
        if next_loc in obstacles:
            cur_dir = next(dx_dy)
        else:
            cur_loc = next_loc
            if pt2:
                if (cur_loc, cur_dir) in visited:
                    return False
        visited.add((cur_loc, cur_dir))
    return visited


with open('inputs/06.txt') as f:
    raw = f.readlines()
    start = parse_grid(raw, "^").pop()
    obstacles = parse_grid(raw)

max_y, max_x = len(raw), len(raw[0].strip())
pos_and_dr = run(start, obstacles, max_y, max_x)
unique_pos = {loc for loc, dr in pos_and_dr}

print(f"Part 1: {len(unique_pos) - 1}")  # first loc outside of grid is wrongly added
print(f"Part 2: {sum(not run(start, obstacles | {(x, y)}, max_y, max_x, pt2=True) for x, y in unique_pos)}")
