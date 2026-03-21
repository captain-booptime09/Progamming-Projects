maze_pattern = [["#","#","#","#","#","#","#","#","#","#","#","#","#","#",".","#","#","#","#","#","#","#"],
                ["#",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","#"],
                ["#","#","#","#","#","#","#","#","#",".","#","#","#","#","#","#","#","#","#","#",".","#"],
                ["#",".",".",".",".",".",".",".","#",".","#",".",".","#",".","#","#",".",".",".",".","#"],
                ["#",".","#",".","#","#",".","#","#",".","#","#",".","#",".","#","#",".","#","#","#","#"],
                ["#",".","#",".","#",".",".",".","#",".",".",".",".","#",".","#","#",".","#","#","#","#"],
                ["#",".","#",".","#",".","#","#","#","#","#",".","#","#",".","#","#",".",".",".",".","#"],
                ["#",".","#",".","#",".","#",".",".",".","#",".",".","#",".","#","#","#","#","#",".","#"],
                ["#",".","#",".","#",".","#",".","#",".","#","#",".","#",".",".",".",".",".",".",".","#"],
                ["#",".","#",".","#",".","#",".","#",".",".","#",".","#",".","#","#","#","#","#",".","#"],
                ["#",".","#",".","#",".","#",".","#","#",".","#",".","#",".","#",".",".",".",".",".","#"],
                ["#",".","#",".","#",".","#",".",".","#",".","#",".","#",".","#",".","#","#","#","#","#"],
                ["#",".","#",".","#",".","#","#",".","#",".","#",".","#",".","#",".",".",".",".",".","#"],
                ["#","#","#",".","#",".","#","#",".","#",".","#",".","#",".","#","#","#","#",".","#","#"],
                [".",".","#",".","#",".","#","#",".","#",".","#",".","#",".","#","#",".","#",".","#","#"],
                ["#",".","#",".","#",".","#","#",".","#",".","#",".","#","#","#","#",".",".",".","#","#"],
                ["#",".",".",".","#",".",".",".",".","#",".",".",".",".","#",".",".",".","#","#","#","#"],
                ["#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#"]]

# <<< Starting Position >>> #
y_pos = 0
x_pos = 14

# counter to measure the amount of attempts the algorithm takes to solve the maze #
count = 0

# condition to continue until maze is solved #
maze_solved = False

# continue searching to find the exist to the maze #
while maze_solved == False:

    # add maze marker #
    maze_pattern[y_pos][x_pos] = "@"

    print(" " * 40)

    # display maze pattern #
    for i in maze_pattern:
        print(i)

    # if y and x position are met then the exist is found and the maze is solved #
    if y_pos == 14 and x_pos == 0:

        # switch boolean variable to true to stop while loop #
        maze_solved = True
    
    # if y and x position are not met then continue to find exist #
    else:

        # increment attempt counter #
        count += 1

        # if position next to marker is '.' then proceed to that position and replace previous position with '*'
        if maze_pattern[y_pos][x_pos + 1] == ".":
            x_pos += 1
            maze_pattern[y_pos][x_pos - 1] = "*"
        elif maze_pattern[y_pos][x_pos - 1] == ".":
            x_pos -= 1
            maze_pattern[y_pos][x_pos + 1] = "*"
        elif maze_pattern[y_pos + 1][x_pos] == ".":
            y_pos += 1
            maze_pattern[y_pos - 1][x_pos] = "*"
        elif maze_pattern[y_pos - 1][x_pos] == ".":
            y_pos -= 1
            maze_pattern[y_pos + 1][x_pos] = "*"
        
        # back track previous path to find new path and replace previous position with 'X'
        elif maze_pattern[y_pos][x_pos + 1] == "*":
            maze_pattern[y_pos][x_pos] = "X"
            x_pos = x_pos + 1
        elif maze_pattern[y_pos][x_pos - 1] == "*":
            maze_pattern[y_pos][x_pos] = "X"
            x_pos = x_pos - 1
        elif maze_pattern[y_pos + 1][x_pos] == "*":
            maze_pattern[y_pos][x_pos] = "X"
            y_pos = y_pos + 1
        elif maze_pattern[y_pos - 1][x_pos] == "*":
            maze_pattern[y_pos][x_pos] = "X"
            y_pos = y_pos - 1


# highlighting the correct route through the maze
outer_count = 0
while outer_count < len(maze_pattern):
    inner_count = 0
    while inner_count < len(maze_pattern[outer_count]):
        if maze_pattern[outer_count][inner_count] == "*":
            maze_pattern[outer_count][inner_count] = "$"
        inner_count += 1
    outer_count += 1

print(" " * 40)

for aa in maze_pattern:
    print(aa)

print(" " * 10)


# display total attempts
print(f"Completed in {count} attempts")
