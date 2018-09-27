from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem.snowball import SnowballStemmer
from nltk.stem import PorterStemmer
import nltk

# If you get an error uncomment this line and download the necessary libraries
#nltk.download()

text = "The solution proposed by Dijkstra was to include the third arrangement, also known as the “the interrupt”.  While thecomputer calculates at full speed, a piece of dedicated hardware monitors the outside world for completion signals from communication devices. When a completion is detected, the program under execution is interrupted after thecurrent instruction and in such a way such that it can be resumed at a later moment as if nothing happened, thus instantaneously freeing the central processor for a suddenly more urgent task."
stemmer = SnowballStemmer("english")
ps = PorterStemmer()
stopWords = set(stopwords.words("english"))
words = word_tokenize(text)

freqTable = dict()
for word in words:
	word = word.lower()
	if word in stopWords:
		continue

	word = ps.stem(word)

	if word in freqTable:
		freqTable[word] += 1
	else:
		freqTable[word] = 1

sentences = sent_tokenize(text)
sentenceValue = dict()

for sentence in sentences:
	for word, freq in freqTable.items():
		if word in sentence.lower():
			if sentence in sentenceValue:
				sentenceValue[sentence] += freq
			else:
				sentenceValue[sentence] = freq



sumValues = 0
for sentence in sentenceValue:
	sumValues += sentenceValue[sentence]

# Average value of a sentence from original text
average = int(sumValues / len(sentenceValue))


summary = ''
for sentence in sentences:
	if (sentence in sentenceValue) and (sentenceValue[sentence] > (1.1 * average)):
		summary += " " + sentence

print(summary)