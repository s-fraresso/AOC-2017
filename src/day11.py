MOVEMENT = {'n' : (0, -1 ,1),
            'ne': (1, -1, 0),
            'se': (1, 0, -1),
            's' : (0, 1, -1),
            'sw': (-1, 1, 0),
            'nw': (-1, 0, 1)}


def steps_from_origin(q, r, s):
    return max(abs(q), abs(r), abs(s))


def part1(input_file):
    with open(input_file, 'r') as f:
        directions = f.readline().strip().split(',')

    q = r = s = 0
    for dir in directions:
        move = MOVEMENT[dir]
        q += move[0]
        r += move[1]
        s += move[2]

    return steps_from_origin(q, r, s)


def part2(input_file):
    with open(input_file, 'r') as f:
        directions = f.readline().strip().split(',')

    max_steps = 0
    q = r = s = 0
    for dir in directions:
        move = MOVEMENT[dir]
        q += move[0]
        r += move[1]
        s += move[2]

        max_steps = max(max_steps, steps_from_origin(q, r, s))

    return max_steps


print(part1("input\\day11.txt"))
print(part2("input\\day11.txt"))