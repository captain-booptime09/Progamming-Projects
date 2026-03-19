import random

grid_arr = [[0 for i in range(0,8)] for i in range(0,8)]
grid_arr1 = [[0 for i in range(0,8)] for i in range(0,8)]

ships = {"carrier":5, "battleship":4, "cruiser":3, "submarine":3, "destroyer":2} 

game_finished = False
game_prep = False
x = 0
y = 0
no_ships = 0
enemy_hits = 0
friendly_hits = 0

x_axis = ["0", "1", "2", "3", "4", "5", "6", "7"]
x_a_c = 0
while game_finished == False:
    
    print("    0  1  2  3  4  5  6  7")
    for g in grid_arr:
        print(x_axis[x_a_c], "", g)
        x_a_c += 1
    x_a_c = 0
    
    while game_prep == False:
        for s in ships:
            print("Ship: ", s, ships[s])
            ship_count = ships[s]
            while ship_count > 0:
                robot_plotx = random.randint(0,7)
                robot_ploty = random.randint(0,7)
                perm_robplot = robot_plotx
                grid_arr1[perm_robplot][robot_ploty] = 1
                xpos = int(input("Enter x coord(0,7): "))
                ypos = int(input("Enter y coord(0,7): "))
                grid_arr[xpos][ypos] = 1
                print("    0  1  2  3  4  5  6  7")
                for g in grid_arr:
                    print(x_axis[x_a_c], "", g)
                    x_a_c += 1
                x_a_c = 0
                ship_count = ship_count - 1
            no_ships += 1
        if no_ships == len(ships):
            game_prep = True
    
    print("YOUR SCORE: ", str(enemy_hits), "  ", "ENEMY SCORE: ", str(friendly_hits))
    
    robot_x = random.randint(0,7)
    robot_y = random.randint(0,7)
    
    if grid_arr[robot_x][robot_y] == 1:
        print("ROBOT HAS HIT")
        grid_arr[robot_x][robot_y] = 0
        friendly_hits += 1
    else:
        print("ROBOT HAS MISS")
        
    xps = int(input("Enter x coord(0,7): "))
    yps = int(input("Enter y coord(0,7): "))
    if grid_arr[xps][yps] == 1:
        print("YOU HAVE HIT")
        grid_arr[xps][yps] = 0
        enemy_hits += 1
    else:
        print("YOU HAVE MISS")
        
    if enemy_hits == 17:
        print("YOU WIN")
        game_finished = True
    if friendly_hits == 17:
        print("ROBOT WINS")
        game_finished = True