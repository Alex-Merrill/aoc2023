def row_sym(pattern, diffs_req=0):
    for i in range(len(pattern) - 1):
        first, second = i, i + 1
        num_diffs = 0
        while first >= 0 and second < len(pattern):
            diffs = num_diff(pattern[first], pattern[second])
            if diffs > 1:
                break
            elif diffs == 1:
                num_diffs += 1

            first -= 1
            second += 1

        if num_diffs == diffs_req and (first < 0 or second >= len(pattern)):
            return i

    return -1


def num_diff(s, r):
    return sum([s != r for s, r in zip(s, r)])


def main():
    patterns = open("input.txt").read().strip().split("\n\n")
    patterns = [pattern.split("\n") for pattern in patterns]

    p1_ans = 0
    p2_ans = 0
    for pattern in patterns:
        r_sym1 = row_sym(pattern)
        r_sym2 = row_sym(pattern, diffs_req=1)

        pattern = list(zip(*pattern[::-1]))
        c_sym1 = row_sym(pattern)
        c_sym2 = row_sym(pattern, diffs_req=1)

        p1_ans += c_sym1 + 1 + (r_sym1 + 1) * 100
        p2_ans += c_sym2 + 1 + (r_sym2 + 1) * 100

    print(f"part1: {p1_ans}")
    print(f"part2: {p2_ans}")


main()
