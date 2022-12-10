from aoc.helpers import aoc

# https://adventofcode.com/2022/day/10


@aoc(2022, 10)
def part1(input):

    cycles = {}
    X = 1
    cycle = 1

    for line in input.splitlines():
        c = line.split()[0]
        if c == "addx":
            cycles[cycle] = X
            cycle += 1
            X += int(line.split()[1])
        cycles[cycle] = X
        cycle += 1

    sig_sum = 0
    for c in (20, 60, 100, 140, 180, 220):
        sig_sum += c * cycles[c-1]

    return sig_sum

@aoc(2022, 10)
def part2(input):

    cycles = {0:1}
    X = 1
    cycle = 1

    for line in input.splitlines():
        c = line.split()[0]
        if c == "addx":
            cycles[cycle] = X
            cycle += 1
            X += int(line.split()[1])
        cycles[cycle] = X
        cycle += 1

    row = 0
    col = 0
    for cycle in range(1, len(cycles.items()) + 1):
        value = cycles[cycle-1]
        if col in (value- 1, value, value + 1):
            print("#", end="")
        else:
            print(".", end="")
        col += 1
        if cycle // 40 > row:
            row = cycle // 40
            col = 0
            print()

