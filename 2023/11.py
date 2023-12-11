from pprint import pprint
from aoc.helpers import aoc

# https://adventofcode.com/2023/day/11


def expand(input):

    rows = input.strip().splitlines()

    rows = [list(row) for row in rows]

    i = 0
    while i < len(rows):
        if "#" in rows[i]:
            i += 1
        else:
            rows.insert(i, list("." * len(rows[i])))
            i += 2

    c = 0
    while c < len(rows[0]):
        if all(row[c] == "." for row in rows):
            for row in rows:
                row.insert(c, ".")
            c += 2
        else:
            c += 1

    return rows


@aoc(2023, 11)
def part1(input: str):

    image = expand(input)

    galaxies = []

    for y, row in enumerate(image):
        for x, space in enumerate(row):
            if space == "#":
                galaxies.append((x, y))

    print(galaxies)
    distances = []

    for i, galaxy in enumerate(galaxies):
        g = 0
        while g < len(galaxies):
            if g <= i:
                distances.append(
                    abs(galaxy[0] - galaxies[g][0]) + abs(galaxy[1] - galaxies[g][1])
                )

            g += 1

    return sum(distances)


@aoc(2023, 11)
def part2(input: str):

    rows = input.strip().splitlines()

    image = [list(row) for row in rows]

    galaxies = []
    offset_x = 0
    offset_y = 0

    for y, row in enumerate(image):
        offset_x = 0
        if "#" not in row:
            offset_y += 1000000 - 1
            continue
        for x, space in enumerate(row):
            if space == "#":
                galaxies.append((x + offset_x, y + offset_y))
            if all(row[x] == "." for row in image):
                offset_x += 1000000 - 1

    distances = []

    for i, galaxy in enumerate(galaxies):
        g = 0
        while g < len(galaxies):
            if g <= i:
                distances.append(
                    abs(galaxy[0] - galaxies[g][0]) + abs(galaxy[1] - galaxies[g][1])
                )

            g += 1

    return sum(distances)
