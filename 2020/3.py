from aocd import lines

SLOPES = [
    (1, 1),
    (3, 1),
    (5, 1),
    (7, 1),
    (1, 2),
]

def trees_collided(tree_map, slope):
    collided = 0
    witdh = len(tree_map[0])
    right, down = slope
    pos_x = 0
    pos_y = 0
    while pos_y < len(tree_map) - 1:
        pos_x = (pos_x + right) % witdh
        pos_y += down
        if tree_map[pos_y][pos_x] == "#":
            collided += 1
    return collided

print("Part 1:", trees_collided(lines, (3, 1)))

prod = 1
for s in SLOPES:
    prod *= trees_collided(lines, s)

print("Part 2:", prod)
