def part1(input_file):
    with open(input_file, 'r') as f:
        stream = f.readline().strip()

    total_score = 0
    current_score = 0

    i = 0
    is_garbage = is_cancelled = False

    while i < len(stream):
        if is_cancelled:
            is_cancelled = False
        elif stream[i] == '!':
            is_cancelled = True
        elif is_garbage:
            if stream[i] == '>':
                is_garbage = False
        else:
            if stream[i] == '{':
                current_score += 1
            elif stream[i] == '}':
                total_score += current_score
                current_score -= 1
            elif stream[i] == '<':
                is_garbage = True
        i += 1

    return total_score


def part2(input_file):
    with open(input_file, 'r') as f:
        stream = f.readline().strip()

    nb_garbage = 0
    i = 0
    is_garbage = is_cancelled = False
    while i < len(stream):
        if is_cancelled:
            is_cancelled = False
        elif stream[i] == '!':
            is_cancelled = True
        elif is_garbage:
            if stream[i] == '>':
                is_garbage = False
            else:
                nb_garbage += 1
        elif stream[i] == '<':
            is_garbage = True
        i += 1

    return nb_garbage


print(part1("input\\day9.txt"))
print(part2("input\\day9.txt"))