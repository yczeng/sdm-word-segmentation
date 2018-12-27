''' Create seed vectors for all phonemes. 
10K dimension, random equally probably +1s and -1s
'''

import numpy as np

phonemes = {" ": 1, "#": 1, "%": 1, "&": 1, "(": 1, ")": 1, "*": 1, "3": 1, "6": 1, "7": 1, "9": 1, "A": 1, "D": 1, "E": 1, "G": 1, "I": 1, "L": 1, "M": 1, "N": 1, "O": 1, "Q": 1, "R": 1, "S": 1, "T": 1, "U": 1, "W": 1, "Z": 1, "a": 1, "b": 1, "c": 1, "d": 1, "e": 1, "f": 1, "g": 1, "h": 1, "i": 1, "k": 1, "l": 1, "m": 1, "n": 1, "o": 1, "p": 1, "r": 1, "s": 1, "t": 1, "u": 1, "v": 1, "w": 1, "y": 1, "z": 1, "~": 1}

languageVector = np.zero(10000)

def createSeedVector(phonemes):
	for key in phonemes:
		phonemes[key] = np.random.choice([-1, 1], size=10000)

createSeedVector(phonemes)
print(phonemes)

def evalUtterance(utterance):

	n = len(utterance)

	# encode trigrams into the languageVector
	for i in range(2, n):
		firstLetter = utterance[i-2]
		secondLetter = utterance[i-1]
		thirdLetter = utterance[i]

		first = phoneme[firstLetter][2:] + phoneme[firstLetter][0:2]
		second = phoneme[secondLetter][1:] + phoneme[secondLetter][0:1]
		third = phoneme[thirdLetter]

		multiplyResult = np.multiply( np.multiply(first, second), third)

		languageVector += multiplyResult

def queryVector(word):
	

if __name__ == "__main__":
	with open('data/Bernstein-Ratner87', "r") as text:
		with open('results/result.txt','w') as result:

			for count, line in enumerate(text):
				processedLine = line.replace('\n', '').replace(' ', '')

				segmentedWord = evalUtterance(processedLine)
				print(segmentedWord)
				result.write(segmentedWord + "\n")