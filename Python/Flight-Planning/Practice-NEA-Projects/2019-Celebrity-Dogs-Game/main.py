import random
import os

os.system('cls')
#basic clear screen command that is built into replit, normally I would use import os and os.system("cls")

global winner
winner = "p"
categories = ["e", "i", "f", "d"]
playerdeck = []
aideck = []

names = []
f = open("dogs.txt", "r")
lines = f.readlines()
for line in lines:
	line = line.replace("\n", "")
	names.append(str(line))


class card:
	def __init__(self, name, exercise, intelligence, friendliness, drool):
		self.n = name
		self.e = exercise
		self.i = intelligence
		self.f = friendliness
		self.d = drool


def getdecknumber():
	while True:
		print("Enter the number of cards in play:")
		totalcards = input()
		if totalcards.isdigit() == False:
			print("[please enter a number]")
			continue
		totalcards = int(totalcards)
		if totalcards % 2 == 0 and totalcards >= 4 and totalcards <= 30:
			print("[total number of cards in play entered successfully]")
			break
		else:
			print("[please enter an even number between 4 and 30]")
	return totalcards


def createdecks(n):
	cardsperdeck = int(int(n) / 2)
	for i in range(0, cardsperdeck):
		appendabledog = card(names[i], random.randint(1, 5),
		                     random.randint(1, 100), random.randint(1, 10),
		                     random.randint(1, 10))
		playerdeck.append(appendabledog)
	for i in range(0, cardsperdeck):
		appendabledog = card(names[i + cardsperdeck], random.randint(1, 5),
		                     random.randint(1, 100), random.randint(1, 10),
		                     random.randint(1, 10))
		aideck.append(appendabledog)
	random.shuffle(playerdeck)
	random.shuffle(aideck)


def printcard(card):
	print("""
        {}
    Exercise: {}/5
    Intelligence: {}/100
    Friendliness: {}/10
    Drool: {}/10
    """.format(card.n, card.e, card.i, card.f, card.d))


def pickcategory():
	while True:
		print("""
    Enter a Category:
  a) Exercise       (higher is better)
  b) Intelligence   (higher is better)
  c) Friendliness   (higher is better)
  d) Drool          (lower is better)
    """)
		category = input()
		if category == "a" or category == "e" or category == "exercise":
			return "e"
		elif category == "b" or category == "i" or category == "intelligence":
			return "i"
		elif category == "c" or category == "f" or category == "friendliness":
			return "f"
		elif category == "d" or category == "drool":
			return "d"
		print("")


def whowins(category):
	global winner
	if category == "d":
		if playerdeck[0].d < aideck[0].d:
			winner = "p"
		elif playerdeck[0].d == aideck[0].d:
			winner = "d"
		elif playerdeck[0].d > aideck[0].d:
			winner = "o"
	elif category == "e":
		if playerdeck[0].e > aideck[0].e:
			winner = "p"
		elif playerdeck[0].e == aideck[0].e:
			winner = "d"
		elif playerdeck[0].e < aideck[0].e:
			winner = "o"
	elif category == "i":
		if playerdeck[0].i > aideck[0].i:
			winner = "p"
		elif playerdeck[0].i == aideck[0].i:
			winner = "d"
		elif playerdeck[0].i < aideck[0].i:
			winner = "o"
	elif category == "f":
		if playerdeck[0].f > aideck[0].f:
			winner = "p"
		elif playerdeck[0].f == aideck[0].f:
			winner = "d"
		elif playerdeck[0].f < aideck[0].f:
			winner = "o"
	return winner


def round(w):
	if w == "o":
		print("AI card:")
		printcard(aideck[0])
		category = random.choice(categories)
		if category == "e":
			print("The AI has chosen the category exercise")
		elif category == "i":
			print("The AI has chosen the category intelligence")
		elif category == "f":
			print("The AI has chosen the category friendliness")
		else:
			print("The AI has chosen the category drool")
		print("Your card:")
		printcard(playerdeck[0])
	elif w == "p" or w == "d":
		print("Your card:")
		printcard(playerdeck[0])
		category = pickcategory()
		print("AI card:")
		printcard(aideck[0])
	return whowins(category)


def movecards(w):
	if w == "p":
		print("You WIN the round")
		playerdeck.append(playerdeck[0])
		playerdeck.append(aideck[0])
	elif w == "o":
		print("You LOSE the round")
		aideck.append(aideck[0])
		aideck.append(playerdeck[0])
	else:
		print("The round is a draw!")
		aideck.append(aideck[0])
		playerdeck.append(playerdeck[0])
	aideck.remove(aideck[0])
	playerdeck.remove(playerdeck[0])
	print("Cards in your hand", len(playerdeck))
	print("Cards in the AI's hand", len(aideck))
	print("")


def main():
	global winner
	createdecks(getdecknumber())
	input("[press enter to continue] ")
	os.system('cls')
	while True:
		movecards(round(winner))
		input("[press enter to continue] ")
		os.system('cls')
		if len(aideck) == 0:
			print("YOU WIN")
			print("[You have all of the cards in play]")
			break
		elif len(playerdeck) == 0:
			print("YOU LOSE")
			print("[The AI has all of the cards in play]")
			break


def menu():
	while True:
		print("""
**Celebrity Dogs Game**
    a) Play Game
    b) Quit.
    """)
		choice = input()
		choice = choice.lower()
		if choice == "a" or choice == "play" or choice == "play game":
			main()
			break
		elif choice == "quit" or choice == "b":
			print("[The program is suitably ending]")
			break
		else:
			print("[please enter either a or b]")


menu()
