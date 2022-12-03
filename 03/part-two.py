input = open("input.txt", "r").read()

lines = input.splitlines()

score = 0
counter = 0
first_ruck = {}
second_ruck = {}




def get_priority(item):
    comparator = 'a'
    offset = 1
    if item < 'a':
        comparator = 'A'
        offset = 27
    return (ord(item) - ord(comparator) + offset)


for line in lines:
    if counter == 0:
        for item in line:
            if item not in first_ruck:
                first_ruck[item] = 1
        counter += 1
    elif counter == 1:
        for item in line:
            if item in first_ruck:
                second_ruck[item] = 1
        counter += 1
    else:
        for item in line:
            if item in second_ruck:
                score += get_priority(item)
                break
        first_ruck = {}
        second_ruck = {}
        counter -= 2
print(score)