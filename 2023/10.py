# import matplotlib.pyplot as plt
from aoc.helpers import aoc

# https://adventofcode.com/2023/day/10


def find_next_pipe(current_x, current_y, offsets, rows):

    prev_x, prev_y = 0, 0

    for offset in offsets:
        pipe_x = current_x + offset[0]
        pipe_y = current_y + offset[1]

        pipe_char = rows[pipe_y][pipe_x]

        if any(
            (
                pipe_y > current_y and pipe_char in ("|", "J", "L"),
                pipe_y < current_y and pipe_char in ("|", "F", "7"),
                pipe_x < current_x and pipe_char in ("F", "L", "-"),
                pipe_x > current_x and pipe_char in ("7", "J", "-"),
                pipe_char == "S",
            )
        ):
            prev_x, prev_y = current_x, current_y
            current_x, current_y = pipe_x, pipe_y
            break

    return current_x, current_y, prev_x, prev_y


def find_loop(rows, start_x, start_y):
    prev_x, prev_y = 0, 0
    current_x, current_y = start_x, start_y

    offsets = ((-1, 0), (1, 0), (0, 1), (0, -1))
    # start direction finding
    current_x, current_y, prev_x, prev_y = find_next_pipe(
        current_x, current_y, offsets, rows
    )

    tile_coords = []

    while rows[current_y][current_x] != "S":

        check_offsets = []
        prev_offset = []

        char = rows[current_y][current_x]
        if char == "|":
            check_offsets = [(0, 1), (0, -1)]
        elif char == "F":
            check_offsets = [(1, 0), (0, 1)]
        elif char == "7":
            check_offsets = [(-1, 0), (0, 1)]
        elif char == "-":
            check_offsets = [(-1, 0), (1, 0)]
        elif char == "J":
            check_offsets = [(-1, 0), (0, -1)]
        elif char == "L":
            check_offsets = [(1, 0), (0, -1)]

        tile_coords.append((current_x, current_y))

        if (prev_offset := (prev_x - current_x, prev_y - current_y)) in check_offsets:
            check_offsets.remove(prev_offset)

        current_x, current_y, prev_x, prev_y = find_next_pipe(
            current_x, current_y, check_offsets, rows
        )

    return tile_coords


@aoc(2023, 10)
def part1(input: str):

    rows = input.strip().splitlines()
    row_length = len(rows[0])

    start_x, start_y = (start := input.index("S")) % (row_length + 1), start // (
        row_length + 1
    )

    tile_coords = find_loop(rows, start_x, start_y)

    step_count = len(tile_coords)

    return (step_count + 1) // 2


@aoc(2023, 10)
def part2(input: str):

    rows = input.strip().splitlines()
    row_length = len(rows[0])

    start_x, start_y = (start := input.index("S")) % (row_length + 1), start // (
        row_length + 1
    )

    tile_coords = find_loop(rows, start_x, start_y)

    step_count = len(tile_coords)

    # input = input.replace("F", "|")
    # input = input.replace("J", "|")
    # input = input.replace("L", "|")
    # input = input.replace("7", "|")

    # rows = input.strip().splitlines()

    scanned = ""

    inside_chars = []

    for y, row in enumerate(rows):
        inside = False
        for x, char in enumerate(row.strip()):

            if char in "FLJ7|" and ((x, y) in tile_coords):
                inside = not inside

                scanned += f"\033[{32 if inside else 31}m{char}\033[0m"

            elif inside and ((x, y) not in tile_coords):
                inside_chars.append((x, y))

                scanned += f"\033[36m{char}\033[0m"

            else:
                scanned += char
        scanned += "\n"
    print(scanned)

    # plt.scatter(start_x, start_y, color="RED")
    # plt.scatter(*zip(*tile_coords), color="BLUE")
    # plt.scatter(*zip(*inside_chars), color="GREEN")

    # plt.show()
