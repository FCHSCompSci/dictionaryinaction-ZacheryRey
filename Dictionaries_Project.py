# Zachery Reynolds
# Dictionary 09/17/18


# Imports
import time
import sys
import random



difficulties = ['Regular', 'Recruit', 'Hardened', 'Veteran']

user_profile = {
    'username' : "" ,
    'rank' : "" ,
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
start = input("Welcome to Black Ops 3 Campaign. Press 'f' to pay respec... I mean to start. ")
if start == 'f':
    time.sleep(1)
    print("*Ali A theme song*")
    time.sleep(1)

# Name/Rnk
user_profile["username"] = input("Please enter your username. ")
time.sleep(1)
user_profile["rank"] = input("What is your Rank? ")


while True: 
     
# Select
    camo = input("Would you like to start_game(s), join_public_game(j), select_mission(m), or change_difficulty(d)? You can also enter yeet to show your gamertag and rank. ")



# CAMPAIGN
    if camo == 'yeet':
        for val in user_profile.values():
            print(val)
        
    # Start_Game
        if camo == 's':
            print("Starting game")
            time.sleep(2)
            print("Try not to die too fast.")
            break
           

    # Join Game
        if camo == 'j':
            print("Loading into game")
            time.sleep(1)
            print("Please wait")
            time.sleep(3)
            print("You may begin")

    #Change Difficulty
        if camo == 'd':
            print (difficulties)
            dif = input("What difficulty setting would you like to play on? ")
            if dif == 'Regular':
                print("You may begin*whispers* noob. ")
            elif dif == 'Recruit':
                print("YOU'RE JUST LIKE YOUR FATHER... Bigin. ")
            elif dif == 'Hardened':
                print("That's a little more like it. ")
            elif dif == 'Veteran':
                print("Now you're really a man. You're gonna die. ")

        
        
    # Select_Mission                                                  
        if camo == 'm':
            for val in select_mission.values():
                print(val)
            map_select = input("Which mission would you like to play? ")
            if map_select == 'Black Ops':
                print("Alongside a team of Winslow Accord Cyber Soldiers, Infiltrate teh NRC airfield in Ethiopia and secure the captured Egyptian Minister for extraction. ")
            elif map_select == 'New World':
                print("Undergo surgery, rehabilitation adn training for potentian indiction into the Winslow Accord Cyber Soldier program. Success is not guarenteed. ")
            elif map_select == 'In Darkness':
                print("Five years later. In cooperation with CIA. Investigate the sudden silence of a CIA Black Staion in Singapore Quarantine Zone - established in the wake of the disaster that killed 300,000 people. ")
            elif map_select == 'Provocation':
                print("Posing as arms dealers, infiltrate the headquarters of The 54 Immortals - The Quarantine Zone's dominant criimnal faction, in order to recover the Black Station's stolen Data drives.")
            elif map_select == 'Hypocenter':
                print("Investigate the Coalescence Corporation facility - Ground Zero of the Singapore disaster - in search of an explanation for your former allie's betrayal.")
            elif map_select == 'Vengence':
                print("Disobey a direct order - amd move to prevent the 54 Immortals from overrunnung the CIA safe house, in order to secure LNO  Kane for extraction.")
            elif map_select == 'Rise & Fall':
                print("Proceed to Ramses Station - last stronghold of the beleaguered Egyption army and interrodate Dr. Salim - one of teh survuvors of the Singapore Disaster.")
            elif map_select == 'Demon Within':
                print("Cut of from WA command, fight alongside the Egyptian army as you pursue the three remaining targets to Kebechet - the lost city.")
            elif map_select == 'Sand Castle':
                print("A joint operation with the Egyption Army, launch an air assult on the aquifer drilling platform - suspected location of the two remaining targets.")
            elif map_select == 'Lotus Tower':
                print("Together with the Egyptian army and the civilian militia - Overthrow the NRC domination of Lotus Towers and secure the final target.")
            elif map_select == 'Life':
                print("Head to Zurchi headquarters of Coalescence in order to prevent the further spread of the ONI infectio...")

        over = input("Enter 'x' to end. Enter any other key to go back to the beggining.")
        if over == 'x':
            break


            
         
            
