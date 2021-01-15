import re
from aocd import lines

HGT_REGEX = r"^(\d+)(cm|in)$"
HCL_REGEX = r"^#[a-f0-9]{6}$"
PID_REGEX = r"^\d{9}$"

def valid_byr(byr):
    return len(byr) == 4 and 1920 <= int(byr) <= 2002

def valid_iyr(iyr):
    return len(iyr) == 4 and 2010 <= int(iyr) <= 2020

def valid_eyr(eyr):
    return len(eyr) == 4 and 2020 <= int(eyr) <= 2030

def valid_hgt(hgt):
    match = re.match(HGT_REGEX, hgt)
    if not match:
        return False
    if match.group(2) == "cm":
        return 150 <= int(match.group(1)) <= 193
    if match.group(2) == "in":
        return 59 <= int(match.group(1)) <= 76
    return False

def valid_hcl(hcl):
    return re.match(HCL_REGEX, hcl) is not None

def valid_ecl(ecl):
    return ecl in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

def valid_pid(pid):
    return re.match(PID_REGEX, pid) is not None

REQUIRED_FIELDS = {
    "byr": valid_byr,
    "iyr": valid_iyr,
    "eyr": valid_eyr,
    "hgt": valid_hgt,
    "hcl": valid_hcl,
    "ecl": valid_ecl,
    "pid": valid_pid,
}

def get_passports():
    passports = []
    passport = {}
    for line in lines:
        if not line:
            passports.append(passport)
            passport = {}
            continue
        line_split = line.split(" ")
        for data in line_split:
            data_split = data.split(":")
            passport[data_split[0]] = data_split[1]
    passports.append(passport)
    return passports

def valid_passport1(passport):
    return all([f in passport.keys() for f in REQUIRED_FIELDS])

def valid_passport2(passport):
    if not valid_passport1(passport):
        return False
    for field in passport:
        if field in REQUIRED_FIELDS:
            fun = REQUIRED_FIELDS[field]
            if not fun(passport[field]):
                return False
    return True

PASSPORTS = get_passports()
print("Part 1:", sum(valid_passport1(p) for p in PASSPORTS))
print("Part 2:", sum(valid_passport2(p) for p in PASSPORTS))
