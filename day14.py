import re
from functools import reduce

input = open("day14input.txt", "r").read().splitlines()

maskRgx = re.compile("mask = ([X|1|0]{36})")
memRgx = re.compile("mem\[(.*)\] = (\d+)")

input_test_v1 = ["mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X",
"mem[8] = 11",
"mem[7] = 101",
"mem[8] = 0"]

input_test_v2 = ["mask = 000000000000000000000000000000X1001X",
"mem[42] = 100",
"mask = 00000000000000000000000000000000X0XX",
"mem[26] = 1"]

def to_bitstring(num):
    bitstring = ""
    for i in range(36):
        bit = pow(2, 36-(i+1))
        if(num >= bit):
            bitstring += "1"
            num -= bit
        else:
            bitstring += "0"
    return bitstring

def get_all_bitstrings(partial_strings):
    finished_strings = set()
    while(len(partial_strings) > 0):
        toRemove = []
        toAdd = []
        for bitstring in partial_strings:
            if(not "X" in bitstring):
                toRemove.append(bitstring)
                finished_strings.add(bitstring)
            else:
                for i in range(len(bitstring)):
                    if(bitstring[i] == "X"):
                        toRemove.append(bitstring)
                        toAdd.append(bitstring[:i] + "0" + bitstring[i+1:])
                        toAdd.append(bitstring[:i] + "1" + bitstring[i+1:])
                        break
        for remove in toRemove:
            partial_strings.remove(remove)
        for add in toAdd:
            partial_strings.add(add)
    return finished_strings

def to_decimals(bitstring):
    bitstrings = get_all_bitstrings({ bitstring })
    numbers = []
    for bs in bitstrings:
        num = 0
        for i in range(len(bs)):
            if(bs[i] == "1"):
                num += pow(2, 36-(i+1))
        numbers.append(num)
    return numbers

def combine(bitmask, bitstring):
    combined = ""
    for i in range(len(bitstring)):
        if(bitmask[i] != "X"):
            combined += bitmask[i]
        else:
            combined += bitstring[i]
    return combined

def combine_v2(bitmask, bitstring):
    combined = ""
    for i in range(len(bitstring)):
        if(bitmask[i] == "1"):
            combined += bitmask[i]
        elif(bitmask[i] == "0"):
            combined += bitstring[i]
        else:
            combined += "X"
    return combined

def run(program, isV2):
    memory = dict()
    bitmask = ""
    for line in program:
        mask = re.search(maskRgx, line)
        if mask:
            bitmask = mask.group(1)
        else:
            mem = re.search(memRgx, line)
            if(not isV2):
                memory[int(mem.group(1))] = to_decimals(combine(bitmask, to_bitstring(int(mem.group(2)))))[0]
            else:
                memVal = int(mem.group(2))
                for key in to_decimals(combine_v2(bitmask, to_bitstring(int(mem.group(1))))):
                    memory[key] = memVal
    sum = 0
    for m in memory:
        sum += memory[m]
    return sum
        

print(run(input, True))
