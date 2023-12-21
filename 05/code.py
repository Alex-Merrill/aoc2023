import os
import time


def part1(lines):
    seeds, mappings = get_mappings(lines)
    locations = []
    for seed in seeds:
        curr = seed
        for curr_map in mappings:
            l, r = 0, len(curr_map) - 1
            while l <= r:
                mid = l + (r - l) // 2
                s_start, s_end, d_start = curr_map[mid]
                if s_start <= curr <= s_end:
                    curr = curr - s_start + d_start
                    break
                elif curr > s_end:
                    l = mid + 1
                elif curr < s_start:
                    r = mid - 1
        locations.append(curr)

    return min(locations)


def part2(lines):
    seed_ranges, mappings = get_mappings(lines, part2=True)
    curr_seed_ranges = seed_ranges
    for mapping in mappings:
        new_seed_ranges = []
        while curr_seed_ranges:
            seed_range = curr_seed_ranges.pop()
            seed_range_found = False
            for source_start, source_end, destination_start in mapping:
                off = destination_start - source_start
                if seed_range[1] < source_start or seed_range[0] > source_end:
                    # seed range is not in the current mapping range
                    continue
                elif (
                    seed_range[0] >= source_start
                    and seed_range[1] <= source_end
                ):
                    # seed range is fully within current mapping range
                    new_seed_ranges.append(
                        (seed_range[0] + off, seed_range[1] + off)
                    )
                elif seed_range[0] <= source_end <= seed_range[1]:
                    # seed range is partly in mapping. add intersection to next
                    # round. add non intersection back to current round
                    new_seed_ranges.append(
                        (seed_range[0] + off, source_end + off)
                    )
                    curr_seed_ranges.append((source_end + 1, seed_range[1]))
                elif seed_range[0] <= source_start <= seed_range[1]:
                    # same as above
                    new_seed_ranges.append(
                        (source_start + off, seed_range[1] + off)
                    )
                    curr_seed_ranges.append((seed_range[0], source_start - 1))

                seed_range_found = True
                break

            if not seed_range_found:
                new_seed_ranges.append(seed_range)

        curr_seed_ranges = new_seed_ranges

    return min(curr_seed_ranges, key=lambda t: t[0])[0]


def get_mappings(lines, part2=False):
    """
    mappings[0]: seed-to-soil
    mappings[1]: soil-to-fertilizer
    ...
    mappings[6]: humidity-to-location
    ----------------------------------
    mappings[0][0]: (source_start, source_end, destination_start)
    """
    seeds = [int(n) for n in lines[0].split(":")[1].split()]
    mappings = [[] for i in range(7)]
    mappings_idx = 0
    i = 3
    while i < len(lines):
        if lines[i] == "":
            mappings_idx += 1
            i += 2
            continue

        destination_start, source_start, rnge = lines[i].split()
        source_end = int(source_start) + int(rnge) - 1
        mappings[mappings_idx].append(
            (int(source_start), source_end, int(destination_start))
        )
        i += 1

    # sort mappings
    for i in range(len(mappings)):
        mappings[i].sort(key=lambda t: t[0])

    if part2:
        seed_ranges = []
        for i in range(0, len(seeds), 2):
            seed_ranges.append((seeds[i], seeds[i] + seeds[i + 1] - 1))
        seeds = seed_ranges

    return seeds, mappings


def main():
    lines = []
    with open(f"{os.path.dirname(__file__)}/input.txt") as f:
        for line in f:
            lines.append(line.strip())
    print(part1(lines))
    start = time.perf_counter()
    print(part2(lines))
    print(f"part2 finished in {time.perf_counter() - start} seconds")


main()
