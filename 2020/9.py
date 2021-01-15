from aocd import numbers

def find_first_invalid(xmas_data, preamble_size):
    for idx in range(len(xmas_data) - preamble_size):
        if not valid(xmas_data[idx:idx+preamble_size+1]):
            return xmas_data[idx+preamble_size]

def valid(num):
    last_num = num[-1]
    for idx1 in range(len(num)-1):
        for idx2 in range(len(num)-1):
            if idx1 != idx2 and num[idx1] + num[idx2] == last_num:
                return True
    return False

def find_contiguous(num, target):
    idx1 = idx2 = 0
    while True:
        contiguous = num[idx1:idx2]
        contiguous_sum = sum(contiguous)
        if contiguous_sum == target:
            break
        if contiguous_sum > target:
            idx1 += 1
        elif contiguous_sum < target:
            idx2 += 1
    return contiguous

first_invalid = find_first_invalid(numbers, 25)
print("Part 1:", first_invalid)
cont = find_contiguous(numbers, first_invalid)
sum2 = min(cont) + max(cont)
print("Part 2:", sum2)
