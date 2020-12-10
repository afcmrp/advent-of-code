from aocd import numbers

def main():
    adaptors = sorted(numbers + [0, max(numbers)+ 3])
    diff = [adaptors[i] - adaptors[i-1] for i in range(1, len(adaptors))]
    answer_1 = diff.count(1) * diff.count(3)
    print("Part 1: " + str(answer_1))
    d_str = "".join([str(d) for d in diff])
    d_str = d_str.replace("1111", "A").replace("111", "B").replace("11", "C")
    answer_2 = 7 ** d_str.count("A") * 4 ** d_str.count("B") * 2 ** d_str.count("C")
    print("Part 2: " + str(answer_2))

if __name__ == "__main__":
    main()
