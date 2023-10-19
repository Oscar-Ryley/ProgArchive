#2022 -ALevel
#RPG Game designed to work on a CG50 Graphical calculator

import random

class playerc():
    def __init__(self):
        self.n = "You"
        self.l = 1
        self.exp = 0
        self.a = 5
        self.h = 10
        self.c = 0
    
    def __repr__(self):
        return "You; atk:" + str(self.a) + ", hp:" + str(self.h)

    def levelup(self):
        if self.exp >= (self.l * self.a * self.h):
            self.exp = 0
            print("LEVELED UP")
            self.a -= 5 * self.l
            self.h -= 10 * self.l
            self.l += 1
            self.a += 5 * self.l
            self.h += 10 * self.l
            input()

    def heal(self):
        self.h += int((10*self.l)/2)
        if self.h > int(10*self.l):
            self.h = int(10*self.l)
    
    def die(self):
        if self.h > 0:
            return True
        else:
            return False
player = playerc()

class monster():
    def __init__(self, name, attack, health):
        self.n = name
        self.a = attack * player.l
        self.h = health * player.l
    
    def __repr__(self):
        return self.n + "; atk:" + str(self.a) + ", hp:" + str(self.h)

def intro():
    print("""
R epetitive
P laying
G ame
      by Oscar Ryley
""")
    input("     |START|")

def print_shop(patk_price, php_price, pl_price):
    print("""SHOP
(1)atk +5: {}
(2)hp +5: {}
(3)lvl +1: {}""" .format(patk_price, php_price, pl_price))

def shop(splayer):
    atk_price = splayer.l *50
    hp_price = splayer.l *75
    l_price = (splayer.l+1) *100
    print_shop(atk_price, hp_price, l_price)
    bchoice = input()
    if bchoice == "1":
        if splayer.c >= atk_price:
            splayer.c -= atk_price
            splayer.a += 5
        else:
            print("NOT ENOUGH $")
            input()
    elif bchoice == "2":
        if splayer.c >= hp_price:
            splayer.c -= hp_price
            splayer.h += 5
        else:
            print("NOT ENOUGH $")
            input()
    elif bchoice == "3":
        if splayer.c >= l_price:
            splayer.c -= l_price
            splayer.levelup()
        else:
            print("NOT ENOUGH $")
            input()
    return splayer

def attack(attacker, defender):
    new_health = defender.h - attacker.a
    print(attacker.n + " hit " + defender.n + " for " + str(attacker.a))
    return new_health

def print_turn(pplayer, propponent):
    print(pplayer)
    print("lvl", pplayer.l , "exp:" , pplayer.exp, "$:", pplayer.c)
    print(propponent)

def choice():
    while True:
        print("(1)Attack or (2)Heal")
        dchoice = input()
        try:
            if dchoice == "1" or dchoice == "2" or dchoice == "3":
                dchoice = int(dchoice)
                break
        except:
            pass
    return dchoice

def player_turn(ptplayer, ptopponent):
    cchoice = choice()
    if cchoice == 3 or cchoice == "shop":
        mhealth = ptopponent.h
        ptplayer = shop(ptplayer)
        cchoice = choice()
    if cchoice == 1:
        mhealth = attack(ptplayer, ptopponent)
    else:
        mhealth = ptopponent.h
        ptplayer.heal()

    if mhealth <= 0:
        print("You killed", ptopponent.n)
        ptplayer.exp += ptopponent.a * ptplayer.l
        ptplayer.c += ptopponent.h * 2
        ptopponent = "dead"
        input()

    else:
        ptopponent.h = mhealth

    return ptplayer, ptopponent

def monster_turn(mtplayer, mtopponent):
    if random.randint(1, 2) == 1:
        phealth = attack(mtopponent, mtplayer)
    else:
        print(mtopponent.n, "didn't attack!")
        phealth = mtplayer.h
    
    mtplayer.h = phealth

    if mtplayer.die() == False:
        pass

    else:
        mtplayer.h = phealth
    
    return mtplayer, mtopponent

def new_opp():
    monsters = define_monster_list()
    newi = random.randint(0, len(monsters)-1)
    return monsters[newi]

def opp_dead(odplayer, odopponent):
    if odopponent == "dead":
        odplayer.levelup()
        odopponent = new_opp()
    return odplayer, odopponent

def turn(turn_counter, tplayer, topponent):
    tplayer,topponent = opp_dead(tplayer, topponent)
    print("")
    print("Turn", turn_counter)
    
    while topponent != "dead" and tplayer.h > 0:
        print_turn(tplayer, topponent)
        tplayer,topponent = player_turn(tplayer, topponent)
        if topponent != "dead":
            tplayer,topponent = monster_turn(tplayer, topponent)
            input()
            print("")
    
    tplayer,topponent = opp_dead(tplayer, topponent)

    return tplayer.die()

def define_monster_list():
    ratman = monster("Ratman", 3, 7)
    daemon = monster("Daemon", 4, 7)
    goblin = monster("Goblin", 4, 6)
    dragon = monster("Dragon", 5, 8)
    troll = monster("Troll", 2, 10)
    slime = monster("Slime", 1, 6)
    hydra = monster("Hydra", 6, 7)
    ghost = monster("Ghost", 4, 4)
    ogre = monster("Ogre", 3, 10)
    devil = monster("Devil", 5, 7)

    monsters = [ratman, daemon, goblin, dragon, troll, slime, hydra, ghost, ogre, devil]

    return monsters

def main():         
    intro()
    cont = True
    turn_counter = 0
    opponent = "dead"
    while cont == True:
        turn_counter += 1
        cont = turn(turn_counter, player, opponent)
    print("GAME OVER")

main()