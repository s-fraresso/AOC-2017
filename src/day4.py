from collections import Counter


def part1(input_file):
    nb_valid_passphrases = 0

    with open(input_file, 'r') as f:
        for line in f:
            passphrase = line.strip()
            words = passphrase.split()

            if len(words) == len(set(words)):
                nb_valid_passphrases += 1

    return nb_valid_passphrases


def is_passphrase_valid(passphrase):
    words = passphrase.split()

    for i in range(len(words) - 1):
        for j in range(i + 1, len(words)):
            if Counter(words[i]) == Counter(words[j]):
                return False
        
    return True


def part2(input_file):
    nb_valid_passphrases = 0

    with open(input_file, 'r') as f:
        for line in f:
            passphrase = line.strip()

            if is_passphrase_valid(passphrase):
                nb_valid_passphrases += 1

    return nb_valid_passphrases


print(part1("input\\day4.txt"))
print(part2("input\\day4.txt"))