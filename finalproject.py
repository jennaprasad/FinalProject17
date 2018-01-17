import random
inventory={'coins': 50, 'apples': 3}
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
    print(f"Your hp is now {self.hp}. You have {inventory['apples']} apples left.")

class Resident(object):
    def __init__(self, name, bio, gift):
        self.name=name
        self.bio=bio
        self.gift=gift
socrates=Resident('Socrates', 'insert dialogue here', '10 coins')
cleopatra=Resident('Cleopatra', 'insert dialogue here', '10 coins')
ciacco=Resident('Ciacco', 'insert dialogue here', '10 coins')
avaricious=Resident('Avaricious', 'insert dialogue here', '10 coins')
filippo=Resident('Filippo Argenti', 'insert dialogue here', '10 coins')
epicurus=Resident('Epicurus', 'insert dialogue here', '10 coins')
alexander=Resident('Alexander the Great', 'insert dialogue here', '10 coins')
ulysses=Resident('Ulysses', 'insert dialogue here', '10 coins')
judas=Resident('Judas', 'insert dialogue here', '10 apples')

def introduce(self):
    print(f'Resident: "My name is {self.name}. {self.bio}. You have a long journey ahead-- take these."')
    print('---')
    print(f'You get {self.gift}.')
    inventory['coins']+=10
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
    player.hp-=random.randint(7,13)


class Level(object):
    def __init__(self, name3, level, description, position):
        self.name3=name3
        self.level=level
        self.description=description
        self.position=position
one=Level('Limbo', 'Level 1', 'insert description here', 1)
two=Level('Lust', 'Level 2', 'insert description here', 2)
three=Level('Gluttony', 'Level 3', 'insert description here', 3)
four=Level('Greed', 'Level 4', 'insert description here', 4)
five=Level('Wrath', 'Level 5', 'insert description here', 5)
six=Level('Heresy', 'Level 6', 'insert description here', 6)
seven=Level('Violence', 'Level 7', 'insert description here', 7)
eight=Level('Malebolge', 'Level 8', 'insert description here', 8)
nine=Level('Treachery', 'Level 9', 'insert description here', 8)

def enter(self):
    print(f"Enter {self.level}: {self.name3}")

funny={'one': 'As you walk, you approach a body of water. You peer over the edge to see what lurks below. Whoops. You slip into the River Acheron. You klutz.', 'two': '', 'three': '', 'four': '', 'five': '', 'six': '', 'seven': '', 'eight': '', 'nine':''}


###START GAME


print("You have fallen into Hell. Survive the nine levels to escape.")
print("---")
stats(player)
print(f"{inventory}")
print("Apples heal 10hp. Use them wisely.")
print('---')


###LEVEL 1


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

while True:
    if charon.hp<=0:
        print('---')
        print('Charon hp: 0')
        print('---')
        print("You've defeated the boss!")
        break
    elif player.hp<=0:
        print('---')
        print("Your hp is 0. Game Over.")
        print('---')
        enter(one)
        break
    elif player.hp>0 and charon.hp>0:
        print(f'Player: hp {player.hp}, Charon: hp {charon.hp}')
        print('---')
        while True:
            battle=input(("Attack ('a') or heal ('h')? ")).lower()
            if battle=='a':
                print('---')
                attack(charon)
                print(f"You attack {charon.name2}.")
                print('---')
                if charon.hp<0:
                    break
                else:
                    print(f'Player: {player.hp}, Charon: {charon.hp}')
                attack2(player)
                print('---')
                print('---')
                print('Charon attacks you.')
                print('---')
                if player.hp<0:
                    break
                else:
                    print(f'Player: {player.hp}, Charon: {charon.hp}')
                    break
            elif battle=='h':
                print('---')
                while True:
                    if inventory['apples']>0:
                        print(f"You ate an apple.")
                        heal(player)
                        print('---')
                        print(f'Player hp: {player.hp}, Charon hp: {charon.hp}')
                        print('---')
                        print('---')
                        attack2(player)
                        print('Charon attacks you.')
                        print('---')
                        print(f'Player hp: {player.hp}, Charon hp: {charon.hp}')
                        print('---')
                        print('---')
                        break
                    else:
                        print("You don't have any apples.")
                        print('--')
                        break
            else:
                print('---')
                print("Choose a valid response.")
                print('---')

print('---')
print('---')
print('You pass through the doorway to the next level.')
print('---')
print('---')


###LEVEL 2

enter(two)
print(f"{two.description}")
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
        introduce(cleopatra)
        print("---")
        print("Cleopatra vanishes.")
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
print(funny['two'])
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

guard(minos)

while True:
    if minos.hp<=0:
        print('---')
        print('Minos hp: 0')
        print('---')
        print("You've defeated the boss!")
        print('---')
        print('---')
        print('You pass through the doorway to the next level.')
        print('---')
        print('---')
        break
    elif player.hp<=0:
        print('---')
        print("Your hp is 0. Game Over.")
        print('---')
        enter(two)
        break
    elif player.hp>0 and minos.hp>0:
        print(f'Player: hp {player.hp}, Minos: hp {minos.hp}')
        print('---')
        while True:
            battle=input(("Attack ('a') or heal ('h')? ")).lower()
            if battle=='a':
                print('---')
                attack(minos)
                print(f"You attack {minos.name2}.")
                print('---')
                if minos.hp<0:
                    break
                else:
                    print(f'Player: {player.hp}, Minos: {minos.hp}')
                attack2(player)
                print('---')
                print('---')
                print('Minos attacks you.')
                print('---')
                if player.hp<0:
                    break
                else:
                    print(f'Player: {player.hp}, Minos: {minos.hp}')
                    break
            elif battle=='h':
                print('---')
                while True:
                    if inventory['apples']>0:
                        print(f"You ate an apple.")
                        heal(player)
                        print('---')
                        print(f'Player hp: {player.hp}, Minos hp: {minos.hp}')
                        print('---')
                        print('---')
                        attack2(player)
                        print('Minos attacks you.')
                        print('---')
                        print(f'Player hp: {player.hp}, Minos hp: {minos.hp}')
                        print('---')
                        print('---')
                        break
                    else:
                        print("You don't have any apples.")
                        print('--')
                        break
            else:
                print('---')
                print("Choose a valid response.")
                print('---')
