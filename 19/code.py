import os
from collections import deque


def solve1(parts, workflows):
    total = 0
    for part in parts:
        curr_workflow = "in"
        while curr_workflow != "A" and curr_workflow != "R":
            rules = workflows[curr_workflow]
            for i, rule in enumerate(rules):
                if i == len(rules) - 1:
                    curr_workflow = rule
                    break

                k = rule[0][0]
                cond = int(rule[2:].split(":")[0])
                dest = rule.split(":")[1]
                if "<" in rule:
                    if part[k] < cond:
                        curr_workflow = dest
                        break
                elif ">" in rule:
                    if part[k] > cond:
                        curr_workflow = dest
                        break

        if curr_workflow == "A":
            total += sum(part.values())

    return total


def solve2(workflows):
    total = 0
    parts = deque()
    parts.append(({k: (1, 4000) for k in "xmas"}, "in"))
    while parts:
        curr_part, curr_workflow = parts.popleft()
        while curr_workflow != "A" and curr_workflow != "R":
            rules = workflows[curr_workflow]
            for i, rule in enumerate(rules):
                if i == len(rules) - 1:
                    curr_workflow = rule
                    break

                k = rule[0][0]
                rnge = curr_part[k]
                cond = int(rule[2:].split(":")[0])
                dest = rule.split(":")[1]
                if "<" in rule:
                    if rnge[0] < cond <= rnge[1]:
                        new_part = {**curr_part, k: (rnge[0], cond - 1)}
                        parts.append((new_part, dest))
                        curr_part = {**curr_part, k: (cond, rnge[1])}
                    if rnge[1] < cond:
                        curr_workflow = dest
                        break
                elif ">" in rule:
                    if rnge[0] <= cond < rnge[1]:
                        new_part = {**curr_part, k: (cond + 1, rnge[1])}
                        parts.append((new_part, dest))
                        curr_part = {**curr_part, k: (rnge[0], cond)}
                    if rnge[0] > cond:
                        curr_workflow = dest
                        break

        if curr_workflow == "A":
            total += combs(curr_part.values())

    return total


def combs(ranges):
    t = 1
    for rnge in ranges:
        t *= rnge[1] - rnge[0] + 1
    return t


def main():
    rules, parts = open(f"{os.path.dirname(__file__)}/input.txt").read().strip().split("\n\n")
    rules = {
        rule.split("{")[0]: rule.split("{")[1][:-1].split(",")
        for rule in rules.splitlines()
    }
    parts = [
        {v.split("=")[0]: int(v.split("=")[1]) for v in part[1:-1].split(",")}
        for part in parts.splitlines()
    ]

    p1_ans = solve1(parts, rules)
    print(f"part 1: {p1_ans}")

    p2_ans = solve2(rules)
    print(f"part2: {p2_ans}")


main()
