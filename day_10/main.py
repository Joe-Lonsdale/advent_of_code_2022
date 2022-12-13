from math import floor


file = open("input.txt", "r")

reg_x = 1
cycle = 1
CRT = [[],[],[],[],[],[]]

for line in file:
    row = floor((cycle-1)/40)
    print(row,cycle)
    line = line.replace("\n","")
    if line == "noop":
        op = "noop"
    else:
        op,num = line.replace("\n","").split(" ")
    if op == "noop":
        if (cycle-1)%40 in range(reg_x-1,reg_x+1):
            CRT[row].append('#')
        else:
            CRT[row].append('.')
        cycle += 1
    else:
        if (cycle-1)%40 in range(reg_x-1,reg_x+1):
            CRT[row].append('#')
        else:
            CRT[row].append('.')
        cycle += 1
        if (cycle-1)%40 in range(reg_x-1,reg_x+1):
            CRT[row].append('#')
        else:
            CRT[row].append('.')
        cycle += 1
        reg_x += int(num)

print(CRT)