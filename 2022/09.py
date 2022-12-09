import re
import math

from aoc.helpers import aoc

# https://adventofcode.com/2022/day/9


@aoc(2022, 9)
def part1(input):

    head_x = 0
    head_y = 0

    tail_x = 0
    tail_y = 0

    points = set()

    for line in input.splitlines():
        for _ in range(0, abs(int(line.split()[1]))):
            match line.split():
                case ["R", v]:
                    head_x += 1
                case ["L", v]:
                    head_x -= 1
                case ["U", v]:
                    head_y += 1
                case ["D", v]:
                    head_y -= 1

            # Did this stuff because I originally was going to just have
            # the head move by the value instantly instead of incrementing
            # by 1 repeatedly, but found incrementing easier because
            # I could get all the tail's points easier.
            d = math.sqrt(((head_x - tail_x) ** 2) + ((head_y - tail_y) ** 2))
            if int(d) > 1:
                prev_tail_x = tail_x
                prev_tail_y = tail_y
                dx = head_x - tail_x
                dy = head_y - tail_y
                if abs(dx) > abs(dy):
                    if dx > 0:
                        tail_x += dx - 1
                    else:
                        tail_x += dx + 1
                    tail_y += dy
                else:
                    if dy > 0:
                        tail_y += dy - 1
                    else:
                        tail_y += dy + 1
                    tail_x += dx

            points.add((tail_x, tail_y))

    return len(points)


@aoc(2022, 9)
def part2(input):

    knots = [{"x": 0, "y": 0} for _ in range(10)]

    points = set()

    for line in input.splitlines():
        for _ in range(0, abs(int(line.split()[1]))):
            match line.split():
                case ["R", v]:
                    knots[0]["x"] += 1
                case ["L", v]:
                    knots[0]["x"] -= 1
                case ["U", v]:
                    knots[0]["y"] += 1
                case ["D", v]:
                    knots[0]["y"] -= 1

            for k, knot in enumerate(knots[1:], start=1):
                # Did this stuff because I originally was going to just have
                # the head move by the value instantly instead of incrementing
                # by 1 repeatedly, but found incrementing easier because
                # I could get all the tail's points easier.

                dx = knots[k - 1]["x"] - knot["x"]
                dy = knots[k - 1]["y"] - knot["y"]
                d = math.sqrt((dx**2) + (dy**2))

                if int(d) > 1:

                    if abs(dx) > abs(dy):
                        if dx > 0:
                            knot["x"] += dx - 1
                        else:
                            knot["x"] += dx + 1
                        knot["y"] += dy
                    elif abs(dx) == abs(dy):
                        if dx > 0:
                            knot["x"] += dx - 1
                        else:
                            knot["x"] += dx + 1
                            # could have been done better :( some math would have helped
                        if dy > 0:
                            knot["y"] += dy - 1
                        else:
                            knot["y"] += dy + 1
                    else:
                        if dy > 0:
                            knot["y"] += dy - 1
                        else:
                            knot["y"] += dy + 1
                        knot["x"] += dx

            points.add((knots[9]["x"], knots[9]["y"]))

    # for y in range(15, -6, -1):
    #     for x in range(-11, 15):

    #         if (x, y) in points:
    #             print("#", end="")
    #         elif (x, y) == (0, 0):
    #             print("s", end="")
    #         else:
    #             print(".", end="")
    #     print()
    # print()

    return len(points)
