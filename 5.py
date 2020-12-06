
def get_boarding_passes():
    with open("5.txt") as boarding_file:
        boarding_passes_raw = boarding_file.readlines()
    boarding_passes = [s.replace("\n", "") for s in boarding_passes_raw]
    return boarding_passes

def decode(code):
    l = 0
    h = 2 ** len(code) - 1
    for c in code:
        m = l + int((h-l)/2)
        if c in ["F", "L"]:
            h = m
        elif c in ["B", "R"]:
            l = m
    return h

def get_id(row, col):
    return 8 * row + col

def main():
    passes = get_boarding_passes()
    highest_id = 0
    seat_ids = []
    for code in passes:
        row = decode(code[:7])
        col = decode(code[7:])
        seat_id = get_id(row, col)
        seat_ids.append(seat_id)
        if seat_id > highest_id:
            highest_id = seat_id
    seat_ids.sort()
    print("Part 1: " + str(highest_id))
    for i, sid in enumerate(seat_ids):
        if sid + 1 != seat_ids[i+1]:
            print("Part 2: " + str(sid+1))
            break

if __name__ == "__main__":
    main()
