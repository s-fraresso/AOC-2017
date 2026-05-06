def part1(input_file):
    with open(input_file, 'r') as f:
        maze = [int(line.strip()) for line in f.readlines()]
    
    nb_step = 0
    current_index = 0

    while 0 <= current_index < len(maze):
        step = maze[current_index]
        maze[current_index] += 1
        
        current_index += step
        nb_step += 1

    return nb_step


def part2(input_file):
    with open(input_file, 'r') as f:
        maze = [int(line.strip()) for line in f.readlines()]
    
    nb_step = 0
    current_index = 0

    while 0 <= current_index < len(maze):
        step = maze[current_index]
        if step >= 3:
            maze[current_index] -= 1
        else:
            maze[current_index] += 1
        
        current_index += step
        nb_step += 1

    return nb_step


print(part1("input\\day5.txt"))
print(part2("input\\day5.txt"))