# Zachery Reynolds
# Dictionary 09/17/18


# Imports
import time
import sys
import random


while True:
difficulties = ['Regular', 'Recruit', 'Hardened', 'Veteran']

user_profile = {
    'username' : "default",
    'rank' : "default",
    }


black_ops = 'Black Ops'
new_world = 'New World'
in_darkness = 'In Darkness'
provocation = 'Provocation'
hypocenter = 'Hypocnter'
vengence = 'Vengence'
rise_and_fall = 'Rise & Fall'
demon_within = 'Demon Within'
sand_castle = 'Sand Castle'
lotus_tower = 'Lotus Tower'
life = 'Life'


select_mission = {
    'black_ops':black_ops,
    'new_world':new_world,
    'in_darkness':in_darkness,
    'provocation':provocation,
    'hypocenter':hypocenter,
    'vengence':vengence,
    'rise_and_fall':rise_and_fall,
    'demon_within':demon_within,
    'sand_castle':sand_castle,
    'lotus_towers':lotus_tower,
    'life' : life,
    }
   






# Start
start = input("Welcome to Black Ops 3. Press 'f' to pay respec... I mean to start. ")
if start == 'f':
    time.sleep(1)
    print("*Ali A theme song*")
    time.sleep(3)

user = input("Please enter your username")
time.sleep(2)
ran = input("What is your Rank?")


      
     
# Select
game = input("Would you like to access Campaign, Multiplayer, Zombies, or Bonus?")
if game == 'Campaign':
        camo = input("Would you like to start_game, join_public_game, select_mission, or change_difficulty? ")
        


# Start_Game
if camo == 'start_game':
    print("Starting game")
    time.sleep(2)
    print("Begin")

# Join Game
if camo == 'join_public_game':
    print("Loading into game")
    time.sleep(1)
    print("Please wait")
    time.sleep(3)
    print("You may begin")

#Change Difficulty
if camo == 'change_difficulty':
    print (difficulties)
    dif = input("What difficulty setting would you like to play on?")
    if dif == 'Regular':
        print("You may begin*whispers* noob. ")
    elif dif == 'Recruit':
        print("YOU'RE JUST LIKE YOUR FATHER... Bigin. ")
    elif dif == 'Hardened':
        print("That's a little more like it. ")
    elif dif == 'Veteran':
        print("Now you're really a man. You're gonna die. ")
    
    
    
    




    
    
# Select_Mission                                                    # INSERT PRINTS!!!!!!!!!!!!!!!!!!!!!!!!!
if camo == 'select_mission':
    for val in select_mission.values():
        print(val)
    map_select = input("Which mission would you like to play?")
    if map_select == 'Black Ops':
        print("This is where it all begins, try not to get yourself killed. ")
    elif map_select == 'New World':
        print("")
    elif map_select == 'In Darkness':
        print("")
    elif map_select == 'Provocation':
        print("")
    elif map_select == 'Hypocenter':
        print("")
    elif map_select == 'Vengence':
        print("")
    elif map_select == 'Rise & Fall':
        print("")
    elif map_select == 'Demon Within':
        print("")
    elif map_select == 'Sand Castle':
        print("")
    elif map_select == 'Lotus Tower':
        print("")
    elif map_select == 'Life':
        print("")


    
 
    
