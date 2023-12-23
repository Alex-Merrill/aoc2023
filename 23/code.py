import os
import sys
import time
from collections import defaultdict, deque

sys.setrecursionlimit(10000)


def valid_neighbors(grid, i, j, part2=False):
    R = len(grid)
    C = len(grid[0])
    smap = {">": [(0, 1)], "<": [(0, -1)], "^": [(-1, 0)], "v": [(1, 0)]}
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    if not part2 and grid[i][j] in smap:
        dirs = smap[grid[i][j]]
    for di, dj in dirs:
        ni, nj = i + di, j + dj
        if ni < 0 or ni >= R or nj < 0 or nj >= C or grid[ni][nj] == "#":
            continue
        yield (ni, nj)


def part1(grid, start, end):
    def dfs(i, j, d):
        if (i, j) == end:
            return d

        md = 0
        for ni, nj in valid_neighbors(grid, i, j):
            if (ni, nj) not in visited:
                visited.add((ni, nj))
                md = max(md, dfs(ni, nj, d + 1))
                visited.remove((ni, nj))

        return md

    visited = set([start])
    return dfs(start[0], start[1], 0)


def get_intersections(grid, start, end):
    R = len(grid)
    C = len(grid[0])
    intersections = [start, end]
    for i in range(R):
        for j in range(C):
            if grid[i][j] == ".":
                poss_paths = list(valid_neighbors(grid, i, j, part2=True))
                if len(poss_paths) > 2:
                    intersections.append((i, j))

    return intersections


def get_intersection_dist(grid, start, end, inters):
    q = deque([(*start, 0)])
    visited = set([start])
    while q:
        i, j, d = q.popleft()

        if (i, j) == end:
            return d

        # if the current cell is not the start, but is an intersection, skip
        # we are only looking for paths that go directly from start to end
        # without passing through any other intersection
        if (i, j) != start and (i, j) in inters:
            continue

        for ni, nj in valid_neighbors(grid, i, j, part2=True):
            if (ni, nj) not in visited:
                visited.add((ni, nj))
                q.append((ni, nj, d + 1))

    return 0


def get_best_intersection_path_dist(graph, start, end):
    def dfs(i, j, d):
        if (i, j) == end:
            return d

        max_dist = 0
        for neigh, dist in graph[(i, j)].items():
            if neigh in visited:
                continue
            visited.add((i, j))
            max_dist = max(max_dist, dfs(*neigh, d + dist))
            visited.remove((i, j))

        return max_dist

    visited = set([start])
    return dfs(*start, 0)


def part2(grid, start, end):
    intersections = get_intersections(grid, start, end)
    graph = defaultdict(dict)
    for i1, j1 in intersections:
        for i2, j2 in intersections:
            if i1 == i2 and j1 == j2:
                continue
            d = get_intersection_dist(grid, (i1, j1), (i2, j2), intersections)
            if d != 0:
                graph[(i1, j1)][(i2, j2)] = d
                graph[(i2, j2)][(i1, j1)] = d

    return get_best_intersection_path_dist(graph, start, end)


def main():
    lines = (
        open(f"{os.path.dirname(__file__)}/input.txt")
        .read()
        .strip()
        .splitlines()
    )
    grid = [[c for c in l] for l in lines]
    start = (0, lines[0].index("."))
    end = (len(grid) - 1, lines[-1].index("."))

    st = time.perf_counter()
    print(f"part 1: {part1(grid, start, end)}")
    print(f"Part 1 took {time.perf_counter()-st} seconds")

    st = time.perf_counter()
    print(f"part 2: {part2(grid, start,end)}")
    print(f"Part 2 took {time.perf_counter()-st} seconds")


main()
