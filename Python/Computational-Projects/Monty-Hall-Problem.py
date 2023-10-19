#2019 -GCSE

import os
import random
os.system('cls')

class stats:
  def __init__(self, wins_change, losses_change, wins_keep, losses_keep):
    self.wc = wins_change
    self.lc = losses_change
    self.wk = wins_keep
    self.lk = losses_keep

stats = stats(0, 0, 0, 0)

class door:
  def __init__(self, number, goat, n2):
    self.g = goat
    self.n = number
    self.nt = n2

def main():
  os.system('cls')
  one = door("1", False, 0)
  two = door("2", False, 1)
  three = door("3", False, 2)
  doors = [one, two, three]
  doors[random.randint(0, 2)].g = True
  print("THE MONTY HALL PROBLEM")
  print("----------------------")
  while True:
    print("Pick one of these doors")
    for i in range(0, len(doors)):
      print(doors[i].n)
    choice = input()
    if choice == "1":
      choice2 = one
      break
    elif choice == "2":
      choice2 = two
      break
    elif choice == "3":
      choice2 = three
      break
  os.system('cls')
  print("Now one of the wrong doors will be removed:")
  while True:
    deleted = random.randint(0, 2)
    if deleted != choice2.nt and doors[deleted].g == False:
      doors.remove(doors[deleted])
      break
  for i in range(0, len(doors)):
      print(doors[i].n)
  while True:
    print("Do you want to change your choice?")
    answer = input()
    if answer == "yes" or answer == "y" or answer == "change":
      doors.remove(choice2)
      choice2 = doors[0]
      change = 1
      break
    elif answer == "no" or answer == "n" or answer == "nope":
      change = 0
      break
  print("")
  if choice2.g == True:
    print(choice2.n, "was the right door")
    print("You win")
    print("The car is yours")
    print("""                                                                      /-----|
                              _.-="_-         _                       |  |  
                         _.-="   _-          | ||---------._______    ___..
             ___.===___-.______-_____________`-''----- -----       -----  __.
      __.--__     __        ,'                   o \           __        [__|
 __-__=======.--""  ""--.=================================.--""  ""--.=======:
]       [-] : /        \ : |========================|    : /        \ :  [-] [
\___________:|          |: |========================|    :|          |:   _-"
 \__________: \        / :_|=======================/_____: \        / :__-"
  ----------'  "-____-"  `-------------------------------'  "-____-"
    """)
    if change == 1:
      stats.wc += 1
    elif change == 0:
      stats.wk += 1
  else:
    print(choice2.n, "was the wrong door")
    print("You didn't pick the correct door")
    print("...So you lose")
    print("""
(_(
/_/'_____/)
"  |______|
   |      |
    """)
    if change == 1:
      stats.lc += 1
    elif change == 0:
      stats.lk += 1
  print("""
Changes: {}
  Wins: {}
  Losses: {}

Keeps: {}
  Wins: {}
  Losses: {}
  """.format((stats.wc+stats.lc), stats.wc, stats.lc, (stats.wk+stats.lk), stats.wk, stats.lk))

while True:
  main()
  input()