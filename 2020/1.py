import math
from itertools import combinations
from aocd import numbers

def find_product(input_list, length):
    for combination in combinations(input_list, length):
        if sum(combination) == 2020:
            return math.prod(combination)

def main():
    answer_1 = find_product(numbers, 2)
    print("Part 1: " + str(answer_1))
    answer_2 = find_product(numbers, 3)
    print("Part 2: " + str(answer_2))

if __name__ == "__main__":
    main()
