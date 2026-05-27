def part1(nb_steps):
    buffer = [0]
    pos = 0

    for next_value in range(1, 2018):
        pos = (pos + nb_steps) % len(buffer)
        buffer.insert(pos + 1, next_value)
        pos += 1
    
    return buffer[(pos + 1) % len(buffer)]


def part2(nb_steps):
    value_after_zero = None
    pos = 0

    for next_value in range(1, 50_000_001):
        pos = (pos + nb_steps) % next_value

        if pos == 0:
            value_after_zero = next_value
            
        pos += 1
    
    return value_after_zero


print(part1(345))
print(part2(345))