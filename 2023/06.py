from functools import reduce
import math
from aoc.helpers import aoc

# https://adventofcode.com/2023/day/6


@aoc(2023, 6)
def part1(input: str):
    # did this first part in desmos, but it uses scientific notation once
    # the numbers get big enough

    # This problem describes basically a graph, with a peak at half the time.
    # plotting this graph, we can get d = -x^2 + tx, with d being distance and t being time.

    lines = input.strip().splitlines()

    times = [int(n) for n in lines[0][5:].strip().split(" ") if n]
    distances = [int(n) for n in lines[1][9:].strip().split(" ") if n]

    nums = []

    print(list(zip(times, distances)))

    for t, d in zip(times, distances):

        # quadratic formula it to get the x value

        min = (-t + math.sqrt((t**2) - (4 * d))) // -2
        max = (-t - math.sqrt((t**2) - (4 * d))) // -2

        nums.append(max - min)

    return int(reduce(lambda x, y: x * y, nums))


@aoc(2023, 6)
def part2(input: str):

    lines = input.strip().splitlines()

    t = int(lines[0][5:].strip().replace(" ", ""))
    d = int(lines[1][9:].strip().replace(" ", ""))

    min = (-t + math.sqrt((t**2) - (4 * d))) // -2
    max = (-t - math.sqrt((t**2) - (4 * d))) // -2

    return int(max - min)
