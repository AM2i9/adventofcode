from aoc.helpers import aoc

# https://adventofcode.com/2022/day/1

def get_totals(input):
    totals = []
    elves = input.split('\n\n')

    for elf in elves:
        calories = elf.split('\n')
        totals.append(sum([int(c) for c in calories if c.isdigit()]))
    
    return totals

@aoc(2022, 1)
def part1(input):
    totals = get_totals(input)
    return max(totals)

@aoc(2022, 1)
def part2(input):
    totals = get_totals(input)
    totals.sort(reverse=True)
    return sum(totals[:3])