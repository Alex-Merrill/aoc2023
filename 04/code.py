import os
def part1(lines):
    sum = 0
    for line in lines:
        _, game_data = line.split(":")
        winning_nums, my_nums = game_data.split("|")
        winning_nums = set(winning_nums.split())
        my_nums = set(my_nums.split())
        num_wins = len(my_nums.intersection(winning_nums))
        sum += pow(2, num_wins-1) if num_wins else 0

    return sum


def part2(lines):
    copies = [1] * len(lines)
    for i, line in enumerate(lines):
        _, game_data = line.split(":")
        winning_nums, my_nums = game_data.split("|")
        winning_nums = set(winning_nums.split())
        my_nums = set(my_nums.split())
        num_wins = len(my_nums.intersection(winning_nums))

        for j in range(i+1, min(i+1+num_wins, len(lines))):
            copies[j] += copies[i]
        
    return sum(copies)


def main():
    lines = []
    with open(f"{os.path.dirname(__file__)}/input.txt") as f:
        for line in f:
            lines.append(line.strip())
    print(part1(lines))
    print(part2(lines))


main()