filename = "input.txt"

file = open(filename, "r").readlines()
total = 0
for line in file:
    line = line.replace("\n","").split(',')
    elf1, elf2 = line[0].split('-'), line[1].split('-')

    if (int(elf1[0]) <= int(elf2[0]) <= int(elf1[1])) or \
       (int(elf2[0]) <= int(elf1[0]) <= int(elf2[1])):
        total += 1
        print(elf1, elf2)
print(total)