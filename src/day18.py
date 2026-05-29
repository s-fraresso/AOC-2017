def string_to_instruction(line):
    instruction = {"type": line[:3]}

    if instruction["type"] in ("rcv", "snd"):
        instruction["reg"] = line.split(" ")[1]
    elif instruction["type"] == "jgz":
        fst, snd = line.split(" ")[1:]
        instruction |= {"reg1":None, "immediate1":None, "reg2":None, "immediate2":None}
        if fst.isalpha():
            instruction["reg1"] = fst
        else:
            instruction["immediate1"] = int(fst)
        if snd.isalpha():
            instruction["reg2"] = snd
        else:
            instruction["immediate2"] = int(snd)
    else:
        instruction["reg1"], second_parameter = line.split(" ")[1:]
        if second_parameter.isalpha():
            instruction["reg2"] = second_parameter
            instruction["immediate"] = None
        else:
            instruction["reg2"] = None
            instruction["immediate"] = int(second_parameter)

    return instruction


def part1(input_file):
    with open(input_file, 'r') as f:
        instructions = [string_to_instruction(line.strip()) for line in f.readlines()]

    registers = {'a':0, 'b':0, 'f':0, 'i':0, 'p':0}
    last_frequency = None
    program_clock = 0

    while 0 <= program_clock < len(instructions):
        instr = instructions[program_clock]

        if instr["type"] == 'jgz':
            test_val = registers[instr["reg1"]] if instr["reg1"] is not None else instr["immedaite1"]
            if test_val > 0:
                if instr["reg2"] is not None:
                    program_clock += registers[instr["reg2"]]
                else:
                    program_clock += instr["immediate2"]
            else:
                program_clock += 1
        else:
            if instr["type"] == "snd":
                last_frequency = registers[instr["reg"]]
            elif instr["type"] == "set":
                if instr["reg2"] is not None:
                    registers[instr["reg1"]] = registers[instr["reg2"]]
                else:
                    registers[instr["reg1"]] = instr["immediate"]
            elif instr["type"] == 'add':
                if instr["reg2"] is not None:
                    registers[instr["reg1"]] += registers[instr["reg2"]]
                else:
                    registers[instr["reg1"]] += instr["immediate"]
            elif instr["type"] == 'mul':
                if instr["reg2"] is not None:
                    registers[instr["reg1"]] *= registers[instr["reg2"]]
                else:
                    registers[instr["reg1"]] *= instr["immediate"]
            elif instr["type"] == 'mod':
                if instr["reg2"] is not None:
                    registers[instr["reg1"]] %= registers[instr["reg2"]]
                else:
                    registers[instr["reg1"]] %= instr["immediate"]
            elif instr["type"] == "rcv":
                if registers[instr["reg"]] != 0:
                    return last_frequency
                
            program_clock += 1

    
    return last_frequency


print(part1("input\\day18.txt"))