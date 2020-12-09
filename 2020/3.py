import math
from aocd import lines

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

def main():
    tree_map = lines
    answer1 = trees_collided(tree_map, (3, 1))
    print("Part 1: " + str(answer1))
    slopes = [
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2),
    ]
    collided2 = []
    for slope in slopes:
        col = trees_collided(tree_map, slope)
        collided2.append(col)
    answer2 = math.prod(collided2)
    print("Part 2: " + str(answer2))

if __name__ == "__main__":
    main()
