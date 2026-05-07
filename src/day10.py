def tie_knot(circle, lengths, pos, skip):
    N = len(circle)

    for length in lengths:
        for i in range(length // 2):
            circle[(pos + i) % N], circle[(pos + length - 1 - i) % N] = circle[(pos + length - 1 - i) % N], circle[(pos + i) % N]
        
        pos = (pos + length + skip) % N
        skip = (skip + 1) % N

    return pos, skip


def part1(input_file):
    with open(input_file, 'r') as f:
        lengths = list(map(int, f.readline().strip().split(",")))

    circle = list(range(256))
    tie_knot(circle, lengths, 0, 0)

    return circle[0] * circle[1]


def part2(input_file):
    with open(input_file, 'r') as f:
        lengths = list(map(ord, f.readline().strip())) + [17, 31, 73, 47, 23]

    circle = list(range(256))
    pos = skip = 0
    for _ in range(64):
        pos, skip = tie_knot(circle, lengths, pos, skip)

    knot_hash = ""
    for i in range(16):
        cur_dense = circle[16 * i]
        for j in range(1, 16):
            cur_dense ^= circle[16 * i + j]
        
        knot_hash += hex(cur_dense)[2:].zfill(2)

    return knot_hash


print(part1("input\\day10.txt"))
print(part2("input\\day10.txt"))
