#2019 -GCSE

letters_to_morse = {
    " ": "/",
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "0": "-----",
    ".": ".-.-.-",
    ",": "--..--",
    "?": "..--.."
}

def accept_input():
	while True:
		print("Enter text to be translated into Morse code")
		text = input()
		return text

def translate_to(text):
	text = text.lower()
	tlist = list(text)
	mlist = []
	for i in tlist:
		mlist.append(letters_to_morse[i])
	morse = " ".join(mlist)
	return (morse)

def main():
	return translate_to(accept_input())

print(main())