from copy import deepcopy
from aocd import lines

N = int((len(lines)-1)/2)
PLAYER_1 = [int(n) for n in lines[1:N]]
PLAYER_2 = [int(n) for n in lines[N+2:]]

def turn(p1, p2):
    if p1[0] > p2[0]:
        return p1, p2
    return p2, p1

def score(cards):
    return sum((i+1)*c for i, c in enumerate(reversed(cards)))

def combat(player_1, player_2):
    p1 = deepcopy(player_1)
    p2 = deepcopy(player_2)
    while p1 and p2:
        winner, loser = turn(p1, p2)
        winner.append(winner.pop(0))
        winner.append(loser.pop(0))
    return score(winner)

def recursive_combat(player_1, player_2):
    p1 = deepcopy(player_1)
    p2 = deepcopy(player_2)
    p1_mem = []
    p2_mem = []
    while p1 and p2:
        if p1 in p1_mem or p2 in p2_mem:
            return p1, p2, True
        p1_mem.append(deepcopy(p1))
        p2_mem.append(deepcopy(p2))
        if p1[0] < len(p1) and p2[0] < len(p2):
            _, _, p1_win = recursive_combat(p1[1:p1[0]+1], p2[1:p2[0]+1])
            winner = p1 if p1_win else p2
            loser = p2 if p1_win else p1
        else:
            winner, loser = turn(p1, p2)
        winner.append(winner.pop(0))
        winner.append(loser.pop(0))
    return winner, loser, winner == p1

print("Part 1:", combat(PLAYER_1, PLAYER_2))
recursive_winner, _, _ = recursive_combat(PLAYER_1, PLAYER_2)
print("Part 2:", score(recursive_winner))
