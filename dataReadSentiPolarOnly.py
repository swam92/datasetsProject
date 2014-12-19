import csv
import nltk
from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer
import os

for file in os.listdir("data"):
  for t in csv.DictReader(open('data/'+file,'r'), delimiter=','):
      into = str(t['title'])
      into = into.decode('utf-8')
      blob = TextBlob(into, analyzer = NaiveBayesAnalyzer())
      #    print "positivity:",blob.sentiment.p_pos
      #    print "negativity:",blob.sentiment.p_neg
      test = TextBlob(into)
      if(test.sentiment.polarity != 0 or test.sentiment.subjectivity !=0 ):
          #        print "subjectivity:", test.sentiment.subjectivity
          #        print "polarity:", test.sentiment.polarity
          print (str(t['id'])+"\t"+str(test.sentiment.subjectivity)+"\t"+str(test.sentiment.polarity))
      #print test.sentiment.polarity
      #print test.sentiment.subjectivity
