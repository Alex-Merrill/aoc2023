import os
import re
from collections import defaultdict, deque


def get_cells(brick):
    return [
        (x, y, z)
        for x in range(brick[0], brick[3] + 1)
        for y in range(brick[1], brick[4] + 1)
        for z in range(brick[2], brick[5] + 1)
    ]


def drop(brick):
    return (
        brick[0],
        brick[1],
        brick[2] - 1,
        brick[3],
        brick[4],
        brick[5] - 1,
        brick[6],
    )


def collapse(bricks):
    matrix3d = {}

    for i, brick in enumerate(bricks):
        while min(brick[2], brick[5]) > 1 and all(
            cell not in matrix3d for cell in get_cells(drop(brick))
        ):
            brick = drop(brick)
        for cell in get_cells(brick):
            matrix3d[cell] = brick[6]
        bricks[i] = brick

    return matrix3d


def get_supports(matrix3d, bricks):
    supports = defaultdict(set)
    supported = defaultdict(set)
    for brick in bricks:
        cells, lbl = get_cells(brick), brick[6]
        supports[lbl] = set()
        for x, y, z in cells:
            if (x, y, z + 1) in matrix3d and matrix3d[x, y, z + 1] != lbl:
                supports[lbl].add(matrix3d[x, y, z + 1])
                supported[matrix3d[x, y, z + 1]].add(lbl)

    return supports, supported


def part1(bricks):
    matrix3d = collapse(bricks)
    supports, supported = get_supports(matrix3d, bricks)
    dis = 0
    for curr_lbl, above_curr in supports.items():
        multi_supports = True
        for brick in above_curr:
            if len(supported[brick]) == 1:
                multi_supports = False

        if multi_supports:
            dis += 1

    return dis


def part2(bricks):
    matrix3d = collapse(bricks)
    supports, supported = get_supports(matrix3d, bricks)
    total_dis = 0
    for brick in bricks:
        lbl = brick[6]
        q = deque(supports[lbl])
        dis = set([lbl])
        while q:
            curr_brick = q.popleft()
            if curr_brick in dis:
                continue

            below_curr = supported[curr_brick]
            has_support = False
            for support in below_curr:
                if support not in dis:
                    has_support = True

            if not has_support:
                dis.add(curr_brick)
                for above_curr in supports[curr_brick]:
                    q.append(above_curr)

        total_dis += len(dis) - 1

    return total_dis


def main():
    lines = (
        open(f"{os.path.dirname(__file__)}/input.txt")
        .read()
        .strip()
        .splitlines()
    )
    bricks = [
        [*map(int, re.findall(r"\d+", l)), i] for i, l in enumerate(lines)
    ]
    bricks.sort(key=lambda x: min(x[2], x[5]))

    print(f"part 1: {part1(bricks)}")

    print(f"part 2: {part2(bricks)}")


main()
