from aocd import lines

DECODE = {
    "B": "1",
    "R": "1",
    "F": "0",
    "L": "0"
}

def get_id(seat):
    return int("".join(DECODE[c] for c in seat), 2)

seat_ids = [get_id(seat) for seat in lines]
seat_ids.sort()

print("Part 1:", max(seat_ids))
for i, sid in enumerate(seat_ids):
    if sid + 1 != seat_ids[i+1]:
        print("Part 2:", sid+1)
        break
