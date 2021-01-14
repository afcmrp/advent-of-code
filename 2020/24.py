from aocd import lines

DIR = {
    "e": 1+0j,
    "ne": 1-1j,
    "nw": 0-1j,
    "w": -1+0j,
    "sw": -1+1j,
    "se": 0+1j,
}

ADJ = list(DIR.values())

def tile_position(tile):
    s = 0
    pos = 0+0j
    while s < len(tile):
        i = 1 if tile[s:s+1] in DIR else 2
        pos += DIR[tile[s:s+i]]
        s += i
    return pos

def adjacent(tile):
    for adj in ADJ:
        yield tile + adj

def flip_tiles(tiles, days):
    t = {pos: tiles.count(pos) for pos in tiles}
    black = set(pos for pos in t if t[pos] % 2)
    for _ in range(days):
        flip = set()
        checked = []
        for b in black:
            # Check if black should be flipped
            black_adjacent = sum(True for a in adjacent(b) if a in black)
            if black_adjacent == 0 or black_adjacent > 2:
                flip.add(b)
            checked.append(b)
            # Check if any adjecent white should be flipped
            for adj in adjacent(b):
                if adj in checked or adj in black:
                    continue
                black_adjacent = sum(True for a in adjacent(adj) if a in black)
                if black_adjacent == 2:
                    flip.add(adj)
                checked.append(adj)
        black ^= flip
    return len(black)

tiles_init = [tile_position(t) for t in lines]
print("Part 1:", flip_tiles(tiles_init, 0))
print("Part 2:", flip_tiles(tiles_init, 100))
