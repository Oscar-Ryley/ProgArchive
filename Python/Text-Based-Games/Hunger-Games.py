#2019 -GCSE

import os
import random
os.system("cls")

def main():
  kills = ["stabbed", "poisoned", "throttled", "strangled", "pushed", "drowned", "shot"]
  groupkills = ["pushed", "stabbed", "pummeled", "snuck up upon"]
  
  goodkarma = ["bandaged their wounds", "got a gift of food from an unknown sponsor", "got a gift of water from an unknown sponsor", "got a gift of medical supplies from an unknown sponsor", "ate a restful meal", "thought about winning"]
  badkarma = ["fell over a rock", "made a fire", "tripped themselves up", "got scared", "injured themself running", "hit their own foot whilst hunting", "remembered home"]
  
  inspirational_quotes = ["Do or do not, there is no try", "All unsaved will be lost", "Press enter to continue through the game", "A journey of a thousand miles starts with a single step", "Rome wasn't burnt in a day", "...", "Thou shalt not terminate insanity", "May the odds always be ever in your favour", "Sting like a butterfly, Fly like a bee"]
  names = ["Charles", "Bob", "Horachio", "Ethan", "Ben", "Jesus", "Oscar", "Oliver", "Aayush", "Rohit", "Tom", "Oliver", "Ash", "Margret", "Theresa", "Benji", "Hilda", "David", "John", "Donald", "Luke", "Vladimir", "Boris", "Dmitri", "Sergei", "Ivan", "Roza", "Kira", "Ian", "Stuart", "Simon", "Ralph", "Jack", "Peter", "Sam", "Eric", "Roger", "Lenny", "Maurice", "Lesley", "Marcus", "Oliver", "Ashley", "Matthew"]

  day = 1
  namelist = []
  
  print("""
HUNGER GAMES
       - by Oscar Ryley
          __
         (  )
          ||
          ||           Randomly
         _||_          Generated
        |  | |         Enjoyment.
         \ | |
          \| |
           \ |           ______
            V           |      |
                        | 1  2 |
                        |__BSRB|
  """)
  print(random.choice(inspirational_quotes))
  print("   ___________________________")
  print("   Input your character names:")
  print("...")
  print("Enter 'random list of names' for a random list of names")
  print("...")
  x = 1
  t = 1
  y = 0
  while x < 13:
    while True:
     print("District" , x , ":")
     inp = input()
     if inp == "random list of names" and x == 1:
       t = 1
       while t < 25:
         namelist.append(random.choice(names))
         t += 1
     if inp != "":
       break
     else:
        print("*Enter a name*")
        print("")
    namelist.append(inp)
    if  y == 1:
      y = 0
      x += 1
    elif y == 0:
      y = 1
    if t != 1:
      break
  
  class player:
    def __init__(self, name, district):
      self.district = district
      self.name = name
      self.kills = 0
      self.karma = 2  

  p1a = player(namelist[0], 1)
  p1b = player(namelist[1], 1)
  p2a = player(namelist[2], 2)
  p2b = player(namelist[3], 2)
  p3a = player(namelist[4], 3)
  p3b = player(namelist[5], 3)
  p4a = player(namelist[6], 4)
  p4b = player(namelist[7], 4)
  p5a = player(namelist[8], 5)
  p5b = player(namelist[9], 5)
  p6a = player(namelist[10], 6)
  p6b = player(namelist[11], 6)
  p7a = player(namelist[12], 7)
  p7b = player(namelist[13], 7)
  p8a = player(namelist[14], 8)
  p8b = player(namelist[15], 8)
  p9a = player(namelist[16], 9)
  p9b = player(namelist[17], 9)
  p10a = player(namelist[18], 10)
  p10b = player(namelist[19], 10)
  p11a = player(namelist[20], 11)
  p11b = player(namelist[21], 11)
  p12a = player(namelist[22], 12)
  p12b = player(namelist[23], 12)
  
  namelist2 = [p1a, p1b, p2a, p2b, p3a, p3b, p4a, p4b, p5a, p5b, p6a, p6b, p7a, p7b, p8a, p8b, p9a, p9b, p10a, p10b, p11a, p11b, p12a, p12b]
  
  def action():
    teamer = random.choice(namelist2)

    if len(namelist2) != 1:
     currentdoer = random.choice(namelist2)
     deathstoday = []
     
     if random.randint(1, 4) == 4:
        died1 = currentdoer
        while died1.district == currentdoer.district and namelist2 != 2:
           died1 = random.choice(namelist2)
        died2 = died1.name
        print(currentdoer.name , random.choice(kills), died2)
        currentdoer.kills += 1
        deathstoday.append(died2)
        namelist2.remove(died1)

     elif currentdoer.karma < 1 and random.randint(1, 3) == 3:
        died1 = currentdoer
        while died1.district == currentdoer.district and namelist2 != 2:
           died1 = random.choice(namelist2)
        died2 = died1.name
        print(currentdoer.name , random.choice(kills), died2)
        currentdoer.name += 1
        deathstoday.append(died2)
        namelist2.remove(died1)

     elif random.randint(1, 12) == 12:
        if len(namelist2) > 4:
         friend1 = currentdoer
         while friend1 == currentdoer:
            friend1 = random.choice(namelist2)
        
         friend2 = currentdoer
         while friend2 == currentdoer or friend2 == friend1:
            friend2 = random.choice(namelist2)
        
         friend3 = currentdoer
         while friend3 == currentdoer or friend3 == friend1 or friend3 == friend2:
            friend3 = random.choice(namelist2)
        
         died1 = currentdoer
         while died1 == currentdoer or died1 == friend1 or died1 == friend2 or died1 == friend3:
            died1 = random.choice(namelist2)
        
         died2 = died1.name
         nooffriends = random.randint(1, 3)

         if nooffriends == 1:
            print(currentdoer.name, "and" , friend1.name, random.choice(groupkills), died2)
            currentdoer.kills += 1
            friend1.kills += 1
            namelist2.remove(died1)

         elif nooffriends == 2:
            print(str(currentdoer.name) + "," , friend1.name, "and", friend2.name, random.choice(groupkills), died2)
            currentdoer.kills += 1
            friend1.kills += 1
            friend2.kills += 1
            namelist2.remove(died1)

         elif nooffriends == 3:
            print(str(currentdoer.name) + "," , friend1.name, ",", friend2.name, "and" , friend3.name, random.choice(groupkills), died2)
            currentdoer.kills += 1
            friend1.kills += 1
            friend2.kills += 1
            friend3.kills += 1
            namelist2.remove(died1)

     elif random.randint(1, currentdoer.karma) == 1:
       print(currentdoer.name, random.choice(goodkarma))
       if currentdoer.karma != 1:
         currentdoer.karma -= 1

     elif random.randint(1, currentdoer.karma) == 2:
        print(currentdoer.name, random.choice(badkarma))
        currentdoer.karma += 1

     elif currentdoer.karma > 3:
       stupiddeath = random.randint(1,3)
       if stupiddeath == 1:
         print(currentdoer.name , "died of their wounds")
       if stupiddeath == 2:
         print(currentdoer.name , "fell off a cliff")
       if stupiddeath == 3:
         print(currentdoer.name , "fell out of a tree whilst napping")

     elif currentdoer.karma == teamer.karma:
        if teamer.name != currentdoer.name:
          print(currentdoer.name, "teamed up with", teamer.name)
          print("will this friendship last?")
          if currentdoer.karma != 1:
            currentdoer.karma -= 1
            teamer.karma -= 1
      
     print("")
  
  def actions():
    if len(namelist2) > 1:
      action()

  a = 1
  while len(namelist2) > 1 and a == 1:
   os.system("cls")
   print("_________________________")
   print("It is the morning on day" , day)
   print("")
   actions()
   actions()
   actions()

   print("_________________________")
   print("It is the evening on day" , day)
   print("")
   actions()
   actions()
   actions()

   print(len(namelist2), "people remain")
   day += 1
   input()
  
  if len(namelist2) == 1:
    print((namelist2[0]).name, "from District", (namelist2[0]).district , "has won!")
    print("They got", (namelist2[0]).kills , "kills" )

main()