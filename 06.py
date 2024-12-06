from utils.parsing import parse_grid
from itertools import cycle

with open('inputs/06.txt') as f:
    raw = f.readlines()
    start = parse_grid(raw, "^").pop()
    obstacles = parse_grid(raw)

max_y, max_x = len(raw), len(raw[0].strip())
dx_dy = cycle(((-1, 0), (0, 1), (1, 0), (0, -1)))

cur_loc = start
cur_dir = next(dx_dy)
visited = set()
while 0 < cur_loc[0] < max_x and 0 < cur_loc[1] < max_y:
    dx, dy = cur_dir
    next_loc = cur_loc[0] + dx, cur_loc[1] + dy
    if next_loc in obstacles:
        cur_dir = next(dx_dy)
    else:
        cur_loc = next_loc
        visited.add(cur_loc)

print(len(visited)-1)
