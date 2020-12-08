def get_input():
    with open("8.txt") as input_file:
        input_raw = input_file.readlines()
    return [s.replace("\n", "") for s in input_raw]

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
    for instruction_idx, instruction in enumerate(instructions):
        if instruction[0:3] in ["jmp", "nop"]:
            f = "jmp" if "jmp" in instruction else "nop"
            t = "nop" if "jmp" in instruction else "jmp"
            new = [i.replace(f, t) if idx == instruction_idx else i for idx, i in enumerate(instructions)]
            terminates, acc = run(new)
            if terminates:
                return acc

def main():
    instructions = get_input()
    _, acc1 = run(instructions)
    print("Part 1: " + str(acc1))
    acc2 = terminate_instructions(instructions)
    print("Part 2: " + str(acc2))

if __name__ == "__main__":
    main()
