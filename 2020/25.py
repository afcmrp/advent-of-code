from aocd import numbers

CARD_PUBLIC_KEY = numbers[0]
DOOR_PUBLIC_KEY = numbers[1]

def transform(value, subject_number):
    value *= subject_number
    return value % 20201227

val = 1
key = 1
while val != CARD_PUBLIC_KEY:
    val = transform(val, 7)
    key = transform(key, DOOR_PUBLIC_KEY)

print("Part 1:", key)
