''' Create seed vectors for all phonemes. 
10K dimension, random equally probably +1s and -1s
'''

import numpy as np

def createSeedVector():
	phonemes = {" ": 1, "#": 1, "%": 1, "&": 1, "(": 1, ")": 1, "*": 1, "3": 1, "6": 1, "7": 1, "9": 1, "A": 1, "D": 1, "E": 1, "G": 1, "I": 1, "L": 1, "M": 1, "N": 1, "O": 1, "Q": 1, "R": 1, "S": 1, "T": 1, "U": 1, "W": 1, "Z": 1, "a": 1, "b": 1, "c": 1, "d": 1, "e": 1, "f": 1, "g": 1, "h": 1, "i": 1, "k": 1, "l": 1, "m": 1, "n": 1, "o": 1, "p": 1, "r": 1, "s": 1, "t": 1, "u": 1, "v": 1, "w": 1, "y": 1, "z": 1, "~": 1}
	for key in phonemes:
		phonemes[key] = np.random.choice([-1, 1], size=10000)
	return phonemes

def evalUtterance(utterance, languageVector=None):
	n = len(utterance)
		
	# encode trigrams into the languageVector
	for i in range(2, n):
		# print(i, "time!")
		firstLetter = utterance[i-2]
		secondLetter = utterance[i-1]
		thirdLetter = utterance[i]

		# print(firstLetter, secondLetter, thirdLetter)
		first = np.concatenate([phonemes[firstLetter][2:], phonemes[firstLetter][0:2]])
		second = np.concatenate([phonemes[secondLetter][1:], phonemes[secondLetter][0:1]])
		third = phonemes[thirdLetter]

		multiplyResult = np.multiply( np.multiply(first, second), third)

		if languageVector == None:
			languageVector = multiplyResult
		else:
			languageVector += multiplyResult

	return languageVector

def printNext(word, phonemes, languageVector):
	n = len(word)
	if n == 0:
		return

	Q = None

	comparePhonemes = phonemes.copy()

	first = np.concatenate([phonemes[word[0]][2:], phonemes[word[0]][0:2]])
	second = np.concatenate([phonemes[word[1]][1:], phonemes[word[1]][0:1]])

	Q = first * second

	# for i in range(n):
		# letterRotated = np.concatenate([phonemes[word[i]][i + 1:], phonemes[word[i]][0:i + 1]])

		# if (Q == None):
		# 	Q = letterRotated
		# else:
		# 	Q *= letterRotated

	for phoneme in phonemes:
		comparePhonemes[phoneme] = np.dot(phonemes[phoneme], languageVector * Q)

	# find highest 3 letters
	letterResults = []
	for i in range(3):
		letter = max(comparePhonemes, key=comparePhonemes.get)
		# print("THE LETTER IS", letter)
		comparePhonemes.pop(letter)
		letterResults.append(letter)

	return letterResults

if __name__ == "__main__":
	phonemes = createSeedVector()
	# print(phonemes)
	languageVector = evalUtterance("yu want tu si D6 bUk")
	print("language vector is", languageVector)
	print(printNext("wa", phonemes, languageVector))

	# with open('data/Bernstein-Ratner87', "r") as text:
	# 	with open('results/result.txt','w') as result:

	# 		for count, line in enumerate(text):
	# 			processedLine = line.replace('\n', '').replace(' ', '')

	# 			segmentedWord = evalUtterance(processedLine)
	# 			print(segmentedWord)
	# 			result.write(segmentedWord + "\n")

	# 			exit()