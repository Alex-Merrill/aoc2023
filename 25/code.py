import os
from collections import defaultdict

import networkx


def part1(graph, start):
    G = networkx.Graph()

    for node, neighs in graph.items():
        for neigh in neighs:
            G.add_edge(node, neigh)

    for a, b in networkx.minimum_edge_cut(G):
        G.remove_edge(a, b)

    return prod(map(len, networkx.connected_components(G)))


def prod(l):
    s = 1
    for n in l:
        s *= n

    return s


def main():
    lines = (
        open(f"{os.path.dirname(__file__)}/input.txt")
        .read()
        .strip()
        .splitlines()
    )
    graph = defaultdict(list)
    start = lines[0].split(":")[0]
    for line in lines:
        n, neighs = line.split(":")
        neighs = neighs.split(" ")[1:]
        for neigh in neighs:
            graph[n].append(neigh)
            graph[neigh].append(n)

    print(f"part 1: {part1(graph,start)}")


main()
