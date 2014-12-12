import csv
import nltk
from textblob import TextBlob
from textblob.classifiers import NaiveBayesClassifier
from textblob.sentiments import NaiveBayesAnalyzer
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

for t in csv.DictReader(open(csv_file), delimiter=','):
    count=count+1
    into = str(t['title'])
    into = into.decode('utf-8')
    blob = TextBlob(into, analyzer = NaiveBayesAnalyzer())
    #    print "positivity:",blob.sentiment.p_pos
    #    print "negativity:",blob.sentiment.p_neg
    
    pos = pos + blob.sentiment.p_pos
    neg = neg + blob.sentiment.p_neg
    test = TextBlob(into)
    if(test.sentiment.polarity != 0 or test.sentiment.subjectivity !=0 ):
        polar = polar + test.sentiment.polarity
        subj  = subj + test.sentiment.subjectivity
        #        print "subjectivity:", test.sentiment.subjectivity
        #        print "polarity:", test.sentiment.polarity
        countForSentiment = countForSentiment+1
        print (str(t['id'])+"\t"+str(test.sentiment.subjectivity)+"\t"+str(test.sentiment.polarity))
    #print test.sentiment.polarity
    #print test.sentiment.subjectivity
