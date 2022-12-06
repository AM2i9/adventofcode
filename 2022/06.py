from aoc.helpers import aoc
import more_itertools
# https://adventofcode.com/2022/day/6

@aoc(2022, 6)
def part1(input):
    for i, x in enumerate(more_itertools.sliding_window(input.strip(), 4)):
        if len(set(x)) == len(x):
            return i + 4

@aoc(2022, 6)
def part2(input):
    for i, x in enumerate(more_itertools.sliding_window(input.strip(), 14)):
        if len(set(x)) == len(x):
            return i + 14
    
