import os
import collections


def solve(hands, part2=False):
    # group hands by strength
    rank = [[] for i in range(25)]  # max strength 25 (AAAAA) -> (5+5+5+5+5)
    for hand in hands:
        strength = calc_strength(hand[0], part2)
        rank[strength - 1].append((map_hand(hand[0], part2), hand[1]))

    # sort all hands of same strength by card ordering and combine to singular list
    sorted_hands = []
    for hands in rank:
        hands.sort(key=lambda x: x[0])
        sorted_hands.extend(hands)

    winnings = 0
    for i in range(len(sorted_hands)):
        winnings += sorted_hands[i][1] * (i + 1)
    return winnings


def map_hand(hand, part2=False):
    """
    maps card values in hand so that hands of the same strength can be compared
    by ascii ordering
    """
    mapping = {
        "A": "Z",
        "K": "Y",
        "Q": "X",
        "J": "W",
        "T": "V",
    }
    if part2:
        mapping["J"] = "1"

    hand = "".join(list(map(lambda x: mapping[x] if x in mapping else x, hand)))
    return hand


def calc_strength(hand, part2=False):
    """
    strength of hand is the sum of the counts of each card. ex:
    AAAAA -> 5+5+5+5+5
    AAAAQ -> 4+4+4+4+1
    AAAQQ -> 3+3+3+2+2
    AAAQ9 -> 3+3+3+1+1
    AAQQ9 -> 2+2+2+2+1
    AAQ98 -> 2+2+1+1+1
    23456 -> 1+1+1+1+1

    if on part 2, turn J cards into highest frequency card that is not a J
    """
    strength = 0
    card_counts = collections.Counter(hand)
    card_strengths = [card_counts[c] for c in hand]
    strength = sum(card_strengths)

    if part2 and "J" in card_counts:
        max_card = ("", 0)
        for k, v in card_counts.items():
            if k != "J" and v > max_card[1]:
                max_card = (k, v)
        card_counts[max_card[0]] += card_counts["J"]
        card_counts["J"] = card_counts[max_card[0]]
        card_strengths = [card_counts[c] for c in hand]
        strength = max(strength, sum(card_strengths))

    return strength


def main():
    hands = [
        (hand.split()[0], int(hand.split()[1]))
        for hand in open(f"{os.path.dirname(__file__)}/input.txt").read().strip().split("\n")
    ]

    print(solve(hands))
    print(solve(hands, part2=True))


main()
