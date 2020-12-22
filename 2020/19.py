import regex
from aocd import lines

RULES = dict(l.replace('"', "").split(": ", 1) for l in lines[:lines.index("")])
MESSAGES = lines[lines.index("")+1:]

def expand(value):
    if not value.isdigit():
        return value
    return "(?:" + "".join(map(expand, RULES[value].split())) + ")"

def matches(rule_n):
    r = regex.compile(expand(rule_n))
    return sum(r.fullmatch(m) is not None for m in MESSAGES)

print("Part 1:", matches("0"))
RULES["8"] = "42 +"  # repeat pattern
RULES["11"] = "(?P<R> 42 (?&R)? 31 )"  # recursive pattern
print("Part 2:", matches("0"))
