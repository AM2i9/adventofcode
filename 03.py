from aoc.helpers import aoc
import string

# https://adventofcode.com/2022/day/3

@aoc(2022, 3)
def part2(input):

    pri_sum = 0
    sacks = input.splitlines()
    for i in range(0, len(sacks), 3):
        group = [set(s) for s in sacks[i:i+3]]

        pri_sum += string.ascii_letters.index(list(group[0] & group[1] & group[2])[0]) + 1 
    
    print("part 2:", pri_sum)

@aoc(2022, 3)
def part1(input):

    pri_sum = 0

    for sack in input.splitlines():
        compart_1 = sack[:len(sack)//2]
        compart_2 = sack[len(sack)//2:]
        
        pri_sum += string.ascii_letters.index(list(set(compart_1) & set(compart_2))[0]) + 1
    
    print("part 1:",pri_sum)