from aocd import lines

CUPS = [int(n) for n in lines[0]]

def crab_cups(init_cups, rounds):
    cups = dict(zip(init_cups, init_cups[1:] + init_cups[:1]))
    current = init_cups[0]
    for _ in range(rounds):
        pick_up = []
        tmp_label = current
        for _ in range(3):
            tmp_label = cups[tmp_label]
            pick_up.append(tmp_label)
        cups[current] = cups[tmp_label]
        destination = current - 1
        while destination in pick_up or destination < 1:
            destination -= 1
            destination = max(init_cups) if destination < 1 else destination
        cups[destination], cups[pick_up[-1]] = pick_up[0], cups[destination]
        current = cups[current]
    return cups

def print_cups(cups):
    c = 1
    cup_list = []
    for _ in range(len(cups)-1):
        cup_list.append(str(cups[c]))
        c = cups[c]
    return "".join(cup_list)

print("Part 1:", print_cups(crab_cups(CUPS, 100)))
cups_2 = CUPS + list(range(max(CUPS)+1, 1000001))
result = crab_cups(cups_2, 10000000)
part_2 = result[1] * result[result[1]]
print("Part 2:", part_2)
