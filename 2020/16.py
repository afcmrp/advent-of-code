import re
from aocd import lines

FIELD_REGEX = r"^(.+): (\d+)-(\d+) or (\d+)-(\d+)$"
TICKET_REGEX = r"^\d+(,\d+)+$"

FIELDS = {}
TICKETS = []
for line in lines:
    m = re.match(FIELD_REGEX, line)
    if m:
        FIELDS[m.group(1)] = [int(m.group(2)),
                              int(m.group(3)),
                              int(m.group(4)),
                              int(m.group(5))]
        continue
    m = re.match(TICKET_REGEX, line)
    if m:
        t = [int(i) for i in line.split(",")]
        TICKETS.append(t)

def invalid_value(ticket):
    for val in ticket:
        if not any_valid_field(val):
            return val
    return None

def valid_field(field, val):
    v = FIELDS[field]
    return v[0] <= val <= v[1] or v[2] <= val <= v[3]

def any_valid_field(val):
    for field in FIELDS:
        if valid_field(field, val):
            return True
    return False

def valid_field_order(idx, field):
    for ticket in VALID_TICKETS:
        if not valid_field(field, ticket[idx]):
            return False
    return True

invalid_values = [invalid_value(t) for t in TICKETS]
part1 = sum(v for v in invalid_values if v is not None)
print("Part 1:", part1)

VALID_TICKETS = [t for t in TICKETS if invalid_value(t) is None]
candidates = {}
for f in FIELDS:
    for i in range(len(FIELDS)):
        if valid_field_order(i, f):
            if f in candidates:
                candidates[f].append(i)
            else:
                candidates[f] = [i]

valid_orders = {}
while candidates:
    for c in candidates:
        if len(candidates[c]) == 1:
            order = candidates[c][0]
            valid_orders[c] = order
            f = c
            break
    for c2 in candidates:
        if order in candidates[c2]:
            candidates[c2].remove(order)
    del candidates[f]

prod = 1
for f in valid_orders:
    if f.startswith("departure"):
        prod *= TICKETS[0][valid_orders[f]]

print("Part 2:", prod)
