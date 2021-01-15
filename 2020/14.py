import re
from more_itertools import powerset
from aocd import lines

MSK_REGEX = r"^mask = (.{36})$"
MEM_REGEX = r"^mem\[(\d*)\] = (\d*)$"

def get_instructions():
    program = []
    instructions = []
    for line in lines:
        if "mask" in line and program:
            instructions.append(program)
            program = []
        program.append(line)
    instructions.append(program)
    return instructions

def decode_value(val, mask):
    val |= int(mask.replace("X", "0"), 2)
    val &= int(mask.replace("X", "1"), 2)
    return val

def decode_address(addr, mask):
    addr |= int(mask.replace("X", "0"), 2)
    addr &= int(mask.replace("0", "1").replace("X", "0"), 2)
    floating = [2**idx for idx, c in enumerate(reversed(mask)) if c == 'X']
    return [addr + sum(f) for f in powerset(floating)]

def part1(instructions):
    mem = {}
    for prog in instructions:
        mask = re.match(MSK_REGEX, prog[0]).group(1)
        for value in prog[1:]:
            match = re.match(MEM_REGEX, value)
            addr = int(match.group(1))
            val = int(match.group(2))
            mem[addr] = decode_value(val, mask)
    return sum(mem.values())

def part2(instructions):
    mem = {}
    for prog in instructions:
        mask = re.match(MSK_REGEX, prog[0]).group(1)
        for value in prog[1:]:
            match = re.match(MEM_REGEX, value)
            addr = int(match.group(1))
            val = int(match.group(2))
            addresses = decode_address(addr, mask)
            for address in addresses:
                mem[address] = val
    return sum(mem.values())

inst = get_instructions()
print("Part 1:", part1(inst))
print("Part 2:", part2(inst))
