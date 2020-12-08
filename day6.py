import re

input = open("day6input.txt", "r").readlines()
input_test = open("day6input_test.txt", "r").readlines()

def get_total_any(data):
    sum_group_yes = 0
    yes_answers = set([])
    for line in data:
        if(line.isspace()):
            sum_group_yes += len(yes_answers)
            yes_answers = set([])
        else:
            for answer in line:
                if(answer.isalpha()):
                    yes_answers.add(answer)
    return sum_group_yes + len(yes_answers)

def get_total_unanimous(data):
    sum_group_yes = 0
    yes_answers = []
    new_group = True
    for line in data:
        if(line.isspace()):
            sum_group_yes += len(yes_answers)
            new_group = True
        else:
            if new_group:
                yes_answers = list(line.strip())
                new_group = False
            else:
                for answer in yes_answers.copy():
                    if answer not in line:
                        yes_answers.remove(answer)
    return sum_group_yes + len(yes_answers)


print(get_total_unanimous(input))
