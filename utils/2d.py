def parse_sparse_grid(path):
    with open(path, 'r') as f:
        lines = f.readlines()
    d = set()
    for i, line in enumerate(lines):
        for j, num in enumerate(line.strip()):
            if num == "#":
                d.add((i, j))
    return d


def print_sparse_map(grid, width, height):
    for x in range(0, height):
        row = ""
        for y in range(0, width):
            if (x, y) in grid:
                row += "#"
            else:
                row += "."
        print(row)
