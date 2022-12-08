from aoc.helpers import aoc

import numpy as np

# https://adventofcode.com/2022/day/8

@aoc(2022, 8)
def part1(input):
    input="""30373
25512
65332
33549
35390"""

    trees = np.array([[int(t) for t in x] for x in input.splitlines()])
    count = 0

    counted = []

    for i, row in enumerate(trees):
        for i in range(len(row)):
            to_edge = row[:i]
            other_edge = row[i+1:]
            if 0 == i or i == len(row) - 1 or max(to_edge) < row[i] or max(other_edge) < row[i]:
                counted.append(())
                count += 1
    
    for row in trees:
        for i in range(len(row)):
            to_edge = row[:i]
            other_edge = row[i+1:]
            if 0 == i or i == len(row) - 1 or max(to_edge) < row[i] or max(other_edge) < row[i]:
                print(row[i])
                count += 1

    return count


@aoc(2022, 8)
def part2(input):
    ...
    