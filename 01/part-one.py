input = open("input.txt", "r").read()

lines = input.splitlines()

max_cals = 0
elf_cals = 0
for line in lines:
    if line != "":
        elf_cals += int(line)
    else:
        max_cals = max(max_cals, elf_cals)
        elf_cals = 0
print(max_cals)