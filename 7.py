TAKEN = []

def get_bags():
    with open("7.txt") as input_file:
        input_raw = input_file.readlines()
    rules = [s.replace("\n", "") for s in input_raw]
    bags = {}
    bags_inv = {}
    for line in rules:
        line_split = line.split(" bags contain ")
        bag = line_split[0]
        content = line_split[1]
        bags_inside = [c[:c.index(" bag")] for c in content.split(", ")]
        bags[bag] = []
        if bags_inside == ["no other"]:
            continue
        for inside_bag in bags_inside:
            n = int(inside_bag[:inside_bag.index(" ")])
            b = inside_bag[inside_bag.index(" ")+1:]
            bags[bag].append((n, b))
            if b in bags_inv:
                bags_inv[b].append(bag)
            else:
                bags_inv[b] = [bag]
    return bags_inv, bags

def bag_carriers(target_bag, bags):
    global TAKEN
    if target_bag not in bags:
        return 0
    carriers = 0
    content = bags[target_bag]
    for bag in content:
        if bag in TAKEN:
            continue
        TAKEN.append(bag)
        carriers += bag_carriers(bag, bags) + 1
    return carriers

def bag_amount(target_bag, bags):
    amount = 1
    for bag in bags[target_bag]:
        amount += bag[0] * bag_amount(bag[1], bags)
    return amount

def main():
    bags1, bags2 = get_bags()
    answer1 = bag_carriers("shiny gold", bags1)
    print("Part 1: " + str(answer1))
    answer2 = bag_amount("shiny gold", bags2) - 1
    print("Part 2: " + str(answer2))

if __name__ == "__main__":
    main()
