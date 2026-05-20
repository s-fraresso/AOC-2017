def find(parents, i):
    while parents[i] != i:
        i = parents[i]
    return i


def part1(input_file):
    with open(input_file, 'r') as f:
        instructions = f.readlines()
        parents = list(range(len(instructions)))
    
    for i, instr in enumerate(instructions): 
        for j in map(int, instr.strip().split('>')[1].split(',')):
            parents[find(parents, i)] = find(parents, j)

    return sum(find(parents, i) == find(parents, 0) for i in range(len(instructions)))


print(part1("input\\day12.txt"))