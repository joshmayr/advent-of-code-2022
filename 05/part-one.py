import collections

input = open("input.txt", "r").read()

lines = input.splitlines()

stacks = []

getting_starting_position = True


for line in lines:
    if getting_starting_position:
        if line == "":
            getting_starting_position = False
            continue
        if len(stacks) == 0:
            for i in range(0, int(len(line)/4) + 1):
                stacks.append(collections.deque())
        stack_counter = 0
        while len(line) >= 3:
            this_stack = line[:3]
            line = line[4:]
            if this_stack[1].isalpha():
                stacks[stack_counter].appendleft(this_stack[1])
            stack_counter += 1
    else:
        instructions = line.split(" ")
        num_to_move = int(instructions[1])
        from_stack = int(instructions[3]) - 1
        to_stack = int(instructions[5]) - 1

        for i in range(0, num_to_move):
            stacks[to_stack].append(stacks[from_stack].pop())

answer = ''
for stack in stacks:
    answer += stack[-1]
print(answer)
