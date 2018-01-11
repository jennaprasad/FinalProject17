player_hp=100
player_attack=10
player_stats=(f"Hp: {player_hp}, Attack: {player_attack}")

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
    def __init__(self, name2, stats, attack):
        self.name2=name2
        self.stats=stats
        self.attack=attack
charon=Boss('Charon', 'hp 50', '')
minos=Boss('Minos', 'hp 60', '')
cereberus=Boss('Cereberus', 'hp 70', '')
plutus=Boss('Plutus', 'hp 80', '')
phlegyas=Boss('Phlegyas', 'hp 90', '')
demon=Boss('Guard Demon', 'hp 100', '')
centaurus=Boss('Centaurus', 'hp 110', '')
geryon=Boss('Geryon', 'hp 120', '')
devil=Boss('Devil', 'hp 150', '')

def guard(self):
    print("You are close to the end. You see a gateway up ahead and a figure blocking the entrance.")
    print("---")
    print(f"{self.name2} guards the door to the next level.")
    print("---")
    print(f"{self.name2}: {self.stats}, {self.attack}")



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

inventory={'coins': 10, 'apples': 3}

#START GAME

print("You have fallen into Hell. Survive the nine levels to escape.")
print("---")
print(f"{player_stats}")
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

