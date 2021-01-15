import re
from aocd import lines

PASSWORD_REGEXP = r"^(\d+)-(\d+) ([a-zA-Z]+): ([a-zA-Z]+)$"

def parse_password(password):
    match = re.match(PASSWORD_REGEXP, password)
    min_char = int(match.group(1))
    max_char = int(match.group(2))
    char = match.group(3)
    p = match.group(4)
    return char, min_char, max_char, p

def valid_password1(password):
    char, min_char, max_char, password = parse_password(password)
    return min_char <= password.count(char) <= max_char

def valid_password2(password):
    char, idx1, idx2, password = parse_password(password)
    return (password[idx1-1] == char) ^ (password[idx2-1] == char)

print("Part 1:", sum(1 for password in lines if valid_password1(password)))
print("Part 2:", sum(1 for password in lines if valid_password2(password)))
