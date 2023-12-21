import os
from collections import defaultdict


def part1(lines):
    sum = 0
    gears = defaultdict(list) # (i,j): [num1, num2,..., numx]
    for i in range(len(lines)):
        j = 0
        while j < len(lines[i]):
            if not lines[i][j].isnumeric():
                j += 1
                continue

            j_end = j
            replacement = ""
            while j_end < len(lines[i]) and lines[i][j_end].isnumeric():
                replacement += "."
                j_end += 1
            
            num = int("".join(lines[i][j:j_end]))

            lines[i] = lines[i][:j] + replacement + lines[i][j_end:]

            is_part_number = False
            # left
            if j - 1 >= 0 and not lines[i][j-1].isnumeric() and lines[i][j-1] != ".":
                if lines[i][j-1] == "*":
                    gears[(i, j-1)].append(num)
                    
                is_part_number = True
            
            # right
            if (
                not is_part_number and
                j_end < len(lines[i]) and
                not lines[i][j_end].isnumeric() and
                lines[i][j_end] != "."
            ):
                if lines[i][j_end] == "*":
                    gears[(i, j_end)].append(num)

                is_part_number = True

            # above
            if not is_part_number and i - 1 >= 0:
                for k in range(j-1, j_end + 1):
                    if (
                        k >= 0 and k < len(lines[i]) and
                        not lines[i-1][k].isnumeric() and
                        lines[i-1][k] != '.'
                    ):
                        if lines[i-1][k] == "*":
                            gears[(i-1, k)].append(num)

                        is_part_number = True
                        break
            
            # below
            if not is_part_number and i + 1 < len(lines):
                for k in range(j-1, j_end + 1):
                    if (
                        k >= 0 and k < len(lines[i]) and
                        not lines[i+1][k].isnumeric() and
                        lines[i+1][k] != '.'
                    ):
                        if lines[i+1][k] == "*":
                            gears[(i+1, k)].append(num)
                        is_part_number = True
                        break
            
            sum += num if is_part_number else 0
            j = j_end

    return sum, gears



def part2(gears):
    sum = 0
    for k, v in gears.items():
        prod = 0
        if len(v) == 2:
            prod = v[0] * v[1]
        sum += prod

    return sum

def main():
    lines = []
    with open(f"{os.path.dirname(__file__)}/input.txt") as f:
        for line in f:
            lines.append(line.strip())
    sum, gears = part1(lines)
    print(sum)
    print(part2(gears))


main()