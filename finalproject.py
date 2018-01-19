import random
inventory={'coins': 200, 'apples': 10}
#defines inventory with coins and apples
class Player(object):
    def __init__(self, hp, attack):
        self.hp=hp
        self.attack=attack
#creates a player class
player=Player(100, (7,13))
#makes an object in the class
def stats(self):
    print(f"Health: {self.hp}")
#makes a function to show the player's health

def attack(boss):
    boss.hp-=random.randint(7,13)
#makes an attack function for the player during battle

def heal(self):
    self.hp+=10
    inventory['apples']-=1
    print(f"Your hp is now {self.hp}. You have {inventory['apples']} apples left.")
#makes a heal function for the player during battle

class Resident(object):
    def __init__(self, name, bio, gift):
        self.name=name
        self.bio=bio
        self.gift=gift
#makes a class for people that the player encounter
socrates=Resident('Socrates', 'insert dialogue here', '15 coins')
cleopatra=Resident('Cleopatra', 'insert dialogue here', '15 coins')
ciacco=Resident('Ciacco', 'insert dialogue here', '15 coins')
avaricious=Resident('Avaricious', 'insert dialogue here', '15 coins')
filippo=Resident('Filippo Argenti', 'insert dialogue here', '15 coins')
epicurus=Resident('Epicurus', 'insert dialogue here', '15 coins')
alexander=Resident('Alexander the Great', 'insert dialogue here', '15 coins')
ulysses=Resident('Ulysses', 'insert dialogue here', '15 coins')
judas=Resident('Judas', 'insert dialogue here', '15 apples')
#makes 9 objects in the class (one for every level)

def introduce(self):
    print(f'Resident: "My name is {self.name}. {self.bio}. You have a long journey ahead-- take these."')
    print('---')
    print(f'You get {self.gift}.')
    inventory['coins']+=15
    print(inventory)
#makes a function giving the Resident something to say to the player and something to give them

class Boss(object):
    def __init__(self, name2, description, hp):
        self.name2=name2
        self.description=description
        self.hp=hp
#makes a boss class for the player to fight

charon=Boss('Charon', '', 50)
minos=Boss('Minos', '', 60)
cereberus=Boss('Cereberus', '', 70)
plutus=Boss('Plutus', '', 80)
phlegyas=Boss('Phlegyas', '', 90)
demon=Boss('Guard Demon', '', 100)
centaurus=Boss('Centaurus', '', 110)
geryon=Boss('Geryon', '', 120)
devil=Boss('Devil', '', 150)
#makes 9 bosses (one for each level)

def guard(self):
    print("You are close to the end. You see a gateway up ahead and a figure blocking the entrance.")
    print("---")
    print(f"{self.name2} guards the door to the next level.")
    print("---")
    print(f"{self.name2}: {self.description}")
    print(f'Hp: {self.hp}')
#gives the boss stats, makes them guard the doorway

def attack1(player):
    player.hp-=random.randint(7,13)

#makes each boss attack the player with different stats

class Level(object):
    def __init__(self, name3, level, description, position):
        self.name3=name3
        self.level=level
        self.description=description
        self.position=position
#makes a class for the 9 levels
one=Level('Limbo', 'Level 1', 'insert description here', 1)
two=Level('Lust', 'Level 2', 'insert description here', 2)
three=Level('Gluttony', 'Level 3', 'insert description here', 3)
four=Level('Greed', 'Level 4', 'insert description here', 4)
five=Level('Wrath', 'Level 5', 'insert description here', 5)
six=Level('Heresy', 'Level 6', 'insert description here', 6)
seven=Level('Violence', 'Level 7', 'insert description here', 7)
eight=Level('Malebolge', 'Level 8', 'insert description here', 8)
nine=Level('Treachery', 'Level 9', 'insert description here', 8)
#defines each of the levels as an object in the class

def enter(self):
    print(f"Enter {self.level}: {self.name3}")
#basically a title screen

funny={'one': 'As you walk, you approach a body of water. You peer over the edge to see what lurks below. Whoops. You slip into the River Acheron. You klutz.', 'two': '', 'three': '', 'four': '', 'five': '', 'six': '', 'seven': '', 'eight': '', 'nine':''}
#random intermission thing


###START GAME


print("You have fallen into Hell. Survive the nine levels to escape.")
print("---")
stats(player)
print(f"{inventory}")
print("Apples heal 10hp. Use them wisely.")
print('---')
#gives the player an objective, displays stats, explains apples

###LEVEL 1

def play_level(one):
#level function
    if player.hp<=0:
        player.hp=100
        charon.hp=50
    #if the player games over, they restart with full health
    enter(one)
    #prints title for level
    print(f"{one.description}")
    #prints level description
    print("---")
    print('To keep walking, press "w". To shop, press "s". If a resident of Hell approaches, press "t" to talk.')
    #game tutorial basically
    while True:
    #player has choices to progress in the game
        choice=(input('Continue walking ("w") or shop ("s")? ')).lower()
        #player can continue walking or shop based on what they input
        if choice=='s':
        #if player chooses to shop, they enter a while loop
            print("You have entered the shop.")
            print(inventory)
            #displays inventory
            print("5 coins for an apple.")
            while True:
                shop=input('Would you like to buy apples? y/n ').lower()
                #lets player choose to buy apples
                if shop=='y':
                    apple_amount=int((input('How many apples? # ')))
                    #player inputs an amount (integer)
                    if inventory['coins']>=apple_amount*5:
                    #tests if the player has enough money
                        inventory['apples']+=apple_amount
                        #increases player's amout of apples based on the number they chose to buy
                        inventory['coins']-=apple_amount*5
                        #inventory coins are taken away based on the number of apples
                        print(inventory)
                        print("You have exited the shop.")
                        break
                        #shows the inventory and leaves the shop by breaking out of the loop
                    else:
                        print("You don't have enough money.")
                        print("You have exited the shop.")
                        break
                    #if he/she doesn't have enough money, he/she breaks out of the loop

                elif shop=='n':
                    print("You have exited the shop.")
                    break
                    #breaks out of loop and leaves the shop if the character says no
                else:
                    print("Choose a valid response.")
        elif choice=='w':
            print("You keep walking.")
            break
            #same thing as before
        else:
            print("Choose a valid response.")

    print('---')
    print('As you walk, you see someone approaching in the distance.')
    #prints dialogue that lets player know there's someone to talk to
    while True:
        choice=(input('Talk ("t"), continue walking ("w") or shop ("s")? ')).lower()
        #now gives option to talk too
        if choice=='s':
        #same process/documentation as before
            print("You have entered the shop.")
            print(inventory)
            print("5 coins for an apple.")
            while True:
                shop=input('Would you like to buy apples? y/n ').lower()
                if shop=='y':
                    apple_amount=int((input('How many apples? # ')))
                    if inventory['coins']>=apple_amount*5:
                        inventory['apples']+=apple_amount
                        inventory['coins']-=apple_amount*5
                        print(inventory)
                        print("You have exited the shop.")
                        break
                    else:
                        print("You don't have enough money.")
                        print("You have exited the shop.")
                        break

                elif shop=='n':
                    print("You have exited the shop.")
                    break
                else:
                    print("Choose a valid response.")
            #same shopping loop
        elif choice=='w':
            #same process/documentation as before
            print("You keep walking.")
            break
        elif choice=='t':
            #lets the character talk to the Resident
                print("You choose to talk to the stranger.")
                print("---")
                introduce(socrates)
                #calls introduce function
                print("---")
                print("Socrates vanishes.")
                print('---')
                choice=(input('Continue walking ("w") or shop ("s")? ')).lower()
                if choice=='s':
                    print("You have entered the shop.")
                    print(inventory)
                    print("5 coins for an apple.")
                    while True:
                        shop=input('Would you like to buy apples? y/n ').lower()
                        if shop=='y':
                            apple_amount=int((input('How many apples? # ')))
                            if inventory['coins']>=apple_amount*5:
                                inventory['apples']+=apple_amount
                                inventory['coins']-=apple_amount*5
                                print(inventory)
                                print("You have exited the shop.")
                                break
                            else:
                                print("You don't have enough money.")
                                print("You have exited the shop.")
                                break

                        elif shop=='n':
                            print("You have exited the shop.")
                            break
                        else:
                            print("Choose a valid response.")

                elif choice=='w':
                    print("You keep walking.")
                    break
                else:
                    print("Choose a valid response.")
            #lets the character proceed after talking by going back to the original loop

    print('---')
    print(funny['one'])
    print('---')
    #prints the intermission

    while True:
        choice=(input('Continue walking ("w") or shop ("s")? ')).lower()
        if choice=='s':
            print("You have entered the shop.")
            print(inventory)
            print("5 coins for an apple.")
            while True:
                shop=input('Would you like to buy apples? y/n ').lower()
                if shop=='y':
                    apple_amount=int((input('How many apples? # ')))
                    if inventory['coins']>=apple_amount*5:
                        inventory['apples']+=apple_amount
                        inventory['coins']-=apple_amount*5
                        print(inventory)
                        print("You have exited the shop.")
                        break
                    else:
                        print("You don't have enough money.")
                        print("You have exited the shop.")
                        break

                elif shop=='n':
                    print("You have exited the shop.")
                    break
                else:
                    print("Choose a valid response.")
        elif choice=='w':
            print("You keep walking.")
            break
        else:
            print("Choose a valid response.")
    #all the same exact thing

    guard(charon)
    #calls guard function

    while True:
        if charon.hp<=0:
            print('---')
            print('Charon hp: 0')
            print('---')
            print("You've defeated the boss!")
            #game progresses if boss runs out of hp
            break
            #proceeds to the next level
        elif player.hp<=0:
            print('---')
            print("Your hp is 0. Game Over.")
            print('---')
            #Game over if player runs out of hp
            play_level(one)
            #calls function to restart the level
        elif player.hp>0 and charon.hp>0:
            print(f'Player: hp {player.hp}, Charon: hp {charon.hp}')
            print('---')
            while True:
                battle=input(("Attack ('a') or heal ('h')? ")).lower()
                #player can choose to attack or heal
                if battle=='a':
                #if player chooses to attack, he/she enters a while loop
                    print('---')
                    attack(charon)
                    #calls attack function
                    print(f"You attack {charon.name2}.")
                    print('---')
                    if charon.hp<0:
                        break
                        #if the character beats the boss, they proceed to the next level
                    else:
                        print(f'Player: {player.hp}, Charon: {charon.hp}')
                        #prints stats
                    attack1(player)
                    #calls attack function
                    print('---')
                    print('---')
                    print('Charon attacks you.')
                    print('---')
                    if player.hp<0:
                        break
                        #breaks out of the loop if player loses all his/her health
                    else:
                        print(f'Player: {player.hp}, Charon: {charon.hp}')
                        #prints stats
                        break
                        #breaks out of the loop
                elif battle=='h':
                #if player chooses to heal, the code enters a while loop
                    print('---')
                    while True:
                    #while loop so the player can eat an apple only if he/she has enough
                        if inventory['apples']>0:
                            print(f"You ate an apple.")
                            #has player eat apple if they have apples to eat
                            heal(player)
                            #calls heal function
                            print('---')
                            print(f'Player hp: {player.hp}, Charon hp: {charon.hp}')
                            #prints player and boss hp
                            print('---')
                            print('---')
                            break
                            #breaks out of the function
                        else:
                            print("You don't have any apples.")
                            print('--')
                            break
                        #if the player has no apples, this prints
                else:
                    print('---')
                    print("Choose a valid response.")
                    print('---')
                #if they type an invalid response, this prints
play_level(one)
#calls the function

print('---')
print('---')
print('You pass through the doorway to the next level.')
print('---')
print('---')
#segway to the next level



###LEVEL 2



def play_level(two):
#level function
    if player.hp<=0:
        player.hp=100
        minos.hp=60
    #if the player games over, they restart with full health
    enter(two)
    #prints title for level
    print(f"{two.description}")
    #prints level description
    print("---")
    print('To keep walking, press "w". To shop, press "s". If a resident of Hell approaches, press "t" to talk.')
    #game tutorial basically
    while True:
    #player has choices to progress in the game
        choice=(input('Continue walking ("w") or shop ("s")? ')).lower()
        #player can continue walking or shop based on what they input
        if choice=='s':
        #if player chooses to shop, they enter a while loop
            print("You have entered the shop.")
            print(inventory)
            #displays inventory
            print("5 coins for an apple.")
            while True:
                shop=input('Would you like to buy apples? y/n ').lower()
                #lets player choose to buy apples
                if shop=='y':
                    apple_amount=int((input('How many apples? # ')))
                    #player inputs an amount (integer)
                    if inventory['coins']>=apple_amount*5:
                    #tests if the player has enough money
                        inventory['apples']+=apple_amount
                        #increases player's amout of apples based on the number they chose to buy
                        inventory['coins']-=apple_amount*5
                        #inventory coins are taken away based on the number of apples
                        print(inventory)
                        print("You have exited the shop.")
                        break
                        #shows the inventory and leaves the shop by breaking out of the loop
                    else:
                        print("You don't have enough money.")
                        print("You have exited the shop.")
                        break
                    #if he/she doesn't have enough money, he/she breaks out of the loop

                elif shop=='n':
                    print("You have exited the shop.")
                    break
                    #breaks out of loop and leaves the shop if the character says no
                else:
                    print("Choose a valid response.")
        elif choice=='w':
            print("You keep walking.")
            break
            #same thing as before
        else:
            print("Choose a valid response.")

    print('---')
    print('As you walk, you see someone approaching in the distance.')
    #prints dialogue that lets player know there's someone to talk to
    while True:
        choice=(input('Talk ("t"), continue walking ("w") or shop ("s")? ')).lower()
        #now gives option to talk too
        if choice=='s':
        #same process/documentation as before
            print("You have entered the shop.")
            print(inventory)
            print("5 coins for an apple.")
            while True:
                shop=input('Would you like to buy apples? y/n ').lower()
                if shop=='y':
                    apple_amount=int((input('How many apples? # ')))
                    if inventory['coins']>=apple_amount*5:
                        inventory['apples']+=apple_amount
                        inventory['coins']-=apple_amount*5
                        print(inventory)
                        print("You have exited the shop.")
                        break
                    else:
                        print("You don't have enough money.")
                        print("You have exited the shop.")
                        break

                elif shop=='n':
                    print("You have exited the shop.")
                    break
                else:
                    print("Choose a valid response.")
            #same shopping loop
        elif choice=='w':
        #same process/documentation as before
            print("You keep walking.")
            break
        elif choice=='t':
        #lets the character talk to the Resident
            print("You choose to talk to the stranger.")
            print("---")
            introduce(cleopatra)
            #calls introduce function
            print("---")
            print("Cleopatra vanishes.")
            print('---')
            choice=(input('Continue walking ("w") or shop ("s")? ')).lower()
            if choice=='s':
                print("You have entered the shop.")
                print(inventory)
                print("5 coins for an apple.")
                while True:
                    shop=input('Would you like to buy apples? y/n ').lower()
                    if shop=='y':
                        apple_amount=int((input('How many apples? # ')))
                        if inventory['coins']>=apple_amount*5:
                            inventory['apples']+=apple_amount
                            inventory['coins']-=apple_amount*5
                            print(inventory)
                            print("You have exited the shop.")
                            break
                        else:
                            print("You don't have enough money.")
                            print("You have exited the shop.")
                            break

                    elif shop=='n':
                        print("You have exited the shop.")
                        break
                    else:
                        print("Choose a valid response.")
            elif choice=='w':
                print("You keep walking.")
                break
            else:
                print("Choose a valid response.")
        #lets the character proceed after talking by going back to the original loop

    print('---')
    print(funny['two'])
    print('---')
    #prints the intermission

    while True:
        choice=(input('Continue walking ("w") or shop ("s")? ')).lower()
        if choice=='s':
            print("You have entered the shop.")
            print(inventory)
            print("5 coins for an apple.")
            while True:
                shop=input('Would you like to buy apples? y/n ').lower()
                if shop=='y':
                    apple_amount=int((input('How many apples? # ')))
                    if inventory['coins']>=apple_amount*5:
                        inventory['apples']+=apple_amount
                        inventory['coins']-=apple_amount*5
                        print(inventory)
                        print("You have exited the shop.")
                        break
                    else:
                        print("You don't have enough money.")
                        print("You have exited the shop.")
                        break

                elif shop=='n':
                    print("You have exited the shop.")
                    break
                else:
                    print("Choose a valid response.")
        elif choice=='w':
            print("You keep walking.")
            break
        else:
            print("Choose a valid response.")
    #all the same exact thing

    guard(minos)
    #calls guard function

    while True:
        if minos.hp<=0:
            print('---')
            print('Minos hp: 0')
            print('---')
            print("You've defeated the boss!")
            #game progresses if boss runs out of hp
            break
            #proceeds to the next level
        elif player.hp<=0:
            print('---')
            print("Your hp is 0. Game Over.")
            print('---')
            #Game over if player runs out of hp
            play_level(two)
            #calls function to restart the level
        elif player.hp>0 and minos.hp>0:
            print(f'Player: hp {player.hp}, Minos: hp {minos.hp}')
            print('---')
            while True:
                battle=input(("Attack ('a') or heal ('h')? ")).lower()
                #player can choose to attack or heal
                if battle=='a':
                #if player chooses to attack, he/she enters a while loop
                    print('---')
                    attack(minos)
                    #calls attack function
                    print(f"You attack {minos.name2}.")
                    print('---')
                    if minos.hp<0:
                        break
                        #if the character beats the boss, they proceed to the next level
                    else:
                        print(f'Player: {player.hp}, Minos: {minos.hp}')
                        #prints stats
                    attack1(player)
                    #calls attack function
                    print('---')
                    print('---')
                    print('Minos attacks you.')
                    print('---')
                    if player.hp<0:
                        break
                        #breaks out of the loop if player loses all his/her health
                    else:
                        print(f'Player: {player.hp}, Minos: {minos.hp}')
                        #prints stats
                        break
                        #breaks out of the loop
                elif battle=='h':
                #if player chooses to heal, the code enters a while loop
                    print('---')
                    while True:
                    #while loop so the player can eat an apple only if he/she has enough
                        if inventory['apples']>0:
                            print(f"You ate an apple.")
                            #has player eat apple if they have apples to eat
                            heal(player)
                            #calls heal function
                            print('---')
                            print(f'Player hp: {player.hp}, Minos hp: {minos.hp}')
                            #prints player and boss hp
                            print('---')
                            print('---')
                            break
                            #breaks out of the function
                        else:
                            print("You don't have any apples.")
                            print('--')
                            break
                        #if the player has no apples, this prints
                else:
                    print('---')
                    print("Choose a valid response.")
                    print('---')
                #if they type an invalid response, this prints
play_level(two)
#calls the function

print('---')
print('---')
print('You pass through the doorway to the next level.')
print('---')
print('---')
#segway to the next level


###LEVEL 3


def play_level(three):
#level function
    if player.hp<=0:
        player.hp=100
        cereberus.hp=70
    #if the player games over, they restart with full health
    enter(three)
    #prints title for level
    print(f"{three.description}")
    #prints level description
    print("---")
    print('To keep walking, press "w". To shop, press "s". If a resident of Hell approaches, press "t" to talk.')
    #game tutorial basically
    while True:
    #player has choices to progress in the game
        choice=(input('Continue walking ("w") or shop ("s")? ')).lower()
        #player can continue walking or shop based on what they input
        if choice=='s':
        #if player chooses to shop, they enter a while loop
            print("You have entered the shop.")
            print(inventory)
            #displays inventory
            print("5 coins for an apple.")
            while True:
                shop=input('Would you like to buy apples? y/n ').lower()
                #lets player choose to buy apples
                if shop=='y':
                    apple_amount=int((input('How many apples? # ')))
                    #player inputs an amount (integer)
                    if inventory['coins']>=apple_amount*5:
                    #tests if the player has enough money
                        inventory['apples']+=apple_amount
                        #increases player's amout of apples based on the number they chose to buy
                        inventory['coins']-=apple_amount*5
                        #inventory coins are taken away based on the number of apples
                        print(inventory)
                        print("You have exited the shop.")
                        break
                        #shows the inventory and leaves the shop by breaking out of the loop
                    else:
                        print("You don't have enough money.")
                        print("You have exited the shop.")
                        break
                    #if he/she doesn't have enough money, he/she breaks out of the loop

                elif shop=='n':
                    print("You have exited the shop.")
                    break
                    #breaks out of loop and leaves the shop if the character says no
                else:
                    print("Choose a valid response.")
        elif choice=='w':
            print("You keep walking.")
            break
            #same thing as before
        else:
            print("Choose a valid response.")

    print('---')
    print('As you walk, you see someone approaching in the distance.')
    #prints dialogue that lets player know there's someone to talk to
    while True:
        choice=(input('Talk ("t"), continue walking ("w") or shop ("s")? ')).lower()
        #now gives option to talk too
        if choice=='s':
        #same process/documentation as before
            print("You have entered the shop.")
            print(inventory)
            print("5 coins for an apple.")
            while True:
                shop=input('Would you like to buy apples? y/n ').lower()
                if shop=='y':
                    apple_amount=int((input('How many apples? # ')))
                    if inventory['coins']>=apple_amount*5:
                        inventory['apples']+=apple_amount
                        inventory['coins']-=apple_amount*5
                        print(inventory)
                        print("You have exited the shop.")
                        break
                    else:
                        print("You don't have enough money.")
                        print("You have exited the shop.")
                        break

                elif shop=='n':
                    print("You have exited the shop.")
                    break
                else:
                    print("Choose a valid response.")
            #same shopping loop
        elif choice=='w':
        #same process/documentation as before
            print("You keep walking.")
            break
        elif choice=='t':
        #lets the character talk to the Resident
            print("You choose to talk to the stranger.")
            print("---")
            introduce(ciacco)
            #calls introduce function
            print("---")
            print("Ciacco vanishes.")
            print('---')
            choice=(input('Continue walking ("w") or shop ("s")? ')).lower()
            if choice=='s':
                print("You have entered the shop.")
                print(inventory)
                print("5 coins for an apple.")
                while True:
                    shop=input('Would you like to buy apples? y/n ').lower()
                    if shop=='y':
                        apple_amount=int((input('How many apples? # ')))
                        if inventory['coins']>=apple_amount*5:
                            inventory['apples']+=apple_amount
                            inventory['coins']-=apple_amount*5
                            print(inventory)
                            print("You have exited the shop.")
                            break
                        else:
                            print("You don't have enough money.")
                            print("You have exited the shop.")
                            break

                    elif shop=='n':
                        print("You have exited the shop.")
                        break
                    else:
                        print("Choose a valid response.")
            elif choice=='w':
                print("You keep walking.")
                break
            else:
                print("Choose a valid response.")
        #lets the character proceed after talking by going back to the original loop

    print('---')
    print(funny['three'])
    print('---')
    #prints the intermission

    while True:
        choice=(input('Continue walking ("w") or shop ("s")? ')).lower()
        if choice=='s':
            print("You have entered the shop.")
            print(inventory)
            print("5 coins for an apple.")
            while True:
                shop=input('Would you like to buy apples? y/n ').lower()
                if shop=='y':
                    apple_amount=int((input('How many apples? # ')))
                    if inventory['coins']>=apple_amount*5:
                        inventory['apples']+=apple_amount
                        inventory['coins']-=apple_amount*5
                        print(inventory)
                        print("You have exited the shop.")
                        break
                    else:
                        print("You don't have enough money.")
                        print("You have exited the shop.")
                        break

                elif shop=='n':
                    print("You have exited the shop.")
                    break
                else:
                    print("Choose a valid response.")
        elif choice=='w':
            print("You keep walking.")
            break
        else:
            print("Choose a valid response.")
    #all the same exact thing

    guard(cereberus)
    #calls guard function

    while True:
        if cereberus.hp<=0:
            print('---')
            print('Cereberus hp: 0')
            print('---')
            print("You've defeated the boss!")
            #game progresses if boss runs out of hp
            break
            #proceeds to the next level
        elif player.hp<=0:
            print('---')
            print("Your hp is 0. Game Over.")
            print('---')
            #Game over if player runs out of hp
            play_level(three)
            #calls function to restart the level
        elif player.hp>0 and cereberus.hp>0:
            print(f'Player: hp {player.hp}, Cereberus: hp {cereberus.hp}')
            print('---')
            while True:
                battle=input(("Attack ('a') or heal ('h')? ")).lower()
                #player can choose to attack or heal
                if battle=='a':
                #if player chooses to attack, he/she enters a while loop
                    print('---')
                    attack(cereberus)
                    #calls attack function
                    print(f"You attack {cereberus.name2}.")
                    print('---')
                    if cereberus.hp<0:
                        break
                        #if the character beats the boss, they proceed to the next level
                    else:
                        print(f'Player: {player.hp}, Cereberus: {cereberus.hp}')
                        #prints stats
                    attack1(player)
                    #calls attack function
                    print('---')
                    print('---')
                    print('Cereberus attacks you.')
                    print('---')
                    if player.hp<0:
                        break
                        #breaks out of the loop if player loses all his/her health
                    else:
                        print(f'Player: {player.hp}, Cereberus: {cereberus.hp}')
                        #prints stats
                        break
                        #breaks out of the loop
                elif battle=='h':
                #if player chooses to heal, the code enters a while loop
                    print('---')
                    while True:
                    #while loop so the player can eat an apple only if he/she has enough
                        if inventory['apples']>0:
                            print(f"You ate an apple.")
                            #has player eat apple if they have apples to eat
                            heal(player)
                            #calls heal function
                            print('---')
                            print(f'Player hp: {player.hp}, Cereberus hp: {cereberus.hp}')
                            #prints player and boss hp
                            print('---')
                            print('---')
                            break
                            #breaks out of the function
                        else:
                            print("You don't have any apples.")
                            print('--')
                            break
                        #if the player has no apples, this prints
                else:
                    print('---')
                    print("Choose a valid response.")
                    print('---')
                #if they type an invalid response, this prints
play_level(three)
#calls the function

print('---')
print('---')
print('You pass through the doorway to the next level.')
print('---')
print('---')
#segway to the next level


###LEVEL 4


def play_level(four):
#level function
    if player.hp<=0:
        player.hp=100
        plutus.hp=80
    #if the player games over, they restart with full health
    enter(four)
    #prints title for level
    print(f"{four.description}")
    #prints level description
    print("---")
    print('To keep walking, press "w". To shop, press "s". If a resident of Hell approaches, press "t" to talk.')
    #game tutorial basically
    while True:
    #player has choices to progress in the game
        choice=(input('Continue walking ("w") or shop ("s")? ')).lower()
        #player can continue walking or shop based on what they input
        if choice=='s':
        #if player chooses to shop, they enter a while loop
            print("You have entered the shop.")
            print(inventory)
            #displays inventory
            print("5 coins for an apple.")
            while True:
                shop=input('Would you like to buy apples? y/n ').lower()
                #lets player choose to buy apples
                if shop=='y':
                    apple_amount=int((input('How many apples? # ')))
                    #player inputs an amount (integer)
                    if inventory['coins']>=apple_amount*5:
                    #tests if the player has enough money
                        inventory['apples']+=apple_amount
                        #increases player's amout of apples based on the number they chose to buy
                        inventory['coins']-=apple_amount*5
                        #inventory coins are taken away based on the number of apples
                        print(inventory)
                        print("You have exited the shop.")
                        break
                        #shows the inventory and leaves the shop by breaking out of the loop
                    else:
                        print("You don't have enough money.")
                        print("You have exited the shop.")
                        break
                    #if he/she doesn't have enough money, he/she breaks out of the loop

                elif shop=='n':
                    print("You have exited the shop.")
                    break
                    #breaks out of loop and leaves the shop if the character says no
                else:
                    print("Choose a valid response.")
        elif choice=='w':
            print("You keep walking.")
            break
            #same thing as before
        else:
            print("Choose a valid response.")

    print('---')
    print('As you walk, you see someone approaching in the distance.')
    #prints dialogue that lets player know there's someone to talk to
    while True:
        choice=(input('Talk ("t"), continue walking ("w") or shop ("s")? ')).lower()
        #now gives option to talk too
        if choice=='s':
        #same process/documentation as before
            print("You have entered the shop.")
            print(inventory)
            print("5 coins for an apple.")
            while True:
                shop=input('Would you like to buy apples? y/n ').lower()
                if shop=='y':
                    apple_amount=int((input('How many apples? # ')))
                    if inventory['coins']>=apple_amount*5:
                        inventory['apples']+=apple_amount
                        inventory['coins']-=apple_amount*5
                        print(inventory)
                        print("You have exited the shop.")
                        break
                    else:
                        print("You don't have enough money.")
                        print("You have exited the shop.")
                        break

                elif shop=='n':
                    print("You have exited the shop.")
                    break
                else:
                    print("Choose a valid response.")
            #same shopping loop
        elif choice=='w':
        #same process/documentation as before
            print("You keep walking.")
            break
        elif choice=='t':
        #lets the character talk to the Resident
            print("You choose to talk to the stranger.")
            print("---")
            introduce(avaricious)
            #calls introduce function
            print("---")
            print("Avaricious vanishes.")
            print('---')
            choice=(input('Continue walking ("w") or shop ("s")? ')).lower()
            if choice=='s':
                print("You have entered the shop.")
                print(inventory)
                print("5 coins for an apple.")
                while True:
                    shop=input('Would you like to buy apples? y/n ').lower()
                    if shop=='y':
                        apple_amount=int((input('How many apples? # ')))
                        if inventory['coins']>=apple_amount*5:
                            inventory['apples']+=apple_amount
                            inventory['coins']-=apple_amount*5
                            print(inventory)
                            print("You have exited the shop.")
                            break
                        else:
                            print("You don't have enough money.")
                            print("You have exited the shop.")
                            break

                    elif shop=='n':
                        print("You have exited the shop.")
                        break
                    else:
                        print("Choose a valid response.")
                    break
            elif choice=='w':
                print("You keep walking.")
                break
            else:
                print("Choose a valid response.")
        #lets the character proceed after talking by going back to the original loop

    print('---')
    print(funny['four'])
    print('---')
    #prints the intermission

    while True:
        choice=(input('Continue walking ("w") or shop ("s")? ')).lower()
        if choice=='s':
            print("You have entered the shop.")
            print(inventory)
            print("5 coins for an apple.")
            while True:
                shop=input('Would you like to buy apples? y/n ').lower()
                if shop=='y':
                    apple_amount=int((input('How many apples? # ')))
                    if inventory['coins']>=apple_amount*5:
                        inventory['apples']+=apple_amount
                        inventory['coins']-=apple_amount*5
                        print(inventory)
                        print("You have exited the shop.")
                        break
                    else:
                        print("You don't have enough money.")
                        print("You have exited the shop.")
                        break

                elif shop=='n':
                    print("You have exited the shop.")
                    break
                else:
                    print("Choose a valid response.")
        elif choice=='w':
            print("You keep walking.")
            break
        else:
            print("Choose a valid response.")
    #all the same exact thing

    guard(plutus)
    #calls guard function

    while True:
        if plutus.hp<=0:
            print('---')
            print('Plutus hp: 0')
            print('---')
            print("You've defeated the boss!")
            #game progresses if boss runs out of hp
            break
            #proceeds to the next level
        elif player.hp<=0:
            print('---')
            print("Your hp is 0. Game Over.")
            print('---')
            #Game over if player runs out of hp
            play_level(four)
            #calls function to restart the level
        elif player.hp>0 and plutus.hp>0:
            print(f'Player: hp {player.hp}, Plutus: hp {plutus.hp}')
            print('---')
            while True:
                battle=input(("Attack ('a') or heal ('h')? ")).lower()
                #player can choose to attack or heal
                if battle=='a':
                #if player chooses to attack, he/she enters a while loop
                    print('---')
                    attack(plutus)
                    #calls attack function
                    print(f"You attack {plutus.name2}.")
                    print('---')
                    if plutus.hp<0:
                        break
                        #if the character beats the boss, they proceed to the next level
                    else:
                        print(f'Player: {player.hp}, Plutus: {plutus.hp}')
                        #prints stats
                    attack1(player)
                    #calls attack function
                    print('---')
                    print('---')
                    print('Plutus attacks you.')
                    print('---')
                    if player.hp<0:
                        break
                        #breaks out of the loop if player loses all his/her health
                    else:
                        print(f'Player: {player.hp}, Plutus: {plutus.hp}')
                        #prints stats
                        break
                        #breaks out of the loop
                elif battle=='h':
                #if player chooses to heal, the code enters a while loop
                    print('---')
                    while True:
                    #while loop so the player can eat an apple only if he/she has enough
                        if inventory['apples']>0:
                            print(f"You ate an apple.")
                            #has player eat apple if they have apples to eat
                            heal(player)
                            #calls heal function
                            print('---')
                            print(f'Player hp: {player.hp}, Plutus hp: {plutus.hp}')
                            #prints player and boss hp
                            print('---')
                            print('---')
                            break
                            #breaks out of the function
                        else:
                            print("You don't have any apples.")
                            print('--')
                            break
                        #if the player has no apples, this prints
                else:
                    print('---')
                    print("Choose a valid response.")
                    print('---')
                #if they type an invalid response, this prints
play_level(four)
#calls the function

print('---')
print('---')
print('You pass through the doorway to the next level.')
print('---')
print('---')
#segway to the next level



###LEVEL 5


def play_level(five):
#level function
    if player.hp<=0:
        player.hp=100
        charon.hp=90
    #if the player games over, they restart with full health
    enter(five)
    #prints title for level
    print(f"{five.description}")
    #prints level description
    print("---")
    print('To keep walking, press "w". To shop, press "s". If a resident of Hell approaches, press "t" to talk.')
    #game tutorial basically
    while True:
    #player has choices to progress in the game
        choice=(input('Continue walking ("w") or shop ("s")? ')).lower()
        #player can continue walking or shop based on what they input
        if choice=='s':
        #if player chooses to shop, they enter a while loop
            print("You have entered the shop.")
            print(inventory)
            #displays inventory
            print("5 coins for an apple.")
            while True:
                shop=input('Would you like to buy apples? y/n ').lower()
                #lets player choose to buy apples
                if shop=='y':
                    apple_amount=int((input('How many apples? # ')))
                    #player inputs an amount (integer)
                    if inventory['coins']>=apple_amount*5:
                    #tests if the player has enough money
                        inventory['apples']+=apple_amount
                        #increases player's amout of apples based on the number they chose to buy
                        inventory['coins']-=apple_amount*5
                        #inventory coins are taken away based on the number of apples
                        print(inventory)
                        print("You have exited the shop.")
                        break
                        #shows the inventory and leaves the shop by breaking out of the loop
                    else:
                        print("You don't have enough money.")
                        print("You have exited the shop.")
                        break
                    #if he/she doesn't have enough money, he/she breaks out of the loop

                elif shop=='n':
                    print("You have exited the shop.")
                    break
                    #breaks out of loop and leaves the shop if the character says no
                else:
                    print("Choose a valid response.")
        elif choice=='w':
            print("You keep walking.")
            break
            #same thing as before
        else:
            print("Choose a valid response.")

    print('---')
    print('As you walk, you see someone approaching in the distance.')
    #prints dialogue that lets player know there's someone to talk to
    while True:
        choice=(input('Talk ("t"), continue walking ("w") or shop ("s")? ')).lower()
        #now gives option to talk too
        if choice=='s':
        #same process/documentation as before
            print("You have entered the shop.")
            print(inventory)
            print("5 coins for an apple.")
            while True:
                shop=input('Would you like to buy apples? y/n ').lower()
                if shop=='y':
                    apple_amount=int((input('How many apples? # ')))
                    if inventory['coins']>=apple_amount*5:
                        inventory['apples']+=apple_amount
                        inventory['coins']-=apple_amount*5
                        print(inventory)
                        print("You have exited the shop.")
                        break
                    else:
                        print("You don't have enough money.")
                        print("You have exited the shop.")
                        break

                elif shop=='n':
                    print("You have exited the shop.")
                    break
                else:
                    print("Choose a valid response.")
            #same shopping loop
        elif choice=='w':
        #same process/documentation as before
            print("You keep walking.")
            break
        elif choice=='t':
        #lets the character talk to the Resident
            print("You choose to talk to the stranger.")
            print("---")
            introduce(filippo)
            #calls introduce function
            print("---")
            print("Filippo vanishes.")
            print('---')
            choice=(input('Continue walking ("w") or shop ("s")? ')).lower()
            if choice=='s':
                print("You have entered the shop.")
                print(inventory)
                print("5 coins for an apple.")
                while True:
                    shop=input('Would you like to buy apples? y/n ').lower()
                    if shop=='y':
                        apple_amount=int((input('How many apples? # ')))
                        if inventory['coins']>=apple_amount*5:
                            inventory['apples']+=apple_amount
                            inventory['coins']-=apple_amount*5
                            print(inventory)
                            print("You have exited the shop.")
                            break
                        else:
                            print("You don't have enough money.")
                            print("You have exited the shop.")
                            break

                    elif shop=='n':
                        print("You have exited the shop.")
                        break
                    else:
                        print("Choose a valid response.")
            elif choice=='w':
                print("You keep walking.")
                break
            else:
                print("Choose a valid response.")
        #lets the character proceed after talking by going back to the original loop

    print('---')
    print(funny['five'])
    print('---')
    #prints the intermission

    while True:
        choice=(input('Continue walking ("w") or shop ("s")? ')).lower()
        if choice=='s':
            print("You have entered the shop.")
            print(inventory)
            print("5 coins for an apple.")
            while True:
                shop=input('Would you like to buy apples? y/n ').lower()
                if shop=='y':
                    apple_amount=int((input('How many apples? # ')))
                    if inventory['coins']>=apple_amount*5:
                        inventory['apples']+=apple_amount
                        inventory['coins']-=apple_amount*5
                        print(inventory)
                        print("You have exited the shop.")
                        break
                    else:
                        print("You don't have enough money.")
                        print("You have exited the shop.")
                        break

                elif shop=='n':
                    print("You have exited the shop.")
                    break
                else:
                    print("Choose a valid response.")
        elif choice=='w':
            print("You keep walking.")
            break
        else:
            print("Choose a valid response.")
    #all the same exact thing

    guard(phlegyas)
    #calls guard function

    while True:
        if phlegyas.hp<=0:
            print('---')
            print('Phylegyas hp: 0')
            print('---')
            print("You've defeated the boss!")
            #game progresses if boss runs out of hp
            break
            #proceeds to the next level
        elif player.hp<=0:
            print('---')
            print("Your hp is 0. Game Over.")
            print('---')
            #Game over if player runs out of hp
            play_level(five)
            #calls function to restart the level
        elif player.hp>0 and phlegyas.hp>0:
            print(f'Player: hp {player.hp}, Phlegyas: hp {phlegyas.hp}')
            print('---')
            while True:
                battle=input(("Attack ('a') or heal ('h')? ")).lower()
                #player can choose to attack or heal
                if battle=='a':
                #if player chooses to attack, he/she enters a while loop
                    print('---')
                    attack(phlegyas)
                    #calls attack function
                    print(f"You attack {phlegyas.name2}.")
                    print('---')
                    if phlegyas.hp<0:
                        break
                        #if the character beats the boss, they proceed to the next level
                    else:
                        print(f'Player: {player.hp}, Phlegyas: {phlegyas.hp}')
                        #prints stats
                    attack1(player)
                    #calls attack function
                    print('---')
                    print('---')
                    print('Phlegyas attacks you.')
                    print('---')
                    if player.hp<0:
                        break
                        #breaks out of the loop if player loses all his/her health
                    else:
                        print(f'Player: {player.hp}, Phlegyas: {phlegyas.hp}')
                        #prints stats
                        break
                        #breaks out of the loop
                elif battle=='h':
                #if player chooses to heal, the code enters a while loop
                    print('---')
                    while True:
                    #while loop so the player can eat an apple only if he/she has enough
                        if inventory['apples']>0:
                            print(f"You ate an apple.")
                            #has player eat apple if they have apples to eat
                            heal(player)
                            #calls heal function
                            print('---')
                            print(f'Player hp: {player.hp}, Phlegyas hp: {phlegyas.hp}')
                            #prints player and boss hp
                            print('---')
                            print('---')
                            break
                            #breaks out of the function
                        else:
                            print("You don't have any apples.")
                            print('--')
                            break
                        #if the player has no apples, this prints
                else:
                    print('---')
                    print("Choose a valid response.")
                    print('---')
                #if they type an invalid response, this prints
play_level(five)
#calls the function

print('---')
print('---')
print('You pass through the doorway to the next level.')
print('---')
print('---')
#segway to the next level


###LEVEL 6


def play_level(six):
#level function
    if player.hp<=0:
        player.hp=100
        demon.hp=100
    #if the player games over, they restart with full health
    enter(six)
    #prints title for level
    print(f"{six.description}")
    #prints level description
    print("---")
    print('To keep walking, press "w". To shop, press "s". If a resident of Hell approaches, press "t" to talk.')
    #game tutorial basically
    while True:
    #player has choices to progress in the game
        choice=(input('Continue walking ("w") or shop ("s")? ')).lower()
        #player can continue walking or shop based on what they input
        if choice=='s':
        #if player chooses to shop, they enter a while loop
            print("You have entered the shop.")
            print(inventory)
            #displays inventory
            print("5 coins for an apple.")
            while True:
                shop=input('Would you like to buy apples? y/n ').lower()
                #lets player choose to buy apples
                if shop=='y':
                    apple_amount=int((input('How many apples? # ')))
                    #player inputs an amount (integer)
                    if inventory['coins']>=apple_amount*5:
                    #tests if the player has enough money
                        inventory['apples']+=apple_amount
                        #increases player's amout of apples based on the number they chose to buy
                        inventory['coins']-=apple_amount*5
                        #inventory coins are taken away based on the number of apples
                        print(inventory)
                        print("You have exited the shop.")
                        break
                        #shows the inventory and leaves the shop by breaking out of the loop
                    else:
                        print("You don't have enough money.")
                        print("You have exited the shop.")
                        break
                    #if he/she doesn't have enough money, he/she breaks out of the loop

                elif shop=='n':
                    print("You have exited the shop.")
                    break
                    #breaks out of loop and leaves the shop if the character says no
                else:
                    print("Choose a valid response.")
        elif choice=='w':
            print("You keep walking.")
            break
            #same thing as before
        else:
            print("Choose a valid response.")

    print('---')
    print('As you walk, you see someone approaching in the distance.')
    #prints dialogue that lets player know there's someone to talk to
    while True:
        choice=(input('Talk ("t"), continue walking ("w") or shop ("s")? ')).lower()
        #now gives option to talk too
        if choice=='s':
        #same process/documentation as before
            print("You have entered the shop.")
            print(inventory)
            print("5 coins for an apple.")
            while True:
                shop=input('Would you like to buy apples? y/n ').lower()
                if shop=='y':
                    apple_amount=int((input('How many apples? # ')))
                    if inventory['coins']>=apple_amount*5:
                        inventory['apples']+=apple_amount
                        inventory['coins']-=apple_amount*5
                        print(inventory)
                        print("You have exited the shop.")
                        break
                    else:
                        print("You don't have enough money.")
                        print("You have exited the shop.")
                        break

                elif shop=='n':
                    print("You have exited the shop.")
                    break
                else:
                    print("Choose a valid response.")
            #same shopping loop
        elif choice=='w':
        #same process/documentation as before
            print("You keep walking.")
            break
        elif choice=='t':
        #lets the character talk to the Resident
            print("You choose to talk to the stranger.")
            print("---")
            introduce(epicurus)
            #calls introduce function
            print("---")
            print("Epicurus vanishes.")
            print('---')
            choice=(input('Continue walking ("w") or shop ("s")? ')).lower()
            if choice=='s':
                print("You have entered the shop.")
                print(inventory)
                print("5 coins for an apple.")
                while True:
                    shop=input('Would you like to buy apples? y/n ').lower()
                    if shop=='y':
                        apple_amount=int((input('How many apples? # ')))
                        if inventory['coins']>=apple_amount*5:
                            inventory['apples']+=apple_amount
                            inventory['coins']-=apple_amount*5
                            print(inventory)
                            print("You have exited the shop.")
                            break
                        else:
                            print("You don't have enough money.")
                            print("You have exited the shop.")
                            break

                    elif shop=='n':
                        print("You have exited the shop.")
                        break
                    else:
                        print("Choose a valid response.")
            elif choice=='w':
                print("You keep walking.")
                break
            else:
                print("Choose a valid response.")
        #lets the character proceed after talking by going back to the original loop

    print('---')
    print(funny['six'])
    print('---')
    #prints the intermission

    while True:
        choice=(input('Continue walking ("w") or shop ("s")? ')).lower()
        if choice=='s':
            print("You have entered the shop.")
            print(inventory)
            print("5 coins for an apple.")
            while True:
                shop=input('Would you like to buy apples? y/n ').lower()
                if shop=='y':
                    apple_amount=int((input('How many apples? # ')))
                    if inventory['coins']>=apple_amount*5:
                        inventory['apples']+=apple_amount
                        inventory['coins']-=apple_amount*5
                        print(inventory)
                        print("You have exited the shop.")
                        break
                    else:
                        print("You don't have enough money.")
                        print("You have exited the shop.")
                        break

                elif shop=='n':
                    print("You have exited the shop.")
                    break
                else:
                    print("Choose a valid response.")
        elif choice=='w':
            print("You keep walking.")
            break
        else:
            print("Choose a valid response.")
    #all the same exact thing

    guard(demon)
    #calls guard function

    while True:
        if demon.hp<=0:
            print('---')
            print('Demon hp: 0')
            print('---')
            print("You've defeated the boss!")
            #game progresses if boss runs out of hp
            break
            #proceeds to the next level
        elif player.hp<=0:
            print('---')
            print("Your hp is 0. Game Over.")
            print('---')
            #Game over if player runs out of hp
            play_level(six)
            #calls function to restart the level
        elif player.hp>0 and demon.hp>0:
            print(f'Player: hp {player.hp}, Demon: hp {demon.hp}')
            print('---')
            while True:
                battle=input(("Attack ('a') or heal ('h')? ")).lower()
                #player can choose to attack or heal
                if battle=='a':
                #if player chooses to attack, he/she enters a while loop
                    print('---')
                    attack(demon)
                    #calls attack function
                    print(f"You attack {demon.name2}.")
                    print('---')
                    if demon.hp<0:
                        break
                        #if the character beats the boss, they proceed to the next level
                    else:
                        print(f'Player: {player.hp}, Demon: {demon.hp}')
                        #prints stats
                    attack1(player)
                    #calls attack function
                    print('---')
                    print('---')
                    print('Demon attacks you.')
                    print('---')
                    if player.hp<0:
                        break
                        #breaks out of the loop if player loses all his/her health
                    else:
                        print(f'Player: {player.hp}, Demon: {demon.hp}')
                        #prints stats
                        break
                        #breaks out of the loop
                elif battle=='h':
                #if player chooses to heal, the code enters a while loop
                    print('---')
                    while True:
                    #while loop so the player can eat an apple only if he/she has enough
                        if inventory['apples']>0:
                            print(f"You ate an apple.")
                            #has player eat apple if they have apples to eat
                            heal(player)
                            #calls heal function
                            print('---')
                            print(f'Player hp: {player.hp}, Demon hp: {demon.hp}')
                            #prints player and boss hp
                            print('---')
                            print('---')
                            break
                            #breaks out of the function
                        else:
                            print("You don't have any apples.")
                            print('--')
                            break
                        #if the player has no apples, this prints
                else:
                    print('---')
                    print("Choose a valid response.")
                    print('---')
                #if they type an invalid response, this prints
play_level(six)
#calls the function

print('---')
print('---')
print('You pass through the doorway to the next level.')
print('---')
print('---')
#segway to the next level


###LEVEL 7


def play_level(seven):
#level function
    if player.hp<=0:
        player.hp=100
        centaurus.hp=110
    #if the player games over, they restart with full health
    enter(seven)
    #prints title for level
    print(f"{seven.description}")
    #prints level description
    print("---")
    print('To keep walking, press "w". To shop, press "s". If a resident of Hell approaches, press "t" to talk.')
    #game tutorial basically
    while True:
    #player has choices to progress in the game
        choice=(input('Continue walking ("w") or shop ("s")? ')).lower()
        #player can continue walking or shop based on what they input
        if choice=='s':
        #if player chooses to shop, they enter a while loop
            print("You have entered the shop.")
            print(inventory)
            #displays inventory
            print("5 coins for an apple.")
            while True:
                shop=input('Would you like to buy apples? y/n ').lower()
                #lets player choose to buy apples
                if shop=='y':
                    apple_amount=int((input('How many apples? # ')))
                    #player inputs an amount (integer)
                    if inventory['coins']>=apple_amount*5:
                    #tests if the player has enough money
                        inventory['apples']+=apple_amount
                        #increases player's amout of apples based on the number they chose to buy
                        inventory['coins']-=apple_amount*5
                        #inventory coins are taken away based on the number of apples
                        print(inventory)
                        print("You have exited the shop.")
                        break
                        #shows the inventory and leaves the shop by breaking out of the loop
                    else:
                        print("You don't have enough money.")
                        print("You have exited the shop.")
                        break
                    #if he/she doesn't have enough money, he/she breaks out of the loop

                elif shop=='n':
                    print("You have exited the shop.")
                    break
                    #breaks out of loop and leaves the shop if the character says no
                else:
                    print("Choose a valid response.")
        elif choice=='w':
            print("You keep walking.")
            break
            #same thing as before
        else:
            print("Choose a valid response.")

    print('---')
    print('As you walk, you see someone approaching in the distance.')
    #prints dialogue that lets player know there's someone to talk to
    while True:
        choice=(input('Talk ("t"), continue walking ("w") or shop ("s")? ')).lower()
        #now gives option to talk too
        if choice=='s':
        #same process/documentation as before
            print("You have entered the shop.")
            print(inventory)
            print("5 coins for an apple.")
            while True:
                shop=input('Would you like to buy apples? y/n ').lower()
                if shop=='y':
                    apple_amount=int((input('How many apples? # ')))
                    if inventory['coins']>=apple_amount*5:
                        inventory['apples']+=apple_amount
                        inventory['coins']-=apple_amount*5
                        print(inventory)
                        print("You have exited the shop.")
                        break
                    else:
                        print("You don't have enough money.")
                        print("You have exited the shop.")
                        break

                elif shop=='n':
                    print("You have exited the shop.")
                    break
                else:
                    print("Choose a valid response.")
            #same shopping loop
        elif choice=='w':
        #same process/documentation as before
            print("You keep walking.")
            break
        elif choice=='t':
        #lets the character talk to the Resident
            print("You choose to talk to the stranger.")
            print("---")
            introduce(alexander)
            #calls introduce function
            print("---")
            print("Alexander the Great vanishes.")
            print('---')
            choice=(input('Continue walking ("w") or shop ("s")? ')).lower()
            if choice=='s':
                print("You have entered the shop.")
                print(inventory)
                print("5 coins for an apple.")
                while True:
                    shop=input('Would you like to buy apples? y/n ').lower()
                    if shop=='y':
                        apple_amount=int((input('How many apples? # ')))
                        if inventory['coins']>=apple_amount*5:
                            inventory['apples']+=apple_amount
                            inventory['coins']-=apple_amount*5
                            print(inventory)
                            print("You have exited the shop.")
                            break
                        else:
                            print("You don't have enough money.")
                            print("You have exited the shop.")
                            break

                    elif shop=='n':
                        print("You have exited the shop.")
                        break
                    else:
                        print("Choose a valid response.")
            elif choice=='w':
                print("You keep walking.")
                break
            else:
                print("Choose a valid response.")
        #lets the character proceed after talking by going back to the original loop

    print('---')
    print(funny['seven'])
    print('---')
    #prints the intermission

    while True:
        choice=(input('Continue walking ("w") or shop ("s")? ')).lower()
        if choice=='s':
            print("You have entered the shop.")
            print(inventory)
            print("5 coins for an apple.")
            while True:
                shop=input('Would you like to buy apples? y/n ').lower()
                if shop=='y':
                    apple_amount=int((input('How many apples? # ')))
                    if inventory['coins']>=apple_amount*5:
                        inventory['apples']+=apple_amount
                        inventory['coins']-=apple_amount*5
                        print(inventory)
                        print("You have exited the shop.")
                        break
                    else:
                        print("You don't have enough money.")
                        print("You have exited the shop.")
                        break

                elif shop=='n':
                    print("You have exited the shop.")
                    break
                else:
                    print("Choose a valid response.")
        elif choice=='w':
            print("You keep walking.")
            break
        else:
            print("Choose a valid response.")
    #all the same exact thing

    guard(centaurus)
    #calls guard function

    while True:
        if centaurus.hp<=0:
            print('---')
            print('Centaurus hp: 0')
            print('---')
            print("You've defeated the boss!")
            #game progresses if boss runs out of hp
            break
            #proceeds to the next level
        elif player.hp<=0:
            print('---')
            print("Your hp is 0. Game Over.")
            print('---')
            #Game over if player runs out of hp
            play_level(seven)
            #calls function to restart the level
        elif player.hp>0 and centaurus.hp>0:
            print(f'Player: hp {player.hp}, Centaurus: hp {centaurus.hp}')
            print('---')
            while True:
                battle=input(("Attack ('a') or heal ('h')? ")).lower()
                #player can choose to attack or heal
                if battle=='a':
                #if player chooses to attack, he/she enters a while loop
                    print('---')
                    attack(centaurus)
                    #calls attack function
                    print(f"You attack {centaurus.name2}.")
                    print('---')
                    if centaurus.hp<0:
                        break
                        #if the character beats the boss, they proceed to the next level
                    else:
                        print(f'Player: {player.hp}, Centaurus: {centaurus.hp}')
                        #prints stats
                    attack1(player)
                    #calls attack function
                    print('---')
                    print('---')
                    print('Centaurus attacks you.')
                    print('---')
                    if player.hp<0:
                        break
                        #breaks out of the loop if player loses all his/her health
                    else:
                        print(f'Player: {player.hp}, Centaurus: {centaurus.hp}')
                        #prints stats
                        break
                        #breaks out of the loop
                elif battle=='h':
                #if player chooses to heal, the code enters a while loop
                    print('---')
                    while True:
                    #while loop so the player can eat an apple only if he/she has enough
                        if inventory['apples']>0:
                            print(f"You ate an apple.")
                            #has player eat apple if they have apples to eat
                            heal(player)
                            #calls heal function
                            print('---')
                            print(f'Player hp: {player.hp}, Centaurus hp: {centaurus.hp}')
                            #prints player and boss hp
                            print('---')
                            print('---')
                            break
                            #breaks out of the function
                        else:
                            print("You don't have any apples.")
                            print('--')
                            break
                        #if the player has no apples, this prints
                else:
                    print('---')
                    print("Choose a valid response.")
                    print('---')
                #if they type an invalid response, this prints
play_level(seven)
#calls the function

print('---')
print('---')
print('You pass through the doorway to the next level.')
print('---')
print('---')
#segway to the next level


###LEVEL 8


def play_level(eight):
#level function
    if player.hp<=0:
        player.hp=100
        geryon.hp=120
    #if the player games over, they restart with full health
    enter(eight)
    #prints title for level
    print(f"{eight.description}")
    #prints level description
    print("---")
    print('To keep walking, press "w". To shop, press "s". If a resident of Hell approaches, press "t" to talk.')
    #game tutorial basically
    while True:
    #player has choices to progress in the game
        choice=(input('Continue walking ("w") or shop ("s")? ')).lower()
        #player can continue walking or shop based on what they input
        if choice=='s':
        #if player chooses to shop, they enter a while loop
            print("You have entered the shop.")
            print(inventory)
            #displays inventory
            print("5 coins for an apple.")
            while True:
                shop=input('Would you like to buy apples? y/n ').lower()
                #lets player choose to buy apples
                if shop=='y':
                    apple_amount=int((input('How many apples? # ')))
                    #player inputs an amount (integer)
                    if inventory['coins']>=apple_amount*5:
                    #tests if the player has enough money
                        inventory['apples']+=apple_amount
                        #increases player's amout of apples based on the number they chose to buy
                        inventory['coins']-=apple_amount*5
                        #inventory coins are taken away based on the number of apples
                        print(inventory)
                        print("You have exited the shop.")
                        break
                        #shows the inventory and leaves the shop by breaking out of the loop
                    else:
                        print("You don't have enough money.")
                        print("You have exited the shop.")
                        break
                    #if he/she doesn't have enough money, he/she breaks out of the loop

                elif shop=='n':
                    print("You have exited the shop.")
                    break
                    #breaks out of loop and leaves the shop if the character says no
                else:
                    print("Choose a valid response.")
        elif choice=='w':
            print("You keep walking.")
            break
            #same thing as before
        else:
            print("Choose a valid response.")

    print('---')
    print('As you walk, you see someone approaching in the distance.')
    #prints dialogue that lets player know there's someone to talk to
    while True:
        choice=(input('Talk ("t"), continue walking ("w") or shop ("s")? ')).lower()
        #now gives option to talk too
        if choice=='s':
        #same process/documentation as before
            print("You have entered the shop.")
            print(inventory)
            print("5 coins for an apple.")
            while True:
                shop=input('Would you like to buy apples? y/n ').lower()
                if shop=='y':
                    apple_amount=int((input('How many apples? # ')))
                    if inventory['coins']>=apple_amount*5:
                        inventory['apples']+=apple_amount
                        inventory['coins']-=apple_amount*5
                        print(inventory)
                        print("You have exited the shop.")
                        break
                    else:
                        print("You don't have enough money.")
                        print("You have exited the shop.")
                        break

                elif shop=='n':
                    print("You have exited the shop.")
                    break
                else:
                    print("Choose a valid response.")
            #same shopping loop
        elif choice=='w':
        #same process/documentation as before
            print("You keep walking.")
            break
        elif choice=='t':
        #lets the character talk to the Resident
            print("You choose to talk to the stranger.")
            print("---")
            introduce(ulysses)
            #calls introduce function
            print("---")
            print("Ulysses vanishes.")
            print('---')
            choice=(input('Continue walking ("w") or shop ("s")? ')).lower()
            if choice=='s':
                print("You have entered the shop.")
                print(inventory)
                print("5 coins for an apple.")
                while True:
                    shop=input('Would you like to buy apples? y/n ').lower()
                    if shop=='y':
                        apple_amount=int((input('How many apples? # ')))
                        if inventory['coins']>=apple_amount*5:
                            inventory['apples']+=apple_amount
                            inventory['coins']-=apple_amount*5
                            print(inventory)
                            print("You have exited the shop.")
                            break
                        else:
                            print("You don't have enough money.")
                            print("You have exited the shop.")
                            break

                    elif shop=='n':
                        print("You have exited the shop.")
                        break
                    else:
                        print("Choose a valid response.")
            elif choice=='w':
                print("You keep walking.")
                break
            else:
                print("Choose a valid response.")
        #lets the character proceed after talking by going back to the original loop

    print('---')
    print(funny['eight'])
    print('---')
    #prints the intermission

    while True:
        choice=(input('Continue walking ("w") or shop ("s")? ')).lower()
        if choice=='s':
            print("You have entered the shop.")
            print(inventory)
            print("5 coins for an apple.")
            while True:
                shop=input('Would you like to buy apples? y/n ').lower()
                if shop=='y':
                    apple_amount=int((input('How many apples? # ')))
                    if inventory['coins']>=apple_amount*5:
                        inventory['apples']+=apple_amount
                        inventory['coins']-=apple_amount*5
                        print(inventory)
                        print("You have exited the shop.")
                        break
                    else:
                        print("You don't have enough money.")
                        print("You have exited the shop.")
                        break

                elif shop=='n':
                    print("You have exited the shop.")
                    break
                else:
                    print("Choose a valid response.")
        elif choice=='w':
            print("You keep walking.")
            break
        else:
            print("Choose a valid response.")
    #all the same exact thing

    guard(geryon)
    #calls guard function

    while True:
        if geryon.hp<=0:
            print('---')
            print('Geryon hp: 0')
            print('---')
            print("You've defeated the boss!")
            #game progresses if boss runs out of hp
            break
            #proceeds to the next level
        elif player.hp<=0:
            print('---')
            print("Your hp is 0. Game Over.")
            print('---')
            #Game over if player runs out of hp
            play_level(eight)
            #calls function to restart the level
        elif player.hp>0 and geryon.hp>0:
            print(f'Player: hp {player.hp}, Geryon: hp {geryon.hp}')
            print('---')
            while True:
                battle=input(("Attack ('a') or heal ('h')? ")).lower()
                #player can choose to attack or heal
                if battle=='a':
                #if player chooses to attack, he/she enters a while loop
                    print('---')
                    attack(geryon)
                    #calls attack function
                    print(f"You attack {geryon.name2}.")
                    print('---')
                    if geryon.hp<=0:
                        break
                        #if the character beats the boss, they proceed to the next level
                    else:
                        print(f'Player: {player.hp}, Geryon: {geryon.hp}')
                        #prints stats
                    attack1(player)
                    #calls attack function
                    print('---')
                    print('---')
                    print('Geryon attacks you.')
                    print('---')
                    if player.hp<=0:
                        break
                        #breaks out of the loop if player loses all his/her health
                    else:
                        print(f'Player: {player.hp}, Geryon: {geryon.hp}')
                        #prints stats
                        break
                        #breaks out of the loop
                elif battle=='h':
                #if player chooses to heal, the code enters a while loop
                    print('---')
                    while True:
                    #while loop so the player can eat an apple only if he/she has enough
                        if inventory['apples']>0:
                            print(f"You ate an apple.")
                            #has player eat apple if they have apples to eat
                            heal(player)
                            #calls heal function
                            print('---')
                            print(f'Player hp: {player.hp}, Geryon hp: {geryon.hp}')
                            #prints player and boss hp
                            print('---')
                            print('---')
                            break
                            #breaks out of the function
                        else:
                            print("You don't have any apples.")
                            print('--')
                            break
                        #if the player has no apples, this prints
                else:
                    print('---')
                    print("Choose a valid response.")
                    print('---')
                #if they type an invalid response, this prints
play_level(eight)
#calls the function

print('---')
print('---')
print('You pass through the doorway to the next level.')
print('---')
print('---')
#segway to the next level


###LEVEL 9


def play_level(nine):
#level function
    if player.hp<=0:
        player.hp=100
        devil.hp=130
    #if the player games over, they restart with full health
    enter(nine)
    #prints title for level
    print(f"{nine.description}")
    #prints level description
    print("---")
    print('To keep walking, press "w". To shop, press "s". If a resident of Hell approaches, press "t" to talk.')
    #game tutorial basically
    while True:
    #player has choices to progress in the game
        choice=(input('Continue walking ("w") or shop ("s")? ')).lower()
        #player can continue walking or shop based on what they input
        if choice=='s':
        #if player chooses to shop, they enter a while loop
            print("You have entered the shop.")
            print(inventory)
            #displays inventory
            print("5 coins for an apple.")
            while True:
                shop=input('Would you like to buy apples? y/n ').lower()
                #lets player choose to buy apples
                if shop=='y':
                    apple_amount=int((input('How many apples? # ')))
                    #player inputs an amount (integer)
                    if inventory['coins']>=apple_amount*5:
                    #tests if the player has enough money
                        inventory['apples']+=apple_amount
                        #increases player's amout of apples based on the number they chose to buy
                        inventory['coins']-=apple_amount*5
                        #inventory coins are taken away based on the number of apples
                        print(inventory)
                        print("You have exited the shop.")
                        break
                        #shows the inventory and leaves the shop by breaking out of the loop
                    else:
                        print("You don't have enough money.")
                        print("You have exited the shop.")
                        break
                    #if he/she doesn't have enough money, he/she breaks out of the loop

                elif shop=='n':
                    print("You have exited the shop.")
                    break
                    #breaks out of loop and leaves the shop if the character says no
                else:
                    print("Choose a valid response.")
        elif choice=='w':
            print("You keep walking.")
            break
            #same thing as before
        else:
            print("Choose a valid response.")

    print('---')
    print('As you walk, you see someone approaching in the distance.')
    #prints dialogue that lets player know there's someone to talk to
    while True:
        choice=(input('Talk ("t"), continue walking ("w") or shop ("s")? ')).lower()
        #now gives option to talk too
        if choice=='s':
        #same process/documentation as before
            print("You have entered the shop.")
            print(inventory)
            print("5 coins for an apple.")
            while True:
                shop=input('Would you like to buy apples? y/n ').lower()
                if shop=='y':
                    apple_amount=int((input('How many apples? # ')))
                    if inventory['coins']>=apple_amount*5:
                        inventory['apples']+=apple_amount
                        inventory['coins']-=apple_amount*5
                        print(inventory)
                        print("You have exited the shop.")
                        break
                    else:
                        print("You don't have enough money.")
                        print("You have exited the shop.")
                        break

                elif shop=='n':
                    print("You have exited the shop.")
                    break
                else:
                    print("Choose a valid response.")
            #same shopping loop
        elif choice=='w':
        #same process/documentation as before
            print("You keep walking.")
            break
        elif choice=='t':
        #lets the character talk to the Resident
            print("You choose to talk to the stranger.")
            print("---")
            introduce(judas)
            #calls introduce function
            print("---")
            print("Judas vanishes.")
            print('---')
            choice=(input('Continue walking ("w") or shop ("s")? ')).lower()
            if choice=='s':
                print("You have entered the shop.")
                print(inventory)
                print("5 coins for an apple.")
                while True:
                    shop=input('Would you like to buy apples? y/n ').lower()
                    if shop=='y':
                        apple_amount=int((input('How many apples? # ')))
                        if inventory['coins']>=apple_amount*5:
                            inventory['apples']+=apple_amount
                            inventory['coins']-=apple_amount*5
                            print(inventory)
                            print("You have exited the shop.")
                            break
                        else:
                            print("You don't have enough money.")
                            print("You have exited the shop.")
                            break

                    elif shop=='n':
                        print("You have exited the shop.")
                        break
                    else:
                        print("Choose a valid response.")
            elif choice=='w':
                print("You keep walking.")
                break
            else:
                print("Choose a valid response.")
        #lets the character proceed after talking by going back to the original loop

    print('---')
    print(funny['nine'])
    print('---')
    #prints the intermission

    while True:
        choice=(input('Continue walking ("w") or shop ("s")? ')).lower()
        if choice=='s':
            print("You have entered the shop.")
            print(inventory)
            print("5 coins for an apple.")
            while True:
                shop=input('Would you like to buy apples? y/n ').lower()
                if shop=='y':
                    apple_amount=int((input('How many apples? # ')))
                    if inventory['coins']>=apple_amount*5:
                        inventory['apples']+=apple_amount
                        inventory['coins']-=apple_amount*5
                        print(inventory)
                        print("You have exited the shop.")
                        break
                    else:
                        print("You don't have enough money.")
                        print("You have exited the shop.")
                        break

                elif shop=='n':
                    print("You have exited the shop.")
                    break
                else:
                    print("Choose a valid response.")
        elif choice=='w':
            print("You keep walking.")
            break
        else:
            print("Choose a valid response.")
    #all the same exact thing

    guard(devil)
    #calls guard function

    while True:
        if devil.hp<=0:
            print('---')
            print('Devil hp: 0')
            print('---')
            print("You've defeated the boss!")
            #game progresses if boss runs out of hp
            break
            #proceeds to the next level
        elif player.hp<=0:
            print('---')
            print("Your hp is 0. Game Over.")
            print('---')
            #Game over if player runs out of hp
            play_level(nine)
            #calls function to restart the level
        elif player.hp>0 and devil.hp>0:
            print(f'Player: hp {player.hp}, Devil: hp {devil.hp}')
            print('---')
            while True:
                battle=input(("Attack ('a') or heal ('h')? ")).lower()
                #player can choose to attack or heal
                if battle=='a':
                #if player chooses to attack, he/she enters a while loop
                    print('---')
                    attack(devil)
                    #calls attack function
                    print(f"You attack {devil.name2}.")
                    print('---')
                    if devil.hp<0:
                        break
                        #if the character beats the boss, they proceed to the next level
                    else:
                        print(f'Player: {player.hp}, Devil: {devil.hp}')
                        #prints stats
                    attack1(player)
                    #calls attack function
                    print('---')
                    print('---')
                    print('Devil attacks you.')
                    print('---')
                    if player.hp<0:
                        break
                        #breaks out of the loop if player loses all his/her health
                    else:
                        print(f'Player: {player.hp}, Devil: {devil.hp}')
                        #prints stats
                        break
                        #breaks out of the loop
                elif battle=='h':
                #if player chooses to heal, the code enters a while loop
                    print('---')
                    while True:
                    #while loop so the player can eat an apple only if he/she has enough
                        if inventory['apples']>0:
                            print(f"You ate an apple.")
                            #has player eat apple if they have apples to eat
                            heal(player)
                            #calls heal function
                            print('---')
                            print(f'Player hp: {player.hp}, Devil hp: {devil.hp}')
                            #prints player and boss hp
                            print('---')
                            print('---')
                            break
                            #breaks out of the function
                        else:
                            print("You don't have any apples.")
                            print('--')
                            break
                        #if the player has no apples, this prints
                else:
                    print('---')
                    print("Choose a valid response.")
                    print('---')
                #if they type an invalid response, this prints
play_level(nine)
#calls the function

print('---')
print('---')
print('You pass through the doorway.')
print('---')
print('---')
print("You have escaped Hell. Congratulations.")
print('---')
print('---')
#end game