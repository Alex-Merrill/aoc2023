def part1(lines):
    sum = 0
    for line in lines:
        game_id, game_data = line.split(":")
        _, game_id = game_id.split()
        winning_nums, my_nums = game_data.split("|")
        winning_nums = set(winning_nums.split())
        my_nums = set(my_nums.split())
        num_wins = len(my_nums.intersection(winning_nums))
        sum += pow(2, num_wins-1) if num_wins else 0

    return sum


def part2(lines):
    total_scratchcards = 0
    copies = [1] * len(lines)
    for i, line in enumerate(lines):
        while copies[i] > 0:
            game_id, game_data = line.split(":")
            _, game_id = game_id.split()
            winning_nums, my_nums = game_data.split("|")
            winning_nums = set(winning_nums.split())
            my_nums = set(my_nums.split())
            num_wins = len(my_nums.intersection(winning_nums))
            for j in range(i+1, i+1+num_wins):
                copies[j] += 1
            
            copies[i] -= 1
            total_scratchcards += 1


    return total_scratchcards


def main():
    lines = []
    with open("input.txt") as f:
        for line in f:
            lines.append(line.strip())
    print(part1(lines))
    print(part2(lines))


main()