def print_map(grid, height, width):
    for y in range(0, height):
        row = ""
        for x in range(0, width):
            if (x, y) in grid:
                row += "#"
            else:
                row += "."
        print(row)
