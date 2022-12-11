from aoc.helpers import aoc

from pprint import pprint

# https://adventofcode.com/2022/day/11


@aoc(2022, 11)
def part1(input):
    
    monkeys = {}

    for raw_m in input.split("\n\n"):
        lines = raw_m.splitlines()
        monkeys[int(lines[0][7])] = {
            "items": [int(i) for i in lines[1].split(": ")[1].split(", ")],
            "operation": lines[2].split("new = ")[1],
            "div": int(lines[3].split("by ")[1]),
            True: int(lines[4].split("monkey ")[1]),
            False: int(lines[5].split("monkey ")[1]),
            "count": 0
        }
    
    for round in range(20):
        for _, monkey in monkeys.items():
            monkey["count"] += len(monkey["items"])
            for i in range(len(monkey["items"])):
                old = monkey["items"].pop(0)
                new = eval(monkey["operation"]) // 3
                monkeys[monkey[new % monkey["div"] == 0]]["items"].append(new)

    businesses = [monkey["count"] for _,monkey in monkeys.items()]
    businesses.sort()
    return businesses[-1] * businesses[-2]

@aoc(2022, 11)
def part2(input):
    
    monkeys = {}
    mod = 1

    for raw_m in input.split("\n\n"):
        lines = raw_m.splitlines()
        div = int(lines[3].split("by ")[1])
        monkeys[int(lines[0][7])] = {
            "items": [int(i) for i in lines[1].split(": ")[1].split(", ")],
            "operation": lines[2].split("new = ")[1],
            "div": div,
            True: int(lines[4].split("monkey ")[1]),
            False: int(lines[5].split("monkey ")[1]),
            "count": 0
        }
        mod *= div
    

    for round in range(10000):
        for _, monkey in monkeys.items():
            monkey["count"] += len(monkey["items"])
            for i in range(len(monkey["items"])):
                old = monkey["items"].pop(0)
                new = eval(monkey["operation"]) % mod
                monkeys[monkey[new % monkey["div"] == 0]]["items"].append(new)

    businesses = [monkey["count"] for _,monkey in monkeys.items()]
    businesses.sort()
    return businesses[-1] * businesses[-2]
