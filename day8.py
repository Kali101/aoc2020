import re

input = open("day8input.txt", "r").read().splitlines()
input_test = open("day8input_test.txt", "r").read().splitlines()

instruction_regex = r'(\w{3}) (\+|-)(\d*)'

def run_program(data):
    acc = 0
    stack = []
    i = 0
    while i not in stack:
        stack.append(i)
        if i >= len(data):
            return (True, i, acc)
        instruction = re.search(instruction_regex, data[i])
        if instruction.group(1) == "acc":
            if(instruction.group(2) == "+"):
                acc += int(instruction.group(3))
            else:
                acc -= int(instruction.group(3))
            i += 1
        elif instruction.group(1) == "jmp":
            if(instruction.group(2) == "+"):
                i += int(instruction.group(3))
            else:
                i -= int(instruction.group(3))
        else:
            i += 1
    return (len(stack) == len(data), i, acc)

def fix_program(data):
    for i in range(len(data)):
        if data[i].startswith("jmp"):
            data[i] = data[i].replace("jmp", "nop")
            if run_program(data)[0]:
                return data
            else:
                data[i] = data[i].replace("nop", "jmp")
        elif data[i].startswith("nop"):
            data[i] = data[i].replace("nop", "jmp")
            if run_program(data)[0]:
                return data
            else:
                data[i] = data[i].replace("jmp", "nop")

print(run_program(fix_program(input)))
