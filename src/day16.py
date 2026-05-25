NB_PROG = 16


def dance_once(dance_moves, program_string):
    programs = list(program_string)
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


def part1(input_file):
    with open(input_file, 'r') as f:
        dance_moves = f.readline().strip().split(',')
    return dance_once(dance_moves, "".join(map(chr, range(ord("a"), ord("a") + NB_PROG))))


def part2(input_file):
    with open(input_file, 'r') as f:
        dance_moves = f.readline().strip().split(',')
    
    
    program_string = "".join(map(chr, range(ord("a"), ord("a") + NB_PROG)))
    seen_strings = list()

    while program_string not in seen_strings:
        seen_strings.append(program_string)
        program_string = dance_once(dance_moves, program_string)

    return seen_strings[1_000_000_000 % len(seen_strings)]


print(part1("input\\day16.txt"))
print(part2("input\\day16.txt"))