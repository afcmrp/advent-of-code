from aocd import lines

def get_groups():
    groups = []
    group = []
    for line in lines:
        if not line:
            groups.append(group)
            group = []
            continue
        group.append(line)
    groups.append(group)
    return groups

def unique_q(group):
    return list({q for p in group for q in p})

def all_q(group):
    q_sum = 0
    g_len = len(group)
    qs = [q for p in group for q in p]
    qs_unique = unique_q(group)
    for q in qs_unique:
        if qs.count(q) == g_len:
            q_sum += 1
    return q_sum

def get_qsum1(groups):
    q_sum = 0
    for group in groups:
        qs = unique_q(group)
        q_sum += len(qs)
    return q_sum

def get_qsum2(groups):
    q_sum = 0
    for group in groups:
        q_sum += all_q(group)
    return q_sum

def main():
    groups = get_groups()
    q_sum1 = get_qsum1(groups)
    print("Part 1: " + str(q_sum1))
    q_sum2 = get_qsum2(groups)
    print("Part 2: " + str(q_sum2))

if __name__ == "__main__":
    main()
