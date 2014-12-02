import csv
import nltk

words = []

#######################
#put titles from csv file into array 
#######################
for t in csv.DictReader(open('data/911truth.csv'), delimiter=','):
    words.extend(t['title'].lower().split()) # <-----------

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

print totalStr
