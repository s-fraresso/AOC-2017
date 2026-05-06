def part1(input_file):
    with open(input_file, 'r') as f:
        sequence = list(f.readline())
        sequence[-1] = sequence[0] # remplace \n pour rendre la suite circulaire
        sequence = list(map(int, sequence))

    total = 0
    for i in range(len(sequence) - 1):
        if sequence[i] == sequence[i + 1]:
            total += sequence[i]
    return total

print(part1("input\\day1.txt"))