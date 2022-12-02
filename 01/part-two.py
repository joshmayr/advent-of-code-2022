input = open("input.txt", "r").read()

lines = input.splitlines()

top_three_elvs_cals = [0, 0, 0]

elf_cals = 0
for line in lines:
    if line != "":
        elf_cals += int(line)
    else:
        if(elf_cals > min(top_three_elvs_cals)):
            top_three_elvs_cals[top_three_elvs_cals.index(min(top_three_elvs_cals))] = elf_cals
        elf_cals = 0
print(sum(top_three_elvs_cals))