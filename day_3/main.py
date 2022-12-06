filename = "input.txt"

file = open(filename, "r").readlines()

total_priorities = 0

# for line in file:
#     found = False
#     line=line.replace("\n","")
#     backpack_1, backpack_2 = line[:int(len(line)/2)], line[int(len(line)/2):]
#     for c in backpack_1:
#         if c in backpack_2 and not found:
#             found = True
#             print(c, backpack_1, backpack_2)
#             if c.isupper():
#                 total_priorities += ord(c) - 64 + 26
#                 print(ord(c) - 64 + 26)
#             else:
#                 total_priorities += ord(c) - 96
#                 print(ord(c) - 96)

x = 0
while x < len(file):
    l1 = file[x]
    x+=1
    l2 = file[x]
    x+=1
    l3 = file[x]
    x+=1

    found = False
    for c in l1:
        if c in l2 and c in l3 and not found:
            found = True
            if c.isupper():
                total_priorities += ord(c) - 64 + 26
                print(ord(c) - 64 + 26)
            else:
                total_priorities += ord(c) - 96
                print(ord(c) - 96)

print(total_priorities)