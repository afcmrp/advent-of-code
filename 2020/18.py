from operator import add, mul
import re
from aocd import lines

BRACKET_REGEX = r"(\([^()]+\))"
ADDITION_REGEX = r"(\d+ \+ \d+)"

OPERATORS = {
    "+": add,
    "*": mul
}

def operate(exp):
    return str(OPERATORS[exp[1]](int(exp[0]), int(exp[2])))

def evaluate(expression, add_precedence):
    brackets = re.search(BRACKET_REGEX, expression)
    while brackets:
        b = brackets.group(1)
        expression = expression.replace(b, evaluate(b[1:-1], add_precedence), 1)
        brackets = re.search(BRACKET_REGEX, expression)
    addition = re.search(ADDITION_REGEX, expression)
    while add_precedence and addition:
        a = addition.group(1)
        expression = expression.replace(a, evaluate(a, False), 1)
        addition = re.search(ADDITION_REGEX, expression)
    exp = expression.split(" ")
    while len(exp) > 1:
        exp = [operate(exp[:3])] + exp[3:]
    return exp[0]

print("Part 1:", sum(int(evaluate(line, False)) for line in lines))
print("Part 2:", sum(int(evaluate(line, True)) for line in lines))
