def part1(input_file):
    severity = 0
    
    with open(input_file, 'r') as f:
        for line in f:
            layer, area = map(int, line.strip().split(":"))
            mod = area * 2 - 2

            if layer % mod == 0:
                severity += layer * area

    return severity



print(part1("input\\day13.txt"))