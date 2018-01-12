import random
inventory={'coins': 10, 'apples': 3}
class Player(object):
    def __init__(self, hp, attack):
        self.hp=hp
        self.attack=attack
player=Player(100, (7,13))
def stats(self):
    print(f"Health: {self.hp}")

def attack(boss):
    boss.hp-=random.randint(7,13)

def heal(self):
    self.hp+=10
    inventory['apples']-=1
    print(f" You chose to heal. Your hp is now {self.hp}. You have {inventory['apples']} left.")

def stats(player):
    print(f'Hp: {player.hp}')

class Resident(object):
    def __init__(self, name, bio, gift):
        self.name=name
        self.bio=bio
        self.gift=gift
socrates=Resident('Socrates', 'insert dialogue here', '3 coins')
cleopatra=Resident('Cleopatra', 'insert dialogue here', '3 coins')
ciacco=Resident('Ciacco', 'insert dialogue here', '3 coins')
avaricious=Resident('Avaricious', 'insert dialogue here', '3 coins')
filippo=Resident('Filippo Argenti', 'insert dialogue here', '3 coins')
epicurus=Resident('Epicurus', 'insert dialogue here', '3 coins')
alexander=Resident('Alexander the Great', 'insert dialogue here', '3 coins')
ulysses=Resident('Ulysses', 'insert dialogue here', '3 coins')
judas=Resident('Judas', 'insert dialogue here', '3 apples')

def introduce(self):
    print(f'Resident: "My name is {self.name}. {self.bio}. You have a long journey ahead-- take these."')
    print('---')
    print(f'You get {self.gift}.')
    inventory['coins']+=3
    print(inventory)

class Boss(object):
    def __init__(self, name2, description, hp, attack2):
        self.name2=name2
        self.description=description
        self.hp=hp
        self.attack2=attack

charon=Boss('Charon', '', 50, (7,13))
minos=Boss('Minos', '', 60, [7,13])
cereberus=Boss('Cereberus', '', 70, [7,13])
plutus=Boss('Plutus', '', 80, [7,13])
phlegyas=Boss('Phlegyas', '', 90, [7,13])
demon=Boss('Guard Demon', '', 100, [7,13])
centaurus=Boss('Centaurus', '', 110, [7,13])
geryon=Boss('Geryon', '', 120, [7,13])
devil=Boss('Devil', '', 150, [7,13])

def guard(self):
    print("You are close to the end. You see a gateway up ahead and a figure blocking the entrance.")
    print("---")
    print(f"{self.name2} guards the door to the next level.")
    print("---")
    print(f"{self.name2}: {self.description}")
    print(f'Hp: {self.hp}')

def attack2(player):
    player.hp=-random.randint(7,13)


class Level(object):
    def __init__(self, name3, level, description):
        self.name3=name3
        self.level=level
        self.description=description
one=Level('Limbo', 'Level 1', 'insert description here')
two=Level('Lust', 'Level 2', 'insert description here')
three=Level('Gluttony', 'Level 3', 'insert description here')
four=Level('Greed', 'Level 4', 'insert description here')
five=Level('Wrath', 'Level 5', 'insert description here')
six=Level('Heresy', 'Level 6', 'insert description here')
seven=Level('Violence', 'Level 7', 'insert description here')
eight=Level('Malebolge', 'Level 8', 'insert description here')
nine=Level('Treachery', 'Level 9', 'insert description here')

def enter(self):
    print(f"Enter {self.level}: {self.name3}")

funny={'one': 'As you walk, you approach a body of water. You peer over the edge to see what lurks below. Whoops. You slip into the River Acheron. You klutz.', 'two': '', 'three': '', 'four': '', 'five': '', 'six': '', 'seven': '', 'eight': '', 'nine':''}


#START GAME

print("You have fallen into Hell. Survive the nine levels to escape.")
print("---")
stats(player)
print(f"{inventory}")
print("Apples heal 10hp. Use them wisely.")
print('---')
enter(one)
print(f"{one.description}")
print("---")
print('To keep walking, press "w". To shop, press "s". If a resident of Hell approaches, press "t" to talk.')
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

print('---')
print('As you walk, you see someone approaching in the distance.')
while True:
    choice=(input('Talk ("t"), continue walking ("w") or shop ("s")? ')).lower()
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
    elif choice=='t':
        print("You choose to talk to the stranger.")
        print("---")
        introduce(socrates)
        print("---")
        print("Socrates vanishes.")
        print('---')
        break
    elif choice=='w':
        print("You keep walking.")
        break
    else:
        print("Choose a valid response.")

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

print('---')
print(funny['one'])
print('---')

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

guard(charon)

print(f'Player: {player.hp}, Charon: {charon.hp}')
while charon.hp>0 and player.hp>0:
    print(f'Player: player.hp, Charon: charon.hp')
    battle=input(("Attack ('a') or heal ('h')? ")).lower()
    if battle=='a':
        print('---')
        attack(charon)
        print(f"You attack {charon.name2}.")
        print('---')
        print(f'Player: {player.hp}, Charon: {charon.hp}')
        charon.attack2
        print('---')
        print('---')
        print('Charon attacks you.')
        print('---')
        print(f'Player: {player.hp}, Charon: {charon.hp}')
    elif battle=='h':
        print('---')
        heal(player)
        print(f"You ate an apple.")
        print('---')
        print(f'Player hp: {player.hp}, Charon hp: {charon.hp}')
        print('---')
        print('---')
        charon.attack2
        print('Charon attacks you.')
        print('---')
        print(f'Player hp: {player.hp}, Charon hp: {charon.hp}')
    else:
        print('---')
        print("Choose a valid response.")
    if charon.hp<=0:
        print('---')
        print("You've defeated the boss!")
        break
    if player.hp<=0:
        print('---')
        print("Your hp is 0. Game Over.")
        enter(one)
        break
