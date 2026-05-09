MOVEMENT = {'n' : (0, -1 ,1),
            'ne': (1, -1, 0),
            'se': (1, 0, -1),
            's' : (0, 1, -1),
            'sw': (-1, 1, 0),
            'nw': (-1, 0, 1)}


def part1(input_file):
    with open(input_file, 'r') as f:
        directions = f.readline().strip().split(',')

    q = r = s = 0
    for dir in directions:
        move = MOVEMENT[dir]
        q += move[0]
        r += move[1]
        s += move[2]

    return max(abs(q), abs(r), abs(s))


print(part1("input\\day11.txt"))