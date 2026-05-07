SIZE = 256


def part1(input_file):
    with open(input_file, 'r') as f:
        lengths = list(map(int, f.readline().strip().split(",")))

    circle = list(range(SIZE))
    pos = 0
    skip = 0

    for length in lengths:
        for i in range(length // 2):
            circle[(pos + i) % SIZE], circle[(pos + length - 1 - i) % SIZE] = circle[(pos + length - 1 - i) % SIZE], circle[(pos + i) % SIZE]
        
        pos += length + skip
        skip += 1

    return circle[0] * circle[1]


print(part1("input\\day10.txt"))
