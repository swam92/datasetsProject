import re
import csv
import nltk
from nltk.classify import*
import os
meaninglessWords = []
featureList = []

#normalize the post
def process(topRedditPost):
	topRedditPost = topRedditPost.lower()
	topRedditPost = re.sub('[\s]+', ' ', topRedditPost)
	return topRedditPost


def getMeaningless(wordList):
	noMeaning = []
	fp = open('meaninglessWords.txt', 'r')
	line = fp.readline()
	while line:
		word = line.strip()
		noMeaning.append(word)
		line = fp.readline()
	fp.close()
	return noMeaning

#start getfeatureVector
def feature(post, words):
	feature = []
	#split tweet into words
	words = post.split()
	for word in words:
		word = word.strip('\'"?,.')
		value = re.search(r"^[a-zA-Z][a-zA-Z0-9]*$", word)
		if(word in words or value is None):
			continue
		else:
			featureList.append(word.lower())
			feature.append(word.lower())

	return feature
#end

def feature_Modified(post):
	feature = []
	#split tweet into words
	words = post.split()
	for word in words:
		word = word.strip('\'"?,.')
		value = re.search(r"^[a-zA-Z][a-zA-Z0-9]*$", word)
		if(value is None or word in meaninglessWords):
			continue
		else:
			featureList.append(word.lower())
			feature.append(word.lower())

	return feature
#end

st = open('meaninglessWords.txt', 'r')
meaninglessWords = getMeaningless('meaninglessWords.txt')

trainers = csv.reader(open('trainer.csv', 'rb'), delimiter=',', quotechar='|')
predictors = []
for row in trainers:
	sentiment = row[0]
	toProcess = str(row[1])
	processedPost = process(toProcess)
	features = feature(processedPost, meaninglessWords)
	predictors.append((features,sentiment))


def extract_features(post):
	post_words = set(post)
	features = {}
	for word in featureList:
		print word
		features['contains(%s)' % word] = (word in post_words)
	return features

trainingSet = nltk.classify.util.apply_features(extract_features, predictors)
naivesBayes = nltk.NaiveBayesClassifier.train(trainingSet)

pos_count = 0
neg_count = 0
#######
#THIS IS WHERE THE CSV IS READ FROM SO WE SHOULD ITERATE FROM HERE

for t in csv.DictReader(open('data/911truth.csv'), delimiter=','):
#  print naivesBayes.show_most_informative_features(10)
	postToProcess = str(t['title'])
	postToProcess = postToProcess.decode('utf-8')
	postToProcess = process(postToProcess)
	result = naivesBayes.classify(extract_features(feature_Modified(postToProcess)))
	if(result == 'positive'):
		pos_count = pos_count+1
	else:
		neg_count = neg_count + 1

#for t in csv.DictReader(open(csv_file), delimiter=','):
#  print naivesBayes.show_most_informative_features(10)
for file in os.listdir("data"):
  source = open("data/"+file,'r')
  for t in csv.DictReader(source, delimiter=','):
    postToProcess = str(t['title'])
    postToProcess = postToProcess.decode('utf-8')
    result = naivesBayes.classify(extract_features(feature_Modified(postToProcess)))
    if(result == 'positive'):
      print (str(t['id'])+"\t1")
      pos_count = pos_count+1
    else:
      print (str(t['id'])+"\t0")
      neg_count = neg_count + 1
    #print naivesBayes.classify(extract_features(feature_Modified(postToProcess)))


#print pos_count, " ", neg_count
