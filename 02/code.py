import collections
import os
import re


def part1(lines):
    max_cubes = {"red": 12, "green": 13, "blue": 14}
    sum = 0
    for l in lines:
        game, game_data = l.split(":")  # "Game x:", "3 blue, 4 red; 1 green"
        game_id = int(game.split()[1])
        rounds = game_data.split(";")  # ["3 blue, 4 red", "1 green"]
        max_cubes_drawn = collections.defaultdict(int)
        game_invalid = False
        for r in rounds:
            cube_draws = r.split(",")  # ["3 blue", "4 red"]
            for draw in cube_draws:
                num_cubes, color = draw.split()
                max_cubes_drawn[color] = max(
                    max_cubes_drawn[color], int(num_cubes)
                )
                if max_cubes_drawn[color] > max_cubes[color]:
                    game_invalid = True

        if game_invalid:
            continue

        sum += game_id

    return sum


def part2(lines):
    sum = 0
    for l in lines:
        game, game_data = l.split(":")  # "Game x:", "3 blue, 4 red; 1 green"
        game_id = int(game.split()[1])
        rounds = game_data.split(";")  # ["3 blue, 4 red", "1 green"]
        max_cubes_drawn = collections.defaultdict(int)
        game_invalid = False
        for r in rounds:
            cube_draws = r.split(",")  # ["3 blue", "4 red"]
            for draw in cube_draws:
                num_cubes, color = draw.split()
                max_cubes_drawn[color] = max(
                    max_cubes_drawn[color], int(num_cubes)
                )

        power = 1
        for v in max_cubes_drawn.values():
            power *= v

        sum += power

    return sum


def main():
    lines = []
    with open(f"{os.path.dirname(__file__)}/input.txt") as f:
        for line in f:
            lines.append(line.strip())
    print(part1(lines))
    print(part2(lines))


main()
