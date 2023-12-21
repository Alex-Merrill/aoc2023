import os
def part1(seq):
    lines = [seq]
    seq_i = 0
    not_zero = True
    while not_zero:
        new_seq = []
        not_zero = False
        for i in range(len(lines[seq_i]) - 1):
            curr, next = lines[seq_i][i], lines[seq_i][i + 1]
            new_seq.append(next - curr)
            if next - curr != 0:
                not_zero = True

        lines.append(new_seq)
        seq_i += 1

    prev_diff = 0
    for i in range(len(lines) - 2, -1, -1):
        lines[i].append(lines[i][-1] + prev_diff)
        prev_diff = lines[i][-1]

    return lines[0][-1]


def part2(seq):
    lines = [seq]
    seq_i = 0
    not_zero = True
    while not_zero:
        new_seq = []
        not_zero = False
        for i in range(1, len(lines[seq_i])):
            curr, prev = lines[seq_i][i], lines[seq_i][i - 1]
            new_seq.append(curr - prev)
            if curr - prev != 0:
                not_zero = True

        lines.append(new_seq)
        seq_i += 1

    prev_diff = 0
    for i in range(len(lines) - 2, -1, -1):
        lines[i].insert(0, lines[i][0] - prev_diff)
        prev_diff = lines[i][0]

    return lines[0][0]


def main():
    inpt = [
        line.split() for line in open(f"{os.path.dirname(__file__)}/input.txt").read().strip().split("\n")
    ]
    seqs = [[int(x) for x in seq] for seq in inpt]
    predictions = []
    for seq in seqs:
        predictions.append(part1(seq))
    print(f"part1: {sum(predictions)}")
    predictions = []
    for seq in seqs:
        predictions.append(part2(seq))
    print(f"part2: {sum(predictions)}")


main()
