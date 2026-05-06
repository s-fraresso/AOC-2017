def part1(input_file):
    all_programs = set()
    sub_programs = set()

    with open(input_file, 'r') as f:
        for line in f:
            all_programs.add(line.split(" ")[0])
            if '->' in line:
                sub_programs.update(line.strip().split(" -> ")[1].split(", "))
                
            
    return all_programs.difference(sub_programs).pop()


print(part1("input\\day7.txt"))