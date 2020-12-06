import re

PASSWORD_REGEXP = r"^(\d+)-(\d+) ([a-zA-Z]+): ([a-zA-Z]+)$"
MIN = 1
MAX = 2
CHAR = 3
PASSWORD = 4

def valid_password1(char, min_char, max_char, password):
    return min_char <= password.count(char) <= max_char

def valid_password2(char, idx1, idx2, password):
    return (password[idx1-1] == char) ^ (password[idx2-1] == char)

def main():
    with open("2.txt") as password_file:
        passwords_raw = password_file.readlines()
    passwords = [p.replace("\n", "") for p in passwords_raw]
    valid1 = 0
    valid2 = 0
    for password_str in passwords:
        match = re.match(PASSWORD_REGEXP, password_str)
        min_char = int(match.group(MIN))
        max_char = int(match.group(MAX))
        char = match.group(CHAR)
        password = match.group(PASSWORD)
        if valid_password1(char, min_char, max_char, password):
            valid1 += 1
        if valid_password2(char, min_char, max_char, password):
            valid2 += 1
    print("Part 1: " + str(valid1))
    print("Part 2: " + str(valid2))

if __name__ == "__main__":
    main()
