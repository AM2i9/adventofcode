from aoc.helpers import aoc
import more_itertools
# https://adventofcode.com/2022/day/6

@aoc(2022, 6)
def part1(input):
    # for i, x in enumerate(more_itertools.sliding_window(input.strip(), 4)):
    #    if len(set(x)) == len(x):
    #        return i + 4
    return [len(set(input[i-4:i]))==4 for i,x in enumerate(input)].index(True)

@aoc(2022, 6)
def part2(input):
    for i, x in enumerate(more_itertools.sliding_window(input.strip(), 14)):
        if len(set(x)) == len(x):
            return i + 14
    
