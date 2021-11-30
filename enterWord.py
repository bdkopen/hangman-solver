from dictionary import *
from art import draw

def enterWord():
	wordSolved = 0
	letters_guessed = ""
	last_input = ""
	bad_guesses = 0;

	while(not wordSolved):
		print("Enter your word with \".\" for all unknown letters")
		word_input = input("Enter word: ")

		if(word_input == last_input):
			draw(bad_guesses)
			if(bad_guesses > 5):
				print("You beat the computer!")
				return
			bad_guesses += 1


		matches = getMatches(word_input, letters_guessed)

		if(len(matches) > 1 ):
			returnTuple = getLetterProbability(word_input, matches)

			print("The computer guesses " + returnTuple[0] + ".")

			letters_guessed += returnTuple[0]

		elif(len(matches) == 1):
			print("The word is " + matches[0])
			wordSolved = 1
			return;
		elif(len(matches) == 0):
			print("There is no matching word")
			return;

		last_input = word_input;
