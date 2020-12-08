import re

input = open("day7input.txt", "r").readlines()
input_test = open("day7input_test.txt", "r").readlines()

rule_regex = r'(.*) bags contain (.*)'
contains_regex = r'(\d*) (\w* \w*) bag'

def generate_holder_rules(data):
    rules_dictionary = {}
    for line in data:
        rule = re.search(rule_regex, line)
        for bag in re.findall(contains_regex, rule.group(2)):
            if(len(bag) == 2 and int(bag[0]) > 0):
                if bag[1] in rules_dictionary:
                   rules_dictionary[bag[1]].append(rule.group(1))
                else:
                    rules_dictionary[bag[1]] = [rule.group(1),]
    return rules_dictionary

def count_holders(rules_dictionary, color, holders = set([])):
    if color in rules_dictionary:
        for holder_color in rules_dictionary[color]:
            holders.add(holder_color)
            count_holders(rules_dictionary, holder_color, holders)
    return len(holders);

def generate_holding_rules(data):
    rules_dictionary = {}
    for line in data:
        rule = re.search(rule_regex, line)
        for bag in re.findall(contains_regex, rule.group(2)):
            if(len(bag) == 2 and int(bag[0]) > 0):
                if rule.group(1) in rules_dictionary:
                   rules_dictionary[rule.group(1)].append((bag[1], int(bag[0])))
                else:
                    rules_dictionary[rule.group(1)] = [(bag[1], int(bag[0])),]
    return rules_dictionary

def count_holding(rules_dictionary, color, count = 0, multiple = 1):
    if color in rules_dictionary:
        for holding_color in rules_dictionary[color]:
            count += count_holding(rules_dictionary, holding_color[0], multiple * holding_color[1], multiple * holding_color[1])
    return count

print(count_holders(generate_holder_rules(input), 'shiny gold'))
print(count_holding(generate_holding_rules(input), 'shiny gold'))
