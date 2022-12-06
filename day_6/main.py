filename = "input.txt"

file = open(filename, "r").read()

def all_unique(chars):
    for c in chars:
        if chars.count(c) != 1:
            return False
    return True

chars = file[:14]
counter = 14

while not all_unique(chars):
    chars = chars[1:] + file[counter]
    counter += 1

print(counter, chars)



