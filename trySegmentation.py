''' Create seed vectors for all phonemes. 
10K dimension, random equally probably +1s and -1s
'''

import numpy as np

def createSeedVector():
	phonemeList = [" ", "#", "%", "&", "(", ")", "*", "3", "6", "7", "9", "A", "D", "E", "G", "I", "L", "M", "N", "O", "Q", "R", "S", "T", "U", "W", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u", "v", "w", "y", "z", "~"]
	phonemes = {}
	for key in phonemeList:
		phonemes[key] = np.random.choice([-1, 1], size=10000)
	return phonemes

def evalUtterance(utterance, languageVector):
	n = len(utterance)
	
	storedWord = ""
	spaceIndexes = []
	# try to predict next letters
	for i in range(2, n):
		try:
			predictedLetter = printNext(utterance[i-2: i], phonemes, languageVector)[0]
		except:
			predictedLetter = None
		# print("WORD", utterance[i-2: i])
		# print("PREDICTION", predictedLetter)

		if (predictedLetter == utterance[i]):
			storedWord += predictedLetter
		else:
			if len(storedWord) != 0:
				# print("INSERT SPACE NOW!")
				# print("stored word", storedWord, "\n")
				spaceIndexes.append(i)
				storedWord = ""
			else:
				storedWord = ""

	# print(spaceIndexes)
	for count, i in enumerate(spaceIndexes):
		utterance = utterance[0:i + count] + " " + utterance[i + count:]
		# print("ADDED SPACE:", utterance)

	# print("NEW UTTERANCE IS", utterance)
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

		languageVector += multiplyResult

	return languageVector, utterance

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
	for i in range(1):
		letter = max(comparePhonemes, key=comparePhonemes.get)
		# print(letter, comparePhonemes[letter])
		# if comparePhonemes[letter] > 9000:
			# print(word, letter)
		# print("THE LETTER IS", letter)

		if (comparePhonemes[letter]) != 0:
			if comparePhonemes[letter] > 2000:
				letterResults.append(letter)
		comparePhonemes.pop(letter)

	# print(letterResults)
	return letterResults

if __name__ == "__main__":
	phonemes = createSeedVector()
	languageVector=np.zeros(10000)
	# languageVector = evalUtterance("yu want tu si D6 bUk", languageVector)
	# print(printNext("wa", phonemes, languageVector))

	# with open('../data/Bernstein-Ratner87', "r") as text:
	# 	for count, line in enumerate(text):
	# 		# removes spaces and new line
	# 		# processedLine = line.replace('\n', '').replace(' ', '')

	# 		processedLine = line.replace('\n', '')

	# 		languageVector = evalUtterance(processedLine, languageVector)

	# print(printNext("It", phonemes, languageVector))
	# print(printNext("an", phonemes, languageVector))

	with open('data/Bernstein-Ratner87', "r") as text:
		with open('results/result.txt','w') as result:
			for count, line in enumerate(text):
				processedLine = line.replace('\n', '').replace(' ', '')

				languageVector, segmentedUtterance = evalUtterance(processedLine, languageVector)
				print(segmentedUtterance)
				result.write(segmentedUtterance + "\n")

		# print(printNext("uw", phonemes, languageVector))

