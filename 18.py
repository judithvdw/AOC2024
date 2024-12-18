from collections import deque, defaultdict

from utils.parsing import parse_ints


def dfs_shortest_path(graph, start, goal):
    visited = set()
    stack = deque([[start]])

    while stack:
        path = stack.popleft()
        node = path[-1]
        if node not in visited:
            neighbors = graph[node]
            for neighbor in neighbors:
                new_path = path + [neighbor]
                stack.append(new_path)
                if neighbor == goal:
                    return len(new_path) - 1  # steps, not squares
            visited.add(node)
    return 0


def get_adjacency_graph(grid):
    graph = defaultdict(list)
    for coord in grid:
        dx_dy = ((0, 1), (1, 0), (0, -1), (-1, 0))
        for dx, dy in dx_dy:
            x, y = coord
            neighbour = (x + dx, y + dy)
            if neighbour in grid:
                graph[coord].append(neighbour)
    return graph


def explore(until, coords, total_grid):
    fallen_bytes = set(coords[:until])
    grid = total_grid - fallen_bytes
    graph = get_adjacency_graph(grid)
    return dfs_shortest_path(graph, (0, 0), (SIZE, SIZE))


with open("inputs/18.txt") as f:
    coords = parse_ints(f.readlines())

SIZE = 70
UNTIL = 1024
total_grid = {(x, y) for x in range(SIZE + 1) for y in range(SIZE + 1)}
print(f"Part 1: {explore(UNTIL, coords, total_grid)}")


left = UNTIL
right = len(coords)
while left < right:
    mid = (left + right) // 2
    if explore(mid, coords, total_grid):
        left = mid + 1
    else:
        right = mid

print(f"Part 2: {coords[left - 1][0]},{coords[left - 1][1]}")
