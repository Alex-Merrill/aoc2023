import os
from collections import deque


def calc_energy(grid, start, dir):
    R = len(grid)
    C = len(grid[0])
    curr_beams = deque([(*start, *dir)])
    visited = set()
    while curr_beams:
        i, j, di, dj = curr_beams.pop()

        if i < 0 or i >= R or j < 0 or j >= C:
            continue

        if (i, j, di, dj) in visited:
            continue

        visited.add((i, j, di, dj))

        curr = grid[i][j]
        if curr == "/":
            di, dj = -dj, -di
        elif curr == "\\":
            di, dj = dj, di
        elif curr == "|":
            if dj:
                di, dj = 1, 0
                curr_beams.append((i + di, j + dj, di, dj))
                di, dj = -1, 0
        elif curr == "-":
            if di:
                di, dj = 0, 1
                curr_beams.append((i + di, j + dj, di, dj))
                di, dj = 0, -1

        curr_beams.append((i + di, j + dj, di, dj))

    return len({(i, j) for i, j, _, _ in visited})


def main():
    inpt = open(f"{os.path.dirname(__file__)}/input.txt").read().strip().splitlines()
    grid = [[c for c in row] for row in inpt]
    R = len(grid)
    C = len(grid[0])

    p1_ans = calc_energy(grid, (0, 0), (0, 1))
    print(f"part 1: {p1_ans}")

    p2_ans = 0
    for i in range(len(grid)):
        p2_ans = max(p2_ans, calc_energy(grid, (i, 0), (0, 1)))
        p2_ans = max(p2_ans, calc_energy(grid, (i, C - 1), (0, -1)))
    for j in range(len(grid[0])):
        p2_ans = max(p2_ans, calc_energy(grid, (0, j), (1, 0)))
        p2_ans = max(p2_ans, calc_energy(grid, (R - 1, j), (-1, 0)))

    print(f"part2: {p2_ans}")


main()
