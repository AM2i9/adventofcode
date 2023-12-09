from aoc.helpers import aoc

# https://adventofcode.com/2023/day/9


@aoc(2023, 9)
def part1(input: str):

    histories = [
        [int(n.strip()) for n in line.split(" ")] for line in input.strip().splitlines()
    ]

    ans = 0

    def derive(arr):
        return [arr[i] - arr[i - 1] for i in range(1, len(arr))]

    for history in histories:
        ds = [history]

        current = history
        while not all(n == 0 for n in current):
            current = derive(current)
            ds.append(current)

        ds.reverse()

        prediction = ds[1][-1]

        for i in range(2, len(ds)):
            prediction = ds[i][-1] + prediction

        ans += prediction

    return ans


@aoc(2023, 9)
def part2(input: str):

    histories = [
        [int(n.strip()) for n in line.split(" ")] for line in input.strip().splitlines()
    ]

    ans = 0

    def derive(arr):
        return [arr[i] - arr[i - 1] for i in range(1, len(arr))]

    for history in histories:
        ds = [history]

        current = history
        while not all(n == 0 for n in current):
            current = derive(current)
            ds.append(current)

        ds.reverse()

        prediction = ds[1][0]

        for i in range(2, len(ds)):
            prediction = (
                ds[i][0] - prediction
            )  # man it's literally just like two things here that I change
            # I could figure out how to make this slightly more abstract...
            # but that sounds like work that I technically don't have to do
        ans += prediction

    return ans
