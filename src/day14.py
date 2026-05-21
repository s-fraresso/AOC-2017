def tie_knot(circle, lengths, pos, skip):
    N = len(circle)

    for length in lengths:
        for i in range(length // 2):
            circle[(pos + i) % N], circle[(pos + length - 1 - i) % N] = circle[(pos + length - 1 - i) % N], circle[(pos + i) % N]
        
        pos = (pos + length + skip) % N
        skip = (skip + 1) % N

    return pos, skip


def knot_hash(keystring):
    lengths = list(map(ord, keystring)) + [17, 31, 73, 47, 23]
    circle = list(range(256))
    pos = skip = 0
    for _ in range(64):
        pos, skip = tie_knot(circle, lengths, pos, skip)

    hsh = ""
    for i in range(16):
        cur_dense = circle[16 * i]
        for j in range(1, 16):
            cur_dense ^= circle[16 * i + j]
        
        hsh += hex(cur_dense)[2:].zfill(2)

    return hsh


def part1(keystring):
    nb_used = 0

    for row in range(128):
        hsh = knot_hash(keystring + "-" + str(row))
        nb_used += int(hsh, 16).bit_count()

    return nb_used


print(part1("stpzcrnm"))