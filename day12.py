import math

input = open("day12input.txt", "r").read().splitlines()
input_test = ["F10", "N3", "F7", "R90", "F11"]

def get_distance(data):
    east_distance = north_distance = 0
    facing = 0
    for instruction in data:
        if(instruction[0] is "F"):
            r = int(instruction[1:])
            east_distance += r * math.cos(math.radians(facing))
            north_distance += r * math.sin(math.radians(facing))
        elif(instruction[0] is "N"):
            north_distance += int(instruction[1:])
        elif(instruction[0] is "S"):
            north_distance -= int(instruction[1:])
        elif(instruction[0] is "W"):
            east_distance -= int(instruction[1:])
        elif(instruction[0] is "E"):
            east_distance += int(instruction[1:])
        elif(instruction[0] is "L"):
            facing = (facing + int(instruction[1:])) % 360
        elif(instruction[0] is "R"):
            facing = (facing - int(instruction[1:])) % 360
    return abs(north_distance) + abs(east_distance)

def get_waypoint_distance(data):
    waypoint_east = 10
    waypoint_north = 1
    east_distance = north_distance = 0
    for instruction in data:
        if(instruction[0] is "F"):
            r = int(instruction[1:])
            east_distance += r * waypoint_east
            north_distance += r * waypoint_north
        elif(instruction[0] is "N"):
            waypoint_north += int(instruction[1:])
        elif(instruction[0] is "S"):
            waypoint_north -= int(instruction[1:])
        elif(instruction[0] is "W"):
            waypoint_east -= int(instruction[1:])
        elif(instruction[0] is "E"):
            waypoint_east += int(instruction[1:])
        else:
            r = math.sqrt(pow(waypoint_east, 2) + pow(waypoint_north, 2))
            facing = math.degrees(math.atan2(waypoint_north, waypoint_east))
            if(instruction[0] is "L"):
                facing = (facing + int(instruction[1:])) % 360
            elif(instruction[0] is "R"):
                facing = (facing - int(instruction[1:])) % 360
            waypoint_east = r * math.cos(math.radians(facing))
            waypoint_north = r * math.sin(math.radians(facing))
    return abs(north_distance) + abs(east_distance)

print(get_waypoint_distance(input))
