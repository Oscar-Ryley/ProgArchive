#2019-2020 -GCSE

import os
import random
os.system("cls")

class enemy:
  def __init__(self, name, health, attack, lowest_lvl, spattkname, spattk):
    self.wealth = lowest_lvl * 10
    self.health = health
    self.attack = attack
    self.spattk = spattk
    if player.level > 10:
      self.health = ((player.level/5) * health)
      self.attack = ((player.level/5) * attack)
      self.spattk = ((player.level/5) * spattk)
    elif player.level > 20:
      self.health = ((player.level/4) * health)
      self.attack = ((player.level/4) * attack)
      self.spattk = ((player.level/4) * spattk)
    elif player.level > 30:
      self.health = ((player.level/3.5) * health)
      self.attack = ((player.level/3.5) * attack)
      self.spattk = ((player.level/3.5) * spattk)
    elif player.level > 60:
      self.health = ((player.level/2) * health)
      self.attack = ((player.level/2) * attack)
      self.spattk = ((player.level/2) * spattk)
    elif player.level > 100:
      self.health = (player.level * health)
      self.attack = (player.level * attack)
      self.spattk = (player.level * spattk)
    self.name = str(name)
    self.lowest_lvl = lowest_lvl
    self.spattkname = spattkname

class player:
  def __init__(self):
    self.health = 80
    self.maxhealth = 80
    self.attack = 10
    self.level = 1
    self.aord = 1
    self.money = 0
player = player()

class item_:
  def __init__(self, name, bool_, number, stataffected, affect):
    self.name = name
    self.b = bool_
    self.n = number
    self.s = stataffected
    self.a = affect

class item:
  def __init__(self, current):
    self.current = current

def numberintheshop(cost):
  afford = False
  while True:
   if afford == False:
    if cost > player.money:
      print("You can't afford this")
      numberofitems = 0
      return numberofitems
    while True:
      numberofitems = input("How many do you want to buy?")
      if numberofitems.isdigit() == True:
        if player.money >= cost * int(numberofitems):
          player.money -= cost * int(numberofitems)
          numberofitems = int(numberofitems)
          return numberofitems
          break
        else:
          print("You can't afford that many")
          numberofitems = 0
          afford = True
  return numberofitems

def decision():
  while True:
    if opponent.health <= 0:
       break
    
    print("""
 ________________              You (lvl. {})
|::: {} :::
|----------------     vs.
| Health: {}                   Health: {}
| Attack: {}                   Attack: {}
|________________
""" .format(player.level, opponent.name, opponent.health, player.health, opponent.attack, player.attack))
    print("")
    if item.current.b == 1 and item.current.n > 0:
      if item.current.n > 1:
        plural = "s"
      else:
        plural = ""
      
      print("Attack, Defend or use your Item (", item.current.name + plural , "x", item.current.n, ")")
      choice = input()
      if choice == "attack" or choice == "a":
        player.aord = 1
        break
      elif choice == "defend" or choice == "d":
        player.aord = 0
        break
      elif choice == "item" or choice == "i":
        player.aord = 2
        break
      else:
        print("*** please enter 'attack', 'defend' or 'item' ***")
    else:
      print("Attack or Defend?")
      choice = input()
      if choice == "attack" or choice == "a":
        player.aord = 1
        break
      elif choice == "defend" or choice == "d":
        player.aord = 0
        break
      else:
        print("*** please enter 'attack' or 'defend' ***")

def attacksyou():
  spattack = 0
  if opponent.health > 0:
   if random.randint(1, 12) == 12 and player.aord != 0:
     print("The opponent uses it's", opponent.spattkname, "attack    -{}" .format(opponent.spattk))
     print("")
     spattack = 1
   else:
     print("The", opponent.name, "attacks you    -{}" .format(opponent.attack))
     print("")
   if player.aord == 0:
      print("you defend the", opponent.name, "'s attack    ", player.attack/2, "damage")
      print("")
      if random.randint(1, 12) == 12:
        print("LUCKY SAVE")
        opponent.health -= player.attack / 2
      else:
        opponent.health -= player.attack / 2
        player.health -= opponent.attack / 2
   elif spattack == 1:
      player.health -= opponent.spattk
   else:
     player.health -= opponent.attack

def attackit():
  if player.aord == 1:
    print("You attack the", opponent.name, "   ", player.attack, "damage")
    print("")
    if random.randint(1, 12) == 12:
      print("CRITICAL HIT!")
      print("")
      opponent.health -= player.attack *1.5
    else:
      opponent.health -= player.attack
    
    if opponent.health <= 0:
      print("You killed the", opponent.name)
      print("Health:", player.health)
      print("Attack:", player.attack)
      player.money += opponent.wealth
      print("Money:", player.money, "   (+{})" .format(opponent.wealth))
      while True:
        if player.level % 10 == 0:
          print("You level up from the grueling fight!")
          print("")
          player.maxhealth += 20
          player.attack += 10
          player.money += opponent.wealth
          player.health += 100
          if player.health > player.maxhealth:
              player.health = player.maxhealth
          player.level += 1
          print("LvL.", player.level)
          print("________")
          print("New Maximum Health:", player.maxhealth)
          print("New Attack:", player.attack)
          print("New Money:", player.money)
          input()
          break
        else:
          print("Would you like to level up, heal or visit the shop?")
          lorh = input()
          if lorh == "heal" or lorh == "h":
            print("You heal")
            player.health = player.maxhealth
            input()
            break
          elif lorh == "level up" or lorh == "l":
            print("You level up")
            print("")
            player.maxhealth += 20
            player.attack += 10
            
            player.health += 20
            if player.health > player.maxhealth:
               player.health = player.maxhealth
            player.level += 1
            print("LvL.", player.level)
            print("________")
            print("New Maximum Health:", player.maxhealth)
            print("New Attack:", player.attack)
            print("New Money:", player.money)
            input()
            break
          elif lorh == "shop" or lorh == "s":
            print("You visit the shop")
            print("You have", player.money, "coins")
            print("""
Douglas O'Dreary's Thing Emporium
---------------------------------
Healing potions - 100 coins each
Clubs - 300 coins each
Viles - 400 coins each
Apples - 500 coins each
            """)
            while True:
              item2 = input("What do you want to buy? ")
              if item2 == "nothing" or item2 == "none" or item2 == "no":
                print("You left the shop")
                break
              if item2 == "clubs" or item2 == "club" or item2 == "c":
                print("You picked the clubs")
                n = numberintheshop(300)
                if n == 0:
                  break
                else:
                 if item.current.n == 0:
                   item.current = item_("Club", 1, n, "attack", 30)
                 else:
                   t = item.current.n
                   item.current = item_("Club", 1, n + t, "attack", 30)
                 break
              if item2 == "healing potions" or item2 == "healing potions" or item2 == "h":
                print("You picked the health potions")
                n = numberintheshop(100)
                if n == 0:
                  break
                else:
                 if item.current.n == 0:
                   item.current = item_("Healing potion", 1, n, "health", 50)
                 else:
                   t = item.current.n
                   item.current = item_("Healing potion", 1, n + t, "health", 50)
                 break
              if item2 == "viles" or item2 == "vile" or item2 == "v":
                print("You picked the viles")
                n = numberintheshop(400)
                if n == 0:
                  break
                else:
                 if item.current.n == 0:
                   item.current = item_("Vile", 1, n, "maxhealth", 20)
                 else:
                   t = item.current.n
                   item.current = item_("Vile", 1, n + t, "maxhealth", 20)
                 break
              if item2 == "apples" or item2 == "apple" or item2 == "a":
                print("You picked the apples")
                n = numberintheshop(500)
                if n == 0:
                  break
                else:
                 if item.current.n == 0:
                   item.current = item_("Apple", 1, n, "level", 1)
                 else:
                   t = item.current.n
                   item.current = item_("Apple", 1, n + t, "level", 1)
                 break
              else:
                print("Please pick one or type 'nothing' to leave the shop with nothing")
  if player.aord == 2:
    print("You used your", item.current.name)
    print("")
    item.current.n -= 1
    if item.current.s == "attack":
      player.attack += item.current.a
    elif item.current.s == "health":
      player.health += item.current.a
      if player.health > player.maxhealth:
        player.health = player.maxhealth
    elif item.current.s == "maxhealth":
      player.maxhealth += item.current.a
    elif item.current.s == "level":
      while True:
        if player.level % 10 == 0:
          print("You level up from the grueling fight!")
          print("")
          player.maxhealth += 20
          player.attack += 10
          player.health += 100
          if player.health > player.maxhealth:
              player.health = player.maxhealth
          player.level += 1
          print("LvL.", player.level)
          print("________")
          print("New Maximum Health:", player.maxhealth)
          print("New Attack:", player.attack)
          input()
          break
        else:
          print("You level up")
          print("")
          player.maxhealth += 20
          player.attack += 10
          player.health += 20
          if player.health > player.maxhealth:
              player.health = player.maxhealth
          player.level += 1
          print("LvL.", player.level)
          print("________")
          print("New Maximum Health:", player.maxhealth)
          print("New Attack:", player.attack)
          input()
          break

print("""
R epetitive
P laying
G ame
          by Oscar Ryley
""")
input("      |START|")

while True:
  print("""
  Please Pick a special starting item!
  1. Healing potions
  2. Club
  3. Apple
  4. Vile
  0. Nothing
  """)
  item1 = input()
  if item1 == "nothing" or item1 == "0" or item1 == "n":
    print("You picked nothing!")
    current = item_("Nothing", 0, 0, "none", 0)
    item.current = current
    break
  if item1 == "club" or item1 == "2" or item1 == "c":
    print("You picked the club")
    current = item_("Club", 1, 1, "attack", 20)
    item.current = current
    break
  if item1 == "healing potions" or item1 == "1" or item1 == "h":
    print("You picked the healing potions")
    current = item_("Healing Potion", 1, 5, "health", 50)
    item.current = current
    break
  if item1 == "apple" or item1 == "3" or item1 == "a":
    print("You picked the apple")
    current = item_("Apple", 1, 1, "level", 1)
    item.current = current
    break
  if item1 == "vile" or item1 == "4" or item1 == "v":
    print("You picked the vile")
    current = item_("Vile", 1, 1, "maxhealth", 20)
    item.current = current
    break

while True:
  os.system("cls")
  
  # Enemy Guide
  # enemy(name, health, attack, lowest level they can appear, special attack name, special attack)

  ogre = enemy("Ogre", 100, 10, 2, "Sweep", 50)
  spider = enemy("Spider", 20, 15, 1, "Web Shot", 40)
  ghoul = enemy("Ghoul", 40, 5, 1, "Scare", 20)
  zombie = enemy("Zombie", 50, 10, 1, "Crunch", 30)
  ghost = enemy("Ghost", 80, 15, 2, "Scare", 50)
  headlesshorseman = enemy("Headless Horseman", 60, 20, 3, "Behead", 60)
  headlesshorse = enemy("Headless Horse", 60, 20, 3, "Behead", 60)
  gargoyle = enemy("Gargoyle", 70, 30, 4, "Rock slam", 60)
  banshee = enemy("Banshee", 80, 30, 5, "Scream", 65)
  birdperson = enemy("Bird Person", 80, 40, 6, "Swoop", 80)
  centaur = enemy("Centaur", 100, 40, 8, "Gallop", 50)
  deathworm = enemy("Death Worm", 150, 20, 11, "Burrow", 80)
  kelpie = enemy("Kelpie", 100, 40, 12, "Drown", 70)
  troll = enemy("Troll", 200, 20, 13, "Sweep", 80)
  slime = enemy("Slime", 120, 50, 14, "Globulet", 100)
  minotaur = enemy("Minotaur", 150, 70, 15, "Axe swing", 100)
  hordeofbats = enemy("Horde of bats", 180, 40, 16, "Barage", 100)
  
  monsters = [ogre, spider, ghoul, zombie, headlesshorseman, gargoyle, ghost, banshee, deathworm, kelpie, minotaur, birdperson, centaur, hordeofbats, slime, troll, headlesshorse]
  
  frankenstein = enemy("Frankenstein", 350, 60, 10, "Electricute", 100)
  swampthing = enemy("Swamp Thing", 400, 50, 10, "Drown", 120)
  dracula = enemy("Dracula", 150, 75, 20, "Bite", 100)
  dragon = enemy("Dragon", 250, 70, 30, "Fire-breath", 100)
  hydra = enemy("Hydra", 300, 40, 40, "Bite", 160)
  godzilla = enemy("Godzilla", 400, 60, 40, "Car throw", 100)
  thedevil = enemy("Devil", 500, 60, 40, "Burn", 200)
  cerberus = enemy("Cerberus", 300, 100, 50, "Crunch", 150)
  beelzebub = enemy("Beelzebub", 800, 30, 50, "Fly Lord", 60)
  angelofdeath = enemy("The Angel of Death", 200, 100, 60, "Death touch", 300)
  cthulhu = enemy("Cthulhu", 900, 125, 70, "Swipe", 250)

  bosses = [cthulhu, thedevil, dragon, beelzebub, angelofdeath, dracula, frankenstein, godzilla, cerberus, hydra, swampthing]
  
  motif = "."

  opponent = random.choice(monsters)
  while opponent.lowest_lvl > player.level:
    opponent = random.choice(monsters)
  
  if player.level % 10 == 0:
    print("BOSS FIGHT")
    opponent = random.choice(bosses)
    while opponent.lowest_lvl > player.level:
      opponent = random.choice(bosses)
    motif = "!"

  if player.health <= 0:
     print("________")
     print("You Died")
     print("At Lvl.", player.level)
     break
  
  print(opponent.name , "appeared!")
  print("It has", opponent.health, "Health and", opponent.attack, "Attack{}" .format(motif))
  
  while True:
   if player.health <= 0:
     break
   if opponent.health <= 0:
     break
   itemused = 0
   decision()
  
   eventorder = random.randint(1, 2)
   if eventorder == 1:
      attackit()
      attacksyou() 
   else:
      attacksyou() 
      attackit()  
   
   if opponent.health <= 0:
     break
  
   if player.health <= 0:
     print("________")
     print("You Died")
     print("At Lvl.", player.level)
     break   

   print("________")
   print("Lvl.", player.level)
   print("________")
   print("Health:", player.health)
   print("Attack:", player.attack)
   print("")
   print("{}'s Health: {}" .format(opponent.name, opponent.health))
   print("")
   input()
   os.system("cls")