input = open("day11input.txt", "r").read().splitlines()
input_test = open("day11input_test.txt", "r").read().splitlines()

def get_occupied_adjacent(data, i, j, threshold, isMaxThreshold):
    occupied = 0
    for ai in (i-1, i, i+1):
        for aj in (j-1, j, j+1):
            if(ai >= 0 and aj >= 0 and (ai != i or aj != j) and ai < len(data) and aj < len(data[i]) and data[ai][aj] == "#"):
                occupied += 1
                if(occupied > threshold):
                    return isMaxThreshold
    return not isMaxThreshold;

def get_lineofsight_seat_occupied(data, i, j, iDir, jDir):
    n = 1
    while(i + n*iDir >= 0 and j + n*jDir >= 0 and i + n*iDir < len(data) and j + n*jDir < len(data[i])):
          if(data[i + n*iDir][j + n*jDir] != "."):
              if(data[i + n*iDir][j + n*jDir] == "L"):
                  return False
              else:
                  return True
          n += 1
    return False

def get_occupied_lineofsight(data, i, j, threshold, isMaxThreshold):
    occupied = 0
    for iDir in (-1, 0, 1):
        for jDir in (-1, 0, 1):
            if(iDir == 0 and jDir == 0):
                continue
            elif(get_lineofsight_seat_occupied(data, i, j, iDir, jDir)):
                occupied += 1
                if(occupied > threshold):
                    return isMaxThreshold
    return not isMaxThreshold;


def seat_passengers(data, seated_count = 0):
    has_changed_state = False
    new_data = []
    for i in range(len(data)):
        new_row = ""
        for j in range(len(data[i])):
            if(data[i][j] == "L" and get_occupied_lineofsight(data, i, j, 0, False)):
                new_row += '#'
                seated_count += 1
                has_changed_state = True
            elif(data[i][j] == "#" and get_occupied_lineofsight(data, i, j, 4, True)):
                new_row += 'L'
                seated_count -= 1
                has_changed_state = True
            else:
                new_row += data[i][j]
        new_data.append(new_row)
    return (new_data, seated_count, has_changed_state)


def count_seats(input_data):
    data = input_data
    seated_count = 0
    has_changed_state = True
    while(has_changed_state):
        (data, seated_count, has_changed_state) = seat_passengers(data, seated_count)
    return seated_count
        
print(count_seats(input))

