#Import RegEx
from dictionary import *

#Keep looping the command inputs.
def solveProblem():

	wordSolved = 0
	while (not wordSolved):

		#Request word input
		print("Enter the currently known letters and use \".\" if the letter is unknown.")
		word_input = input("Enter word: ")
		print("Enter letters that you have tried without spaces. Press enter if no letters listed.")
		tried_input = input("Tried letters: ")

		matches = getMatches(word_input, tried_input)

		if(len(matches) > 5):
			print("Too many possible results to guess.")
			outputTuple = getLetterProbability(word_input, matches)
			print("The next most likely letter is an \"" + outputTuple[0] + "\" with a chance of " + outputTuple[1] + "%")
		elif(len(matches) == 1):
			print("The word is " + matches[0])
			wordSolved = 1
		elif(len(matches) == 0):
			print("There is no matching word")
			return;
		else:
			print("Your answer is one of the following:")
			for word in matches:
				print(word)

		print("---");