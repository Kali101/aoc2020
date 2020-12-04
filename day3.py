test_input = open("day3input_test.txt", "r").read().splitlines()
real_input = open("day3input.txt", "r").read().splitlines()

def count_trees(terrain, xslope, yslope):
    trees = xpos = ypos = 0
    while ypos < len(terrain):
        if(terrain[ypos][xpos] == '#'):
            trees += 1
        xpos = (xpos + xslope) % len(terrain[ypos])
        ypos += yslope
    return trees

print(count_trees(real_input, 3, 1))
print(count_trees(real_input, 1, 1)*count_trees(real_input, 3, 1)*count_trees(real_input, 5, 1)*count_trees(real_input, 7, 1)*count_trees(real_input, 1, 2))
