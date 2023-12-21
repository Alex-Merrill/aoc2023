import os
import time


def push_north_south(rows, dir):
    row_start = 0 if dir == "north" else len(rows) - 1
    row_end = len(rows) if dir == "north" else -1
    row_step = 1 if dir == "north" else -1
    ob_start = -1 if dir == "north" else len(rows)
    for j in range(len(rows[0])):
        ob_row = ob_start
        for i in range(row_start, row_end, row_step):
            if rows[i][j] == "#":
                ob_row = i
            if rows[i][j] == "O":
                rows[i][j] = "."
                rows[ob_row + row_step][j] = "O"
                ob_row = ob_row + row_step

    return rows


def push_east_west(rows, dir):
    col_start = 0 if dir == "west" else len(rows[0]) - 1
    col_end = len(rows[0]) if dir == "west" else -1
    col_step = 1 if dir == "west" else -1
    ob_start = -1 if dir == "west" else len(rows[0])
    for i in range(len(rows)):
        ob_col = ob_start
        for j in range(col_start, col_end, col_step):
            if rows[i][j] == "#":
                ob_col = j
            if rows[i][j] == "O":
                rows[i][j] = "."
                rows[i][ob_col + col_step] = "O"
                ob_col = ob_col + col_step


def push_rocks(rows, dir):
    if dir in ["north", "south"]:
        push_north_south(rows, dir)
    else:
        push_east_west(rows, dir)


def part1(rows):
    push_rocks(rows, "north")
    return calc_load(rows)


def part2(rows, cycles):
    """
    for each cycle, push rocks in each direction. Then store the grid state
    and the number of cycles it took in order to find a repeating grid state.
    Since each cycle iteration does the same operations, we know we have now
    found a loop. Now we simply calculate which iteration in the loop the
    grid will be at after "cycles" iterations and return that grid state
    """
    g_to_cycle = dict()
    cycle_to_g = dict()
    cycle_start = None
    period = None
    for i in range(1, cycles + 1):
        for dir in ["north", "west", "south", "east"]:
            push_rocks(rows, dir)

        key = "\n".join(["".join(r) for r in rows])
        if key in g_to_cycle:
            cycle_start = g_to_cycle[key]
            period = i - cycle_start
            break

        g_to_cycle[key] = i
        cycle_to_g[i] = key

    cycles = cycle_start + (cycles - cycle_start) % period
    return calc_load(cycle_to_g[cycles].split("\n"))


def calc_load(g):
    sum = 0
    for i, row in enumerate(g):
        for c in row:
            if c == "O":
                sum += len(g) - i

    return sum


def transpose(g):
    return list(map(list, zip(*g[::-1])))


def main():
    inpt = open(f"{os.path.dirname(__file__)}/input.txt").read().strip().splitlines()
    rows = [list(row) for row in inpt]

    t = time.perf_counter()
    p1_ans = part1([[c for c in row] for row in rows])
    print(f"part 1: {p1_ans} in {time.perf_counter() - t} seconds")

    t = time.perf_counter()
    p2_ans = part2([[c for c in row] for row in rows], 1000000000)
    print(f"part2: {p2_ans} in {time.perf_counter() - t} seconds")


main()
