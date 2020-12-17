# bailey posante
# 12/17/2020
# advent of code day 4 puzzle

import re

with open("aoc4input.txt") as file:
    passports = file.read().split("\n\n")
    passports = [line.replace("\n", " ") for line in passports]

#print(passports)

# part 1
def validpassports(list):
    count = 0
    requirements = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    for string in list:
        if all(x in string for x in requirements):
            count += 1
    return count

print(validpassports(passports))

# part 2
# puts the info in a list of dictionaries instead for this part
with open("aoc4input.txt") as file:
    passports1 = file.read().split("\n\n")
    passports1 = [re.split(" |\n", passport) for passport in passports1]
    passports1 = [dict(pairs.split(":") for pairs in passport if pairs != "") for passport in passports1]
    #print(passports1)


def validvalues(list):
    count = 0
    requirements = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    ecl = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    for passport in list:
        if all(key in passport for key in requirements):
            if 1920 <= int(passport["byr"]) <= 2002:
                if 2010 <= int(passport["iyr"]) <= 2020:
                    if 2020 <= int(passport["eyr"]) <= 2030:
                        if ("cm" in passport["hgt"] and 150 <= int(passport["hgt"][:-2]) <= 193) or ("in" in passport["hgt"] and 59 <= int(passport["hgt"][:-2]) <= 76):
                            if re.match(r"#[0-9a-f]{6}", passport["hcl"]):
                                if passport["ecl"] in ecl:
                                    if re.match(r"^[0-9]{9}$", passport["pid"]):
                                        count += 1  
    return count

print(validvalues(passports1))
