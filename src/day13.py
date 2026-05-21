def part1(input_file):
    severity = 0

    with open(input_file, 'r') as f:
        for line in f:
            layer, area = map(int, line.strip().split(":"))
            mod = area * 2 - 2

            if layer % mod == 0:
                severity += layer * area

    return severity


def part2(input_file):
    with open(input_file, 'r') as f:
        firewall = [tuple(map(int, line.strip().split(":"))) for line in f.readlines()]

    is_safe = False
    delay = -1
    while not is_safe:
        is_safe = True
        delay += 1
        for scanner in firewall:
            mod = scanner[1] * 2 - 2
            if (scanner[0] + delay) % mod == 0:
                is_safe = False
                break

    return delay


print(part1("input\\day13.txt"))
print(part2("input\\day13.txt"))