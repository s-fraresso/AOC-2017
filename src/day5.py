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


print(part1("input\\day5.txt"))