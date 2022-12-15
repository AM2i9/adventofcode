from aoc.helpers import aoc

from more_itertools import windowed

# https://adventofcode.com/2022/day/14


@aoc(2022, 14)
def part1(input):

    points = []

    for line in [
        (eval(f"({point})") for point in line.split(" -> "))
        for line in input.splitlines()
    ]:
        for a, b in windowed(line, 2):

            if a[0] != b[0]:
                for i in range(0, abs(a[0] - b[0]) + 1):
                    points.append(
                        (a[0] + (i * -((a[0] - b[0]) // abs(a[0] - b[0]))), a[1])
                    )
            elif a[1] != b[1]:
                for i in range(0, abs(a[1] - b[1]) + 1):
                    points.append(
                        (a[0], a[1] + (i * -((a[1] - b[1]) // abs(a[1] - b[1]))))
                    )

    points = list(set(points))
    points.sort(key=lambda x: -x[1])

    abyss = points[0][1]

    points.sort()

    # min_x = points[0][0]
    # max_x = points[-1][0]

    points = set(points)
    sands = set()

    while True:

        # for y in range(0, abyss + 1):
        #     for x in range(min_x, max_x):
        #         if (x, y) in points and (x, y) not in sands:
        #             print("#", end='')
        #         elif (x, y) in sands:
        #             print("O", end='')
        #         elif y == 0 and x == 500:
        #             print("+", end='')
        #         else:
        #             print(".", end='')
        #     print()

        y = 0
        x = 500

        while True:
            if (x, y + 1) in points:
                if (x - 1, y + 1) not in points:
                    x -= 1
                elif (x + 1, y + 1) not in points:
                    x += 1
                else:
                    points.add((x, y))
                    sands.add((x, y))
                    break
            elif y > abyss:
                return len(sands)
            else:
                y += 1


@aoc(2022, 14)
def part2(input):

    points = []

    for line in [
        (eval(f"({point})") for point in line.split(" -> "))
        for line in input.splitlines()
    ]:
        for a, b in windowed(line, 2):

            if a[0] != b[0]:
                for i in range(0, abs(a[0] - b[0]) + 1):
                    points.append(
                        (a[0] + (i * -((a[0] - b[0]) // abs(a[0] - b[0]))), a[1])
                    )
            elif a[1] != b[1]:
                for i in range(0, abs(a[1] - b[1]) + 1):
                    points.append(
                        (a[0], a[1] + (i * -((a[1] - b[1]) // abs(a[1] - b[1]))))
                    )

    points = list(set(points))
    points.sort(key=lambda x: -x[1])

    floor = points[0][1] + 2

    points.sort()

    # min_x = points[0][0]
    # max_x = points[-1][0]

    points = set(points)
    sands = set()

    while True:

        # for y in range(0, floor + 1):
        #     for x in range(min_x, max_x):
        #         if (x, y) in points and (x, y) not in sands:
        #             print("#", end='')
        #         elif (x, y) in sands:
        #             print("O", end='')
        #         elif y == 0 and x == 500:
        #             print("+", end='')
        #         else:
        #             print(".", end='')
        #     print()
        # print()

        y = 0
        x = 500

        while True:
            if y + 1 == floor:
                points.add((x, y))
                sands.add((x, y))
                break
            elif (x, y + 1) in points:
                if (x - 1, y + 1) not in points:
                    x -= 1
                elif (x + 1, y + 1) not in points:
                    x += 1
                else:
                    if x == 500 and y == 0:
                        return len(sands) + 1
                    points.add((x, y))
                    sands.add((x, y))
                    break
            else:
                y += 1
