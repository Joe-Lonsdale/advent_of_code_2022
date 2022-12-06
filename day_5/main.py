def fill_stacks():
    stacks=[['M','N','Z','W'],
            ['B','D','Z'],
            ['P','F','L','C','S','T','G'],
            ['J','V','T','W','M','N'],
            ['T','S','L','F','D','H','B'],
            ['Q','G','M','N','J','V','C','P'],
            ['C','B','S','N','W'],
            ['G','W','F','C','B','S','T','V'],
            ['V','C','D','R','Z','G','B','W']]
    stacks.reverse() # don't ask, i'm dumb
    return stacks

def main():
    filename = "input.txt"
    file = open(filename, "r")
    stacks = fill_stacks()
    for line in file:
        line = line.replace('\n', '')
        if len(line) == 0:
            continue
        if line[0] != 'm':
            continue
        else:
            line = line.split(" ")
            number, source, dest = int(line[1]), int(line[3])-1, int(line[5])-1

            temp = []

            for i in range(number):
                if len(stacks[source]) != 0:
                    popped = stacks[source].pop()
                    temp.append(popped)

            for i in range(number):
                stacks[dest].append(temp.pop())

    answer = ""
    for i in stacks:
        top = i.pop()
        answer += top

    print(answer)



if __name__ == "__main__":
    main()