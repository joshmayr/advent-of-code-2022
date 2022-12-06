input = open("input.txt", "r").read()

for i in range(0, len(input)-3):
    four_digits = input[i:i+4]
    flag = len(set(four_digits)) == len(four_digits)
    if flag == True:
        print(i+4)
        break
