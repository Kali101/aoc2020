import re

input = open("day5input.txt", "r").read().splitlines()

def get_seat_id(code):
    row_lowest = 0
    row_highest = 128
    column_lowest = 0
    column_highest = 8
    for char in code:
        if char == 'F':
            row_highest = row_highest - ((row_highest - row_lowest) / 2)
        elif char == 'B':
            row_lowest = row_lowest + ((row_highest - row_lowest) / 2)
        elif char == 'L':
            column_highest = column_highest - ((column_highest - column_lowest) / 2)
        elif char == 'R':
            column_lowest = column_lowest + ((column_highest - column_lowest) / 2)
    return row_lowest * 8 + column_lowest

def get_highest_seat_id(data):
    highest_seat_id = 0
    for code in data:
        highest_seat_id = max(get_seat_id(code), highest_seat_id)
    return highest_seat_id

all_open_seats = list(range(0, int(get_highest_seat_id(input)) + 1))
for code in input:
    all_open_seats.remove(int(get_seat_id(code)))
print(all_open_seats)
            
