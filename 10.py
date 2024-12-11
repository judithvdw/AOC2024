from collections import deque, defaultdict
from utils.parsing import parse_grid_v2


def dfs(graph, source):
    all_paths = set()
    stack = deque([(source, [source])])

    while stack:
        current_node, path = stack.pop()
        all_paths.add(tuple(path))
        for neighbor in graph[current_node]:
            if neighbor not in path:
                stack.append((neighbor, path + [neighbor]))

    return all_paths


def get_adjacency_graph(grid):
    graph = defaultdict(list)
    for num, coords in grid.items():
        if num == 9:
            continue
        for coord in coords:
            dx_dy = ((0, 1), (1, 0), (0, -1), (-1, 0))
            for dx, dy in dx_dy:
                x, y = coord
                neighbour = (x + dx, y + dy)
                if neighbour in grid[num + 1]:
                    graph[coord].append(neighbour)
    return graph


with open('inputs/10.txt') as f:
    data = parse_grid_v2(f.readlines(), nums=True)

graph = get_adjacency_graph(data)

ends = []
for trail_head in data[0]:
    e = []
    for path in dfs(graph, trail_head):
        if path[-1] in data[9]:
            e.append(path[-1])
    ends.append(e)

print(f'Part 1: {sum((len(set(x)) for x in ends))}')
print(f'Part 2: {sum((len(x) for x in ends))}')
