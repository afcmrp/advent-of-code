from aocd import lines

timestamp = int(lines[0])
bus_ids = [(int(b), idx) for idx, b in enumerate(lines[1].split(",")) if b != "x"]

def earliest_depart():
    departures = [b - (timestamp % b) for b, _ in bus_ids]
    d_min = min(departures)
    b_idx = departures.index(d_min)
    return d_min * bus_ids[b_idx][0]

def find_t():
    t = 0
    step = 1
    for bus, offset in bus_ids:
        ts = t
        while True:
            ts += step
            if (ts + offset) % bus == 0:
                t = ts
                step *= bus
                break
    return t

print("Part 1: " + str(earliest_depart()))
print("Part 2: " + str(find_t()))
