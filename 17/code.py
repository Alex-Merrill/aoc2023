import os
import heapq


def solve(grid, min_straight=0, max_straight=3):
    R = len(grid)
    C = len(grid[0])
    end = (R - 1, C - 1)
    heap = [
        (grid[1][0], 1, 0, 1, 0, 1),
        (grid[0][1], 0, 1, 0, 1, 1),
    ]  # (cost,i,j,di,dj,straight)
    heapq.heapify(heap)
    visited = set()
    min_cost = float("infinity")

    while heap:
        cost_so_far, i, j, di, dj, straight = heapq.heappop(heap)

        if (i, j) == end:
            min_cost = min(min_cost, cost_so_far)
            continue

        if (i, j, di, dj, straight) in visited:
            continue

        visited.add((i, j, di, dj, straight))

        # straight
        if straight < max_straight and 0 <= i + di < R and 0 <= j + dj < C:
            ni, nj = i + di, j + dj
            new_cost = cost_so_far + grid[ni][nj]
            heapq.heappush(heap, (new_cost, ni, nj, di, dj, straight + 1))

        # turn
        if straight >= min_straight:
            for ndi, ndj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if ndi == di and ndj == dj:  # straight
                    continue
                if ndi == -di and ndj == -dj:  # reverse
                    continue
                ni, nj = i + ndi, j + ndj
                if 0 <= ni < R and 0 <= nj < C:
                    new_cost = cost_so_far + grid[ni][nj]
                    heapq.heappush(heap, (new_cost, ni, nj, ndi, ndj, 1))

    return min_cost


def main():
    inpt = open(f"{os.path.dirname(__file__)}/input.txt").read().strip().splitlines()
    grid = [[int(c) for c in row] for row in inpt]

    p1_ans = solve(grid)
    print(f"part 1: {p1_ans}")

    p2_ans = solve(grid, min_straight=4, max_straight=10)
    print(f"part2: {p2_ans}")


main()
