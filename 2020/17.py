from aocd import lines

def key(x, y, z, w):
    return "x"+str(x)+"y"+str(y)+"z"+str(z)+"w"+str(w)

def minmax(state):
    max_x = max(int(k[1:k.index("y")]) for k in state)
    min_x = min(int(k[1:k.index("y")]) for k in state)
    max_y = max(int(k[k.index("y")+1:k.index("z")]) for k in state)
    min_y = min(int(k[k.index("y")+1:k.index("z")]) for k in state)
    max_z = max(int(k[k.index("z")+1:k.index("w")]) for k in state)
    min_z = min(int(k[k.index("z")+1:k.index("w")]) for k in state)
    max_w = max(int(k[k.index("w")+1:]) for k in state)
    min_w = min(int(k[k.index("w")+1:]) for k in state)
    return max_x, min_x, max_y, min_y, max_z, min_z, max_w, min_w

def print_state(state):
    max_x, min_x, max_y, min_y, max_z, min_z, max_w, min_w = minmax(state)
    for w in range(min_w, max_w+1):
        for z in range(min_z, max_z+1):
            print("z=%d, w=%d" % (z, w))
            for x in range(min_x, max_x+1):
                _str = ""
                for y in range(min_y, max_y+1):
                    k = key(x, y, z, w)
                    _str += state[k]
                print(_str)
    print()

def initial_state():
    state = {}
    for x, line in enumerate(lines):
        for y, c in enumerate(line):
            state[key(x, y, 0, 0)] = c
    return state

def neighbors_active3(state, x, y, z):
    active = 0
    for x2 in range(x-1, x+2):
        for y2 in range(y-1, y+2):
            for z2 in range(z-1, z+2):
                if [x2, y2, z2] == [x, y, z]:
                    continue
                k = key(x2, y2, z2, 0)
                if k in state and state[k] == "#":
                    active += 1
    return active

def neighbors_active4(state, x, y, z, w):
    active = 0
    for x2 in range(x-1, x+2):
        for y2 in range(y-1, y+2):
            for z2 in range(z-1, z+2):
                for w2 in range(w-1, w+2):
                    if [x2, y2, z2, w2] == [x, y, z, w]:
                        continue
                    k = key(x2, y2, z2, w2)
                    if k in state and state[k] == "#":
                        active += 1
    return active

def next_state3(state):
    n_state = {}
    max_x, min_x, max_y, min_y, max_z, min_z, _, _ = minmax(state)
    for x in range(min_x-1, max_x+2):
        for y in range(min_y-1, max_y+2):
            for z in range(min_z-1, max_z+2):
                k = key(x, y, z, 0)
                n = neighbors_active3(state, x, y, z)
                if k in state and state[k] == "#" and n in [2, 3]:
                    n_state[k] = "#"
                elif (not k in state or state[k] == ".") and n == 3:
                    n_state[k] = "#"
                else:
                    n_state[k] = "."
    return n_state

def next_state4(state):
    n_state = {}
    max_x, min_x, max_y, min_y, max_z, min_z, max_w, min_w = minmax(state)
    for x in range(min_x-1, max_x+2):
        for y in range(min_y-1, max_y+2):
            for z in range(min_z-1, max_z+2):
                for w in range(min_w-1, max_w+2):
                    k = key(x, y, z, w)
                    n = neighbors_active4(state, x, y, z, w)
                    if k in state and state[k] == "#" and n in [2, 3]:
                        n_state[k] = "#"
                    elif (not k in state or state[k] == ".") and n == 3:
                        n_state[k] = "#"
                    else:
                        n_state[k] = "."
    return n_state

def active_cubes(state):
    return sum(state[k] == "#" for k in state)

def run(dim):
    n_state = initial_state()
    next_fun = next_state3 if dim == 3 else next_state4
    for _ in range(6):
        n_state = next_fun(n_state)
    return active_cubes(n_state)

print("Part 1:", run(3))
print("Part 2:", run(4))
