from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem.snowball import SnowballStemmer
from nltk.stem import PorterStemmer
import nltk

# If you get an error uncomment this line and download the necessary libraries
#nltk.download()
# Corpus is basically a set of popular words that may be omitted while summarizing. They are called stopwords
# Tokenizer is basically breaking them into different ones
# Stemmer is basically a library that does intelligent parsing on words rooting out punctuations

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
# The entire logic is keeping words which have higher frequency while maintaining context. Therefore we dont change the sentence reordering and in a way hash the sentences
sentences = sent_tokenize(text)
sentenceValue = dict()

for sentence in sentences:
	for word in freqTable:
		if word in sentence.lower():
			if sentence in sentenceValue:
				sentenceValue[sentence] += freqTable[word]
			else:
				sentenceValue[sentence] = freqTable[word]



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