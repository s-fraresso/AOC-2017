from collections import defaultdict


def part1(input_file):
    registers = defaultdict(int)

    with open(input_file, "r") as f:
        for line in f:
            instruction, condition = line.strip().split(" if ")
            modified_reg, action, added_value = instruction.split(" ")
            checked_reg, check = condition.split(" ", maxsplit=1)
 
            if eval("registers[\"" + checked_reg + "\"] " + check):
                sign = 1 if action == "inc" else -1
                registers[modified_reg] += sign * int(added_value)
    
    return max(registers.values())


print(part1("input\\day8.txt"))