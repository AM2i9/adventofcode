from aoc.helpers import aoc

# https://adventofcode.com/2023/day/2


@aoc(2023, 2)
def part1(input: str):

    games = input.strip().splitlines()

    sum = 0

    for game in games:
        head, sets = game.split(":")
        id = int(head.split(" ")[-1])

        for thing in sets.split(";"):
            stuff = {
                phrase.split(" ")[1]: int(phrase.split(" ")[0])
                for phrase in thing.strip().split(", ")
            }

            if (
                stuff.get("red", 0) > 12
                or stuff.get("green", 0) > 13
                or stuff.get("blue", 0) > 14
            ):
                break
        else:  # never did I ever
            sum += id

    return sum


@aoc(2023, 2)
def part2(input: str):

    games = input.strip().splitlines()

    sum = 0

    for game in games:
        head, sets = game.split(":")
        id = int(head.split(" ")[-1])

        red = 0
        blue = 0
        green = 0

        for thing in sets.split(";"):
            stuff = {
                phrase.split(" ")[1]: int(phrase.split(" ")[0])
                for phrase in thing.strip().split(", ")
            }

            if stuff.get("red") is not None and stuff.get("red") > red:
                red = stuff["red"]
            if stuff.get("green") is not None and stuff.get("green") > green:
                green = stuff["green"]
            if stuff.get("blue") is not None and stuff.get("blue") > blue:
                blue = stuff["blue"]

        sum += red * blue * green

    return sum
