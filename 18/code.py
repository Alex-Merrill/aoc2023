import os
def solve(insts):
    """
    shoelace + picks theorem
    """
    dirs = {
        "0": (0, 1),
        "1": (1, 0),
        "2": (0, -1),
        "3": (-1, 0),
        "R": (0, 1),
        "D": (1, 0),
        "L": (0, -1),
        "U": (-1, 0),
    }
    total = 0
    perimiter = 0
    i = j = 0
    for dir, dist in insts:
        di, dj = dirs[dir]
        ni = i + (di * dist)
        nj = j + (dj * dist)
        total += i * nj
        total -= j * ni
        perimiter += dist
        i, j = ni, nj

    area = abs(total) // 2

    return area + perimiter // 2 + 1


def main():
    inpt = open(f"{os.path.dirname(__file__)}/input.txt").read().strip().splitlines()
    insts = [(r.split()[0], int(r.split()[1])) for r in inpt]

    p1_ans = solve(insts)
    print(f"part 1: {p1_ans}")

    new_insts = []
    for r in inpt:
        hex = r.split()[2][2:-1]
        dir = hex[-1]
        dist = int(hex[:-1], 16)
        new_insts.append((dir, dist))

    p2_ans = solve(new_insts)
    print(f"part2: {p2_ans}")


main()
