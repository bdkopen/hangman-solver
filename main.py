from solver import solveProblem
from enterWord import enterWord
from guessWord import guessWord

def displayMenu():
	print("===========")
	print("  HANGMAN")
	print("===========")
	print("Select an Option:")
	print("1. Guess The Word")
	print("2. Enter The Word")
	print("3. Word Solver")

def guessTheWord():
	wordGuessed = 0
	while(not wordGuessed):
		print("Guess a word");

while(1):
	displayMenu();
	menu_input = input("Enter selection: ")
	if(menu_input == "1"):
		print("\nGuess The Word Selected")
		guessWord()

	elif(menu_input == "2"):
		print("\nEnter The Word Selected")
		enterWord()

	elif(menu_input == "3"):
		print("\nWord Solver Selected")
		solveProblem()

	else:
		print("\nInvalid input - Try again.\n")