import networkx as nx

with open('inputs/23.txt') as f:
    edges = [tuple(x.strip().split('-')) for x in f.readlines()]

graph = nx.Graph()
graph.add_edges_from(edges)

part1 = list(x for x in nx.enumerate_all_cliques(graph) if len(x) == 3 and 't' in ''.join(y[0] for y in x))
print(f'Part 1: {len(part1)}')

part2 = nx.find_cliques(graph)
print(f'Part 2: {','.join(sorted(max(list(part2), key=len)))}')
