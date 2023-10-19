#2022 -ALevel

import os
import random
os.system("cls")
subclasses = []
powers = []
items = ["Healing Potions", "Xp boost potion", "Sword", "Armour", "Battle Axe", "Helmet"]
races = ["Ork", "Human", "Elf", "Centaur", "Giant", "Mermaid", "???", "Gremlin", "Vampire"]

class character:
    def __init__(self, clas, subclas, item, gender, strength, magic, dexterity, charisma, power):
        #A class which I am using to hold all of the character's attributes in one place, this can also be used to use the randomly generated character's stats in a game
        self.c = clas
        self.subc = subclas
        self.g = gender
        self.s = strength
        self.m = magic
        self.d = dexterity
        self.p = power
        self.i = item
        self.ch = charisma
        self.r = random.choice(races)

def randomname():
    #The name generator for the character
    adjective = ["Big", "Hungry", "Hench", "Feeble", "Powerful", "Magic"]
    prefix = ["Sho", "Doh", "Bam", "Cho", "Tan", "Akk", "Pan"]
    middle = ["bam", "gen", "lim", "lam", "sip", "aaa", "doo"]
    suffix = ["cho", "san", "lan", "car", "bar", "nia", "man", "don"]
    name = (random.choice(adjective), random.choice(prefix) + random.choice(middle) + random.choice(suffix))
    name = " ".join(name)
    return name

def addtofile(x):
    #A procedure which adds something to the file
    f = open("Stats.txt", "a")
    f.write(str(x)+"\n")
    f.close

def input_class():
    #User input for their class, this also adds subclasses, powers and some special items for each choosable class
    print("Choose a class:")
    print("a) Mage")
    print("b) Paladin")
    print("c) Bard")
    print("d) Cleric")
    print("e) Druid")
    print("")
    while True:
        choice = input()
        choice = choice.lower()
        if choice == "mage" or choice == "a":
            subclasses.append("Flame")
            subclasses.append("Water")
            subclasses.append("Wind")
            powers.append("Fire ball")
            powers.append("Magic hat")
            powers.append("Light blade")
            return "Mage"
            break
        elif choice == "paladin" or choice == "b":
            items.append("Cross")
            subclasses.append("Unholy")
            subclasses.append("Holy")
            powers.append("Ritual")
            powers.append("Sacrafice")
            powers.append("Summon")
            return "Paladin"
            break
        elif choice == "bard" or choice == "c":
            items.clear()
            items.append("Guitar")
            items.append("Cello")
            items.append("Keytar")
            items.append("Piano")
            items.append("Otamatone")
            subclasses.append("Harmonious")
            subclasses.append("Rock")
            subclasses.append("Heavy Metal")
            powers.append("Screech")
            powers.append("Power chord")
            powers.append("Strum")
            return "Bard"
            break
        elif choice == "cleric" or choice == "d":
            items.clear()
            items.append("Health potions")
            items.append("Stim")
            items.append("Health kit")
            subclasses.append("Bandage")
            subclasses.append("Magic")
            powers.append("Revive")
            powers.append("UnBreak")
            return "Cleric"
            break
        elif choice == "druid" or choice == "e":
            items.append("Stick")
            subclasses.append("Tree")
            subclasses.append("Animorph")
            powers.append("Transform")
            powers.append("Grow")
            powers.append("Life drain")
            return "Druid"
            break
        else:
          print("That is not a valid input, please enter a letter or a class name")

def input_gender():
    #Gender input from the user
    print("")
    return input("Enter your character's gender: ")

def generatecharacter():
    #The character generator- also adds the character to the Stats.txt file
    char = character(input_class(), random.choice(subclasses), random.choice(items), input_gender(), random.randint(1, 100), random.randint(1, 100), random.randint(1, 100), random.randint(1, 100), random.choice(powers))
    addtofile("""
    {}
      {} {}

    Race: {}
    Gender: {}
    Power: {}
    Item: {}

   -- STATS -- 
    Strength: {} {}
    Magic: {} {}
    Dexterity: {} {}
    Charisma: {} {}
    """.format(randomname(), char.subc, char.c, char.r, char.g, char.p, char.i, "|| "*int(char.s/10), char.s, "|| "*int(char.m/10), char.m, "|| "*int(char.d/10), char.d, "|| "*int(char.ch/10), char.ch))

def main():
    generatecharacter()
    os.system("cls")
    f = open("Stats.txt", "r")
    for line in f:
        print(line)

main()