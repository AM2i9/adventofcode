from aoc.helpers import aoc

from string import ascii_letters
from pprint import pprint
from collections import deque

import numpy as np


# https://adventofcode.com/2022/day/12


def get_neighbors(grid, x, y):
    row, col = range(len(grid)), range(len(grid[0]))
    offsets = [(-1,0), (1,0), (0,-1), (0,1)]
    for dx, dy in offsets:
        nx = x + dx
        ny = y + dy
        if nx in row and ny in col:
            if grid[x, y] - grid[nx, ny] >= -1:
                yield (nx, ny)


@aoc(2022, 12)
def part1(input):

    grid = np.array([[ascii_letters.index(l) for l in line] for line in input.splitlines()])
    res = np.where(grid == ascii_letters.index("S"))
    S = list(zip(res[0], res[1]))[0]
    grid[*S] = 0
    res = np.where(grid == ascii_letters.index("E"))
    E = list(zip(res[0], res[1]))[0]
    grid[*E] = 25
    
    d = deque()
    d.append((S, 0))

    visited = set()

    while d:
        cur, depth = d.popleft()
        
        for nx, ny in get_neighbors(grid, *cur):

            if cur in visited:
                continue

            if (nx, ny) == E:
                d.clear()
                break
            else:
                if (nx, ny) not in visited:
                    d.append(((nx, ny), depth + 1))

        visited.add(cur)

    return depth + 1


@aoc(2022, 12)
def part2(input):

    grid = np.array([[ascii_letters.index(l) for l in line] for line in input.splitlines()])
    res = np.where(grid == ascii_letters.index("S"))
    S = list(zip(res[0], res[1]))[0]
    grid[*S] = 0
    res = np.where(grid == ascii_letters.index("E"))
    E = list(zip(res[0], res[1]))[0]
    grid[*E] = 25
    
    dists = []

    # I opted for the super slow method because I'm tired
    # would not recommend

    a = np.where(grid==0)

    for v in list(zip(a[0], a[1])):
        d = deque()
        d.append((v, 0))

        visited = set()

        while d:
            cur, depth = d.popleft()
            
            for nx, ny in get_neighbors(grid, *cur):

                if cur in visited:
                    continue

                if (nx, ny) == E:
                    d.clear()
                    dists.append(depth + 1)
                    break
                else:
                    if (nx, ny) not in visited:
                        d.append(((nx, ny), depth + 1))

            visited.add(cur)
        
    return min(dists)
