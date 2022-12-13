from functools import reduce
from math import floor


file = open("input.txt", "r").read()

file = file.split("\n\n")

items = []
operations = []
tests = []
jumps = []
inspects = []

for f in file:
    f = f.split("\n")
    for x in f:
        x = x.replace(":","").replace(",","").split(" ")
        for _ in range(x.count('')):
            x.remove('')
        if(x[0] == 'Monkey'):
            monkey = int(x[1])
            items.append([])
            jumps.append([[],[]])

        elif(x[0] == 'Starting'):
            for item in x[2:]:
                items[monkey].append(int(item))
        
        elif(x[0] == 'Operation'):
            op = ""
            for i in x[1:]:
                op += i
            operations.append(op)
        
        elif(x[0] == 'Test'):
            tests.append(int(x[3]))
        
        elif(x[1] == 'true'):
            jumps[monkey][0] = int(x[-1])
        
        else:
            jumps[monkey][1] = int(x[-1])
            inspects.append(0)

worry_level = 0

print(jumps)

common = reduce((lambda x, y: y*x), tests)

print(common)

# Run 20 rounds. 
# A round consists of each monkey inspecting each of their items, applying their operation to each item,
# Testing each item against their test, and either throwing to the 'True' or 'False' monkey.
for round in range(10000):
    for monkey in range(len(items)):
        #print(f"\nmonkey {monkey}")
        for item in items[monkey]:
            #print(items[monkey],item)
            new = 0
            old = item
            exec(operations[monkey])
            to_throw = new % common
            if(to_throw % tests[monkey] == 0):
                items[jumps[monkey][0]].append(to_throw)
                #print(f"{to_throw} thrown to monkey {jumps[monkey][0]}")
            else:
                items[jumps[monkey][1]].append(to_throw)
                #print(f"{to_throw} thrown to monkey {jumps[monkey][1]}")
            inspects[monkey] += 1
        items[monkey] = []
    if round%100 == 0:
        print(f"After round {round}: {inspects}")

m1 = max(inspects)
inspects.remove(m1)
m2 = max(inspects)

print(m1*m2)


