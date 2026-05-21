def tie_knot(circle, lengths, pos, skip):
    N = len(circle)

    for length in lengths:
        for i in range(length // 2):
            circle[(pos + i) % N], circle[(pos + length - 1 - i) % N] = circle[(pos + length - 1 - i) % N], circle[(pos + i) % N]
        
        pos = (pos + length + skip) % N
        skip = (skip + 1) % N

    return pos, skip


def knot_hash(keystring):
    lengths = list(map(ord, keystring)) + [17, 31, 73, 47, 23]
    circle = list(range(256))
    pos = skip = 0
    for _ in range(64):
        pos, skip = tie_knot(circle, lengths, pos, skip)

    hsh = ""
    for i in range(16):
        cur_dense = circle[16 * i]
        for j in range(1, 16):
            cur_dense ^= circle[16 * i + j]
        
        hsh += hex(cur_dense)[2:].zfill(2)

    return hsh


def part1(keystring):
    nb_used = 0

    for row in range(128):
        hsh = knot_hash(keystring + "-" + str(row))
        nb_used += int(hsh, 16).bit_count()

    return nb_used


def find_root_label(equivalence_dict, label):
    while equivalence_dict[label] != label:
        label = equivalence_dict[label]
    return label


def count_regions(grid):
    current_label = 1
    label_grid = [[0]*129 for _ in range(129)] # ligne/colonne en plus sur coin supérieur gauche pour éviter débordements d'indice
    equivalence_dict = dict()

    for i in range(1, 129):
        for j in range(1, 129):
            if grid[i - 1][j - 1] == 0:
                continue

            up = label_grid[i - 1][j]
            left = label_grid[i][j - 1]

            if up == left == 0:
                label_grid[i][j] = current_label
                equivalence_dict[current_label] = current_label
                current_label += 1
            elif up == 0 or left == 0:
                label_grid[i][j] = max(up, left)
            else:
                label_grid[i][j] = up
                root_up, root_left = find_root_label(equivalence_dict, up), find_root_label(equivalence_dict, left)
                equivalence_dict[max(root_up, root_left)] = min(root_up, root_left)
    
    final_labels = set()
    for label in range(1, current_label):
        final_labels.add(find_root_label(equivalence_dict, label))
    
    return len(final_labels)


def part2(keystring):
    grid = []
    for row in range(128):
        hsh = knot_hash(keystring + "-" + str(row))
        grid.append(list(map(int, list(bin(int(hsh, 16))[2:].zfill(128)))))

    return count_regions(grid)


print(part1("stpzcrnm"))
print(part2("stpzcrnm"))