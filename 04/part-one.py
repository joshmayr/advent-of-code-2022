input = open("input.txt", "r").read()

lines = input.splitlines()

counter = 0

for line in lines:
    assignments = line.split(',')
    elves = []
    for elf in assignments:
        elf = elf.split('-')
        elf = [eval(i) for i in elf]
        elves.append(elf)

    elf1_range = elves[0][1] - elves[0][0]
    elf2_range = elves[1][1] - elves[1][0]

    if elf2_range - elf1_range <= 0:
        if elves[1][1] <= elves[0][1] and elves[1][0] >= elves[0][0]:
            counter += 1
    else:
        if elves[0][1] <= elves[1][1] and elves[0][0] >= elves[1][0]:
            counter += 1
print(counter)