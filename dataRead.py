import csv
import nltk
from nltk.book import *

words = []

for t in csv.DictReader(open('data/911truth.csv'), delimiter=','):
    words.extend(t['title'].lower().split()) # <-----------


csv_text = nltk.Text(words)
z = str(csv_text)
s = unicode(z, "utf-8")
s.concordance('america')

print csv_text.count('government')


