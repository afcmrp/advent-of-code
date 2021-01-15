from functools import reduce
from operator import mul
from itertools import combinations
from aocd import numbers

def find_product(input_list, length):
    for combination in combinations(input_list, length):
        if sum(combination) == 2020:
            return reduce(mul, combination, 1)

print("Part 1:", find_product(numbers, 2))
print("Part 2:", find_product(numbers, 3))
