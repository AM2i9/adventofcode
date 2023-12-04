from aoc.helpers import aoc

# https://adventofcode.com/2023/day/4


@aoc(2023, 4)
def part1(input: str):

    cards = input.strip().splitlines()

    score = 0

    for card in cards:

        nums = card[8:]
        elf_nums, winning_nums = nums.split(" | ")

        elf_nums = set(
            [int(n.strip()) for n in elf_nums.split(" ") if n.strip().isnumeric()]
        )

        winning_nums = set(
            [int(n.strip()) for n in winning_nums.split(" ") if n.strip().isnumeric()]
        )

        matches = list(elf_nums & winning_nums)

        if len(matches) > 0:
            score += 2 ** (len(matches) - 1)

    return score


@aoc(2023, 4)
def part2(input: str):

    cards = input.strip().splitlines()

    card_counts = []
    total = 0

    for id, card in enumerate(cards):

        nums = card[8:]
        elf_nums, winning_nums = nums.split(" | ")

        elf_nums = set(
            [int(n.strip()) for n in elf_nums.split(" ") if n.strip().isnumeric()]
        )

        winning_nums = set(
            [int(n.strip()) for n in winning_nums.split(" ") if n.strip().isnumeric()]
        )

        matches = list(elf_nums & winning_nums)

        card_counts.append((id, len(matches)))

    i = 0
    for id, card_score in card_counts:
        card_counts.extend( # baaaaaad I'm being devious this year
            card_counts[
                id + 1 : m if (m := id + card_score + 1) < len(cards) else len(cards)
            ]
        )
        i += 1

    return len(card_counts)
