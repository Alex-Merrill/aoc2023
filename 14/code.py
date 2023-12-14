def push_north(rows):
    """
    pushes all rocks north
    """
    for i in range(1, len(rows)):
        for j in range(len(rows[0])):
            if rows[i][j] != "O":
                continue
            curr_row = i
            while curr_row >= 1 and rows[curr_row - 1][j] == ".":
                rows[curr_row - 1][j] = "O"
                rows[curr_row][j] = "."
                curr_row = curr_row - 1

    return rows


def part2(rows, cycles):
    """
    for each cycle, push rocks north, transpose, repeat, until one
    cycle has completed. We store the grid state and cycle iteration
    to look for a point in which we have a repeated grid state.
    Since each cycle iteration does the same operations, we know we have
    now found a loop. Now we simply calculate which iteration in the loop
    the grid will be at after "cycles" iterations and return that grid state
    """
    g_to_cycle = dict()
    cycle_to_g = dict()
    cycle_start = None
    period = None
    for i in range(1, cycles + 1):
        for _ in range(4):
            rows = push_north(rows)
            rows = transpose(rows)

        key = "\n".join(["".join(r) for r in rows])
        if key in g_to_cycle:
            cycle_start = g_to_cycle[key]
            period = i - cycle_start
            break

        g_to_cycle[key] = i
        cycle_to_g[i] = key

    cycles = cycle_start + (cycles - cycle_start) % period
    return cycle_to_g[cycles].split("\n")


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
    inpt = open("input.txt").read().strip().splitlines()
    rows = [list(row) for row in inpt]

    end_state = push_north([[c for c in row] for row in rows])
    print(f"part1: {calc_load(end_state)}")

    cycles = 1000000000
    end_state = part2([[c for c in row] for row in rows], cycles)
    print(f"part2: {calc_load(end_state)}")


main()
