import heapq


def solve(insts):
    grid = {(0, 0, 0, 0)}
    curr_pos = (0, 0)
    dirs = {
        "R": (0, 1),
        "L": (0, -1),
        "D": (1, 0),
        "U": (-1, 0),
    }
    for inst in insts:
        dir = dirs[inst[0]]
        for i in range(inst[1]):
            curr_pos = (curr_pos[0] + dir[0], curr_pos[1] + dir[1])
            if i == inst[1] - 1:
                dir = (0, 0)
            grid.add((*curr_pos, *dir))

    min_i, max_i = 0, 0
    min_j, max_j = 0, 0
    for k in grid:
        if k[0] < min_i:
            min_i = k[0]
        elif k[0] > max_i:
            max_i = k[0]
        if k[1] < min_j:
            min_j = k[1]
        elif k[1] > max_j:
            max_j = k[1]

    R = max_i - min_i + 1
    C = max_j - min_j + 1
    i_off = 0 - min_i
    j_off = 0 - min_j
    composed_grid = [["." for _ in range(C)] for _ in range(R)]
    chars = {(0, 0): "S", (1, 0): "|", (-1, 0): "|", (0, 1): "-", (0, -1): "-"}
    for k in grid:
        i = i_off + k[0]
        j = j_off + k[1]
        composed_grid[i][j] = chars[(k[2], k[3])]

    for i in range(len(composed_grid)):
        for j in range(len(composed_grid[0])):
            if composed_grid[i][j] == "S":
                replace_start(composed_grid, (i, j))

    print_g(composed_grid, replace=False)
    filled_size = fill_in_grid(composed_grid)
    print(len(grid), filled_size)
    print_g(composed_grid)
    return len(grid) + filled_size


def replace_start(grid, start):
    i, j = start
    R = len(grid)
    C = len(grid[0])
    start = 0
    if j + 1 < C and grid[i][j + 1] in ["-", "J", "7", "S"]:
        start += 1
    if j - 1 >= 0 and grid[i][j - 1] in ["-", "L", "F", "S"]:
        start += 2
    if i + 1 < R and grid[i + 1][j] in ["|", "L", "J", "S"]:
        start += 3
    if i - 1 >= 0 and grid[i - 1][j] in ["|", "F", "7", "S"]:
        start += 5

    if start == 3:
        print("here")
        grid[i][j] == "-"
    elif start == 8:
        grid[i][j] = "|"
    elif start == 6:
        grid[i][j] = "L"
    elif start == 7:
        grid[i][j] = "J"
    elif start == 5:
        grid[i][j] = "7"
    elif start == 4:
        grid[i][j] = "F"

    if grid[i][j] == "S":
        print(f"start: {start}")

    return grid


def print_g(grid, replace=True):
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
    for line in grid:
        print("".join([d[c] if replace else c for c in line]))


def fill_in_grid(grid):
    num_inside = 0
    for i in range(len(grid)):
        boundaries = 0
        for j in range(len(grid[0])):
            if grid[i][j] in ["|", "J", "L"]:
                boundaries += 1
            elif grid[i][j] == "." and boundaries % 2 == 1:
                num_inside += 1
                grid[i][j] = "I"
            elif grid[i][j] == ".":
                grid[i][j] = "O"

    return num_inside


def main():
    inpt = open("test.txt").read().strip().splitlines()
    insts = []
    for r in inpt:
        insts.append((r.split()[0], int(r.split()[1]), r.split()[2][1:-1]))

    p1_ans = solve(insts)
    print(f"part 1: {p1_ans}")

    new_insts = []
    dirs = {"0": "R", "1": "D", "2": "L", "3": "U"}
    for inst in insts:
        dir = dirs[inst[2][-1]]
        dist = int(inst[2][1:-1], 16)
        new_insts.append((dir, dist))
    # p2_ans = solve(new_insts)
    # print(f"part2: {p2_ans}")


main()
