import os
from collections import deque


def solve(grid, start, part2=False):
    end_steps = 26501365 if part2 else 64
    D = len(grid)
    q = deque([(*start, 0)])
    factors = []
    step = 0
    while True:
        step += 1
        next_q = set()
        while q:
            ci, cj, gi, gj, s = q.popleft()

            for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                ni, nj = ci + di, cj + dj

                ngi = gi + ni // len(grid)
                ngj = gj + nj // len(grid[0])
                ni = ni % len(grid)
                nj = nj % len(grid[0])

                if grid[ni][nj] == "#" or (ni, nj, ngi, ngj) in next_q:
                    continue

                next_q.add((ni, nj, ngi, ngj, s + 1))

        q = deque(next_q)

        if not part2 and step == end_steps:
            return len(q)
        if part2 and step % D == end_steps % D:
            factors.append(len(q))
            if len(factors) == 3:
                break

    f = lambda n, a, b, c: a + n * (b - a) + n * (n - 1) // 2 * ((c - b) - (b - a))

    return f(end_steps // D, *factors)


def calc_steps(visited, parity):
    ans = 0
    for k, v in visited.items():
        if v % 2 == parity or k[2] != 0 or k[3] != 0:
            continue
        ans += 1
    return ans


def main():
    lines = open(f"{os.path.dirname(__file__)}/input.txt").read().strip().splitlines()
    grid = [[c for c in r] for r in lines]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "S":
                start = (i, j, 0, 0)
                grid[i][j] = "."

    print(f"part 1: {solve(grid, start)}")

    print(f"part 2: {solve(grid, start, part2=True)}")


main()
