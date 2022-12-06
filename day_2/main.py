filename = "input.txt"

file = open(filename, "r")

total_score = 0
rock_score, paper_score, scissors_score = 1, 2, 3
loss_score, draw_score, win_score = 0, 3, 6
lost, drew, won = ["A X", "B X", "C X"], ["A Y", "B Y", "C Y"], ["A Z", "B Z", "C Z"]

#           Lose  Win  Draw
#     Rock
#    Paper
# Scissors

need_to_play = [[3, 1, 2],
                [1, 2, 3],
                [2, 3, 1]]

for line in file:
    if len(line) > 2:
        if any(elem in line for elem in lost):
            total_score += loss_score
        elif any(elem in line for elem in drew):
            total_score += draw_score
        else:
            total_score += win_score
        total_score += need_to_play[ord(line[0])-65][ord(line[2]) - 88]

print(total_score)