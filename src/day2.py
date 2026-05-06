def part1(input_file):
    checksum = 0

    with open(input_file, 'r') as f:
        for line in f:
            row = list(map(int, line.split()))

            min_elt = max_elt = row[0]
            for i in range(1, len(row)):
                if row[i] < min_elt:
                    min_elt = row[i]
                elif row[i] > max_elt:
                    max_elt = row[i]

            checksum += max_elt - min_elt

    return checksum
        

print(part1("input\\day2.txt"))