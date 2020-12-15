from aocd import lines

def get_num(start, stop):
    mem = {v: i for i, v in enumerate(start[:-1])}
    num = start[-1]
    for i in range(len(start)-1, stop-1):
        mem[num], num = i, i - mem.get(num, i)
    return num

starting_nums = [int(x) for x in lines[0].split(",")]
print("Part 1: " + str(get_num(starting_nums, 2020)))
print("Part 2: " + str(get_num(starting_nums, 30000000)))
