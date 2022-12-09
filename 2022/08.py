from aoc.helpers import aoc

import numpy as np

# https://adventofcode.com/2022/day/8

@aoc(2022, 8)
def part1(input):

    trees = np.array([[int(t) for t in x] for x in input.splitlines()])

    counted = []

    for y, row in enumerate(trees[1:-1]):
        for x in range(0, len(row)):
            to_edge = row[:x]
            other_edge = row[x+1:]
            if 0 < x < len(row) - 1 and (max(to_edge) < row[x] or max(other_edge) < row[x]):
               counted.append((x, y + 1)) 
                
    for y, row in enumerate(np.flipud(np.rot90(trees))[1:-1], start=1):
        for x in range(len(row)):
            to_edge = row[:x]
            other_edge = row[x+1:]
            if (0 < x < len(row) - 1) and (max(to_edge) < row[x] or max(other_edge) < row[x]):
                counted.append((y, x))

    return len(set(counted)) + (len(trees[0]) - 2) * 2 + len(trees) * 2

@aoc(2022, 8)
def part2(input): 
    
    trees = np.array([[int(t) for t in x] for x in input.splitlines()])
    flip = np.flipud(np.rot90(trees))

    scores = []

    for y, row in enumerate(trees):
        for x in range(0, len(row)):
            to_edge = row[:x]
            other_edge = row[x+1:]
            up_edge = flip[x][:y]
            down_edge = flip[x][y+1:]
            score = 0
        
            count = []
            for side in (to_edge[::-1], other_edge, up_edge[::-1], down_edge):
                side_temp = 0
                for t in side:
                    if t < row[x]:
                        side_temp += 1
                    else:
                        side_temp += 1
                        break
                count.append(side_temp)
            
            score = np.prod(np.array(count)[np.nonzero(count)])
            scores.append(score)

    return max(scores) 
