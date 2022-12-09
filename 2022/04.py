from aoc.helpers import aoc

# https://adventofcode.com/2022/day/4


@aoc(2022, 4)
def part1(input):
    pairs = [p.split(",") for p in input.splitlines()]

    count = 0

    for a, b in pairs:
        w, x = a.split("-")
        a_r = range(int(w), int(x) + 1)
        y, z = b.split("-")
        b_r = range(int(y), int(z) + 1)

        if len(a_r) > len(b_r):
            a_r, b_r = b_r, a_r

        if len((set(a_r) & set(b_r))) == len(a_r):
            count += 1

    return count


@aoc(2022, 4)
def part2(input):
    pairs = [p.split(",") for p in input.splitlines()]

    count = 0

    for a, b in pairs:
        w, x = a.split("-")
        a_r = range(int(w), int(x) + 1)
        y, z = b.split("-")
        b_r = range(int(y), int(z) + 1)

        if len(a_r) > len(b_r):
            a_r, b_r = b_r, a_r

        if len((set(a_r) & set(b_r))) > 0:
            count += 1

    return count
