def part1(input_file):
    nb_valid_passphrases = 0

    with open(input_file, 'r') as f:
        for line in f:
            passphrase = line.strip()
            words = passphrase.split()

            if len(words) == len(set(words)):
                nb_valid_passphrases += 1

    return nb_valid_passphrases


print(part1("input\\day4.txt"))