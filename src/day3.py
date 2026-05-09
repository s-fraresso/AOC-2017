from math import sqrt, ceil


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


print(part1(265149))
