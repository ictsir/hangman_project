#Newton Chan command line game
#Assesment 1.45


#Dark 1.7
 



#    ___    ___   __  
#    |  \  | _ | | _\ ||//
#    | | | | _ | |  / | .
#    |__/  || || ||\\ ||\\ 1.7
#
#         /| _________________
#   O|===|* >________________/
#         \|
# 

#-----------------------------



#NOTES - FOR TESTING
#----------------------

#Enter 'test' when prompted for name to speed up game ticks
#Enter 'weak' "                    " to test death / hp regen sequence

#To test variables mid game, when prompted to 'attack or block' enter ']'
#this will stop the game so you can test variables

#Try the warrior named 'newton'








import random
import sys
import time

#Misc Variables
spacing = ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n") #Space text out
_time = 1                              #for testing pourposes (i can set to 0.1 to skip timers)
action = 0                              #For testing what the player does
action_2 = 0                            #Displaying actions and calculations
action_rpt = 0                          #testing for correct / incorrect inputs
action_list = ("blocks", "attacks","chugs an Hp potion")     #Names of actions
level = 1                               #level player is currently on
start = 0                               #test for when player starts a level
level_loop = 0                          #How many enemies appear on a level
room = 0                                #wether its a treasure room or not
enemies_killed = 0                      #Counts how many enemies player has defeated

dark_text = ("     ___    ___   __  \n     |  \  | _ | | _\ ||//\n     | | | | _ | |  / | .\n     |__/  || || ||\\\\ ||\\\\ 1.7\n\n         /| _________________\n   O|===|* >________________/\n         \|\n--------------------------------- ")


#player related variables

hp = 100         #Players hit points
hp_bottle = 3   #how many Hp potions player has
player_atk = 0  #Players final attack value
name = 0        #Stores player / character name
max_hp = 150


#enemy related variables

enemy_atk = 0       #Final attack value of the enemy
enemy = 0           #Stores which enemy is present 
enemies = ("Null",
           "Rat",
           "Crab",
           "Python",
           "Bat",
           "Flea",
           "Missing.no"
           ) #List of enemy names 
enemy_art = ("Null", #Place holder
             "        _ _\n       (_(_)_\n       / ''_>O<\n__    / __ \ \n  \__(_/__| |", #Rat art
             "V ._. V\n\(___)/\n // \\)", #crab art
             "            -º__\n           /.--'\n.      ___//\n''. _ (____)\n '.i_(______)", #Snake
             "  /\ |\___/| /\ \n ///\| > < |/\\\\\\   \n/////|  _  |\\\\\\\\\ \n|////|     |\\\\\\\\|\n|/_//|     |\\\\_\|\n\/ \/|_____|\/ \/\n      ^   ^",
             ".",
             "#s@^C_+\n+$%^&*(\n#$(57@$\n@*%#412\n#*(#!DR"
             
             )
enemy_hp = 0 #Enemy hit points
enemy_count = len(enemies) - 1 #Modular variable and allows easy additions of new enemies 

#Weapon variables
weapon = 1 #Which weapon player currently posseses 
weapon_base = 1 #Base damage of weapon, pre calculation
weapon_bonus = 0 #Bonus damage of weapon, added after calculation
weapon_name = ("Null", #Names of each weapon
               "Rusty sword", 
               "Iron sword",
               "Paladins sword",
               "Double ended sword",
               "Broad sword",
               "developers_sword"
               )
weapon_art = ("Null",
              "o--(=======>", #Rusty sword
              "     /\nOsss(============-\n     \ ", #Iron sword
              "   ^\n  |!|\n  |!|\n  |!|\n  |!|\n  |!|\n  |!|\n  |!|\n  |!|\n\_|!|_/\n  \!/\n   x\n   x\n   x\n   V ",#Paladins sword
              "           \   /\n<___________xxx__________>\n           /   \ ", #double ended sword
              "      /| __________________\nO|===|* >________________/\n      \|", #Broad sword
              "c==(D-E-V-E-L-O-P-E-R_S-W-O-R-D>"#Dev sword
              ) 
weapon_count = len(weapon_name) - 2 #Modular variable, allows easy addition of new swords







#START

print ("Whats the name of your soon to be glorious warrior?")
name = input("> ") #asks player for name

time.sleep (_time * 0.5)


print ("{}, the best of all names, im sure this warrior will live long!".format(name)) 

if name == 'test':
    _time = 0.1
    
elif name == 'weak':
    hp = 1
    weapon_base = 0
    
elif name == 'newton':
    hp = 10000*10000
    weapon_base = 100000*10000*10000000
    weapon_bonus = 100000*1000000*10000000
    weapon = 6
    max_hp = 1000000000000000000000000

    

print (spacing)
time.sleep (_time * 2)
print ("")

print (dark_text) #Fancy title
print ("    *Play in full screen*")

for i in range (15):
    
    print ("\n")
    time.sleep (_time * 0.05) #Fancy title scrolls up

time.sleep (_time * 2)

for i in range (10):
    print ("\n")
    time.sleep (_time * 0.03) #Fancy title scrolls off screen 

while True:

    hp = round(hp, 2)
    
    #displaying iformation for player
    print (weapon_art [weapon])
    print (weapon_name [weapon])
    print ("___________________________________________________")
    print ("Weapon base damage:{} ".format(weapon_base))
    print ("Weapon bonus damage: (+{})".format(weapon_bonus))
    print ("Hp potions: {}".format(hp_bottle))
    print ("___________________________________________________")
    print ("{}'s HP {}/{}".format(name, hp,max_hp))
    print ("Level: {}".format(level))
    print ("___________________________________________________")
    print("press enter to start")
    print (spacing)

    
    start = input("")

    if start == "":
    

        print ("___________________________________________________")


        #Choosing random room
        room = random.randrange(1,5)

        if room >= 2:


            #Fighting sequence start
            level += 1
            level_loop = random.randint (1,3)

            for x in range(level_loop):

            
                enemy_hp = level*(level * random.randint(1,3)) #Assigning hp values to enemy
                enemy = random.randint(1,enemy_count) #Selecting random enemy

                time.sleep (_time * 1)

                while enemy_hp >= 1: #Dectecting enemy hp 

                    action_rpt = 0
                
                    while action_rpt == 0:

                        #Displaying enemy info
                    
                        print (enemy_art[enemy])
                        print ("")
                        print (enemies[enemy])
                        print ("Enemy HP:{}".format(enemy_hp))
                        print ("-----------------------------------")
                        print ("Your HP: {}/{}".format(hp,max_hp))
                        print ("Health potions: {}".format(hp_bottle))
                        print ("-----------------------------------")
                        print ("a) Attack")
                        print ("b) Block")
                        print ("h) Drink Hp potion")
                        print ("-----------------------------------")
                        print (spacing)
                    
                        action = 0
                        action = input("> ")
                        action = action.strip() #changes all inputs to be lower case\
        
                        if action == 'a':

                            #Player attacks
                            action_2 = 1
                            action_rpt = 1
    

                        elif action == 'b':

                            #Player blocks
                            action_2 = 0
                            action_rpt = 1

                    
                        elif action == 'h':

                            #Player drinks hp potion
                            if hp_bottle > 0:

                                #Player drinks
                                hp += 50
                                hp_bottle -= 1
                                action_rpt = 1
                                
                                if hp >= max_hp: #Testing for if hp is greater than maximum hp
                                    hp = max_hp #if true set hp to max hp
                            
                                print ("{} guzzles a health potion".format(name))
                                print ("+50 HP")
                            else:
                                #Player doesnt have any left
                                print ("{} doesnt have any left :(".format(name))
                                print (spacing)
                                
                                action_rpt = 0
                            

                            action_2 = 2
                       
                            
                        

                        elif action == ']':
    
                            #Enable developer console
                            print ("Dev console enabled, Welcome, Newton.")
                            sys.exit("Accessed command console")
                        
                
                        else:
    
                            #player enters wrong input 
                            print ("thats not an action, matey")
                            print (spacing)

                            time.sleep (_time * 1)
    
                    #Player attacks
                        
    
                    print ("")
                    print ("{} {}".format(name, action_list[action_2]))

                    action_rpt = 1

                    if action_2 == 1:
                        player_atk = (random.randint(1,4) * weapon_base * 3 + weapon_bonus) #Calculating Player atk
                    elif action_2 == 0 or 2:
                        player_atk = 0
                

                    print ("{} deals {} damage!".format(name, player_atk))

                    enemy_hp -= player_atk #Setting new player hp value
                   
                    print ("{} hp: {}".format(enemies[enemy], enemy_hp))
                    print ("\n\n\n\n\n\n\n" + spacing) #Spacing out text
                
                    time.sleep (_time * 2)

                    if action_2 == 1:
                       enemy_atk = level * random.randint(1,10) #Calculating enemy atk when not blocking
                    elif action_2 == 0 or 2:
                        enemy_atk = level * random.randint(1,5) * 0.3 #Calculating enemy atk when blocked
                

                    if enemy_hp >= 1:
    
                    
                        #Enemies attack sequence
                        print ("{} attacks!".format(enemies[enemy]))

                        time.sleep (_time * 1)
                        enemy_atk = round(enemy_atk,2)

                        print ("{} deals {} damage to {}!".format(enemies[enemy], enemy_atk, name))

                        hp -= enemy_atk #Setting hp to new vaule 
                        time.sleep (_time * 1)

                        if hp <= 0:
                            hp = 0
                    
                        print ("")
                        print ("{}'s HP:{}/{}".format(name,hp,max_hp))
                        print (spacing + "\n\n\n\n\n\n")
                        time.sleep (_time * 2)
                    
                        if hp <= 0: #Dectecting if the player 
                        

                            print ("{} takes a hard blow to the head, and crumples to the ground lifeless.".format(name))
                            print ("_________________________________")

                            print (name)
                            print ("Defeated by: {}".format(enemies[enemy]))
                            print ("Enemies killed: {}".format(enemies_killed))
                            print ("Died on level: {}".format(level))
                            for i in range (30):
                                print ("")
                                time.sleep(_time * 0.05)

                            time.sleep (_time * 10)

                            print (spacing)
                            print ("")

                            print (dark_text) #Fancy title

                            for i in range (15):
    
                                print ("\n")
                                time.sleep (_time * 0.05) #Fancy title scrolls up

                            time.sleep (10)


                        

                            sys.exit("Game over, matey")
                                                
                        

                action_rpt = 0

                print ("{} defeated {}!".format (name, enemies[enemy]))

                enemies_killed += 1
    
                print (spacing+"\n\n\n\n\n\n\n\n\n\n")
                time.sleep (_time * 2)

            

        else:

            #Treasure room- Generating random stats for new weapon
        
            weapon_rnd = random.randrange(2,weapon_count)  #Selects random weapon from list weapon
            weapon_name_rnd = weapon_name[weapon_rnd] #Assigns weapon name
            weapon_art_rnd = weapon_art[weapon_rnd] #Assigns weapon art 

            weapon_bonus_rnd = random.randint(1,level)+2 #Generating random bonus stat
            weapon_base_rnd = random.randint(level,level+2) #Generating random base stats


            action_rpt = 0

            while action_rpt == 0:
                #Displaying random weapon to player
                print ("You find a {}!".format(weapon_name_rnd))
                print (weapon_art_rnd)
                print ("Base damage: {}".format(weapon_base_rnd))
                print ("Bonus damage: {}".format(weapon_bonus_rnd))
                print ("Current damage:{}".format(weapon_base))
                print ("Current bonus: {}".format(weapon_bonus))
                print ("________________________________________________________________________")
                print ("Press 't' to take the sword, or 'l' to leave it")
                
                print (spacing)

                #Asks player 
                action = input("> ")
                action = action.strip()
                
                print (spacing)
            

                if action == 't':
             
                    #Player picks up new weapon
                    print ("{} picks up the new sword".format(name))

                    weapon = weapon_rnd              #Setting 'picked up' weapons variables to main weapon variables
                    weapon_base = weapon_base_rnd
                    weapon_bonus = weapon_bonus_rnd
                    action_rpt = 1

                elif action == 'l':
                    #Player doesnt pick up weapon
                    print ("{} leaves the inferior sword".format(name))
                    action_rpt = 1

                else:
                    action_rpt = 0
                    

            time.sleep (_time * 1.5)

            #Increasing health
            print ("")
            print("{} finds a magical potion of health, and quickly chugs it".format(name))

            time.sleep (_time * 1)
            hp_bottle += random.randrange (1,3)

            print("")
            print("{} picks up a couple more hp potions and stuffs them into a bag".format(name))
            print("Hp potions:{}".format(hp_bottle))
        
            print (spacing)

            time.sleep (_time * 2)
            hp = hp * 1.3 #Increasing player's hp

            if hp > max_hp: #Sets hp to 100 if its past max hp 
                hp = max_hp
