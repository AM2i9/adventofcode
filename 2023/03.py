from operator import mul
from functools import reduce
from aoc.helpers import aoc

# https://adventofcode.com/2023/day/3


def clamp(x, min, max):
    if x < min:
        return min
    elif x > max:
        return max
    return x


@aoc(2023, 3)
def part1(input: str):

    lines = input.strip()[::-1].splitlines()

    lines[-1] += "."  # gotta have this or it won't work for reasons

    sum = 0
    cur_num = 0
    num_cnt = 0
    symbol = False

    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char.isnumeric():
                cur_num += int(char) * (10**num_cnt)
                num_cnt += 1

                if not symbol:
                    for row in lines[
                        clamp(y - 1, 0, len(lines)) : clamp(y + 2, 0, len(lines))
                    ]:
                        symbol = symbol or row[
                            clamp(x - 1, 0, len(row)) : clamp(x + 2, 0, len(row))
                        ].strip(".1234567890")

            else:
                if symbol:
                    sum += cur_num
                num_cnt = 0
                cur_num = 0
                symbol = False

    return sum


@aoc(2023, 3)
def part2(input: str):

    lines = input.strip()[::-1].splitlines()

    lines[-1] += "."  # gotta have this or it won't work for reasons
    # not pround of it

    cur_num = 0
    num_cnt = 0
    symbol = None

    gears = {}

    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char.isnumeric():
                cur_num += int(char) * (10**num_cnt)
                num_cnt += 1

                if not symbol:
                    for coln, row in enumerate(
                        lines[
                            clamp(y - 1, 0, len(lines)) : clamp(y + 2, 0, len(lines))
                        ],
                        start=-(y > 0),
                    ):
                        if "*" in row[
                            clamp(x - 1, 0, len(row)) : clamp(x + 2, 0, len(row))
                        ].strip(".1234567890"):
                            symbol = (
                                row[
                                    clamp(x - 1, 0, len(row)) : clamp(
                                        x + 2, 0, len(row)
                                    )
                                ].index("*")
                                + x,
                                coln + y,
                            )
                            break

            else:
                if symbol:
                    if not gears.get(symbol):
                        gears[symbol] = []
                    gears[symbol].append(cur_num)
                num_cnt = 0
                cur_num = 0
                symbol = None

    sum = 0
    for _, nums in gears.items():
        if len(nums) > 1:
            sum += reduce(mul, nums, 1)

    return sum
