import re
from typing import List
from aoc.helpers import aoc

# https://adventofcode.com/2023/day/1


@aoc(2023, 1)
def part1(input:str ):
    
    lines= input.strip().split('\n')
    sum = 0
    for line in lines:
        nums = [int(c) for c in line if c.isdigit()]
        sum += (nums[0] * 10) + nums[-1]
    
    return sum


@aoc(2023, 1)
def part2(input: str):
    
    # i really didn't want to do regex but here I am
    # probably could have done something shorter and easier and more efficient
    # but I myself and not at all a regex wizzard

    sum = 0

    pattern = "^.*?(\d|(?:one|two|three|four|five|six|seven|eight|nine))(?:.*(\d|(?:one|two|three|four|five|six|seven|eight|nine)))?.*?$"
    numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    for line in input.strip().split('\n'):
        match = re.match(pattern, line)
        num_1 = match.group(1)
        num_2 = match.group(2) or num_1

        sum += (
            (numbers.index(num_1) + 1 if not num_1.isdigit() else int(num_1)) * 10
            + (numbers.index(num_2) + 1 if not num_2.isdigit() else int(num_2))
        )
    
    return sum
