from aoc.helpers import aoc

import re

# https://adventofcode.com/2021/day/2

@aoc(2021, 2)
def part1(input):
    dirs = {
        "forward": 0,
        "up": 0,
        "down": 0
    }

    for dir in dirs:
        s = sum([int(m) for m in re.findall(f"{dir} (\d)", input)])
        dirs[dir] = s
    
    return (dirs["forward"]) * (dirs["down"] - dirs["up"])


@aoc(2021, 2)
def part2(input):

    aim = 0
    pos = 0
    depth = 0
    
    for d, m in [(d, int(m)) for d,m in re.findall(f"(.*) (\d)", input)]:
        match d:
            case "down":
                aim += m
            case "up":
                aim -= m
            case "forward":
                pos += m
                depth += aim * m

    return pos * depth

    