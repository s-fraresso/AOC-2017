def select_bank(banks):
    max_index = 0
    max_value = banks[0]

    for i in range(1, len(banks)):
        if banks[i] > max_value:
            max_index = i
            max_value = banks[i]

    return max_index


def part1(input_file):
    seen_configurations = set()

    with open(input_file, 'r') as f:
        banks = list(map(int, f.readline().split()))
        
    configuration = tuple(banks)
    while configuration not in seen_configurations:
        seen_configurations.add(configuration)

        selected_bank = select_bank(banks)
        nb_blocks = banks[selected_bank]
        banks[selected_bank] = 0

        i = (selected_bank + 1) % len(banks)
        while nb_blocks > 0:
            banks[i] += 1
            i = (i + 1) % len(banks)
            nb_blocks -= 1

        configuration = tuple(banks)

    return len(seen_configurations)
        


print(part1("input\\day6.txt"))