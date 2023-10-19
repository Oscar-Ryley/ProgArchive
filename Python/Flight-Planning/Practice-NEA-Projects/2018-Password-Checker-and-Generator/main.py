import random

acceptedchar = []
f = open("acceptedchar.txt", "r")
lines = f.readlines()
for line in lines:
	line = line.replace("\n", "")
	acceptedchar.append(str(line))


def password_input():
	while True:
		quit = 0
		print("[enter a password:]")
		password = str(input())
		if len(password) < 8 or len(password) > 24:
			print(
			    "[Password must be more than 8 and less than 24 characters long]"
			)
			quit = 1
			pass
		plist = list(password)
		x = 1
		for i in plist:
			if i not in acceptedchar:
				x = 0
		if x == 0:
			print("[the password entered includes some banned characters]")
			print("[type 'a' to see the accepted characters]")
			quit = 1
			if input("") == "a":
				print("""[
    accepted characters:
@ Upper case letters (A to Z)
@ Lower case letters (a to z)
@ Digits (0 to 9)
@ Allowed symbols (! $ % ^ & * ( ) - _ = +)

passwords must be from 8 to 24 characters long
            ]""")

				pass
		if quit == 0:
			break
	return password


def check(p):
	p = str(p)
	score = len(p)

	#Points being Added
	acceptedp = ["!", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+"]
	upp = 0
	low = 0
	dig = 0
	pun = 0
	for i in p:
		if i == i.upper() and upp == 0:
			upp = 1
			score += 5
		elif i == i.lower() and low == 0:
			low = 1
			score += 5
		elif i.isdigit() == True and dig == 0:
			dig = 1
			score += 5
		for j in acceptedp:
			if i == j and pun == 0:
				pun = 1
				score += 5
	if upp == 1 and low == 1 and dig == 1 and pun == 1:
		score += 10

	#Points being Subtracted
	keyboardlayout = [
	    "q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f",
	    "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m"
	]
	if dig == 0 and pun == 0:
		score -= 5
	elif dig == 1 and upp == 0 and low == 0 and pun == 0:
		score -= 5
	elif pun == 1 and upp == 0 and low == 0 and dig == 0:
		score -= 5

	for i in range(0, len(str(p)) - 3):
		for j in range(0, len(keyboardlayout) - 3):
			if p[i].lower() == keyboardlayout[j] and p[i + 1].lower(
			) == keyboardlayout[j + 1] and p[i +
			                                 2].lower() == keyboardlayout[j +
			                                                              2]:
				score -= 5

	strength = ""
	if score < 0:
		strength = "weak"
	elif score > 20:
		strength = "strong"
	else:
		strength = "medium"

	return strength, score


def gen():
	while True:
		length = random.randint(8, 12)
		plist = []
		for i in range(0, length):
			plist.append(random.choice(acceptedchar))
		password = "".join(plist)
		s = check(password)
		if s[0] == "strong":
			return password, s[1]
			break


def menu():
	while True:
		print("""
**Password Checker and Generator**
    a) Check Password
    b) Generate Password
    c) Quit.
    """)
		choice = input()
		choice = choice.lower()
		if choice == "a" or choice == "check" or choice == "check password":
			printable = check(password_input())
			print(printable[0], " ", printable[1], "points")
			break
		elif choice == "b" or choice == "generate" or choice == "generate password":
			printable = gen()
			print(printable[0], " ", printable[1], "points", "(strong)")
			break
		elif choice == "quit" or choice == "c":
			print("[The program is suitably ending]")
			break
		else:
			print("[please enter either a, b or c]")


menu()
