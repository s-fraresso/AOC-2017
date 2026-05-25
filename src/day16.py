NB_PROG = 16


def part1(input_file):
    with open(input_file, 'r') as f:
        dance_moves = f.readline().strip().split(',')
    
    programs = list(map(chr, range(ord("a"), ord("a") + NB_PROG)))
    start_index = 0

    for move in dance_moves:
        if move[0] == "s":
            offset = int(move[1:])
            start_index = (start_index - offset) % NB_PROG
        elif move[0] == "x":
            i, j = map(int, move[1:].split("/"))
            offset_i = (start_index + i) % NB_PROG
            offset_j = (start_index + j) % NB_PROG
            programs[offset_i], programs[offset_j] = programs[offset_j], programs[offset_i]
        else:
            p1, p2 = move[1:].split("/")
            i, j = int(programs.index(p1)), int(programs.index(p2))
            programs[i], programs[j] = programs[j], programs[i]
    
    return "".join(programs[start_index:] + programs[:start_index])


print(part1("input\\day16.txt"))