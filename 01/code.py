import os
import re


def part1(lines):
    # read input
    sum = 0
    for line in lines:
        n = ""
        l = 0
        while l < len(line):
            if line[l].isnumeric():
                n += line[l]
                break
            l += 1

        r = len(line) - 1
        while r >= l:
            if line[r].isnumeric():
                n += line[r]
                break
            r -= 1
        sum += int(n)

    return sum


def part2(lines):
    num_dict = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
        "1": "1",
        "2": "2",
        "3": "3",
        "4": "4",
        "5": "5",
        "6": "6",
        "7": "7",
        "8": "8",
        "9": "9",
    }
    sum = 0
    for l in lines:
        nums = []
        for k, v in num_dict.items():
            for match in re.finditer(k, l):
                if match.start() != -1:
                    nums.append((match.start(), v))
        nums.sort()
        calibration = nums[0][1] + nums[-1][1]

        sum += int(calibration)

    return sum


def main():
    lines = []
    with open(f"{os.path.dirname(__file__)}/input.txt") as f:
        for line in f:
            lines.append(line.strip())
    print(part1(lines))
    print(part2(lines))


main()
