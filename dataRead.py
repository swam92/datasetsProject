import csv
import nltk
from nltk.tokenize import word_tokenize
from textblob import TextBlob
from textblob.classifiers import NaiveBayesClassifier
from textblob.sentiments import NaiveBayesAnalyzer
import pprint
import sys

csv_file = sys.argv[1]
words = []
words_red = []
#######################
#put titles from csv file into array 
#######################

polar=0
subj=0
count=0
pos=0
neg=0
countForSentiment=0

print("CSV_FILE_NAME:"+csv_file)

for t in csv.DictReader(open(csv_file), delimiter=','):
    count=count+1
    into = str(t['title'])
    into = into.decode('utf-8')
    blob = TextBlob(into, analyzer = NaiveBayesAnalyzer())
    print "positivity:",blob.sentiment.p_pos
    print "negativity:",blob.sentiment.p_neg

    pos = pos + blob.sentiment.p_pos
    neg = neg + blob.sentiment.p_neg
    test = TextBlob(into)
    if(test.sentiment.polarity != 0 or test.sentiment.subjectivity !=0 ):
        polar = polar + test.sentiment.polarity
        subj  = subj + test.sentiment.subjectivity
        print "subjectivity:", test.sentiment.subjectivity
        print "polarity:", test.sentiment.polarity
        countForSentiment = countForSentiment+1
        print (str(t['id'])+"\t"+str(test.sentiment.subjectivity)+"\t"+str(test.sentiment.polarity))
    #print test.sentiment.polarity
    #print test.sentiment.subjectivity
    words.extend(t['title'].lower().split()) # <-----------


print '\nAGGREGATED SUBREDDIT INFORMATION IS BELOW\n'
polarTotal = polar / countForSentiment
subjTotal = subj / countForSentiment
negTotal = neg / count
posTotal = pos / count

print polarTotal, subjTotal, negTotal, posTotal

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
        print row['title']


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
    pnTagger = 0
    wordCount = 0
    global tokenizer
    global tagger
    if not tokenizer:
        init_nltk()
    tokenized = tokenizer.tokenize(text)
    tagged = tagger.tag(tokenized)
    for word, tag in tagger.tag(tokenized):
        wordCount = wordCount + 1
        if(tag == 'NP'):
            pnTagger = pnTagger + 1

    tagged.sort(lambda x,y:cmp(x[1],y[1]))
    print pnTagger, '\n'
    print wordCount

    return tagged


def main():
	text = totalStr
	tagged = tag(text)    
	l = list(set(tagged))
	l.sort(lambda x,y:cmp(x[1],y[1]))
	#pprint.pprint(l)



if __name__ == '__main__':
    main()



