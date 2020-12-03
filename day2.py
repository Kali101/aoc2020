import re

pwRegex = re.compile('(\d+)-(\d+) (\w): (\w+)')

test_input = ["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc"]
real_input = open("day2input.txt", "r").readlines()

def validate_sled(password):
    match = pwRegex.match(password)
    lowerBound = int(match.group(1))
    upperBound = int(match.group(2))
    matchLetter = match.group(3)
    numMatches = 0
    for letter in match.group(4):
        if letter == matchLetter:
            numMatches += 1
    return lowerBound <= numMatches <= upperBound

def validate_toboggan(password):
    match = pwRegex.match(password)
    first_position = int(match.group(1))
    second_position = int(match.group(2))
    matchLetter = match.group(3)
    first_match = match.group(4)[first_position-1] == matchLetter
    second_match = match.group(4)[second_position-1] == matchLetter
    return ((first_match and not second_match) or (second_match and not first_match))
    
def count_valid(passwords):
    numValid = 0
    for pw in passwords:
        if(validate_toboggan(pw)):
            numValid += 1
    return numValid
        

print(count_valid(real_input))
                
