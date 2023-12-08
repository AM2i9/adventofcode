from collections import Counter
from enum import Enum
from aoc.helpers import aoc

# https://adventofcode.com/2023/day/7


class T(Enum):
    FiveOfAKind = 7
    FourOfAKind = 6
    FullHouse = 5
    ThreeOfAKind = 4
    TwoPair = 3
    OnePair = 2
    HighCard = 1


cardmap = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "J": 11,
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2,
    "0": 0,
}


@aoc(2023, 7)
def part1(input: str):

    hands = [
        ((h := line.split(" "))[0], int(h[1])) for line in input.strip().splitlines()
    ]

    hands_with_scores = []

    for hand, bid in hands:

        counts = list(Counter(hand).values())
        counts.sort(reverse=True)

        hand_score = 0

        if counts[0] == 5:
            # five of a kind
            hand_score = T.FiveOfAKind
        elif counts[0] == 4:
            # four of a kind
            hand_score = T.FourOfAKind
        elif counts[0] == 3 and counts[1] == 2:
            # full house
            hand_score = T.FullHouse
        elif counts[0] == 3 and counts[1] == 1:
            # three of a kind
            hand_score = T.ThreeOfAKind
        elif counts[0] == 2 and counts[1] == 2:
            # two pair
            hand_score = T.TwoPair
        elif counts[0] == 2 and counts[1] == 1:
            # one pair
            hand_score = T.OnePair
        elif counts[0] == 1:
            # high card
            hand_score = T.HighCard

        hands_with_scores.append((hand, bid, hand_score))

    hands_with_scores.sort(
        key=lambda hand: (hand[2].value, *(cardmap[c] for c in hand[0]))
    )

    return sum(hand[1] * i for i, hand in enumerate(hands_with_scores, start=1))


@aoc(2023, 7)
def part2(input: str):

    hands = [
        ((h := line.split(" "))[0].replace("J", "0"), int(h[1]))
        for line in input.strip().splitlines()
    ]

    hands_with_scores = []

    for hand, bid in hands:

        counter = Counter(hand)

        joker_value = counter.get("0", 0)
        del counter["0"]

        counts = list(counter.values())
        counts.sort(reverse=True)

        if counts:
            counts[0] += joker_value
        else:
            counts.append(5)

        hand_score = 0

        if counts[0] == 5:
            # five of a kind
            hand_score = T.FiveOfAKind
        elif counts[0] == 4:
            # four of a kind
            hand_score = T.FourOfAKind
        elif counts[0] == 3 and counts[1] == 2:
            # full house
            hand_score = T.FullHouse
        elif counts[0] == 3 and counts[1] == 1:
            # three of a kind
            hand_score = T.ThreeOfAKind
        elif counts[0] == 2 and counts[1] == 2:
            # two pair
            hand_score = T.TwoPair
        elif counts[0] == 2 and counts[1] == 1:
            # one pair
            hand_score = T.OnePair
        elif counts[0] == 1:
            # high card
            hand_score = T.HighCard

        hands_with_scores.append((hand, bid, hand_score))

    hands_with_scores.sort(
        key=lambda hand: (hand[2].value, *(cardmap[c] for c in hand[0]))
    )

    return sum(hand[1] * i for i, hand in enumerate(hands_with_scores, start=1))
