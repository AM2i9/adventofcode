from aoc.helpers import aoc

from pprint import pprint

# https://adventofcode.com/2022/day/7

def calc_dir_size(dir, dirs):
    for item in dirs[dir]["contents"]:
        if item.startswith("dir"):
            dirs[dir]['total'] += calc_dir_size(f"{dir}-{item.split()[1]}", dirs)
    return dirs[dir]['total']

def parse_input(input):
    
    current_dir = "/"

    dirs = {}
    
    for line in input.splitlines():
        if line.startswith("$ cd "):
            if line.endswith(".."):
                current_dir = dirs[current_dir]["parent"]
            else:
                dirs[f"{current_dir}-{line.split()[2]}"] = {"total":0, "parent": current_dir, "contents":[]}
                current_dir = f"{current_dir}-{line.split()[2]}"

        elif not line.startswith("$ ls"):
            if line.startswith("dir"):
                dirs[current_dir]["contents"].append(line)
            
            elif line[0].isdigit():
                dirs[current_dir]["contents"].append(line)
                dirs[current_dir]["total"] += int(line.split()[0])
    
    calc_dir_size('/-/', dirs)
    return dirs

@aoc(2022, 7)
def part1(input):
    dirs = parse_input(input)
    
    total = 0

    for dir in dirs:
        if dirs[dir]["total"] <= 100000:
            total += dirs[dir]["total"]

    return total

@aoc(2022, 7)
def part2(input):
    dirs = parse_input(input)

    needed = 30000000 - (70000000 - dirs['/-/']['total'])
    current = dirs['/-/']['total']

    for dir in dirs:
        cur_total = dirs[dir]['total']
        if cur_total >= needed and cur_total < current:
            current = cur_total

    return current
    
