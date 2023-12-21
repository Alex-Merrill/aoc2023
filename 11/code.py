import os
def solve(gals, rows_no_gal, cols_no_gal, scale):
    sum_dist = 0
    for i in range(len(gals)):
        for j in range(i + 1, len(gals)):
            num_rows_btwn = len(
                [x for x in rows_no_gal if between(x, gals[i][0], gals[j][0])]
            )
            num_cols_btwn = len(
                [x for x in cols_no_gal if between(x, gals[i][1], gals[j][1])]
            )

            sum_dist += (
                man_dist(gals[i], gals[j])
                + num_rows_btwn * (scale - 1)
                + num_cols_btwn * (scale - 1)
            )

    return sum_dist


def man_dist(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def between(val, b1, b2):
    return min(b1, b2) < val < max(b1, b2)


def main():
    inpt = open(f"{os.path.dirname(__file__)}/input.txt").read().strip().split("\n")
    graph = [[c for c in line] for line in inpt]

    gals = []
    rows_no_gal = [True] * len(graph)
    cols_no_gal = [True] * len(graph[0])
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            if graph[i][j] == "#":
                gals.append((i, j))
                rows_no_gal[i] = False
                cols_no_gal[j] = False
    rows_no_gal = [i for i in range(len(rows_no_gal)) if rows_no_gal[i]]
    cols_no_gal = [i for i in range(len(cols_no_gal)) if cols_no_gal[i]]

    dist = solve(gals, rows_no_gal, cols_no_gal, 2)
    print(f"part1: {dist}")
    dist = solve(gals, rows_no_gal, cols_no_gal, 1000000)
    print(f"part2: {dist}")


main()
