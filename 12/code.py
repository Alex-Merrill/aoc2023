import os
import time


def solve(s, groups):
    def rec(s_i, group_i, cur_group_len):
        c_key = (s_i, group_i, cur_group_len)
        if c_key in cache:
            return cache[c_key]

        if s_i == len(s):
            # no damaged machines since last group
            if group_i == len(groups) and cur_group_len == 0:
                return 1
            # last group goes till end of string
            if group_i == len(groups) - 1 and cur_group_len == groups[group_i]:
                return 1
            return 0

        perms = 0
        groups_used = group_i >= len(groups)

        # machine damaged:
        if s[s_i] == "#":
            if (
                not groups_used and cur_group_len < groups[group_i]
            ):  # continue group or start group
                perms += rec(s_i + 1, group_i, cur_group_len + 1)

        # machine working
        if s[s_i] == ".":
            if (
                not groups_used and cur_group_len == groups[group_i]
            ):  # group ends
                perms += rec(s_i + 1, group_i + 1, 0)
            if cur_group_len == 0:  # don't start group
                perms += rec(s_i + 1, group_i, 0)

        # machine unknown
        if s[s_i] == "?":
            if (
                not groups_used and cur_group_len == groups[group_i]
            ):  # group ends
                perms += rec(s_i + 1, group_i + 1, 0)
            if (
                not groups_used and cur_group_len < groups[group_i]
            ):  # continue group or start group
                perms += rec(s_i + 1, group_i, cur_group_len + 1)
            if cur_group_len == 0:  # choose not to start a group here
                perms += rec(s_i + 1, group_i, 0)

        cache[c_key] = perms

        return perms

    cache = {}
    return rec(0, 0, 0)


def main():
    rows = open(f"{os.path.dirname(__file__)}/input.txt").read().strip().splitlines()
    rows = [
        (row.split()[0], [int(g) for g in row.split()[1].split(",")])
        for row in rows
    ]

    start = time.perf_counter()
    p1_ans = [solve(*row) for row in rows]
    print(f"part1: {sum(p1_ans)} in {time.perf_counter() - start} seconds")

    start = time.perf_counter()
    rows = [("?".join([row[0]] * 5), row[1] * 5) for row in rows]
    p2_ans = [solve(*row) for row in rows]
    print(f"part2: {sum(p2_ans)} in {time.perf_counter() - start} seconds")


main()
