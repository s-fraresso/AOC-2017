def part1(nb_steps):
    buffer = [0]
    pos = 0

    for next_value in range(1, 2018):
        pos = (pos + nb_steps) % len(buffer)
        buffer.insert(pos + 1, next_value)
        pos += 1
    
    return buffer[(pos + 1) % len(buffer)]


print(part1(345))