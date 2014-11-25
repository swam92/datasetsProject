import csv
csvToArr = []
count = 0
current = str
with open('data/911truth.csv') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		current = row['title']
		if current.find("CIA") != -1:
			count=count+1
		print(current)
		csvToArr.append(row['title'])

print count