from aocd import lines

TIMESTAMP = int(lines[0])
BUS_IDS = [(int(b), idx) for idx, b in enumerate(lines[1].split(",")) if b != "x"]

def earliest_depart():
    departures = [b - (TIMESTAMP % b) for b, _ in BUS_IDS]
    d_min = min(departures)
    b_idx = departures.index(d_min)
    return d_min * BUS_IDS[b_idx][0]

def find_t():
    t = 0
    step = 1
    for bus, offset in BUS_IDS:
        ts = t
        while True:
            ts += step
            if (ts + offset) % bus == 0:
                t = ts
                step *= bus
                break
    return t

print("Part 1:", earliest_depart())
print("Part 2:", find_t())
