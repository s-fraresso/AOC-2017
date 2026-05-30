def part1(input_file):
    with open(input_file, 'r') as f:
        maze = [line[:-1] for line in f.readlines()]

    path = ""
    diri = 1
    dirj = 0
    i = 0
    j = maze[0].index('|')

    while maze[i][j] != ' ':
        if maze[i][j].isalpha():
            path += maze[i][j]
        elif maze[i][j] == '+':
            if diri == 0:
                if maze[i + 1][j] != ' ':
                    diri = 1
                else:
                    diri = -1
                dirj = 0
            else:
                if maze[i][j + 1] != ' ':
                    dirj = 1
                else:
                    dirj = -1
                diri = 0 
        
        i += diri
        j += dirj

    return path


print(part1("input\\day19.txt"))