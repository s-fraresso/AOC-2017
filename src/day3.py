from math import sqrt, ceil
from collections import defaultdict


def part1(puzzle_input):
    side_length = ceil(sqrt(puzzle_input))
    if side_length % 2 == 0:
        side_length += 1

    i = j = side_length // 2
    square = side_length**2
    
    for di, dj in ((0, -1), (-1, 0), (0, 1), (1, 0)):
        for _ in range(side_length - 1):
            if square == puzzle_input:
                return abs(i) + abs(j)
            
            i += di
            j += dj
            square -= 1
    
    return -1


def sum_neighbours(i, j, grid):
    total = 0

    for i2 in (i - 1, i, i + 1):
        for j2 in (j - 1, j, j + 1):
            total += grid[(i2, j2)]

    return total


def part2(puzzle_input):
    i, j = 1, 1
    grid = defaultdict(int)
    grid[(0, 0)] = 1
    side_length = 3

    while True:
        for di, dj in ((-1, 0), (0, -1), (1, 0), (0, 1)):
            for _ in range(side_length - 1):
                i += di
                j += dj

                grid[(i, j)] = sum_neighbours(i, j, grid)

                if grid[(i, j)] > puzzle_input:
                    return grid[(i, j)]

        side_length += 2
        i += 1
        j += 1


print(part1(265149))
print(part2(265149))