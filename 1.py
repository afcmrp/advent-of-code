
def get_list():
    with open("1.txt") as input_file:
        input_str = input_file.readlines()
    input_int = [int(s.replace("\n", "")) for s in input_str]
    return input_int

def find_two_product(input_list):
    n_lines = len(input_list)
    for idx1 in range(n_lines):
        for idx2 in range(idx1+1, n_lines):
            if sum([input_list[idx1], input_list[idx2]]) == 2020:
                return input_list[idx1] * input_list[idx2]

def find_three_product(input_list):
    n_lines = len(input_list)
    for idx1 in range(n_lines):
        for idx2 in range(idx1+1, n_lines):
            for idx3 in range(idx2+2, n_lines):
                if sum([input_list[idx1], input_list[idx2], input_list[idx3]]) == 2020:
                    return input_list[idx1] * input_list[idx2] * input_list[idx3]

def main():
    input_list = get_list()
    answer_1 = find_two_product(input_list)
    print("Part 1: " + str(answer_1))
    answer_2 = find_three_product(input_list)
    print("Part 2: " + str(answer_2))

if __name__ == "__main__":
    main()
