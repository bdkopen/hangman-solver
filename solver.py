#Import RegEx
import re

def convertToPercent(numerator, total):
	return str( round(numerator / total*100, 1) ) + "%"

def getLetterProbability(word_input, matches):
	#Define an array for each letter. Index 0 = a, index 25 = z.
	letters = [0]*26
	letter_total = 0
	for x in range(0, len(word_input)):
		for match in matches:
			if(word_input[x] == "." and ord(match[x]) >= 97 and ord(match[x]) <= 122):
				#print(str(x) + " " + match[x] + " " + match + " " + str(ord(match[x])-97))
				#print(ord(match[x])-97)
				#Add letter to respective array
				letters[ord(match[x])-97] += 1
				letter_total += 1

	return("The next most likely letter is an \"" + str(chr(letters.index(max(letters))+97)) + "\" with a chance of " + str(convertToPercent(max(letters), letter_total)) + "%")




w10 = open("scowl/final/english-words.10", 'r', encoding="latin-1")
w20 = open("scowl/final/english-words.20", 'r', encoding="latin-1")
w35 = open("scowl/final/english-words.35", 'r', encoding="latin-1")
w40 = open("scowl/final/english-words.40", 'r', encoding="latin-1")
w50 = open("scowl/final/english-words.50", 'r', encoding="latin-1")
w55 = open("scowl/final/english-words.55", 'r', encoding="latin-1")
w60 = open("scowl/final/english-words.60", 'r', encoding="latin-1")
w70 = open("scowl/final/english-words.70", 'r', encoding="latin-1")
w80 = open("scowl/final/english-words.80", 'r', encoding="latin-1")
w95 = open("scowl/final/english-words.95", 'r', encoding="latin-1")

v1_10 = open("scowl/final/variant_1-words.10", 'r', encoding="latin-1")
v1_20 = open("scowl/final/variant_1-words.20", 'r', encoding="latin-1")
v1_35 = open("scowl/final/variant_1-words.35", 'r', encoding="latin-1")
v1_40 = open("scowl/final/variant_1-words.40", 'r', encoding="latin-1")
v1_50 = open("scowl/final/variant_1-words.50", 'r', encoding="latin-1")
v1_55 = open("scowl/final/variant_1-words.55", 'r', encoding="latin-1")
v1_60 = open("scowl/final/variant_1-words.60", 'r', encoding="latin-1")
v1_70 = open("scowl/final/variant_1-words.70", 'r', encoding="latin-1")
v1_80 = open("scowl/final/variant_1-words.80", 'r', encoding="latin-1")
v1_95 = open("scowl/final/variant_1-words.95", 'r', encoding="latin-1")

v2_10 = open("scowl/final/variant_1-words.10", 'r', encoding="latin-1")
v2_20 = open("scowl/final/variant_1-words.20", 'r', encoding="latin-1")
v2_35 = open("scowl/final/variant_1-words.35", 'r', encoding="latin-1")
v2_40 = open("scowl/final/variant_1-words.40", 'r', encoding="latin-1")
v2_50 = open("scowl/final/variant_1-words.50", 'r', encoding="latin-1")
v2_55 = open("scowl/final/variant_1-words.55", 'r', encoding="latin-1")
v2_60 = open("scowl/final/variant_1-words.60", 'r', encoding="latin-1")
v2_70 = open("scowl/final/variant_1-words.70", 'r', encoding="latin-1")
v2_80 = open("scowl/final/variant_1-words.80", 'r', encoding="latin-1")
v2_95 = open("scowl/final/variant_1-words.95", 'r', encoding="latin-1")

v3_10 = open("scowl/final/variant_1-words.10", 'r', encoding="latin-1")
v3_20 = open("scowl/final/variant_1-words.20", 'r', encoding="latin-1")
v3_35 = open("scowl/final/variant_1-words.35", 'r', encoding="latin-1")
v3_40 = open("scowl/final/variant_1-words.40", 'r', encoding="latin-1")
v3_50 = open("scowl/final/variant_1-words.50", 'r', encoding="latin-1")
v3_55 = open("scowl/final/variant_1-words.55", 'r', encoding="latin-1")
v3_60 = open("scowl/final/variant_1-words.60", 'r', encoding="latin-1")
v3_70 = open("scowl/final/variant_1-words.70", 'r', encoding="latin-1")
v3_80 = open("scowl/final/variant_1-words.80", 'r', encoding="latin-1")
v3_95 = open("scowl/final/variant_1-words.95", 'r', encoding="latin-1")


#We want to support the full dictionary, including regional spelling (ex: gray vs grey, color vs colour, etc.)
files = [w10, w20, w35, w40, w50, w55, w60, w70, w80, w95,
		v1_10, v1_20, v1_35, v1_40, v1_50, v1_55, v1_60, v1_70, v1_80, v1_95,
		v2_10, v2_20, v2_35, v2_40, v2_50, v2_55, v2_60, v2_70, v2_80, v2_95,
		v3_10, v3_20, v3_35, v3_40, v3_50, v3_55, v3_60, v3_70, v3_80, v3_95
		]


#words = [word.rstrip('\n') for word in files[0]]

words = []
for file in files:
	words += [word.rstrip('\n') for word in file]


words.sort()

#Initiate the nested array that the words will be stored into.
words_array = []
for i in range(1000):
	words_array.append([])

#Store words into a list based on the word length
for word in words:
	words_array[len(word)].append(word)


#Keep looping the command inputs.
while True:

	#Request word input
	print("Enter the currently known letters and use \".\" if the letters are unknown.")
	word_input = input("Enter word: ")
	print("Enter letters that you have tried without spaces. Press enter if no letters listed.")
	tried_input = input("Tried letters: ")

	# Create an exclusion regex only if letters have been tried.
	regex = word_input
	if(tried_input != ""):
		regex = regex.replace(".", "[^"+tried_input+"]")

	#Search through words to find ones that meet the RegEx.
	matches = []
	for word in words_array[len(word_input)]:
		if re.search(regex, word):
			matches.append(word)

	if(len(matches) > 5):
		print("Too many possible results to guess.")
		print( getLetterProbability(word_input, matches) );
	elif(len(matches) == 1):
		print("The word is " + matches[0])
	elif(len(matches) == 0):
		print("There is no matching word")
	else:
		print("Your answer is one of the following:")
		for word in matches:
			print(word)

	print("---");