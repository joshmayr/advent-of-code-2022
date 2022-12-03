input = open("input.txt", "r").read()

lines = input.splitlines()

items_in_both = {}


for line in lines:
    rucksack_one_dict = {}
    rucksack_one = line[:int(len(line)/2)]
    rucksack_two = line[int(len(line)/2):]
    for item in rucksack_one:
        if item not in rucksack_one_dict:
            rucksack_one_dict[item] = 1

    rucksack_two_items_dict = {}
    for item in rucksack_two:
        if item not in rucksack_two_items_dict:
            if item in rucksack_one_dict:
                if item in items_in_both:
                    items_in_both[item] += 1
                else:
                    items_in_both[item] = 1
        rucksack_two_items_dict[item] = True


score = 0
for item in items_in_both:
    comparator = 'a'
    offset = 1
    if item < 'a':
        comparator = 'A'
        offset = 27
    score += items_in_both[item] * (ord(item) - ord(comparator) + offset)
print(score)