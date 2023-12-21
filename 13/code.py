import os
def row_sym(pattern, diffs_req=0):
    for i in range(len(pattern) - 1):
        total_diffs = 0
        for first, second in zip(pattern[i::-1], pattern[i + 1 :]):
            total_diffs += sum([f != s for f, s in zip(first, second)])
            if total_diffs > diffs_req:
                break

        if total_diffs == diffs_req:
            return i + 1

    return 0


def main():
    patterns = open(f"{os.path.dirname(__file__)}/input.txt").read().strip().split("\n\n")
    patterns = [pattern.split("\n") for pattern in patterns]

    p1_ans = 0
    p2_ans = 0
    for pattern in patterns:
        r_sym1 = row_sym(pattern)
        r_sym2 = row_sym(pattern, diffs_req=1)

        pattern = list(zip(*pattern[::-1]))
        c_sym1 = row_sym(pattern)
        c_sym2 = row_sym(pattern, diffs_req=1)

        p1_ans += c_sym1 + r_sym1 * 100
        p2_ans += c_sym2 + r_sym2 * 100

    print(f"part1: {p1_ans}")
    print(f"part2: {p2_ans}")


main()
