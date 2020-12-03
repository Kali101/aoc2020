test_input = ["1721", "979", "366", "299", "675", "1456"]
real_input = open("day1input.txt", "r").readlines()

def product_2020(input):
    for number in input:
        addend1 = int(number)
        for otherNumber in input:
            addend2 = int(otherNumber)
            if addend1+addend2 == 2020:
                return addend1*addend2

def product_2_2020(input):
    for number in input:
        addend1 = int(number)
        for otherNumber in input:
            addend2 = int(otherNumber)
            if addend1+addend2 < 2020:                
                for finalNumber in input:
                    addend3 = int(finalNumber)
                    if addend1+addend2+addend3 == 2020:
                        return addend1*addend2*addend3

print(product_2_2020(real_input))
                
