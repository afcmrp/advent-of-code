from math import sqrt
from aocd import lines

# with open("2020/20.txt") as f:
#     lines = f.readlines()
#     lines = [l.replace("\n", "") for l in lines]
N = 10
TILES = {int(lines[i][5:-1]): lines[i+1:i+N+1] for i in range(0, len(lines), N+2)}
SIZE = int(sqrt(len(TILES)))
N_I = (N - 2)

                  #
#    ##    ##    ###
 #  #  #  #  #  #
SEA_MONSTER = [
    (18, -1),
    (5, 0), (6, 0), (11, 0), (12, 0), (17, 0), (18, 0), (19, 0),
    (1, 1), (4, 1), (7, 1), (10, 1), (13, 1), (16, 1)
]

def flip(t):
    return [t[i] for i in range(len(t)-1, -1, -1)]

def rotate(t):
    return ["".join([r[i] for r in t]) for i in range(len(t)-1, -1, -1)]

def match_left(t_l, t):
    return t_l is None or [l[N-1] for l in t_l] == [l[0] for l in t]

def match_up(t_u, t):
    return t_u is None or t_u[N-1] == t[0]

def match(t_l, t_u, t):
    return match_left(t_l, t) and match_up(t_u, t)

def remove_borders(t):
    return [t[i][1:-1] for i in range(1, N-1)]

def combinations(tile):
    tiles = [tile]
    tiles.append(rotate(tiles[-1]))
    tiles.append(rotate(tiles[-1]))
    tiles.append(rotate(tiles[-1]))
    tiles.append(flip(tiles[-1]))
    tiles.append(rotate(tiles[-1]))
    tiles.append(rotate(tiles[-1]))
    tiles.append(rotate(tiles[-1]))
    return tiles

def match_tiles(tiles, corrected, used, i=0):
    if i == len(TILES):
        return True
    r = int(i / SIZE)
    c = int(i % SIZE)
    tile_left = None if c == 0 else corrected[used[r][c-1]]
    tile_up = None if r == 0 else corrected[used[r-1][c]]
    free_tiles = [k for k in tiles if not any(k in l for l in used)]
    for k in free_tiles:
        for tile in tiles[k]:
            if match(tile_left, tile_up, tile):
                used[r][c] = k
                corrected[k] = tile
                if match_tiles(tiles, corrected, used, i+1):
                    return corrected, used
                del corrected[k]
                used[r][c] = None
    return False

def assemble_image(images, ids):
    images = {k: remove_borders(images[k]) for k in images}
    image = []
    for r in range(SIZE):
        for i in range(N_I):
            image.append("".join(images[ids[r][c]][i] for c in range(SIZE)))
    return image

def find_sea_monsters(image):
    n = len(image)
    sea_monsters = 0
    i = n * 1
    while i < ((n-1) ** 2):
        r = int(i / n)
        c = int(i % n)
        if c < n-19 and image[r][c] == "#" and all(image[r+s[1]][c+s[0]] == "#" for s in SEA_MONSTER):
            sea_monsters += 1
        i += 1
    return sea_monsters

def calculate_roughness(image, sea_monsters):
    squares = sum(c == "#" for r in image for c in r)
    return squares - sea_monsters * (len(SEA_MONSTER) + 1)

def main():
    tile_combinations = {k: combinations(TILES[k]) for k in TILES}
    order = [[None for _ in range(SIZE)] for _ in range(SIZE)]
    images, ids = match_tiles(tile_combinations, {}, order)
    part1 = ids[0][0] * ids[0][-1] * ids[-1][0] * ids[-1][-1]
    print("Part 1:", part1)
    image = assemble_image(images, ids)
    image_combinations = combinations(image)
    for i in image_combinations:
        sea_monsters = find_sea_monsters(i)
        if sea_monsters:
            break
    part2 = calculate_roughness(image, sea_monsters)
    print("Part 1:", part2)

if __name__ == "__main__":
    main()
