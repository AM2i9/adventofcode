from aoc.helpers import aoc

# https://adventofcode.com/2021/day/1


@aoc(2021, 1)
def part1(input):

    depths = [int(d) for d in input.splitlines()]

    count = 0

    for i, depth in enumerate(depths[1:]):
        if depth > depths[i]:
            count += 1

    return count


@aoc(2021, 1)
def part2(input):

    depths = [int(d) for d in input.splitlines()]

    count = 0
    prev_sum = -1

    for i in range(1, len(depths) - 1):
        s = sum((depths[i - 1 : i + 2]))
        if s > prev_sum and prev_sum != -1:
            count += 1
        prev_sum = s

    return count
