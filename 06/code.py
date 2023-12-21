import os
import math


def solve(races):
    """
    must take the floor of the upper root, since we can only hold down
    the button for a whole number of ms, and holding any longer than p_root
    would be slower than the record. vice versa for lower root

    if the quadratic has whole integer roots, we need to decrement the
    upper root and increment the lower root, as holding the button down
    for exactly upper or lower root seconds will tie the record, not beat it
    """
    res = 1
    for t, d in races:
        p_root = (t + math.sqrt(t**2 - 4 * (d))) / 2
        n_root = (t - math.sqrt(t**2 - 4 * (d))) / 2

        if p_root == math.floor(p_root) and n_root == math.ceil(n_root):
            p_root -= 1
            n_root += 1

        res *= math.floor(p_root) - math.ceil(n_root) + 1

    return res


def main():
    times, dists = open(f"{os.path.dirname(__file__)}/input.txt").read().strip().split("\n")
    times = times.split(":")[1].split()
    dists = dists.split(":")[1].split()
    races = [(int(t), int(d)) for t, d in zip(times, dists)]
    race = [(int("".join(times)), int("".join(dists)))]

    print(solve(races))
    print(solve(race))


main()
