def part1(seed_A, seed_B):
    nb_matches = 0
    A_value, B_value = seed_A, seed_B

    for _ in range(40_000_000):
        A_value = (A_value * 16807) % 2147483647
        B_value = (B_value * 48271) % 2147483647

        if A_value % 2**16 == B_value % 2**16:
            nb_matches += 1

    return nb_matches


def part2(seed_A, seed_B):
    nb_matches = 0
    A_value, B_value = seed_A, seed_B

    for _ in range(5_000_000):
        A_value = (A_value * 16807) % 2147483647
        while A_value % 4 != 0:
            A_value = (A_value * 16807) % 2147483647
        
        B_value = (B_value * 48271) % 2147483647
        while B_value % 8 != 0:
            B_value = (B_value * 48271) % 2147483647
        
        if A_value % 2**16 == B_value % 2**16:
            nb_matches += 1
    
    return nb_matches
        


print(part1(783, 325))
print(part2(783, 325))