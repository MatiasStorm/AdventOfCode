import re

def get_input():
    input = []
    passport_str = ""
    with open('input.txt', 'r') as f:
        for l in f.readlines():
            if l == "\n":
                fields = [i for i in passport_str[0: -1].split(" ")]
                passport = {}
                for field in fields:
                    key, val = field.split(":")
                    passport[key] = val
                input.append(passport)
                passport_str = ""
            else:
                passport_str += l.replace("\n", " ")
    return input


def check_passports_1(passports):
    result = 0
    for passport in passports:
        keys = passport.keys()
        if len(keys) == 8 or ( len(keys) == 7 and 'cid' not in keys ):
            result += 1
    return result


def byr(b):
    return 1920 <= int(b) <= 2002

def iyr(i):
    return 2010 <= int(i) <= 2020

def eyr(e):
    return 2020 <= int(e) <= 2030

def hgt(h):
    unit = h[-2:len(h)]
    if unit == "cm":
        return 150 <= int(h[0:-2]) <= 193
    if unit == "in":
        return 59 <= int(h[0:-2]) <= 76
    return False

def hcl(h):
    return re.sub("^#[a-f0-9]{6}", "", h) == ""

def ecl(e):
    return e in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

def pid(p):
    return len(p) == 9

def check_fields(p):
    return pid(p["pid"]) and ecl(p["ecl"]) and hcl(p["hcl"]) and hgt(p["hgt"]) and eyr(p["eyr"]) and iyr(p["iyr"]) and byr(p["byr"])

def check_passports_2(passports):
    result = 0
    for passport in passports:
        keys = passport.keys()
        if len(keys) == 8 or ( len(keys) == 7 and 'cid' not in keys ):
            if check_fields(passport):
                result += 1
    return result



if __name__ == "__main__":
    input = get_input()
    print("Correct Passports: ", check_passports_1(input))
    print("Correct Passports: ", check_passports_2(input))


