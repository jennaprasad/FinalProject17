player_hp=100
player_attack=10
player_stats=(f"Health: {player_hp}, Attack: {player_attack}")

class Resident(object):
    def __init__(self, name, bio, gift):
        self.name=name
        self.bio=bio
        self.gift=gift
socrates=Resident('Socrates', '', '3 coins')
cleopatra=Resident('Cleopatra', '', '3 coins')
ciacco=Resident('Ciacco', '', '3 coins')
avaricious=Resident('Avaricious', '', '3 coins')
filippo=Resident('Filippo Argenti', '', '3 coins')
epicurus=Resident('Epicurus', '', '3 coins')
alexander=Resident('Alexander the Great', '', '3 coins')
ulysses=Resident('Ulysses', '', '3 coins')
judas=Resident('Judas', '', '3 apples')

def introduce(self):
    print(f"My name is {self.name}. {self.bio}. You have a long journey ahead-- take these.")

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
    print(f"{self.name} guards the door to the next level.")
    print("---")
    print(f"{self.stats}, {self.attack}")

class Level(object):
    def __init__(self, name3, level, description):
        self.name3=name3
        self.level=level
        self.description=description
one=Level('Limbo', 'Level 1', '')
two=Level('Lust', 'Level 2', '')
three=Level('Gluttony', 'Level 3', '')
four=Level('Greed', 'Level 4', '')
five=Level('Wrath', 'Level 5', '')
six=Level('Heresy', 'Level 6', '')
seven=Level('Violence', 'Level 7', '')
eight=Level('Malebolge', 'Level 8', '')
nine=Level('Treachery', 'Level 9', '')

def enter(self):
    print(f"Enter {self.level}: {self.name3}")

inventory={'coins': 10, 'apples': 3}


#start

print("You have fallen into Hell. Survive the nine levels to escape.")
print("---")
print(f"{player_stats}")
print(f"{inventory}")
enter(one)
print(f"{one.description}")
print("---")
print('To keep walking, press "w". To shop, press "s". If a resident of Hell approaches, press "t" to talk.')
print('Continue walking ("w") or shop ("s")?')
