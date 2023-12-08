from itertools import islice
from aoc.helpers import aoc

# https://adventofcode.com/2023/day/5


@aoc(2023, 5)
def part1(input: str):
    raw_maps = input.strip().split("\n\n")

    seeds = [int(seed) for seed in raw_maps[0][7:].split(" ")]

    maps = []

    for map in raw_maps:
        mappings = {}
        for line in map.split("\n")[1:]:
            dest, src, length = line.strip().split(" ")

            mappings.update({range(int(src), int(src) + int(length)): int(dest)})
        maps.append(mappings)

    seed_out = []

    for i, seed in enumerate(seeds):
        for map in maps:
            for rng in map:
                if seed in rng:
                    seed = map[rng] + (seed - rng[0])
                    break
        seed_out.append(seed)

    return min(seed_out)


class SeedRange:
    def __init__(self, start, length):
        self.start = start
        self.length = length
        self.end = start + length - 1

    @classmethod
    def from_end(cls, start, end):
        return SeedRange(start, end - start + 1)

    def __repr__(self):
        return f"SeedRange<start={self.start} end={self.end} length={self.length}>"

    def __and__(self, other):
        int_start = max(self.start, other.start)
        int_end = min(self.end, other.end)

        if int_end <= int_start:
            return None

        return SeedRange.from_end(int_start, int_end)


def remove_from_ranges(r1, rsub: list[range]) -> list[range]:

    return [
        range(r1[0], rsub[0][0] + 1),
        range(rsub[0][-1], r1[-1] + 1),
        *remove_from_ranges,
    ]


# I don't have 3.12 installed so unfortunately here we are
# copied from the Python docs
def batched(iterable, n):
    # batched('ABCDEFG', 3) --> ABC DEF G
    if n < 1:
        raise ValueError("n must be at least one")
    it = iter(iterable)
    while batch := tuple(islice(it, n)):
        yield batch


@aoc(2023, 5)
def part2(input: str):

    input = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
"""

    raw_maps = input.strip().split("\n\n")

    seeds = [
        SeedRange(int(s), int(l)) for s, l in batched(raw_maps[0][7:].split(" "), 2)
    ]
    print(seeds)
    maps = []

    for map in raw_maps:
        mappings = {}
        for line in map.split("\n")[1:]:
            dest, src, length = line.strip().split(" ")

            mappings.update({SeedRange(int(src), int(length)): int(dest)})
        maps.append(mappings)

    for i, seed in enumerate(seeds):
        map = maps[1]
        print("SEED:", seed)

        overlaps = []

        for rng in map:
            overlap = seed & rng

            if overlap:
                overlaps.append(overlap)
                print("OVERLAP:", overlap)
