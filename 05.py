from utils.parsing import parse_ints

from collections import defaultdict
from graphlib import TopologicalSorter
from itertools import chain


def order_ok(rules, update):
    for a, b in rules:
        if (a in update and b in update) and (not update.index(a) < update.index(b)):
            return False
    return True


def get_middel_num(update):
    assert len(update) % 2 == 1
    return update[len(update) // 2]


def reorder(rules, update):
    graph = defaultdict(set)
    for a, b in rules:
        if a in update and b in update:
            graph[b].add(a)
    ts = TopologicalSorter(graph)
    return tuple(ts.static_order())


with open("inputs/05.txt") as f:
    rules, updates = (parse_ints(x.split("\n")) for x in f.read().split("\n\n"))
    all_used = set(chain.from_iterable(updates))

print(sum(get_middel_num(update) for update in updates if order_ok(rules, update)))
print(sum(get_middel_num(reorder(rules, update)) for update in updates if not order_ok(rules, update)))
