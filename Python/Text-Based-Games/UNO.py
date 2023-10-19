#2021 -ALevel

import random
import os
os.system("cls")

class card:
  def __init__(self, colour, name):
    self.c = colour
    self.n = name

class add_:
  def __init__(self, amount, type_):
    self.a = amount
    self.t = type_

def print_hand(hand):
  x = 0
  for i in hand:
    x+=1
    print(str(x)+":", i.c, i.n)

def generate_deck():
  colours = ["red", "yellow", "blue", "green"]
  numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "reverse", "+2", "cancel"]
  wilds = ["+4", "change colour"]
  deck = []
  for i in range(0,10000):
    if random.randint(0, 15) == 0:
      ccard = card("wild", random.choice(wilds))
    else:
      ccard = card(random.choice(colours), random.choice(numbers))
    deck.append(ccard)
  return deck

def start_hands(deck):
  p_hand = []
  cpu_hand1 = []
  cpu_hand2 = []
  cpu_hand3 = []
  hands = [p_hand, cpu_hand1, cpu_hand2, cpu_hand3]
  random.shuffle(deck)
  for i in hands:
    for j in range(0, 7):
      i.append(deck[0])
      deck.remove(deck[0])
  cc = deck[0]
  deck.remove(deck[0])
  if cc.c == "wild":
    colours = ["red", "yellow", "green", "blue"]
    cc.c = random.choice(colours)
  return hands,deck,cc

def p_turn(cc, hands, deck, add, r):
  print("Your hand:")
  print_hand(hands[0])
  print("What card would you like to play?")
  while True:
    x = 0
    d = 0
    cancel = 0
    add = add_(0, "+2")
    while True:
      choice = input()
      if choice.isdigit() == True:
        choice = int(choice)
        if choice <= len(hands[0]):
          choice -= 1
          choice = hands[0][choice]
          break
      if choice == "draw" or choice == "d":
        hands[0].append(deck[0])
        deck.remove(deck[0])
        d = 1
        break
      print("INVALID INPUT (enter a number or 'draw')")
    if d == 0:
      if choice.c == cc.c or choice.n == cc.n or choice.c == "wild":
        if choice.c == "wild":
          print("What colour do you want to change it to?")
          while True:
            c_choice = input()
            if c_choice.lower() == "y" or c_choice.lower() == "yellow":
              choice.c = "yellow"
              x = 1
              break
            elif c_choice.lower() == "b" or c_choice.lower() == "blue":
              choice.c = "blue"
              x = 1
              break
            elif c_choice.lower() == "g" or c_choice.lower() == "green":
              choice.c = "green"
              x = 1
              break
            elif c_choice.lower() == "r" or c_choice.lower() == "red":
              choice.c = "red"
              x = 1
              break
            else:
              print("INVALID INPUT")
        elif choice.n == "cancel":
          cancel = 1
        elif choice.n == "+2":
          add = add_(2, "+2")
        if choice.n == "+4":
          add = add_(4, "+4")
        if choice.n == "reverse":
          r = 1
        deck.append(cc)
        cc = choice
        hands[0].remove(choice)
        break
      else:
        print("You cannot play that card")
    if d == 1:
      break
  print("")
  return cc, hands, deck, cancel, add, r
  
def cpu_turn(cpu_num, cc, hands, deck, add, r):
  f = 0
  l = len(hands[cpu_num])
  cancel = 0
  add = add_(0, "+2")
  for i in hands[cpu_num]:
    if i.c == cc.c or i.n == cc.n or i.c == "wild":
      if i.c == "wild":
        colours = ["red", "green", "yellow", "blue"]
        i.c = random.choice(colours)
      elif i.n == "cancel":
        cancel = 1
      elif i.n == "+2":
        add = add_(2, "+2")
      if i.n == "+4":
        add = add_(4, "+4")
      if i.n == "reverse":
        r = 1
      print("CPU opponent", cpu_num, "plays a", i.c, i.n)
      deck.append(cc)
      cc = i
      hands[cpu_num].remove(i)
      break
    else:
      f += 1
  if f == l and f != 0:
    hands[cpu_num].append(deck[cpu_num])
    deck.remove(deck[cpu_num])
    print("CPU opponent", cpu_num, "draws 1 card")
  print("CPU opponent", cpu_num, "has", len(hands[cpu_num]), "card/s")
  print("")
  return cc, hands, deck, cancel, add, r

def check_win(hands):
  x = 0
  p = 0
  for i in range(0, 4):
    if len(hands[i]) == 0:
      if p == 0:
        print("Player Wins!")
        x = 1
        break
      else:
        print("CPU opponent", i, "Wins!")
        x = 1
        break
    elif len(hands[i]) == 1:
      if i == 0:
        print("UNO! for Player")
      else:
        print("UNO for CPU", i)
    p+=1
  return x

def turn(cpu_num, cc, hands, deck, cancel, add, r):
  if cpu_num == 0:
    print("Your Turn")
  else:
    print("CPU", str(cpu_num)+ "'s Turn")
  s = 0
  if add.a != 0:
    for i in hands[cpu_num]:
      if i.n == "+2" and add.t == "+2":
        print("A",i.c , i.n, "was stacked")
        print("")
        add.a += 2
        deck.append(cc)
        cc = i
        hands[cpu_num].remove(i)
        s = 1
        break
      elif i.n == "+4" and  add.t == "+4":
        print("A",i.c , i.n, "was stacked")
        if cpu_num == 0:
          print("What colour do you want to change it to?")
          while True:
            choice = input()
            if choice.lower() == "y" or choice.lower() == "yellow":
              i.c = "yellow"
              x = 1
            elif choice.lower() == "b" or choice.lower() == "blue":
              i.c = "blue"
              break
            elif choice.lower() == "g" or choice.lower() == "green":
              i.c = "green"
              break
            elif choice.lower() == "r" or choice.lower() == "red":
              i.c = "red"
              break
            else:
              print("INVALID INPUT")
          print("")
        else:
          colours = ["yellow", "blue", "red", "green"]
          i.c = random.choice(colours)
        add.a += 4
        deck.append(cc)
        cc = i
        hands[cpu_num].remove(i)
        s = 1
        break
    if s == 0:
      print(add.a, "cards were picked up")
      for i in range(0, add.a):
        hands[cpu_num].append(deck[0])
        deck.remove(deck[0])
      if cpu_num == 0:
        print("You now have", len(hands[cpu_num]), "cards")
      else:
        print("They now have", len(hands[cpu_num]), "cards")
      print("")
      add.a = 0
      s = 0
      return 0,cc,hands,deck,cancel,add,r
  if cancel == 0 and s == 0:
    print("The current card is", cc.c, cc.n)
    if cpu_num == 0:
      cc,hands,deck,cancel,add,r = p_turn(cc, hands, deck, add, r)
    else:
      cc,hands,deck,cancel,add,r = cpu_turn(cpu_num, cc, hands, deck, add, r)
    x = check_win(hands)
    if x == 1:
      return 1,cc,hands,deck,cancel,add,r
  elif s == 0:
    cancel = 0
    print("Turn cancelled")
    print("")
  return 0,cc,hands,deck,cancel,add,r

def start():
  print("UNO")
  print("")
  input("[press enter to begin]")
  os.system("cls")

def main():
  hands,deck,cc = start_hands(generate_deck())
  cancel = 0
  add = add_(0, "+2")
  r = 0
  x = 0
  order = [0, 1, 2, 3]
  start()
  while x == 0:
    x,cc,hands,deck,cancel,add,r = turn(order[0], cc, hands, deck, cancel, add, r)
    if x == 1:
      break
    if r == 1:
      order = [order[0], order[3], order[2], order[1]]
      r = 0
    order.append(order[0])
    order.remove(order[0])
    input("[continue]")
    print("")
  print("GAME OVER")
  input("[restart]")
  os.system("cls")

while True:
  main()