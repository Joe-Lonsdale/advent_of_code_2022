import numpy as np
import collections

filename = "input.txt"


file_string = open(filename, "r").read().replace("\n", "")
file_lines = open(filename, "r").readlines()

width = len(file_lines[0])-1
height = len(file_lines)

def main():
    arr = np.fromiter(file_string, dtype='int').reshape(width, height)
    count = 0
    max_score = 0
    for x in range(arr.shape[0]):
        for y in range(arr.shape[1]):
            if x == 0 or y == 0 or x == width-1 or y == height-1:
                continue
            north = arr[:y+1, x]
            east = arr[y, x:]
            south = arr[y:, x]
            west = arr[y, :x+1]
            # Part 1:
            # Check if max of each array is the current value to check against,
            # And check if this is the only occurrence of this value in the array
            # If so, this tree is visible from the edges

            # if np.max(north) == arr[y, x] and collections.Counter(north)[arr[y, x]] == 1:
            #     count += 1
            # elif np.max(south) == arr[y, x] and collections.Counter(south)[arr[y, x]] == 1:
            #     count += 1
            # elif np.max(east) == arr[y, x] and collections.Counter(east)[arr[y, x]] == 1:
            #     count += 1
            # elif np.max(west) == arr[y, x] and collections.Counter(west)[arr[y, x]] == 1:
            #     count += 1

            # Part 2:

            # Ensure first value of array is the position we are looking at
            north = np.flip(north)
            west = np.flip(west)
            directions = [north, east, south, west]

            # For each direction, calculate the viewing distance, and multiply together
            views = [1, 1, 1, 1]
            for dir_ in range(len(views)):
                # While there are trees smaller than the current position
                # and there is no edge, add 1 to viewing distance
                while directions[dir_][views[dir_]] < arr[y, x] and views[dir_] < directions[dir_].shape[0]-1:
                    views[dir_] += 1
            score = views[0] * views[1] * views[2] * views[3]
            if score > max_score:
                max_score = score

    print(max_score)


if __name__ == "__main__":
    main()



