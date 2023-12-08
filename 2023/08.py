import math
from aoc.helpers import aoc

# https://adventofcode.com/2023/day/8


@aoc(2023, 8)
def part1(input: str):

    directions, raw_nodes = input.strip().split("\n\n")

    nodes = {}

    for node in raw_nodes.split("\n"):
        src, dest = node.split(" = ")
        nodes[src] = (dest[1:4], dest[6:9])

    current = "AAA"
    steps = 0
    direction_i = 0

    while current != "ZZZ":

        if directions[direction_i] == "R":
            current = nodes[current][1]
        elif directions[direction_i] == "L":
            current = nodes[current][0]

        steps += 1
        direction_i += 1
        if direction_i >= len(directions):
            direction_i = 0

    return steps


@aoc(2023, 8)
def part2(input: str):

    directions, raw_nodes = input.strip().split("\n\n")

    nodes = {}

    for node in raw_nodes.split("\n"):
        src, dest = node.split(" = ")
        nodes[src] = (dest[1:4], dest[6:9])

    starting_points = [c for c in nodes.keys() if c[-1] == "A"]

    step_counts = []

    for point in starting_points:
        current = point
        steps = 0
        direction_i = 0

        while current[-1] != "Z":

            if directions[direction_i] == "R":
                current = nodes[current][1]
            elif directions[direction_i] == "L":
                current = nodes[current][0]

            steps += 1
            direction_i += 1
            if direction_i >= len(directions):
                direction_i = 0

        step_counts.append(steps)

    return math.lcm(*step_counts)
