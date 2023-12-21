import os
import collections


def part1(graph, start):
    path = {  # tells us what directions to travel based on current pipe
        "|": [(1, 0), (-1, 0)],
        "-": [(0, 1), (0, -1)],
        "L": [(-1, 0), (0, 1)],
        "J": [(-1, 0), (0, -1)],
        "7": [(1, 0), (0, -1)],
        "F": [(1, 0), (0, 1)],
    }
    cleaned_graph = [["."] * len(graph[0]) for _ in range(len(graph))]
    q = collections.deque([(start[0], start[1], 0)])
    visited = set(start)
    mx_d = (start[0], start[1], 0)
    while q:
        i, j, d = q.popleft()
        c = graph[i][j]
        cleaned_graph[i][j] = c

        if d > mx_d[2]:
            mx_d = (i, j, d)

        for di, dj in path[c]:
            ni, nj = i + di, j + dj
            if (ni, nj) in visited:
                continue
            visited.add((ni, nj))
            q.append((ni, nj, d + 1))

    return mx_d[2], cleaned_graph


def replace_start(graph, start):
    i, j = start
    start = 0
    if graph[i][j + 1] in ["-", "J", "7"]:
        start += 1
    if graph[i][j - 1] in ["-", "L", "F"]:
        start += 2
    if graph[i + 1][j] in ["|", "L", "J"]:
        start += 3
    if graph[i - 1][j] in ["|", "F", "7"]:
        start += 5

    if start == 3:
        graph[i][j] == "-"
    elif start == 8:
        graph[i][j] = "|"
    elif start == 6:
        graph[i][j] = "L"
    elif start == 7:
        graph[i][j] = "J"
    elif start == 5:
        graph[i][j] = "7"
    elif start == 4:
        graph[i][j] = "F"

    return graph


def part2(graph):
    """
    if there are an even number of pipe boundaries between a node and the boundary of the
    environment, then we must not be inside the pipe, if odd, we are inside the pipe
    we start from the left side of the environment, and work our way across keeping track
    of how many boundaries we have crossed.

    Only count '|', 'J', or 'L' since 'L7' would basically be a kink in the pipe downwards,
    same but opposite for 'FJ'. The other two special cases are a U-turn in the pipe, which would indicate
    we are outside of the pipe as that should count as two boundaries. These are handled because
    'LJ' would be counted twice and thus stay in whichever state, inside or outside, that we are
    at before hitting the U-turn, and 'F7' will not be counted at all, thus staying in whichever
    state we are at before hitting th U-turn
    """
    num_inside = 0
    for i in range(len(graph)):
        boundaries = 0
        for j in range(len(graph[0])):
            if graph[i][j] in ["|", "J", "L"]:
                boundaries += 1
            elif graph[i][j] == "." and boundaries % 2 == 1:
                num_inside += 1
                graph[i][j] = "I"
            elif graph[i][j] == ".":
                graph[i][j] = "O"

    print_graph(graph)
    return num_inside


def print_graph(graph):
    d = {
        "-": "─",
        "|": "│",
        "L": "╰",
        "J": "╯",
        "7": "╮",
        "F": "╭",
        "I": "█",
        "O": "░",
        ".": " ",
    }
    for line in graph:
        print("".join([d[c] for c in line]))


def main():
    lines = open(f"{os.path.dirname(__file__)}/input.txt").read().strip().splitlines()
    graph = [[] for _ in range(len(lines))]
    start = (-1, -1)
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            graph[i].append(c)
            if c == "S":
                start = (i, j)

    graph = replace_start(graph, start)
    print_graph(graph)
    p1_ans, cleaned_graph = part1(graph, start)
    print_graph(cleaned_graph)
    p2_ans = part2(cleaned_graph)
    print(f"part 1: {p1_ans}")
    print(f"part 2: {p2_ans}")


main()
