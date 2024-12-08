from utils.parsing import parse_grid_v2
from itertools import combinations


def get_antinodes(antennas, n):
    antinodes = set()
    for frequency, locs in antennas.items():
        pairs = combinations(locs, r=2)
        for a, b in pairs:
            a_x, a_y = a
            b_x, b_y = b
            x_diff, y_diff = a_x - b_x, a_y - b_y
            for i in range(n): # who needs checks anyways
                antinodes.add((a_x + (x_diff * i), a_y + (y_diff * i)))
                antinodes.add((b_x - (x_diff * i), b_y - (y_diff * i)))
    return antinodes


with open('inputs/08.txt') as f:
    all_locs = parse_grid_v2(f.readlines())

allowed_locations = set.union(*all_locs.values())
empty_spots = all_locs.pop(".")

print(f"Part 1: {len(get_antinodes(all_locs, 1) & allowed_locations)}")
print(f"Part 2: {len(get_antinodes(all_locs, 50) & allowed_locations)}")  # 50 is the gridsize
