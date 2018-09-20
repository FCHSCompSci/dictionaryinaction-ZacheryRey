# Zachery Reynolds
# Dictionary 09/17/18


# Imports
import time
import sys
import random



select_mission = [
    'Black Ops',
    'New World',
    'In Darkness',
    'Provocation',
    'Hypocenter',
    'Vengence',
    'Rise & Fall',
    'Demon Within',
    'Sand Castle',
    'Lotus Towers',
    'Life'
    ]





# Start
start = input("Welcome to Black Ops 3. Press 'f' to pay respec... I mean to start. ")
if start == 'f':
    time.sleep(1)
    print("*Ali A theme song*")
    time.sleep(3)


      
     
# Select
game = input("Would you like to access Campaign, Multiplayer, Zombies, or Bonus?")
if game == 'Campaign':
        camo = input("Would you like to start_game, join_public_game, select_mission, or change_difficulty? ")
        


# Start_Game
if camo == 'start_game':
    print("Starting game")
    time.sleep(2)
    print("Begin")

# Select_Mission
if camo == 'select_mission':
    print(select_mission)
    map_select = input("Which mission would you like to play?")
    if map_select == 'Black Ops':
        print("This is where it all begins, try not to get yourself killed.")
 
    
