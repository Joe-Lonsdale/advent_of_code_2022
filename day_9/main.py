import os

file = open("input.txt","r").readlines()

def make_grid(height, width, start_y, start_x):
	grid = []
	for i in range(height):
		grid.extend([['.']*width])
	grid[start_y][start_x] = '#'
	return(grid)

def dist(head,tail):
	if head[0] == tail[0] and head[1] == tail[1]:
		return 0
	if abs(head[0] - tail[0]) >= 2 or abs(head[1] - tail[1]) >= 2:
		return 2
	else: return 1

def update_pos(head, tail):
	new_pos = [0,0]
	if head[0] - tail[0] >= 1:
		new_pos[0] = tail[0] + 1
	elif head[0] - tail[0] <= -1:
		new_pos[0] = tail[0] - 1
	else:
		new_pos[0] = tail[0]

	if head[1] - tail[1] >= 1:
		new_pos[1] = tail[1] + 1
	elif head[1] - tail[1] <= -1:
		new_pos[1] = tail[1] - 1
	else:
		new_pos[1] = tail[1]
	return new_pos


# Calculate how big the grid needs to be to accommodate for the moves in the input.
curr_x=curr_y=max_x=max_y=min_x=min_y = 0
for line in file:
	dir_,num = line.replace("\n","").split(" ")
	if dir_ == "U":
		curr_y += int(num)
		if curr_y >= max_y:
			max_y = curr_y
	if dir_ == "D":
		curr_y -= int(num)
		if curr_y <= min_y:
			min_y = curr_y
	if dir_ == "R":
		curr_x += int(num)
		if curr_x >= max_x:
			max_x = curr_x
	if dir_ == "L":
		curr_x -= int(num)
		if curr_x <= min_x:
			min_x = curr_x

grid = make_grid(max_y-min_y+51,max_x-min_y+51,-min_y,-min_x)

knots = []
for k in range(10):
	knots.append([-min_x, -min_y])

first_move = [True]*10
for line in file:
	dir_,num = line.replace("\n","").split(" ")
	for _ in range(int(num)):
		if dir_ == "U":
			knots[0][1] += 1
		if dir_ == "D":
			knots[0][1] -= 1
		if dir_ == "R":
			knots[0][0] += 1
		if dir_ == "L":
			knots[0][0] -= 1
	
		for k in range(1,len(knots)):
				if dist(knots[k-1],knots[k]) == 2:
					knots[k] = update_pos(knots[k-1],knots[k])
				
		grid[knots[-1][1]][knots[-1][0]] = '#'
		first_move[0] = False
print(sum(i.count('#') for i in grid))