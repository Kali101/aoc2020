import re

input = open("day4input.txt", "r").readlines()

def validate_passports(data):
    numValid = 0
    passportStr = ""
    for line in data:
        if(line.isspace()):
            if(validate_passport(passportStr)):
                numValid += 1
            passportStr = ""
        else:
            passportStr = passportStr + " " + line
    if(validate_passport(passportStr)):
        numValid += 1
    return numValid

def validate_passport(data):
    if valid_year("byr", 1920, 2002, data):
        if valid_year("iyr", 2010, 2020, data):
            if valid_year("eyr", 2020, 2030, data):
                if valid_hgt(data):
                    if valid_hcl(data):
                        if valid_ecl(data):
                            if valid_pid(data):
                                return True
    return False

def valid_year(id, lowerBound, upperBound, data):
    regex = re.search(id+":\s*(\d+)\s+", data)
    if regex:
        return lowerBound <= int(regex.group(1)) <= upperBound
    return False

def valid_hgt(data):
    regex = re.search("hgt:\s*(\d+)(in|cm)\s+", data)
    if regex:
        if regex.group(2) == "cm":
            return 150 <= int(regex.group(1)) <= 193
        else:
            return 59 <= int(regex.group(1)) <= 76
    return False

def valid_hcl(data):
    regex = re.search("hcl:\s*#\s*([a-f0-9]{6})\s+", data)
    return regex

def valid_ecl(data):
    regex = re.search("ecl:\s*(\w{3})\s+", data)
    if regex:
        return regex.group(1) in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    return False

def valid_pid(data):
    regex = re.search("pid:\s*(\d{9})\s+", data)
    return regex
    
print(validate_passports(input))
