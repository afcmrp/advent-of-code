from aocd import lines

def navigate1(instructions):
    direction = 0
    pos_y = 0
    pos_x = 0
    for instruction in instructions:
        d = instruction[0]
        val = int(instruction[1:])
        if d == "N":
            pos_y += val
        elif d == "S":
            pos_y -= val
        elif d == "E":
            pos_x += val
        elif d == "W":
            pos_x -= val
        elif d == "L":
            direction += val
        elif d == "R":
            direction -= val
        elif direction == 0:
            pos_x += val
        elif direction == 90:
            pos_y += val
        elif direction == 180:
            pos_x -= val
        elif direction == 270:
            pos_y -= val
        direction = direction % 360
    return abs(pos_x + pos_y)

def navigate2(instructions):
    pos_x = 0
    pos_y = 0
    wp_y = 1
    wp_x = 10
    for instruction in instructions:
        d = instruction[0]
        val = int(instruction[1:])
        if d == "N":
            wp_y += val
        elif d == "S":
            wp_y -= val
        elif d == "E":
            wp_x += val
        elif d == "W":
            wp_x -= val
        elif (d == "L" and val == 90) or (d == "R" and val == 270):
            wp_x, wp_y = -wp_y, wp_x
        elif d in ["L", "R"] and val == 180:
            wp_x, wp_y = -wp_x, -wp_y
        elif (d == "R" and val == 90) or (d == "L" and val == 270):
            wp_x, wp_y = wp_y, -wp_x
        else:
            pos_x += val*wp_x
            pos_y += val*wp_y
    return abs(pos_x) + abs(pos_y)

distance1 = navigate1(lines)
print("Part 1: " + str(distance1))
distance2 = navigate2(lines)
print("Part 2: " + str(distance2))
