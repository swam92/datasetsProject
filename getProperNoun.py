import os
import csv
dirListing = os.listdir('results/')  
name = []
properNounCount = []

for resultFile in dirListing:
	count = 0
	absolute = 'results/'+resultFile
	f = open(absolute, 'r')
	reader = csv.reader(f, delimiter='\n')
	totalLength = len(list(csv.reader(open(absolute))))
	for row in reader:
		if(count==0):
			temp = str(row)
			name.append(temp.split(".")[0])
		count = count + 1
		if(count == (totalLength-2)):
			properNounCount.append(row)