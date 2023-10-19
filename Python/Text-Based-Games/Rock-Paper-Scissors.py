#2019 -GCSE

import time
import os
import random

list_rps = ["Rock", "Paper", "Scissors"]

def play():
  AIscore = 0
  score = 0
  continuep = 1
  while continuep == 1:
    os.system('cls')
    p=1
    print("Play Rock, Paper, Scissors!")
    while p == 1:
     print("")
     print("Pick One:")
     print("A) Rock")
     print("B) Paper")
     print("C) Scissors")
     choice = input()
     if choice == "a":
        p= 0
        rps = "Rock"
     elif choice == "b":
        p= 0
        rps = "Paper"
     elif choice == "c":
        p= 0
        rps = "Scissors"
     else:
        p=1

    AIchoice = random.choice(list_rps)
    time.sleep(1)
    print("ROCK")
    time.sleep(0.1)
    print("PAPER")
    time.sleep(0.1)
    print("SCISSORS")
    time.sleep(0.5)
    print("SHOOT")
    print("")
    time.sleep(0.5)
    print(rps + " vs. " + AIchoice)
  
    if rps == "Rock" and AIchoice == "Scissors":
      print("You win!")
      score += 1
    elif rps == "Paper" and AIchoice == "Rock":
      print("You win!")
      score += 1
    elif rps == "Scissors" and AIchoice == "Paper":
      print("You win!")
      score += 1
    elif rps == AIchoice:
      print("You Draw!")
    else:
      print("You Lose")
      AIscore += 1
    
    print("")
    print("You: " + str(score))
    print("AI: " + str(AIscore))
    print("")

    print("Do you want to continue?")
    continuing = input()
    if continuing == "no":
      continuep = 0
    if continuing == "n":
      continuep = 0

def play2():
  score1 = 0
  score2 = 0
  continuep = 1
  print("Player One name:")
  p1name = input()
  print("Player Two name:")
  p2name = input()
  while continuep == 1:
    os.system('cls')
    p=1
    print( p2name +" look away! " + p1name +"...")
    while p == 1:
     print("")
     print("Pick One:")
     print("A) Rock")
     print("B) Paper")
     print("C) Scissors")
     choice = input()
     if choice == "a":
        p= 0
        choice1 = "Rock"
     elif choice == "b":
        p= 0
        choice1 = "Paper"
     elif choice == "c":
        p= 0
        choice1 = "Scissors"
     else:
        p=1
      
     os.system('cls')
    
    print( p1name +" look away! " + p2name +"...")
    p2 = 1
    while p2 == 1:
     print("")
     print("Pick One:")
     print("A) Rock")
     print("B) Paper")
     print("C) Scissors")
     choice = input()
     if choice == "a":
        p2= 0
        choice2 = "Rock"
     elif choice == "b":
        p2= 0
        choice2 = "Paper"
     elif choice == "c":
        p2= 0
        choice2 = "Scissors"
     else:
        p2=1
      
     os.system('cls')

    time.sleep(1)
    print("ROCK")
    time.sleep(0.1)
    print("PAPER")
    time.sleep(0.1)
    print("SCISSORS")
    time.sleep(0.5)
    print("SHOOT")
    print("")
    time.sleep(0.5)
    print(p1name+":"+choice1+"  "+p2name+":"+ choice2)
    print(choice1 + " vs. " + choice2)

    if choice1 == "Rock" and choice2 == "Scissors":
      print(p1name +" Wins!")
      score1 += 1
    elif choice1 == "Paper" and choice2 == "Rock":
      print(p1name +" Wins!")
      score1 += 1
    elif choice1 == "Scissors" and choice2 == "Paper":
      print(p1name +" Wins!")
      score1 += 1
    elif choice1 == choice2:
      print("Draw!")
    else:
      print(p2name +" Wins!")
      score2 += 1
    
    print("")
    print(p1name +": " + str(score1))
    print(p2name +": " + str(score2))
    print("")

    print("Do you want to continue?")
    continuing = input()
    if continuing == "no":
      continuep = 0
    if continuing == "n":
      continuep = 0

def game():
  os.system('cls')
  gamego = 1
  print("")
  print("Rock, Paper, Scissors!")
  print("")
  while gamego == 1:
    print("Do you want to play against a computer or against another person?")
    print("-(Computer or Person)")
    corp = input()
    if corp == "computer":
      play()
      gamego = 0
    if corp == "person":
      play2()
      gamego = 0

game()