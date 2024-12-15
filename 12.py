from collections import defaultdict, deque

from utils.parsing import parse_grid_v2


def perimiter(coords):
    dx_dy = ((0, -1), (1, 0), (0, 1), (-1, 0))
    total = 0
    for coord in coords:
        for dx, dy in dx_dy:
            x, y = coord
            if (x + dx, y + dy) not in coords:
                total += 1
    return total

def sides(coords):
    pass


def dfs(graph, source):
    visited = set()
    stack = deque()
    stack.appendleft(source)

    while stack:
        s = stack.popleft()
        if s not in visited:
            visited.add(s)
        else:
            continue
        for neighbour in graph[s]:
            stack.appendleft(neighbour)
    return visited


def get_adjacency_graph(grid):
    graph = defaultdict(list)
    for coord in grid:
        total = 0
        dx_dy = ((0, 1), (1, 0), (0, -1), (-1, 0))
        for dx, dy in dx_dy:
            x, y = coord
            neighbour = (x + dx, y + dy)
            if neighbour in grid:
                graph[coord].append(neighbour)
                total += 1
        if total == 0:
            graph[coord] = []
    return graph


with open('inputs/12.txt') as f:
    raw = f.readlines()

groups = parse_grid_v2(raw)

total = 0
for letter, grid in groups.items():
    paths = set()
    graph = get_adjacency_graph(grid)
    for node in graph:
        paths.add(tuple(sorted(tuple(dfs(graph, node)))))
    for p in paths:
        total += len(p) * perimiter(set(p))

print(total)

