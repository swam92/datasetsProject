import csv
import nltk
from nltk.tokenize import word_tokenize
from textblob import TextBlob
from textblob.classifiers import NaiveBayesClassifier
from textblob.sentiments import NaiveBayesAnalyzer
import pprint

with open ("articles/boston/fox.txt", "r") as myfile:
    data=myfile.read().replace('\n', '')



train = [
('I love this sandwich.', 'pos'),
('This is an amazing place!', 'pos'),
('I feel very good about these beers.', 'pos'),
('I do not like this restaurant', 'neg'),
('kill', 'neg'),
("murder", 'neg'),
("terrorist", "neg")
]
cl = NaiveBayesClassifier(train)
print cl.classify("kill murder death suicide terrorist")

#g = TextBlob(data1, analyzer = NaiveBayesAnalyzer())
#print g.sentiment


cleanData= data.decode('utf-8')
test = TextBlob(cleanData, analyzer = NaiveBayesAnalyzer())

for s in test.sentences:
	s1=str(s)
	blob = TextBlob(s1, analyzer = NaiveBayesAnalyzer())
	print 's.classsssify', blob.sentiment
	test = TextBlob(s1)
	print 'naive bayes yields', test.sentiment
	print s


#print test.word_counts
print test.sentiment.polarity
print test.sentiment.subjectivity
#print "sentiment is- ",blob.sentiment

