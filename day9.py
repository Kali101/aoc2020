input = [int(i) for i in open("day9input.txt", "r")]
input_test = [35,20,15,25,47,40,62,55,65,95,102,117,150,182,127,219,299,277,309,576]

def get_invalid(data, preamble_length):
    addends = []
    for i in data:
        if len(addends) != preamble_length:
            addends.append(i)
        else:
            if not sum_to(i, addends):
                return i
            addends.pop(0)
            addends.append(i)

def sum_to(target, addends):
    for i in range(len(addends)):
        if addends[i] < target:
            for j in range(len(addends)):
                if i != j and addends[j] + addends[i] == target:
                    return True
    return False

def find_weakness(data, preamble_length):
    target = get_invalid(data, preamble_length)
    addends = []
    sum = 0
    for i in data:
        addends.append(i)
        sum += i
        if sum == target:
            return max(addends) + min(addends)
        while(sum > target):
            sum -= addends.pop(0)
            if sum == target:
                return max(addends) + min(addends)


print(find_weakness(input_test, 5))
print(find_weakness(input, 25))
