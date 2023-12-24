import os

import z3


def line(h):
    p1 = h
    p2 = [h[0] + h[3], h[1] + h[4], h[2] + h[5], h[3], h[4], h[5]]
    A = p1[1] - p2[1]
    B = p2[0] - p1[0]
    C = p1[0] * p2[1] - p2[0] * p1[1]
    return A, B, -C


def intersection(L1, L2):
    D = L1[0] * L2[1] - L1[1] * L2[0]
    Dx = L1[2] * L2[1] - L1[1] * L2[2]
    Dy = L1[0] * L2[2] - L1[2] * L2[0]
    if D != 0:
        x = Dx / D
        y = Dy / D
        return x, y
    else:
        return False


def collision_in_past(inter, h1, h2):
    if inter[0] > h1[0] and h1[3] < 0:
        return True
    if inter[0] < h1[0] and h1[3] > 0:
        return True
    if inter[1] > h1[1] and h1[4] < 0:
        return True
    if inter[1] < h1[1] and h1[4] > 0:
        return True
    if inter[0] > h2[0] and h2[3] < 0:
        return True
    if inter[0] < h2[0] and h2[3] > 0:
        return True
    if inter[1] > h2[1] and h2[4] < 0:
        return True
    if inter[1] < h2[1] and h2[4] > 0:
        return True

    return False


def part1(hailstones):
    t_min = 200000000000000
    t_max = 400000000000000
    intersections = 0
    for i1 in range(len(hailstones)):
        for i2 in range(i1, len(hailstones)):
            h1 = hailstones[i1]
            h2 = hailstones[i2]
            if i1 == i2:
                continue

            h1l = line(h1)
            h2l = line(h2)
            inter = intersection(h1l, h2l)
            if inter and not collision_in_past(inter, h1, h2):
                if t_min <= inter[0] <= t_max and t_min <= inter[1] <= t_max:
                    intersections += 1

    return intersections


def part2(hs):
    n = 5
    x, y, z, dx, dy, dz = (
        z3.Real("x"),
        z3.Real("y"),
        z3.Real("z"),
        z3.Real("vx"),
        z3.Real("vy"),
        z3.Real("vz"),
    )
    S = z3.Solver()
    for i in range(n):
        x1, y1, z1, dx1, dy1, dz1 = hs[i]
        t = z3.Real(f"t{i}")
        S.add(x1 + dx1 * t == x + dx * t)
        S.add(y1 + dy1 * t == y + dy * t)
        S.add(z1 + dz1 * t == z + dz * t)

    assert S.check() == z3.sat

    M = S.model()
    return M.evaluate(x + y + z)


def main():
    lines = (
        open(f"{os.path.dirname(__file__)}/input.txt")
        .read()
        .strip()
        .splitlines()
    )
    hailstones = [
        list(map(int, l.split("@")[0].split(",")))
        + list(map(int, l.split("@")[1].split(",")))
        for l in lines
    ]

    print(f"part 1: {part1(hailstones)}")

    print(f"part 2: {part2(hailstones)}")


main()
