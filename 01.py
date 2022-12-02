from aoc.helpers import aoc

# https://adventofcode.com/2022/day/1

@aoc(2022, 1)
def main(input):
    totals = []
    elves = input.split('\n\n')

    for elf in elves:
        calories = elf.split('\n')
        totals.append(sum([int(c) for c in calories if c.isdigit()]))

    print(max(totals))

    totals.sort(reverse=True)
    print(sum(totals[:3]))