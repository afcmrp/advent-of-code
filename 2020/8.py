from aocd import lines

def run(instructions):
    executed = [False for _ in instructions]
    accumulator = 0
    i = 0
    last_i = len(instructions) - 1
    while i <= last_i and not executed[i]:
        executed[i] = True
        operation = instructions[i][:3]
        val = int(instructions[i][4:])
        if operation == "acc":
            accumulator += val
        if i == last_i:
            return True, accumulator
        if operation == "jmp":
            i += val
        else:
            i += 1
    return False, accumulator

def terminate_instructions(instructions):
    for idx, instruction in enumerate(instructions):
        if instruction[0:3] in ["jmp", "nop"]:
            f = "jmp" if "jmp" in instruction else "nop"
            t = "nop" if "jmp" in instruction else "jmp"
            new = [i.replace(f, t) if idx_n == idx else i for idx_n, i in enumerate(instructions)]
            terminates, accumulator = run(new)
            if terminates:
                return accumulator

_, acc = run(lines)
print("Part 1:", acc)
print("Part 2:", terminate_instructions(lines))
