from aocd import lines

ADJ = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1), (0, 1),
    (1, -1), (1, 0), (1, 1)
]

def next_seat1(seats, row, col):
    if seats[row][col] == ".":
        return "."
    rows = len(seats)
    cols = len(seats[0])
    adj = [seats[row+r][col+c] for r, c in ADJ if 0 <= row+r < rows and 0 <= col+c < cols]
    if seats[row][col] == "L" and adj.count("#") == 0:
        return "#"
    if seats[row][col] == "#" and adj.count("#") >= 4:
        return "L"
    return seats[row][col]

def next_seat2(seats, row, col):
    if seats[row][col] == ".":
        return "."
    occupied_visible = 0
    for direction in ADJ:
        r = row + direction[0]
        c = col + direction[1]
        while 0 <= r < len(seats) and 0 <= c < len(seats[0]):
            if seats[r][c] == "L":
                break
            if seats[r][c] == "#":
                occupied_visible += 1
                break
            r += direction[0]
            c += direction[1]
    if seats[row][col] == "L" and occupied_visible == 0:
        return "#"
    if seats[row][col] == "#" and occupied_visible >= 5:
        return "L"
    return seats[row][col]

def stabilize(seats, fun):
    rows = len(seats)
    cols = len(seats[0])
    while True:
        next_seats = [[fun(seats, r, c) for c in range(cols)] for r in range(rows)]
        if next_seats == seats:
            return sum(r.count("#") for r in seats)
        seats = next_seats

def main():
    seats = [[s for s in l] for l in lines]
    answer_1 = stabilize(seats, next_seat1)
    print("Part 1: " + str(answer_1))
    answer_2 = stabilize(seats, next_seat2)
    print("Part 2: " + str(answer_2))

if __name__ == "__main__":
    main()
