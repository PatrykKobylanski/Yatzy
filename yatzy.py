import os
import random
import time

points = {"One": ["--","--"], "Two": ["--","--"], "Three": ["--","--"], "Four": ["--","--"], "Five": ["--","--"], "Six": ["--","--"], "Bouns": ["00","00"], "3  of a  kind": ["--","--"], "4  of a  kind": ["--","--"], "Full house": ["--","--"], "Small Strit": ["--","--"], "Big strit": ["--","--"], "Chance": ["--","--"], "Yatzy": ["--","--"]}
names = ["One", "Two", "Three", "Four", "Five", "Six", "Bouns", "3  of a  kind", "4  of a  kind", "Full house", "Small Strit", "Big strit", "Chance", "Yatzy"]
dices = [
    ['+-------+', '|       |', '|   *   |', '|       |', '+-------+'], ['+-------+', '|*      |', '|       |', '|      *|', '+-------+'], ['+-------+', '|*      |', '|   *   |', '|      *|', '+-------+'], ['+-------+', '|*     *|', '|       |', '|*     *|', '+-------+'], ['+-------+', '|*     *|', '|   *   |', '|*     *|', '+-------+'], ['+-------+', '|*     *|', '|*     *|', '|*     *|', '+-------+'] ]

def display_table(ammount_of_players):
    
    os.system('cls')

    if ammount_of_players == 2:

        print("+----------------------------------------+                   +----------------------------------------+")
        print("|                Player 1                |                   |                  Player 2              |")
        print("+----------------------------------------+                   +----------------------------------------+")
        for index, value in enumerate(points):
            if index <= 6:
                print("|" + " (" + str(index+1) +") " + names[index] + " "*(5-len(value)) + "| " + readable_output_of_the_points(str(points[names[index]][0]), 2) + " |" + " (" + str(index+8) +") "+ str(names[index+7])  + " "*(12-len(str(names[index+7]))) + " | " +  readable_output_of_the_points(str(points[names[index+7]][0]),2) +" |                   "+ "|"+
                      " (" + str(index+1) +") " + names[index] + " "*(5-len(value)) + "| " + readable_output_of_the_points(str(points[names[index]][1]), 2) + " |" + " (" + str(index+8) +") "+ str(names[index+7])  + " "*(12-len(str(names[index+7]))) + " | " +  readable_output_of_the_points(str(points[names[index+7]][1]),2) +" |")
                print("+----------+----+-------------------+----+                   +----------+----+-------------------+----+")
            else:

                sum_of_points_for_players = [0,0]

                for i in range(0,2):
                    for p in points.values():
                        if p[i] != "00" and p[i] != "--" :
                            sum_of_points_for_players[i]+=int(p[i])

                print("|           Sum of points : "+readable_output_of_the_points(str(sum_of_points_for_players[0]),3)+"          |                   "+"|           Sum of points : "+readable_output_of_the_points(str(sum_of_points_for_players[1]),3)+"          |")
                print("+----------------------------------------+                   +----------------------------------------+")
                break
        
    else:

        print("+----------------------------------------+")
        print("|               Solo mode                |")
        print("+----------+----+-------------------+----+")
        for index, value in enumerate(points):
            if index <= 6:
                print("|" + " (" + str(index+1) +") " + names[index] + " "*(5-len(value)) + "| " + readable_output_of_the_points(str(points[names[index]][0]), 2) + " |" + " (" + str(index+8) +") "+ str(names[index+7])  + " "*(12-len(str(names[index+7]))) + " | " +  readable_output_of_the_points(str(points[names[index+7]][0]),2) +" |")
                print("+----------+----+-------------------+----+")
            else:

                sum_of_points = 0
                for p in points.values():
                    if p[0] != "00" and p[0] != "--" :
                        sum_of_points+=int(p[0])

                print("|           Sum of points : "+readable_output_of_the_points(str(sum_of_points),3)+"          |")
                print("+----------------------------------------+")
                break

#readable_output_of_the_points 
def readable_output_of_the_points(points, goal_len):
    if points == "--":
        return "--"
    else:
        if len(points) == goal_len:
            return points
        else:
            r_points = points[::-1]
            while len(r_points) < goal_len:
                r_points +=  "0"

            return r_points[::-1]

def check_if_int(given):
    arr = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14"]
    while given not in arr:
        print('"'+ str(given)+'"' + " is an incorrect input")
        given = input("Type correct input: ")
    
    return int(given)

def check_if_repeats(given):

    for i in range(1,7):
        check = 0
        for number in given:
            if number == ',':
                continue
            else:
                if number == i:
                    check+=1
        
        if check > 1:
            return True
   
    return False
                
def roll_dices(ammount_of_players, player, round, rolled_dices, chances):
    if ammount_of_players == 1:
        if round == 14:
            print("Game over")
            exit()
    else:
        if round == 27:
            print("Game over")
            exit()

    print("Round " + str(round))
    print("Player " + str(player) + " trun")

    if chances == 2 and rolled_dices == []:
        
        for _ in range(0,5):
            rn = random.randint(1,6)
            rolled_dices.append(rn)

        display_dices(rolled_dices)
    
    if  chances > 0 and chances <= 2:    
        which_to_change = str(input("Which dice/dices do you want to change('2', '2,3,5', 'all'): "))

        # change all
        if which_to_change =="all":
            for index in range(0, len(rolled_dices)):
                rn = random.randint(1,6)
                rolled_dices[index] = rn
            
            display_table(ammount_of_players)
            display_dices(rolled_dices)
            roll_dices(ammount_of_players, player, round, rolled_dices, chances-1)

        # exact change
        elif which_to_change !="all" and which_to_change != "":
            
            to_check = ((" ").join(which_to_change)).split()

            check_len = 0
            for item in to_check:
                if item != ",":
                    check_len+=1


            if check_len > 5:
                print("You can change max 5 items at one time.")
                time.sleep(2.0)
                display_table(ammount_of_players)
                display_dices(rolled_dices)
                roll_dices(ammount_of_players, player, round, rolled_dices, chances)
            
            for num_to_check in range(0,len(to_check)):
                if to_check[num_to_check] != ',':
                    checking = int(check_if_int(to_check[num_to_check]))
                    
                    while checking < 1 or checking > 5:
                        print('"'+ str(checking)+'"' + " is an incorrect input")
                        checking = check_if_int(input("Dice to change:"))

                    to_check[num_to_check] = int(checking)

            if check_if_repeats(to_check) == True:
                print("Some of numbers repeat. Try again.")
                time.sleep(1.5)
                display_table(ammount_of_players)
                display_dices(rolled_dices)
                roll_dices(ammount_of_players, player, round, rolled_dices, chances)

            for index in to_check:
                if index != ',':
                    rn = random.randint(1,6)
                    rolled_dices[(int(index))-1] = rn

            display_table(ammount_of_players)
            display_dices(rolled_dices)
            roll_dices(ammount_of_players, player, round, rolled_dices, chances-1)

        # no change
        elif which_to_change == "":
            chances = 0

    if chances == 0:
        print("Time to assign points.")
        print()
        analyze_and_chose_points(ammount_of_players, player, round, rolled_dices)



def analyze_and_chose_points(ammount_of_players, player, round, dices ):

    temporary_points = {"One": 0, "Two": 0, "Three": 0, "Four":0, "Five": 0, "Six":0, "Bouns": "-", "3  of a  kind": 0, "4  of a  kind": 0, "Full house": 0, "Small Strit": 0, "Big strit":0, "Chance": 0, "Yatzy":0}

    dices.sort()
    sum_of_points = sum(dices)

    # summing up the points
    for each_point in dices:
        if each_point == 1:
            temporary_points['One'] +=1
        
        if each_point == 2:
            temporary_points['Two'] +=2

        if each_point == 3:
            temporary_points['Three'] +=3

        if each_point == 4:
            temporary_points['Four'] +=4
        
        if each_point == 5:
            temporary_points['Five'] +=5

        if each_point == 6:
            temporary_points['Six'] +=6

    # 3 of pair, 4 of pair, full, yatzy,chance
    for point in range(1,7):
        counter = 0
        for each_point in dices:
            if each_point == point:
                counter+=1
            
        if counter >= 3:
            temporary_points["3  of a  kind"] += sum_of_points
            print("3 of pair " + str(sum_of_points) + " points !") 
            if counter == 3:
                for sec_point in range(1,7):
                    sec_counter = 0  
                    if sec_point == point:
                        continue
                    for each_point in dices:
                        if each_point == sec_point:
                            sec_counter+=1
                    
                    if sec_counter == 2:
                        temporary_points["Full house"] += 25
                        print("Full house 25 points !" )

        if counter >=4:
            temporary_points["4  of a  kind"] += sum_of_points
            print("4 of pair " + str(sum_of_points) + " points !") 

        if counter == 5:
            temporary_points["Yatzy"] += 50
            print("Yatzy 50 points !")

    # small strit, big strit
    to_compare = []
    for each in dices:
        if each not in to_compare:
            to_compare.append(each)

    if to_compare[0:4] == [1,2,3,4] or to_compare[0:4] == [2,3,4,5] or to_compare[0:4] == [3,4,5,6]:
        temporary_points["Small Strit"] += 30
        print("Small strit 30 points !")

    if to_compare == [1,2,3,4,5] or to_compare == [2,3,4,5,6]:
        temporary_points["Big strit"] += 40
        print("Big strit 40 points !")

    # chance 
    temporary_points["Chance"] = sum_of_points

    # print(temporary_points)
    space_counter = 0
    part = ""

    print()
    for name, point in temporary_points.items():
        space_counter+=1
        if space_counter != 7:
            part += "(" + str(space_counter) + ")" +str(name)+"': " + str(point) + "  "
            if space_counter % 3 == 0:
                print(part)
                part = ""

    print()
    choice = check_if_int(input("Chose position to assign points from 1 to 14: "))
    while choice == 7 or points[names[choice-1]][player-1] != "--":
        print("Given possition can't be chosen. Please select other position.")
        choice = check_if_int(input("Chose position to assign points from 1 to 14: "))
        
    points[names[choice-1]][player-1] = temporary_points[names[choice-1]]
    
    #bonus check 
    if points["Bouns"][player-1] == "00":
        control_sum = 0
        for k in range(0,6):
            if points[names[k]][player-1] != "--":
                control_sum+= points[names[k]][player-1]
        
            if control_sum >= 63:
                points["Bouns"][player-1] = 35

    if ammount_of_players == 2:
        display_table(2)
        if player == 1:
            roll_dices(2,2,round+1,[],2)
        else:
            roll_dices(2,1,round+1,[],2)

    else:
        display_table(1)
        roll_dices(1,1,round+1,[],2)

def display_dices(rolled_dices):
    # print(rolled_dices)
    for i in range(0, len(rolled_dices)):
        part  = ""
        for x in range(0,5):
            part = part + dices[rolled_dices[x]-1][i] 
            part = part + "  "

        print(part)
    
# how many players
ammount_of_players = check_if_int(input("1 or 2 players: "))

while ammount_of_players < 1 or ammount_of_players > 2:
    print('"'+ str(ammount_of_players)+'"' + " is an incorrect input")
    ammount_of_players = check_if_int(input("1 or 2 players: "))

# start of the game
display_table(ammount_of_players)
roll_dices(ammount_of_players, 1, 1, [], 2)
