''' Create seed vectors for all phonemes. 
10K dimension, random equally probably +1s and -1s
'''

import numpy as np

# distinctive features
def createSeedVector():
	phonemeList = [" ", "#", "%", "&", "(", ")", "*", "3", "6", "7", "9", "A", "D", "E", "G", "I", "L", "M", "N", "O", "Q", "R", "S", "T", "U", "W", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u", "v", "w", "y", "z", "~"]
	phonemes = {}
	for key in phonemeList:
		phonemes[key] = np.random.choice([-1, 1], size=10000)
	return phonemes

def evalUtterance(utterance, languageVector):
	n = len(utterance)
		
	# encode trigrams into the languageVector
	# wan = rr(w) + r(a) + n
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
	languageVector=np.zeros(10000)
	# languageVector = evalUtterance("yu want tu si D6 bUk", languageVector)
	# print(printNext("an", phonemes, languageVector))

	with open('data/Bernstein-Ratner87', "r") as text:
		for count, line in enumerate(text):
			# removes spaces and new line
			# processedLine = line.replace('\n', '').replace(' ', '')

			processedLine = line.replace('\n', '')

			languageVector = evalUtterance(processedLine, languageVector)

	print(printNext("It", phonemes, languageVector))
	print(printNext("an", phonemes, languageVector))