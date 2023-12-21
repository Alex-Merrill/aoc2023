import os
def hash(word):
    val = 0
    for c in word:
        val += ord(c)
        val *= 17
        val %= 256

    return val


def generate_boxes(words):
    # since dicts are insertion-ordered, we can just use them without
    # having to worry about ordering
    boxes = [{} for _ in range(256)]
    for word in words:
        if "-" in word:
            label = word[:-1]
            box_id = hash(label)
            if label in boxes[box_id]:
                del boxes[box_id][label]
        else:
            label, lens = word.split("=")
            box_id = hash(label)
            boxes[box_id][label] = int(lens)

    return boxes


def part1(words):
    res = 0
    for word in words:
        res += hash(word)
    return res


def part2(words):
    boxes = generate_boxes(words)
    s = 0
    for i, box in enumerate(boxes):
        j = 1
        for label, lens in box.items():
            s += (1 + i) * j * lens
            j += 1

    return s


def main():
    inpt = open(f"{os.path.dirname(__file__)}/input.txt").read().strip()
    words = inpt.split(",")

    print(f"part 1: {part1(words)}")
    print(f"part2: {part2(words)}")


main()
