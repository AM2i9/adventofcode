from aoc.helpers import aoc

import re
from pprint import pprint

from more_itertools import split_at

# https://adventofcode.com/2022/day/5


def parse_input(input):
    crates, moves = input.split("\n\n")

    stacks = [[] for _ in range(0, 9)]

    for row in crates.splitlines()[:-1]:
        for i, crate in enumerate(re.findall("\[(\S)\][ \n]?|   [ \n]?", row)):
            if crate:
                stacks[i].insert(0, crate)

    instructions = re.findall("move (\d\d?) from (\d) to (\d)", moves)

    return stacks, instructions


def move_crates(input, part):
    stacks, instructions = parse_input(input)

    for quan, stack, dest in instructions:
        if part == 1:
            n = stacks[int(stack) - 1][-int(quan) :][::-1]
        else:
            n = stacks[int(stack) - 1][-int(quan) :]
        stacks[int(stack) - 1] = stacks[int(stack) - 1][: -int(quan)]
        stacks[int(dest) - 1].extend(n)

    return "".join([stack[-1] for stack in stacks if stack[-1:]])


@aoc(2022, 5)
def part1(input):
    return move_crates(input, 1)


@aoc(2022, 5)
def part2(input):
    return move_crates(input, 2)
