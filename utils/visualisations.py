def print_map(grid, width, height):
    for x in range(0, height):
        row = ""
        for y in range(0, width):
            if (x, y) in grid:
                row += "#"
            else:
                row += "."
        print(row)
