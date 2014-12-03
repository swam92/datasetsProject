import csv
import nltk
from nltk.tokenize import word_tokenize
from textblob import TextBlob
from textblob.classifiers import NaiveBayesClassifier
import pprint

words = []
words_red = []
#######################
#put titles from csv file into array 
#######################
for t in csv.DictReader(open('data/911truth.csv'), delimiter=','):
    words.extend(t['title'].lower().split()) # <-----------

#words_red = words[len(words)-800]

csv_text = nltk.Text(words)
#put any word here.  counts occureneces in text
print csv_text.count('government')


#######################
#put titles into one giant string
#######################
totalStr = ""
with open('data/TheWire.csv', 'rb') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		tempStr = str(row['title'])
		totalStr = totalStr + " " + tempStr
        words_red.append(row['title'])

print totalStr

word1 = []
word1 = words_red[:50]

#############################
#Determines part of speech for every word in the text! Below is the dictionary.
#############################
#CC- coordinating conjunction
#RB- adverbs
#IN- preposition
#NN- noun
#JJ- adjective
#ADJ- adjective
#ADP- adposition (preposition??)
#VBZ- verb!
###############################

tokenizer = None
tagger = None

def init_nltk():
    global tokenizer
    global tagger
    tokenizer = nltk.tokenize.RegexpTokenizer(r'\w+|[^\w\s]+')
    tagger = nltk.UnigramTagger(nltk.corpus.brown.tagged_sents())

def tag(text):
    global tokenizer
    global tagger
    if not tokenizer:
        init_nltk()
    tokenized = tokenizer.tokenize(text)
    tagged = tagger.tag(tokenized)
    tagged.sort(lambda x,y:cmp(x[1],y[1]))
    return tagged

def main():
	text = totalStr
	tagged = tag(text)    
	l = list(set(tagged))
	l.sort(lambda x,y:cmp(x[1],y[1]))
	pprint.pprint(l)


test = TextBlob("This is so cool")
print test.sentiment

if __name__ == '__main__':
    main()


#train = [('attack','neg'),('terrorist','neg'),('gun','neg'), ('innovate','pos')]
#cl = NaiveBayesClassifier(train)

#print cl.classify("I love dolphins so much!")
#print cl.accuracy("I love dolphins so much!")
